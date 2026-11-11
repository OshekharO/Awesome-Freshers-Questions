# DevOps & Cloud Infrastructure Cheat Sheet 🚀☁️

*Curated for freshers and entry-level DevOps / Cloud Platform engineers with comprehensive technical interview questions asked as of November 2026.*

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

## Part 2: Linux & Networking Diagnostics Cheat Sheet 🐧

```bash
# System Resources
top / htop               # Real-time process & CPU/memory monitor
free -m                  # RAM usage in megabytes
df -h                    # Disk filesystem capacity
du -sh /var/log/*        # Folder disk space usage
vmstat 1 5               # Virtual memory and I/O wait statistics
iostat -xz 1 5           # Disk I/O bottlenecks and queue length

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
  docker container prune -f         # Removes all stopped containers
  docker image prune -f             # Removes dangling (untagged) images
  docker volume prune -f            # Removes anonymous unused volumes
  docker system prune -af --volumes # Comprehensive clean: stopped containers, all unused images, networks, volumes
  ```
- **Pros**: Safe, official, cleans internal Docker metadata atomically.

#### Method 2: Shell Script Filtering with Pipes / xargs (Custom Criteria)
- **Logic**: Query Docker IDs using `--filter` or formatted output and pipe to removal commands.
- **Commands**:
  ```bash
  docker ps -a --filter "status=exited" -q | xargs -r docker rm
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

### Question 2: A Kubernetes Pod is stuck in `CrashLoopBackOff`, `ImagePullBackOff`, `Pending`, or `OOMKilled`. How do you diagnose and resolve each?

#### Logic & Background:
Pod lifecycle issues are the #1 most frequently asked Kubernetes interview topic for freshers. Each state indicates a distinct root failure.

#### Method 1: Root Cause Matrix & Diagnostic CLI Steps
- **CrashLoopBackOff**: Container starts, fails, crashes, and Kubernetes backs off restarting it.
  - *Diagnosis*: Check exit code: `kubectl describe pod <pod>` and view prior crash logs: `kubectl logs <pod> --previous`.
  - *Fix*: Check application unhandled exceptions, missing required environment variables, or failure to connect to database on startup.
- **ImagePullBackOff / ErrImagePull**: Kubelet cannot download the container image.
  - *Diagnosis*: `kubectl describe pod <pod>` (Events section).
  - *Fix*: Verify image tag spelling, check if image exists in registry, verify `imagePullSecrets` for private repositories.
- **Pending**: Scheduler cannot place the Pod onto any worker node.
  - *Diagnosis*: `kubectl describe pod <pod>` (Events section).
  - *Fix*: Insufficient CPU/Memory resources on nodes (scale cluster or lower Pod resource `requests`), node tainted without matching toleration, or node selector mismatch.
- **OOMKilled (Exit Code 137)**: Linux kernel killed container because memory exceeded cgroup `limits`.
  - *Diagnosis*: `kubectl describe pod <pod>` shows `Last State: Terminated, Reason: OOMKilled, Exit Code: 137`.
  - *Fix*: Increase memory limits in deployment YAML (`resources.limits.memory`) or fix memory leaks in code.

#### Method 2: Interactive Debugging via Ephemeral Container
- **Logic**: If the container has no shell tools (e.g., distroless or scratch base image), attach a debug container to inspect network and filesystem:
  ```bash
  kubectl debug -it <pod-name> --image=busybox:1.36 --target=<container-name>
  ```

---

### Question 3: A Linux production server is experiencing 100% CPU utilization. How do you troubleshoot and identify the offending process?

#### Logic & Background:
Tests system administration fundamentals, resource monitoring, and Linux process management.

#### Method 1: Interactive Top / Htop Triage
- Run `htop` or `top`.
- Press `P` (in `top`) to sort processes by CPU usage (%CPU).
- Note down the `PID`, user, and process command.

#### Method 2: Non-Interactive CLI Querying
- Find top 5 CPU-consuming processes instantly:
  ```bash
  ps -eo pid,ppid,user,%cpu,%mem,cmd --sort=-%cpu | head -n 6
  ```
- Inspect thread-level utilization:
  ```bash
  top -H -p <PID>     # Inspect thread activity inside process
  pidstat -u 1 5      # CPU statistics per process over 5 seconds
  ```

#### Method 3: Remediation Actions
- **Graceful Termination**: `kill -15 <PID>` (SIGTERM allows process to complete write operations).
- **Force Termination (if frozen)**: `kill -9 <PID>` (SIGKILL).
- **CPU Throttling**: Lower process priority using `renice +10 -p <PID>` or enforce CPU quotas using systemd cgroups (`CPUQuota=50%`).

---

### Question 4: A CI/CD deployment fails with a 502 Bad Gateway after rolling out a new release. How do you troubleshoot and fix it?

#### Logic & Background:
A 502 Bad Gateway indicates that the reverse proxy (Nginx, Ingress, ALB) cannot connect to or receive a valid response from the backend application process.

#### Method 1: Immediate Rollback First (MTTR Prioritization)
- Restore availability for users immediately before investigating root cause.
- Kubernetes: `kubectl rollout undo deployment/<app-name>`
- Git/CI: Re-deploy the last known stable Docker image tag or commit hash.

#### Method 2: Application Process & Port Audit
- Verify the backend app is running: `systemctl status <service>` or `docker ps`.
- Check listening port and interface binding: `ss -tulpn | grep <port>`. Ensure application listens on `0.0.0.0` (all interfaces) and NOT just `127.0.0.1` inside a container.

#### Method 3: Reverse Proxy Upstream & Timeout Configuration
- Inspect Nginx error log: `tail -f /var/log/nginx/error.log` (Look for `Connection refused` or `upstream prematurely closed connection`).
- Adjust `proxy_read_timeout` and `proxy_connect_timeout` if the application performs long-running initial migrations.

---

### Question 5: What are the primary zero-downtime deployment strategies, and when should you choose each?

#### Solution Breakdown:
- **Rolling Deployment**:
  - *Logic*: Incrementally replaces old pods with new pods.
  - *Pros*: Built-in default in Kubernetes; no extra infrastructure costs.
  - *Cons*: Old and new versions run concurrently; requires backward-compatible database schemas.
- **Blue-Green Deployment**:
  - *Logic*: Two identical environments (Blue = live, Green = new). Route 100% traffic to Green once verified.
  - *Pros*: Instant switchover and instant 1-click rollback.
  - *Cons*: Doubles infrastructure cost during releases.
- **Canary Deployment**:
  - *Logic*: Send 5% traffic to new version, monitor error rates and latency via Prometheus/Datadog, gradually scale up to 100%.
  - *Pros*: Minimizes blast radius of critical production bugs.
  - *Cons*: Requires advanced traffic ingress routing (Istio, Linkerd, AWS ALB weighted routing).

---

### Question 6: How do you secure a CI/CD pipeline and scan container images for security vulnerabilities?

#### Logic & Background:
DevSecOps is a key requirement in modern engineering to prevent supply chain attacks and CVE exploits.

#### Method 1: Automated Container Image Vulnerability Scanning in CI
- Integrate static vulnerability scanners into the build stage:
  - **Trivy**: `trivy image --severity HIGH,CRITICAL myapp:latest`
  - **Grype**: `grype myapp:latest --fail-on medium`
  - **Docker Scout**: `docker scout cves myapp:latest`
- Fail the pipeline build if vulnerabilities exceeding threshold are detected.

#### Method 2: Shift-Left Secret Scanning & SAST
- **Secret Scanning**: Use tools like `Gitleaks` or `TruffleHog` as pre-commit hooks and CI gates to prevent committing API keys, tokens, or private keys.
- **Static Application Security Testing (SAST)**: Run SonarQube, Semgrep, or CodeQL on source code.

#### Method 3: Container Hardening Best Practices
- Use minimal distroless or alpine base images (`FROM node:20-alpine` or `gcr.io/distroless/nodejs20-debian12`).
- Never run containers as root: specify `USER nonroot` or `USER 1000:1000`.
- Mark container root filesystem read-only: `readOnlyRootFilesystem: true`.

---

### Question 7: How do you detect and resolve Infrastructure as Code (IaC) drift in Terraform?

#### Logic & Background:
Drift occurs when someone makes manual changes in the cloud console (e.g. AWS console, Azure portal) that bypass the Terraform code repository.

#### Method 1: `terraform plan -refresh-only` (Native Terraform Reconciliation)
- Compares real-world infrastructure state with the state file without proposing code changes.
- Shows exactly what drifted outside of code.
- Run `terraform apply -refresh-only` to sync state with reality.

#### Method 2: Scheduled Drift Detection in CI/CD
- Run a daily or weekly cron job in GitHub Actions / GitLab CI executing `terraform plan -detailed-exitcode`.
- Exit code 0 = No changes, Exit code 2 = Drift detected (triggers Slack / PagerDuty alert to the DevOps team).

#### Method 3: Dedicated Drift Scanning Tools
- Use specialized open-source tools such as `driftctl` to identify unmanaged and modified cloud resources across AWS/GCP/Azure.

---

### Question 8: How do you resolve a Git merge conflict during a rebase vs a merge?

#### Logic & Background:
Tests practical collaborative version control knowledge and Git internal behavior.

#### Method 1: Resolving Conflicts During `git merge`
- Command: `git merge feature-branch`
- When conflict occurs:
  1. Check conflicting files: `git status`.
  2. Open files and resolve conflict markers (`<<<<<<< HEAD`, `=======`, `>>>>>>>`).
  3. Stage resolved files: `git add <file>`.
  4. Finalize merge commit: `git commit -m "Merge and resolve conflicts"`.

#### Method 2: Resolving Conflicts During `git rebase`
- Command: `git checkout feature-branch && git rebase main`
- When conflict occurs:
  1. Fix conflict in file.
  2. Stage: `git add <file>`.
  3. Continue rebase: `git rebase --continue` (do NOT run git commit).
  4. If rebase needs to be abandoned: `git rebase --abort`.

---

*Created By Shekher Saksham Shashi (AMPICS)*
