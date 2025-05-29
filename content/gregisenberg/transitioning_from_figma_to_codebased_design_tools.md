---
title: Transitioning from Figma to codebased design tools
videoId: XoOx5xPdv4M
---

From: [[gregisenberg]] <br/> 

The design workflow often begins in Figma, serving as a generative space for exploring ideas, but eventually transitions to code-based tools for final implementation and refinement <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. This approach allows designers to iterate quickly and then build with the end-product's technical requirements in mind <a class="yt-timestamp" data-t="01:12:50">[01:12:50]</a>.

## Figma's Role in the Design Process

Figma is considered an excellent starting point for design, akin to using a pencil and paper for sketching <a class="yt-timestamp" data-t="00:37:13">[00:37:13]</a>. It's ideal for being generative and getting as many ideas out as possible <a class="yt-timestamp" data-t="00:35:53">[00:35:53]</a>.

Key benefits of starting in Figma include:
*   **Rapid Iteration** <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>: It allows designers to try many things quickly, which is crucial for good design <a class="yt-timestamp" data-t="01:12:50">[01:12:50]</a>.
*   **Divergent Idea Exploration** <a class="yt-timestamp" data-t="00:36:03">[00:36:03]</a>: Figma enables pushing visual ideas and figuring out what you truly want to make <a class="yt-timestamp" data-t="00:36:12">[00:36:12]</a>.
*   **Learning and Inspiration** <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>: Designers should constantly seek inspiration, collecting and categorizing elements they like in a database (like Notion) <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>, <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This allows for designing "from abundance" <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>, meaning ideas are already in mind from prior collection <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
*   **Prototyping and Interactivity** <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>: Figma supports basic [[prototyping_and_interactivity_in_figma | prototyping and interactivity]], such as creating hover states using components and Smart Animate <a class="yt-timestamp" data-t="00:23:27">[00:23:27]</a>, <a class="yt-timestamp" data-t="00:24:53">[00:24:53]</a>. This helps in feeling out how designs behave <a class="yt-timestamp" data-t="00:22:55">[00:22:55]</a>.

### Figma Best Practices for Code Transition
Effective [[figma_design_best_practices | Figma design best practices]] can streamline the transition to code:
*   **[[component_usage_in_figma | Component Usage]]** <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>: Turn elements into components early in the process to avoid doing the same thing twice <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. The Multi-edit variants feature (Q key) allows changes to populate everywhere, ensuring consistency <a class="yt-timestamp" data-t="00:27:04">[00:27:04]</a>.
*   **Auto Layout** <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>: Using Auto Layout (Shift+A) is crucial as it maps well to Flexbox in CSS <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. If something can be built with Auto Layout, it's easy to build in Flexbox <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>. Randomly positioning elements is like using absolute positioning in CSS, which is generally to be avoided <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.
*   **Adherence to Development Standards** <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>: Designing with the build process in mind, such as using values that are multiples of eight (common in Tailwind CSS), helps ensure a smoother transition to code <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.
*   **[[figma_plugins_for_design_efficiency | Figma Plugins for Design Efficiency]]** <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>: Plugins can automate tedious tasks and add visual effects:
    *   **Phosphor** (for icons): Provides a consistent library of icons <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>.
    *   **Smooth Shadow**: Creates complex, layered shadows that are difficult to achieve manually <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>.
    *   **Noise and Texture**: Adds graininess and visual interest <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>.
    *   **Destroyer**: Removes component instances, "freezing" a design iteration in time for comparison <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.
    *   **Content Re**: Populates designs with images and related content quickly <a class="yt-timestamp" data-t="00:30:44">[00:30:44]</a>.
    *   **Select Similar Layers**: Helps select multiple elements for bulk changes <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>.
*   **Visual Enhancements** <a class="yt-timestamp" data-t="00:27:24">[00:27:24]</a>:
    *   Using opacity (number keys) to subtly adjust colors or backgrounds <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   Applying layer blur and blend modes (like Luminosity) to create depth and visual interest <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
    *   Utilizing inner shadows to create a rounded, 3D curvature effect, making elements feel like lighting is shining over the edge <a class="yt-timestamp" data-t="00:33:22">[00:33:22]</a>, <a class="yt-timestamp" data-t="00:34:07">[00:34:07]</a>.

## Transitioning to Code-Based Tools

While Figma is excellent for exploration, the next step often involves building directly in code-based tools like Framer, especially for web design <a class="yt-timestamp" data-t="00:36:26">[00:36:26]</a>.

*   **Framer's Role**: Once a design feels good in Figma, moving to Framer helps refine the final 5-10% in the actual medium <a class="yt-timestamp" data-t="00:36:45">[00:36:45]</a>. Other pages of a website might even be built directly in Framer after the initial core design is settled <a class="yt-timestamp" data-t="00:36:53">[00:36:53]</a>.
*   **AI Tools and the Blurring Line**: [[comparison_of_ai_coding_tools | AI coding tools]] like V0 are changing the landscape. While V0 might produce "tame, slightly templated" designs <a class="yt-timestamp" data-t="00:36:06">[00:36:06]</a>, the general trend is towards blurring the line between high-fidelity design in Figma and high-fidelity code <a class="yt-timestamp" data-t="00:38:09">[00:38:09]</a>. This suggests Figma might shift to an even lower-fidelity, exploratory role in the future, with AI handling the high-fidelity code generation <a class="yt-timestamp" data-t="00:38:14">[00:38:14]</a>.

The ultimate goal is to build ideas in code-based tools, as it's seen as the better way forward <a class="yt-timestamp" data-t="00:37:02">[00:37:02]</a>.

## Conclusion

Regardless of the tools used, the best way to learn is by actively engaging with them <a class="yt-timestamp" data-t="00:39:30">[00:39:30]</a>. Starting a new Figma file and experimenting is the most effective approach to gaining confidence and mastering design workflows <a class="yt-timestamp" data-t="00:39:43">[00:39:43]</a>.