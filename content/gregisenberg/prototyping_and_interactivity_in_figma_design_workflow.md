---
title: Prototyping and interactivity in Figma design workflow
videoId: XoOx5xPdv4M
---

From: [[gregisenberg]] <br/> 

Figma is a powerful tool for designing and prototyping, enabling designers to rapidly iterate and explore visual ideas <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. This article explores key features and best practices for creating interactive prototypes within Figma, drawing insights from a live design session.

## Core Concepts for Efficient Prototyping

### Frames as Containers
In Figma, frames act as fundamental containers for design elements, similar to a CSS `div` <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. To create a frame, simply hit `F` on the keyboard <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. Anything you need to design is placed inside a frame <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

### Leveraging Components for Speed
Components are not just for large [[design_sprint_methodology | Design Systems]]; they can be used as "hacky speed mechanisms" in Figma to avoid repetitive work <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. By turning a frame into a component early in the design process, even before adding content, designers can make changes once at the source, which then propagates to all instances <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>, saving time and effort <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### Harnessing Auto Layout
Auto Layout, activated by hitting `Shift + A`, functions much like CSS Flexbox <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. It allows designers to control spacing, alignment, and responsiveness, making designs easier to build in code later <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>. When building in Figma using Auto Layout, the resulting design is naturally more compatible with front-end development <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. Avoid random positioning in frames, as this is akin to absolute positioning in CSS, which is generally less desirable <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.

### Iteration Workflow and Inspiration
A key aspect of effective design is rapid iteration <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

*   **Designing from Abundance**: Rather than starting from a blank page, designers should constantly collect inspiration <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. Maintaining a database of ideas and categorizing them allows for "writing from abundance," where inspiration is always at hand <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
*   **"Destroyer" Plugin**: To preserve design iterations without affecting the main component, designers can duplicate a frame and use the "Destroyer" plugin to "destroy instances" <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>. This freezes the design in time, allowing for further exploration without unintended changes <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
*   **Real-time Preview**: Designing in one main frame while viewing the prototype in real-time on a separate screen (e.g., a laptop in prototype mode) helps maintain context and ensures the design looks good at actual size <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>. The leftmost frame typically serves as the "source of truth" <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

## Adding Interactivity and Visual Effects

### Creating Hover States
To add a hover state to a component in Figma:
1.  Make the element a component <a class="yt-timestamp" data-t="00:23:29">[00:23:29]</a>.
2.  Click "Add variant" in the top right <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>.
3.  Design the "hover" variant with desired visual changes (e.g., increased blur, background pop, border changes) <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>.
4.  In prototype mode, drag a connection from the default state to the hover state <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>.
5.  Set the interaction to "While hovering" <a class="yt-timestamp" data-t="00:24:38">[00:24:38]</a>.
6.  Use "Smart Animate" for a smooth transition <a class="yt-timestamp" data-t="00:24:53">[00:24:53]</a>, avoiding "Instant" for a better user experience <a class="yt-timestamp" data-t="00:24:48">[00:24:48]</a>. Adjust easing curves and duration for the desired feel <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>.

### Visual Enhancement Techniques
*   **Number Key Opacity Adjustment**: Quickly adjust layer opacity by typing numbers on the keyboard (e.g., `6` for 60%, `0` for 100%) <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Plugins for Icons**: Using icon plugins like Phosphor (accessed via `Command + K`) ensures visual consistency and saves time <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>.
*   **Adding Blur for Visual Interest**: Use a rectangle with a color fill, move it to the back (`Command + [`), and apply a "Layer blur" effect in the Effects panel <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.
*   **Blend Modes**: The "Luminosity" blend mode (found under "Apply blend mode") is useful for tinting images, allowing underlying colors to bleed through, creating a tinted black and white effect <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>.
*   **Noise and Texture**: Adding a subtle layer of noise or graininess using a plugin like "Noise and Texture" can add visual interest <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>. After adding a rectangle and applying the noise, decrease its opacity to a low percentage (e.g., 5%) for a subtle effect <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>.
*   **Smooth Shadows**: Instead of manually tweaking drop shadows, plugins like "Smooth Shadow" (accessed via `Command + K`) can generate aesthetically pleasing shadows with easing curves and adjustable transparency <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>. Good shadows often involve multiple layers, which plugins handle automatically <a class="yt-timestamp" data-t="00:25:52">[00:25:52]</a>.
*   **Inner Shadows for Depth**: Inner shadows can create a subtle 3D, rounded feel on corners, making it appear as if light is shining over the edge <a class="yt-timestamp" data-t="00:33:22">[00:33:22]</a>. Set inner shadows with white at the top and a darker shade at the bottom, adjusting blur and opacity for a soft effect <a class="yt-timestamp" data-t="00:33:51">[00:33:51]</a>. This adds depth and texture commonly seen in modern designs <a class="yt-timestamp" data-t="00:34:50">[00:34:50]</a>.

