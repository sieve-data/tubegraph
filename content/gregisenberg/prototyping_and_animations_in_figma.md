---
title: Prototyping and animations in Figma
videoId: XoOx5xPdv4M
---

From: [[gregisenberg]] <br/> 

Figma is a widely used design tool that allows designers to not only create static user interfaces but also to develop interactive prototypes and animations. This functionality enables designers to visualize user flows, test interactions, and present dynamic designs.

## Interactive Prototyping Basics

One of the key advantages of Figma is its ability to facilitate rapid [[interactive_prototyping_tools_for_app_development | interactive prototyping]]. A designer can start building a course page for a website, which involves creating a "course card" as a core element <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>.

### Starting with a Frame
To begin, create a frame by hitting `F` on the keyboard, which acts as a container similar to a CSS `div` <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>. This frame can then be styled and filled with content <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.

### Leveraging Components for Efficiency
A crucial technique for efficient prototyping is to immediately turn a basic design element into a [[creating_and_using_components_in_figma | component]] <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>. While components are often associated with Design Systems, they are also useful for quickly iterating on designs by minimizing repetitive tasks <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>. By duplicating a component multiple times, any change made to the master component will automatically apply to all instances, creating a "one knob" control <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.

### Auto Layout
[[figma_design_techniques | Auto Layout]] (activated by `Shift A`) is essential for responsive designs, functioning similarly to CSS Flexbox <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>. It allows for dynamic spacing and arrangement of elements within a container <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>. Building with [[figma_design_techniques | Auto Layout]] makes it much easier to translate designs into code, as it naturally maps to front-end development practices <a class="yt-timestamp" data-t="15:01:00">[15:01:00]</a>.

## Creating Interactive States

Prototyping quickly allows designers to feel how their designs behave, especially hover states <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.

### Variants for Hover States
To add a hover state, ensure the element is a component. Then, in the top right, select "Add Variant" <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>. One variant can be named "default" and the other "hover" <a class="yt-timestamp" data-t="02:45:00">[02:45:00]</a>. Changes made to the "hover" variant, such as increasing blur, background, or border, will define its appearance <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.

### Prototyping Connections
In the "Prototype" mode, drag a connection from the "default" component to the "hover" variant <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>. Set the interaction to "while hovering" instead of the default "on click" <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.

## Animation Settings

When connecting interactive states, choosing the right animation preset is crucial for a smooth user experience <a class="yt-timestamp" data-t="02:45:00">[02:45:00]</a>.

### Smart Animate
Avoid "instant" animations <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>. Instead, select "Smart Animate" to smoothly transition between states <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>. "Gentle" is a recommended easing curve, often with a duration around 400ms <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>. This allows elements to expand or other property changes to animate seamlessly <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.

## Enhancing Visual Interest with Effects

Figma offers several effects that can add depth and realism to designs, especially when prototyping.

### Layer Blur
Layer blur can add visual interest, making elements like background colors pop <a class="yt-timestamp" data-t="17:37:00">[17:37:00]</a>. Applying a blur effect to a colored rectangle placed behind an element can create a soft glow <a class="yt-timestamp" data-t="17:51:00">[17:51:00]</a>.

### Blend Modes
Blend modes, like "Luminosity," can be used to tint images based on underlying colors, creating a "tinted black and white" effect that looks appealing <a class="yt-timestamp" data-t="18:48:00">[18:48:00]</a>.

### Noise and Texture
Adding a subtle layer of noise or texture can significantly enhance visual interest <a class="yt-timestamp" data-t="19:43:00">[19:43:00]</a>. This can be achieved by adding a rectangle, filling it with a noise texture using a plugin, and then decreasing its opacity <a class="yt-timestamp" data-t="19:53:00">[19:53:00]</a>.

### Smooth Shadow Plugin
For creating realistic shadows that give elements a sense of "lift" or elevation, the "Smooth Shadow" [[figma_plugins_and_workflow_enhancements | plugin]] is highly recommended <a class="yt-timestamp" data-t="25:57:00">[25:57:00]</a>. It generates multi-layered shadows that appear more natural than a single drop shadow effect <a class="yt-timestamp" data-t="25:52:00">[25:52:00]</a>.

### Inner Shadows for Depth
[[figma_design_techniques | Inner Shadows]] can create a subtle 3D curvature or "rounded feel" on corners <a class="yt-timestamp" data-t="33:17:00">[33:17:00]</a>. By setting an inner shadow to white and adjusting its offset and blur, it can simulate light shining over an edge <a class="yt-timestamp" data-t="33:43:00">[33:43:00]</a>. Using both top (positive Y-offset) and bottom (negative Y-offset) inner shadows can create a full rounded appearance <a class="yt-timestamp" data-t="34:13:00">[34:13:00]</a>. This subtle effect is common in high-quality modern designs <a class="yt-timestamp" data-t="34:36:00">[34:36:00]</a>.

## Figma's Role in the Design Workflow

Figma excels as a generative tool for getting a wide array of ideas out quickly and exploring diverse concepts <a class="yt-timestamp" data-t="35:53:00">[35:53:00]</a>. It allows for faster iteration compared to code-based tools like Vercel or Framer <a class="yt-timestamp" data-t="35:58:00">[35:58:00]</a>. While tools like Vercel might offer templated designs, Figma empowers designers to push visual boundaries and define what they truly want to create <a class="yt-timestamp" data-t="36:06:00">[36:06:00]</a>.

The design process often involves using Figma for initial ideation and exploration ("throwing paint at the wall") <a class="yt-timestamp" data-t="36:31:00">[36:31:00]</a>. Once a strong direction is established, the design might then be refined and built in a code-based tool like Framer for the final 5-10% polish and development <a class="yt-timestamp" data-t="36:40:00">[36:40:00]</a>. This approach highlights Figma's strength as a sketching and ideation canvas <a class="yt-timestamp" data-t="37:13:00">[37:13:00]</a>.

Figma is still considered a prime starting point for [[drafting_app_concepts_with_minimal_coding_knowledge | drafting app concepts with minimal coding knowledge]] <a class="yt-timestamp" data-t="37:43:00">[37:43:00]</a>. However, the future of software creation may see a blurring of lines between high-fidelity design and high-fidelity code, potentially shifting Figma's role even earlier in the process as a lower-fidelity exploration tool <a class="yt-timestamp" data-t="37:51:00">[37:51:00]</a>.

## Learning Figma
The best way to learn Figma is by actively using the tool <a class="yt-timestamp" data-t="39:27:00">[39:27:00]</a>. Starting by simply drawing a frame on the canvas (by pressing `F`) is the first step into hands-on practice <a class="yt-timestamp" data-t="39:43:00">[39:43:00]</a>.