---
title: Animated morphing SVG with JavaScript
videoId: lPJVi797Uy0
---

From: [[fireship]] <br/> 

Creating an animated, morphing SVG can bring a webpage to life, making a flat design into a dynamic, "curvaceous" one <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. This technique allows one SVG shape to smoothly transition into another <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

## Overview and Setup
This approach involves using [[SVG and CSS integration | SVG]] graphics and [[techniques_for_svg_styling_with_css_and_javascript | JavaScript]] to perform the animation <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. While seemingly complex, specialized tools and libraries simplify the process significantly <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

To prepare the environment for this animation, a basic HTML page is used, potentially with [[creating_wavy_backgrounds_with_svg_and_css | wavy backgrounds]] or other [[SVG and CSS integration | SVG]] elements as section separators <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

### HTML Structure
Within a content section, typically one with a distinct background color (e.g., `pink` class), two spacer layers (potentially flipped) are added on either side of where the blob will appear <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. The core of the animation resides in an [[SVG and CSS integration | SVG]] element containing two different "blob" shapes <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

1.  **Generate Blobs:** Use an [[SVG and CSS integration | SVG]] generation tool like "Haikei" to create two distinct "blob" shapes <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
2.  **Extract SVG Paths:** Download the raw [[SVG and CSS integration | SVG]] files and extract the `path` elements (the shape data) from each blob <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. Remove any extraneous elements like `rect` <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
3.  **Combine Paths:** Place both `path` elements within a single [[SVG and CSS integration | SVG]] container in your HTML <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
4.  **Assign IDs:** Assign unique IDs, such as `blob-one` and `blob-two`, to each `path` element <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

```html
<section class="pink">
  <!-- Spacer layers above and below (optional) -->
  <div class="spacer blob-spacer-top flip"></div>

  <svg viewBox="0 0 500 500" xmlns="http://www.w3.org/2000/svg" id="blob-svg">
    <g transform="translate(0 0)">
      <path id="blob-one" d="M410.5 352.5C453.7 266.3 433.8 140.6 371.4 79.5C309 18.4 204.3 -12.4 126.9 29.8C49.5 72 20.3 162.2 28.5 250.7C36.7 339.2 62.3 426.3 147 458.7C231.7 491.1 367.3 438.7 410.5 352.5Z"></path>
      <path id="blob-two" d="M381.5 385C315.8 450.4 213.9 467.5 130.4 429.2C46.9 390.9 0 297.2 0 200.7C0 104.2 46.9 7.4 125.4 0.9C203.9 -5.6 314.9 3.6 397.9 66.4C480.9 129.2 537.9 253.2 492.4 330.1C446.9 407 447.2 319.6 381.5 385Z"></path>
    </g>
  </svg>

  <div class="spacer blob-spacer-bottom"></div>
</section>
```
> **NOTE:** Obtaining the raw [[SVG and CSS integration | SVG]] code and combining paths can be cumbersome; using a design tool like Figma might simplify this <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

### CSS Styling and Positioning
Apply CSS to position the [[SVG and CSS integration | SVG]] blob and manage its visibility.

```css
.pink .blob-svg {
  position: absolute; /* Allows precise placement within the parent section */
  bottom: 0;
  left: 50%;
  transform: translateX(-50%); /* Centers the blob horizontally */
  width: 500px; /* Example size */
  height: 500px; /* Example size */
  z-index: 1; /* Ensures it sits above other elements if necessary */
}

/* Hide the second blob until the animation starts */
#blob-two {
  visibility: hidden;
}
```

## [[creating_interactive_svg_animations | Animating]] with Kute.js
The Kute.js library simplifies the process of creating morph animations for [[SVG and CSS integration | SVG]] paths <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

### Installation
Add the Kute.js CDN link as a script tag in the `<head>` of your HTML document <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>:

```html
<script src="https://cdn.jsdelivr.net/npm/kute.js@2.1.2/dist/kute.min.js"></script>
```

### [[techniques_for_svg_styling_with_css_and_javascript | JavaScript]] Implementation
Place a script tag at the bottom of the section containing the [[SVG and CSS integration | SVG]] to trigger the animation <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.

```javascript
<script>
  // Select the SVG paths by their IDs
  const blobOne = document.getElementById('blob-one');
  const blobTwo = document.getElementById('blob-two');

  // Create a Kute.js tween to animate from blob-one to blob-two
  const morphTween = Kute.fromTo(
    blobOne, // Starting element (blob-one)
    { path: blobOne }, // Starting state (current path of blob-one)
    { path: blobTwo }, // Target state (path of blob-two)
    {
      duration: 3000, // Animation duration in milliseconds (3 seconds)
      yoyo: true,     // Makes the animation go back and forth
      repeat: Infinity // Loops the animation indefinitely
    }
  );

  // Start the animation
  morphTween.start();
</script>
```
The `Kute.fromTo()` method takes the starting [[SVG and CSS integration | SVG]] element, its initial state, the target [[SVG and CSS integration | SVG]] element's path, and an options object <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.
*   `duration`: Sets the length of the animation in milliseconds <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.
*   `yoyo`: Makes the animation play forward and then reverse <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.
*   `repeat`: Can be set to `Infinity` for continuous looping.

This setup creates a smoothly [[creating_interactive_svg_animations | animated]] [[SVG and CSS integration | SVG]] that morphs between two different blob shapes, enhancing the visual appeal of the webpage <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.