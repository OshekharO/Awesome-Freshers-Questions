# Web Development & JavaScript Cheat Sheet 🌐⚡

*Curated for freshers and junior web developers with comprehensive technical interview questions asked as of November 2026 (ES2024+, Modern Web APIs, Event Loop, CSS Layouts, Web Security, Performance).*

---

## Part 1: Core Web Fundamentals

### The Critical Rendering Path
1. **DOM (Document Object Model)**: Parsed from HTML tokens into a node tree.
2. **CSSOM (CSS Object Model)**: Parsed from CSS rules into a style tree.
3. **Render Tree**: Combines visible DOM elements with CSSOM styles (ignoring `display: none` and `<head>`).
4. **Layout (Reflow)**: Computes exact geometry and screen coordinates for each visible node.
5. **Paint**: Fills pixels on screen (colors, borders, text, shadows).
6. **Composite**: Assembles layered elements via GPU acceleration (`transform`, `opacity`).

### JavaScript Runtime & The Event Loop
- **Call Stack**: Executes synchronous code (LIFO).
- **Web APIs**: Browser background threads handling asynchronous timers, fetch requests, DOM events.
- **Microtask Queue**: `Promise.then/catch/finally`, `queueMicrotask()`, `MutationObserver`.
- **Task / Macrotask Queue**: `setTimeout`, `setInterval`, `setImmediate`, I/O.
- **Priority Rule**: The Event Loop empties the entire Microtask Queue *immediately after* the current stack frame empties, *before* executing the next macrotask or rendering the screen.

---

## Part 2: Technical Interview Questions & Multiple Solutions (Web Development Freshers) 🎯

### Question 1: How do you Deep Clone an object with nested structures in JavaScript?

#### Logic & Background:
Shallow cloning (like `{ ...obj }` or `Object.assign({}, obj)`) only copies top-level references. Mutating a nested object or array modifies the original source, creating subtle bugs.

#### Method 1: Modern Native `structuredClone()` (ES2022+ Standard)
- **Logic**: Use the browser and Node.js built-in global function `structuredClone(obj)`.
- **How it works**: Deep copies cyclic references, `Date`, `RegExp`, `Map`, `Set`, `ArrayBuffer`, and nested plain objects.
- **Limitation**: Cannot clone functions or DOM nodes (throws `DataCloneError`).
- **Verdict**: The standard answer in 2026 interviews for production JavaScript.

#### Method 2: `JSON.parse(JSON.stringify(obj))` (Legacy Quick Hack)
- **Logic**: Serialize object to JSON string and parse back into a brand new memory reference.
- **Limitations**:
  - Drops `undefined`, functions, and `Symbol` keys.
  - Converts `Date` objects to ISO strings.
  - Converts `NaN` and `Infinity` to `null`.
  - Throws error on circular references.
- **When to mention**: Good to show you know both the historical approach and its exact pitfalls.

#### Method 3: Recursive Traversal Function
- **Logic**: Inspect whether each property is a primitive or an object. If object/array, recursively instantiate and copy keys; maintain a `WeakMap` to handle circular references.
- **Why interviewers ask**: Demonstrates recursion, data type checking (`typeof`, `Array.isArray`), and handling memory references.

---

### Question 2: What is Event Delegation and how does it leverage Event Bubbling and Capturing?

#### Logic & Background:
When a web page has hundreds or thousands of clickable list items (e.g. an e-commerce catalog or chat list), attaching an event listener to every single item degrades memory performance and fails for dynamically added items.

#### The Three Phases of DOM Events:
1. **Capturing Phase**: The event travels down from `window` through the DOM hierarchy to the target element.
2. **Target Phase**: The event reaches the actual element clicked.
3. **Bubbling Phase**: The event bubbles up from the target element back up to `window`.

#### Event Delegation Logic:
- Attach **one single event listener** to the parent container element (`<ul>` or `<table>`).
- In the handler, check `event.target` (the actual clicked element) or `event.target.closest('.item-btn')`.
- Read custom dataset attributes (`event.target.dataset.id`) to execute the action.
- **Benefits**:
  - Eliminates thousands of event listener allocations.
  - Automatically works for newly added DOM elements without re-attaching listeners.

---

### Question 3: What is the difference between Debounce and Throttle, and how do you implement them?

#### Logic & Background:
Both limit the rate at which a function executes, but for different user experience needs.

#### Concept Comparison:
- **Debounce**: "Wait until the user stops doing this for X milliseconds." (e.g. search autocomplete, window resize finish).
- **Throttle**: "Execute at most once every X milliseconds while the user continues doing this." (e.g. scroll position tracking, game firing, infinite scroll threshold).

#### Debounce Implementation Logic:
1. Store a `timer` variable in a closure.
2. Return a wrapper function that accepts arguments.
3. Every time the wrapper is called, call `clearTimeout(timer)`.
4. Re-assign `timer = setTimeout(() => fn.apply(this, args), delay)`.

#### Throttle Implementation Logic:
- **Approach A (Timer-based flag)**: Maintain a boolean `isThrottled`. If false, execute `fn`, set `isThrottled = true`, and set a timeout to reset `isThrottled = false` after delay.
- **Approach B (Timestamp-based)**: Track `lastRan = 0`. On each call, check if `Date.now() - lastRan >= limit`. If yes, execute `fn` and update `lastRan = Date.now()`.

---

### Question 4: How do JavaScript Closures work, and what are practical use cases and memory leak risks?

