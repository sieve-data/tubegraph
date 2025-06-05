---
title: History and adoption of TypeScript
videoId: 5ChkQKUzDCs
---

From: [[fireship]] <br/> 

[[introduction_to_typescript | TypeScript]], a language developed by Microsoft, has seen a fluctuating journey regarding its adoption and perception within the developer community.

### Early Release and Initial Reception
[[introduction_to_typescript | TypeScript]] was first released in 2012 <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Initially, it garnered little attention <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

### Shifting Perceptions and Widespread Adoption
A notable shift in sentiment was observed through the public statements of developer Kent C Dodds:
*   **2017**: He stated, "I don't use [[introduction_to_typescript | typescript]] so I don't ever plan on supporting it" <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.
*   **2019**: His view evolved to, "you are impassioned love of [[introduction_to_typescript | typescript]] is sort of freaking me out" <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.
*   **2023**: He capitulated, declaring, "[[introduction_to_typescript | typescript]] is one and it's only a matter of time you're using it whether you like it or not" <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This change reflects the adaptability expected of good developers <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

A few years after its release, [[introduction_to_typescript | TypeScript]] gained significant traction when it was adopted by the Angular 2 framework <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. By the early 2020s, [[introduction_to_typescript | TypeScript]] had become ubiquitous, converting many previous critics into proponents <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

### Recent Trends in Adoption
Despite its widespread adoption, a [[recent_trend_of_ditching_typescript_for_javascript | recent trend has emerged]] where several large open-source projects have opted to [[recent_trend_of_ditching_typescript_for_javascript | move away from TypeScript]] in favor of vanilla [[history_of_javascript | JavaScript]] <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

Projects that have decided to [[recent_trend_of_ditching_typescript_for_javascript | ditch TypeScript]] include:
*   **Svelte**: Svelte 5 will not use [[introduction_to_typescript | TypeScript]], and SvelteKit is already written in plain [[history_of_javascript | JavaScript]] <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. This move is primarily for practical reasons, such as eliminating the compile step, which boosts productivity for a large framework <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. Projects like Svelte still achieve most of the benefits of [[introduction_to_typescript | TypeScript]] by using JSDoc, a standard comment format for declaring types and documentation <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. This approach allows for type inference and provides Intellisense in editors, helping to catch bugs early <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   **Drizzle** <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>
*   **Turbo**: Turbo version 8 is moving away from [[introduction_to_typescript | TypeScript]] <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. One reason cited is that [[introduction_to_typescript | TypeScript]] can "pollute the code with quote type gymnastics," especially when developing libraries <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

Despite this [[recent_trend_of_ditching_typescript_for_javascript | shift in libraries]], using [[introduction_to_typescript | TypeScript]] in applications built with frameworks like SvelteKit or Next.js remains seamless. Achieving similar results with JSDoc in such applications would be challenging <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### The Future of Types in JavaScript
There is a Stage 1 ECMAScript proposal to natively add optional type annotations to [[history_of_javascript | JavaScript]], which could potentially make [[introduction_to_typescript | TypeScript]] nearly obsolete <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.