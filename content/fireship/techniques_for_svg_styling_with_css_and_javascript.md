---
title: Techniques for SVG styling with CSS and JavaScript
videoId: UTHgr6NLeEw
---

From: [[fireship]] <br/> 

Combining [[implementing_svg_for_scalable_vector_graphics | scalable vector graphics]] with [[css_for_styling_and_layout | CSS animation]] is a powerful technique for web designers to create unique and engaging experiences <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. Examples include the animated duotone icons on the Stripe homepage or the looping animated explainer sequences on the Gatsby homepage <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. These effects can be achieved without being an expert designer, animator, or developer, primarily using [[implementing_svg_for_scalable_vector_graphics | SVG]] and [[css_for_styling_and_layout | CSS]] <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Understanding Scalable Vector Graphics (SVG)

[[implementing_svg_for_scalable_vector_graphics | Scalable Vector Graphics]] are fundamentally different from raster images like PNGs or JPEGs <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   **Raster Images**: Represent images as a grid of pixels, where resolution is dependent on the number of pixels <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. Higher resolution requires a larger matrix of pixels <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **Vector Images**: Use a geometry and math-based approach, not static pixels <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

An [[implementing_svg_for_scalable_vector_graphics | SVG]] file appears as HTML-like markup <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
*   The `<svg>` tag contains a `viewBox` attribute that defines a grid <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Graphics computed within this grid can be scaled to any size because it's based on multiplying mathematical values <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   Inside the `<svg>` tags, elements like `rect`, `circle`, and `polygon` draw basic shapes <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. These shapes have attributes defining their `xy` coordinates and size <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   The `path` element is the most powerful, allowing definition of any sequence of lines and curves <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

While it's good to understand the structure, you rarely need to write the graphics code by hand <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Graphic designers typically create these in tools like Figma, Illustrator, or Inkscape, which can then export to [[implementing_svg_for_scalable_vector_graphics | SVG]] format <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

## [[SVG and CSS integration | Integrating SVG with CSS and JavaScript]]

Once an [[implementing_svg_for_scalable_vector_graphics | SVG]] graphic is created, it can be enhanced by [[SVG and CSS integration | integrating CSS for styling]] and JavaScript for interaction <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. This process involves creating an HTML file and using a design tool that can export [[implementing_svg_for_scalable_vector_graphics | SVG]], like Figma <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

### Reverse Engineering Animations

Chrome Dev Tools' "Animations" tab is highly useful for inspecting impressive animations on other websites <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. It records page animations, breaks down keyframes, and shows affected elements <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. This allows users to pause, slow down, and jump to elements in the DOM <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>, and even copy [[implementing_svg_for_scalable_vector_graphics | SVG]] code <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

### Preparing SVG for Styling and Animation

1.  **Drawing Graphics**: Use a tool like Figma to create a frame (equivalent to `viewBox`) <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. Design on the smallest possible frame for pixel-perfect alignment <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
2.  **Naming Layers**: Give custom names to layers intended for [[css_for_styling_and_layout | CSS styling]] or animation (e.g., `dark1`, `dark2`, `light1`) <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. Figma exports these names as `id` attributes on [[implementing_svg_for_scalable_vector_graphics | SVG]] elements, making them targetable by [[css_for_styling_and_layout | CSS selectors]] <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
3.  **Grouping Elements**: For duotone icons or complex animations, group elements by color or function <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. Figma creates a `<g>` element (similar to an HTML `div`) for groups, which acts as a container for styling <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
4.  **Exporting from Figma**:
    *   Select the frame and choose `SVG` format <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
    *   Ensure "Include ID attributes" is checked to make it easier to work with [[css_for_styling_and_layout | CSS]] <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
    *   Uncheck "Show frame fill color" on export <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
5.  **Embedding SVG in HTML**: Copy the exported [[implementing_svg_for_scalable_vector_graphics | SVG]] markup directly into the HTML `<body>` <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This allows for custom [[css_for_styling_and_layout | styling]] and animation, unlike using an `<img>` tag <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

## Styling SVG with CSS

