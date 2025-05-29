---
title: Incorporating visual effects and textures in design with Figma plugins
videoId: XoOx5xPdv4M
---

From: [[gregisenberg]] <br/> 

In a live design session, an expert showcased how to leverage Figma for designing a course marketplace, emphasizing best practices and visual enhancements, particularly through the use of plugins and iterative design processes. The session aimed to provide a window into a designer's process of iterating and making visual improvements to designs. This includes considerations for building components, applying styling, and incorporating advanced visual effects and textures. <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>

## Figma Fundamentals and Workflow
The design process often begins with creating a "frame" by hitting `F`, which acts as a container similar to a CSS `div`. <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a> These frames can be immediately converted into components, even before content is added, to facilitate rapid iteration and minimize repetitive tasks. <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>

[[Building components and using Auto layout in Figma | Auto layout]], activated by `Shift A`, is crucial for throwing elements into a stack and controlling spacing, akin to CSS Flexbox. <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a> This structural approach ensures that designs are easily translatable into code. <a class="yt-timestamp" data-t="14:58:00">[14:58:00]</a>

### Iterative Design and Inspiration
A key aspect of the design workflow is constant iteration. This involves:
*   **Collecting Inspiration**: Maintaining a database (e.g., Notion) of design inspirations, similar to David Perell's concept of "writing from abundance." <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>
*   **Rapid Prototyping**: Quickly duplicating frames and "destroying" component instances using a plugin (like "Destroyer") to preserve design states at different stages of exploration. <a class="yt-timestamp" data-t="09:58:00">[09:58:00]</a> This allows for quick shifts between design ideas without affecting previous iterations. <a class="yt-timestamp" data-t="11:14:00">[11:14:00]</a>
*   **Real-time Preview**: Designing in one frame while simultaneously viewing the design at 1x scale in prototype mode on a separate screen to ensure accuracy and feel. <a class="yt-timestamp" data-t="11:26:00">[11:26:00]</a>

## Enhancing Visuals with Effects and Textures

Several techniques can be used to add [[balancing_and_blending_aesthetic_elements_using_ai | visual interest]] and polish to designs:

### 1. Lighting and Blur
To add a subtle visual effect, create a rectangle (`R`), give it a color fill, and move it to the back of the layer tree (`Command [`). <a class="yt-timestamp" data-t="17:30:00">[17:30:00]</a> Apply a "Layer blur" effect and adjust its value. <a class="yt-timestamp" data-t="18:08:00">[18:08:00]</a> The opacity can also be subtly decreased using number keys (e.g., `4` for 40% opacity). <a class="yt-timestamp" data-t="18:25:00">[18:25:00]</a>

### 2. Blend Modes
The "Luminosity" blend mode, accessible via the "apply blend mode" dropdown, is particularly useful. <a class="yt-timestamp" data-t="18:45:00">[18:45:00]</a> It allows colors from layers below to bleed through, creating a tinted black-and-white effect, which can significantly enhance visual appeal. <a class="yt-timestamp" data-t="19:05:00">[19:05:00]</a>

### 3. Noise and Texture
Adding graininess can elevate a design. This is achieved by creating another rectangle, pinning it to the edges, and moving it to the back. <a class="yt-timestamp" data-t="19:40:00">[19:40:00]</a>
*   **Plugin**: The "Noise and Texture" plugin is recommended for adding various visual effects, including simple noise. <a class="yt-timestamp" data-t="20:10:00">[20:10:00]</a>
*   After applying the effect, adjust its opacity (e.g., `05` for 5%) to achieve a subtle texture. <a class="yt-timestamp" data-t="20:47:00">[20:47:00]</a>

### 4. Smooth Shadows
For professional-looking shadows, avoid manual adjustments.
*   **Plugin**: The "Smooth Shadow" plugin is highly effective, offering easing curves and alpha control for creating beautiful, multi-layered shadows. <a class="yt-timestamp" data-t="25:57:00">[25:57:00]</a> Applying these shadows can give elements a sense of elevation. <a class="yt-timestamp" data-t="26:31:00">[26:31:00]</a>

