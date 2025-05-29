---
title: Figma design best practices
videoId: XoOx5xPdv4M
---

From: [[gregisenberg]] <br/> 

This article outlines best practices and tips for efficient design in Figma, focusing on workflows for speed, iteration, and creating visually appealing user interfaces.

## Core Design Workflow in Figma

The process typically begins with a specific design task, such as creating a course page for a marketplace [00:00:57].

### Starting a Design

*   **Frames as Containers**: Use the 'F' key to create a frame, which acts as a container for design elements, similar to a CSS `div` [00:02:04].
*   **Early Component Conversion**: Convert elements into [[component_usage_in_figma | components]] early in the process, even before adding content. This is a "hacky speed mechanism" to avoid repeating work and provide a single "knob" for adjustments [00:02:42]. The goal is to "never do the same thing twice" [00:03:00].
*   **Auto Layout**: Utilize auto layout (Shift+A) to arrange items. This mirrors CSS Flexbox, allowing dynamic control over spacing and arrangement [00:03:32].

### Managing Content and Styling

*   **Text Styles**: Employ pre-set text styles or reference values from established design systems like Polaris or frameworks like Tailwind CSS for typography [00:04:19].
*   **Opacity Shortcut**: Adjust opacity quickly using number keys (e.g., '6' for 60%, '0' for 100%, '.5' for 5%) [00:08:20].
*   **Adding Images**: Draw a rectangle ('R') and then paste an image from your clipboard to fill it [00:08:58].
*   **Icon Libraries**: Use [[Figma plugins for design efficiency | plugins]] like Phosphor (Command+K) for consistent icon sets [00:13:16].
*   **Spacing Values**: When setting padding or spacing, use multiples of eight to align with common development frameworks like Tailwind CSS (e.g., 16px is `pl-4`, 48px is `pl-12` in Tailwind's base 4px system) [00:16:50].

## Iteration and Efficiency

Effective design involves rapid iteration and collecting inspiration.

*   **Inspiration Gathering**: Constantly collect design inspiration in a database (e.g., Notion) to draw from an "abundance" of ideas rather than starting from a blank page [00:05:16]. Copy and paste interesting examples directly into Figma to recreate or adapt parts of them [00:06:01].
*   **Iterative Design Cycle**:
    *   Duplicate your design frame (`Command+D`) to create a new iteration [00:10:00].
    *   Use the [[Figma plugins for design efficiency | Destroyer plugin]] (`Command+K`, search "destroyer instances") to remove component links in the duplicated frame, freezing that iteration in time [00:10:22]. This allows for continued exploration in the main component without affecting saved versions [00:10:12].
    *   The goal is to try many variations quickly, as "it's actually just about trying more things than everyone else" [00:12:50].
*   **Real-time Prototyping**: Maintain a prototype view of your design (1x scale) on a separate screen (e.g., laptop) while working on the main canvas. This allows you to see changes update in real-time at the actual size [00:11:26].
*   **Traversing Layers**: Quickly navigate the layer tree using 'Enter' to drill into elements and 'Shift+Enter' to move back up [00:15:41].
*   **Multi-Edit Mode**: Use 'Q' to enter multi-edit variant mode, allowing simultaneous changes across all component variants without having to manually select each one [00:27:04].

## Enhancing Visuals

Beyond basic layout, several techniques can add depth and appeal.

*   **Dynamic Lighting and Blur**:
    *   Add a rectangle and fill it with color [00:17:44].
    *   Apply a "Layer blur" effect (under Effects panel) to create soft lighting effects [00:18:10].
    *   Use the "Luminosity" blend mode (under 'Apply blend mode') to allow underlying colors to bleed through, creating a tinted black-and-white effect [00:19:05].
*   **Noise and Texture**: Add a rectangle, pin it to the edges, and use the [[Figma plugins for design efficiency | Noise and Texture plugin]] (`Command+K`). Decrease its opacity to add subtle graininess [00:19:42].
*   **Smooth Shadows**: Use the [[Figma plugins for design efficiency | Smooth Shadow plugin]] (`Command+K`, search "smooth Shadow") to create realistic, multi-layered drop shadows that visually "lift" elements [00:25:57].
*   **Inner Shadows for Depth**: Apply inner shadows to elements to create a sense of curvature or lighting shining over an edge, adding a subtle 3D effect [00:33:26]. This technique can create a "rounded and bending" feel [00:34:31].

## [[Prototyping and interactivity in Figma | Prototyping and Interactivity]]

Adding interactivity allows you to feel how the design behaves.

*   **Hover States**:
    *   Create a component, then add a variant (`Add Variant` button in the top right) to define a hover state [00:23:27].
    *   Make desired visual changes to the hover variant (e.g., increased blur, background pop, border change) [00:23:58].
    *   In Prototype mode, drag a connection from the default state to the hover state [00:24:27].
    *   Set the interaction trigger to "While hovering" [00:24:38].
    *   Use "Smart Animate" with a smooth easing (e.g., "Gentle" with a duration like 400ms) for fluid transitions [00:24:53]. Avoid "Instant" transitions [00:24:46].

## [[Figma plugins for design efficiency | Plugin Recommendations]]

While Figma has improved its built-in features, some plugins remain highly valuable for specific workflows:

*   **Visual Effects**:
    *   **Noise and Texture**: For adding graininess and other visual effects [00:30:01].
    *   **Smooth Shadow**: For generating beautiful, multi-layered shadows [00:30:03].
*   **Workflow Enhancements**:
    *   **Destroyer**: Crucial for freezing component instances to save design iterations [00:30:29].
    *   **Content Reel**: Excellent for populating designs with placeholder content, such as avatars or text [00:30:44].
    *   **Select Similar Layers**: Useful when combined with Content Reel to quickly select and replace elements across multiple instances [00:31:10].

It is not necessary to have a large repertoire of plugins, as Figma's native capabilities have significantly improved [00:32:43].

## Figma's Role in the Design Ecosystem

Figma excels at rapid ideation and divergent exploration [00:35:53].

*   **Generative Tool**: Figma is fantastic for being generative and getting many ideas out quickly [00:35:53]. It allows for exploring "more divergent ideas" than templated tools [00:36:03].
*   **Transition to Code-Based Tools**: For web design, once initial ideas are solid, designers may transition to [[transitioning_from_figma_to_codebased_design_tools | code-based tools]] like Framer to build out the final 5-10% and subsequent pages [00:36:26].
*   **Future of Design Fidelity**: The line between high-fidelity design in Figma and high-fidelity code is blurring, suggesting that Figma might shift to an earlier, lower-fidelity exploration phase in the future as code generation tools advance [00:38:09].

## Getting Started

The best way to learn Figma is to "get in there, get your hands dirty" [00:39:27]. Open a new file, hit 'F' on your keyboard, and start drawing [00:39:43].