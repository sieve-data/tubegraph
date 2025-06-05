---
title: React modal creation from scratch
videoId: SuqU904ZHA4
---

From: [[fireship]] <br/> 

Animation is a highly satisfying aspect for developers, capable of transforming a basic feature into something distinctive [00:00:00]. This guide details the process of building a modal window in React from scratch, incorporating the Framer Motion library for advanced animations [00:00:07].

This tutorial covers:
*   How to [[styling_a_modal_with_css | style a modal with CSS]] [00:00:18].
*   How to [[managing_modal_state_with_javascript | manage its open and closed state with JavaScript]] [00:00:20].
*   How to implement declarative animations with Framer Motion and React [00:00:24].
*   Making the modal draggable [00:00:28].

A modal window is a valuable UI feature for focusing user attention or when you want to avoid navigating them to a different route [00:01:07]. Complex functionalities, such as an entire login feature, can be handled within a modal [00:01:14]. However, it's generally not recommended to automatically pop up modals for newsletter subscriptions or cookie acceptance after a few seconds [00:01:20].

## Project Setup

To begin, generate a React project using `create-react-app` [00:01:31]. Once created, open the project in your code editor and install Framer Motion, the primary dependency [00:01:37]. Framer Motion is maintained by the Framer design tool team and is considered a polished library for animations, offering an intuitive approach [00:01:42].

Run the app using `npm start` to launch the default React app on localhost 3000 [00:01:54].

### Initial Cleanup

Delete all boilerplate code from `App.js` [00:02:00] and `index.css` [00:02:05]. Instead of the default CSS, import `normalize.css` to provide a blank slate for styling [00:02:08]. The full CSS for the project is available on GitHub [00:02:18]. After these steps, the application should display an empty black background [00:02:26].

## Introducing Framer Motion

Framer Motion simplifies animations in React compared to traditional CSS animations [00:03:06]. It offers ease of use and more simplified code, and can perform actions that CSS cannot, such as listening to browser events and integrating with React application state [00:03:11].

### Basic Animation Example: Button Hover

To implement a simple animation like a button growing on hover and shrinking on tap:
1.  Import the `motion` component from `framer-motion` [00:03:35].
2.  Wrap a standard HTML button (e.g., `<button className="save-button">`) with `motion.button` [00:02:47].
3.  Use the `whileHover` prop to define the scale when hovered (e.g., `whileHover={{ scale: 1.1 }}`) [00:02:54].
4.  Use the `whileTap` prop to define the scale when tapped (e.g., `whileTap={{ scale: 0.9 }}`) [00:02:59].

```jsx
import { motion } from 'framer-motion';

function App() {
  return (
    <motion.button
      className="save-button"
      whileHover={{ scale: 1.1 }}
      whileTap={{ scale: 0.9 }}
    >
      Launch Modal
    </motion.button>
  );
}
```

This immediately creates an interactive animated button [00:03:03].

## Building the Modal Components

A modal consists of two main parts: the backdrop and the modal window [00:03:30]. These are typically organized into separate components within a `components` directory [00:03:31].

### The Backdrop

The backdrop is an overlay that covers the entire screen, making underlying content appear dark [00:03:33].

1.  **Component Structure**:
    *   Import `motion` [00:04:04].
    *   Define a `Backdrop` component that accepts `children` (for embedding other components) and `onClick` (for handling clicks to update global state) props [00:04:06].
    *   The `Backdrop` component itself is a `motion.div` [00:04:33]. Its `onClick` handler is set to the passed `onClick` prop [00:04:35], and `children` are rendered inside [00:04:39].

    ```jsx
    import { motion } from 'framer-motion';

    const Backdrop = ({ children, onClick }) => {
      return (
        <motion.div
          onClick={onClick}
          className="backdrop"
          // Animation variants will go here
        >
          {children}
        </motion.div>
      );
    };

    export default Backdrop;
    ```

