---
title: Structural patterns in software design
videoId: tv-_1er1mWI
---

From: [[fireship]] <br/> 

[[overview_of_software_design_patterns | Software design patterns]] offer solutions to recurring [[problemsolving_skills_in_software_development | problems]] in programming <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>. The influential book "Design Patterns" by the "Gang of Four" categorizes 23 different approaches into three main types: [[understanding_creational_patterns | creational patterns]] (how objects are created), structural patterns (how objects relate to each other), and [[behavioral_patterns_in_programming | behavioral patterns]] (how objects communicate) <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>. Structural patterns focus on composing objects and classes into larger structures, making them more flexible and efficient <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>.

While it can be tempting to implement [[overview_of_software_design_patterns | design patterns]] everywhere, improper use can add complexity and boilerplate <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>. Despite some [[criticism_and_practical_use_of_design_patterns | criticisms]], knowing recognized [[overview_of_software_design_patterns | design patterns]] can significantly enhance a programmer's skill <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>.

## Facade Pattern

The Facade pattern provides a simplified API (Application Programming Interface) to hide complex, low-level details of a system <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>.

### Analogy
Imagine a building where a facade is its visible "face" <a class="yt-timestamp" data-t="04:55:00">[04:55:00]</a>. Inside, there's intricate plumbing and electrical systems, but the end-user doesn't need to interact with every wire or pipe <a class="yt-timestamp" data-t="04:58:00">[04:58:00]</a>.

### Practical Example
Consider classes for a plumbing system and an electrical system, each with complex internal operations like managing pressure or voltage <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>. A Facade class can be created to encapsulate these systems as dependencies, simplifying their operation <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>. For instance, it might combine electrical and plumbing details into a single method, allowing a user to simply "turn them on or off" <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>.

In [[design_techniques_in_app_development | app development]], many JavaScript packages function as facades, like jQuery, which simplified interacting with complex, low-level JavaScript features <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a>.

## Proxy Pattern

The Proxy pattern involves replacing a target object with a substitute <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>.

### Analogy
Think of a substitute teacher replacing the main teacher in a school <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.

### Use Cases
*   **Reactivity Systems**: In frameworks like Vue.js, data changes need to trigger UI updates <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>. Vue.js handles this by replacing the original data object with a Proxy <a class="yt-timestamp" data-t="06:10:00">[06:10:00]</a>. A Proxy takes the original object and a `Handler` as arguments <a class="yt-timestamp" data-t="06:13:00">[06:13:00]</a>. Inside the `Handler`, methods like `get` and `set` can be overridden to run custom code when a property is accessed or changed <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>. For example, within the `set` method, the framework can be told to re-render the UI, while `Reflect` updates the data on the original object <a class="yt-timestamp" data-t="06:25:00">[06:25:00]</a>. Users interact with the proxy as if it were the original object, triggering side effects behind the scenes <a class="yt-timestamp" data-t="06:32:00">[06:32:00]</a>.
*   **Memory Efficiency**: Proxies are also useful when dealing with very large objects that would be expensive to duplicate in memory <a class="yt-timestamp" data-t="06:38:00">[06:38:00]</a>.