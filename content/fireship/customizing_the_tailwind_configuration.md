---
title: Customizing the Tailwind configuration
videoId: pfaSUYaSgRo
---

From: [[fireship]] <br/> 

The `tailwind.config.js` file is the primary location for customizing the behavior of Tailwind CSS in a project <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>. This file allows developers to tailor Tailwind to their specific design needs, including customizing colors, adding plugins, and much more <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>.

## Key Configuration Options

### Just-in-Time Mode

One significant feature available for configuration is "just-in-time" (JIT) mode <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>. While in developer preview, this mode compiles CSS on the fly, leading to significantly faster build times <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.

### Automatic Style Purging

Tailwind can be configured to [[automatic_style_purging_with_tailwind | purge any unused CSS]] from the final bundle <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>. This feature is particularly useful when deploying to production, as it helps ship a very small CSS file to the browser <a class="yt-timestamp" data-t="03:15:00">[03:15:00]</a>.

### Customizing the Theme

The `theme` object within the `tailwind.config.js` file is where extensive visual customization can be done <a class="yt-timestamp" data-t="07:03:00">[07:03:00]</a>.

*   **Extending Colors**: Developers can extend the default theme with their own custom color types, such as `primary` and `secondary` <a class="yt-timestamp" data-t="07:08:00">[07:08:00]</a>. This provides unique utility classes based on these custom colors (e.g., `BG primary` or `text secondary`) <a class="yt-timestamp" data-t="07:15:00">[07:15:00]</a>.
*   **Using Pre-built Palettes**: Tailwind also ships with various other color palettes that can be imported and utilized <a class="yt-timestamp" data-t="07:27:00">[07:27:00]</a>. For example, `Tailwind colors` can be imported to set gray colors to options like `blue gray` or `warm gray` <a class="yt-timestamp" data-t="07:30:00">[07:30:00]</a>.
*   **Replacing Defaults**: It's possible to replace the default Tailwind colors with custom ones, such as those reverse-engineered from a specific application like Discord <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>.

### Dark Mode Configuration

Implementing dark mode with Tailwind is straightforward and requires opting into it within the config file <a class="yt-timestamp" data-t="11:56:00">[11:56:00]</a>. There are two primary strategies:

1.  **Media Query (Recommended for most sites)**: Using the `media` option, Tailwind will detect the user's `prefers-color-scheme` CSS property <a class="yt-timestamp" data-t="12:01:00">[12:01:00]</a>. If the scheme is dark, any classes prefixed with the `dark` variant will be applied <a class="yt-timestamp" data-t="12:06:00">[12:06:00]</a>.
2.  **Class Strategy**: The `class` option allows Tailwind to look for a `dark` class on parent HTML elements <a class="yt-timestamp" data-t="12:13:00">[12:13:00]</a>. When this class is present, the `dark` variant will be used for any of its children <a class="yt-timestamp" data-t="12:17:00">[12:17:00]</a>. This strategy is used when managing user preferences (e.g., in local storage) <a class="yt-timestamp" data-t="12:22:00">[12:22:00]</a>.

Once configured, implementing dark mode involves using the `dark` variant on elements to define the desired colors when dark mode is active <a class="yt-timestamp" data-t="12:30:00">[12:30:00]</a>.