2.  **CSS Styling**:
    *   Set `position: absolute` and position it at `top: 0`, `left: 0`, with `height: 100%` and `width: 100%` to make it an overlay [00:04:49].
    *   Use a black background color with an additional two characters for opacity (e.g., `#000000e1`) to allow underlying elements to be somewhat visible [00:04:56].
    *   Use `display: flex` to center its children (the modal window) both horizontally and vertically [00:05:07].

3.  **Animation States**:
    *   `initial`: `opacity: 0` (invisible) [00:05:19].
    *   `animate`: `opacity: 1` (fully visible when active) [00:05:23].
    *   `exit`: `opacity: 0` (fades out when animation is finished) [00:05:27].

    ```jsx
    // ...inside Backdrop component...
    <motion.div
      onClick={onClick}
      className="backdrop"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
    >
      {children}
    </motion.div>
    ```

### The Modal Window

The modal window sits on top of the backdrop and is where the user's attention is focused [00:03:39].

1.  **Component Structure**:
    *   Import `motion` and the `Backdrop` component [00:05:38].
    *   Define a `Modal` component that accepts `handleClose` (a function to close the modal) and `text` (content to display) props [00:05:44].
    *   The `Modal` component renders the `Backdrop` component, passing `handleClose` to its `onClick` prop [00:05:55].
    *   Inside the `Backdrop`, add a `motion.div` to represent the actual modal window [00:06:06].
    *   Crucially, inside the `motion.div` for the modal window, call `event.stopPropagation()` on its `onClick` handler to prevent clicks inside the modal from bubbling up and closing the backdrop [00:06:12].

    ```jsx
    import { motion } from 'framer-motion';
    import Backdrop from './Backdrop'; // Assuming path

    const Modal = ({ handleClose, text }) => {
      return (
        <Backdrop onClick={handleClose}>
          <motion.div
            onClick={(e) => e.stopPropagation()} // Prevent closing when clicking inside
            className="modal"
            // Animation variants will go here
          >
            <p>{text}</p>
            <button onClick={handleClose}>Close</button>
          </motion.div>
        </Backdrop>
      );
    };

    export default Modal;
    ```

2.  **CSS Styling (Responsive Design)**:
    *   To make the modal responsive, use CSS `clamp()` and `min()` functions [00:06:34].
    *   `clamp(MIN, PREFERRED, MAX)` allows setting a preferred width (e.g., 700px), but ensures it doesn't go below a minimum (e.g., 90vw) or above a maximum (e.g., 50%) [00:06:38]. This eliminates the need for extensive media queries [00:06:50].

3.  **Animation Variants (`drop`)**:
    *   Framer Motion's `variants` prop allows defining multiple custom animation states within an object [00:07:00]. This is useful for creating complex animation sequences based on user interactions [00:07:09].
    *   Define three states for the `drop` variant:
        *   `hidden`: Translates the modal along the y-axis by `-100vh` (off-screen above) [00:07:20].
        *   `visible`: Sets y-axis position to `0` (natural position) [00:07:31].
        *   `exit`: Translates the modal along the y-axis by `100vh` (off-screen below) [00:07:27].

    ```javascript
    // Define outside the component or within the component scope
    const dropIn = {
      hidden: {
        y: "-100vh",
        opacity: 0,
      },
      visible: {
        y: "0",
        opacity: 1,
        transition: {
          duration: 0.1,
          type: "spring",
          damping: 25, // Controls decrease in oscillation amplitude
          stiffness: 500, // Controls reaction speed of the spring
        },
      },
      exit: {
        y: "100vh",
        opacity: 0,
      },
    };

    // ...inside Modal component's motion.div...
    <motion.div
      onClick={(e) => e.stopPropagation()}
      className="modal"
      variants={dropIn} // Reference the variants object
      initial="hidden"   // Set initial state
      animate="visible"  // Animate to visible state
      exit="exit"      // Animate to exit state
    >
    ```

4.  **Transition Settings (Spring Physics)**:
    *   Customize the `transition` settings for the `visible` state [00:07:44].
    *   `duration`: Set to a small value, like `0.1` seconds [00:07:48].
    *   `type: "spring"`: Creates a bouncy animation [00:07:51].
    *   `damping`: Controls the decrease in oscillation amplitude. Lower values lead to more bouncing, higher values to less [00:07:59].
    *   `stiffness`: Controls how slowly or quickly the spring reacts. Lower values make it react slowly, higher values make it react quickly [00:08:15].

