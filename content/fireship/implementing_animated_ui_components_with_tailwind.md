---
title: Implementing animated UI components with Tailwind
videoId: pfaSUYaSgRo
---

From: [[fireship]] <br/> 

[[Tailwind CSS]] is a disruptive web technology that promotes a [[tailwind_css_utility_class_approach | utility class approach]] to CSS, enabling developers to build customizable UIs faster than traditional methods <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This approach allows for the creation of beautiful and interactive designs with a minimal CSS footprint <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Core Concepts for UI Design with Tailwind CSS

Tailwind CSS provides a vast collection of CSS utility classes <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. Unlike traditional CSS, it allows you to write less code overall and maintain consistent standards <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. While it doesn't offer pre-built components like Bootstrap, it provides greater control over customization <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

### Development Environment & Setup
Modern tooling, including VS Code extensions, provides intellisense that shows the exact CSS properties inside each Tailwind class when you hover over it <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Tailwind also performs [[automatic_style_purging_with_tailwind | dead code elimination]] to ensure a small CSS file for production <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

[[integrating_tailwind_with_componentbased_javascript_frameworks | Tailwind CSS works well with component-based JavaScript libraries]] like React, Vue, Angular, and Svelte <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. The setup generally involves:
1.  Generating a project with a JavaScript framework (e.g., Create React App) <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
2.  Installing Tailwind CSS dependencies <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
3.  Generating a `tailwind.config.js` file using `npx tailwindcss init` <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
4.  Including Tailwind styles in your main CSS file (e.g., `index.css`) using `@tailwind` directives <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

### [[customizing_the_tailwind_configuration | Customizing the Tailwind Configuration]]
The `tailwind.config.js` file allows for extensive customization, including colors and plugins <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. Key configurations for performance and customization include:
*   **Just-in-Time Mode**: Compiles CSS on the fly for faster build times (in developer preview) <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
*   **Purge**: Configures Tailwind to remove any unused CSS from the final bundle for production <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   **Theme Extension**: You can extend the default theme with custom colors or use existing palettes from `tailwind-colors` <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. For example, to match Discord's branding, custom colors can replace defaults <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

### Utility-First Styling
The core idea behind Tailwind is to combine utility classes directly in your HTML markup to design your UI <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Text Alignment**: `text-center` for `text-align: center;` <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
*   **Colors**: `text-green-500` applies a green text color <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Positioning**: `fixed`, `top-0`, `left-0` for fixed positioning <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Sizing**: `h-screen` (100% viewport height), `w-16` (16 units on Tailwind's spacing scale, which means 4rem or 64 pixels) <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
*   **Spacing**: `m-` for margin, `p-` for padding, using the same spacing scale <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **Backgrounds**: `bg-color-shade` (e.g., `bg-gray-800`) applies a background color <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
*   **Shadows**: `shadow-lg` for pre-built shadows <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

## Building Interactive UI Components

When designing complex UIs, it's best to break them down into smaller components <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. [[colocation_of_styles_with_tailwind | Tailwind CSS integrates well with component-based frameworks]], allowing styles to be co-located with the components <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

### Custom Classes with `@apply`
While Tailwind encourages a utility-first approach, you can define custom classes composed of Tailwind utilities using the `@apply` directive in your CSS file (e.g., `index.css`) <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. This is useful for reusable component styles.

Example: `sidebar-icon` class <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
```css
@layer components {
  .sidebar-icon {
    @apply relative flex items-center justify-center
           h-12 w-12 mt-2 mb-2 mx-auto shadow-lg
           bg-gray-800 text-green-500
           hover:bg-green-600 hover:text-white
           rounded-3xl hover:rounded-xl
           transition-all duration-300 ease-linear;
  }
}
```
This example sets:
*   Positioning: `relative`, `flex`, `items-center`, `justify-center` <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
*   Sizing & Spacing: `h-12`, `w-12`, `mt-2`, `mb-2`, `mx-auto` <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   Colors: `bg-gray-800`, `text-green-500` <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.

### Hover States and Animations
Tailwind provides variants for CSS pseudo-classes by prefixing existing classes with `hover:` or `focus:` <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.
*   **Color Change**: `hover:bg-green-600`, `hover:text-white` <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.
*   **Shape Animation**: Changing `border-radius` on hover (e.g., `rounded-3xl hover:rounded-xl` for a circle-to-square animation) <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Transitions**: Apply `transition-all` to enable smooth transitions between states, with options to customize `duration-` or `ease-` <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

### Animated Tooltips with Groups
To implement animated tooltips that appear on parent hover:
1.  **Invisible by Default**: Hide the tooltip by default using `scale-0` <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
2.  **Parent-Child Interaction**: Use the `group` utility on the parent element and `group-hover:` variant on the child element to change its appearance when the parent is hovered <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>. For example, `group-hover:scale-100` makes the tooltip visible and animates its scale on hover <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.

:::caution
The `group` feature does not work properly with the `@apply` directive <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. Classes using `group-hover:` should be applied directly in the markup <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.
:::

## Dark Mode Implementation
Tailwind CSS makes [[frontend_ui_libraries_and_frameworks | dark mode]] easy to implement by opting into it in the config file <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>. There are two main strategies:
*   **Media Query (`media`)**: Tailwind will check for the `prefers-color-scheme` CSS property. If it's dark, classes prefixed with `dark:` will be applied <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.
*   **Class Strategy (`class`)**: Tailwind looks for a `dark` class on parent elements. When present, the `dark:` variant applies to any of its children <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>. This is often used with a custom React hook to manage user preference in local storage <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.

Once configured, simply define the colors or styles you want to activate in dark mode using the `dark:` variant (e.g., `dark:bg-gray-900`) <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.

By leveraging these features, you can build interactive and animated UI components efficiently with Tailwind CSS <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.