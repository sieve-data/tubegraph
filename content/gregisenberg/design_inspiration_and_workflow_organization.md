---
title: Design inspiration and workflow organization
videoId: XoOx5xPdv4M
---

From: [[gregisenberg]] <br/> 
In the realm of design, particularly within tools like Figma, two crucial elements contribute to efficiency and quality: continuous inspiration and streamlined workflow organization. This approach emphasizes not just creating, but also collecting and refining ideas through systematic practices.

## Design Inspiration: A Continuous Process

Looking for inspiration should be a constant activity for designers <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>. Rather than starting from a blank page, designers should build a personal database of ideas, similar to "writing from abundance" as described by David Perell <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>.

### Methods for Collecting and Using Inspiration
*   **Notion Database:** Maintain a Notion database to continuously dump, categorize, and organize design inspirations <a class="yt-timestamp" data-t="05:20:00">[05:20:00]</a>.
*   **Direct Recreation in Figma:** When starting a new design or if ideas are scarce, directly paste images from your inspiration collection into Figma and recreate parts of them, adapting them to new contexts <a class="yt-timestamp" data-t="06:02:00">[06:02:00]</a>.
*   **Observational Learning:** Actively notice what you like in designs and consistently ask yourself why you like certain details <a class="yt-timestamp" data-t="07:42:00">[07:42:00]</a>.
*   **Collecting, Not Just Creating:** Effective designers are collectors of design, not just creators <a class="yt-timestamp" data-t="07:34:00">[07:34:00]</a>. This discipline significantly eases the design process, preventing feelings of "shooting in the dark" <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>.

## Figma Workflow Organization

Efficient workflow in Figma is key to rapidly iterating and refining designs. Several [[best_practices_for_designing_in_figma | best practices for designing in Figma]] can streamline this process.

### Core Concepts and Tools

*   **Frames (`F` key):** Act as primary containers for any design element, functioning similarly to a CSS `div` <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.
*   **Components:** Utilize components from the very first step, even before content is added, as "hacky speed mechanisms" to avoid repetitive work <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>, <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>. The goal is to minimize the "knobs" needing adjustment by having one primary control point for changes <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.
*   **Auto Layout (`Shift A`):** Essential for throwing elements into a stack, resembling CSS Flexbox. This allows for easy control over spacing and dynamic adjustments <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>, <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>. Using Auto Layout in Figma aligns well with frontend development practices, making it easier to build designs in code like Flexbox <a class="yt-timestamp" data-t="15:01:00">[15:01:00]</a>.
*   **Metadata Integration:** Approach design like a spreadsheet, considering all available "metadata" or content elements (e.g., title, instructor name, course length, price) to inform the layout and styling of elements <a class="yt-timestamp" data-t="08:04:00">[08:04:00]</a>.
*   **Number Keys for Opacity:** Use number keys (0-9) to quickly adjust the opacity of selected layers <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>.
*   **Command `K` (Quick Actions):** Access quick actions like "remove background" for images <a class="yt-timestamp" data-t="09:30:00">[09:30:00]</a>.
*   **Command + Bracket Keys (`[`/`]`):** Move layers up and down in the layer tree quickly <a class="yt-timestamp" data-t="17:56:00">[17:56:00]</a>.
*   **Enter/Shift + Enter:** Drill down into or move back up from layers in the canvas <a class="yt-timestamp" data-t="15:41:00">[15:41:00]</a>.
*   **`Q` Key (Multi-Edit Variants):** Enable multi-edit mode for component variants to make changes across all instances simultaneously, avoiding redundant work <a class="yt-timestamp" data-t="27:04:00">[27:04:00]</a>.

### Iteration and Saving Progress

*   **Duplicating Frames (`Command D`):** Duplicate entire frames to save different design iterations. This creates a "bookmark" of the design at a specific point in time <a class="yt-timestamp" data-t="09:59:00">[09:59:00]</a>, <a class="yt-timestamp" data-t="21:05:00">[21:05:00]</a>.
*   **Destroyer Plugin:** After duplicating a frame, run the "Destroyer" plugin (specifically "Destroy instances") to remove all component instances within that new frame. This "freezes" the design, preventing future changes to the original component from affecting this saved iteration <a class="yt-timestamp" data-t="10:16:00">[10:16:00]</a>, <a class="yt-timestamp" data-t="11:14:00">[11:14:00]</a>. This allows for a linear visual history of design evolution <a class="yt-timestamp" data-t="30:31:00">[30:31:00]</a>.
*   **Live Prototype View:** Always keep the design open in prototype mode on a separate screen (e.g., a laptop) at 1x size. This allows for real-time visual feedback while making changes on the primary monitor <a class="yt-timestamp" data-t="11:18:00">[11:18:00]</a>.

### Prototyping and Interaction Design

[[prototyping_and_interaction_design_in_figma | Prototyping and interaction design in Figma]] are crucial for evaluating how designs feel.

