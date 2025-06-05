---
title: State and props in React
videoId: Tn6-PIqc4UM
---

From: [[fireship]] <br/> 

[[reactjs_overview_and_history | React]], a JavaScript library for [[building_components_with_react | building components]] user interfaces, provides mechanisms to manage data within components, namely through "props" and "state" <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Props

Props are used to pass data into a component <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. To pass data, you simply provide a `props` argument to the component <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This `props` argument can then be referenced within the component's [[reactjs_functional_and_classbased_components | function body]] or in the UI using braces <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. If the value of a prop changes, [[reactjs_overview_and_history | React]] will "react" by updating the UI <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## State

To give a component its own internal state, you can use the [[react_hooks_explained | state hook]] <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. A [[react_hooks_explained | hook]] is a function that returns a value and a corresponding function to change that value <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

For example, `count` could be a reactive state, and `setCount` would be the function to change it <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. When used in the template, `count` will always display its most recent value <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This `setCount` function can be bound to events, such as a button click, allowing users to modify the component's state <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

[[reactjs_overview_and_history | React]] offers various other built-in [[react_hooks_explained | hooks]] to handle common use cases <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Beyond its core library, [[reactjs_overview_and_history | React]] is surrounded by a massive [[react_ecosystem_and_libraries | ecosystem]] of supporting libraries that address concerns like [[css_variables_and_state_management | state management]], routing, and animation <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.