---
title: Creating interactive SVG animations
videoId: UTHgr6NLeEw
---

From: [[fireship]] <br/> 

[[Implementing SVG for scalable vector graphics | Combining Scalable Vector Graphics (SVG)]] with [[CSS transforms for complex animations | CSS animation]] is a powerful technique for web designers to create standout web experiences <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. Examples include the [[techniques_for_svg_styling_with_css_and_javascript | animated duotone icons]] on the Stripe homepage or looping animated explainer sequences on the Gatsby homepage <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. These effects do not require expert design, animation, or development skills <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This guide will cover how to build an animated icon that a user can interact with, and a looping animated sequence, all powered by SVG and CSS <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## What is a Scalable Vector Graphic (SVG)?

An SVG is fundamentally different from raster images like PNGs or JPEGs <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. Raster images represent an image as a grid of pixels, meaning their resolution depends on the number of pixels <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. To achieve higher resolution, a larger pixel matrix is required <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

In contrast, a vector image uses a geometry and math-based approach instead of static pixels <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

### SVG Structure

When opened in an editor, an SVG file appears as HTML-like markup <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The core element is the `<svg>` tag, which includes a `viewBox` attribute that defines a grid <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Any graphics computed within this grid can be scaled to any size because it merely involves multiplying the mathematical definitions in that grid by the desired image resolution <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

Inside the SVG tags, various elements draw basic shapes <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>:
*   `rect` (rectangle) <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>
*   `circle` <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>
*   `polygon` <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>

These shapes have attributes defining their x, y coordinates, and size <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. The `path` element is the most powerful, allowing the definition of any sequence of lines and curves <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

While it's helpful to understand SVG's internal structure, you typically won't write the graphics code by hand <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Instead, graphic designers use tools like Figma, Illustrator, or Inkscape, which can export vector graphics to the SVG format <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

## Integrating SVG with CSS and JavaScript

Once a graphic is drawn, it can be manipulated by [[SVG and CSS integration | integrating CSS]] for styling and JavaScript for interaction <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

### Building an Animated SVG Icon (Interactive)

To follow along, you'll need an HTML file and a design tool like Figma that can export SVG <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

#### Reverse Engineering Animations

Chrome DevTools offers an "Animations" tab (accessible via Command+P or Ctrl+P) that records page animations <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This feature provides a breakdown of keyframes and affected elements, allowing you to pause, slow down, and inspect animations <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. This is useful for analyzing how complex animations are structured, including SVG code <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. For example, analyzing a Stripe homepage icon revealed it was composed of four triangles, with two initially hidden off-canvas <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

#### Designing the Graphic in Figma

