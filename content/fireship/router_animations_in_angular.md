---
title: Router animations in Angular
videoId: 7JA90VI9fAI
---

From: [[fireship]] <br/> 

Implementing animations between router transitions is an effective way to enhance the polish and user experience of an Angular application <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This guide provides a comprehensive overview of router animations in Angular, demonstrating various styles from simple fades to complex key-framed sequences <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Animation Styles Demonstrated

This guide will build and demonstrate four distinct styles of router animations:
*   **Simple Fade-in:** Applied universally to every route transition <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   **[[slide_animations_based_on_router_data | Slide Animations Based on Router Data]]:** Pages slide from left or right, with the direction determined by data passed through the Angular Router <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
*   **Transformations:** Incorporates CSS transforms, allowing pages to rotate in from corners <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   **[[key_framed_animations_in_angular | Key Framed Animations in Angular]]:** Utilizes keyframes to create a sequence of style changes, such as a new page bumping the old one off-screen with spins and scaling <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## Initial Setup

To begin, ensure your Angular application (e.g., an Angular 7 app <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>) has components set up for routing <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

### Import `BrowserAnimationsModule`
In your `app.module.ts`, import `BrowserAnimationsModule` and add it to the `imports` array <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

### Configure `app.component.html`
In the `app.component.html` file, create a `main` element and define an animation called `routeAnimations` on it <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This animation will point to a method `prepareRoute`, which will determine which animation to apply to a given route <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

```html
<main [@routeAnimations]="prepareRoute(outlet)">
  <nav>...</nav>
  <router-outlet #outlet="outlet"></router-outlet>
</main>
```
The `router-outlet` is given a template variable name `outlet` to allow animating its content when a route changes <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. The navigation bar can remain fixed, outside the animated area <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

### Configure `app.component.ts`
In `app.component.ts`, you'll import the defined animations and add them to the `animations` property in the component decorator <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

The `prepareRoute` method is essential for applying different animations based on different routes <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This method, derived from Angular documentation, is optional if a single animation is used for all routes, in which case the `outlet` can be passed directly to the animation in the HTML <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

```typescript
// Example prepareRoute method
import { outletAnimations } from './route-animations'; // assuming animations are in route-animations.ts

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  animations: [
    // Uncomment the animation you want to use
    // fadeAnimation,
    // slideAnimations,
    // transformAnimations,
    // keyframeAnimation,
    outletAnimations // A wrapper or the specific animation
  ]
})
export class AppComponent {
  prepareRoute(outlet: RouterOutlet) {
    return outlet && outlet.activatedRouteData && outlet.activatedRouteData['animation'];
  }
}
```

### Configure Router
For animations that depend on route data, configure your router with a `data` attribute. For example, to determine slide direction, you can add `data: { animation: 'isRight' }` or `data: { animation: 'isLeft' }` to your route definitions <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. The `prepareRoute` method will then use this property to apply the corresponding animation <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

### Create `route-animations.ts`
Create a file, e.g., `route-animations.ts`, in your app directory. This file will contain all animation definitions, requiring imports from `@angular/animations` <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

## Core Animation Concepts

Angular animations utilize several key concepts:
*   **`trigger`**: Defines the animation with a name (e.g., `routeAnimations`) that matches the one used in the HTML <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
*   **`transition`**: Determines how styles are applied from one animation state to the next. The `* => *` wildcard syntax applies to every route transition <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   **`query`**: Allows selection of elements within the DOM for animation. Angular applies pseudo-selectors `:enter` (new page) and `:leave` (old page) to the animating elements <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   **`style`**: Defines the CSS properties to be applied.
*   **`animate`**: Sets up the actual transition, including timing (e.g., `600ms`) and easing functions <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **`group`**: Allows multiple animations to run concurrently <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   **`keyframes`**: Enables defining multiple intermediate steps in an animation rather than just a single start and end point <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. Each keyframe has an `offset` value (0-1) to determine when it applies during the total animation time <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

## 1. Simple Fade-in Animation

This is the most basic animation, applied to every route change <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

1.  **Initial Setup:** Position both entering and leaving elements as `absolute`. Set their initial `opacity` to `0`, `translateY` to `100%`, and `scale` to `0` to hide them and prepare them for animation <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
2.  **Enter Animation:** Query the `:enter` selector (the new page) <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. Animate it over 600ms with an `ease` function <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. The final style should set `opacity` to `1`, `scale` to `1`, and `translateY` to `0` <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
3.  **Styling Note:** Ensure the main element (the animation container) has `position: relative` in your `styles.css` for consistent page transitions <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

This process hides both components initially, then fades in the new component <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

## 2. [[slide_animations_based_on_router_data | Slide Animations Based on Router Data]]

This animation takes into account the position of components (left or right) to determine the slide direction <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. It uses a reusable `slideTwo` function.

1.  **Router Data:** Define `data: { animation: 'isLeft' }` or `data: { animation: 'isRight' }` in your router configuration for specific components <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
2.  **Transitions:**
    *   Transition to `isLeft` animations will slide to the left <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
    *   Transition to `isRight` animations will slide to the right <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
    *   Transitions from `isRight` to any component also slide left <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
    *   And vice versa for `isLeft` <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
3.  **`slideTwo` Function:**
    *   Set initial default styles for both components to `position: absolute` and `top: 0` <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
    *   Add an additional style to the entering component to offset it `100%` in the specified `direction` (e.g., `translateX(-100%)` for left, `translateX(100%)` for right) <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
    *   Group animations to run concurrently <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
    *   Animate the leaving component `100%` off-screen in the opposite direction <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
    *   Animate the entering component to `0%` (its intended final position) <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. Both animations should have the same timing function <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

## 3. Transformations with CSS Transforms

This is a variation of the slide animation that leverages CSS transforms for effects like rotation and scaling <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

1.  **Function Arguments:** The animation function takes named arguments like `x`, `y`, and `rotation` to allow for configurable animations <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. Destructuring with default values can be used for convenience <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
2.  **Transformations:** Define transformations by interpolating values into strings, e.g., `translateX({{x}}%)`, `translateY({{y}}%)`, `rotate({{rotation}}deg)` <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. This can be extended to include `skew` and `scale` <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
3.  **Animation Logic:** The animation logic is similar to the slide example, but applies the transform values instead of just `direction` <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

## 4. [[key_framed_animations_in_angular | Key Framed Animations in Angular]]

Unlike single-point transitions, key-framed animations allow for multiple intermediate steps <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

1.  **Trigger and Group:** Define a new animation using a wildcard `* => *` transition to apply to every route <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. Set initial position to `absolute` and use a `group` to run concurrent page animations <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
2.  **`keyframes` Function:**
    *   **Entering Component:** Use the `keyframes` function to pass an array of styles <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
        *   `offset: 0`: As the animation starts, scale the component to `0` and translate it off-page <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.
        *   `offset: 0.3` (30% of animation time): Apply an intermediate style <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
        *   `offset: 1` (end of animation): Component is fully visible (`scale: 1`, `translate: 0`) <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
    *   **Leaving Component:** Roughly match keyframes to the entering component to create a "bumping" effect <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
        *   Scale it up (e.g., to `600%`), rotate it, and fade it out to `opacity: 0` concurrently <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

This creates a 3D effect where pages appear to collide <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.

These examples provide a foundation for building custom and visually appealing router transitions in Angular <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.