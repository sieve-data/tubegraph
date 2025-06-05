---
title: Using Framer Motion for animations in React
videoId: SuqU904ZHA4
---

From: [[fireship]] <br/> 

Animation is a highly satisfying aspect for developers, capable of transforming a mundane feature into something remarkable <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This guide explores building an animated modal window in React from scratch, leveraging the [[advanced_animation_techniques_with_framer_motion | Framer Motion]] library to implement complex animations <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Why Use Framer Motion?

[[advanced_animation_techniques_with_framer_motion | Framer Motion]] is a library maintained by the team behind the Framer design tool, offering a well-maintained and polished solution for implementing animations <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. While not the only method for animation in React, it's considered a highly intuitive approach for features like modals <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

Advantages of [[advanced_animation_techniques_with_framer_motion | Framer Motion]] over regular CSS animations include:
*   **Ease of Use & Simplified Code** <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   **Advanced Capabilities**: It can listen to different browser events and integrate directly with the [[creating_css_animations_based_on_react_state | actual state of your React application]] <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
*   **Developer-Friendly**: Provides a more intuitive workflow for developers <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

## Project Setup and Initial Animation

To begin, generate a React project, typically using Create React App <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. The only dependency required is [[advanced_animation_techniques_with_framer_motion | Framer Motion]] <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. After creation, open the project in a code editor like VS Code and install [[advanced_animation_techniques_with_framer_motion | Framer Motion]] via npm or yarn <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

Initial setup involves:
*   Running `npm start` to view the default React app <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   Deleting boilerplate code from `App.js` and `index.css` <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   Importing `normalize.css` for a blank slate <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   Pasting in the project's CSS (available on GitHub) <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### Animating a Simple Button

[[advanced_animation_techniques_with_framer_motion | Framer Motion]] wraps HTML elements, providing additional props for animation configuration <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

1.  **Import `motion` component**: Start by importing `motion` from `framer-motion` <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
2.  **Swap for `motion` element**: Replace a regular HTML button (`<button>`) with its `motion` equivalent (`<motion.button>`) <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
3.  **Add Animation Props**:
    *   `whileHover`: Makes the button bigger when hovered <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
    *   `whileTap`: Makes the button smaller when tapped, simulating a push <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

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

## Building the Modal Window

The modal consists of two main parts: a `Backdrop` (an overlay) and the `Modal` window itself <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. It's good practice to organize components in separate files, ideally with a directory for each major component <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

### Backdrop Component

The `Backdrop` component serves as an overlay that darkens the screen, making the modal the focus <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

*   **Props**:
    *   `children`: Allows embedding additional components <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
    *   `onClick`: A custom event handler to update the global state when the backdrop is clicked <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. This makes it a "dump component" without its own internal state <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
*   **CSS**:
    *   `position: absolute`, `top: 0`, `left: 0`, `height: 100%`, `width: 100%` for overlay <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
    *   Black background with an opacity hex value (e.g., `#000000E1`) <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
    *   `display: flex` to center children horizontally and vertically <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Animation States**:
    *   `initial`: `opacity: 0` (invisible) <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
    *   `animate`: `opacity: 1` (active) <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
    *   `exit`: `opacity: 0` (finished animation) <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

```jsx
// components/Backdrop/index.jsx
import { motion } from 'framer-motion';

const Backdrop = ({ children, onClick }) => {
  return (
    <motion.div
      onClick={onClick}
      className="backdrop"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
    >
      {children}
    </motion.div>
  );
};

export default Backdrop;
```

### Modal Component

The `Modal` window sits on top of the backdrop, focusing user attention <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

*   **Props**:
    *   `closeModal`: A function to close the modal <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
    *   `text`: The content to display inside the window <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   **Event Handling**:
    *   The `motion.div` representing the modal window should have an `onClick` handler that calls `event.stopPropagation()` <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. This prevents clicks on the modal content from bubbling up to the backdrop and closing the modal unexpectedly <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
*   **Responsive CSS**:
    *   The `clamp()` and `min()` CSS functions can be used for responsive width/height without media queries <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. For example, `width: clamp(700px, 90%, 50vw)` sets the width to 700px, but adapts to 90% if the screen is smaller or a maximum of 50vw if larger <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
*   **Variants for Custom Animation States**:
    *   The `variants` prop references an object (e.g., `dropIn`) that defines multiple custom animation states <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. This allows for complex animation sequences based on user interaction <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
    *   Example `dropIn` variant:
        *   `hidden`: `y: "-100vh"` (starts above viewport) <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
        *   `visible`: `y: "0"` (lands in natural position) <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
        *   `exit`: `y: "100vh"` (drops below viewport) <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   **Transition Settings**:
    *   `duration`: Controls the animation speed <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
    *   `type: "spring"`: Creates a bouncy animation effect <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
    *   `damping`: Decreases oscillation amplitude as energy drains from the system <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. Low damping leads to continuous bouncing, high damping reduces bounce <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
    *   `stiffness`: Affects how slowly or quickly the spring reacts <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

