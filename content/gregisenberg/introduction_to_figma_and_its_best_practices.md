---
title: Introduction to Figma and its best practices
videoId: XoOx5xPdv4M
---

From: [[gregisenberg]] <br/> 

Figma is a powerful design tool used for live design sessions and building startup ideas <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. It allows designers to quickly iterate on ideas and apply best practices for visual improvements and [[prototyping_and_interactivity_in_figma_design_workflow | interactivity]] <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Core Concepts and Basic Operations

*   **Frames (`F` key)**: A frame is like a container in Figma, similar to a CSS `div`. It's the basic unit for creating any design element <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   **[[building_components_and_using_auto_layout_in_figma | Components]]**: Though often associated with Design Systems, components are excellent for speeding up the design process. They act as "speed mechanisms" allowing designers to make changes once and have them propagate everywhere, minimizing repetitive tasks <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. Create a component as a first step even before adding content <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **[[building_components_and_using_auto_layout_in_figma | Auto Layout]] (`Shift A`)**: This feature works similarly to CSS Flexbox, allowing you to stack elements and control spacing between them <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. Building designs using Auto Layout makes them easier to implement in code <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.
*   **Duplicating (`Command D`)**: Quickly duplicate elements <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
*   **Drawing Rectangles (`R` key)**: Use to create shapes or placeholders for images <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
*   **Adding Text (`T` key)**: Use to create text layers <a class="yt-timestamp" data-t="00:32:41">[00:32:41]</a>.
*   **Changing Opacity (Number Keys)**: Quickly adjust element opacity by typing a number key (e.g., `6` for 60%, `0` for 100%) <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Navigating Layers (`Enter` and `Shift Enter`)**: Hit `Enter` to drill into layers and `Shift Enter` to move back up the layer tree for faster traversal <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.
*   **Moving Layers (`Command + Bracket Keys`)**: Use `Command + [` to move a selected layer down and `Command + ]` to move it up in the layer hierarchy <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.
*   **Multi-Edit Variants (`Q` key)**: When editing a component, pressing `Q` allows you to make changes simultaneously across all instances of that component, preventing redundant work <a class="yt-timestamp" data-t="00:27:04">[00:27:04]</a>.

## Design Workflow and Best Practices

### Iteration and Exploration
*   **Embrace Iteration**: Design is about trying many things. The faster you can explore different options, the better your outcome <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.
*   **Preserve Iterations**: Duplicate frames (`Command D`) to save different versions of your design. Use the "Destroyer" plugin to detach components within duplicated frames, effectively "freezing" that iteration in time so it won't be updated by main component changes <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. This allows you to have a visual history of your design evolution <a class="yt-timestamp" data-t="00:30:31">[00:30:31]</a>.
*   **Real-time Preview**: Keep your design open in prototype mode on a separate device (e.g., a laptop) to see it at actual size while you zoom in and make changes on your main monitor <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.

### Inspiration and Mental Models
*   **Constant Inspiration Gathering**: Maintain a database (like Notion) of designs you like, categorizing them constantly. This creates an "abundance" of ideas, so you're not starting from a blank page <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. Collect and analyze why you like certain details in designs you encounter <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   **Metadata Approach**: Think about design elements like a spreadsheet, considering all available metadata (e.g., title, instructor name, course length, price) to guide your layout <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

### Technical Considerations
*   **Design with Development in Mind**: If you're technically minded, consider how your design choices will translate into code. Figma's Auto Layout maps directly to Flexbox in CSS, making handoff smoother <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. Avoid arbitrary positioning, which is akin to `absolute` positioning in CSS, generally less ideal <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.
*   **Tailwind CSS Values**: When in doubt about spacing or sizing, use multiples of eight, as these align well with Tailwind CSS syntax and common web development practices <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.

## Visual Enhancements

*   **Layer Blur**: Add depth and interest using the Layer Blur effect under the effects panel <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>.
*   **Blend Modes**: Experiment with blend modes like "Luminosity" to allow underlying colors to bleed through images, creating a tinted black and white effect <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>.
*   **[[incorporating_visual_effects_and_textures_in_design_with_figma_plugins | Noise and Texture]]**: Adding subtle graininess or texture can significantly enhance visual interest <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>.
*   **Inner Shadows**: Use inner shadows to create a subtle rounded, 3D, or "lighting over the edge" effect on corners, a common technique in modern designs <a class="yt-timestamp" data-t="00:33:17">[00:33:17]</a>.

## [[prototyping_and_interactivity_in_figma_design_workflow | Prototyping]]
*   **Interactive Components**: To add [[prototyping_and_interactivity_in_figma_design_workflow | interactivity]] like hover states, create a component and then add a "variant" (e.g., a "hover" variant). Link the default state to the hover variant in prototype mode, setting the trigger to "While Hovering" <a class="yt-timestamp" data-t="00:23:27">[00:23:27]</a>.
*   **Smart Animate**: Always use "Smart Animate" for transitions to create smooth, natural-feeling interactions instead of instant changes <a class="yt-timestamp" data-t="00:24:53">[00:24:53]</a>. "Gentle" easing with a duration around 400ms is a good starting point <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>.

## Recommended Plugins
While Figma's built-in features are robust, some plugins enhance specific workflows:
*   **Destroyer**: Removes components from a frame, allowing you to "freeze" an iteration in time <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.
*   **Phosphor**: A great library for consistent, beautiful icons <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.
*   **Smooth Shadow**: Creates complex, realistic shadows that are difficult to achieve manually with single shadow layers <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>.
*   **Noise and Texture**: Generates various visual effects, including simple noise for added texture <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>.
*   **Content Reel**: Populates designs with diverse content (images, avatars, text) quickly, often used with "Select Similar Layers" to target specific elements <a class="yt-timestamp" data-t="00:30:44">[00:30:44]</a>.

## Figma vs. Code-based Tools
Figma excels at rapid, generative exploration of ideas, allowing for more divergent and less templated designs compared to tools like [[future_of_design_tools_figma_versus_codebased_tools_like_framer | V0]] <a class="yt-timestamp" data-t="00:35:53">[00:35:53]</a>. It's ideal for throwing "paint at the wall" and figuring out what you want to make <a class="yt-timestamp" data-t="00:36:37">[00:36:37]</a>.

However, the design process is evolving. For web design, moving from Figma to a tool like [[future_of_design_tools_figma_versus_codebased_tools_like_framer | Framer]] can be beneficial to build out the final 5-10% of a design, especially for [[prototyping_and_interactivity_in_figma_design_workflow | interactive]] elements <a class="yt-timestamp" data-t="00:36:26">[00:36:26]</a>. As the line blurs between high-fidelity design tools and code, Figma may increasingly serve as a lower-fidelity ideation and exploration platform <a class="yt-timestamp" data-t="00:38:09">[00:38:09]</a>.

## Getting Started
The best way to learn Figma is to "get your hands dirty" and start playing with the tools <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>. Open a new file, type `F`, and draw a frame to begin <a class="yt-timestamp" data-t="00:39:43">[00:39:43]</a>.