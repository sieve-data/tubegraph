---
title: Alternatives to TypeScript in projects
videoId: 5ChkQKUzDCs
---

From: [[fireship]] <br/> 

While [[history_and_adoption_of_typescript | TypeScript]] experienced significant growth and adoption, a [[recent_trend_of_ditching_typescript_for_javascript | recent trend]] has emerged where prominent open-source projects are moving away from [[introduction_to_typescript | TypeScript]] in favor of [[state_of_javascript_in_modern_development | vanilla JavaScript]] or alternative typing solutions <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

The shift reflects a reevaluation of [[introduction_to_typescript | TypeScript]]'s benefits versus its [[criticisms_and_drawbacks_of_using_typescript | drawbacks]] in specific contexts.

## The Shifting Landscape

For years, [[introduction_to_typescript | TypeScript]] seemed poised to dominate the [[state_of_javascript_in_modern_development | JavaScript]] ecosystem. As late as 2023, even previous skeptics like Kent C. Dodds acknowledged its widespread adoption <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

> "I don't use [[introduction_to_typescript | typescript]] so I don't ever plan on supporting it." <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>
> "You are impassioned love of [[introduction_to_typescript | typescript]] is sort of freaking me out." <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>
> "[[introduction_to_typescript | Typescript]] is one and it's only a matter of time you're using it whether you like it or not." <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>

Despite this perceived victory, several major projects, including Svelte, Drizzle, and Turbo, have recently opted to [[recent_trend_of_ditching_typescript_for_javascript | ditch TypeScript]] from their core codebases <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. It's important to note that this move primarily affects the development of these libraries, not necessarily their end-user experience, as users can often still use [[introduction_to_typescript | TypeScript]] with them <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Reasons for Ditching TypeScript

Projects are moving away from [[introduction_to_typescript | TypeScript]] for several reasons, primarily stemming from its impact on code complexity and developer productivity.

### Code Pollution and "Type Gymnastics"
One significant [[criticisms_and_drawbacks_of_using_typescript | criticism]], highlighted by DHH, creator of Ruby on Rails and involved with Turbo, is that [[introduction_to_typescript | TypeScript]] can "pollute the code with quote [[type_annotations_and_strong_typing_in_typescript | type gymnastics]]" <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>, <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. This refers to the often complex and verbose [[type_annotations_and_strong_typing_in_typescript | type annotations]] required, especially when developing libraries, which can detract from code readability and maintainability <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. The need to satisfy the compiler, particularly in strict modes, can lead to less beautiful code or the overuse of `any` types <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

### Compile Step Overhead
Another practical reason, particularly for large frameworks like Svelte, is the overhead of the [[using_typescript_compiler_and_setting_ts_config | compile step]] <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. Eliminating this step provides a "huge boost in productivity" for the framework's development <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

## JSDoc as a Viable Alternative

Despite moving away from [[introduction_to_typescript | TypeScript]], projects like Svelte are still able to achieve many of its benefits by leveraging **JSDoc** <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

JSDoc is a standard comment format in [[state_of_javascript_in_modern_development | JavaScript]] where developers can declare [[type_annotations_and_strong_typing_in_typescript | types]] and documentation using regular [[state_of_javascript_in_modern_development | JavaScript]] comments <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>, <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. This approach offers several advantages:
*   **Type Generation**: JSDoc comments can be used to generate `.d.ts` files, providing [[type_annotations_and_strong_typing_in_typescript | type definitions]] for consumers <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   **IntelliSense**: Crucially, JSDoc enables "IntelliSense" in code editors, allowing developers to understand function parameters, return [[type_annotations_and_strong_typing_in_typescript | types]], and catch bugs early, much like [[introduction_to_typescript | TypeScript]] <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>, <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. This addresses a primary reason many developers use [[introduction_to_typescript | TypeScript]] in the first place <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   **No Compile Step**: By relying on comments and editor tooling, JSDoc avoids the need for a separate [[using_typescript_compiler_and_setting_ts_config | compilation step]], improving productivity <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

## The Future of Types in JavaScript

While projects can successfully use JSDoc for internal development, [[introduction_to_typescript | TypeScript]] continues to offer seamless integration for building applications with tools like SvelteKit or Next.js <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>, <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. Attempting to achieve the same level of [[type_annotations_and_strong_typing_in_typescript | type safety]] and tooling with JSDoc in application development can be a challenge <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

A long-term solution may come from within [[state_of_javascript_in_modern_development | JavaScript]] itself. There is currently a Stage 1 ECMAScript proposal to natively add optional [[type_annotations_and_strong_typing_in_typescript | type annotations]] to [[state_of_javascript_in_modern_development | JavaScript]] <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>, <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. If this proposal advances, it could potentially make [[introduction_to_typescript | TypeScript]] nearly obsolete by providing built-in [[type_annotations_and_strong_typing_in_typescript | type checking]] capabilities directly within the language <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.