*   **Adding Hover States:**
    1.  Make the element a component.
    2.  Add a variant (e.g., "hover" state) by clicking "Add variant" in the top right of the component properties <a class="yt-timestamp" data-t="23:27:00">[23:27:00]</a>.
    3.  Define the visual changes for the hover variant (e.g., increased blur, background pop, border changes) <a class="yt-timestamp" data-t="23:58:00">[23:58:00]</a>.
    4.  In prototype mode, drag a connection from the default state to the hover state.
    5.  Set the interaction trigger to "while hovering" <a class="yt-timestamp" data-t="24:38:00">[24:38:00]</a>.
    6.  Choose "Smart Animate" for a smooth transition, and select an easing preset like "gentle" with a duration (e.g., 400ms) for a good feel <a class="yt-timestamp" data-t="24:53:00">[24:53:00]</a>.
*   **"Smart Animate" vs. "Instant":** Always use "Smart Animate" for smooth transitions between states, as "Instant" can result in a "Herky-jerky" experience <a class="yt-timestamp" data-t="28:50:00">[28:50:00]</a>.

### Visual Improvements and [[aesthetics_in_software_design | Aesthetics in software design]]

*   **Tailwind CSS Values:** When in doubt about spacing or sizing, use values that are multiples of eight, as this often aligns with modern web development frameworks like Tailwind CSS <a class="yt-timestamp" data-t="16:50:00">[16:50:00]</a>.
*   **Lighting and Blur:** Incorporate lighting and blur effects to add visual interest. Create a rectangle, fill it with a color, move it to the back of the layer tree, and apply a "Layer blur" effect <a class="yt-timestamp" data-t="17:30:00">[17:30:00]</a>.
*   **Luminosity Blend Mode:** Use the "Luminosity" blend mode on images to allow underlying colors to bleed through, creating a tinted black-and-white effect <a class="yt-timestamp" data-t="18:45:00">[18:45:00]</a>.
*   **Noise and Texture:** Add a subtle layer of graininess or texture to designs using plugins to enhance visual interest. Create a rectangle, pin it to the edges, move it to the back, and apply a noise plugin like "Noise and Texture" with low opacity <a class="yt-timestamp" data-t="19:43:00">[19:43:00]</a>.
*   **Smooth Shadows:** Use plugins like "Smooth Shadow" to create sophisticated, multi-layer drop shadows that are difficult to achieve manually <a class="yt-timestamp" data-t="25:50:00">[25:50:00]</a>.
*   **Inner Shadows for Depth:** Apply inner shadows, particularly white at the top and darker at the bottom, to create a subtle rounded, 3D curvature effect on corners, mimicking lighting and adding depth <a class="yt-timestamp" data-t="33:08:00">[33:08:00]</a>.

### [[using_plugins_for_enhanced_design_capabilities_in_figma | Using plugins for enhanced design capabilities in Figma]]

Plugins are categorized into two main workflows:

1.  **Visual Effects:**
    *   **Noise and Texture:** For adding graininess or complex shaders <a class="yt-timestamp" data-t="30:01:00">[30:01:00]</a>.
    *   **Smooth Shadow:** For creating beautiful, multi-layer shadows <a class="yt-timestamp" data-t="30:03:00">[30:03:00]</a>.
2.  **Workflow Enhancements:**
    *   **Destroyer:** Essential for "freezing" design iterations by removing component instances <a class="yt-timestamp" data-t="30:27:00">[30:27:00]</a>.
    *   **Content Reel:** Populates designs with various types of content (e.g., avatars, text) from defaults or custom folders <a class="yt-timestamp" data-t="30:44:00">[30:44:00]</a>.
    *   **Select Similar Layers:** Used in conjunction with Content Reel to select all instances of a specific layer type (e.g., all images) to apply bulk changes <a class="yt-timestamp" data-t="31:20:00">[31:20:00]</a>.

Figma itself has incorporated many previously plugin-dependent functionalities, reducing the need for a large plugin repertoire <a class="yt-timestamp" data-t="32:33:00">[32:33:00]</a>.

## Figma vs. Code-Based Tools

Figma is still considered the best place to start design work because it allows for rapid generation and exploration of a wide array of divergent ideas <a class="yt-timestamp" data-t="35:53:00">[35:53:00]</a>. It's like sketching with a pencil on a piece of paper, enabling pure ideation <a class="yt-timestamp" data-t="37:13:00">[37:13:00]</a>.

However, once ideas are solidified, moving to code-based tools like Framer becomes beneficial for the final 5-10% refinement and production <a class="yt-timestamp" data-t="36:26:00">[36:26:00]</a>. Tools like Vercel's v0, while offering templated or "productized" results, are useful for quick, predefined outputs <a class="yt-timestamp" data-t="37:37:00">[37:37:00]</a>.

The distinction between high-fidelity design in Figma and high-fidelity code is blurring <a class="yt-timestamp" data-t="38:09:00">[38:09:00]</a>. This suggests that Figma might shift to a more "lower-fidelity" role for early idea exploration, with AI tools handling the high-fidelity code generation directly <a class="yt-timestamp" data-t="38:18:00">[38:18:00]</a>.

## Learning Design

The best way to learn design, especially in Figma, is to actively engage with the tools <a class="yt-timestamp" data-t="39:29:00">[39:29:00]</a>. Simply open a new file, type `F` on the keyboard, and start drawing to begin the hands-on learning process <a class="yt-timestamp" data-t="39:43:00">[39:43:00]</a>.