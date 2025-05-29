---
title: Figma design best practices
videoId: XoOx5xPdv4M
---

From: [[gregisenberg]] <br/> 

Figma is a powerful tool for [[design_sprint_for_product_building | product building]], enabling designers to explore and iterate on ideas quickly <a class="yt-timestamp" data-t="00:54:33">[00:54:33]</a>. This article outlines best practices and workflows demonstrated in a live design session, focusing on efficiency, visual appeal, and developer hand-off.

## Core Figma Workflow & Techniques

Effective use of Figma's fundamental features can significantly speed up the design process:

*   **Frames (F key)** Frames act as containers, similar to CSS `div` elements, for organizing design elements <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. Any new "thing" you create in Figma starts with a frame <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   **[[using_components_and_auto_layout_in_figma | Components]] (Early Adoption)** Turn elements into components as a first step, even before adding content <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. This "hacky speed mechanism" allows for quick, global changes from a single "knob," minimizing repetitive tasks <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   **[[using_components_and_auto_layout_in_figma | Auto Layout]] (Shift+A)** Auto Layout functions like CSS Flexbox, enabling efficient stacking and spacing of elements within a container <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. It's crucial for building designs that easily translate to code <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.
*   **Text Styles** Utilize pre-existing basic type scales, which can be derived from popular websites, Polaris, or Tailwind CSS for consistent typography <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   **Opacity (Number Keys)** Quickly adjust the opacity of selected layers by typing numbers on the keyboard (e.g., `6` for 60%, `0` for 100%, `05` for 5%) <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Iteration Workflow**
    *   **Duplicate Frames (Command+D):** Create duplicates of entire frames to save design progress at different stages of iteration <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
    *   **Destroyer Plugin:** Use the "Destroyer" plugin to detach all components within a duplicated frame, "freezing it in time" and allowing for independent exploration of new ideas without affecting previous iterations <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
*   **Navigating the Layer Tree** Use `Enter` to drill into layers on the canvas and `Shift+Enter` to move back up, enabling fast traversal of your design structure <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.
*   **Real-time Prototyping View** Design in one frame while simultaneously viewing the prototype at 1x real size on another monitor (e.g., a laptop) to immediately assess the visual impact of changes <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.
*   **Multi-Edit Variants (Q key)** When editing a component, activate multi-edit mode (`Q`) to make changes that populate across all variants simultaneously, avoiding repetitive edits <a class="yt-timestamp" data-t="00:27:03">[00:27:03]</a>.

## Visual Enhancements

Elevate design aesthetics with subtle visual treatments:

*   **Lighting and Blur (Layer Blur)** Add visual interest by introducing blurred color fills beneath elements, mimicking lighting effects <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>. Use the "Layer Blur" effect in Figma's effects panel <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
*   **Blend Modes (Luminosity)** Apply blend modes like "Luminosity" to images or layers to allow underlying colors to bleed through, creating a tinted black-and-white or unique color effect <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>.
*   **[[plugins_for_figma_design_enhancement | Noise and Texture Plugin]]** Introduce subtle graininess and texture using the "Noise and Texture" plugin to add visual depth <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>.
*   **Borders** Implement subtle borders with low opacity (e.g., 10%) for a clean, interesting separation <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a>.
*   **[[plugins_for_figma_design_enhancement | Smooth Shadow Plugin]]** Instead of manually creating drop shadows, use the "Smooth Shadow" plugin for automatically generated, visually pleasing shadows that suggest elevation <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>.
*   **Inner Shadows** Create a sense of depth and curvature on corners by adding inner shadows. Use white for the top shadow and a darker color (like dark gray or black) for the bottom, adjusting X/Y values and blur to achieve a subtle "lighting over the edge" effect <a class="yt-timestamp" data-t="00:33:11">[00:33:11]</a>.

## [[prototyping_methods_in_figma | Prototyping]]

Quickly bring designs to life with interactivity:

*   **Creating Hover States** For interactive elements like cards, create a component with a "default" variant and a "hover" variant. Design the desired visual changes in the hover state <a class="yt-timestamp" data-t="00:23:27">[00:23:27]</a>.
*   **Smart Animate** Link the default and hover states in Prototype mode using "While Hovering" as the interaction trigger and "Smart Animate" for a smooth transition <a class="yt-timestamp" data-t="00:24:41">[00:24:41]</a>. Use easing presets like "Gentle" and adjust duration (e.g., 400ms) for a polished feel <a class="yt-timestamp" data-t="00:24:59">[00:24:59]</a>.

## Recommended Plugins

While Figma's native capabilities have grown, certain [[plugins_for_figma_design_enhancement | plugins]] enhance workflow and visual effects:

*   **Visual Effects Plugins:**
    *   **Noise and Texture:** For adding graininess and unique textures <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>.
    *   **Smooth Shadow:** For creating realistic, multi-layered shadows <a class="yt-timestamp" data-t="00:30:03">[00:30:03]</a>.
*   **Workflow Plugins:**
    *   **Destroyer:** Essential for detaching components from master instances to save iterative design progress <a class="yt-timestamp" data-t="00:30:29">[00:30:29]</a>.
    *   **Phosphor:** A reliable library for high-quality, consistent icons <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.
    *   **Content Reel:** Populates designs with diverse content (images, text) to quickly fill layouts <a class="yt-timestamp" data-t="00:30:44">[00:30:44]</a>.
    *   **Select Similar Layers:** Use in conjunction with Content Reel to select and update multiple elements of the same type across many components simultaneously <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>.

## Design Philosophy

*   **[[inspiration_and_iteration_in_design | Constant Inspiration & Collection]]** Designers are "collectors of design, not just creators" <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. Maintain a database (e.g., Notion) of liked designs, constantly asking "why" you like certain elements to build an internal library of ideas <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
*   **Iterate Rapidly** The key to good design is trying more ideas than others <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. The faster you can try things, the better your designs will be, as it allows you to move past less effective solutions <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.
*   **Consider Development from the Outset** When designing, think about how the components will be built in code. Figma's [[using_components_and_auto_layout_in_figma | Auto Layout]] inherently maps well to CSS Flexbox, making the hand-off smoother <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>. Aim for values that are multiples of 8, aligning with modern web development frameworks like Tailwind CSS <a class="yt-timestamp" data-t="00:16:53">[00:16:53]</a>.
*   **Figma as a Generative Sketching Tool** Figma excels at rapidly generating and exploring a wide array of divergent visual ideas, acting as a "pencil" for sketching <a class="yt-timestamp" data-t="00:35:53">[00:35:53]</a>. While tools like Vercel's v0 offer "productized" or templated designs, Figma allows for pushing creative boundaries <a class="yt-timestamp" data-t="00:36:06">[00:36:06]</a>. For final polish and production, code-based tools like Framer are often preferred to achieve the last 5-10% of refinement <a class="yt-timestamp" data-t="00:36:26">[00:36:26]</a>.
*   **Hands-on Practice** The best way to learn Figma is to get in there and get your hands dirty <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>. Open a new file, hit `F`, and start drawing <a class="yt-timestamp" data-t="00:39:43">[00:39:43]</a>.