## Integrating with React Application State

To trigger the modal's animation, it needs to be connected to the parent React application's state.

1.  **`useState` Hook**:
    *   In the root `App` component, import the `useState` hook from React [00:08:47].
    *   Declare a state variable, e.g., `modalOpen`, with a default value of `false` and a setter function, `setModalOpen` [00:08:52].
    *   Create helper functions, `openModal` and `closeModal`, to toggle this state between `true` and `false` [00:09:03].

    ```jsx
    import React, { useState } from 'react';
    import Modal from './components/Modal'; // Assuming path
    import { motion } from 'framer-motion';

    function App() {
      const [modalOpen, setModalOpen] = useState(false);

      const openModal = () => setModalOpen(true);
      const closeModal = () => setModalOpen(false);

      return (
        <div>
          <motion.button
            className="save-button"
            whileHover={{ scale: 1.1 }}
            whileTap={{ scale: 0.9 }}
            onClick={() => (modalOpen ? closeModal() : openModal())} // Toggle
          >
            Launch Modal
          </motion.button>

          {/* Modal rendering logic here */}
        </div>
      );
    }
    ```

2.  **Conditional Rendering**:
    *   Conditionally render the `Modal` component based on the `modalOpen` state [00:09:30].
    *   Pass the `closeModal` function as the `handleClose` prop to the `Modal` component [00:09:34].

    ```jsx
    // ...inside App component's return...
    {modalOpen && (
      <Modal handleClose={closeModal} text="This is my modal content!" />
    )}
    ```

### Handling Exit Animations with `AnimatePresence`

When the modal state changes (e.g., `modalOpen` becomes `false`), the modal component is completely removed from the DOM, preventing its `exit` animation from playing [00:09:45].

*   Import `AnimatePresence` from `framer-motion` [00:10:01].
*   Wrap the `Modal` component with `AnimatePresence` [00:10:03].
*   Set `initial={false}` on `AnimatePresence` to disable any initial animations [00:10:10].
*   Set `exitBeforeEnter` to `true` to ensure that exiting nodes finish their animations before new nodes are added [00:10:17].

```jsx
import React, { useState } from 'react';
import Modal from './components/Modal';
import { motion, AnimatePresence } from 'framer-motion';

function App() {
  const [modalOpen, setModalOpen] = useState(false);

  const openModal = () => setModalOpen(true);
  const closeModal = () => setModalOpen(false);

  return (
    <div>
      <motion.button
        className="save-button"
        whileHover={{ scale: 1.1 }}
        whileTap={{ scale: 0.9 }}
        onClick={() => (modalOpen ? closeModal() : openModal())}
      >
        Launch Modal
      </motion.button>

      <AnimatePresence
        initial={false}
        mode="wait" // Use 'mode' prop in newer Framer Motion versions, 'exitBeforeEnter' is deprecated
      >
        {modalOpen && (
          <Modal handleClose={closeModal} text="This is my modal content!" />
        )}
      </AnimatePresence>
    </div>
  );
}
```

Now, the modal will animate in and out smoothly [00:10:28].

## Making the Modal Draggable

Framer Motion allows making components draggable with minimal code.
*   Add the `drag` prop to the `motion.div` representing the modal window [00:10:41].

```jsx
// ...inside Modal component's motion.div...
<motion.div
  onClick={(e) => e.stopPropagation()}
  className="modal"
  variants={dropIn}
  initial="hidden"
  animate="visible"
  exit="exit"
  drag // Add this prop
>
  <p>{text}</p>
  <button onClick={handleClose}>Close</button>
</motion.div>
```

This simple addition makes the modal window interactive and movable across the screen [00:10:43].

## Conclusion

By following these steps, you can create a fully animated, responsive, and interactive modal window in React using Framer Motion. For more advanced concepts, such as building a notification feed or working with drag-and-drop gestures in Framer, further resources may be available [00:10:48].