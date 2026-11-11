# React Basics & Modern Concepts Cheat Sheet ⚛️📱

*Curated for freshers and junior frontend engineers with comprehensive technical interview questions asked as of November 2026 (React 18 & React 19 standards).*

---

## Part 1: Core React Fundamentals

### What is React?
React is a declarative, component-based JavaScript library for building user interfaces. It creates and updates UI efficiently using a Virtual DOM and a reconciliation algorithm (Fiber).

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
| `useActionState` | Modern React 19 form actions handling | Automatic pending state and server form submission |

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

### Question 2: How do you prevent Unnecessary Re-renders in React components?

#### Logic & Background:
A parent re-render causes all child components to re-render by default, even if their props have not changed. In heavy UI trees, this causes frame drops and sluggish interaction.

#### Method 1: `React.memo` (Memoizing Pure Child Components)
- **Logic**: Wrap child component in `React.memo(ChildComponent)`.
- **How it works**: Performs a shallow comparison (`Object.is`) of incoming props. If props are identical, skips re-rendering the child.
- **Requirement**: Pair with `useCallback` for function props and `useMemo` for non-primitive object/array props so references don't change every render.

#### Method 2: Component Architecture / Moving State Down
- **Logic**: Do not keep local state at a high parent level if only a tiny sub-component needs it.
- **Example**: If an input box or toggle only affects a small banner, encapsulate the state inside that specific banner component. The rest of the page won't re-render on typing.

#### Method 3: Passing Components as `children` or Props (Slot Pattern)
- **Logic**: Wrap expensive UI elements inside parent components using `{children}`.
- **Why**: When the wrapper component updates its own state, React recognizes that `children` props have not changed in reference and skips re-rendering them.

---

### Question 3: How do you resolve "Prop Drilling" in a large React application?

#### Logic & Background:
Prop drilling occurs when data needs to be passed down through several layers of intermediate components that don't need the data themselves just to reach a deeply nested child.

#### Method 1: React Context API (`createContext` & `useContext`)
- **Logic**: Provide data at a top-level provider and consume it anywhere down the tree via `useContext(MyContext)`.
- **Best for**: Low-frequency global state (Current user session, theme dark/light, internationalization locale).
- **Caveat**: Every component reading the context re-renders whenever any value in that context object changes.

#### Method 2: Component Composition (Inversion of Control)
- **Logic**: Instead of passing props down 5 levels so `<GrandChild user={user} />` can be rendered, render the grandchild at the top level and pass it as a JSX prop: `<Parent middle={<GrandChild user={user} />} />`.
- **Best for**: Clean architecture without external dependencies.

#### Method 3: External State Management (Zustand, Redux Toolkit)
- **Logic**: Decouple state outside of the React component tree into a central store with selective subscriptions (`useStore(state => state.user)`).
- **Benefit**: Only components subscribed to specific slice of state re-render.

---

### Question 4: How do you implement a Debounced Search Input to prevent excessive API calls while a user types?

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

### Question 5: How do you safely fetch API data in React without memory leaks or race conditions?

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

#### Method 3: Modern Data Libraries (TanStack Query) & React 19 `use` Hook
- **Logic**: Avoid doing client-side data fetching inside `useEffect` altogether.
- **Modern approach**:
  - Use TanStack Query (React Query) which handles automatic caching, deduplication, retry, and cancellation out of the box.
  - In React 19: Use Server Components or the `use(Promise)` hook with `<Suspense>`.

---

### Question 6: Controlled vs Uncontrolled Components in React: What is the difference and how does React 19 Form Actions change it?

#### Logic & Background:
Handling form inputs is one of the most core tasks in frontend applications.

#### Method 1: Controlled Components (React State as Single Source of Truth)
- Input value is bound to state: `value={state}` with `onChange={(e) => setState(e.target.value)}`.
- *Pros*: Instant validation, conditional disabling of submit buttons, formatting inputs on the fly (e.g. credit card mask).
- *Cons*: Re-renders the component on every single keystroke.

#### Method 2: Uncontrolled Components (`useRef` / Native DOM)
- Input value is stored directly in the DOM; React reads it only when needed (e.g. form submission): `const inputRef = useRef();`.
- *Pros*: High performance, zero re-renders while user types.
- *Cons*: Difficult to implement real-time validation feedback.

#### Method 3: Modern React 19 Form Actions & `useActionState`
- React 19 embraces native HTML forms with server/client Actions: `<form action={formAction}>`.
- The `useActionState(asyncAction, initialState)` hook provides `[state, formAction, isPending]`, automatically handling pending spinners, submission states, and optimistic updates without manually managing input states.

---

### Question 7: Why is the `key` prop essential in lists, and why is using the array index as a key considered an anti-pattern?

#### Logic & Background:
React uses the `key` prop during reconciliation (Fiber diffing) to match elements in the previous tree with elements in the next tree.

#### The Issue with Index as Key:
- If items are added, removed, or sorted, the index of items shifts.
- React matches nodes by key: if item at index 0 is deleted, the old item 1 becomes index 0. React believes index 0 was updated rather than deleted, causing component state (like checked checkboxes or input text) to persist on the wrong item.

#### Correct Solutions:
- **Unique Database ID**: Always use stable, unique IDs (e.g. `todo.id` or `uuid`).
- **Natural Composite Key**: If no ID exists, combine unique fields: `${item.title}-${item.createdAt}`.

---

### Question 8: How do Error Boundaries work in React, and can they catch errors in asynchronous code?

#### Logic & Background:
Uncaught JavaScript errors inside component rendering crash the entire React application tree, presenting a blank white screen to users.

#### How Error Boundaries Work:
- Components that implement `static getDerivedStateFromError()` and `componentDidCatch()`.
- Wraps child component trees: if a rendering error occurs, it displays a fallback UI instead of crashing the app.

#### Limitations (What Error Boundaries CANNOT Catch):
- Event handlers (e.g. `onClick={() => { throw new Error(); }}`) - Use standard `try/catch` here instead.
- Asynchronous code (`setTimeout`, `requestAnimationFrame`, `async/await` inside `useEffect`).
- Server-side rendering (SSR) errors.

---

*Created By Shekher Saksham Shashi (AMPICS)*
