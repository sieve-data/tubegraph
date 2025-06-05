---
title: Multilevel animated dropdown menu using React and CSS
videoId: IF6k0uZuypA
---

From: [[fireship]] <br/> 

This article details how to reverse engineer features from Facebook's UI, specifically its top navigation bar, icon buttons, and a multi-level animated dropdown menu, using HTML, CSS, and React <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Core Concepts and Learnings

The tutorial covers several key programming and design concepts:
*   [[creating_icon_buttons_with_flexbox_in_react | Creating icon buttons with Flexbox]] <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.
*   Using CSS transforms to create sliding animations <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
*   Fundamental [[react_hooks_explanation | React concepts]] such as component composition <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>, hooks <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>, and [[creating_css_animations_based_on_react_state | creating CSS animations based on the state of your React application]] <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Project Overview

The project aims to create several reusable React components for navigation and dropdowns <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>:
*   **Navbar Component**: Acts as the top navigation bar <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   **Nav Items**: Children of the `Navbar`, represented as icon buttons <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. These buttons can toggle their children (e.g., a dropdown menu) <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **Dropdown Component**: Renders when a nav item with a "carrot" icon is clicked <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
*   **Dropdown Items**: Contained within the `Dropdown` component <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. Items with a chevron can toggle to a secondary dropdown menu <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Animations**: The entire menu slides out to the left and the new one slides in from the right <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The height of the menu is also animated to adapt to different content <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Setup and Initial Structure

### React Application Setup
To begin, create a React application by running `npx create-react-app Facebook` in your command line, assuming Node.js is installed <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. For simplicity, delete all files except `index.js`, `App.js`, and `index.css` <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. The `index.js` file is the initial entry point, and its service worker code can be removed <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. All boilerplate code in `App.js` should also be removed <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

### Functional React Components and JSX
The tutorial utilizes functional React components <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. A function whose name starts with a capital letter is considered a component <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. The return value of a functional component is JSX, which is a syntax extension for JavaScript allowing HTML-like templates <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

### Initial CSS Setup
The CSS used is generic and can be adapted to any framework <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Global CSS Variables**: Define a theme and an animation speed variable (e.g., `--speed` for 500ms) <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   **Default Styles**: Override default unordered list styles and match link elements to the text color variable <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

```css
:root {
  /* Define your theme variables here */
  --nav-size: 60px;
  --speed: 500ms;
}

ul {
  list-style: none; /* Remove default list bullets */
}

a {
  color: var(--text-color); /* Match link color to theme */
}
```

## Building the Top Navigation Bar

### Navbar Component
Component composition is used to break the application into small, reusable pieces <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   Define a `Navbar` component in `App.js` that returns an HTML `nav` element containing an unordered list (`ul`) <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   Use `className` (instead of `class` in HTML) to apply CSS classes <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

```javascript
// In App.js
function Navbar(props) {
  return (
    <nav className="navbar">
      <ul className="navbar-nav">{props.children}</ul>
    </nav>
  );
}

function App() {
  return (
    <Navbar>
      {/* Nav items will go here */}
    </Navbar>
  );
}
```

### Styling the Navbar
The `navbar` CSS styles it as a rectangle at the top of the page <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   Fixed height based on `--nav-size`, coloring, and padding <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
*   The `navbar-nav` (the `ul` inside `nav`) is a Flex container for children <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
    *   `display: flex` sets it as a flexible row <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
    *   `justify-content: flex-end` makes children start on the right <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

```css
.navbar {
  height: var(--nav-size);
  background-color: var(--bg);
  padding: 0 1rem;
  border-bottom: var(--border);
}

.navbar-nav {
  max-width: 100%;
  height: 100%;
  display: flex;
  justify-content: flex-end; /* Align items to the right */
}
```

## Creating Nav Items and Icon Buttons

### NavItem Component
Components pass data and UI using `props` <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   The `NavItem` component takes `props` and returns a list item (`li`) with an anchor (`a`) element inside <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
*   Instead of `props.children`, a custom `icon` prop is used to pass the icon <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

```javascript
// In App.js
function NavItem(props) {
  return (
    <li className="nav-item">
      <a href="#" className="icon-button">
        {props.icon}
      </a>
    </li>
  );
}

function App() {
  return (
    <Navbar>
      <NavItem icon="😀"></NavItem>
      <NavItem icon="👍"></NavItem>
      <NavItem icon="🎉"></NavItem>
    </Navbar>
  );
}
```

### Styling Nav Items and Icon Buttons
*   **Nav Item Sizing**: Each `nav-item` is slightly smaller than the `navbar` <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. Its width can be calculated dynamically using `calc(var(--nav-size) * 0.8)` <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   **Centering Children**: `nav-item` and `icon-button` both use Flexbox (`display: flex`, `align-items: center`, `justify-content: center`) to center their children horizontally and vertically <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
*   **Circular Shape**: `icon-button` gets a `--button-size` variable set to `calc(var(--nav-size) * 0.5)` <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. Applying this to `width` and `height`, and `border-radius: 50%` creates a perfect circle <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   **Hover Effect**: A CSS transition is applied to the `filter` property <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. On hover, the `icon-button`'s `filter: brightness(1.2)` makes it slightly brighter <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

