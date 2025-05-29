---
title: Best practices for designing in Figma
videoId: XoOx5xPdv4M
---

From: [[gregisenberg]] <br/> 

This article explores best practices and efficient workflows for designing in Figma, drawing insights from a live design session. The goal is to provide a window into the iterative process, visual improvements, and considerations for effective design.

## The Iterative Design Process

Designing in Figma is an iterative process, focusing on speed and efficiency to explore multiple ideas quickly <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>.

### Starting with Frames and Components
*   **Frames as Containers**: Use 'F' to create a frame, which acts as a container for elements, similar to a CSS `div` <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.
*   **Early Component Creation**: Convert designs into components early in the process, even before adding content. This minimizes repetitive tasks and allows for universal changes from a single "knob" <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>. This aligns with [[creating_and_using_components_in_figma | creating and using components in Figma]].
*   **Auto Layout for Flexibility**: Utilize Auto Layout (Shift + A) to create flexible stacks that behave like CSS Flexbox. This allows for easy control over spacing and arrangement of elements, making designs responsive and developer-friendly <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>.

### Efficient Iteration Techniques
*   **Keyboard Shortcuts**:
    *   Number keys (0-9) can be used to quickly adjust layer opacity (e.g., '6' for 60%, '4' for 40%) <a class="yt-timestamp" data-t="08:18:00">[08:18:00]</a>.
    *   Command + Bracket (left/right) moves layers up or down in the layer tree <a class="yt-timestamp" data-t="01:17:56">[01:17:56]</a>.
    *   Enter key drills into the canvas, and Shift + Enter moves back up, facilitating quick navigation of the layer tree <a class="yt-timestamp" data-t="15:41:00">[15:41:00]</a>.
    *   'Q' activates multi-edit variants, allowing simultaneous changes across different states of a component <a class="yt-timestamp" data-t="27:04:00">[27:04:00]</a>.
*   **Saving Iterations**: Duplicate entire frames (Command + D) to save different design states. This creates a visual history of your exploration process <a class="yt-timestamp" data-t="09:58:00">[09:58:00]</a>.
*   **Destroyer Plugin**: Use the "Destroyer" plugin to detach components from a duplicated frame, freezing that design state in time for reference while continuing to iterate on the main component <a class="yt-timestamp" data-t="10:20:00">[10:20:00]</a>.
*   **Real-time Preview**: Design in one frame on a primary monitor while viewing the prototype at 1x scale on another screen (e.g., a laptop). This allows for immediate feedback on how the design feels in its actual size <a class="yt-timestamp" data-t="11:18:00">[11:18:00]</a>.

## Design Principles and Considerations

### Leveraging Inspiration
*   **Constant Collection**: Actively collect and categorize design inspirations, maintaining a Notion database or similar system <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>. This aligns with [[design_inspiration_and_workflow_organization | design inspiration and workflow organization]].
*   **Writing from Abundance**: Similar to writing from abundance, design from a constantly growing database of visual ideas. If stuck, revisit collected inspirations and recreate interesting elements, adapting them for your design <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a>.
*   **Observe and Analyze**: Notice what you like in other designs and actively ask yourself why you like it. This self-analysis helps internalize design principles <a class="yt-timestamp" data-t="07:42:00">[07:42:00]</a>.

### Technical Alignment
*   **Think Like a Developer**: Design with an understanding of how components will be built in code. Using Auto Layout in Figma naturally maps to Flexbox in CSS, ensuring easier implementation <a class="yt-timestamp" data-t="14:32:00">[14:32:00]</a>.
*   **Tailwind Values**: When in doubt for spacing or sizing, use values that are multiples of eight, as this often aligns with utility-first CSS frameworks like Tailwind CSS, which provides out-of-the-box values <a class="yt-timestamp" data-t="16:55:00">[16:55:00]</a>.

