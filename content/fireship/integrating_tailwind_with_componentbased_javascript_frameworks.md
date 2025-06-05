---
title: Integrating Tailwind with componentbased JavaScript frameworks
videoId: pfaSUYaSgRo
---

From: [[fireship]] <br/> 

[[Tailwind CSS utility class approach | Tailwind CSS]] has emerged as a disruptive web technology, advocating a functional [[Tailwind CSS utility class approach | utility class approach]] over semantic CSS <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It is highly effective at producing beautiful and customizable UIs rapidly <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. A major reason for its popularity is its excellent compatibility with component-based [[Comparison of JavaScript frameworks | JavaScript frameworks]] <a class="yt-timestamp" data-t="01:54:48">[01:54:48]</a>.

## Why Integrate Tailwind with Frameworks?

[[Tailwind CSS utility class approach | Tailwind]] is a vast collection of CSS utility classes <a class="yt-timestamp" data-t="00:58:34">[00:58:34]</a>. It allows developers to write less overall CSS code and establishes standards that prevent common styling issues <a class="yt-timestamp" data-t="01:03:03">[01:03:03]</a>. While it doesn't offer pre-built components like Bootstrap, it provides greater control over customization <a class="yt-timestamp" data-t="01:09:05">[01:09:05]</a>. The tooling, especially with VS Code extensions, makes it beginner-friendly by showing the underlying CSS for each class and performing [[Automatic style purging with Tailwind | dead code elimination]] to keep production CSS files small <a class="yt-timestamp" data-t="01:22:20">[01:22:20]</a>.

The core idea behind [[Tailwind CSS utility class approach | Tailwind]] is to design UI directly in the HTML by combining various utility classes <a class="yt-timestamp" data-t="03:30:26">[03:30:26]</a>. This approach is highly effective in component-based architectures where styles are [[Colocation of styles with Tailwind | co-located]] with the component markup.

## Initial Setup with React (Example)

While the principles apply to any component-based [[Comparison of JavaScript frameworks | JavaScript library]], React is used as a demonstration <a class="yt-timestamp" data-t="02:00:09">[02:00:09]</a>. Setup instructions for major frameworks are available in the official Tailwind documentation <a class="yt-timestamp" data-t="02:05:07">[02:05:07]</a>.

For a React project created with Create React App:

1.  **Install dependencies**: `npm install -D tailwindcss@npm:@tailwindcss/postcss7-compat postcss@^7 autoprefixer@^9` <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>
2.  **Install `craco`**: `npm install @craco/craco` <a class="yt-timestamp" data-t="02:15:39">[02:15:39]</a>
3.  **Override `react-scripts`**: Replace `react-scripts` with `craco` in `package.json` <a class="yt-timestamp" data-t="02:18:04">[02:18:04]</a>.
4.  **Create `craco.config.js`**: Configure `craco` to apply the Tailwind PostCSS plugin <a class="yt-timestamp" data-t="02:20:41">[02:20:41]</a>.
    ```javascript
    module.exports = {
      style: {
        postcss: {
          plugins: [
            require('tailwindcss'),
            require('autoprefixer'),
          ],
        },
      },
    };
    ```
5.  **Generate Tailwind config**: Run `npx tailwindcss init` to create `tailwind.config.js` <a class="yt-timestamp" data-t="02:27:07">[02:27:07]</a>.
6.  **Include Tailwind styles**: Add Tailwind directives to your main CSS file (e.g., `index.css`) <a class="yt-timestamp" data-t="02:33:57">[02:33:57]</a>.
    ```css
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
    ```
7.  **Run project**: `npm start` <a class="yt-timestamp" data-t="02:40:07">[02:40:07]</a>.

Although the setup might seem extensive, the subsequent benefits are significant <a class="yt-timestamp" data-t="02:43:08">[02:43:08]</a>.

## Customizing and Optimizing

The `tailwind.config.js` file is used for [[Customizing the Tailwind configuration | customizing the behavior of Tailwind]], including colors, plugins, and modes <a class="yt-timestamp" data-t="02:48:47">[02:48:47]</a>.

### Just-in-Time Mode
Enabling "just in time" (JIT) mode, which is in developer preview, compiles CSS on the fly, significantly improving build times <a class="yt-timestamp" data-t="02:59:02">[02:59:02]</a>.

