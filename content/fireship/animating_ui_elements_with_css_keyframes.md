---
title: Animating UI elements with CSS keyframes
videoId: rXuHGLzSmSE
---

From: [[fireship]] <br/> 

CSS keyframe animations provide a powerful way to create dynamic visual effects on web pages. This technique allows developers to define the stages of an animation and then apply it to any element in the user interface <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.

## Defining a Keyframe Animation

Keyframe animations are defined using the `@keyframes` CSS rule. This rule allows you to specify the styles an element will have at various points during the animation's sequence <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.

### Example: `color-rotate` Animation

A common application of keyframe animations is to create color transitions or rotations. For instance, a `color-rotate` animation can be set up to cycle through every color on the color wheel <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.

```css
@keyframes color-rotate {
  from {
    filter: hue-rotate(0deg); /* Normal color at the start */ <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>
  }
  to {
    filter: hue-rotate(360deg); /* Cycle through the color wheel */ <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>
  }
}
```

In this example, the animation starts with a `hue-rotate` filter set to `0deg` and transitions to `360deg`, effectively rotating the colors through the spectrum <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>.

## Applying a Keyframe Animation

Once a keyframe animation is defined, it can be applied to an element using the `animation` CSS property <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. This property is a shorthand for several animation-related properties.

### Animation Properties

For an element like a logo, the animation can be triggered on a hover state, applying the following properties:

*   **`animation-name`**: The name of the `@keyframes` rule to apply (e.g., `color-rotate`) <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>.
*   **`animation-duration`**: How long the animation takes to complete one cycle (e.g., `1s`) <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.
*   **`animation-iteration-count`**: How many times the animation should play. Setting it to `infinite` makes it loop continuously <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>.
*   **`animation-direction`**: Whether the animation should play forward, backward, or alternate between the two. Setting it to `alternate` will rotate the color wheel from clockwise to counterclockwise <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.

```css
/* Example: Applying the animation to a logo on hover */
.logo:hover {
  animation: color-rotate 1s infinite alternate; <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>
}
```

This application results in a rainbow effect on the logo when hovered <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.

### Distinctions: Keyframes vs. Transitions

While CSS keyframes define complex, multi-stage animations, the `transition` property is used for simpler state changes, such as smoothly changing a background color or text color <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. Transitions typically animate properties directly between two states, whereas keyframes allow for defining multiple intermediate states.