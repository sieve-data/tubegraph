---
title: React introduction and history
videoId: Tn6-PIqc4UM
---

From: [[fireship]] <br/> 

[[reactjs_overview_and_history | React]] is a [[javascript_basics_and_history | JavaScript]] library designed for building user interfaces <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Developed at Facebook, it was released in 2013 and has since become one of the most influential UI libraries <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Core Concepts

### Components
[[reactjs_overview_and_history | React]] is used to build components, which are logical, reusable parts of the user interface <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. The fundamental principle of building a component in [[reactjs_overview_and_history | React]] is its simplicity; it is essentially just a [[javascript_basics_and_history | JavaScript]] function <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

### JSX
The return value from a [[reactjs_overview_and_history | React]] component function is the UI, which is written in a special syntax called JSX <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. JSX allows developers to easily combine [[javascript_basics_and_history | JavaScript]] logic with HTML markup <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

### Props
Data can be passed into a component using a `props` argument <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. These `props` can then be referenced within the function body or in the UI using braces <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. When the value of a `prop` changes, [[reactjs_overview_and_history | React]] automatically updates the UI <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

### State and Hooks
For a component to manage its own internal state, developers can use the `state` [[react_hooks_explained | hook]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. A [[react_hooks_explained | hook]] is a function that returns a value (the state) and a function to modify that value <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. For example, `count` would be the reactive state, and `setCount` would be the function to change it <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. When `setCount` is used, the `count` in the template will always display the most recent value <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. [[reactjs_overview_and_history | React]] provides a variety of other built-in [[react_hooks_explained | hooks]] to handle common use cases <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## The [[react_ecosystem_and_libraries | React Ecosystem]]

One of the primary reasons to use [[reactjs_overview_and_history | React]] is its massive [[react_ecosystem_and_libraries | ecosystem]] of supporting libraries and tools <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. [[reactjs_overview_and_history | React]] itself focuses solely on UI rendering and does not inherently handle concerns like routing, state management, or animation <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. Instead, it allows these functionalities to evolve naturally within the open-source community <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

There is a vast array of libraries available to assist with various development needs:
*   **Static Sites**: Gatsby <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>
*   **Server-Side Rendering**: Next.js <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>
*   **Animation**: React Spring <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>
*   **Forms**: Formik <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>
*   **State Management**: Redux, MobX, Flux, Recoil, XState, and more <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>

## Beyond Web Development

Once familiar with [[reactjs_overview_and_history | React]], developers can easily transition to [[applications_of_react_including_react_native | React Native]] to build mobile applications <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Knowing [[reactjs_overview_and_history | React]] is considered one of the most in-demand skills for front-end developers today <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.