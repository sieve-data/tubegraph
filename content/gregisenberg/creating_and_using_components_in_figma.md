---
title: Creating and using components in Figma
videoId: XoOx5xPdv4M
---

From: [[gregisenberg]] <br/> 

This article explores [[best_practices_for_designing_in_figma | best practices for designing in Figma]], focusing on creating and utilizing components for efficient and iterative design. It includes insights from a live design session, demonstrating practical techniques for building a course marketplace page on the `dive.club` website <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>.

## Starting with Frames and Components
Figma's fundamental building block for design is the **Frame**, which acts like a container, similar to a CSS `div` <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>. You create a frame by hitting `F` on the keyboard <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.

A powerful hack for rapid design in Figma is to immediately turn your design into a **Component**, even before adding content <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>. Components serve as "hacky speed mechanisms" to avoid doing the same thing twice, allowing for quick, single-point changes that propagate across all instances <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.

### Leveraging Auto Layout
**Auto Layout** (created by hitting `Shift A`) is crucial for organizing content within frames and components <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>. It functions like a stack or CSS Flexbox, enabling designers to control spacing and arrangement dynamically <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>. Building designs using Auto Layout makes them easily translatable to code, as it maps directly to Flexbox properties <a class="yt-timestamp" data-t="15:05:00">[15:05:00]</a>.

## Design Process and Inspiration
Effective design in Figma involves constant inspiration seeking <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>. Keeping a Notion database of design ideas and examples (like the concept of "writing from abundance" by David Perell) helps maintain a rich mental library <a class="yt-timestamp" data-t="05:20:00">[05:20:00]</a>. When starting a new design, designers can paste inspiration images directly into Figma and recreate elements from them, adapting them in different ways <a class="yt-timestamp" data-t="06:02:00">[06:02:00]</a>. Good designers are "collectors of design" rather than just "creators" <a class="yt-timestamp" data-t="07:34:00">[07:34:00]</a>.

When designing, consider the "metadata" of the content (e.g., title, instructor name, course length, price) as if filling a spreadsheet <a class="yt-timestamp" data-t="08:04:00">[08:04:00]</a>.

### Quick Styling Tips
*   **Opacity**: Use number keys (1-9 for 10%-90%, 0 for 100%, 05 for 5%) to quickly adjust opacity <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>.
*   **Image Placement**: Hit `R` to draw a rectangle, then copy an image from your clipboard to fill it <a class="yt-timestamp" data-t="08:58:00">[08:58:00]</a>.
*   **Remove Background**: Use `Command K` and type "remove background" to apply this effect <a class="yt-timestamp" data-t="09:30:00">[09:30:00]</a>.
*   **Tailwind CSS Values**: For spacing and sizing, use multiples of 8, which aligns well with [[incorporating_tailwind_css_and_design_components | Tailwind CSS]] syntax <a class="yt-timestamp" data-t="16:56:00">[16:56:00]</a>.
*   **Layer Ordering**: Use `Command + [` (left bracket) to move elements down the layer tree and `Command + ]` (right bracket) to move them up <a class="yt-timestamp" data-t="17:56:00">[17:56:00]</a>.
*   **Blend Modes**: Experiment with blend modes for visual interest, especially `Luminosity`, which tints images with underlying colors <a class="yt-timestamp" data-t="18:45:00">[18:45:00]</a>.
*   **Inner Shadows**: Add an inner shadow to create a subtle rounded, 3D effect on corners, making designs appear to have more depth and texture <a class="yt-timestamp" data-t="33:08:00">[33:08:00]</a>.

## [[Using plugins for enhanced design capabilities in Figma | Utilizing Plugins for Enhanced Design]]
Plugins significantly enhance Figma's capabilities, particularly for visual effects and workflow automation <a class="yt-timestamp" data-t="29:55:00">[29:55:00]</a>.
*   **Destroyer**: This plugin (`Command K` -> "Destroy instances") freezes components in time by removing all component instances within a frame, allowing designers to save iterations and revert to previous states without affecting the main component <a class="yt-timestamp" data-t="10:22:00">[10:22:00]</a>. This workflow creates a "left to right" design evolution <a class="yt-timestamp" data-t="30:31:00">[30:31:00]</a>.
*   **Phosphor**: A go-to plugin for high-quality, consistent icons <a class="yt-timestamp" data-t="13:23:00">[13:23:00]</a>.
*   **Smooth Shadow**: Generates beautiful, multi-layered shadows that are difficult to create manually <a class="yt-timestamp" data-t="25:57:00">[25:57:00]</a>.
*   **Noise and Texture**: Adds graininess and other visual effects to designs <a class="yt-timestamp" data-t="20:10:00">[20:10:00]</a>.
*   **Content Reel**: Excellent for populating designs with realistic content like avatars or text, supporting custom folders of content <a class="yt-timestamp" data-t="30:44:00">[30:44:00]</a>.
*   **Select Similar Layers**: Used in conjunction with Content Reel, it allows for selecting and bulk-changing specific elements across many components <a class="yt-timestamp" data-t="31:22:00">[31:22:00]</a>.

