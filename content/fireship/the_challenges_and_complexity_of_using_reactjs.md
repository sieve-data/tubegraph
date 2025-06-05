---
title: The challenges and complexity of using Reactjs
videoId: HyWYpM_S-2c
---

From: [[fireship]] <br/> 

React.js, a functional UI library developed at Facebook, is widely used by developers <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Despite its [[popularity_and_impact_of_reactjs_in_web_development | popularity]], it presents several challenges and complexities in its usage.

## Inconsistent Problem Solving Approaches
React offers numerous methods to solve the same problems <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. These include:
*   [[reactjs_functional_and_classbased_components | Functional and class-based components]] <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>
*   [[react_hooks_explained | Hooks]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>
*   Forward ref <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>
*   Higher-order components <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>
*   Mix-ins <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>
*   Render props <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>
*   Suspense <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>

While it promotes writing pure functional code, doing anything useful often necessitates writing imperative functions with state and effects <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. This approach can make simple tasks, like managing reactive state, more complicated than necessary <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Specific Challenges with Hooks
The `[[react_hooks_explained | useEffect]]` hook, for instance, is noted for its potential to introduce issues such as infinite loops, performance problems, and elusive bugs <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Evolving and Patching
React is continuously evolving, with new features often serving as "monkey patches" to address complexities or "weirdness" from previous releases <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. Strict Mode, for example, is utilized to conceal "baggage" from earlier versions of the library <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## Steep Learning Curve and Ecosystem Dependencies
React has an extremely high [[reactjs_learning_curve_and_tooling | learning curve]] <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. As it is a library rather than a framework, [[building_components_with_react | building]] a functional application requires finding and installing numerous external packages <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. Many of these packages, part of the broader [[react_ecosystem_and_libraries | React ecosystem]], may be unmaintained <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. This often leads developers into "tutorial hell" when starting a new React project <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Templating and Styling
React uses JSX for templating, a non-standard way to write HTML that can lead to "non-portable callback hell" in UI representation <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. Styling with CSS in React can also be particularly challenging, though hundreds of CSS-in-JS libraries exist to address this <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## Performance Requirements
Achieving optimal performance in React often requires implementing "weird tricks flawlessly" <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.