---
title: Prototyping and adding interactivity in Figma
videoId: XoOx5xPdv4M
---

From: [[gregisenberg]] <br/> 

This article explores how to leverage Figma for rapid prototyping and adding interactivity to designs, based on a live design session focusing on creating course cards for a marketplace. The process emphasizes quick iteration and best practices for efficiency and visual appeal. <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>

## Fundamental Figma Concepts for Iteration

### Frames
In Figma, a frame acts as a container for design elements, similar to a CSS `div`. <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a> It is the foundational element for organizing content. To create a frame, press `F` on the keyboard. <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>

### Components
Using [[using_components_and_auto_layout in Figma | components]] early in the design process, even before adding content, is a significant efficiency hack. <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a> While often associated with Design Systems, [[using_components_and_auto_layout in Figma | components]] can serve as "hacky speed mechanisms" to minimize repetitive tasks. <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a> Duplicating a component multiple times allows for simultaneous styling changes to all instances, providing a "one knob" approach to adjustments. <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>

### Auto Layout
[[using_components_and_auto_layout in Figma | Auto layout]] functions like a stack and maps directly to CSS Flexbox. <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a> By using `Shift + A`, any elements can be thrown into an [[using_components_and_auto_layout in Figma | auto layout]] frame. <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a> This allows for easy control over spacing, alignment, and responsiveness, ensuring designs are buildable in code. <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a> Designs built with [[using_components_and_auto_layout in Figma | auto layout]] are easily translatable to Flexbox, which is a best practice for front-end development. <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>

## Adding Interactivity and Visual Polish

### Prototyping Hover States
To add interactivity like a hover state:
1.  Make the element a component. <a class="yt-timestamp" data-t="00:23:29">[00:23:29]</a>
2.  In the top right, click "Add Variant" to create a new state (e.g., "hover"). <a class="yt-timestamp" data-t="00:23:33">[00:23:33]</a>
3.  Make visual changes to the "hover" variant (e.g., increase blur, background, border). <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>
4.  Switch to `Prototype` mode in the top right. <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a>
5.  Drag the blue dot from the default state to the hover state. <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>
6.  Set the interaction trigger to "while hovering". <a class="yt-timestamp" data-t="00:24:42">[00:24:42]</a>
7.  Choose `Smart Animate` for smooth transitions. <a class="yt-timestamp" data-t="00:24:53">[00:24:53]</a> A "gentle" easing curve with a duration of around 400ms is often recommended for a good feel. <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>

### Enhancing Visuals with Effects

*   **Layer Blur**: Add a rectangle, set its color, move it to the back (`Command + Left Bracket`), and apply a `Layer Blur` effect. <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a> Adjusting opacity (`number keys`) can create subtle lighting effects. <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>
*   **Blend Mode (Luminosity)**: For images, applying the `Luminosity` blend mode can make underlying colors bleed through, creating a tinted black and white effect. <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a> This is a commonly used CSS property. <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>
*   **Noise and Texture**: Adding a subtle layer of noise or graininess using a plugin like `Noise and Texture` can significantly enhance visual interest and depth. <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>
*   **Inner Shadows**: Using inner shadows can create a subtle 3D, rounded, or "lighting over the edge" effect on corners, adding depth and texture to designs. <a class="yt-timestamp" data-t="00:33:11">[00:33:11]</a> Set inner shadows to white for a highlight from the top and a darker color for a shadow from the bottom. <a class="yt-timestamp" data-t="00:33:43">[00:33:43]</a>

## Workflow and Efficiency Hacks

### Iteration Workflow
An effective workflow involves designing in one main frame and frequently duplicating it (`Command + D`) to create "saved bookmarks" of design iterations. <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>

### Plugins for Enhanced Workflow
While Figma offers many native features, certain [[plugins_and_tools_for_enhancing_figma_design_workflow | plugins]] can significantly speed up specific workflows:
*   **Destroyer**: Removes all components within a frame, "freezing" that iteration in time. <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a> This allows for continued exploration of a new design path without affecting previous saved states. <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>
*   **Phosphor**: A favored [[plugins_and_tools_for_enhancing_figma_design_workflow | plugin]] for icons, ensuring visual consistency. <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a> Access it via `Command + K` and typing "phosphor". <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>
*   **Smooth Shadow**: Generates multi-layered, soft shadows that mimic realistic lighting, providing more depth than a single drop shadow layer. <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>
*   **Content Reel**: Useful for populating designs with diverse content like avatars, names, or other placeholder data, streamlining the content filling process. <a class="yt-timestamp" data-t="00:30:44">[00:30:44]</a> It works well in conjunction with `Select Similar Layers` (right-click -> `Select Similar Layers` -> `By Name`) to quickly select and update multiple elements. <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>
*   **Noise and Texture**: Used for adding subtle visual noise or grain to elements. <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>

### Keyboard Shortcuts
*   `F`: Create a Frame. <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>
*   `Shift + A`: Convert selection to Auto Layout. <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>
*   `Command + D`: Duplicate. <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>
*   `Command + K`: Open the quick actions menu for plugins. <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>
*   `R`: Draw a Rectangle. <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>
*   `Number Keys (0-9)`: Adjust opacity of selected element (e.g., `6` for 60%, `0` for 100%, `05` for 5%). <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>
*   `Command + Left/Right Bracket`: Move selected layer down/up in the layer tree. <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>
*   `Enter`: Drill into elements within a frame. <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>
*   `Shift + Enter`: Move back up the layer tree. <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>
*   `Q`: Toggle Multi-edit variants mode for editing component variants simultaneously. <a class="yt-timestamp" data-t="00:27:07">[00:27:07]</a>
*   `T`: Create a Text layer. <a class="yt-timestamp" data-t="00:27:35">[00:27:35]</a>

### Other Practices
*   **Design from Abundance**: Collect inspiration constantly in a database (e.g., Notion) to build an internal library of ideas, rather than starting from a blank page. <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>
*   **Design with Buildability in Mind**: Consider how components will be engineered, particularly with web technologies like CSS Flexbox and Tailwind CSS. <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a> Figma's [[using_components_and_auto_layout in Figma | Auto Layout]] inherently promotes this. <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>
*   **Use Real-Time Preview**: Keep the Figma file open on a separate device (e.g., laptop) in prototype mode to see the design at 1x scale while making changes on the primary monitor. <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>

## Figma in the Broader Prototyping Landscape

Figma excels at being generative and exploring diverse visual ideas, allowing for quick iteration and throwing "paint at the wall." <a class="yt-timestamp" data-t="00:35:53">[00:35:53]</a> It functions like a "piece of paper and a pencil," ideal for sketching and initial concepts. <a class="yt-timestamp" data-t="00:37:13">[00:37:13]</a>

However, for final implementation and deployment, tools like [[prototyping_tools_like_cursor_and_vzer | Vzer]] or Framer, which are more code-based, may be preferred. <a class="yt-timestamp" data-t="00:36:26">[00:36:26]</a> While Figma is best for divergent exploration, Framer is used for building and refining the "final five to ten percent" of the design. <a class="yt-timestamp" data-t="00:36:45">[00:36:45]</a>

The distinction between high-fidelity design in Figma and high-fidelity code is blurring with the rise of AI-driven tools, suggesting that Figma's role might shift further towards lower-fidelity exploration in the future. <a class="yt-timestamp" data-t="00:38:09">[00:38:09]</a>

The best way to learn Figma is by actively using the tool, getting your hands dirty, and experimenting. <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>