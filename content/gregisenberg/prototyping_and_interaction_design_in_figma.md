---
title: Prototyping and interaction design in Figma
videoId: XoOx5xPdv4M
---

From: [[gregisenberg]] <br/> 

Prototyping is crucial for understanding how designs feel and behave, especially regarding interactive elements like hover states <a class="yt-timestamp" data-t="00:22:52">[00:22:52]</a>. Figma allows for rapid iteration and exploration of diverse ideas in the design process <a class="yt-timestamp" data-t="00:35:53">[00:35:53]</a>.

## Creating Interactive Components

To add interactivity, like a hover state, to a design element in Figma, convert it into a component <a class="yt-timestamp" data-t="00:23:27">[00:23:27]</a>.

### Adding Variants

Once an element is a component, use the "Add variant" option in the top right of the Design panel <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>. This creates a new state for the component, such as a "hover" state in addition to the "default" state <a class="yt-timestamp" data-t="00:23:45">[00:23:45]</a>.

### Defining Hover States

Customize the appearance of the new variant to reflect the interactive state. For example, for a hover state, you might:
*   Increase the blur effect <a class="yt-timestamp" data-t="00:23:58">[00:23:58]</a>.
*   Increase the background opacity to make it "pop" <a class="yt-timestamp" data-t="00:24:07">[00:24:07]</a>.
*   Adjust the border <a class="yt-timestamp" data-t="00:24:11">[00:24:11]</a>.

### Setting Up Interactions

1.  Switch to the "Prototype" mode in the top right <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a>.
2.  Click the blue dot on the default component and drag it to the hover variant <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>.
3.  In the interaction settings, change the trigger from "On click" to "While hovering" <a class="yt-timestamp" data-t="00:24:38">[00:24:38]</a>.

### Animation and Easing

*   Avoid "Instant" animation for smooth transitions <a class="yt-timestamp" data-t="00:24:46">[00:24:46]</a>.
*   Select "Smart animate" to tell Figma to smoothly transition between the two states <a class="yt-timestamp" data-t="00:24:53">[00:24:53]</a>.
*   "Gentle" easing is a good default, providing a subtle bounce <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>.
*   Adjust the animation duration (e.g., 400ms) <a class="yt-timestamp" data-t="00:25:06">[00:25:06]</a>.

## Enhancing Visuals for Interactivity

### Adding Shadows for "Lift"
A common UI pattern involves giving elements a subtle "lift" or "pop" effect on hover <a class="yt-timestamp" data-t="00:25:34">[00:25:34]</a>. Instead of manually tweaking drop shadows, which can be tedious and difficult to get right <a class="yt-timestamp" data-t="00:25:40">[00:25:40]</a>, consider using plugins. The [[using_plugins_for_enhanced_design_capabilities_in_figma | Smooth Shadow plugin]] is recommended for creating beautiful, easing-curved shadows with adjustable transparency (alpha) <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>.

### Using Inner Shadows for Depth and Curvature
Inner shadows can add visual interest, depth, and a rounded feel to corners, making objects appear as if light is shining over their edges <a class="yt-timestamp" data-t="00:33:17">[00:33:17]</a>.
1.  Add an inner shadow effect to your component <a class="yt-timestamp" data-t="00:33:39">[00:33:39]</a>.
2.  Set the shadow color to white for a lighting effect <a class="yt-timestamp" data-t="00:33:51">[00:33:51]</a>.
3.  Adjust the X and Y values (e.g., around 28 for Y) and decrease opacity for a softer look <a class="yt-timestamp" data-t="00:33:57">[00:33:57]</a>.
4.  Pair it with another inner shadow at the bottom, using a negative Y value (e.g., -2) and a slightly darker shade if in dark mode <a class="yt-timestamp" data-t="00:34:13">[00:34:13]</a>.

## Efficiency Tips for Prototyping

*   **Real-time Preview**: Always view your design at 1x scale on a separate monitor or laptop in prototype mode while making changes <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>. This ensures you're seeing the design as users would experience it <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.
*   **[[creating_and_using_components_in_figma | Components]] and Auto Layout**: Figma's component system allows for making changes in one place that propagate everywhere <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. [[creating_and_using_components_in_figma | Auto Layout]] mimics CSS Flexbox, making designs easy to build and control spacing <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a> and allowing for dynamic adjustments when content changes <a class="yt-timestamp" data-t="00:27:58">[00:27:58]</a>. Using Auto Layout is also a [[best_practices_for_designing_in_figma | best practice]] that aligns with how developers would build the interface in CSS <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.
*   **Multi-Edit Variants**: Use the "Multi-edit variants" icon or hotkey `Q` to make changes across all component variants simultaneously, preventing redundant work <a class="yt-timestamp" data-t="00:27:03">[00:27:03]</a>.

## Figma's Role in the Design Workflow

Figma is excellent for generative design, allowing designers to quickly produce and explore a wide range of ideas <a class="yt-timestamp" data-t="00:35:53">[00:35:53]</a>. It enables rapid iteration and the exploration of divergent ideas that might feel "tame" or "templated" in other tools <a class="yt-timestamp" data-t="00:36:01">[00:36:01]</a>.

### Comparison with Code-Based Tools
While Figma is ideal for initial exploration and pushing visual concepts <a class="yt-timestamp" data-t="00:36:12">[00:36:12]</a>, tools like Framer or Vzero are often used for the final stages of a project, especially when moving towards code-based implementation <a class="yt-timestamp" data-t="00:36:26">[00:36:26]</a>. The distinction between high-fidelity design in Figma and high-fidelity code is blurring <a class="yt-timestamp" data-t="00:38:11">[00:38:11]</a>.

> "Figma is almost like a piece of paper and you have a a a pen and you're drawing actually you don't even have a pen you have a a pencil you're sketching out your idea..." <a class="yt-timestamp" data-t="00:37:13">[00:37:13]</a>

### Learning and Best Practices
The most effective way to learn Figma is by actively using the tool <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>. Start by drawing a frame (`F` hotkey) and begin experimenting <a class="yt-timestamp" data-t="00:39:43">[00:39:43]</a>.