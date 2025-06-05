---
title: Implementing transitions and animations in Svelte 3
videoId: 043h4ugAj4c
---

From: [[fireship]] <br/> 

Svelte 3 offers unique and intuitive ways to implement transitions and animations, directly integrating them with your component logic and DOM changes <a class="yt-timestamp" data-t="05:00:01">[05:00:01]</a>. Unlike other frameworks that might require careful CSS animations or JavaScript animation libraries, Svelte provides directives to keep animation logic tied directly to the DOM element being animated <a class="yt-timestamp" data-t="05:24:45">[05:24:45]</a>.

## Svelte's Approach to Animations

Svelte handles animations at **build time** <a class="yt-timestamp" data-t="01:27:54">[01:27:54]</a>, meaning it compiles your code to generate the necessary JavaScript to perform the animations. This results in smaller bundle sizes and optimized code, as only the required framework JavaScript is included <a class="yt-timestamp" data-t="01:40:48">[01:40:48]</a>.

One of Svelte's core features is its reactivity, which is based on variable assignment <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. This reactive system allows Svelte to automatically compute CSS animations based on the logic in your template <a class="yt-timestamp" data-t="05:07:07">[05:07:07]</a>.

## Transition Directives

Svelte provides built-in transition directives that automatically compute CSS animations when elements are added to or removed from the DOM <a class="yt-timestamp" data-t="05:05:30">[05:05:30]</a>. These directives come from the `svelte/transition` module <a class="yt-timestamp" data-t="05:03:01">[05:03:01]</a>.

### `transition:fade`

To make an element fade in and out when it's added or removed from the DOM, you can simply add the `transition:fade` directive <a class="yt-timestamp" data-t="05:12:47">[05:12:47]</a>.

### `transition:fly`

The `transition:fly` directive allows elements to fly in from a specified direction and fly out to another <a class="yt-timestamp" data-t="05:20:25">[05:20:25]</a>. You can customize its behavior by adding properties directly to the directive <a class="yt-timestamp" data-t="05:35:46">[05:35:46]</a>.

*   **Example**: Making elements fly in from the right and out to the left <a class="yt-timestamp" data-t="05:21:40">[05:21:40]</a>.

```html
<p transition:fly="{{ x: 200, duration: 1000 }}">Fly in from right</p>
<p transition:fly="{{ x: -200, duration: 1000 }}">Fly out to left</p>
```

> [!NOTE]
> The `transition:fly` directive simplifies complex [[using_css_transforms_for_sliding_animations|sliding animations]] that would normally require careful thought about CSS or a JavaScript animation library <a class="yt-timestamp" data-t="05:24:45">[05:24:45]</a>.

## SVG Animations

Svelte also includes a directive specifically for SVG graphics, which can draw a path along the shape <a class="yt-timestamp" data-t="05:42:47">[05:42:47]</a>. This provides a direct way for [[implementation_of_keyframe_animations_in_svg|implementing keyframe animations in SVG]] or [[creating_interactive_svg_animations|creating interactive SVG animations]].

## Practical Application

In a real-time to-do list demonstration, the `transition:fly` directive was used to make `todo-item` elements slide in from the right when created <a class="yt-timestamp" data-t="12:23:44">[12:23:44]</a>.

```html
<li transition:fly="{{ x: 200, duration: 500 }}">Todo Item</li>
```

This simple addition allowed for a smooth visual effect without extensive CSS or JavaScript <a class="yt-timestamp" data-t="12:27:42">[12:27:42]</a>.