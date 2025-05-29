---
title: Figma UI design basics and live design session
videoId: XoOx5xPdv4M
---

From: [[gregisenberg]] <br/> 

This article provides an overview of Figma UI design best practices and workflow, demonstrated through a live design session focused on creating course cards for a marketplace.

## Starting a Design Session
A live design session in Figma can demonstrate the process of iterating on an idea and applying best practices <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. The goal is to show considerations made while building, visual improvements, and basic [[prototyping_and_adding_interactivity_in_figma | prototyping]] <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. The example used is designing a course page for dive.club to list design courses with affiliate agreements <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

## Core Figma Concepts

### Frames and Containers
To start a design in Figma, you create a "frame" by hitting the `F` key <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. A frame acts as a container, similar to a CSS `div`, where you can place other elements <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. For example, a "course card" would be treated as a frame <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

### [[using_components_and_auto_layout_in_figma | Components and Auto Layout]]
Using components early in the design process, even before adding content, is a hack for moving quickly in Figma <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. Components help minimize the amount of adjustments needed later by providing a single point of control <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

Auto Layout is created by hitting `Shift + A` and allows you to throw any elements into a stack, which functions similarly to Flexbox in CSS <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. This feature allows control over spacing and manipulation of designs <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. Designing with Auto Layout in Figma makes it very easy to build components in Flexbox in code <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>. Randomly positioning elements without Auto Layout is akin to absolute positioning in CSS, which is generally to be avoided <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.

