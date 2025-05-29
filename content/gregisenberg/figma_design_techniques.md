---
title: Figma design techniques
videoId: XoOx5xPdv4M
---

From: [[gregisenberg]] <br/> 

This article explores key techniques and workflows for designing in Figma, as demonstrated in a live design session. The goal is to provide best practices for iterating quickly and creating visually appealing designs, even for those working on their own startup ideas <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. The session focuses on designing a course marketplace page for dive.Club <a class="yt-timestamp" data-t="01:46">[01:46]</a>.

## Starting a Design in Figma

### Creating a Base Element: The Frame
The fundamental building block in Figma is the "frame" <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   To create a frame, hit the `F` key <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   A frame acts as a container, similar to a CSS `div` <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   Start by defining a main container, such as a "course card" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

### Leveraging [[creating_and_using_components_in_figma | Components]] for Speed
A "hacky" approach to accelerate design in Figma is to turn an empty frame into a component immediately <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   While components are often associated with Design Systems, they are invaluable for rapid iteration to avoid repetitive tasks <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   By duplicating a component, any changes made to the master component will automatically apply to all instances <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This means only one "knob" needs to be turned to make changes <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Introducing Auto Layout
Auto Layout, activated by hitting `Shift + A`, allows for dynamic arrangement of elements <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   It functions much like Flexbox in CSS, allowing control over spacing, alignment, and distribution of items within a container <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   Auto Layout is crucial for designs that translate well to code <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>. Randomly positioning elements without it is equivalent to absolute positioning in CSS, which is generally undesirable <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.

## Core Design Workflow and Practices

### Iterative Design
The design process is highly iterative, often involving multiple explorations that might be discarded <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   It's common to dislike an initial design after exploration (e.g., "I hate this, I don't think it looks good at all") <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. This happens frequently (14-15 times in an exploration process) <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
*   To preserve iteration states, duplicate the main frame and then use the "Destroyer" plugin to detach instances from the main component, effectively "freezing" that version in time <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. This allows for continuous experimentation in the "source of truth" frame <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.

### [[inspiration_and_design_process | Inspiration and Design Process]]
*   **Constant Collection:** Always be collecting inspiration <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. Maintain a database (e.g., Notion) to dump and categorize design examples <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
*   **"Writing from Abundance":** Similar to David Perell's concept for writing, designers should constantly contribute to a database of ideas rather than starting from a blank page <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   **Recreation and Adaptation:** If lacking ideas, open the inspiration database, copy and paste images into Figma, and then recreate parts of them, potentially adapting them in new ways <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   **Observation:** Be observant of details you like in designs, and constantly ask "why" you like something <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.

### Considering Engineering Implementation
Design decisions should often consider how the product will be built <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.
*   Using Figma's Auto Layout inherently makes designs easier to build in CSS Flexbox <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.
*   When setting spacing or padding, aim for values that are multiples of eight, as this aligns well with modern web frameworks like Tailwind CSS <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.

### Dynamic Content and Text
*   Always structure text with defined text styles (e.g., "title," "instructor name") <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. These can be pulled from popular websites or frameworks like Tailwind CSS for consistency <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   Metadata, such as course length or price, should be incorporated into the design, treating it like data in a spreadsheet <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
*   Use number keys (0-9) to quickly adjust opacity of selected elements <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. For example, `6` sets opacity to 60%, `0` to 100%, `05` to 5% <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

## Visual Enhancements in Figma

### Images
*   Hit `R` to draw a rectangle <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. Images can be pasted directly from the clipboard into a rectangle's fill <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
*   **Remove Background:** Figma has a built-in feature to remove backgrounds from images. Access it by pressing `Command + K` (quick actions) and typing "remove background" <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

### Lighting and Blur Effects
*   **Layer Blur:** Add depth and visual interest by placing a colored rectangle behind an element, applying a "Layer blur" effect, and adjusting its value <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.
*   **Blend Mode - Luminosity:** Apply the "Luminosity" blend mode (found under "Apply blend mode") to an image to let underlying colors bleed through, creating a tinted black-and-white effect <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>.

### Noise and Texture
*   Adding a subtle layer of noise and texture can significantly enhance a design's visual interest <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>.
*   Create a rectangle covering the desired area and use the "Noise and Texture" plugin to add graininess <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>. Adjust opacity to make it subtle <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>.

### Shadows
*   **Smooth Shadow Plugin:** For aesthetically pleasing shadows, use the "Smooth Shadow" plugin <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>. It offers easing curves and alpha adjustments for fine-tuning <a class="yt-timestamp" data-t="00:26:12">[00:26:12]</a>.
*   **Inner Shadows:** To create a sense of depth and rounded corners, add inner shadows <a class="yt-timestamp" data-t="00:33:19">[00:33:19]</a>. Apply a light inner shadow from the top and a darker one from the bottom to mimic lighting and curvature <a class="yt-timestamp" data-t="00:33:43">[00:33:43]</a>. This subtle effect is common in high-quality modern designs <a class="yt-timestamp" data-t="00:34:36">[00:34:36]</a>.