```css
.nav-item {
  width: calc(var(--nav-size) * 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
}

.icon-button {
  --button-size: calc(var(--nav-size) * 0.5);
  width: var(--button-size);
  height: var(--button-size);
  background-color: var(--bg-accent);
  border-radius: 50%;
  padding: 5px;
  margin: 2px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: filter 300ms; /* Smooth hover effect */
}

.icon-button:hover {
  filter: brightness(1.2); /* Make brighter on hover */
}
```

### Integrating SVG Icons
SVG icons can be used as React components directly <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.
*   Import an SVG file (e.g., `import { ReactComponent as BellIcon } from './icons/bell.svg';`) <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   Then, use it as a component within JSX (e.g., `<BellIcon />`) <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
*   SVG elements do not inherit size by default, so a fixed width and height should be set for them <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

```css
.icon-button svg {
  fill: var(--text-color);
  width: 20px;
  height: 20px;
}
```

## Implementing the Dropdown Menu

### Managing State with `useState`
To open and close a dropdown, the `NavItem` needs state <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. The `useState` hook manages this <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
*   Call `useState` in `NavItem` to get `open` (boolean state) and `setOpen` (function to change state) <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. Default `open` to `false` <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   Add an `onClick` event handler to the `icon-button` that calls `setOpen(!open)` to toggle the dropdown <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
*   Conditionally render `props.children` only when `open` is `true` <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

```javascript
// In NavItem component
import { useState } from 'react';

function NavItem(props) {
  const [open, setOpen] = useState(false); // State for dropdown visibility

  return (
    <li className="nav-item">
      <a href="#" className="icon-button" onClick={() => setOpen(!open)}>
        {props.icon}
      </a>
      {open && props.children} {/* Conditionally render children */}
    </li>
  );
}
```

### DropdownMenu and DropdownItem Components
*   **DropdownMenu**: A `DropdownMenu` component returns a `div` with class `dropdown` <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
*   **DropdownItem**: A `DropdownItem` component is a link (`a`) with class `menu-item` and uses `props.children` for text <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. It also includes `leftIcon` and `rightIcon` props for flexible icon placement <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.

```javascript
// In App.js
function DropdownMenu() {
  return (
    <div className="dropdown">
      <DropdownItem>My Profile</DropdownItem>
      <DropdownItem leftIcon="⚙️" rightIcon=">">Settings</DropdownItem>
    </div>
  );
}

function DropdownItem(props) {
  return (
    <a href="#" className="menu-item">
      {props.leftIcon && <span className="icon-button">{props.leftIcon}</span>}
      {props.children}
      {props.rightIcon && <span className="icon-button">{props.rightIcon}</span>}
    </a>
  );
}

// Usage in Navbar
function App() {
  return (
    <Navbar>
      <NavItem icon="⚙️">
        <DropdownMenu />
      </NavItem>
    </Navbar>
  );
}
```

### Styling the Dropdown
*   **DropdownMenu Positioning**: `position: absolute` is used to make the dropdown overlap the navbar slightly <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. `top: 58px` will make it overlap by 2px with a 60px nav bar <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
    *   `width: 300px` <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
    *   `transform: translateX(-45%)` moves it to the left <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
    *   `overflow: hidden` is crucial to hide child elements that are slid in or out of the container <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
*   **DropdownItem Styling**: `menu-item` elements are Flex containers (`display: flex`, `align-items: center`) <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
    *   A transition is added to `background` for hover effects <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
    *   On hover, `background-color` changes <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
    *   To push the `rightIcon` to the far right, set `margin-left: auto` on the `icon-button` that is the right icon <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.

```css
.dropdown {
  position: absolute;
  top: 58px;
  width: 300px;
  transform: translateX(-45%);
  background-color: var(--bg);
  border: var(--border);
  border-radius: var(--border-radius);
  padding: 1rem;
  overflow: hidden; /* Hide overflowing elements */
  transition: height var(--speed) ease; /* For animating height */
}

.menu-item {
  height: 50px;
  display: flex;
  align-items: center;
  border-radius: var(--border-radius);
  transition: background var(--speed);
}

.menu-item:hover {
  background-color: var(--bg-accent);
}

.menu-item .icon-button:first-child { /* Left icon */
  margin-right: var(--spacing);
}

.menu-item .icon-button:last-child { /* Right icon */
  margin-left: auto; /* Push to the right */
}
```

## Animated Multi-level Dropdown

### Using `react-transition-group`
The `react-transition-group` package, specifically the `CSSTransition` component, helps control conditional rendering and transitions between multiple menus <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   Install: `npm install react-transition-group` <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   Import `CSSTransition` <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.
*   Add state to `DropdownMenu` to track `activeMenu` (e.g., `main`, `settings`) using `useState` <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   Wrap each menu section in a `CSSTransition` component <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>:
    *   `in={activeMenu === 'menuName'}`: Renders and animates children when true <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.
    *   `unmountOnExit`: Removes children from the DOM when not active <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.
    *   `timeout={500}`: Duration of the animation <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>.
    *   `classNames="menu-primary"` (or `menu-secondary`): Prefix for CSS classes `CSSTransition` will add <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.

