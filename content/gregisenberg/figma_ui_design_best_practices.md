---
title: Figma UI design best practices
videoId: XoOx5xPdv4M
---

From: [[gregisenberg]] <br/> 

Figma is a powerful tool for [[design and user interface considerations in web apps | UI design]], allowing for rapid iteration and exploration of visual ideas <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>. This article outlines best practices and tips for using Figma effectively, focusing on workflow, specific features, styling, and [[prototyping and interactivity with Figma | prototyping]].

## Core Concepts & Workflow

*   **Iteration**: A key to good design is trying many things quickly <a class="yt-timestamp" data-t="12:50:00">[12:50:00]</a>. The faster you can explore options, the better your designs will become <a class="yt-timestamp" data-t="12:55:00">[12:55:00]</a>.
*   **Source of Truth**: Maintain one "source of truth" frame for your design, especially when using components, and see updates in real-time on a separate device in prototype mode <a class="yt-timestamp" data-t="11:45:00">[11:45:00]</a>.
*   **Technical Mindset**: Consider how designs will be built. Figma's Auto Layout maps closely to CSS Flexbox, making development easier <a class="yt-timestamp" data-t="14:32:00">[14:32:00]</a>.
*   **Inspiration**: Constantly gather [[inspiration_and_iteration_in_design | inspiration]]. Maintain a database (e.g., Notion) of liked designs, categorizing them and asking why you like certain elements <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>. This approach is akin to "writing from abundance" <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>. If stuck, paste inspirational images into Figma and recreate parts <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>.
*   **Metadata Thinking**: Approach design by considering the metadata available (e.g., title, name, length, price) <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>.

## Key Figma Features & Shortcuts

### Frames (`F`)
*   Frames are fundamental containers in Figma, similar to CSS `div` elements <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>. Use `F` to create a new frame <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.

### Components
*   **Speed Mechanism**: [[utilizing_components_and_auto_layout_in_figma | Components]] are powerful for quick iteration. Create components early, even from an empty frame, to avoid repeating work <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a>. This ensures changes to the main component propagate to all instances <a class="yt-timestamp" data-t="04:06:00">[04:06:00]</a>.
*   **Variants**: Use variants (found via "Add variant" in the top right) to define different states of a component, such as a hover state <a class="yt-timestamp" data-t="23:27:00">[23:27:00]</a>.
*   **Multi-Edit (`Q`)**: To make changes to multiple component variants simultaneously, use multi-edit mode by pressing `Q` <a class="yt-timestamp" data-t="27:04:00">[27:04:00]</a>.

### Auto Layout (`Shift + A`)
*   Auto Layout organizes elements dynamically, functioning like Flexbox in CSS <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>.
*   It simplifies controlling spacing between elements <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>.
*   **Best Practice**: Prioritize building with Auto Layout, as it makes designs easier to translate to code compared to manually positioning elements (which is akin to absolute positioning in CSS) <a class="yt-timestamp" data-t="15:05:00">[15:05:00]</a>.
*   Press `Shift + A` on a selected frame or group to apply Auto Layout <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>.

