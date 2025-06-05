---
title: Criticisms and drawbacks of using TypeScript
videoId: 5ChkQKUzDCs
---

From: [[fireship]] <br/> 

While [[history_and_adoption_of_TypeScript | TypeScript]] has seen widespread adoption, a recent trend indicates that some significant projects are moving away from it, highlighting various criticisms and drawbacks <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Initial Resistance to TypeScript

In 2017, JavaScript user Kent C Dodds stated he did not use TypeScript and had no plans to support it <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. By 2019, he expressed that the "impassioned love of TypeScript" was "freaking" him out <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Although he later capitulated in 2023, acknowledging TypeScript's prevalence <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>, this initial sentiment points to a learning curve or ideological resistance that some developers might experience.

## Recent Trend of Ditching TypeScript

Despite its widespread presence by the early 2020s <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>, large open-source projects such as Svelte, Drizzle, and Turbo have recently decided to remove [[introduction_to_TypeScript | TypeScript]] from their codebases in favor of vanilla JavaScript <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This move primarily affects the development of these libraries, but end-users can still utilize TypeScript when using frameworks like Svelte <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Code Pollution and "Type Gymnastics"

One significant reason for moving away from TypeScript, as articulated by DHH, creator of Ruby on Rails and involved with Turbo version 8, is that it "pollutes the code with quote type gymnastics" <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>, <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. This means developers often write complex type definitions just to satisfy the compiler or remove IDE warnings <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. For example, in strict mode, using `any` to avoid explicit types can lead to less "beautiful" code <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>, <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. This shift has also caused frustration among developers whose [[type_annotations_and_strong_typing_in_typescript | TypeScript]] contributions are now considered "Dead on Arrival" <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>, <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

### Compile Step Overhead

Another "purely practical" reason cited by Rich Harris for Svelte's move away from TypeScript is the elimination of the compile step <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>, <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. This provides a "huge boost in productivity" for large frameworks <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. Svelte 5 and SvelteKit, for instance, are written in plain vanilla JavaScript <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>, <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. They achieve many of the benefits of TypeScript, like IntelliSense and early bug detection, by using [[alternatives_to_typescript_in_projects | JSDoc]] for type declarations and documentation within standard JavaScript comments <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>, <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

While ditching TypeScript may benefit library development, replicating the same level of seamless integration and type safety with JSDoc in complex applications (like those built with SvelteKit or Next.js) is considered "a total nightmare" <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>, <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. The ongoing "holy war" between TypeScript and JavaScript might eventually end with the [[future_of_JavaScript_with_potential_native_type_annotations | ECMAScript proposal for optional native type annotations in JavaScript]] <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>, which could render TypeScript nearly obsolete <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>, <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.