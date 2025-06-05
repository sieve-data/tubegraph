---
title: Slide animations based on router data
videoId: 7JA90VI9fAI
---

From: [[fireship]] <br/> 
An easy way to make an application more polished is by implementing animations between router transitions <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This can be achieved with [[router_animations_in_angular | router animations in Angular]] <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>, allowing for different styles ranging from simple fade-ins to complex [[key_framed_animations_in_angular | key frame]] sequences <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Setup

To enable router animations in an Angular application:
1.  **Import `BrowserAnimationsModule`**: In the `app.module.ts` file, import `BrowserAnimationsModule` and add it to the `imports` array <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
2.  **Configure `app.component.html`**:
    *   Create a `main` element.
    *   Define an animation trigger on the `main` element, e.g., `@routeAnimations` <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
    *   Point this trigger to a method, e.g., `prepareRoute`, which will determine which animation to apply <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
    *   Place the `<router-outlet>` inside this `main` element and give it a template variable name, e.g., `outlet` <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This allows animating content within the `router-outlet` when a route changes <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
    *   Ensure the `main` element's CSS `position` is set to `relative` for consistent page transitions <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
3.  **Configure `app.component.ts`**:
    *   Import animation definitions (e.g., from `route-animations.ts`).
    *   Add these imported animations to the `animations` property in the `@Component` decorator <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
    *   Define the `prepareRoute` method. This method takes the `outlet` (router outlet) as an argument and returns data from the `router.snapshot.data` property, which can be used to select specific animations <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. If only a single animation is used for all routes, this method is optional <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
4.  **Configure Router Data**: In the `app-routing.module.ts` file, a `data` attribute can be passed into the route configuration. For example, `data: { animation: 'isRight' }` or `data: { animation: 'isLeft' }` can be used to control the direction of a slide animation <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. The `prepareRoute` method will look for this property to apply the corresponding animation <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

## Animation Concepts

Animations are defined in a separate file (e.g., `route-animations.ts`) by importing utilities from `@angular/animations` <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>:
*   **`trigger`**: Defines the animation that gets applied <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. The name of the trigger must match what is used in the HTML (e.g., `routeAnimations`) <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
*   **`transition`**: Determines how styles are applied from one animation state to the next <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
    *   `* <=> *`: A wildcard that applies to every single route transition <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
    *   `'isLeft <=> isRight'` or specific state transitions (e.g., `'isLeft => isRight'`) define animations between specific route data states <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   **`query`**: Selects elements from the DOM that are being animated <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
    *   `:enter`: Pseudo-selector for the new (entering) page <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
    *   `:leave`: Pseudo-selector for the old (leaving) page <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   `{ optional: true }`: Makes a query optional in case the element isn't present <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
*   **`style`**: Defines CSS styles for the elements.
    *   Initial styles for elements to be animated are typically `position: absolute` and `top: 0` <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
*   **`animate`**: Sets up the actual transition with timing and an `ease` function <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **`group`**: Allows multiple animations to run concurrently <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. Otherwise, they would run one after the other <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
*   **`keyframes`**: Used when an animation has multiple intermediate steps rather than just a single start and end point <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. An array of styles is passed in, and their timing within the total animation is determined by an `offset` value (0 for start, 1 for end) <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

## Examples of Router Animations

### 1. Simple Fade-in

This animation applies to every route change <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Initial setup**: Both `:enter` and `:leave` elements are positioned `absolute`, with `opacity: 0`, translated off-screen, and scaled to zero <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. This creates a hidden starting point <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Entering component**: The new page (`:enter`) animates in over 600ms, setting `opacity: 1`, `scale: 1`, and `translateY: 0` <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

### 2. Slide from Left to Right (Based on Router Data)

This animation takes into account the position of the component based on router data (e.g., `isRight` or `isLeft`) <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. A reusable function, `slideTwo`, handles the common logic <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

*   **Transitions**:
    *   `'isLeft => isRight'` (slides left) <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
    *   `'isRight => isLeft'` (slides right) <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
    *   `'isRight => *'` and `'isLeft => *'` handle transitions to/from components without specific animation data <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   **Styles**:
    *   Both entering and leaving components are positioned `absolute` at the top <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
    *   The entering component is offset 100% (`transform: 'translateX(100%)'` or `translateX(-100%)`) in the specified direction <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   **Animation**:
    *   Animations for leaving and entering components occur concurrently within a `group` <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
    *   The leaving component animates 100% off the screen (e.g., `translateX(-100%)`) <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
    *   The entering component animates to 0% translation (`translateX(0%)`) <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
    *   Both animations share the same timing function <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

### 3. [[using_css_transforms_for_sliding_animations | CSS Transforms]] (Rotation, Scaling)

This is a variation of the slide animation that incorporates [[using_css_transforms_for_sliding_animations | CSS transforms]] like `rotate` and `scale` <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. A function is designed to take configurable `x`, `y`, and `rotation` values as named arguments <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   **Transformations**: `transform` styles are created by interpolating values for `translateX`, `translateY`, and `rotate` <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. These can be extended to include `skew` or `scale` <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **Animation**: The animation structure remains similar to the slide, but applies the calculated transform values <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

### 4. [[key_framed_animations_in_angular | Key Framed Animation]]

Unlike simple transitions with a single start/end point, [[key_framed_animations_in_angular | key framed animations]] allow for multiple intermediate steps <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. This example creates a 3D effect where pages appear to collide <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

*   **Initial Setup**: Both entering and leaving components are positioned `absolute` <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>, and animations run concurrently within a `group` <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
*   **Entering Component**:
    *   Uses `keyframes` with an array of styles <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
    *   `offset: 0`: Scales to `0` and translates off-page <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.
    *   `offset: 0.3`: (30% through the animation, e.g., 600ms for a 2000ms animation) applies an intermediate style <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
    *   `offset: 1`: Component is fully visible (`scale: 1`, `translate: 0`) <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Leaving Component**:
    *   Key frames are roughly matched to the entering component to create a "bumping off" effect <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
    *   Scales up to `600%` of its original size while rotating and fading out to `opacity: 0` <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.