1.  **Create a Frame**: In Figma, create a frame (equivalent to SVG's `viewBox`) <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. A 120x100 unit canvas is recommended for pixel-perfect alignment <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
2.  **Draw Shapes**: Use the polygon tool to draw three triangles <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. Assign one a different color and decrease the opacity of all to make them semi-transparent <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
3.  **Name Layers**: Figma automatically creates layer names <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. For layers intended for [[techniques_for_svg_styling_with_css_and_javascript | CSS styling]] or animation, assign custom names (e.g., `dark1`, `dark2`, `light1`) <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. Figma will use these as `id` attributes upon export, making them easy to target with CSS <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
4.  **Group Elements**: For duotone icons, group elements by color <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. Grouping creates a `<g>` element in SVG, similar to an HTML `div` for containment and styling <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. Name these groups (e.g., `dark-group`, `light-group`) <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
5.  **Initial Positioning**: Position the light triangle first, then the dark triangle on top <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. The second dark triangle, initially off-screen, should also be positioned directly on top for now, as its initial off-screen state will be handled by CSS <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

#### Exporting from Figma

Export the Figma frame to SVG format <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. Ensure "Include ID attributes" is checked to preserve custom layer names as IDs <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. Uncheck "Show frame fill color" on export <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

#### Embedding and Styling SVG in HTML

1.  **Embed SVG**: Copy the exported SVG markup directly into your HTML file's `<body>` <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This allows for custom [[techniques_for_svg_styling_with_css_and_javascript | styling and animation]] <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
2.  **Remove Inline Fills**: SVG paths often include inline `fill` attributes <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. Remove these from the SVG code, as inline styles are difficult to override <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. The elements will become invisible initially <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
3.  **Use CSS Variables for Theming**: In a `<style>` tag, define CSS variables on the root element for colors (e.g., `--dark-color`, `--light-color`) <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Then, assign these variables to the SVG groups using their IDs (e.g., `#dark-group { fill: var(--dark-color); }`) <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. This makes the icon easily themeable <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

### CSS Transitions for Hover Effects

To animate the icon on hover:
1.  **Select Elements**: Target the triangles to animate using their IDs <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
2.  **Apply Transitions**: Use the `transition` property on these elements to automatically animate all properties over a specified duration (e.g., `transition: all 1s ease;`) <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
3.  **Initial Positioning**: Position the second dark triangle off-screen by setting its `transform: translateX(-100%)` <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
4.  **Define Hover States**: Target the `:hover` event on the SVG itself <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
    *   **Light Triangle**: Translate it slightly to the right <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
    *   **Dark Triangle**: Translate it to the right and change its `opacity` to `0` to fade it out <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
    *   **Second Dark Triangle**: Bring it into view by setting `transform: translateX(0%)` <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

Now, hovering over the icon will trigger the animation <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

### JavaScript for Click Interactions

To change the icon's styling dynamically on click:
1.  **Add Script Tag**: Include a `<script>` tag before the closing `</body>` tag <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
2.  **Select Element**: Get a reference to the SVG element (or a group within it) using `document.getElementById()` <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
3.  **Define Click Handler**: Create a function to be called on the click event <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
4.  **Change CSS Variables**: Inside the function, define an array of colors <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. Implement a function to randomly select a color from this array <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
5.  **Update Document Styles**: Change the CSS variables defined earlier by targeting `document.documentElement.style.cssText` <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. This will update the `--dark-color` and `--light-color` variables <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

Because of the `transition: all` property, the color change will also be animated, providing a smooth transition <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

## Looping Animations with Keyframes

For animations that run continuously in the background without user interaction, [[implementation_of_keyframe_animations_in_svg | keyframe animations]] are required <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.

### Implementing Keyframe Animations

Consider an animation sequence: a phone outline appears, then skeleton text fades in from the bottom, followed by icons dropping in a staggered motion from the top <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. This typically involves grouping elements in Figma (e.g., `phone`, `skeleton-text`, `bolt-icons`) and numbering individual icons for staggering <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

1.  **Export and Embed**: Export the graphic from Figma and embed it directly into your HTML <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
2.  **Define Keyframes**: Use `@keyframes` to define an animation <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
    *   **`fade-in-up` example**:
        *   `from` (0%): `opacity: 0; transform: translateY(20%);` <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>
        *   `to` (100%): `opacity: 1; transform: translateY(0%);` <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>
3.  **Apply Animation**: Apply the keyframe animation to an SVG group using the `animation` property (e.g., `animation: fade-in-up 1s;`) <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
    *   `animation-direction: forwards;` tells the animation to hold its final state <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
    *   `infinite` value allows the animation to loop continuously <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.

For looping, staggered animations, carefully consider the full duration of the animation (e.g., 8 seconds) <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. Define keyframe percentages to control when elements appear and hold their positions (e.g., not appearing for the first 20%, dropping in between 20% and 30%, then holding position until 100%) <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

### Staggered Keyframe Animations

To stagger animations:
1.  **Inline CSS Variables**: Define inline CSS variables directly on each element within the SVG `<g>` groups that need staggering <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. For example, `style="--order: 1;"` <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>. These inline variables have higher priority <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
2.  **`animation-delay` with `calc()`**: In your CSS, use the `animation-delay` property combined with `calc()` to dynamically calculate the delay based on the `--order` variable <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. For instance, `animation-delay: calc(var(--order) * 200ms);` will make each icon drop in 200 milliseconds after the previous one <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.

This approach allows for impressive [[animated_morphing_svg_with_javascript | animated SVG]] that can enhance web design and user engagement <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.