### Purge Configuration
The config file can also be used to tell Tailwind to [[Automatic style purging with Tailwind | purge unused CSS]] from the final bundle, resulting in very small CSS files for production <a class="yt-timestamp" data-t="03:09:04">[03:09:04]</a>.

### Customizing Colors
To match specific branding, such as Discord's colors when [[Building a Discord inspired dashboard with Tailwind | building a Discord inspired dashboard]], you can extend or override the default color palette in `tailwind.config.js` <a class="yt-timestamp" data-t="07:02:44">[07:02:44]</a>. This allows creating custom utility classes based on your defined colors <a class="yt-timestamp" data-t="07:12:35">[07:12:35]</a>.

## Designing Components with Tailwind

When working with components, [[Tailwind CSS utility class approach | Tailwind's utility-first approach]] shines:

*   **IntelliSense**: VS Code extensions provide excellent IntelliSense, showing all available Tailwind utility classes and their corresponding CSS properties <a class="yt-timestamp" data-t="03:23:04">[03:23:04]</a>.
*   **Direct Application**: Classes like `text-center` or `text-green-500` are applied directly to elements within the component's JSX/HTML <a class="yt-timestamp" data-t="03:30:26">[03:30:26]</a>.
*   **Spacing Scale**: Utilities for width (`w-16`), margin (`m-4`), and padding (`p-2`) use a consistent spacing scale, ensuring visual harmony across the UI <a class="yt-timestamp" data-t="05:54:19">[05:54:19]</a>.
*   **Breaking Down UI**: For better organization, UIs are broken down into smaller components, like a `Sidebar` or `SidebarIcon`, which then encapsulate their own Tailwind styles <a class="yt-timestamp" data-t="04:40:41">[04:40:41]</a>.
*   **Custom Classes via `@apply`**: Optionally, you can define custom classes in your main CSS file using the `@apply` directive to combine multiple Tailwind utilities <a class="yt-timestamp" data-t="08:52:00">[08:52:00]</a>. This can be useful for common component styles.

### [[Implementing animated UI components with Tailwind | Animated UI Components]]

Tailwind makes [[Implementing animated UI components with Tailwind | animations]] straightforward by leveraging CSS pseudo-classes and transitions:

*   **Variants**: Use prefixes like `hover:`, `focus:`, `md:`, `lg:` to apply classes conditionally based on state or viewport size <a class="yt-timestamp" data-t="09:36:20">[09:36:20]</a>.
*   **Transitions**: Apply `transition-all` to create smooth CSS transitions between states, and customize duration or easing with additional utility classes <a class="yt-timestamp" data-t="10:18:23">[10:18:23]</a>.
*   **Group Variants**: For complex interactions, like a tooltip appearing on hover of a parent element, use the `group` utility on the parent and `group-hover:` variants on the child <a class="yt-timestamp" data-t="11:19:16">[11:19:16]</a>. This allows child elements to react to parent state changes.

## Dark Mode Implementation

[[Benefits and drawbacks of Tailwind CSS | Tailwind]] significantly simplifies dark mode implementation:

1.  **Opt-in in Config**: Enable dark mode in `tailwind.config.js` <a class="yt-timestamp" data-t="11:57:07">[11:57:07]</a>.
    *   **`media` strategy**: Tailwind observes the `prefers-color-scheme` CSS media query <a class="yt-timestamp" data-t="12:02:14">[12:02:14]</a>.
    *   **`class` strategy**: Tailwind looks for a `dark` class on parent elements. If present, any `dark:` variants are applied to children <a class="yt-timestamp" data-t="12:14:04">[12:14:04]</a>.
2.  **Apply `dark:` variants**: Once enabled, simply prefix your utility classes with `dark:` (e.g., `dark:bg-gray-800`) to define the styles that activate in dark mode <a class="yt-timestamp" data-t="12:30:17">[12:30:17]</a>.

This approach, especially with the `class` strategy, integrates seamlessly with component-based frameworks, allowing a custom hook to manage user preferences (e.g., in local storage) and apply the `dark` class to the root element <a class="yt-timestamp" data-t="12:23:44">[12:23:44]</a>.