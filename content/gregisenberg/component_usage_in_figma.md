---
title: Component usage in Figma
videoId: XoOx5xPdv4M
---

From: [[gregisenberg]] <br/> 

Figma is a powerful tool for visual design, allowing users to generate ideas and iterate quickly <a class="yt-timestamp" data-t="00:35:53">[00:35:53]</a>. It enables the exploration of divergent ideas and the pushing of visual boundaries, especially when compared to more templated tools like VZero <a class="yt-timestamp" data-t="00:36:03">[00:36:03]</a>. Starting in Figma is often considered the best approach for initiating design projects <a class="yt-timestamp" data-t="00:37:48">[00:37:48]</a>.

## Core Concepts: Frames and Components

At the heart of efficient Figma design are frames and components:

*   **Frames**: A frame is a fundamental container in Figma, similar to a CSS `div` <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. To create a frame, simply hit the 'F' key <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   **Components**: While often associated with comprehensive Design Systems, components in Figma serve as powerful "hacky speed mechanisms" <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. The primary goal of using components is to avoid repeating work and minimize the number of adjustments needed for changes <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

### Designing with Components

A key strategy is to turn a frame into a component as the *very first step* <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. This allows for immediate duplication and styling manipulation, as changes to the main component propagate to all instances <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

Components are especially useful for [[figma_design_best_practices | Figma design best practices]] because they allow for quick iterations without having to manually update every instance of a design element <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## Leveraging Auto Layout

[[figma_design_best_practices | Auto Layout]] is a crucial feature that enhances the efficiency of component-based design:

*   **Creation**: Create an Auto Layout by hitting `Shift + A` <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   **Functionality**: It functions like a stack, allowing you to throw anything into it <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. It maps directly to Flexbox in CSS, making the design process more aligned with development <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.
*   **Benefits**: Using Auto Layout means that anything built with it is easily translatable to Flexbox, ensuring designs are "developer-friendly" <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. Avoiding random positioning of elements in a frame is recommended, as it's equivalent to absolute positioning in CSS, which should generally be avoided <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.

## Iterative Design Workflow

A common workflow for rapid iteration involves:

1.  **Duplicating Frames**: Duplicate the entire design frame (`Command + D`) to create a saved bookmark of the current iteration <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
2.  **Destroying Instances**: Use the "Destroyer" plugin to remove all component instances within the duplicated frame, effectively "freezing" that iteration in time so it won't change with the main component <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.
3.  **Continuous Exploration**: Keep the main component in the leftmost frame as the source of truth, observing real-time updates in a separate prototype view (e.g., on a laptop at 1X scale) <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. This allows for constant experimentation and trying many variations quickly, which is crucial for good design <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.

## [[prototyping_and_interactivity_in_figma | Prototyping and Interactivity]]

Components are essential for adding interactivity:

*   **Variants**: To add a hover state, create a component and then use the "Add Variant" option in the top right <a class="yt-timestamp" data-t="00:23:27">[00:23:27]</a>. Name the variants (e.g., "default", "hover") <a class="yt-timestamp" data-t="00:23:45">[00:23:45]</a>.
*   **Interactions**: In "Prototype" mode, drag a connection from the default state to the hover state. Set the trigger to "while hovering" and the animation to "Smart Animate" with a smooth easing (e.g., "gentle") and a duration (e.g., 400ms) <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>. Smart Animate smoothly transitions between states <a class="yt-timestamp" data-t="00:24:53">[00:24:53]</a>.

## Efficient Component Editing

Figma offers tools for making changes across multiple component variants simultaneously:

*   **Multi-Edit Variants**: Use the "Multi-edit variants" icon or hit 'Q' to enter this mode <a class="yt-timestamp" data-t="00:27:03">[00:27:03]</a>.
*   **Bulk Changes**: Any change made in this mode will populate across all selected variants, ensuring consistency and saving time <a class="yt-timestamp" data-t="00:27:10">[00:27:10]</a>. This is particularly helpful for adjusting padding or layout within nested Auto Layouts <a class="yt-timestamp" data-t="00:28:08">[00:28:08]</a>.

## Recommended [[figma_plugins_for_design_efficiency | Figma Plugins]]

While Figma's built-in features are robust, a few plugins can significantly enhance workflows:

*   **Destroyer**: Crucial for the iterative workflow, allowing the removal of component instances to freeze design versions <a class="yt-timestamp" data-t="00:30:29">[00:30:29]</a>.
*   **Phosphor**: A go-to library for icons, ensuring consistent and beautiful iconography <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>. Access by `Command + K` and typing "phosphor" <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
*   **Smooth Shadow**: Generates multi-layered, realistic shadows that are difficult to create manually with a single layer <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>. Access by `Command + K` and typing "smooth shadow" <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>.
*   **Noise and Texture**: Adds subtle graininess and texture, improving visual interest <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>. Access by `Command + K` and typing "noise and texture" <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>.
*   **Content Reel**: Excellent for populating designs with realistic content like avatars or text, especially when working with many related items <a class="yt-timestamp" data-t="00:30:44">[00:30:44]</a>. Can be used in conjunction with "Select Similar Layers" to quickly select elements by name or type <a class="yt-timestamp" data-t="00:31:20">[00:31:20]</a>.

## Advanced Visual Effects

*   **Layer Blur**: Adds visual interest by blurring elements, controllable via effects panel <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
*   **Luminosity Blend Mode**: Found in "Apply blend mode," this option allows underlying colors to bleed through, creating a tinted black-and-white effect on images <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>.
*   **Inner Shadows**: A powerful way to add depth and a rounded, 3D curvature effect to corners, mimicking natural lighting <a class="yt-timestamp" data-t="00:33:26">[00:33:26]</a>. This subtle detail is prevalent in high-quality designs <a class="yt-timestamp" data-t="00:34:36">[00:34:36]</a>.

## Figma in the Broader Design Landscape

While Figma excels at generative design and rapid ideation, the design landscape is evolving:

*   **[[transitioning_from_figma_to_codebased_design_tools | Transitioning from Figma to code-based design tools]]**: Once initial ideas are explored and refined in Figma, tools like Framer are increasingly used for the final 5-10% of polish and for building additional pages directly in a code-based environment <a class="yt-timestamp" data-t="00:36:42">[00:36:42]</a>.
*   **Figma as a Sketchpad**: Figma can be thought of as a pencil and paper for sketching out ideas, while tools like VZero are akin to word processors, offering more templated and productized outputs <a class="yt-timestamp" data-t="00:37:13">[00:37:13]</a>.
*   **Future of Design**: The line between high-fidelity design in Figma and high-fidelity code is blurring <a class="yt-timestamp" data-t="00:38:09">[00:38:09]</a>. Figma may eventually serve more as a lower-fidelity exploration tool, with code-based tools handling the higher fidelity and final product <a class="yt-timestamp" data-t="00:38:18">[00:38:18]</a>.

The best way to learn Figma is by actively using the tool, opening a new file, and getting hands-on with frames and components <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>.