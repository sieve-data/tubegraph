---
title: Using CSS transforms for sliding animations
videoId: IF6k0uZuypA
---

From: [[fireship]] <br/> 

[[CSS transforms for complex animations | CSS transforms]] can be utilized to create dynamic sliding animations within a user interface <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This technique is particularly effective when combined with React and a library like `react-transition-group` to manage animation states <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.

## Core Concepts

*   **`translate` Property**: The `translate()` CSS function, part of the `transform` property, is used to reposition an element on the 2D plane without affecting the layout of other elements <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. By setting a `translate` value (e.g., `translate(-110%)` or `translate(110%)`), an element can be moved off-screen, either to the left or right, to prepare for a sliding animation <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.
*   **`transition` Property**: The `transition` CSS property is used to animate changes in property values smoothly over a specified duration <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>. By applying a transition to the `transform` property, the element will slide smoothly from one `translate` position to another <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>.
*   **Timing Functions**: An `ease` timing function can be used to control the acceleration and deceleration of the animation, making it appear more natural <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.
*   **Speed Variable**: A global CSS variable, such as `--speed`, can be defined to control the animation duration consistently across different elements <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## Implementing Sliding Animations with `react-transition-group`

The `react-transition-group` package helps control the conditional logic for rendering and transitioning multiple menus when they are added or removed from the application <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a> <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

1.  **`CSSTransition` Component**: Wrap the elements to be animated within the `CSSTransition` component from `react-transition-group` <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a> <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.
    *   The `in` prop determines when the component should render and animate its children into the UI <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a> <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
    *   `unmountOnExit` ensures that children are completely removed from the DOM when they are not active <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a> <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.
    *   `timeout` defines the duration of the animation <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a> <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
    *   `classNames` provides a prefix for CSS classes that `CSSTransition` will add or remove <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a> <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.

2.  **CSS Class Toggling**: `CSSTransition` does not directly animate elements <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. Instead, it adds and removes specific CSS classes to the child element based on the animation's state <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a> <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a> <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>:
    *   `-[prefix]-enter`: Added when the `in` prop first becomes true <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a> <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.
    *   `-[prefix]-enter-active`: Added after a specified timeout <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a> <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.
    *   `-[prefix]-exit`: Added when the `in` prop becomes false <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a> <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>.
    *   `-[prefix]-exit-active`: Added after the `exit` class <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a> <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>.

3.  **CSS for Sliding Effect**:
    *   **Entering Animation (Slide-In)**: For a menu sliding in from left to right, initially set its `transform` to `translate(-110%)` (off-screen to the left) for the `*-enter` class <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a> <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>. Then, for the `*-enter-active` class, set the `transform` to `translate(0%)` <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a> <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>. Apply a `transition` to the `transform` property <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a> <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
    *   **Exiting Animation (Slide-Out)**: For a menu sliding out, set its `transform` to `translate(0%)` for the `*-exit` class, and then to `translate(-110%)` (off-screen to the left) for the `*-exit-active` class <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a> <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.
    *   **Secondary Menu (Slide-In from Right)**: A secondary menu can slide in from the right by initially setting its `transform` to `translate(110%)` (off-screen to the right) <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a> <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a> <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.

### Animating Height

When transitioning between menus of different heights, the height can be animated dynamically <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a> <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.
1.  **State for Height**: Maintain a state variable for the menu's height <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a> <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.
2.  **Calculate Height Function**: Create a function to calculate the height of a DOM element using its `offsetHeight` property <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a> <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.
3.  **Lifecycle Hook**: Use `CSSTransition`'s `onEnter` lifecycle hook to call the `calculateHeight` function when the enter class is first added to the element, providing the element as an argument <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a> <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a> <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.
4.  **Apply as Style**: Dynamically apply the calculated height to the `style` attribute of the dropdown component <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a> <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a> <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a> <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.
5.  **CSS Transition for Height**: Add a `transition` for the `height` property in the CSS to ensure a smooth animation <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a> <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a> <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>. This allows the dropdown to shrink and grow based on the current menu's size <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a> <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.