### Adding Visual Interest and Depth
*   **Lighting and Blur**: Use rectangles with color fills, moved to the background, and apply "Layer Blur" effects to create subtle lighting and atmospheric effects <a class="yt-timestamp" data-t="17:30:00">[17:30:00]</a>.
*   **Blend Modes**: Experiment with blend modes, especially "Luminosity," to tint images and allow underlying colors to bleed through, creating a muted, artistic effect <a class="yt-timestamp" data-t="18:45:00">[18:45:00]</a>.
*   **Noise and Texture**: Add a subtle layer of noise using the "Noise and Texture" plugin to introduce graininess, enhancing visual depth <a class="yt-timestamp" data-t="19:43:00">[19:43:00]</a>.
*   **Inner Shadows**: Utilize inner shadows to create a rounded, three-dimensional, or "bending" effect on corners, mimicking light shining over an edge. This adds depth and modern [[aesthetics_in_software_design | aesthetics]] <a class="yt-timestamp" data-t="33:26:00">[33:26:00]</a>.

### Prototyping Interactions
*   **Hover States**: Create component variants (default and hover) to define interactive states. Link them in prototype mode with "While Hovering" interactions <a class="yt-timestamp" data-t="23:27:00">[23:27:00]</a>. This directly applies to [[prototyping_and_interaction_design_in_figma | prototyping and interaction design in Figma]].
*   **Smart Animate**: Use "Smart Animate" for smooth transitions between states, creating a more professional and natural feel, avoiding jarring "instant" changes <a class="yt-timestamp" data-t="24:53:00">[24:53:00]</a>.

## Recommended Plugins and Resources

Plugins can significantly enhance Figma workflows, especially for visual effects and bulk content management. This aligns with [[using_plugins_for_enhanced_design_capabilities_in_figma | using plugins for enhanced design capabilities in Figma]].

*   **Phosphor**: A favored plugin for accessing a comprehensive library of consistent and aesthetically pleasing icons <a class="yt-timestamp" data-t="13:23:00">[13:23:00]</a>.
*   **Smooth Shadow**: Generates realistic, multi-layered shadows that are difficult to achieve manually, providing depth and elevation to elements <a class="yt-timestamp" data-t="25:57:00">[25:57:00]</a>.
*   **Destroyer**: Crucial for the iterative workflow, allowing designers to detach component instances from a main component, effectively "freezing" a design state <a class="yt-timestamp" data-t="10:20:00">[10:20:00]</a>.
*   **Content Re**: Populates designs with relevant content (e.g., avatars, text, images) quickly, useful for filling tables or large arrays of components <a class="yt-timestamp" data-t="30:44:00">[30:44:00]</a>.
*   **Select Similar Layers**: A powerful plugin to select multiple layers based on criteria like name, making it efficient to apply changes (e.g., replacing all headshots) across a design <a class="yt-timestamp" data-t="31:20:00">[31:20:00]</a>.
*   **Noise and Texture**: Adds subtle grain or complex shaders to elements, enhancing visual depth and interest <a class="yt-timestamp" data-t="19:43:00">[19:43:00]</a>.

It's recommended to focus on plugins for visual effects and workflow enhancements rather than building an extensive repertoire, as Figma's native capabilities have expanded significantly <a class="yt-timestamp" data-t="29:55:00">[29:55:00]</a>.

## Figma's Role in Modern Design

Figma excels as a generative tool for quickly exploring and diverging ideas. It's akin to sketching with a pencil, allowing for rapid experimentation and pushing visual concepts beyond templated solutions <a class="yt-timestamp" data-t="35:53:00">[35:53:00]</a>.

While tools like V0 and Framer offer production-ready code or high-fidelity web design, Figma remains the best starting point for initial exploration and ideation. It allows designers to throw "paint at the wall" before moving to more code-based tools for final refinement (e.g., Framer for the last 5-10% of a web design) <a class="yt-timestamp" data-t="36:26:00">[36:26:00]</a>.

The future of software creation may see the line between high-fidelity design in tools like Figma and high-fidelity code blur. Figma might lean more towards lower-fidelity exploration, with AI-powered tools handling the transition to code <a class="yt-timestamp" data-t="37:51:00">[37:51:00]</a>.

Ultimately, the best way to learn Figma is to simply "get in there, get your hands dirty." Open a new file, type 'F', and start drawing. Experimentation is key to becoming confident and proficient <a class="yt-timestamp" data-t="39:27:00">[39:27:00]</a>.