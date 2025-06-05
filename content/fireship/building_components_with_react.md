---
title: Building components with React
videoId: Tn6-PIqc4UM
---

From: [[fireship]] <br/> 

[[reactjs_overview_and_history | React]] is a JavaScript library developed at Facebook and released in 2013, designed for building user interfaces (UI) <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It has been one of the most influential UI libraries in recent memory <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## React Components

In [[reactjs_overview_and_history | React]], components are used to build logical, reusable parts of the user interface <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. The approach to building a component is intentionally simple, brought down to its theoretical minimum <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

### Component Structure

A [[reactjs_overview_and_history | React]] component is essentially a JavaScript function <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. The function's return value is the HTML or UI representation of the component <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. This UI is written using a special syntax called JSX, which allows for the easy combination of JavaScript and HTML markup <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

### Passing Data with Props

To pass data into a component, you can use a [[state_and_props_in_react | `props`]] argument <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. This argument can then be referenced within the function body or directly in the UI using braces <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. If the value of these [[state_and_props_in_react | `props`]] changes, [[reactjs_overview_and_history | React]] will automatically update the UI accordingly <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

### Managing Internal State with Hooks

For a component to manage its own internal [[state_and_props_in_react | state]], the [[react_hooks_explained | `state` hook]] can be used <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. A [[react_hooks_explained | hook]] is a function that returns a value (the reactive [[state_and_props_in_react | state]]) and a dedicated function to modify that value <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

For example:
*   `count` represents the reactive [[state_and_props_in_react | state]] <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   `setCount` is the function used to change this [[state_and_props_in_react | state]] <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

When `count` is used in the template, it will always display its most recent value <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This `setCount` function can be bound to user interactions, such as a button click event, allowing users to modify the component's [[state_and_props_in_react | state]] <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. [[reactjs_overview_and_history | React]] also provides various other built-in [[react_hooks_explained | hooks]] to handle common use cases <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

### The React Ecosystem

A major advantage of using [[reactjs_overview_and_history | React]] is the extensive [[react_ecosystem_and_libraries | ecosystem]] that surrounds it <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. While [[reactjs_overview_and_history | React]] itself doesn't directly handle concerns like routing, [[state_and_props_in_react | state]] management, or animation, it allows these functionalities to evolve naturally within the open-source community <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. This means that for nearly any development need, there is likely a supporting library available <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

Examples of supporting libraries include:
*   **Static Sites**: Gatsby <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>
*   **Server-Side Rendering**: Next.js <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>
*   **Animation**: Spring <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>
*   **Forms**: Formic <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>
*   **State Management**: Redux, MobX, Flux, Recoil, XState, and many more <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>

This abundance of choices allows developers to accomplish tasks in their preferred manner <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

### Beyond Web Components

Once familiar with [[reactjs_overview_and_history | React]], developers can easily transition to [[applications_of_react_including_react_native | React Native]] to build mobile applications <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. The knowledge of this UI library is one of the most in-demand skills for front-end developers today <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.