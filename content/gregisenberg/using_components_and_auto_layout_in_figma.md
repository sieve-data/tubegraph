---
title: Using components and auto layout in Figma
videoId: XoOx5xPdv4M
---

From: [[gregisenberg]] <br/> 

Figma offers powerful features like Components and Auto Layout that significantly enhance design efficiency and maintain consistency, especially for iterative processes. These tools help designers work faster by minimizing repetitive tasks and streamlining changes, often mapping directly to how elements are built in code <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## Frames: The Basic Container

In Figma, a "Frame" serves as the primary container for design elements, similar to a `div` element in CSS <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. To create a frame, you can hit the "F" key <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. Any design element you need can be placed inside a frame <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

## Components: Reusable Elements

Components are a powerful feature in Figma that allow designers to create reusable UI elements. While often associated with [[Figma design best practices | Design Systems]] and large-scale projects, they can also be used as "hacky speed mechanisms" for rapid prototyping and iteration <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

### Benefits of Using Components
*   **Speed and Efficiency**: They enable designers to avoid repetitive work by making changes once to the master component, which then propagates to all instances <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Consistency**: Ensures a consistent look and feel across all uses of an element <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Workflow with Components
1.  **Create a Component Early**: A total "hack" for moving quickly is to turn a frame into a component as the very first step, even before adding content <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
2.  **Duplicate Instances**: Once the main component is created, you can duplicate it multiple times to create instances <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. Any styling or content changes made to the master component will automatically update all instances <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
3.  **Preserving Iterations**: During an iterative design process, if you want to freeze a particular design state without it updating from the master component, duplicate the entire frame containing the instances. Then, use a plugin like "Destroyer" to remove all component links within that duplicated frame, effectively freezing it in time <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
4.  **Multi-Edit Variants**: To make changes across all variants of a component simultaneously, use the "Multi-edit variants" feature by hitting `Q` <a class="yt-timestamp" data-t="00:27:04">[00:27:04]</a>. This ensures changes propagate without having to edit each variant individually <a class="yt-timestamp" data-t="00:27:10">[00:27:10]</a>.

## Auto Layout: Dynamic Layouts

Auto Layout is a core Figma feature that allows you to create dynamic frames that automatically adjust their size based on their content, or distribute space between child objects evenly <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. It functions similarly to Flexbox in CSS <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

### Benefits of Auto Layout
*   **Responsive Design**: Enables layouts to adapt dynamically, which is crucial for responsive web design.
*   **Code-Friendly**: Designs built with Auto Layout are much easier to translate into actual code, especially for front-end frameworks like CSS Flexbox or [[enhancing_web_design_with_tailwind_css_and_ai | Tailwind CSS]] <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>. Arbitrarily positioning elements in a frame is equivalent to absolute positioning in CSS, which is generally undesirable <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.
*   **Control Spacing and Padding**: Easily manage the space between elements and the padding around them <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

### How to Use Auto Layout
1.  **Create an Auto Layout**: Select the elements you want to group and hit `Shift + A` <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. This will turn them into an Auto Layout frame.
2.  **Adjust Properties**: Once in Auto Layout, you can control properties such as:
    *   **Space Between**: Adjust the spacing between items within the layout <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
    *   **Padding**: Set internal padding around the content <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.
    *   **Direction**: Choose vertical or horizontal layout.
    *   **Wrap**: Allow content to wrap to the next line, similar to `flex-wrap` in CSS <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.
3.  **Nesting Auto Layouts**: You can nest Auto Layouts within each other to create complex, yet flexible, UI structures.

## Prototyping with Components

Components are essential for creating interactive prototypes in Figma, particularly for hover states <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.