```jsx
// components/Modal/index.jsx
import { motion } from 'framer-motion';
import Backdrop from '../Backdrop';

const dropIn = {
  hidden: { y: "-100vh", opacity: 0 },
  visible: {
    y: "0",
    opacity: 1,
    transition: {
      duration: 0.1,
      type: "spring",
      damping: 25, // Example values
      stiffness: 500, // Example values
    },
  },
  exit: { y: "100vh", opacity: 0 },
};

const Modal = ({ closeModal, text }) => {
  return (
    <Backdrop onClick={closeModal}>
      <motion.div
        onClick={(e) => e.stopPropagation()}
        className="modal"
        variants={dropIn}
        initial="hidden"
        animate="visible"
        exit="exit"
      >
        <p>{text}</p>
        <button onClick={closeModal}>Close</button>
      </motion.div>
    </Backdrop>
  );
};

export default Modal;
```

## Integrating and Controlling Animations with React State

To trigger the modal's animation in the React app, [[react_hooks_explanation | the `useState` hook]] from React is used <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

1.  **Import `useState` and `Modal`**: Import `useState` and the `Modal` component into your root `App` component <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
2.  **Define Modal State**: Create a state variable, e.g., `modalOpen`, with a default value of `false` <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
3.  **Toggle Functions**: Create `handleClose` and `handleOpen` functions to toggle `modalOpen` <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
4.  **Button Integration**: Define the `onClick` event handler for the launch button to toggle the modal state <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
5.  **Conditional Rendering**: Conditionally render the `Modal` component based on `modalOpen` state, passing `modalOpen` and `handleClose` as props <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

```jsx
// App.js
import React, { useState } from 'react';
import Modal from './components/Modal'; // Assuming path

function App() {
  const [modalOpen, setModalOpen] = useState(false);

  const handleClose = () => setModalOpen(false);
  const handleOpen = () => setModalOpen(true);

  return (
    <div className="App">
      <motion.button
        className="save-button"
        onClick={() => (modalOpen ? handleClose() : handleOpen())}
        whileHover={{ scale: 1.1 }}
        whileTap={{ scale: 0.9 }}
      >
        Launch Modal
      </motion.button>

      {modalOpen && <Modal modalOpen={modalOpen} handleClose={handleClose} />}
    </div>
  );
}
```

### The `AnimatePresence` Component

When the modal is removed from the DOM (e.g., `modalOpen` becomes `false`), it disappears instantly instead of animating out <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. To fix this, use [[advanced_animation_techniques_with_framer_motion | Framer Motion]]'s `AnimatePresence` component <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.

`AnimatePresence` temporarily keeps components visible even after they've been removed from the DOM, allowing exit animations to complete <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

*   **`initial={false}`**: Disables initial animations when the component first mounts <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **`exitBeforeEnter`**: Ensures that all nodes finish animating out before new ones animate in <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

```jsx
// App.js
import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion'; // Import AnimatePresence
import Modal from './components/Modal';

function App() {
  const [modalOpen, setModalOpen] = useState(false);

  const handleClose = () => setModalOpen(false);
  const handleOpen = () => setModalOpen(true);

  return (
    <div className="App">
      <motion.button
        className="save-button"
        onClick={() => (modalOpen ? handleClose() : handleOpen())}
        whileHover={{ scale: 1.1 }}
        whileTap={{ scale: 0.9 }}
      >
        Launch Modal
      </motion.button>

      <AnimatePresence
        initial={false}
        exitBeforeEnter={true}
        onExitComplete={() => null} // Optional: callback when exit animations are complete
      >
        {modalOpen && <Modal modalOpen={modalOpen} handleClose={handleClose} />}
      </AnimatePresence>
    </div>
  );
}
```

## Making the Modal Draggable

To make the modal window draggable, simply add the `drag` prop to the `motion.div` representing the modal <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.

```jsx
// components/Modal/index.jsx
import { motion } from 'framer-motion';
import Backdrop from '../Backdrop';

// ... dropIn variant ...

const Modal = ({ closeModal, text }) => {
  return (
    <Backdrop onClick={closeModal}>
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
        <button onClick={closeModal}>Close</button>
      </motion.div>
    </Backdrop>
  );
};

export default Modal;
```

## Further Learning

For more advanced concepts, such as building a notification feed or working with more complex drag-and-drop gestures in [[advanced_animation_techniques_with_framer_motion | Framer Motion]], additional resources are available <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.