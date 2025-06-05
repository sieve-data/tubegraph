---
title: Implementation of keyframe animations in SVG
videoId: UTHgr6NLeEw
---

From: [[fireship]] <br/> 

[[implementing_svg_for_scalable_vector_graphics | Combining scalable vector graphics]] (SVG) with [[css_transforms_for_complex_animations | CSS animation]] is a powerful technique for web designers to stand out [00:00:01]. Examples include animated duotone icons on the Stripe homepage or looping [[creating_wavy_backgrounds_with_svg_and_css | animated explainer sequences]] on the Gatsby homepage [00:00:09]. Creating such animations does not require expertise in design, animation, or development [00:00:17].

Two main types of [[creating_interactive_svg_animations | animated SVG]] applications can be built using just SVG and [[techniques_for_svg_styling_with_css_and_javascript | CSS]]: an [[creating_interactive_svg_animations | animated icon]] that a user can interact with, and a looping [[creating_wavy_backgrounds_with_svg_and_css | animated sequence]] [00:00:24].

## Understanding SVG for Animation

[[implementing_svg_for_scalable_vector_graphics | Scalable Vector Graphics]] differ from raster images like PNGs or JPEGs, which represent images using a grid of pixels where resolution depends on pixel count [00:00:43]. In contrast, a vector image uses a geometry and math-based approach instead of static pixels [00:01:02].

An SVG file resembles HTML markup when opened in an editor [00:01:08]. The `<svg>` tag includes a `viewBox` attribute that defines a grid [00:01:13]. Graphics computed within this grid can be scaled to any size because it involves multiplying the math in that grid by the image resolution [00:01:17].

Inside the SVG tags, various elements like `rect`, `circle`, and `polygon` draw basic shapes [00:01:25]. These shapes have attributes to define their XY coordinates and size [00:01:31]. The `path` element is the most powerful, allowing definition of any sequence of lines and curves [00:01:35].

While it's beneficial to understand SVG structure, manually writing graphics code is rarely necessary [00:01:44]. Instead, graphic designers typically use tools like Figma, Illustrator, or Inkscape, which can export vector graphics to the SVG format [00:01:49]. Once a graphic is drawn, it can be styled with [[techniques_for_svg_styling_with_css_and_javascript | CSS]] and made interactive with [[techniques_for_svg_styling_with_css_and_javascript | JavaScript]] [00:02:00].

### Exporting SVG from Design Tools

When exporting SVG for animation:
*   Ensure that ID attributes are included in the export (this makes the file larger but easier to work with [[techniques_for_svg_styling_with_css_and_javascript | CSS]]) [00:04:57].
*   Uncheck any option to show the frame fill color in the export [00:05:06].
*   Copy the generated SVG markup directly into your HTML file [00:05:30]. This allows for custom styling and animation [00:05:31].

## Implementing Keyframe Animations in SVG

Unlike animations created with the `transition` property, which automatically animate properties when styling changes [00:06:40], [[animating_ui_elements_with_css_keyframes | keyframe animations]] are required for looping animations that run in the background without user interaction [00:08:38].

### Basic Keyframe Animation

To create a [[key_framed_animations_in_angular | keyframe animation]]:
1.  **Define the `@keyframes` rule:** Specify a name for the animation (e.g., `fadeInUp`) [00:09:28].
2.  **Define animation stages:** Use `from` and `to` (or percentages like `0%` and `100%`) to set properties at the beginning and end of the animation [00:09:40].
    *   Example: For an element to fade upwards, start with `opacity: 0` and `transform: translateY(20%)` at `from` [00:09:50].
    *   At `to`, set `opacity: 1` and `transform: translateY(0)` to bring it back to its original position [00:10:00].
3.  **Apply to an element:** Use the `animation` CSS property on the target SVG element (or group) [00:09:34].
    *   Specify the `animation-name` and `animation-duration` (e.g., `animation: fadeInUp 1s;`) [00:09:37].

### Looping and Staggered Animations

For a looping animation that runs continuously, add the `infinite` value to the `animation` property [00:10:38].

For [[animating_ui_elements_with_css_keyframes | staggered animations]], where elements appear in sequence:
1.  **Group elements:** In the design tool, create separate groups for elements that will be staggered, potentially numbering them based on their desired appearance order [00:09:06]. Figma creates `g` elements in the SVG code for groups, acting like `div`s for grouping and styling [00:04:10].
2.  **Define [[animating_ui_elements_with_css_keyframes | keyframe animations]] for individual elements:** Create a [[key_framed_animations_in_angular | keyframe animation]] (e.g., `dropIn`) that describes how a single element should animate [00:10:19].
    *   Set `animation-direction: forwards` to ensure the element holds its final position after the animation ends [00:10:33].
    *   Carefully consider the entire duration of the looping animation (e.g., 8 seconds), and set keyframes to hold properties at desired intervals (e.g., appearing between 20% and 30%, then holding that state until 100%) [00:10:46].
3.  **Use CSS variables for delay:** Define inline [[techniques_for_svg_styling_with_css_and_javascript | CSS]] variables directly in the SVG markup for each element that needs a staggered delay [00:11:21].
    *   Example: `<g id="bolt-1" style="--order: 1;"></g>` [00:11:34].
4.  **Calculate `animation-delay`:** In the main stylesheet, use the `calc()` function with the CSS variable to dynamically set the `animation-delay` [00:11:47].
    *   Example: `animation-delay: calc(var(--order) * 200ms);` [00:11:51]. This makes each subsequent element start its animation 200 milliseconds after the previous one [00:11:59].

By applying these techniques, complex [[creating_wavy_backgrounds_with_svg_and_css | animated SVG]] sequences can be created [00:12:03].