### 5. Inner Shadows
To create a sense of depth, rounding, or lighting shining over edges, inner shadows are a powerful tool. <a class="yt-timestamp" data-t="33:08:00">[33:08:00]</a>
*   Add an "Inner Shadow" effect and set its color (e.g., white for highlights). <a class="yt-timestamp" data-t="33:39:00">[33:39:00]</a>
*   Adjust the X/Y values and blur to create the desired rounded or bending effect, especially subtle on dark mode designs. <a class="yt-timestamp" data-t="33:51:00">[33:51:00]</a> This subtle visual effect is frequently seen in high-quality modern designs. <a class="yt-timestamp" data-t="34:36:00">[34:36:00]</a>

## [[prototyping_and_interactivity_in_figma_design_workflow | Prototyping and Interactivity]]
Figma allows for adding [[prototyping_and_interactivity_in_figma_design_workflow | interactivity]] like hover states. <a class="yt-timestamp" data-t="23:27:00">[23:27:00]</a>
*   Create a component and add a "variant" for the hover state. <a class="yt-timestamp" data-t="23:31:00">[23:31:00]</a>
*   In "Prototype" mode, drag a connection from the default state to the hover variant. <a class="yt-timestamp" data-t="24:20:00">[24:20:00]</a>
*   Set the interaction to "While hovering" and choose "Smart Animate" with an easing preset (e.g., "gentle" at 400ms) for smooth transitions. <a class="yt-timestamp" data-t="24:45:00">[24:45:00]</a>
*   Use "Multi-edit variants" (`Q`) to make changes across all component states simultaneously, avoiding repetitive edits. <a class="yt-timestamp" data-t="27:04:00">[27:04:00]</a>

## Plugin Recommendations and Philosophy
While many designers use numerous plugins, the recommendation is to focus on a few key ones that fall into two categories:
1.  **Visual Effects**: Plugins that handle tedious or complex visual tasks not easily done manually (e.g., "Noise and Texture", "Smooth Shadow"). <a class="yt-timestamp" data-t="29:55:00">[29:55:00]</a>
2.  **Workflow Enhancements**: Plugins that streamline repetitive tasks (e.g., "Destroyer" for iteration, "Content Reel" for populating designs with data like images or text). <a class="yt-timestamp" data-t="30:27:00">[30:27:00]</a>

Figma's continuous updates have integrated many previously plugin-dependent features directly into the software, reducing the need for an extensive plugin repertoire. <a class="yt-timestamp" data-t="32:40:00">[32:40:00]</a>

## [[future_of_design_tools_figma_versus_codebased_tools_like_framer | Figma vs. Code-based Tools]]
Figma remains excellent for generative design, rapid iteration, and exploring divergent visual ideas because of its speed and flexibility. <a class="yt-timestamp" data-t="35:53:00">[35:53:00]</a> However, for the final 5-10% of refinement and for building production-ready designs, code-based tools like [[future_of_design_tools_figma_versus_codebased_tools_like_framer | Framer]] are increasingly being adopted. <a class="yt-timestamp" data-t="36:26:00">[36:26:00]</a>

Figma can be thought of as a pencil and paper for sketching initial ideas, while tools like VZero or Microsoft Word represent more templatized, productized outcomes. <a class="yt-timestamp" data-t="37:13:00">[37:13:00]</a> The blurring line between high-fidelity design in Figma and high-fidelity code suggests that their roles might evolve, with Figma potentially serving earlier, lower-fidelity exploration stages. <a class="yt-timestamp" data-t="38:09:00">[38:09:00]</a>

Ultimately, hands-on practice is essential for mastering Figma. <a class="yt-timestamp" data-t="39:27:00">[39:27:00]</a>