#### Logic & Background:
A closure is the combination of a function bundled together with references to its surrounding lexical environment. In JavaScript, inner functions always have access to variables in their outer enclosing scope, even after the outer function has returned.

#### Practical Use Cases:
1. **Data Privacy / Encapsulation**: Emulating private variables before ES private fields `#`:
   ```javascript
   function createCounter() {
     let count = 0; // Private to closure
     return {
       increment: () => ++count,
       get: () => count
     };
   }
   ```
2. **Function Currying / Partial Application**: Pre-configuring arguments (e.g. logging formats, discount multipliers).
3. **Event Handlers & Callback Timers**: Maintaining state references inside async handlers.

#### Memory Leak Risks & Mitigation:
- If an unused outer variable is captured in a long-lived closure (e.g. attached to `window` or a global DOM event listener), the garbage collector cannot free the memory.
- *Mitigation*: Nullify references (`ref = null`) or properly remove event listeners on component cleanup.

---

### Question 5: Compare Promise Combinators: `Promise.all()`, `Promise.allSettled()`, `Promise.race()`, and `Promise.any()`.

#### Logic & Background:
Handling multiple asynchronous operations concurrently is a frequent interview topic.

| Combinator | Resolves When... | Rejects When... | Ideal Use Case |
|---|---|---|---|
| `Promise.all([p1, p2])` | **All** promises resolve (returns array of results) | **Any single** promise rejects (fails fast) | Fetching interdependent resources where all are strictly required |
| `Promise.allSettled([p1, p2])` | **All** promises either resolve or reject | **Never** rejects (returns status and value/reason for each) | Batch operations (e.g., uploading 10 files; show which succeeded and which failed) |
| `Promise.race([p1, p2])` | The **very first** promise settles (resolves OR rejects) | Whichever settles first rejects | Setting an API network request timeout promise |
| `Promise.any([p1, p2])` | The **first successful** promise resolves | **All** promises reject (returns `AggregateError`) | Querying redundant CDN mirrors for fastest response |

---

### Question 6: What are XSS, CSRF, and CORS, and how do you protect web applications against them?

#### Logic & Background:
Web security knowledge separates junior developers who only write UI from engineers who build production-ready applications.

#### 1. Cross-Site Scripting (XSS)
- **Attack**: Attacker injects malicious JavaScript into a web page viewed by other users (stealing session tokens or cookies).
- **Defense**:
  - Always sanitize and escape user input before rendering into HTML.
  - Use modern frameworks (React/Vue) that automatically escape content by default (avoid `dangerouslySetInnerHTML`).
  - Set `HttpOnly` and `SameSite=Strict` flags on authentication cookies so JavaScript cannot read them.
  - Implement a strong **Content Security Policy (CSP)** HTTP header.

#### 2. Cross-Site Request Forgery (CSRF)
- **Attack**: Malicious third-party website tricks an authenticated user's browser into submitting unauthorized requests to your API.
- **Defense**:
  - Set `SameSite=Lax` or `SameSite=Strict` on cookies.
  - Implement Anti-CSRF tokens (Synchronizer Token pattern) in mutating POST/PUT/DELETE requests.
  - Check origin and referer headers on server endpoints.

#### 3. Cross-Origin Resource Sharing (CORS)
- **Concept**: A browser security mechanism that restricts cross-origin HTTP requests initiated by scripts.
- **Resolution**: CORS is configured **on the server**, not in client code. The server must return appropriate `Access-Control-Allow-Origin`, `Access-Control-Allow-Methods`, and `Access-Control-Allow-Headers` response headers.

---

### Question 7: How do you optimize Web Performance and Core Web Vitals (LCP, INP, CLS)?

#### Logic & Background:
Google ranks search performance and users abandon sluggish pages based on Core Web Vitals metrics.

#### The Three Core Web Vitals:
1. **LCP (Largest Contentful Paint)**: Measures perceived loading speed (target: < 2.5s).
   - *Optimization*: Preload hero images (`<link rel="preload">`), use modern WebP/AVIF formats, optimize Server Response Time (TTFB), employ CDN caching.
2. **INP (Interaction to Next Paint)**: Measures page responsiveness to user input (target: < 200ms; replaced FID in 2024+).
   - *Optimization*: Break up long-running JavaScript tasks using `scheduler.yield()` or `setTimeout`, offload CPU-heavy math to Web Workers.
3. **CLS (Cumulative Layout Shift)**: Measures visual layout stability (target: < 0.1).
   - *Optimization*: Always include explicit `width` and `height` attributes on images and video embeds; reserve space for dynamic ads/banners with CSS aspect-ratio.

---

### Question 8: Client Storage Comparison: LocalStorage vs SessionStorage vs Cookies vs IndexedDB

| Storage Type | Capacity | Lifetime | Server Accessible | Best Use Case |
|---|---|---|---|---|
| **LocalStorage** | ~5-10 MB | Persistent until manually cleared | No (Client only) | User UI preferences (Dark mode, draft form saves) |
| **SessionStorage** | ~5 MB | Tab lifetime (cleared on close) | No (Client only) | Single-tab checkout wizard or temporary form steps |
| **Cookies** | ~4 KB | Configurable via `Expires` / `Max-Age` | Yes (sent with every HTTP request) | Secure authentication tokens (`HttpOnly; Secure; SameSite=Strict`) |
| **IndexedDB** | > 250 MB (GBs) | Persistent | No (Client only) | Offline caching, PWA datasets, complex object stores |

---

*Created By Shekher Saksham Shashi (AMPICS)*