### Creating a Hover State
1.  **Add a Variant**: With your master component selected, click "Add variant" in the top right panel <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>. Name the original "Default" and the new one "Hover" <a class="yt-timestamp" data-t="00:23:45">[00:23:45]</a>.
2.  **Style the Hover Variant**: Make any desired visual changes to the "Hover" variant (e.g., increase blur, change background, adjust border) <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>.
3.  **Link with Prototype Mode**:
    *   Switch to "Prototype" mode in the top right <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a>.
    *   Click the blue dot on the "Default" variant and drag it to the "Hover" variant <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>.
    *   In the interaction settings, change the trigger from "On click" to "While hovering" <a class="yt-timestamp" data-t="00:24:41">[00:24:41]</a>.
    *   For smooth transitions, select "Smart animate" instead of "Instant" <a class="yt-timestamp" data-t="00:24:53">[00:24:53]</a>. "Smart animate" automatically interpolates between the two states, making the animation fluid <a class="yt-timestamp" data-t="00:24:54">[00:24:54]</a>.

## Useful [[Plugins for Figma design enhancement | Figma Plugins]]

While Figma's built-in features are robust, certain plugins can further enhance the design workflow:
*   **Destroyer**: Removes component instances within a frame, "freezing" that iteration of the design <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.
*   **Phosphor**: A go-to library for icons, ensuring a consistent visual style <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>.
*   **Smooth Shadow**: Creates beautiful, complex shadows that would be tedious to achieve manually <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>.
*   **Noise and Texture**: Adds graininess and other visual effects to designs, enhancing depth and interest <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.
*   **Content Reel**: Populates designs with various types of content, such as avatars or text, quickly <a class="yt-timestamp" data-t="00:30:44">[00:30:44]</a>.
*   **Select Layers**: Used in conjunction with Content Reel to select similar layers by name for bulk content changes <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>.

It is suggested not to stress about having a large repertoire of plugins, as Figma's native capabilities have greatly improved <a class="yt-timestamp" data-t="00:32:46">[00:32:46]</a>.

## Design Best Practices

*   **Iterate Constantly**: Try many different approaches. The faster you can try things, the better your designs will become <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.
*   **Seek Inspiration**: Maintain a database of design inspiration (e.g., in Notion) and constantly dump ideas there <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. Notice what you like, and ask why you like it <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
*   **Consider Development**: Designers should always think about how a design will be built, especially concerning CSS properties and frameworks like [[enhancing_web_design_with_tailwind_css_and_ai | Tailwind CSS]] <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.
*   **Visual Enhancements**:
    *   **Opacity**: Use number keys to quickly adjust layer opacity (e.g., `6` for 60%, `4` for 40%, `0` for 100%) <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
    *   **Layer Blur**: Apply layer blur to create depth and visual interest <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
    *   **Blend Modes**: Experiment with blend modes, like "Luminosity," to allow underlying colors to bleed through images for a tinted black and white effect <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>.
    *   **Inner Shadows**: Add inner shadows to create a subtle rounded or 3D effect on corners, making elements feel like they're "bending" or have depth <a class="yt-timestamp" data-t="00:33:26">[00:33:26]</a>.

## Figma vs. Code-Based Tools

While Figma is excellent for generative design, allowing for quick iteration and exploration of diverse ideas, the industry is seeing a shift towards [[building_websites_with_webflow | code-based tools]] like Framer or [[using_ai_for_creating_production_ready_designs | V0]] <a class="yt-timestamp" data-t="00:36:26">[00:36:26]</a>. Figma is ideal for pushing visual boundaries and exploring options that might feel too "templated" in AI-driven tools <a class="yt-timestamp" data-t="00:36:09">[00:36:09]</a>. However, once a design direction is solidified, transitioning to a tool like Framer for the final 5-10% of refinement and [[building_websites_with_webflow | building the actual website]] is becoming more common <a class="yt-timestamp" data-t="00:36:42">[00:36:42]</a>.

Figma is still considered the best starting point for design, acting like a "piece of paper and a pencil" for sketching ideas <a class="yt-timestamp" data-t="00:37:13">[00:37:13]</a>. The future of software creation might see the line between high-fidelity design in tools like Figma and high-fidelity code blur significantly, potentially positioning Figma more as a lower-fidelity exploration tool <a class="yt-timestamp" data-t="00:38:09">[00:38:09]</a>.