```javascript
// In DropdownMenu component
import { useState } from 'react';
import { CSSTransition } from 'react-transition-group';

function DropdownMenu() {
  const [activeMenu, setActiveMenu] = useState('main'); // e.g., 'main', 'settings'
  const [menuHeight, setMenuHeight] = useState(null); // For animating height

  function calculateHeight(el) {
    const height = el.offsetHeight;
    setMenuHeight(height);
  }

  return (
    <div className="dropdown" style={{ height: menuHeight }}>
      {/* Primary Menu */}
      <CSSTransition
        in={activeMenu === 'main'}
        timeout={500}
        classNames="menu-primary"
        unmountOnExit
        onEnter={calculateHeight}>
        <div className="menu">
          <DropdownItem>My Profile</DropdownItem>
          <DropdownItem
            leftIcon="⚙️"
            rightIcon=">"
            goToMenu="settings" // Prop to navigate to settings menu
            onClick={() => setActiveMenu('settings')}>
            Settings
          </DropdownItem>
        </div>
      </CSSTransition>

      {/* Secondary Menu */}
      <CSSTransition
        in={activeMenu === 'settings'}
        timeout={500}
        classNames="menu-secondary"
        unmountOnExit
        onEnter={calculateHeight}>
        <div className="menu">
          <DropdownItem
            leftIcon="<"
            goToMenu="main" // Prop to navigate back to main menu
            onClick={() => setActiveMenu('main')}>
            Main Menu
          </DropdownItem>
          <DropdownItem>Option 1</DropdownItem>
          <DropdownItem>Option 2</DropdownItem>
        </div>
      </CSSTransition>
    </div>
  );
}

// In DropdownItem, pass goToMenu prop
function DropdownItem(props) {
  return (
    <a href="#" className="menu-item" onClick={props.onClick}>
      {props.leftIcon && <span className="icon-button">{props.leftIcon}</span>}
      {props.children}
      {props.rightIcon && <span className="icon-button">{props.rightIcon}</span>}
    </a>
  );
}
```

### CSS for Slide Animations
`CSSTransition` adds and removes specific classes based on the animation state, allowing CSS to handle the actual animation <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **`.classNames-enter`**: Added when `in` becomes true.
*   **`.classNames-enter-active`**: Added after `timeout` (500ms) with `classNames-enter`.
*   **`.classNames-exit`**: Added when `in` becomes false.
*   **`.classNames-exit-active`**: Added after `timeout` with `classNames-exit`.

For a slide-in from left to right for the primary menu (`menu-primary`):
*   Initial state (`.menu-primary-enter`): `transform: translateX(-110%)` (invisible off-screen left) <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.
*   Active state (`.menu-primary-enter-active`): `transform: translateX(0%)` <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.
*   Transition: `transition: transform var(--speed) ease` <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.
*   Exit: `transform: translateX(-110%)` again for exit <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.

For a slide-in from right to left for the secondary menu (`menu-secondary`):
*   Initial state (`.menu-secondary-enter`): `transform: translateX(110%)` (invisible off-screen right) <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
*   Active state (`.menu-secondary-enter-active`): `transform: translateX(0%)` <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
*   Exit: `transform: translateX(110%)` again for exit <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.

```css
/* Menu Animation */
.menu {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  position: absolute;
  background-color: var(--bg);
  transform: translateX(0%);
  transition: transform var(--speed) ease;
}

.menu-primary-enter {
  transform: translateX(-110%);
}

.menu-primary-enter-active {
  transform: translateX(0%);
}

.menu-primary-exit {
  transform: translateX(0%);
}

.menu-primary-exit-active {
  transform: translateX(-110%);
}

.menu-secondary-enter {
  transform: translateX(110%);
}

.menu-secondary-enter-active {
  transform: translateX(0%);
}

.menu-secondary-exit {
  transform: translateX(0%);
}

.menu-secondary-exit-active {
  transform: translateX(110%);
}
```

### Animating Height Dynamically
When menus have different numbers of items, the dropdown's height needs to animate <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.
*   Create state for `menuHeight` in `DropdownMenu` <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.
*   Define a `calculateHeight` function that takes a DOM element and sets `menuHeight` to `element.offsetHeight` (actual height in pixels) <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.
*   Use the `onEnter` lifecycle hook of `CSSTransition` to call `calculateHeight` when a menu enters the DOM <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.
*   Apply the `menuHeight` state as an inline style to the `dropdown` div: `<div className="dropdown" style={{ height: menuHeight }}>` <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.
*   Add a `transition` for `height` to the `.dropdown` CSS class to animate the height changes <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.

With these steps, the dropdown will dynamically shrink and grow smoothly based on the current menu's size <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>.