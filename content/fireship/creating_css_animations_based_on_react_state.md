---
title: Creating CSS animations based on React state
videoId: IF6k0uZuypA
---

From: [[fireship]] <br/> 

This article details how to build dynamic user interfaces with animated elements by leveraging React's state management capabilities and CSS. It specifically draws lessons from reverse-engineering the UI features of Facebook, including its top navigation bar icon buttons and a [[Multilevel animated dropdown menu using React and CSS | multi-level animated drop-down]] [00:00:07]. The techniques discussed include using [[React Hooks explanation | React Hooks]] (specifically `useState`), component composition, and controlling [[Animating UI elements with CSS keyframes | CSS animations]] based on the application's state [00:00:30].

## Core Concepts

The foundation of animating UI elements based on React state involves several key principles:

### React State Management with `useState`

In React, components can manage data that changes throughout their lifecycle, known as "state" [00:07:53]. The `useState` [[React Hooks explanation | hook]] is a fundamental tool for managing this state in functional components [00:07:57].

*   **Declaring State**: Calling the `useState` function returns an array with two values: the current state value and a function to update that state [00:08:01]. For instance, `const [open, setOpen] = useState(false);` declares an `open` boolean state variable, initialized to `false`, and a `setOpen` function to change it [00:08:10].
*   **Toggling State**: An event handler, such as `onClick`, can be used to call the state-updating function. For example, `setOpen(!open)` flips the `open` boolean to its opposite value, useful for toggling visibility [00:08:33].
*   **Conditional Rendering**: React uses JavaScript expressions within JSX to conditionally render UI elements based on state. If a state variable (e.g., `open`) is true, a component's children can be shown; otherwise, they remain hidden [00:09:01].

### Integrating CSS for Transitions

While React manages the state, CSS is responsible for the visual [[Implementing transitions and animations in Svelte 3 | transitions and animations]]. A `transition` property in CSS can be applied to elements to animate changes in their properties, such as `filter` for brightness or `background-color` for hover effects [00:06:24].

*   **Hover Effects**: A simple CSS transition can be set up for a property (e.g., `filter`) over a specified duration (e.g., 300 milliseconds) [00:06:26]. When a pseudo-selector like `:hover` changes a property (e.g., `filter: brightness(1.2)`), the change will animate smoothly [00:06:33].

## Advanced Animations with `react-transition-group`

For more complex animations, especially when elements are added or removed from the DOM, a popular package like `react-transition-group` is highly beneficial [00:11:38]. It simplifies the conditional logic for rendering and transitioning between multiple UI elements.

### `CSSTransition` Component

The `CSSTransition` component from `react-transition-group` helps control animation lifecycles [00:11:51].

*   **Wrapping Elements**: Wrap the elements you want to animate (e.g., a drop-down menu) with the `CSSTransition` component [00:12:11].
*   **Props Configuration**:
    *   `in`: A boolean prop that, when truthy, renders and animates its children into the UI [00:12:15]. For example, `in={activeMenu === 'main'}` would show the component only when the `activeMenu` state is 'main' [00:12:21].
    *   `unmountOnExit`: When set to `true`, this prop completely removes the children from the DOM when they are not active, preventing hidden elements from interfering with layout or other animations [00:12:27].
    *   `timeout`: Defines the duration of the animation in milliseconds [00:12:33].
    *   `classNames`: This prop specifies a prefix for the CSS classes that `CSSTransition` will add or remove from its child element during the animation lifecycle [00:12:37].

### How `CSSTransition` Controls CSS

`CSSTransition` does not directly animate elements; instead, it dynamically adds and removes specific CSS classes to its child element based on the animation's state [00:12:57]. Developers then define the actual animations within these CSS classes.

*   **CSS Class Patterns**: `CSSTransition` generates classes like:
    *   `[prefix]-enter`: Added when the `in` prop first becomes true [00:13:13].
    *   `[prefix]-enter-active`: Added after a timeout, allowing for a transition from the `enter` state [00:13:17].
    *   `[prefix]-exit`: Added when the `in` prop becomes false, preparing for removal [00:13:24].
    *   `[prefix]-exit-active`: Added after a timeout during the exit phase [00:13:26].
*   **Defining Animations in CSS**: By targeting these classes, you can create various [[Animating UI elements with CSS keyframes | CSS animations]]:
    *   **[[Using CSS transforms for sliding animations | Sliding Animations]]**: To make a menu slide in from the left, you can initially `transform: translateX(-110%)` on the `enter` class (making it invisible off-screen) and then set `transform: translateX(0)` on the `enter-active` class, combined with a `transition` property [00:13:34]. For sliding out, the `exit` and `exit-active` classes would translate the element in the opposite direction (e.g., `translateX(-110%)` for exit) [00:13:57]. This approach allows for distinct [[Slide animations based on router data | slide animations]] for different menus (e.g., primary menu sliding in from the left, secondary menu sliding in from the right) [00:14:26].

## Animating Dynamic Height

A common challenge with animations is ensuring that the container height smoothly adjusts when content (like a menu) changes, especially when different menus have varying heights [00:11:13].

*   **Dynamic Height State**: Introduce a state variable (e.g., `menuHeight`) to store the current height of the menu [00:15:37].
*   **Calculating Height**: Create a function to calculate the height of a DOM element using its `offsetHeight` property, which provides the actual height in pixels [00:15:41].
*   **`onEnter` Lifecycle Hook**: The `CSSTransition` component provides `lifecycle hooks` such as `onEnter` [00:15:56]. This callback is invoked as soon as the `enter` class is added to the element and passes the DOM element as an argument [00:16:00]. This allows you to call the height calculation function and update the `menuHeight` state [00:16:08].
*   **Applying Height as Style**: The calculated `menuHeight` can then be applied directly as an inline style to the animated container (`style={{ height: menuHeight }}`) [00:16:14].
*   **CSS Transition for Height**: Finally, add a `transition` property for `height` in your CSS for the container element to ensure smooth height changes [00:16:23]. This allows the drop-down to "magically shrink and grow" based on the content [00:16:29].

By combining React's state management with `react-transition-group` and well-defined CSS, it's possible to create fluid and intuitive UI animations that enhance the user experience, similar to the impressive UIs found on platforms like Facebook [00:00:01].