> [!TIP] Keyboard Shortcuts
> *   `F`: Create a frame <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>
> *   `Shift + A`: Create an Auto Layout <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>
> *   Number keys (`0-9`): Change opacity (e.g., `6` for 60%, `0` for 100%) <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>
> *   `R`: Draw a rectangle <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>
> *   `Command + K`: Open the quick action menu to search for commands or run plugins <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>
> *   `Command + [ (`left bracket`): Move selected layer down in the layer tree <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>
> *   `Enter`: Drill into layers in the canvas <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>
> *   `Shift + Enter`: Move back up the layer tree <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>
> *   `Q`: Toggle multi-edit variants mode for components <a class="yt-timestamp" data-t="00:27:07">[00:27:07]</a>
> *   `T`: Add text <a class="yt-timestamp" data-t="00:27:35">[00:27:35]</a>

## Design Process and Iteration

### [[inspiration_and_ideation_process_for_ui_design | Inspiration and Ideation]]
Good designers are often collectors of design, not just creators <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. Keeping a database of saved inspiration, like a Notion database, helps to constantly gather and categorize design ideas <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. When starting a design with no clear idea, a common first step is to paste in images from inspiration sources and then recreate or adapt parts of them <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. It's beneficial to constantly ask "why" you like something you see <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

### Iteration Workflow
The design process often involves trying many different approaches rapidly <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>. A common workflow for iteration is to duplicate an entire frame (`Command + D`), then use the "Destroyer" plugin to remove all components within the duplicated frame, effectively "freezing" that iteration in time <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. This allows for continuous changes on the original frame without affecting previous versions <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.

> [!NOTE] Designing in one frame
> It's helpful to always design in one main frame, and have the design open at 1x scale on a separate device (like a laptop in prototype mode) to see updates in real-time <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.

## Adding Visual Interest

### Images and Background Removal
Images can be added by drawing a rectangle (`R`) and then filling it <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. Figma allows users to remove backgrounds from images using the `Command + K` quick action menu <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.

### Lighting, Blur, and Blend Modes
Adding visual interest can involve playing with lighting and blur <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>. A rectangle filled with a color and set to "Layer Blur" under effects, then adjusted for opacity, can create an interesting visual effect <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>.

Blend modes, found under "Apply Blend Mode," can also enhance visuals <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>. "Luminosity" is a commonly used blend mode that allows colors below to bleed through, creating a tinted black and white effect <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>.

### Noise and Texture
Adding noise and texture can significantly spice up designs, especially with gradients and lighting <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>. The "Noise & Texture" plugin allows users to add graininess and other visual effects to elements <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>.

### Shadows (Inner and Drop Shadows)
To create a lifting or popping effect, "Smooth Shadow" is a recommended plugin that creates beautiful, multi-layered shadows <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>.

Inner shadows can add depth and a rounded, 3D feel to corners <a class="yt-timestamp" data-t="00:33:12">[00:33:12]</a>. By adding an inner shadow (e.g., white at the top, darker at the bottom) and tweaking its offset and blur, a subtle lighting effect can be achieved, making elements appear to curve or bend <a class="yt-timestamp" data-t="00:33:43">[00:33:43]</a>. This technique is a common trend in modern designs for creating visual interest <a class="yt-timestamp" data-t="00:34:50">[00:34:50]</a>.

## [[prototyping_and_adding_interactivity_in_figma | Prototyping and Adding Interactivity]]
To add interactivity like a hover state, you first make an element a component, then add a "variant" (e.g., a "hover" variant) <a class="yt-timestamp" data-t="00:23:27">[00:23:27]</a>. In the prototype mode, you link the default component to its hover variant using a "while hovering" interaction <a class="yt-timestamp" data-t="00:24:36">[00:24:36]</a>. Using "Smart Animate" with a "gentle" easing (around 400ms) creates a smooth transition between states <a class="yt-timestamp" data-t="00:24:53">[00:24:53]</a>.

## [[plugins_and_tools_for_enhancing_figma_design_workflow | Plugins and Tools]]
While many plugins exist, a focused set can be very effective:
*   **Visual Effects:**
    *   **Noise & Texture:** For adding graininess and other visual effects <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>.
    *   **Smooth Shadow:** To create beautiful, multi-layered shadows <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>.
*   **Workflow Enhancements:**
    *   **Destroyer:** Removes components from a frame, effectively "freezing" an iteration <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
    *   **Phosphor:** A popular icon library plugin, ensuring consistent icon styles <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.
    *   **Content Reel:** Populates designs with various content like avatars, names, or custom folders of content <a class="yt-timestamp" data-t="00:30:44">[00:30:44]</a>.
    *   **Similar Layer:** Used in conjunction with Content Reel, this plugin helps select all layers with similar properties (e.g., images by name) for bulk changes <a class="yt-timestamp" data-t="00:31:20">[00:31:20]</a>.

> [!NOTE] Fewer Plugins, More Built-in Features
> Figma has incorporated many workflow enhancements that used to require plugins directly into the core application, reducing the need for a large plugin repertoire <a class="yt-timestamp" data-t="00:32:40">[00:32:40]</a>.

## Figma's Role in Modern Design
Figma remains excellent for generative design and rapidly exploring divergent visual ideas, allowing for quick iteration and throwing ideas at the wall <a class="yt-timestamp" data-t="00:35:53">[00:35:53]</a>. Unlike tools like [[building_and_designing_the_user_interface_with_ai_assistance | V0]], Figma allows for more exploration and pushing of visual boundaries, as AI-assisted tools may feel more templated <a class="yt-timestamp" data-t="00:36:06">[00:36:06]</a>.

However, the design process is evolving. After exploring ideas in Figma, designers may move to tools like Framer to build the final product and refine it, especially for web design <a class="yt-timestamp" data-t="00:36:26">[00:36:26]</a>. Figma can be seen as the "sketchbook" (pencil and paper) for ideas, while code-based tools are the "word processor" for more productized output <a class="yt-timestamp" data-t="00:37:13">[00:37:13]</a>. The line between high-fidelity design in Figma and high-fidelity code is blurring, suggesting Figma might move earlier into the low-fidelity exploration phase in the future <a class="yt-timestamp" data-t="00:38:09">[00:38:09]</a>.

## Learning Figma
The best way to learn Figma is to get hands-on and start experimenting <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>. Simply opening a new file, typing `F`, and drawing a frame is a good starting point <a class="yt-timestamp" data-t="00:39:43">[00:39:43]</a>.

For more information, you can find the designer on Twitter [@ridoredesign](https://twitter.com/ridoredesign) and learn about their projects at [dive.club](https://dive.club/) <a class="yt-timestamp" data-t="00:38:49">[00:38:49]</a>.