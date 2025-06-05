---
title: Component composition and hooks in React
videoId: IF6k0uZuypA
---

From: [[fireship]] <br/> 

This article explores fundamental concepts in [[react_hooks_explanation | React]] development, focusing on [[Component composition and hooks in React | component composition]] and [[react_hooks_explanation | hooks]], specifically the `useState` hook, as demonstrated through rebuilding parts of the Facebook UI.

## Introduction to React UI Development
The new Facebook UI is noted for its simplicity, intuitiveness, and speed <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This demonstration reverse engineers features like the top navigation bar with icon buttons and a multi-level animated drop-down using HTML, CSS, and [[react_hooks_explanation | React]] <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. Key concepts covered include:
*   [[creating_icon_buttons_with_flexbox_in_react | Creating icon buttons with Flexbox]] <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>.
*   Using CSS transforms for sliding animations <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>.
*   Fundamental [[react_hooks_explanation | React]] concepts like [[Component composition and hooks in React | component composition]] and [[react_hooks_explanation | hooks]] <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>.
*   [[creating_css_animations_based_on_react_state | Creating CSS animations based on the state of a React application]] <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>.

The goal is to produce reusable [[react_hooks_explanation | React]] components for navigation and dropdowns <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>.

## Setting Up a React Application
To begin, a [[react_hooks_explanation | React]] app is required <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>. Assuming Node.js is installed, `npx create-react-app` can be run from the command line, naming the app "Facebook" for this demo <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>.

For simplicity, extraneous files are deleted, leaving `index.js`, `app.js`, and `index.css` <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>. `index.js` is the initial entry point <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>. Boilerplate code is removed from `app.js` to prepare for using functional [[react_hooks_explanation | React]] components <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>.

### Functional React Components and JSX
In [[react_hooks_explanation | React]], a function whose name starts with a capital letter can be considered a component <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>. The return value of a functional component is its UI, typically written in JSX <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>. JSX is a syntax extension for [[javascript_fundamentals_and_practical_concepts | JavaScript]] that allows HTML-like templates within components <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>.

## Component Composition
[[Component composition and hooks in React | Component composition]] is the practice of breaking down an application into many small, reusable pieces <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>. [[react_hooks_explanation | React]], especially functional components, makes this very easy <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.

### Building the Navbar Component
A `Navbar` component is defined in `App.js`, returning an HTML `nav` element containing an unordered list (`ul`) <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>. CSS classes are applied using `className` (instead of `class` in regular HTML) <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>. The `Navbar` component is then declared within the `App` component's JSX like a regular HTML element <a class="yt-timestamp" data-t="03:15:00">[03:15:00]</a>.

#### Passing Data with Props
[[react_hooks_explanation | React]] components can pass data and UI elements to each other using `props` <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>. `props` is an argument to the component function and can be referenced in the template <a class="yt-timestamp" data-t="04:14:00">[04:14:00]</a>.

A built-in `props` property named `children` projects any UI elements passed inside the component's tags <a class="yt-timestamp" data-t="04:19:00">[04:19:00]</a>. For example, adding a list item inside `Navbar`'s tags will render it where `props.children` is called <a class="yt-timestamp" data-t="04:28:00">[04:28:00]</a>.

### Creating a NavItem Component
A new `NavItem` component is created, which also takes `props` <a class="yt-timestamp" data-t="04:39:00">[04:39:00]</a>. It uses a list item (`li`) as its main element, nesting an anchor (`a`) or link element inside, which represents the icon button <a class="yt-timestamp" data-t="04:44:00">[04:44:00]</a>.

Instead of `props.children`, a custom `icon` prop is passed <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>. This allows passing an [[react_hooks_explanation | SVG]] icon or an emoji string <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>. `props` allow data to be passed from parent to child, similar to arguments in a [[javascript_fundamentals_and_practical_concepts | JavaScript]] function <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>.

## React Hooks: `useState`
To enable opening and closing a dropdown, a `NavItem` needs to manage its `state`—data that changes throughout the app's lifecycle <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>. [[react_hooks_explanation | State]] in [[react_hooks_explanation | React]] is managed using a [[react_hooks_explanation | hook]] called `useState` <a class="yt-timestamp" data-t="07:59:00">[07:59:00]</a>.

