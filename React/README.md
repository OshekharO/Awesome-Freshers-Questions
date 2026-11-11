# React Basics & Modern Concepts Cheat Sheet ⚛️📱

*Curated for freshers and junior frontend engineers with technical interview questions asked as of November 2026 (React 18 & React 19 standards).*

---

## Part 1: Core React Fundamentals

### What is React?
React is a declarative, component-based JavaScript library for building user interfaces. It maintains an in-memory Virtual DOM and calculates minimum required real DOM updates using a reconciliation algorithm (Fiber).

### JSX (JavaScript XML)
A syntax extension for JavaScript that allows writing HTML-like markup inside JS. Under the hood, JSX compiles into standard JavaScript function calls (`React.createElement` or JSX runtime `jsx()`).

### Components: Function vs Class
In modern React, **Function Components with Hooks** are the universal standard. Class components are legacy and largely avoided in modern codebases.

---

## Part 2: Essential React Hooks Overview 🪝

| Hook | Purpose | Common Interview Scenario |
|---|---|---|
| `useState` | Local component state | Managing inputs, toggles, counters |
| `useEffect` | Synchronize component with external systems / side effects | Data fetching, event listeners, timers |
| `useContext` | Read global context without prop drilling | Theme, user authentication, language locale |
| `useRef` | Persist mutable values without triggering re-render | DOM node references, storing previous timer IDs |
| `useReducer` | Complex state transitions via actions | Multi-step forms, cart management |
| `useMemo` | Cache result of expensive calculation | Filtering or sorting large arrays |
| `useCallback` | Cache function reference between re-renders | Passing callback props to memoized child components |
| `useDeferredValue` | Defer re-rendering a non-critical part of UI | Responsive typing in search while list filters |
| `useTransition` | Mark state update as non-blocking transition | Tab switching, large dataset transitions |

---

## Part 3: Technical Interview Questions & Multiple Solutions (React Freshers) 🎯

### Question 1: How do you handle State Management in a Counter with multiple actions (Increment, Decrement, Reset, Step)?

#### Logic & Background:
Tests understanding of React's asynchronous state updates, batching, and when to graduate from basic state to reducer architecture.

#### Method 1: `useState` with Functional State Updates (Standard)
- **Logic**: Use `setCount(prev => prev + step)` instead of `setCount(count + step)`.
- **Why**: React batches state updates. If multiple updates occur in rapid succession, using direct state reference (`count + 1`) uses a stale snapshot, leading to race conditions. Functional updates receive the guaranteed latest committed state.
- **When to use**: Simple components with 1 or 2 independent state variables.

#### Method 2: `useReducer` for Explicit Action Types (Complex / Scalable)
- **Logic**: Centralize state transitions inside a pure `reducer(state, action)` function and trigger changes via `dispatch({ type: 'INCREMENT' })`.
- **Why**: Decouples the logic of *how* state updates happen from the component UI rendering.
- **When to use**: When state contains multiple interdependent properties (e.g., `count`, `step`, `history`), or when next state depends on complex rules.

#### Method 3: Custom Hook (`useCounter`) for Logic Reusability
- **Logic**: Encapsulate `useState` and helper functions (`increment`, `decrement`, `reset`) inside a reusable function starting with `use`.
- **Why**: Promotes clean separation of concerns and allows sharing counter logic across multiple components without duplicating code.

---

### Question 2: How do you implement a Debounced Search Input to prevent excessive API calls while a user types?

#### Logic & Background:
Every keystroke in a search box should not fire an immediate network request. Debouncing delays the execution of a function until a specified time has passed since it was last called.

#### Method 1: Custom `useDebounce` Hook with `useEffect` and `setTimeout` (Standard Pattern)
- **Logic**:
  1. Store immediate typing value in a local `useState` (for an instant responsive input box).
  2. Pass this value into a custom `useDebounce(value, delay)` hook.
  3. Inside the hook's `useEffect`, initialize a `setTimeout` that sets the debounced state after e.g. 500ms.
  4. In the `useEffect` cleanup function, call `clearTimeout(timer)`. Every new keystroke resets the timer before it fires.