### Themeable Duotone Icons with CSS Variables
To make [[implementing_svg_for_scalable_vector_graphics | SVG]] icons easily themeable, remove inline `fill` attributes from the [[implementing_svg_for_scalable_vector_graphics | SVG]] code <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. Then, define [[css_for_styling_and_layout | CSS variables]] on the root element (e.g., `:root`) for colors (e.g., `--dark-color`, `--light-color`) <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. These variables can then be assigned to the `fill` property of [[implementing_svg_for_scalable_vector_graphics | SVG]] groups or elements by targeting their `id`s <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

### Animating with CSS Transitions
The [[css_for_styling_and_layout | CSS `transition` property]] can automatically animate changes to element properties <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. Applying `transition: all 1s ease;` to [[implementing_svg_for_scalable_vector_graphics | SVG]] elements tells [[css_for_styling_and_layout | CSS]] to animate all property changes over 1 second with an `ease` timing function <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

For example, to animate an icon on hover:
1.  Initially position elements that should move into view, such as moving a triangle off-screen using `transform: translateX(-100%);` <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
2.  Use the `:hover` pseudo-class on the [[implementing_svg_for_scalable_vector_graphics | SVG]] element to define the end state of the animation for individual triangles <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. This can include:
    *   Changing `transform: translateX()` to move elements <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
    *   Changing `opacity` to fade elements in or out <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

## [[Creating interactive SVG animations | Creating Interactive SVG Animations with JavaScript]]

JavaScript can target events on the [[implementing_svg_for_scalable_vector_graphics | SVG]] itself or individual shapes within it <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   Select [[implementing_svg_for_scalable_vector_graphics | SVG]] elements using `document.getElementById()` <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.
*   Attach event listeners, such as `click`, to call functions that dynamically change [[css_for_styling_and_layout | CSS variables]] <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
*   Change [[css_for_styling_and_layout | CSS variables]] using `document.documentElement.style.cssText` or `element.style.setProperty()` <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. This will update the `fill` colors (or other properties) defined by the variables <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   If a `transition` property is already set on the [[implementing_svg_for_scalable_vector_graphics | SVG]] elements, these JavaScript-triggered color changes will also be animated <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

## [[Implementation of keyframe animations in SVG | Implementing Keyframe Animations in SVG]]

For looping animations that run in the background without user interaction, [[implementation_of_keyframe_animations_in_svg | CSS keyframe animations]] are used <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.

### Basic Keyframe Animation
1.  Define a `@keyframes` rule with a name (e.g., `fade-in-up`) <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
2.  Define the animation's start (`from` or `0%`) and end (`to` or `100%`) states <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. For instance, `from { opacity: 0; transform: translateY(20%); }` and `to { opacity: 1; transform: translateY(0); }` <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
3.  Apply the animation to an [[implementing_svg_for_scalable_vector_graphics | SVG]] group or element using the `animation` property, specifying the name, duration, and easing function <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
4.  To make the animation loop, add the `infinite` value to the `animation` property <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. Use `animation-direction: forwards;` to ensure the final state is maintained after the animation <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

### Staggered Keyframe Animations
To create a staggered animation (e.g., icons dropping in one after another):
1.  Ensure individual [[implementing_svg_for_scalable_vector_graphics | SVG]] elements or groups are identifiable (e.g., by numbered IDs: `bolt-1`, `bolt-2`, etc.) <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
2.  Define the core `drop-in` `@keyframes` animation, considering the overall duration of the loop and when elements should appear, move, and hold their position <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. For example, an 8-second animation might have elements appear between 20% and 30%, then hold their position until 100% <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.
3.  To stagger, define inline [[css_for_styling_and_layout | CSS variables]] directly in the [[implementing_svg_for_scalable_vector_graphics | SVG]] markup for each element (e.g., `style="--order: 1;"`) <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. These inline variables have higher priority <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
4.  In the main [[css_for_styling_and_layout | CSS stylesheet]], use the `animation-delay` property along with the `calc()` function to dynamically calculate the delay based on the `--order` variable <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. For instance, `animation-delay: calc(var(--order) * 200ms);` would make each icon drop in 200 milliseconds after the previous one <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.

This combination of [[implementing_svg_for_scalable_vector_graphics | SVG]], [[css_for_styling_and_layout | CSS transitions]], and [[implementation_of_keyframe_animations in SVG | keyframe animations]] allows for the creation of sophisticated and impressive web animations.