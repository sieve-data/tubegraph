---
title: Building a Discordinspired animated navbar with Tailwind CSS
videoId: pfaSUYaSgRo
---

From: [[fireship]] <br/> 

Tailwind CSS is a disruptive web technology that promotes a [[functional_utility_class_approach_in_tailwind_css | functional utility class approach]] to CSS, enabling the creation of customizable UIs quickly <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This guide outlines how to build a Discord-inspired animated sidebar (functioning as a navbar) with interactive elements and dark mode.

## What is Tailwind CSS?

Tailwind CSS is a collection of CSS utility classes that allow developers to write less code and maintain consistent standards compared to plain CSS <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. Unlike frameworks like Bootstrap, Tailwind does not provide pre-built components, offering greater control over customization at the cost of initial build time <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

Despite initial perceptions, Tailwind's tooling has improved significantly, providing features like IntelliSense in VS Code to show exact CSS properties when hovering over a class <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. It also includes dead code elimination for smaller production CSS files <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Tailwind is ideal for developers seeking to achieve highly customized designs faster <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

## Setting Up Tailwind CSS

[[introduction_to_tailwind_css | Tailwind CSS]] works well with component-based JavaScript libraries like React, Vue, Angular, and Svelte <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. This demo uses React, but the setup principles apply broadly, with official documentation available for various frameworks <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

### Integration with Create React App

To integrate Tailwind into a Create React App project:
1.  Install dependencies <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
2.  Install `craco` to override native PostCSS configuration <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
3.  Replace `react-scripts` with `craco` in `package.json` <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
4.  Create a `craco.config.js` file to apply the Tailwind plugin <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
5.  Use `npx tailwindcss init` to generate a `tailwind.config.js` file in the project root <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
6.  Include Tailwind styles in `index.css` using the `@tailwind` directive <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
7.  Run `npm start` to run the project locally <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

### Tailwind Configuration

The `tailwind.config.js` file allows customization of Tailwind's behavior, including colors and plugins <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

*   **Just-in-Time (JIT) Mode:** Enable `jit` mode for faster CSS compilation on the fly <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
*   **Purge:** Configure Tailwind to purge unused CSS from the final bundle for smaller production file sizes <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

### Applying Utility Classes

Tailwind's core idea is to combine utility classes directly in HTML to design the UI <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. For example, `text-center` centers text, and `text-green-500` applies a specific shade of green <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. IntelliSense provides guidance on available classes and their underlying CSS properties <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

## Building the Discord-Inspired Sidebar

The sidebar functions as the navbar in this example.

### Structure and Positioning

1.  **Flexible Container:** Wrap the entire UI in a flexible container using `class="flex"` <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
2.  **Component Organization:** Break down the UI into smaller components, such as a `Sidebar.js` functional component <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
3.  **Sidebar Positioning:**
    *   Use `fixed` to fix it to the viewport <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
    *   `top-0` and `left-0` position it at the top-left corner <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
    *   `h-screen` makes it 100% of the viewport height <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
    *   `w-16` sets its width to 16 units on Tailwind's spacing scale (4rem or 64px), ensuring consistent spacing <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

### Styling the Sidebar

*   **Internal Layout:** Use `flex` and `flex-col` to position elements inside the sidebar <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
*   **Background and Text Color:** Apply background colors using `bg-color` and text colors using `text-color` <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. Tailwind offers a comprehensive color palette with nine shades per color <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
*   **Shadows:** Add `shadow-lg` for a polished look <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

### Customizing Colors

To match specific branding, like Discord's, you can customize the color palette in `tailwind.config.js` <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. Within the `theme` object, you can `extend` it with custom color types (e.g., `primary`, `secondary`) or replace default colors by importing `tailwind/colors` and setting new gray scales <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

## Animated Icon Buttons and Tooltips

This section focuses on [[creating_css_animations_based_on_react_state | creating CSS animations based on React state]] for interactive icons.

### Sidebar Icon Component

1.  Create a `SidebarIcon` React component that accepts an `icon` prop <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
2.  Use the `react-icons` package to easily import icons from libraries like Font Awesome and Bootstrap <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
3.  Assign a custom class, `sidebar-icon`, to the icon's container <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

### Creating Custom Tailwind Classes

Instead of applying many utility classes directly to an element, you can create custom classes composed of Tailwind utilities using the `@apply` directive in your `index.css` file <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

*   In `index.css`, use `@layer components` to define custom classes <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
*   Example for `sidebar-icon`:
    ```css
    .sidebar-icon {
      @apply relative flex items-center justify-center
             h-12 w-12 mt-2 mb-2 mx-auto shadow-lg
             bg-gray-800 text-green-500 hover:bg-green-600
             hover:text-white rounded-3xl hover:rounded-xl
             transition-all duration-300 ease-linear;
    }
    ```
    *   `relative`, `flex`, `items-center`, `justify-center`: Positioning and alignment <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
    *   `h-12`, `w-12`: Square dimensions <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
    *   `mt-2`, `mb-2`, `mx-auto`: Margins; `mx` and `my` for horizontal/vertical margins <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
    *   `bg-gray-800`, `text-green-500`: Default background and text colors <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.

### Hover Effects and Animations

Tailwind provides variants for CSS pseudo-classes like `hover` and `focus` by simply prefixing existing classes (e.g., `hover:bg-green-600`) <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

To create animations (e.g., a circle to square transition on hover):
1.  **Define changing properties:** Change `bg-color`, `text-color`, and `border-radius` (e.g., `rounded-3xl` for circle, `hover:rounded-xl` for square) <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
2.  **Apply Transitions:** Use `transition-all` to create a CSS transition between states <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.
3.  **Control Duration and Easing:** Override default transition settings with `duration-300` and `ease-linear` <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.

### Animated Tooltips

To add animated tooltips:
1.  **Add Tooltip Element:** Inside `SidebarIcon`, add a default `text` prop and a `span` with a `sidebar-tooltip` class to display the text <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
2.  **Style Tooltip:** Define the `sidebar-tooltip` class in `index.css` using `@apply` for positioning, background, text, and shadow <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
3.  **Hide by Default:** Make the tooltip invisible by default, e.g., using `scale-0` <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
4.  **Show on Parent Hover (`group` variant):** Since hovering an invisible element is impossible, use Tailwind's `group` feature <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
    *   Apply the `group` utility class to the parent element (e.g., `SidebarIcon`'s root div) <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
    *   Apply `group-hover:scale-100` to the child tooltip element to show it when the parent is hovered <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.
    *   Note: `group` variants do not work correctly with `@apply` and must be applied directly in the markup <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

The result is a hidden tooltip that animates into view when its parent icon is hovered <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

## Implementing Dark Mode

[[customizing_themes_and_enabling_dark_mode_in_tailwind_css | Tailwind makes dark mode implementation straightforward]] by opting into it in `tailwind.config.js` <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.

There are two primary strategies:
1.  **`media` strategy:** Tailwind checks the `prefers-color-scheme` CSS media property. If it's `dark`, classes with the `dark` variant are applied (e.g., `dark:bg-gray-900`) <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.
2.  **`class` strategy:** Tailwind looks for a `dark` class on parent elements. If present, it applies `dark` variant classes to its children <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>. This strategy is used in the demo and often involves a custom React hook to manage user preferences in local storage <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.

Implementing dark mode simply involves using the `dark:` variant to define alternative colors for elements when dark mode is enabled <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.