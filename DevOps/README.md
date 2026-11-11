# DevOps & Cloud Infrastructure Cheat Sheet 🚀☁️

*Curated for freshers and entry-level DevOps / Cloud Platform engineers with technical interview questions asked as of November 2026.*

---

## Part 1: DevOps Core Fundamentals

### What is DevOps?
DevOps is a set of cultural philosophies, practices, and automated tools that merges Software Development (`Dev`) and IT Operations (`Ops`) to increase an organization's velocity and software delivery reliability.

### Key Pillars
- **CI/CD**: Continuous Integration and Continuous Deployment/Delivery
- **IaC**: Infrastructure as Code (e.g. Terraform, OpenTofu, Ansible)
- **Containerization & Orchestration**: Docker, Podman, Kubernetes
- **Observability**: Metrics, Logs, Traces (Prometheus, Grafana, OpenTelemetry, ELK)
- **Cloud Infrastructure**: AWS, Azure, GCP, Render, Neon, Cloudflare

---

## Part 2: Linux & Networking for DevOps 🐧

### Must-Know Diagnostic Commands
```bash
# System Resources
top / htop               # Real-time process & CPU/memory monitor
free -m                  # RAM usage in megabytes
df -h                    # Disk filesystem capacity
du -sh /var/log/*        # Folder disk space usage
vmstat 1 5               # Virtual memory and I/O wait statistics

# Networking & Ports
ss -tulpn                # Socket statistics (modern replacement for netstat)
curl -Iv https://api.com # Inspect HTTP headers, TLS handshake & latency
ping -c 4 8.8.8.8        # Test basic ICMP reachability
traceroute / mtr         # Identify packet drops across network hops
dig +short A example.com # DNS resolution check
nc -zv 10.0.0.1 5432     # Test TCP port reachability
```

---

## Part 3: Technical Interview Questions & Multiple Solutions (DevOps Freshers) 🎯

### Question 1: How do you clean up unused Docker containers, dangling images, and volumes when host disk space is running out?

#### Logic & Background:
During continuous CI/CD runs and local development, old stopped containers, untagged (`<none>`) image layers, and orphaned volumes accumulate, consuming gigabytes of disk and causing "no space left on device" errors.

#### Method 1: Docker Native Prune Commands (Standard & Safe)
- **Logic**: Use Docker's built-in garbage collection commands.
- **Commands**:
  ```bash
  docker container prune -f       # Removes all stopped containers
  docker image prune -f           # Removes dangling (untagged) images
  docker volume prune -f          # Removes anonymous unused volumes
  docker system prune -af --volumes # Comprehensive clean: stopped containers, all unused images, networks, volumes
  ```
- **Pros**: Safe, official, cleans internal Docker metadata atomically.

#### Method 2: Shell Script Filtering with Pipes / xargs (Custom Criteria)
- **Logic**: Query Docker IDs using `--filter` or formatted output and pipe to removal commands.
- **Commands**:
  ```bash
  # Remove exited or dead containers
  docker ps -a --filter "status=exited" -q | xargs -r docker rm

  # Remove dangling images
  docker images -f "dangling=true" -q | xargs -r docker rmi
  ```
- **Pros**: Allows flexible custom shell scripting and integration with cron jobs.

#### Method 3: Retention-Based Cleanup (Age-Based Thresholds)
- **Logic**: Clean items that have not been touched for a given duration (e.g. older than 24 hours or 7 days).
- **Commands**:
  ```bash
  docker container prune --filter "until=24h" -f
  docker image prune -a --filter "until=168h" -f
  ```
- **Pros**: Prevents removing recently stopped containers that may still be needed for debugging.

---

### Question 2: A CI/CD deployment fails with a 502 Bad Gateway / application crash after rolling out a new release. How do you troubleshoot and fix it?

#### Logic & Background:
A 502 Bad Gateway indicates that the reverse proxy (e.g. Nginx, Ingress, AWS ALB) cannot establish a connection or receive a valid response from the backend application process.

#### Method 1: Immediate Rollback First, Then Post-Mortem (MTTR Prioritization)
- **Logic**: Minimize downtime for active users immediately before digging into root cause.
- **Actions**:
  - In Kubernetes: `kubectl rollout undo deployment/<app-name>`
  - In GitHub Actions / Git: Re-deploy the last known successful Git commit hash or Docker tag.
  - In Cloud Providers (Render/AWS): Revert to the prior deployment release in one click or CLI command.
