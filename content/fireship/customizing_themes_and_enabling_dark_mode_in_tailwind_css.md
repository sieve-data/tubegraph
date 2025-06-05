---
title: Customizing themes and enabling dark mode in Tailwind CSS
videoId: pfaSUYaSgRo
---

From: [[fireship]] <br/> 

[[introduction_to_tailwind_css|Tailwind CSS]] is a disruptive web technology that promotes a [[functional_utility_class_approach_in_tailwind_css|functional utility class approach]] to CSS, allowing for the rapid creation of beautiful and customizable UIs <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It provides a vast collection of CSS utility classes that enable developers to write less code and maintain consistent standards <a class="yt-timestamp" data-t="00:58:19">[00:58:19]</a>. Unlike Bootstrap, [[introduction_to_tailwind_css|Tailwind CSS]] does not provide pre-built components, offering greater control over customization <a class="yt-timestamp" data-t="01:09:07">[01:09:07]</a>.

## Customizing the Color Palette

The `tailwind.config.js` file is central to customizing the behavior of [[introduction_to_tailwind_css|Tailwind CSS]], including colors, plugins, and other settings <a class="yt-timestamp" data-t="02:51:19">[02:51:19]</a>.

To customize the color palette:
*   **Extend the theme:** You can extend the existing theme within the `theme` object to include custom color types, such as `primary` and `secondary` <a class="yt-timestamp" data-t="07:07:54">[07:07:54]</a>. This allows [[introduction_to_tailwind_css|Tailwind CSS]] to generate unique utility classes based on these new colors, for example, `BG primary` or `text secondary` <a class="yt-timestamp" data-t="07:16:00">[07:16:00]</a>.
*   **Import [[introduction_to_tailwind_css|Tailwind CSS]] colors:** [[introduction_to_tailwind_css|Tailwind CSS]] ships with various other color palettes that can be imported <a class="yt-timestamp" data-t="07:27:07">[07:27:07]</a>. For instance, you can set gray colors to options like `blue gray` or `warm gray` by importing `Tailwind colors` <a class="yt-timestamp" data-t="07:30:26">[07:30:26]</a>.
*   **Override defaults with custom colors:** For specific branding needs, colors can be [[reverse_engineering_ui_to_create_theme_switcher|reverse-engineered]] from an existing application and used to replace the default [[introduction_to_tailwind_css|Tailwind CSS]] colors directly in the configuration file <a class="yt-timestamp" data-t="07:37:37">[07:37:37]</a>.

## Enabling Dark Mode

[[introduction_to_tailwind_css|Tailwind CSS]] simplifies the implementation of dark mode <a class="yt-timestamp" data-t="11:56:06">[11:56:06]</a>. To enable it, you must first opt-in within the `tailwind.config.js` file <a class="yt-timestamp" data-t="11:58:08">[11:58:08]</a>. There are two primary strategies for dark mode:

1.  **`media` strategy:** [[introduction_to_tailwind_css|Tailwind CSS]] will automatically check for the `prefers-color-scheme` CSS media feature <a class="yt-timestamp" data-t="12:02:43">[12:02:43]</a>. If the user's system preference is dark, any classes prefixed with the `dark:` variant will be applied <a class="yt-timestamp" data-t="12:06:21">[12:06:21]</a>.
2.  **`class` strategy:** This approach involves [[introduction_to_tailwind_css|Tailwind CSS]] looking for a `dark` class on parent elements <a class="yt-timestamp" data-t="12:14:02">[12:14:02]</a>. When a parent element has the `dark` class, any child elements with the `dark:` variant will apply their defined styles <a class="yt-timestamp" data-t="12:17:09">[12:17:09]</a>. This is the strategy used for implementing a [[implementing_a_css_theme_switcher_using_css_variables_and_javascript|CSS theme switcher]] with user preference management <a class="yt-timestamp" data-t="12:22:27">[12:22:27]</a>. A custom React hook can be used to manage the user's dark mode preference in [[using_local_storage_to_save_user_theme_preferences|local storage]] <a class="yt-timestamp" data-t="12:25:21">[12:25:21]</a>.

Once enabled, implementing dark mode styling involves simply going into your HTML elements and using the `dark:` variant to define the colors and other properties that should activate when dark mode is enabled <a class="yt-timestamp" data-t="12:30:26">[12:30:26]</a>.