### Implementing `useState` for Dropdown Toggle
Inside the `NavItem` component, the `useState` function is called <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>. It returns an array with two values, which can be destructured:
1.  **State value**: In this case, `open`, a boolean indicating if the dropdown menu is open <a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>.
2.  **State setter function**: `setOpen`, used to change the state <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>.

A default value can be set as an argument to `useState`, e.g., `false` to keep the dropdown closed by default <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>.

To allow user interaction to change the state, an `onClick` event handler is added to the link element <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>. When clicked, `setOpen` is called, flipping the `open` value to its opposite (`!open`), which is useful for toggling elements <a class="yt-timestamp" data-t="08:37:00">[08:37:00]</a>.

### Conditional Rendering with State
The `open` state is used to conditionally show the dropdown. Below the link, an expression is added: `open && props.children` <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>. If `open` is `true`, `props.children` (which will be the `DropDownMenu` component) is shown; otherwise, nothing is rendered <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>.

### Building the DropDownMenu Component
A `DropDownMenu` component is created, returning a `div` with a `drop-down` class <a class="yt-timestamp" data-t="09:17:00">[09:17:00]</a>. This `DropDownMenu` is then passed as the child of the `NavItem` <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>.

Inside `DropDownMenu`, a `DropDownItem` component is nested. This item is a link (`a`) with a `menu-item` class, and `props.children` controls its text content <a class="yt-timestamp" data-t="09:31:00">[09:31:00]</a>. `DropDownItem` also includes flexible slots for a `leftIcon` and `rightIcon` prop, which will only render if provided <a class="yt-timestamp" data-t="09:44:00">[09:44:00]</a>.

### Animating Multi-Level Dropdowns with `react-transition-group`
For animating multi-level dropdowns, the `react-transition-group` package is installed <a class="yt-timestamp" data-t="11:38:00">[11:38:00]</a>. This package helps control conditional rendering and transitions of menus <a class="yt-timestamp" data-t="11:42:00">[11:42:00]</a>. The `CSSTransition` component from this package is imported <a class="yt-timestamp" data-t="11:49:00">[11:49:00]</a>.

The `DropDownMenu` gains state to track the `activeMenu` (e.g., `main`, `settings`, `animals`) using `useState` <a class="yt-timestamp" data-t="11:54:00">[11:54:00]</a>. `CSSTransition` wraps the dropdown elements, using the `in` prop to determine if children should render and animate (e.g., `activeMenu === 'main'`) <a class="yt-timestamp" data-t="12:09:00">[12:09:00]</a>. `unmountOnExit` removes children when not active, `timeout` defines animation duration, and `classNames` prefixes the CSS classes applied during transition <a class="yt-timestamp" data-t="12:26:00">[12:26:00]</a>.

`CSSTransition` adds or removes CSS classes (e.g., `menu-primary-enter`, `menu-primary-enter-active`, `menu-primary-exit`, `menu-primary-exit-active`) to its first child element based on the animation state, allowing CSS to handle the actual animations <a class="yt-timestamp" data-t="12:42:00">[12:42:00]</a>. For example, a `menu-primary` will slide in from left to right using `transform: translateX()` <a class="yt-timestamp" data-t="13:33:00">[13:33:00]</a>.

### Dynamic Height Animation
A challenge arises when menus have different heights, causing the dropdown to "snap" into place <a class="yt-timestamp" data-t="15:24:00">[15:24:00]</a>. To address this, state is created for the menu `height` <a class="yt-timestamp" data-t="15:37:00">[15:37:00]</a>. A `calculateHeight` function takes a DOM element and uses its `offsetHeight` property to get its pixel height <a class="yt-timestamp" data-t="15:41:00">[15:41:00]</a>.

`CSSTransition` offers lifecycle hooks like `onEnter`, which calls a callback as soon as the `enter` class is added, providing the element as an argument <a class="yt-timestamp" data-t="15:56:00">[15:56:00]</a>. `calculateHeight` is passed to `onEnter`, recalculating the height of the incoming menu <a class="yt-timestamp" data-t="16:00:00">[16:00:00]</a>. This dynamic height is then applied as a `style` attribute to the dropdown `div` <a class="yt-timestamp" data-t="16:13:00">[16:13:00]</a>. Finally, a CSS transition for `height` is added to the `.drop-down` class, allowing the menu to shrink and grow smoothly <a class="yt-timestamp" data-t="16:21:00">[16:21:00]</a>.