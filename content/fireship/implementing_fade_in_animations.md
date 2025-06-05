---
title: Implementing fade in animations
videoId: 7JA90VI9fAI
---

From: [[fireship]] <br/> 

Implementing animations between router transitions is an effective way to make your application feel more polished <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This guide covers a simple fade-in animation applied to every route change in an Angular application <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Initial Setup

Before defining the animation, you need to configure your Angular application:

1.  **Generate Components**: Have a handful of components generated for routing purposes <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. These components do not require any special setup <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
2.  **Import Animations Module**: In your `app.module.ts` file, import `BrowserAnimationsModule` from `@angular/platform-browser/animations` and add it to the `imports` array <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

    ```typescript
    // app.module.ts
    import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

    @NgModule({
      imports: [
        // ... other imports
        BrowserAnimationsModule
      ],
      // ...
    })
    export class AppModule { }
    ```
3.  **Configure App Component HTML**: In `app.component.html`, define a `main` element with an animation trigger and a `router-outlet` inside it <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

    ```html
    <!-- app.component.html -->
    <nav>...</nav> <!-- Stays fixed and is not animated -->
    <main [@routeAnimations]="prepareRoute(outlet)">
      <router-outlet #outlet="outlet"></router-outlet>
    </main>
    ```

    *   `@routeAnimations="prepareRoute(outlet)"`: This defines an animation named `routeAnimations` and points it to a method `prepareRoute` in your component's TypeScript file <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This method's job is to determine which animation to apply to a given route <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
    *   `#outlet="outlet"`: This gives the `router-outlet` a template variable name of `outlet`, allowing its content to be animated when a route changes <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

4.  **Configure App Component TypeScript**: In `app.component.ts`, you'll import the animations (which will be defined shortly) and add them to the `animations` property in the component decorator <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. The `prepareRoute` method is used to pass dynamic data to the animation <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. For a single animation applied to every route, this method is technically optional <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

    ```typescript
    // app.component.ts
    import { Component } from '@angular/core';
    import { outletAnimations } from './route-animations'; // Will define this file next
    import { RouterOutlet } from '@angular/router';

    @Component({
      selector: 'app-root',
      templateUrl: './app.component.html',
      styleUrls: ['./app.component.css'],
      animations: [
        outletAnimations // Use the defined animation
      ]
    })
    export class AppComponent {
      title = 'router-animations-demo';

      prepareRoute(outlet: RouterOutlet) {
        // This method is optional if only using a single animation for every route
        // For a simple fade-in, you could directly pass 'outlet' to the animation in HTML
        return outlet && outlet.activatedRouteData && outlet.activatedRouteData['animation'];
      }
    }
    ```

5.  **Main Element CSS**: For consistent page transitions, set the `main` element in your global `style.css` (or `app.component.css`) to `position: relative` <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

    ```css
    /* style.css or app.component.css */
    main {
      position: relative;
    }
    ```

## Defining the Fade-In Animation

Create a new file, `route-animations.ts`, in your `app` directory to define the animations <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

```typescript
// route-animations.ts
import {
  trigger,
  transition,
  style,
  animate,
  query
} from '@angular/animations';

export const outletAnimations =
  trigger('routeAnimations', [ // Name must match HTML trigger name <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>
    transition('* => *', [ // Wildcard transition applies to every route change <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>
      style({ position: 'relative' }), // Ensure consistent styling <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>
      query(':enter, :leave', [ // Select both entering and leaving elements <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>
        style({
          position: 'absolute', // Position elements absolutely for animation <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>
          top: 0,
          left: 0,
          width: '100%'
        })
      ], { optional: true }), // Optional true means the query won't throw an error if an element isn't found
      query(':enter', [ // Target the entering component (new page) <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>
        style({
          opacity: 0, // Start fully transparent <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>
          transform: 'translateY(100%) scale(0)' // Start off-screen and scaled down <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>
        })
      ]),
      query(':leave', [ // Target the leaving component (old page) <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>
        style({ opacity: 0 }) // Immediately hide the old page <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>
      ]),
      query(':enter', [ // Animate the entering component in <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>
        animate('600ms ease', style({
          opacity: 1, // Fade in to full visibility <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>
          transform: 'translateY(0) scale(1)' // Translate back to original position and full size <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>
        }))
      ])
    ])
  ]);
```

### Explanation of the Fade-In Animation Steps:

1.  **`trigger('routeAnimations', [...])`**: This creates an animation trigger named `routeAnimations` that the HTML can reference <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
2.  **`transition('* => *', [...])`**: This defines a wildcard transition that applies the animation to *every* single route transition <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
3.  **`style({ position: 'relative' })`**: This ensures the main container for the animated content is `position: relative`, which is crucial for the absolute positioning of the child elements <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
4.  **`query(':enter, :leave', [...], { optional: true })`**:
    *   `query()` allows you to select elements within the DOM for animation <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
    *   `:enter` and `:leave` are pseudo-selectors provided by Angular animations. `:enter` refers to the new page entering the view, and `:leave` refers to the old page leaving the view <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
    *   This initial query sets common styles for both the entering and leaving components, positioning them absolutely and covering the full width <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
    *   `{ optional: true }` prevents errors if the element isn't found, which can happen with `:leave` on the first route load.
5.  **`query(':enter', [style(...)])`**: This step prepares the entering component by setting its initial state: `opacity: 0`, `transform: 'translateY(100%) scale(0)'`. This means it starts completely hidden, off-screen, and scaled down <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
6.  **`query(':leave', [style(...)])`**: This step immediately hides the old page (`opacity: 0`) as the transition begins <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
7.  **`query(':enter', [animate(...)])`**: This is the core animation step for the entering component:
    *   `animate('600ms ease', ...)`: The animation will take 600 milliseconds to complete, using an `ease` timing function <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
    *   `style({ opacity: 1, transform: 'translateY(0) scale(1)' })`: This defines the end state of the animation, where the component is fully visible, in its correct position, and at its original scale <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

The entire animation sequence involves hiding both the old and new components initially, then fading in the new component over 600 milliseconds <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. The result is a smooth fade-in effect applied to every route change <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.