## Figma Plugins and Workflows

Plugins generally fall into two categories: visual effects (e.g., "Noise and Texture," "Smooth Shadow") and workflow enhancements (e.g., "Destroyer," "Content Reel") <a class="yt-timestamp" data-t="00:29:55">[00:29:55]</a>.

*   **"Destroyer"**: Used to remove component instances within a frame, freezing an iteration <a class="yt-timestamp" data-t="00:30:29">[00:30:29]</a>.
*   **Phosphor**: A favored plugin for consistent icons <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>.
*   **"Select Similar Layers"**: Useful for selecting multiple elements with similar properties, such as all images, to apply bulk changes <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>.
*   **"Content Reel"**: Allows populating designs with placeholder content, such as avatars, names, or other data, from pre-defined libraries or custom folders <a class="yt-timestamp" data-t="00:31:49">[00:31:49]</a>.
*   **Multi-Edit Variants (Q)**: Hitting `Q` enables multi-edit mode within a component, allowing changes to be applied across all variants simultaneously, preventing redundant work <a class="yt-timestamp" data-t="00:27:04">[00:27:04]</a>.

Figma itself has incorporated many workflow enhancements that used to require plugins, reducing the need for a large plugin repertoire <a class="yt-timestamp" data-t="00:32:40">[00:32:40]</a>.

## Figma in the Modern Design Landscape

While tools like VZERO or [[future_of_design_tools_figma_versus_codebased_tools_like_framer | Framer]] are emerging, Figma remains crucial for the initial, generative stages of design <a class="yt-timestamp" data-t="00:35:53">[00:35:53]</a>.

*   **Figma for Generative Ideas**: Figma excels at rapid iteration and exploring a wide array of divergent visual concepts, where the focus is on pushing ideas and throwing "paint at the wall" <a class="yt-timestamp" data-t="00:36:01">[00:36:01]</a>. Designs generated by AI tools like VZERO tend to feel more "tame" or "templated" <a class="yt-timestamp" data-t="00:36:06">[00:36:06]</a>.
*   **Transition to Code-Based Tools**: For the final 5-10% of a design, especially for web design, moving to code-based tools like [[future_of_design_tools_figma_versus_codebased_tools_like_framer | Framer]] can be beneficial <a class="yt-timestamp" data-t="00:36:45">[00:36:45]</a>. This allows designers to build the idea in a medium that maps more closely to the final product <a class="yt-timestamp" data-t="00:36:51">[00:36:51]</a>.
*   **Figma as a Sketching Tool**: Figma can be seen as a "piece of paper and a pencil" for sketching ideas, while code-based tools are more like a "word processor" for productized results <a class="yt-timestamp" data-t="00:37:13">[00:37:13]</a>.
*   **Blurring Lines**: The distinction between high-fidelity design in Figma and high-fidelity code is expected to blur in the future <a class="yt-timestamp" data-t="00:38:11">[00:38:11]</a>. Figma might shift to an even earlier, lower-fidelity exploration phase, while AI tools or integrated platforms handle the higher-fidelity code generation <a class="yt-timestamp" data-t="00:38:18">[00:38:18]</a>.

## Conclusion

The best way to learn Figma is to get hands-on <a class="yt-timestamp" data-t="00:39:29">[00:39:29]</a>. Simply open a new file, hit `F`, and start drawing to begin your design journey <a class="yt-timestamp" data-t="00:39:43">[00:39:43]</a>.