- **Pros**: Completely framework-agnostic, predictable, and works in all React versions.

#### Method 2: Modern React Concurrent Features (`useDeferredValue` / `useTransition`)
- **Logic**:
  - Keep the input controlled by high-priority `useState`.
  - Pass the query to `useDeferredValue(query)`.
  - React keeps the input immediately responsive while deferring the heavy re-render of the search results list in the background.
- **Pros**: Zero manual `setTimeout` management, no arbitrary millisecond guess; React dynamically pauses and renders as device CPU allows.

#### Method 3: `useCallback` with a Lodash/Utility Debounced Function
- **Logic**: Wrap an API caller function in `lodash.debounce` and memoize it using `useCallback(debounce(apiCall, 500), [])`.
- **Caveat**: Must properly clean up `debounced.cancel()` on unmount to avoid memory leaks.

---

### Question 3: How do you safely fetch API data in React without memory leaks or race conditions?

#### Logic & Background:
When a user navigates quickly between pages or switches dropdown items (e.g., User ID 1 -> User ID 2), network requests might return out of order (race condition), or complete after the component has unmounted.

#### Method 1: `useEffect` with Native `AbortController` (Industry Standard)
- **Logic**:
  1. Instantiate `const controller = new AbortController();` inside `useEffect`.
  2. Pass `{ signal: controller.signal }` to `fetch()`.
  3. Return a cleanup function: `return () => controller.abort();`.
  4. Catch `AbortError` in `.catch()` and ignore it safely.
- **Why**: Cancels in-flight browser network requests immediately when dependencies change or the component unmounts.

#### Method 2: Boolean Active/Ignore Flag Pattern
- **Logic**:
  1. Declare `let ignore = false;` inside `useEffect`.
  2. Before setting state in `.then()`, check `if (!ignore) setState(data);`.
  3. Return `() => { ignore = true; }` in the cleanup function.
- **Pros**: Very simple and works for non-fetch async operations (like third-party SDK promises that don't support `AbortSignal`).

#### Method 3: React Server Components & React 19 `use` Hook / Modern Data Libraries (TanStack Query)
- **Logic**: Avoid doing client-side data fetching inside `useEffect` altogether.
- **Modern approach**:
  - Use TanStack Query (React Query) which handles automatic caching, deduplication, retry, and cancellation out of the box.
  - In React 19 / Next.js: Fetch data directly on the server inside Server Components or use the React 19 `use(Promise)` hook with `<Suspense>`.

---

### Question 4: How do you implement CRUD operations in a List while adhering to state immutability?

#### Logic & Background:
In React, state should never be mutated directly (e.g. `todos.push(newTodo)` or `todo.completed = true`). React compares object references; mutating directly prevents re-renders and breaks time-travel debugging.

#### Method 1: Pure JavaScript Array Methods (`spread`, `map`, `filter`)
- **Add**: `setTodos(prev => [...prev, newItem])` (creates new array with spread).
- **Update / Toggle**: `setTodos(prev => prev.map(item => item.id === targetId ? { ...item, completed: !item.completed } : item))` (maps to new object references only for modified items).
- **Delete**: `setTodos(prev => prev.filter(item => item.id !== targetId))` (returns a new array without the target item).
- **Pros**: Clean, standard, built into JS without external dependencies.

#### Method 2: Centralized `useReducer`
- **Logic**: Dispatch distinct action types (`ADD_TODO`, `TOGGLE_TODO`, `DELETE_TODO`). State transformations remain pure functions.
- **Pros**: Easily testable in isolation without rendering UI.

#### Method 3: Using Immer Library (`produce`)
- **Logic**: Allows writing seemingly "mutative" syntax like `draft.push(newItem)` or `draft[i].completed = true` which Immer converts to an immutable copy under the hood.

---

*Created By Shekher Saksham Shashi (AMPICS)*