While many plugins exist, Figma's native features (like multi-edit mode) have reduced the need for a large plugin repertoire <a class="yt-timestamp" data-t="32:33:00">[32:33:00]</a>.

## [[Prototyping and interaction design in Figma | Prototyping and Interaction Design]]
Figma allows for quick prototyping to test user interactions and visual feel <a class="yt-timestamp" data-t="22:52:00">[22:52:00]</a>.
*   **Component Variants**: Create a `hover` variant for a component <a class="yt-timestamp" data-t="23:27:00">[23:27:00]</a>.
*   **Prototyping Mode**: In the "Prototype" tab, drag a connection from the default state to the hover state <a class="yt-timestamp" data-t="24:27:00">[24:27:00]</a>.
*   **Interaction**: Set the interaction to "While hovering" <a class="yt-timestamp" data-t="24:41:00">[24:41:00]</a>.
*   **Animation**: Use "Smart Animate" for smooth transitions between states (avoid "Instant" for better user experience) <a class="yt-timestamp" data-t="24:53:00">[24:53:00]</a>. Experiment with easing presets like "Gentle" and adjust duration (e.g., 400ms) <a class="yt-timestamp" data-t="25:01:00">[25:01:00]</a>.
*   **Multi-Edit Variants**: Use `Q` to enter "multi-edit variants" mode, allowing simultaneous changes across all component variants <a class="yt-timestamp" data-t="27:04:00">[27:04:00]</a>. This ensures consistency and efficiency when refining interactive elements <a class="yt-timestamp" data-t="27:50:00">[27:50:00]</a>.
*   **Layer Navigation**: Use `Enter` to drill into layers and `Shift Enter` to move back up <a class="yt-timestamp" data-t="15:41:00">[15:41:00]</a>.
*   **Real-time Preview**: Always view designs at 1x scale on a separate monitor or laptop in prototype mode to see how they truly feel <a class="yt-timestamp" data-t="11:26:00">[11:26:00]</a>.

## Figma's Role in Modern Web Design
Figma excels as a **generative tool** for quickly exploring and iterating on a wide array of visual ideas <a class="yt-timestamp" data-t="35:53:00">[35:53:00]</a>. While tools like VZero or [[building_websites_with_webflow | Framer]] can provide more "templated" or "productized" outputs, Figma allows for pushing creative boundaries and divergent thinking <a class="yt-timestamp" data-t="36:06:00">[36:06:00]</a>.

The speaker suggests that Figma is like a "pencil" for sketching ideas, while tools like VZero or Microsoft Word are more like "word processors" for refined, standardized output <a class="yt-timestamp" data-t="37:13:00">[37:13:00]</a>. Figma's strong connection to front-end development, especially through features like Auto Layout, makes it ideal for designers who understand how code works <a class="yt-timestamp" data-t="14:49:00">[14:49:00]</a>.

The line between high-fidelity design in Figma and high-fidelity code is expected to blur further with advancements in software creation <a class="yt-timestamp" data-t="38:09:00">[38:09:00]</a>. Figma might shift to an even earlier, lower-fidelity exploration phase as AI tools automate high-fidelity code generation <a class="yt-timestamp" data-t="38:18:00">[38:18:00]</a>.

To learn more, you can find the speaker on Twitter at `ridoredesign` or explore the podcast at `dive.club` <a class="yt-timestamp" data-t="38:49:00">[38:49:00]</a>. The best way to learn Figma is to simply "get your hands dirty" and start playing with the tools <a class="yt-timestamp" data-t="39:27:00">[39:27:00]</a>.