- **Pros**: Restores business availability immediately (lowest Mean Time To Recovery).

#### Method 2: Diagnostic Triage via Pod / Container Lifecycle Inspection
- **Logic**: Identify if the failure is a crash loop, missing environment variable, port mismatch, or failed health check.
- **Steps**:
  1. Check container state: `kubectl get pods` (Look for `CrashLoopBackOff`, `OOMKilled`, or `Error`).
  2. Inspect exit events: `kubectl describe pod <pod-name>` (Check Exit Code: 137 = Out of Memory, 1 = unhandled runtime exception).
  3. Stream container application logs: `kubectl logs <pod-name> --previous` (shows logs right before container exited).
  4. Verify environment variables and secret injection.

#### Method 3: Health Check & Port Configuration Verification
- **Logic**: The application may be running fine, but the container port does not match the reverse proxy upstream target, or readiness probes fail prematurely.
- **Steps**:
  - Check whether the application server is listening on `0.0.0.0` rather than `127.0.0.1` inside the container.
  - Review readiness/liveness probe thresholds: increase `initialDelaySeconds` if the application takes longer to start up (e.g. database schema migrations on boot).

---

### Question 3: What are the primary zero-downtime deployment strategies, and when should you choose each?

#### Logic & Background:
Modern cloud environments require deploying new code versions continuously without dropping user requests or showing maintenance screens.

#### Method 1: Rolling Deployment (Incremental Replacement)
- **Logic**: Gradually replaces instances of the previous version with instances of the new version one by one or in batches.
- **How it works**: Kubernetes deployment default (`maxSurge: 25%`, `maxUnavailable: 25%`). Once new pods pass readiness checks, old pods are terminated.
- **Pros**: Minimal extra resource consumption; automated out-of-the-box.
- **Cons**: Version N and N+1 co-exist temporarily; database schemas must support backward compatibility.

#### Method 2: Blue-Green Deployment (Environment Swap)
- **Logic**: Maintain two identical production environments: Blue (active production) and Green (new release staging).
- **How it works**: Deploy and test new release in Green. Once verified, switch the load balancer / DNS target from Blue to Green instantly.
- **Pros**: Instant switchover; immediate rollback if unexpected errors occur (just switch traffic back to Blue).
- **Cons**: Requires doubling compute resources during release windows.

#### Method 3: Canary Deployment (Traffic Splitting)
- **Logic**: Route a tiny percentage of live user traffic (e.g., 5%) to the new release while 95% remains on the stable version.
- **How it works**: Monitor latency, error rates, and metrics via Prometheus/Datadog. If error rates remain flat, gradually scale up to 100%.
- **Pros**: Catches bugs with minimal blast radius affecting only a few users.
- **Cons**: Requires sophisticated routing/service mesh (Istio, Envoy, AWS ALB weighted target groups).

---

### Question 4: How do you extract and count HTTP 4xx/5xx status codes from web server / API access logs to identify attacks or outages?

#### Logic & Background:
Log analysis is a fundamental operational skill to quickly detect brute force attacks, broken endpoints, or database timeouts.

#### Method 1: Linux CLI Command Line (awk, grep, sort, uniq)
- **Logic**: Process text streams through UNIX pipes without installing additional software.
- **Command**:
  ```bash
  cat access.log | awk '$9 >= 400 {print $9, $7}' | sort | uniq -c | sort -nr | head -n 10
  ```
- **Explanation**: Column 9 is typically HTTP status, column 7 is the request URI. Counts occurrences and sorts from highest frequency.

#### Method 2: Python Script with Regular Expressions & Collections
- **Logic**: Parse structured log entries with regex, aggregate counts with `collections.Counter`, and output JSON/reports.
- **Approach**: Read line-by-line using a generator to prevent memory overflow on large multi-gigabyte log files.

#### Method 3: Centralized Log Querying (Loki / LogQL or ELK)
- **Logic**: Use distributed log aggregators in production environments.
- **LogQL Expression**:
  ```logql
  {app="web-server"} | json | status >= 400 | count_over_time([5m])
  ```

---

*Created By Shekher Saksham Shashi (AMPICS)*
