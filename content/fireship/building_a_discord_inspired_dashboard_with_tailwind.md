---
title: Building a Discord inspired dashboard with Tailwind
videoId: pfaSUYaSgRo
---

From: [[fireship]] <br/> 

Tailwind CSS is a disruptive web technology that defies traditional semantic CSS by preaching a more functional, [[tailwind_css_utility_class_approach | utility class approach]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It can produce beautiful and customizable UIs faster than other approaches <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. This article details building a Discord-inspired dashboard, focusing on the sidebar with animated icon buttons and tooltips, and [[implementing_animated_ui_components_with_tailwind | dark mode]] <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## What is Tailwind CSS?

Tailwind CSS is a large collection of CSS utility classes <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. [[comparison_between_tailwind_css_and_traditional_css | Compared to plain CSS]], it allows for less code overall and provides standards that prevent common styling errors <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

Unlike [[frontend_ui_libraries_and_frameworks | Bootstrap]], Tailwind does not provide pre-built components <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. While this might mean a longer initial build time for a UI, it offers significantly better control over customization <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Although some believe Tailwind is not for beginners, the tooling has become exceptional, offering features like IntelliSense in VS Code that shows the underlying CSS of each class <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Tailwind also performs [[automatic_style_purging_with_tailwind | dead code elimination]], resulting in a small CSS file for production <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## Project Setup

Tailwind CSS works well with [[integrating_tailwind_with_componentbased_javascript_frameworks | component-based JavaScript frameworks]] like React, Vue, Angular, and Svelte <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

To set up Tailwind with Create React App:
1.  **Install dependencies**: Install necessary packages <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
2.  **Install `craco`**: Install the `craco` package to override the native PostCSS configuration <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
3.  **Replace `react-scripts`**: Use `craco` to replace `react-scripts` in `package.json` <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
4.  **Create `craco.config.js`**: Create a `craco.config.js` file to apply the Tailwind plugin <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
5.  **Generate Tailwind config**: Run `npx tailwindcss init` to generate a `tailwind.config.js` file in the project root <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
6.  **Include Tailwind styles**: Add Tailwind directives (`@tailwind base; @tailwind components; @tailwind utilities;`) to your main CSS file (e.g., `index.css`) <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
7.  **Run the project**: Start the development server with `npm start` <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

### [[customizing_the_tailwind_configuration | Customizing the Tailwind Configuration]]

The `tailwind.config.js` file is used to [[customizing_the_tailwind_configuration | customize Tailwind's behavior]], such as colors, plugins, and more <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

Important configurations:
*   **Just-in-Time (JIT) Mode**: Enable JIT mode (developer preview) to compile CSS on the fly, significantly speeding up build times <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
*   **Purge CSS**: Tell Tailwind to [[automatic_style_purging_with_tailwind | purge unused CSS]] from the final bundle, resulting in a very small CSS file for production <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

## [[tailwind_css_utility_class_approach | Tailwind's Utility Class Approach]]

The core idea behind Tailwind is to add utility classes directly to your HTML/JSX to design your UI <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. For example, `text-center` centers text, `text-green-500` applies a green color, and `font-bold` makes text bold <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. Tailwind's IntelliSense shows the actual CSS properties behind each utility class <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

For specific values not covered by default utilities, you can use arbitrary values with bracket notation (e.g., `top-[10px]`) <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. Tailwind uses a spacing scale (e.g., `w-16` for width, `m` for margin, `p` for padding) to ensure consistent design <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

## Building the Sidebar

The best way to organize a UI in Tailwind is to break it down into smaller components <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

### Sidebar Container

1.  **Flexible Container**: Apply `flex` to the root `div` in `App.js` to enable flexbox layout <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
2.  **Component Structure**: Create a `Sidebar.js` component and import it into `App.js` <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
3.  **Positioning**:
    *   `fixed`: Fixes the sidebar to the viewport <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
    *   `top-0` and `left-0`: Positions it at the top-left corner <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
    *   `h-screen`: Sets height to 100% of the viewport height <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
    *   `w-16`: Sets width to 16 units on Tailwind's spacing scale (64 pixels or 4rem) <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
4.  **Internal Layout**: Apply `flex` and `flex-col` to arrange items vertically within the sidebar <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
5.  **Styling**:
    *   `bg-gray-900`: Sets a dark gray background <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
    *   `shadow-lg`: Adds a subtle shadow for polish <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

### Customizing the Color Palette

To match Discord's branding, you can [[customizing_the_tailwind_configuration | customize Tailwind's color palette]] in `tailwind.config.js` <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

Within the `theme` object, you can:
*   `extend`: Add custom color types like `primary` and `secondary` <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   `colors`: Override default colors with custom values, such as specific Discord-inspired hex codes <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. Tailwind provides a wide range of shades (e.g., `bg-blue-500`) for each color <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

## Animated Icon Buttons and Tooltips

### Sidebar Icon Component

1.  **Create `SidebarIcon` component**: This component takes an `icon` prop and renders a `div` with a custom class `sidebar-icon` <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
2.  **Use `react-icons`**: Install `react-icons` to easily import various icons as React components <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

### [[colocation_of_styles_with_tailwind | Custom Classes with `@apply`]]

Instead of always extracting new React components for reusable styles, you can define custom classes using Tailwind utilities directly in your CSS file with the `@apply` directive <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. This is done by extending core components using the `@layer components` directive in your `index.css` file <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

Example `sidebar-icon` class:
```css
.sidebar-icon {
    @apply relative flex items-center justify-center
    h-12 w-12 mt-2 mb-2 mx-auto shadow-lg
    bg-gray-800 text-green-500
    hover:bg-green-600 hover:text-white
    rounded-3xl hover:rounded-xl transition-all duration-300 ease-linear;
}
```
*   `relative`: Provides positioning for tooltips <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
*   `flex items-center justify-center`: Centers the icon <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
*   `h-12 w-12`: Sets height and width <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
*   `mt-2 mb-2 mx-auto`: Sets margins for spacing and centering <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
*   `bg-gray-800 text-green-500`: Sets initial background and text colors <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
*   `hover:bg-green-600 hover:text-white`: Uses [[tailwind_css_utility_class_approach | hover variants]] to change colors on hover <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.
*   `rounded-3xl hover:rounded-xl`: Changes border-radius from a circle to a rounded square on hover <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
*   `transition-all duration-300 ease-linear`: [[implementing_animated_ui_components_with_tailwind | Animates the property changes]] over 300ms <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

### [[implementing_animated_ui_components_with_tailwind | Animated Tooltips with Groups]]

To add animated tooltips:
1.  **Add `text` prop**: The `SidebarIcon` component accepts a `text` prop for the tooltip content <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
2.  **Tooltip Span**: Render a `span` element with the class `sidebar-tooltip` to display the text <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.
3.  **Define `sidebar-tooltip`**: Use `@apply` in your CSS for the `sidebar-tooltip` class. Initially set its `transform` `scale` to `0` to make it invisible <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
4.  **Group Hover**: To show the tooltip when the *parent* `SidebarIcon` is hovered, use Tailwind's `group` functionality <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.
    *   Add the `group` utility class to the parent element (the `SidebarIcon`'s root `div`).
    *   On the child tooltip element, use the `group-hover:scale-100` variant to apply `scale-100` when the parent is hovered <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>.
    *   *Note*: `group` doesn't work with `@apply` inside CSS, so these classes must be applied directly in the markup <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

This creates a tooltip that is hidden by default and animates into view when its parent icon is hovered <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

## [[implementing_animated_ui_components_with_tailwind | Implementing Dark Mode]]

Tailwind makes dark mode easy to implement. First, opt into it in your `tailwind.config.js` file <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.

Two strategies for dark mode:
1.  **`media`**: Tailwind looks for the `prefers-color-scheme` CSS media query. If it's `dark`, classes with the `dark:` variant are applied automatically <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.
2.  **`class`**: Tailwind looks for a `dark` class on parent elements. When this class is present, it applies `dark:` variants to its children <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>. This is the strategy used in the Discord dashboard demo, often managed with a custom React hook to persist user preference in local storage <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.

Once configured, simply use the `dark:` variant (e.g., `dark:bg-gray-800`) to define the colors that activate when dark mode is enabled for an element <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.

By following these steps, you can create a highly customized and animated UI like a Discord-inspired dashboard with Tailwind CSS.