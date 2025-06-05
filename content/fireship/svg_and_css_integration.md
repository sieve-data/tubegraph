---
title: SVG and CSS integration
videoId: UTHgr6NLeEw
---

From: [[fireship]] <br/> 

Combining [[implementing_svg_for_scalable_vector_graphics | scalable vector graphics]] (SVG) with [[css_for_styling_and_layout | CSS animation]] is a powerful [[techniques_for_svg_styling_with_css_and_javascript | technique]] for web designers to create distinctive web experiences <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This approach enables the creation of interactive icons and looping animated sequences powered solely by SVG and [[css_for_styling_and_layout | CSS]] <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. Examples include animated duotone icons on the Stripe homepage and looping animated explainer sequences on the Gatsby homepage <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## What is a Scalable Vector Graphic (SVG)?

An SVG is fundamentally different from raster images like PNGs or JPEGs <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. While raster images represent an image as a grid of pixels, making their resolution dependent on the number of pixels <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>, a vector image uses a geometry and math-based approach instead of static pixels <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

If an SVG file is opened in a text editor, it appears as HTML-like markup <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The core `<svg>` tag includes a `viewBox` attribute that defines a coordinate grid <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Graphics computed within this grid can be scaled to any size because scaling simply involves multiplying the mathematical coordinates in the grid by the desired resolution <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

Inside the `<svg>` tags, various elements like `rect` (rectangle), `circle`, and `polygon` are used to draw basic shapes <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. These shapes have attributes to define their X/Y coordinates and size <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. The `path` element is particularly powerful, functioning like an imaginary pen that can define any sequence of lines and curves <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

While it's good to understand the internal structure of an SVG, manually writing the graphics code is rarely necessary <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Instead, graphic designers typically create SVGs in design tools such as Figma, Illustrator, or Inkscape, all of which can export to the SVG format <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

## Integrating SVG with CSS

Once an SVG graphic has been created, it can be integrated with [[css_for_styling_and_layout | CSS for styling and layout]] and JavaScript for interaction <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

### Embedding SVG in HTML

An SVG file can be used with an HTML `<img>` tag, but declaring the SVG markup directly within the HTML document allows for custom styling and animation <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. When exported from a design tool, SVG markup includes attributes like `fill` that define colors, but these inline styles are difficult to override <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. Deleting inline `fill` colors from the SVG code and defining them with [[css_for_styling_and_layout | CSS variables]] makes the icon easily themeable <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

To make an SVG icon themeable:
1.  Remove `fill` attributes from the SVG path elements <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.
2.  In a `<style>` tag, define [[css_for_styling_and_layout | CSS variables]] (e.g., `--dark-color`, `--light-color`) on the root element <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
3.  Assign these variables to SVG group elements (e.g., using `id` selectors like `#dark-group` and `#light-group`) to control their `fill` properties <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

### Basic CSS Transitions for Interactive Icons

To animate an SVG icon on user interaction, like hovering:
1.  Select the SVG elements to be animated using their `id`s <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
2.  Apply the `transition` property to these elements, specifying `all` properties, a `duration` (e.g., `1s`), and a timing function (e.g., `ease`) <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. This tells [[css_for_styling_and_layout | CSS]] to animate changes to any property automatically <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
3.  Set initial states for elements, for example, by using `transform: translateX(-100%)` to move an element off-screen before the animation starts <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
4.  Target the hover event on the SVG element (e.g., `svg:hover`) <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
5.  Within the hover state, change the `transform` properties (e.g., `translateX(0)`) and `opacity` of individual SVG elements to define their animated states <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

## Integrating SVG with JavaScript for Interactivity

Beyond hover effects, JavaScript can be used to trigger [[creating_interactive_svg_animations | interactive SVG animations]] on events like clicks <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.

To change the styling of an SVG dynamically on click:
1.  Embed a `<script>` tag in the HTML, preferably before the closing `</body>` tag <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
2.  Select the desired SVG element or group using `document.getElementById()` <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
3.  Define a function to be called on its `click` event <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
4.  Within the function, dynamically change the [[css_for_styling_and_layout | CSS variables]] (e.g., `--dark-color`, `--light-color`) that were defined earlier by targeting `document.documentElement.style.cssText` <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
    *   Since a `transition: all` property might already be applied to the SVG elements, color changes triggered by JavaScript will also animate smoothly <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

## Looping Animations with Keyframes

For continuous, looping animations that run without user interaction, [[css_for_styling_and_layout | CSS keyframe animations]] are required <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.

### Simple Keyframe Animation: Fade In Up

1.  Identify the SVG group or element to animate (e.g., skeleton text) <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
2.  Define a `@keyframes` rule with a name (e.g., `fade-in-up`) <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
3.  Inside the `@keyframes` rule, define properties at `from` (0%) and `to` (100%) <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.
    *   `from` (0%): Set initial `opacity` to `0` and use a `transform` (e.g., `translateY(20%)`) to move the element slightly down <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
    *   `to` (100%): Set `opacity` to `1` and `transform` to its original position (e.g., `translateY(0)`) <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
4.  Apply this animation to the SVG group using the `animation` property, specifying the name, duration, and other properties <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.

### Staggered Keyframe Animation

For more complex scenarios, like icons dropping in a staggered motion, careful planning of keyframes and the use of [[css_for_styling_and_layout | CSS variables]] are essential <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.

1.  **Define Keyframes:** Create a `@keyframes` rule (e.g., `drop-in`) that defines the animation over its full duration (e.g., 8 seconds for a looping animation) <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.
    *   Example:
        *   `0%`: `opacity: 0`, `transform: translateY(-20%)` (initially hidden and above the screen) <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
        *   `20%`: (Hold initial state) `opacity: 0`, `transform: translateY(-20%)` <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
        *   `30%`: `opacity: 1`, `transform: translateY(0)` (element drops in) <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
        *   `100%`: (Hold final state) `opacity: 1`, `transform: translateY(0)` (element remains visible) <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
2.  **Apply Animation and Loop:** Apply the `drop-in` animation to the individual elements. Set `animation-direction: forwards` to ensure the animation uses the last keyframe values after it ends, and `animation-iteration-count: infinite` to make it loop continuously <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
3.  **Staggering with CSS Variables:**
    *   In the SVG markup, add inline [[css_for_styling_and_layout | CSS variables]] (e.g., `--order`) to each element that needs to be staggered <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. This gives them a higher priority <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
    *   In the main stylesheet, use the `animation-delay` property <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.
    *   Utilize the `calc()` function with the [[css_for_styling_and_layout | CSS variable]] to dynamically calculate the delay (e.g., `calc(var(--order) * 200ms)`) <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. This ensures each element drops in with a defined delay after the previous one <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.

By mastering these [[techniques_for_svg_styling_with_css_and_javascript | techniques for SVG styling with CSS and JavaScript]], web designers can create highly engaging and responsive visuals <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.