### Navigation Shortcuts
*   `Enter`: Drill into layers in the canvas <a class="yt-timestamp" data-t="15:41:00">[15:41:00]</a>.
*   `Shift + Enter`: Move back up the layer tree <a class="yt-timestamp" data-t="15:46:00">[15:46:00]</a>.
*   `Command + [ (`Left Bracket)`/`] (`Right Bracket)`: Move selected layers down/up in the layer tree <a class="yt-timestamp" data-t="17:56:00">[17:56:00]</a>.

## Styling & Visual Improvements

*   **Opacity (Number Keys)**: Quickly adjust layer opacity by typing numbers (`1` for 10%, `6` for 60%, `0` for 100%) <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>.
*   **Images**: Use `R` to draw a rectangle, then paste an image from your clipboard to fill it <a class="yt-timestamp" data-t="08:58:00">[08:58:00]</a>.
*   **Remove Background**: Use `Command + K` (quick actions) and search "remove background" to process images <a class="yt-timestamp" data-t="09:30:00">[09:30:00]</a>.
*   **Lighting & Blur**: Add rectangles with a color fill, move them to the back, and apply "Layer blur" from the effects panel to create interesting lighting <a class="yt-timestamp" data-t="17:38:00">[17:38:00]</a>.
*   **Blend Modes**: Experiment with blend modes. "Luminosity" (at the bottom of the blend mode dropdown) is commonly used to tint black and white images with underlying colors <a class="yt-timestamp" data-t="18:45:00">[18:45:00]</a>.
*   **Noise & Texture**: Add a rectangle, set its constraints to cover the entire area, and apply a subtle "Noise" plugin effect <a class="yt-timestamp" data-t="19:43:00">[19:43:00]</a>.
*   **Spacing Values**: When in doubt for spacing or padding, use multiples of eight pixels, which aligns well with modern web development frameworks like Tailwind CSS <a class="yt-timestamp" data-t="16:53:00">[16:53:00]</a>.
*   **Inner Shadows**: Apply inner shadows (from the effects panel) with white or dark colors and adjust opacity to create a subtle rounded, 3D, or "lighting over the edge" feel, especially effective for corners <a class="yt-timestamp" data-t="33:22:00">[33:22:00]</a>. This is a subtle but impactful visual effect common in polished designs <a class="yt-timestamp" data-t="34:36:00">[34:36:00]</a>.

## [[prototyping_and_interactivity_with_figma | Prototyping & Interactivity]]

*   **Hover States**: Create a component variant for your hover state. In Prototype mode, drag a connection from the default state to the hover state, set the interaction to "While hovering," and choose "Smart animate" for smooth transitions <a class="yt-timestamp" data-t="23:27:00">[23:27:00]</a>.
*   **Smart Animate**: Always use "Smart animate" (not "Instant") for smooth transitions between states, creating a better user experience <a class="yt-timestamp" data-t="24:53:00">[24:53:00]</a>. "Gentle" easing is a good default <a class="yt-timestamp" data-t="25:01:00">[25:01:00]</a>.

## [[figma_plugins_and_their_uses | Figma Plugins]]

While Figma's built-in features are robust, plugins can enhance specific workflows:
*   **Icons**:
    *   **Phosphor**: A favored plugin for beautiful, consistent icons <a class="yt-timestamp" data-t="13:23:00">[13:23:00]</a>. Access via `Command + K` and search "Phosphor" <a class="yt-timestamp" data-t="13:26:00">[13:26:00]</a>.
*   **Visual Effects**:
    *   **Smooth Shadow**: Creates complex, realistic shadows (multiple layers) that are difficult to achieve manually <a class="yt-timestamp" data-t="25:57:00">[25:57:00]</a>. Offers easing curves and alpha control <a class="yt-timestamp" data-t="26:12:00">[26:12:00]</a>.
    *   **Noise & Texture**: Adds graininess and other visual effects for added depth <a class="yt-timestamp" data-t="20:10:00">[20:10:00]</a>.
*   **Workflow Enhancements**:
    *   **Destroyer**: Removes all components within a selected frame, "freezing" that iteration in time. Useful for saving design progress at different stages <a class="yt-timestamp" data-t="10:11:00">[10:11:00]</a>.
    *   **Content Reel**: Populates designs with diverse content (images, avatars, text). Can be used in conjunction with "Select similar layers" <a class="yt-timestamp" data-t="30:44:00">[30:44:00]</a>.
    *   **Select Similar Layers**: A native Figma plugin (or feature) that allows selecting layers with similar properties (e.g., by name) to apply bulk changes <a class="yt-timestamp" data-t="31:22:00">[31:22:00]</a>.

## Figma in the Broader Design Ecosystem

*   **Comparison with AI Tools (e.g., V0)**: While AI tools like V0 offer templated solutions, Figma excels at generative design and exploring divergent ideas without limitations <a class="yt-timestamp" data-t="35:35:00">[35:35:00]</a>. Figma allows pushing visual boundaries and figuring out what you truly want to make <a class="yt-timestamp" data-t="36:12:00">[36:12:00]</a>.
*   **Integration with Development Tools (e.g., Framer)**: Designers may start with Figma to explore a wide array of ideas ("throw paint at the wall") <a class="yt-timestamp" data-t="36:31:00">[36:31:00]</a>. Once satisfied, they might transition to a code-based tool like Framer to build out the final design and other pages, achieving the last 5-10% of polish in the actual medium <a class="yt-timestamp" data-t="36:42:00">[36:42:00]</a>.
*   **Future of Design Tools**: The lines between high-fidelity design (Figma) and high-fidelity code are blurring. Figma may evolve to be used earlier in the process for lower-fidelity exploration, with AI tools handling code generation <a class="yt-timestamp" data-t="38:09:00">[38:09:00]</a>.

## Learning Figma
*   The best way to learn Figma is to get your hands dirty and start experimenting. Open a new file, draw a frame, and begin exploring the tools <a class="yt-timestamp" data-t="39:27:00">[39:27:00]</a>.