---
title: Tailwind CSS utility class approach
videoId: pfaSUYaSgRo
---

From: [[fireship]] <br/> 
Tailwind CSS is a prominent web technology that has emerged as a disruptive force in recent years <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It challenges the conventional wisdom of semantic CSS by advocating for a more functional, [[Tailwind CSS utility class approach | utility class approach]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This philosophy enables developers to construct visually appealing and highly customizable user interfaces (UIs) more rapidly than many other methods <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## What is Tailwind CSS?
At its core, Tailwind CSS is a vast collection of CSS utility classes <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
[[comparison_between_tailwind_css_and_traditional_css | Compared to plain CSS]], it significantly reduces the amount of code needed and introduces standards that help maintain consistency <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. However, unlike frameworks such as Bootstrap, Tailwind does not offer pre-built UI components <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. While this might mean a longer initial build time for a UI compared to Bootstrap, it provides unparalleled control over customization <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## [[benefits_and_drawbacks_of_tailwind_css | Benefits and Drawbacks]]
### Benefits
*   **Faster UI Development** Tailwinds pragmatic approach focuses on shipping applications quicker <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
*   **Reduced Code and Standards** It helps in writing less code and enforcing standards, preventing inconsistencies <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
*   **High Customization** Offers superior control for tailoring UI elements <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   **Exceptional Tooling** Modern tooling, particularly in VS Code, provides excellent IntelliSense, displaying the underlying CSS when hovering over a class <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. This feature makes it feel like "CSS with training wheels" <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   **[[automatic_style_purging_with_tailwind | Dead Code Elimination]]** Automatically removes unused CSS, resulting in smaller production CSS files <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### Drawbacks
*   **No Pre-built Components** Requires more effort to build common UI patterns from scratch compared to component libraries <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## Core Concepts of Tailwind CSS
### Utility-First Approach
The fundamental idea behind Tailwind is to compose UIs by applying multiple utility classes directly in the HTML <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Examples of Utility Classes**:
    *   `text-center`: Aligns text to the center <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
    *   `text-green`: Applies a green color to text <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
    *   `flex`: Applies `display: flex` <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
    *   `fixed`: Applies `position: fixed` <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
    *   `h-screen`: Sets height to 100% of the viewport height <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
    *   `w-16`: Sets width to 16 units on Tailwind's spacing scale (e.g., 4rem or 64 pixels) <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
    *   `BG-color` (e.g., `BG-color-900`): Applies a background color <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
    *   `shadow`: Applies a pre-defined shadow effect <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
*   **Naming Convention**: Utility classes are intuitively named, often reflecting the CSS property they control (e.g., `bold` for `font-weight: bold`) <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   **Custom Values**: Brackets `[]` can be used to apply arbitrary CSS values if standard utility classes don't suffice (e.g., `top-[123px]`) <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

### [[colocation_of_styles_with_tailwind | Colocation of Styles]]
Tailwind encourages defining styles directly within the HTML/JSX of a component, leading to better [[colocation_of_styles_with_tailwind | style colocation]] <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. For complex UIs, it is recommended to break down elements into smaller, manageable components <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### [[customizing_the_tailwind_configuration | Customization]]
Tailwind's behavior can be customized via the `tailwind.config.js` file <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Extending Themes**: Developers can extend the default theme with custom colors, spacing, or other design tokens <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. This generates unique utility classes based on the custom definitions <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
*   **Color Palette**: Tailwind includes a vast default color palette with nine shades for each color <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. This can be replaced or extended with custom colors to match specific branding <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

### Just-in-Time (JIT) Mode
A feature in developer preview, JIT mode compiles CSS on the fly, significantly speeding up build times <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

### [[automatic_style_purging_with_tailwind | Automatic Style Purging]]
Tailwind can be configured to purge any unused CSS from the final bundle, resulting in a very small CSS file for production deployments <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

### Variants (Responsive Design & Pseudo-classes)
Tailwind provides "variants" for CSS pseudo-classes (like `:hover`, `:focus`) and responsive breakpoints (e.g., `md`, `lg`) <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. These allow conditional application of classes based on user interaction or screen size.

### Groups
The `group` utility class allows applying styles to a child element when its parent's state changes (e.g., `group-hover:scale-100` on a child when the parent has `group` and is hovered) <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>. This is useful for [[implementing_animated_ui_components_with_tailwind | animated tooltips]] or complex hover effects <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

### [[css_tools_and_preprocessors | Custom Classes with `@apply` Directive]]
While most styles are applied directly, Tailwind allows developers to define custom CSS classes using the `@apply` directive within the main CSS file <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. This combines multiple Tailwind utilities into a single custom class, offering a way to encapsulate common styling patterns.

### [[integrating_tailwind_with_componentbased_javascript_frameworks | Integration with Component-Based JavaScript Frameworks]]
Tailwind CSS integrates seamlessly with modern [[integrating_tailwind_with_componentbased_javascript_frameworks | component-based JavaScript frameworks]] like React, Vue, Angular, and Svelte <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. Setup instructions for major frameworks are available in the official Tailwind documentation <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

## Project Example: [[building_a_discord_inspired_dashboard_with_tailwind | Discord-Inspired Dashboard]]
A practical application of Tailwind CSS involves [[building_a_discord_inspired_dashboard_with_tailwind | cloning a Discord-inspired dashboard]] <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This project demonstrates styling a sidebar with [[implementing_animated_ui_components_with_tailwind | animated icon buttons]] that show tooltips on hover, and implementing dark mode <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
*   **Animated Icons**: Involves changing properties like border-radius and colors on hover, and animating between states using `transition-all` utilities <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
*   **Dark Mode**: Easily implemented by opting into it in the config file (either `media` or `class` strategy) and using `dark:` variants for colors <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.