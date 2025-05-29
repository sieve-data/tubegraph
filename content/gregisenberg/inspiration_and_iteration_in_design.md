---
title: Inspiration and iteration in design
videoId: XoOx5xPdv4M
---

From: [[gregisenberg]] <br/> 

A live design session demonstrated a professional's approach to designing an app, focusing on rapid iteration and drawing from a well-maintained library of inspiration <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. The goal was to provide a window into the design process, highlighting considerations, visual improvements, and basic prototyping <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. The specific design task involved creating a course marketplace page for dive.club <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

## The Iterative Design Process

The core philosophy of the designer is to avoid doing the same thing twice and to minimize "turning knobs" to make changes <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. This is achieved through aggressive use of Figma components and iterative workflows.

### Starting with Components for Rapid Iteration
The first step in designing a new element, like a course card, is to create a frame and immediately turn it into a component <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. This allows for quick duplication and styling, as changes to the main component reflect across all instances <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. This "hacky speed mechanism" allows for much faster iteration <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

### Preserving Iterations with the "Destroyer" Plugin
When exploring different design directions, the designer duplicates the entire frame and then uses a plugin called "Destroyer" to "destroy instances" <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. This removes all component links within the duplicated frame, freezing that iteration in time and allowing the designer to continue experimenting with the main component without losing previous versions <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. This workflow ensures that the leftmost frame always represents the current source of truth <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. The designer often goes through this process 14-15 times in an exploration phase, or even 20 times when actively designing <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a> <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.

### Multi-Edit Mode
Figma's multi-edit variants feature (activated by hitting `Q`) allows designers to make changes across multiple instances of a component simultaneously, further preventing redundant work <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>.

## The Role of Inspiration in Design

The designer emphasizes that they are constantly seeking inspiration <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. Rather than starting from a blank page, they maintain a Notion database where they continuously dump and categorize design ideas <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. This practice is akin to "writing from abundance," where ideas are drawn from a rich, pre-existing database rather than being sought out on demand <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

If no specific ideas come to mind, the first step is to open the Notion database, copy relevant images, and paste them into Figma <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. Designers are seen as "collectors of design" rather than just creators <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. The key is to notice what you like, observe the small details, and constantly ask why you like something when you see it <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.

## Key Principles and Techniques

### [[Prototyping and interactivity with Figma]]
*   **Frames (F)**: Basic containers, similar to a CSS `div`, for holding design elements <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   **Auto Layout (Shift + A)**: Allows grouping of elements into flexible stacks, directly mapping to CSS Flexbox, enabling responsive and organized designs <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a> <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.
*   **Components and Variants**: Creating a component and adding variants (e.g., a "hover" state) enables [[Prototyping and interactivity with Figma]] interactions <a class="yt-timestamp" data-t="00:23:27">[00:23:27]</a>.
*   **Smart Animate**: When connecting component variants in prototype mode, selecting "Smart Animate" creates smooth transitions between states <a class="yt-timestamp" data-t="00:24:53">[00:24:53]</a>.
*   **Real-time Prototype View**: Observing the design in real-time at 1x scale on a separate device (like a laptop) while making changes is crucial for understanding how the design "feels" <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.

### Visual Improvements and Styling
*   **Opacity (Number Keys)**: Quickly adjust opacity of selected elements by typing numbers (e.g., `6` for 60%, `0` for 100%) <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Image Handling**: Rectangles (`R`) can be filled with images from the clipboard <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. Figma's built-in "Remove Background" feature (Command + K) can be applied to images <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
*   **Layer Blur**: Adding a blur effect to a colored rectangle placed behind an element can create an "interesting visual effect" by simulating lighting <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.
*   **Blend Modes**: Applying blend modes (e.g., Luminosity) can allow underlying colors to bleed through, creating tinted effects <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>. This is directly from CSS <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>.
*   **Noise and Texture**: Adding a subtle layer of noise or graininess (using the "Noise and Texture" plugin) can add significant [[User experience and design strategies for app development | visual interest]] and texture <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>.
*   **Inner Shadows**: Using inner shadows can create a sense of depth and curvature, making elements appear to round and bend, a common trend in modern designs <a class="yt-timestamp" data-t="00:33:11">[00:33:11]</a> <a class="yt-timestamp" data-t="00:34:57">[00:34:57]</a>.

### Plugin Recommendations
The designer uses relatively few plugins, categorizing them into two buckets:
1.  **Visual Effects**:
    *   **Noise and Texture**: For adding graininess or complex shaders <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a> <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>.
    *   **Smooth Shadow**: For generating aesthetically pleasing multi-layered drop shadows, which are difficult to create manually <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>.
2.  **Workflows**:
    *   **Destroyer**: For preserving design iterations by removing component links <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a> <a class="yt-timestamp" data-t="00:30:29">[00:30:29]</a>.
    *   **Content Reel**: For quickly populating designs with realistic content like avatars or text, often used in conjunction with "Select Similar Layers" <a class="yt-timestamp" data-t="00:30:44">[00:30:44]</a>.
    *   **Select Similar Layers**: Helps select multiple layers with similar properties (e.g., all images) to make bulk changes <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>.
*   **Phosphor**: A favored plugin for sourcing consistent and beautiful icons <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.

The speaker notes that Figma's native workflow enhancements have reduced the need for many plugins that previously existed <a class="yt-timestamp" data-t="00:32:40">[00:32:40]</a>.

## Figma in a Code-Based World
While tools like V0.dev (AI-powered design to code) and Framer (web design and prototyping tool) are emerging, Figma still holds a critical role <a class="yt-timestamp" data-t="00:35:32">[00:35:32]</a>. Figma is ideal for generative design, allowing for quick iteration and the exploration of diverse, non-templated ideas <a class="yt-timestamp" data-t="00:35:53">[00:35:53]</a>. It serves as the "piece of paper" for sketching and exploring ideas, while code-based tools are for building and refining the final product <a class="yt-timestamp" data-t="00:37:13">[00:37:13]</a>.

The line between high-fidelity design in Figma and corresponding code is blurring, suggesting Figma might move to a lower-fidelity, exploratory role in the future <a class="yt-timestamp" data-t="00:38:09">[00:38:09]</a>. However, it remains the best place to start for creative exploration <a class="yt-timestamp" data-t="00:37:48">[00:37:48]</a>.

The most effective way to learn Figma is to actively engage with the tool: "open up a new file, just type F on your keyboard and draw it somewhere on the page, you're in it now" <a class="yt-timestamp" data-t="00:39:43">[00:39:43]</a>.