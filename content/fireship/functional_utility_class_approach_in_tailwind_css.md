---
title: Functional utility class approach in Tailwind CSS
videoId: pfaSUYaSgRo
---

From: [[fireship]] <br/> 

Tailwind CSS is a disruptive web technology that diverges from the traditional dogma of semantic [[CSS for Styling and Layout | CSS]] by promoting a more functional utility class approach <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This method allows developers to create beautiful and customizable user interfaces (UIs) faster than many other styling approaches <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## What is Tailwind CSS?

At its core, Tailwind CSS is a vast collection of [[CSS for Styling and Layout | CSS]] utility classes <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. Unlike plain [[CSS for Styling and Layout | CSS]], it enables writing less code overall and introduces standards that prevent common styling pitfalls <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. While it doesn't offer pre-built components like Bootstrap, which might make initial UI building take longer, it provides significantly better control over customization <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Tailwind is ideal for developers seeking to achieve highly customized designs quickly <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

## Key Principles and Advantages

*   **Utility-First Approach**: The fundamental idea behind Tailwind is to apply numerous utility classes directly within the HTML to design the UI <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. For instance, `text-center` centers text, and `text-green-500` applies a specific shade of green <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Intuitive Naming**: Utility classes are carefully named, making them intuitive to use; developers can often type out what they want to achieve (e.g., "bold") and find a corresponding utility class <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Spacing Scale**: Utilities for properties like width (`w-`), margin (`m-`), and padding (`p-`) follow a consistent spacing scale, ensuring visual harmony across elements <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Built-in Color Palette**: Tailwind includes an extensive color palette with nine different shades for each color, easily applied with prefixes like `bg-` for background or `text-` for text color <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
*   **Tooling and Optimization**:
    *   **IntelliSense**: When adding [[CSS for Styling and Layout | CSS]] classes, developers benefit from excellent IntelliSense in editors like VS Code, which shows all available Tailwind utility classes <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. Hovering over a class reveals the exact [[CSS for Styling and Layout | CSS]] properties it applies <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
    *   **Just-in-Time Mode**: Enabling just-in-time (JIT) mode compiles [[CSS for Styling and Layout | CSS]] on the fly, significantly speeding up build times <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
    *   **Dead Code Elimination (Purge)**: Tailwind can purge unused [[CSS for Styling and Layout | CSS]] from the final bundle, resulting in a very small [[CSS for Styling and Layout | CSS]] file for production <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## Customization and Configuration

Tailwind's behavior is highly customizable via its `tailwind.config.js` file <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Extending Themes**: Developers can extend the default theme with custom colors or other properties, generating unique utility classes <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   **Arbitrary Values**: For specific, unusual values not covered by the default utility classes, brackets can be used (e.g., `top-[123px]`) to automatically create a custom utility class <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

## Integrating with JavaScript Frameworks

Tailwind CSS works exceptionally well with component-based [[integrating_tailwind_css_with_javascript_frameworks | JavaScript frameworks]] like React, Vue, Angular, and Svelte <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Component Composition**: Breaking down UI into smaller components (e.g., a `Sidebar` component) helps organize the large number of utility classes applied to elements <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **Setup**: For React, setup typically involves installing dependencies, overriding PostCSS configuration, running the Tailwind CLI init command to generate a config file, and including Tailwind directives in the main [[CSS for Styling and Layout | CSS]] file <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## Advanced Features

### Responsive Design and Variants

Tailwind provides **variants** for [[CSS for Styling and Layout | CSS]] pseudo-classes (like `hover` or `focus`) and responsive breakpoints (like `md` for medium screens, `lg` for large screens) <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. These variants are prefixed to existing utility classes to apply styles conditionally <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

### Custom Classes with `@apply`

While direct utility class application is common, developers can also create their own custom [[CSS for Styling and Layout | CSS]] classes composed of Tailwind utilities using the `@apply` directive within the `index.css` file <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. This allows for abstracting common utility patterns into a single, custom class (e.g., `sidebar-icon`) <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

### Animations

Tailwind facilitates [[creating_css_animations_based_on_react_state | CSS animations]] by allowing developers to define transitions between states. For example, `transition-all` can animate changes in properties like color or border-radius, with options to customize duration and easing <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

### Groups for Child Element Styling

The `group` utility enables applying classes to a child element when its parent's state changes (e.g., when the parent is hovered) <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. This is useful for interactive elements like animated tooltips, where a child element (the tooltip) becomes visible or changes appearance when the parent icon is hovered <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. It's important to note that `group` functionality typically works best when applied directly in the markup, rather than within `@apply` directives <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

### [[customizing_themes_and_enabling_dark_mode_in_tailwind_css | Dark Mode]]

Tailwind makes [[customizing_themes_and_enabling_dark_mode_in_tailwind_css | dark mode]] implementation straightforward <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.
*   **Configuration**: Developers can opt into [[customizing_themes_and_enabling_dark_mode_in_tailwind_css | dark mode]] via the config file, choosing between `media` (based on `prefers-color-scheme` [[CSS for Styling and Layout | CSS]] property) or `class` (applying a `dark` class to a parent element) <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.
*   **Implementation**: With `class` mode, for example, developers define colors for [[customizing_themes_and_enabling_dark_mode_in_tailwind_css | dark mode]] by prefixing utilities with `dark:` (e.g., `dark:bg-gray-800`) <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.