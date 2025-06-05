---
title: Managing state in Flutter applications
videoId: 1xipg02Wu8s
---

From: [[fireship]] <br/> 

State refers to the data that changes throughout the life cycle of a Flutter application <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. Effective [[flutter_state_management_strategies | state management]] is crucial for building dynamic and responsive user interfaces.

## Stateless vs. Stateful Widgets

Flutter applications are built using widgets. There are two primary types of widgets relevant to [[Local vs global state in Flutter | state management]]:

### Stateless Widget
A `StatelessWidget` does not have any internal mutable data; it simply paints pixels to the screen based on its configuration <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. As its name implies, a `StatelessWidget` has no state <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

### Stateful Widget
To enable mutable data within a widget, you must convert it to a `StatefulWidget` <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. This can be done by right-clicking on the widget and using the "refactor tool" to select "convert to Stateful Widget" <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.

A `StatefulWidget` is broken down into two distinct classes <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>:
1.  **The widget class itself**: This remains immutable.
2.  **A `State` class**: This is where you manage mutable data <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

The `State` class includes a `build` method <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a> and allows you to define variables <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. To change these variables and trigger a UI update, you use the built-in `setState` function <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>. When `setState` is called, the widget automatically re-renders to reflect the latest data <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

**Example: Counter App with `setState`**
You can create a counter application by defining a `count` property on the `State` class and referencing its value in the UI using a `Text` widget <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. When a button is pressed, `setState` is called to increment the count, and the UI updates automatically <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

### Widget Lifecycle Hooks
Stateful widgets also offer lifecycle hooks for data initialization and cleanup:
*   **`initState`**: Called once when the widget is first initialized <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. This is useful for fetching data from a database or other one-time setup.
*   **`dispose`**: Runs when the widget is removed from the UI <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.

## Advanced State Management Approaches
While `StatefulWidget` with `setState` is fundamental, it's not the only approach to [[State management with Flutter and Firebase | state management]] in Flutter <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. Many different strategies and opinions exist regarding this topic <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

For [[Advanced data management techniques in Flutter apps | more advanced data management]], solutions like the `provider` package can be used <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. `provider` allows sharing real-time data throughout the entire widget tree without needing to use `StatefulWidget` <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. Other full-blown solutions include Block and Cubit <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.