## [[prototyping_and_animations_in_figma | Prototyping and Animations in Figma]]

To make designs interactive and feel realistic, quick prototyping is essential <a class="yt-timestamp" data-t="00:22:52">[00:22:52]</a>.
*   **Hover States:**
    1.  Select a component and click "Add Variant" in the top right to create a "hover" state <a class="yt-timestamp" data-t="00:23:27">[00:23:27]</a>.
    2.  Make desired visual changes to the hover variant (e.g., increase blur, change background, adjust border) <a class="yt-timestamp" data-t="00:23:58">[00:23:58]</a>.
    3.  Switch to "Prototype" mode <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a>.
    4.  Drag a blue dot from the default state to the hover state <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>.
    5.  Set the interaction trigger to "While hovering" <a class="yt-timestamp" data-t="00:24:38">[00:24:38]</a>.
    6.  Choose "Smart animate" for smooth transitions <a class="yt-timestamp" data-t="00:24:53">[00:24:53]</a>. "Gentle" easing with a duration around 400ms is often a good default <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>.
*   **Real-time Preview:** Always have the design open in prototype mode on a separate screen (e.g., laptop) to see changes in real-time at 1x scale <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.

## [[figma_plugins_and_workflow_enhancements | Figma Plugins and Workflow Enhancements]]

While some designers use many plugins, the focus should be on those that enhance workflow or create visual effects not easily achievable manually <a class="yt-timestamp" data-t="00:29:50">[00:29:50]</a>.

### Recommended Plugins:
*   **Visual Effects:**
    *   **Noise and Texture:** For adding graininess and other unique visual textures <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>.
    *   **Smooth Shadow:** For generating complex, layered shadows that look professional <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>.
*   **Workflow Enhancements:**
    *   **Destroyer:** Removes all component instances in a frame, "freezing" that design state for iterative exploration <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.
    *   **Content Reel:** Populates designs with various types of content (e.g., avatars, text, images), useful for filling tables or designs quickly <a class="yt-timestamp" data-t="00:30:44">[00:30:44]</a>.
    *   **Select Similar Layers:** Selects multiple layers based on criteria like name, making it easy to apply bulk changes (e.g., changing all images) <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>.

### Keyboard Shortcuts
*   `F`: Create a frame <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>
*   `Shift + A`: Apply Auto Layout <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>
*   `Command + D`: Duplicate selected elements <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>
*   `R`: Draw a rectangle <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>
*   `Command + K`: Open quick actions menu (for plugins or built-in features) <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>
*   `Command + [` / `Command + ]`: Move selected layer down/up in the layer tree <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>
*   `Enter`: Drill into layers on the canvas <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>
*   `Shift + Enter`: Move back up the layer tree <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>
*   `Q`: Toggle multi-edit variants mode (for editing multiple component variants simultaneously) <a class="yt-timestamp" data-t="00:27:07">[00:27:07]</a>
*   `T`: Create a text layer <a class="yt-timestamp" data-t="00:27:35">[00:27:35]</a>

## Figma's Role in Evolving Design Workflows

### Figma vs. AI/Code-based Tools (e.g., V0, Framer)
Figma remains excellent for generative design and rapidly exploring many divergent ideas <a class="yt-timestamp" data-t="00:35:53">[00:35:53]</a>.
*   AI tools like V0 tend to produce more templated or "tame" designs, limiting the ability to push visual boundaries <a class="yt-timestamp" data-t="00:36:06">[00:36:06]</a>.
*   Figma is akin to sketching with a pencil on paper; it's the ideal starting point for exploring concepts <a class="yt-timestamp" data-t="00:37:13">[00:37:13]</a>.
*   For web design, a workflow might involve:
    1.  Using Figma to explore a wide array of initial ideas and throw "paint at the wall" <a class="yt-timestamp" data-t="00:36:31">[00:36:31]</a>.
    2.  Transitioning to tools like Framer to build out the final 5-10% of the design in a code-based medium, and for developing subsequent pages <a class="yt-timestamp" data-t="00:36:42">[00:36:42]</a>.
*   The distinction between high-fidelity design in Figma and high-fidelity code is blurring <a class="yt-timestamp" data-t="00:38:09">[00:38:09]</a>. As AI tools advance, Figma's role might shift even further towards lower-fidelity exploration, with AI tools handling the high-fidelity translation to code <a class="yt-timestamp" data-t="00:38:14">[00:38:14]</a>.

## Conclusion: Learning and Practicing
The best way to learn Figma and design is to "get your hands dirty" and actively experiment with the tools <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>. Don't just watch; open a new file, hit `F`, and start drawing <a class="yt-timestamp" data-t="00:39:43">[00:39:43]</a>.