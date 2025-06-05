---
title: Managing modal state with JavaScript
videoId: SuqU904ZHA4
---

From: [[fireship]] <br/> 

Animations can transform a basic feature into something special, and this includes managing the state of a modal window in React <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. In a beginner-friendly tutorial, one can learn how to [[styling_a_modal_with_css | style a modal with CSS]], then how to manage its open and closed state with [[javascript_fundamentals_and_practical_concepts | JavaScript]], and how to implement declarative animations with Framer Motion and React <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## Modal Components and State
A typical modal setup involves two primary components:
*   **Backdrop**: An overlay that darkens the entire screen <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. This component can be designed as a "dump component" that doesn't manage its own internal state, instead relying on props to update global state, such as an `onClick` handler <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   **Modal Window**: Sits atop the backdrop, focusing the user's attention <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

Modals are a useful UI feature for focusing a user's attention or when navigation to a different route is undesirable <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. They can handle complex interactions, such as an entire login feature <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Implementing State Management in React
To manage the open and closed state of a modal in a React application, the `useState` hook from React is utilized <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

### State Initialization
The `useState` hook is used in the root `App` component to track whether the modal is currently open or closed <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
```javascript
const [modalOpen, setModalOpen] = useState(false); // Default value is false (closed) <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>
```

### Toggling Modal State
For readability, functions can be set up to toggle the `modalOpen` state between `true` and `false` <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>:
```javascript
const close = () => setModalOpen(false);
const open = () => setModalOpen(true);
```

The modal's state can be toggled from different interactions:
*   **Launch Button**: An `onClick` event handler on a "launch modal" button can run the `close` function if the modal is open, or the `open` function otherwise <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Backdrop/Close Button**: The modal itself needs to be able to toggle its state, for instance, when a user clicks on the backdrop or a dedicated close button within the window <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. This is achieved by passing the `handleClose` function as a prop to the `Modal` component, making it aware of the parent's state <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.

### Conditional Rendering
The `Modal` component is rendered conditionally based on the `modalOpen` state <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>:
```javascript
{modalOpen && <Modal modalOpen={modalOpen} handleClose={close} />}
```

### Handling Animation on Exit
A common issue is that when the modal state changes to `false`, the component is completely removed from the DOM, causing it to disappear instantly instead of animating out <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. To resolve this, Framer Motion's `AnimatePresence` component can be used <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. Wrapping the `Modal` component with `AnimatePresence` temporarily keeps it visible even after it's logically removed from the DOM, allowing exit animations to complete <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

Key props for `AnimatePresence`:
*   `initial={false}`: Disables any initial animations <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   `exitBeforeEnter`: Set to `true` to ensure all nodes have finished animating before they are actually removed <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

This setup enables a full sequence of animations from entry to exit <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.