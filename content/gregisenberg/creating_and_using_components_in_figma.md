---
title: Creating and using components in Figma
videoId: XoOx5xPdv4M
---

From: [[gregisenberg]] <br/> 

Figma is a powerful design tool that enables designers to create and iterate on user interfaces efficiently. A core feature facilitating this efficiency is the use of components. Components are reusable UI elements that help maintain consistency and accelerate the design process by allowing changes to propagate across multiple instances <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>, <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

## Creating a Component

The foundation of any design in Figma begins with a frame, which acts as a container for your design elements, similar to a CSS `div` <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

1.  **Draw a Frame**: Hit `F` on your keyboard and draw out a frame <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. This frame will be your initial design element, e.g., a "course card" <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
2.  **Convert to Component**: Even at the earliest stage, before adding any content, convert this frame into a component <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. This is done by selecting the frame and clicking the "Create Component" icon (usually a four-diamond shape) in the toolbar, or using the keyboard shortcut `Ctrl + Alt + K` (Windows) / `Cmd + Option + K` (Mac).
3.  **Duplicate Instances**: Once it's a component, duplicate it multiple times to create instances <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. Place these instances within an [[prototyping_and_animations_in_figma | Auto Layout]] container (created by hitting `Shift + A`) <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>, which allows you to control spacing and arrangement easily <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

## Benefits and Workflow Enhancements

Using components, even for early exploration, significantly enhances [[figma_plugins_and_workflow_enhancements | creative workflows and tools in AI design]]:

*   **Efficiency**: You never have to do the same thing twice. Changes made to the main component propagate to all its instances automatically <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>, <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   **Rapid Iteration**: This approach allows designers to quickly iterate on ideas and explore different styles without manually updating each element <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>, <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
*   **Consistency**: Ensures visual and functional consistency across the design, mapping well to front-end development principles like Flexbox in CSS <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>, <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.

## Styling Components and Variants

### Adding Content and Basic Styling
Content can be added to the main component, and it will appear in all instances. This includes text, images, and other design elements <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. Basic styling like opacity (using number keys `1-0` for 10-100% opacity) <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>, colors, and font styles can be applied <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

### Incorporating Visual Effects
[[figma_design_techniques | Figma design techniques]] include enhancing visual interest using:
*   **Images**: Add images to components (e.g., by drawing a rectangle `R` and pasting an image) <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. Figma even has a feature to remove backgrounds from images <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
*   **Lighting and Blur**: Use blurred rectangles with low opacity and blend modes (e.g., Luminosity for tinted black and white effects) to create subtle lighting and depth <a class="yt-timestamp" data-t="00:17:38">[00:17:38]</a>, <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>, <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>.
*   **Noise and Texture**: Add a subtle grainy texture using the "Noise and Texture" plugin to add depth and visual interest <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>, <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>.
*   **Smooth Shadows**: For realistic lifting effects, use the "Smooth Shadow" plugin <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>. Good shadows are often not a single layer <a class="yt-timestamp" data-t="00:25:52">[00:25:52]</a>.
*   **Inner Shadows**: A subtle but powerful technique for adding depth and a "rounded" or "bending" feel to corners, making elements appear as if light is shining over their edges <a class="yt-timestamp" data-t="00:33:11">[00:33:11]</a>, <a class="yt-timestamp" data-t="00:34:07">[00:34:07]</a>.

### Prototyping with Variants (Hover States)
Components are essential for [[interactive_prototyping_tools_for_app_development | interactive prototyping tools for app development]]. To add interactivity like a hover state:

1.  **Add Variant**: Select your main component and click "Add Variant" in the top right <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>. Name the variants (e.g., "Default" and "Hover") <a class="yt-timestamp" data-t="00:23:45">[00:23:45]</a>.
2.  **Style the Variant**: Make the desired visual changes to the "Hover" variant (e.g., increase blur, background, or border opacity) <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>.
3.  **Link with Prototype**: Switch to "Prototype" mode in the top right <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a>. Drag the blue dot from the "Default" variant to the "Hover" variant <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>.
4.  **Set Interaction**: Choose "While Hovering" as the trigger <a class="yt-timestamp" data-t="00:24:38">[00:24:38]</a>.
5.  **Choose Animation**: Select "Smart Animate" for a smooth transition, and adjust easing (e.g., "Gentle") and duration (e.g., 400ms) <a class="yt-timestamp" data-t="00:24:53">[00:24:53]</a>.
6.  **Test**: Open the prototype mode to see how the hover state feels <a class="yt-timestamp" data-t="00:25:09">[00:25:09]</a>.

### Multi-Edit Variants
Figma's multi-edit feature (hit `Q`) allows designers to make changes to all variants of a component simultaneously <a class="yt-timestamp" data-t="00:27:03">[00:27:03]</a>. This is useful for consistent structural changes, like adjusting padding or repositioning elements across all states <a class="yt-timestamp" data-t="00:28:08">[00:28:08]</a>.

## Component-Related Plugins

While Figma's native features are robust, some plugins further enhance component workflows:

*   **Destroyer**: This plugin (`Command + K`, then search "Destroyer") allows you to "destroy" or detach instances from their main components within a frame <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>. This freezes specific instances in time, preserving them as bookmarks in your iteration flow without being affected by further changes to the main component <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>, <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.
*   **Content Reel**: Useful for populating designs with realistic content like avatars or text, especially when working with many instances <a class="yt-timestamp" data-t="00:30:44">[00:30:44]</a>.
*   **Select Similar Layers**: Helps select all instances of a specific layer type (e.g., all images by name) to apply changes or populate with content via Content Reel <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>.

While many plugins exist, focusing on a few for specific visual effects or workflow enhancements is often sufficient <a class="yt-timestamp" data-t="00:29:50">[00:29:50]</a>, <a class="yt-timestamp" data-t="00:32:29">[00:32:29]</a>.

## Figma's Role in Modern Design

Figma excels at being a generative tool for exploring and expressing a wide array of visual ideas <a class="yt-timestamp" data-t="00:35:53">[00:35:53]</a>. It allows designers to "throw paint at the wall" and iterate rapidly <a class="yt-timestamp" data-t="00:36:38">[00:36:38]</a>. Compared to tools like VZ (which tend to provide more templated or productized designs) <a class="yt-timestamp" data-t="00:36:06">[00:36:06]</a>, Figma offers greater freedom for pushing creative boundaries <a class="yt-timestamp" data-t="00:36:12">[00:36:12]</a>.

However, the design landscape is evolving. While Figma remains an excellent starting point for sketching and exploring high-fidelity UI concepts <a class="yt-timestamp" data-t="00:37:13">[00:37:13]</a>, the increasing capabilities of [[drafting_app_concepts_with_minimal_coding_knowledge | code-based tools]] like Framer mean that designers may transition to these tools for final polish and building functional pages once core ideas are solidified <a class="yt-timestamp" data-t="00:36:26">[00:36:26]</a>, <a class="yt-timestamp" data-t="00:36:51">[00:36:51]</a>. The distinction between high-fidelity design in Figma and high-fidelity code is blurring <a class="yt-timestamp" data-t="00:38:11">[00:38:11]</a>.

Ultimately, getting hands-on with Figma and experimenting with its tools is the best way to learn and build confidence <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>.