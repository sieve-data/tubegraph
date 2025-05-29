---
title: Server Components without a server
videoId: v1cg7b-Oaxs
---

From: [[swarajmakesstuff]] <br/> 

A common [[Misconception about React Server Components | misconception about React Server Components]] is that they always require a server to run <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. However, this is not entirely accurate <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Client Components

[[Clientside vs Serverside Components in React | Client components]] are designed for instantaneous updates and user interactivity <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. They run directly on the user's computer (e.g., a laptop) <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. This local execution eliminates the delay typically associated with client-server communication in pre-JavaScript eras <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. For interactive elements like range sliders or clicks requiring immediate feedback, [[Enhancing Web App Interactivity | client-side components]] are essential to ensure zero delay <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

## How Server Components Operate

Unlike client components, [[Clientside vs Serverside Components in React | server components]] handle tasks that cannot run on the client side, often because the client's machine lacks the necessary data or access to certain files <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.

Consider an example of a "post preview" component that displays the word count of a post <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>. The user's laptop wouldn't possess the data of other posts (e.g., MDX files) to perform such a count <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. This component works by calling the MDX file, extracting its data, making an array, and counting its length <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>.

### Execution Timing

The crucial distinction lies in *when* this code executes <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>. Instead of running on a server every time a page is reloaded <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>, [[Clientside vs Serverside Components in React | server component]] code runs during the **build time** of the application <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>. For instance, if a blog post was deployed on January 5, 2024, the server component would have executed on that date, generating the static output <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>. Even if the page is reloaded days later, the date (and thus the word count result) remains the same because the component has already been processed <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.

During [[Static file generation during build time in React | build time]], the static output from server components is generated and stored in the build file <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>. These files become static files, similar to images or basic HTML <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>. The component code itself (e.g., `post list` or `post preview`) is no longer present; it has been transformed into basic HTML divs and sections <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>.

## Why "Server Components"?

The term "server components" is used because these components can leverage [[APIs that require serverside execution in React | server-side only APIs]] <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>. Many APIs will throw errors or not function correctly if attempted to run on the client side <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>. By allowing the components to execute during a "server-like" environment (i.e., build time), these [[APIs that require serverside execution in React | server-side APIs]] can be safely called and processed, with their results then baked into the static output that's delivered to the client <a class="yt-timestamp" data-t="05:20:00">[05:20:00]</a>.