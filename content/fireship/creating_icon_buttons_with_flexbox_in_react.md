---
title: Creating icon buttons with Flexbox in React
videoId: IF6k0uZuypA
---

From: [[fireship]] <br/> 
The Facebook UI was praised for its simplicity, intuitiveness, and speed <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. This article explains how to reverse engineer some of its UI features, specifically the top navigation bar's icon buttons <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This demonstration uses HTML, CSS, and React <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

Through this tutorial, you will learn how to:
*   Create icon buttons with Flexbox <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
*   Use CSS transforms for sliding animations <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
*   Understand [[component_composition_and_hooks_in_react | fundamental concepts in React like component composition and hooks]] <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
*   Learn about [[creating_css_animations_based_on_react_state | creating CSS animations based on the state of your React application]] <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

The goal is to create several reusable React components for navigation and dropdowns, including a `Navbar` component with `Nav Items` as icon buttons <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Initial Setup

### Create a React App
To begin, you will need a React application <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
1.  Ensure Node.js is installed <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
2.  Open your command line and run `npx create-react-app Facebook` <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
3.  For simplicity, delete all files except `index.js`, `app.js`, and `index.css` <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
4.  In `index.js`, remove any `serviceworker` imports and registrations <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. This file can be ignored for the remainder of the setup <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
5.  Remove all boilerplate code from `app.js` <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

### Functional React Components
This project primarily uses functional React components <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. A function whose name starts with a capital letter is considered a component <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. The return value of a functional component is your UI, typically written in JSX <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. JSX is a syntax extension for JavaScript that enables writing HTML-like templates within your components <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

### Global CSS Setup
In `index.css`, define global CSS variables for a consistent theme and animation speed <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>:
*   Global CSS variables can be thought of as a theme <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   A `speed` variable defines the animation speed <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   Override the default unordered list style <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
*   Set link elements to match the text color variable in the color scheme <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

## Building the Top Navigation Bar

### Navbar Component
[[component_composition_and_hooks_in_react | Functional components in React]] simplify breaking applications into small, reusable pieces, a practice known as component composition <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

1.  In `App.js`, define a new `Navbar` component that returns JSX <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
2.  Inside the `Navbar`, add an HTML `nav` element containing an unordered list (`ul`) <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
3.  Apply CSS classes using `className` (instead of `class` in regular HTML) to these elements for styling <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
4.  Declare the `Navbar` component in the `App` component's JSX <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

**CSS for Navbar (`index.css`)**:
*   The `navbar` acts as a rectangle at the top <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   Give it a fixed height based on a `nav-size` variable and apply coloring and padding <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   The `ul` inside the `nav` serves as the container for children <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   Set its `display` property to `flex` to create a flexible row <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   Make it take up 100% of the parent's width and height <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   Use `justify-content: flex-end` to align children to the right <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

### Nav Item Component (Icon Buttons)
React components use `props` to pass data and UI elements between them <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. `props` is an argument to your function, and `props.children` references any UI elements passed inside the component's tags <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

1.  Create a new component called `NavItem` <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
2.  `NavItem` also accepts `props` <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
3.  Its main element will be a list item (`li`) with a nested anchor (`a`) or link element <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
4.  The `a` element represents the icon button, so give it a relevant CSS class <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
5.  Instead of `props.children`, pass a custom prop named `icon` to render the icon <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. Props allow passing data from parent to child, similar to arguments in a JavaScript function <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

**CSS for Nav Items (`index.css`)**:
*   Each `nav-item` is a box slightly smaller than the navbar <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   Calculate its width dynamically using `calc()`: `calc(var(--nav-size) * 0.8)` <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   Use Flexbox to center its children: `display: flex; align-items: center; justify-content: center;` <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
*   For the circular icon button shape:
    *   Scope a new CSS variable `button-size` to the class, `calc(var(--nav-size) * 0.5)` <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
    *   Apply `button-size` to `width` and `height` <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
    *   Use `border-radius: 50%` to create a perfect circle <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
    *   Center children inside the circle using Flexbox again <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   **Hover Effect**:
    *   Apply a CSS `transition` to the `filter` property with a duration of 300ms <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
    *   Target the `:hover` pseudo-selector on the icon button and set `filter: brightness(1.2)` to make it slightly brighter <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

### Using SVG Icons
The actual Facebook UI uses SVG icons <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>. You can use SVG icons directly as React components <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

1.  Add an `import` statement at the top of your file that references the path to your SVG icon <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
2.  Import the SVG as a React component using the `as` keyword <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
3.  In your `Navbar` component, instead of an emoji, use braces to pass in your SVG component directly as the `icon` prop <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
4.  SVG's don't inherit a size by default, so set a fixed `width` and `height` for them in CSS <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

At this point, you should have an icon navigation bar very similar to the actual Facebook UI <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.