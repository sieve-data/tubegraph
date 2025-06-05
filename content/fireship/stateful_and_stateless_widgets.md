---
title: Stateful and stateless widgets
videoId: 3tm-R7ymwhc
---

From: [[fireship]] <br/> 

## Understanding State
In a reactive framework like Flutter, the user interface (UI) can be thought of as the return value of a function that takes "state" as its argument <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. [[managing_state_in_flutter_applications | State]] is simply data that changes over the lifecycle of an application <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

There are two primary types of [[local_vs_global_state_in_flutter | state]] in Flutter:
*   **[[local_vs_global_state_in_flutter | Local state]]**: Data self-contained within a single [[building_user_interfaces_with_flutter_widgets | widget]] <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. This is generally straightforward to manage using built-in Flutter tools <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   **[[local_vs_global_state_in_flutter | Global state]] (App State)**: Data that needs to be shared throughout the [[building_user_interfaces_with_flutter_widgets | widget]] tree <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. While passing data from parent to child is possible, passing it the other way (child to parent, or sibling to sibling) is not practical <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. Almost every non-trivial app will require some form of shared state <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

[[managing_state_in_flutter_applications | State management]] is a topic that often elicits strong opinions among developers <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. There are many different [[flutter_state_management_strategies | state management strategies]] and libraries available to address both [[local_vs_global_state_in_flutter | local]] and [[local_vs_global_state_in_flutter | global state]] needs <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Stateful Widget
The `StatefulWidget` is a fundamental building block in Flutter for [[local_vs_global_state_in_flutter | local state management]] <a class="yt-timestamp" data-t="01:02:11">[00:02:21]</a>. When running `flutter create`, the starter code for a counter app uses a `StatefulWidget` to increment a counter <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

To create a `StatefulWidget`, two classes are required <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>:
1.  **The `StatefulWidget` itself**: This class implements a `createState` method <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
2.  **An extension of the `State` class**: This is where the core logic and mutable data (state) reside <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

Within the `State` class:
*   A property, such as `counter` (an integer), defines the actual data state of the [[building_user_interfaces_with_flutter_widgets | widget]] <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   A method, for example `incrementCounter`, calls `setState` <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   The `setState` method tells the [[building_user_interfaces_with_flutter_widgets | widget]] to re-render when the state value changes <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   The `build` function defines the actual [[building_user_interfaces_with_flutter_widgets | widgets]] that will be rebuilt every time `setState` is called <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. For example, a `Text` [[building_user_interfaces_with_flutter_widgets | widget]] displays the counter's current value, and a `FloatingActionButton` increments it when pressed <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

### Downsides of Stateful Widget
While `StatefulWidget` is effective for [[local_vs_global_state_in_flutter | local state]], it has some drawbacks:
*   It requires defining two separate classes, which can be confusing and adds boilerplate code <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   Calling `setState` extensively across many properties does not scale well and can lead to a messy codebase <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

## Stateless Widget
A `StatelessWidget` is a [[building_user_interfaces_with_flutter_widgets | widget]] whose configuration is immutable, meaning its properties should never be reassigned <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. They are ideal for [[building_user_interfaces_with_flutter_widgets | widgets]] that do not manage their own state.

### Stateful Builder within a Stateless Widget
One way to simplify [[local_vs_global_state_in_flutter | local state management]] and avoid some `StatefulWidget` boilerplate is to use a `StatefulBuilder` within a `StatelessWidget` <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

*   You start by extending a `StatelessWidget` <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   Inside the `build` method, a `StatefulBuilder` [[building_user_interfaces_with_flutter_widgets | widget]] is added <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   The `StatefulBuilder`'s `builder` function provides access to `buildContext` and a `setState` function <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
*   Calling this `setState` will tell only the `StatefulBuilder` to rebuild its contained [[building_user_interfaces_with_flutter_widgets | widgets]] <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

**Important Consideration**: While using `StatefulBuilder` in a `StatelessWidget` is possible, directly incrementing a counter variable defined in the `StatelessWidget` violates its immutability contract, indicated by a green squiggly line in development <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. To adhere to the contract, it's recommended to set up mutable data (like a counter) as a map or a list, as values within these data structures can be mutated without breaking the `StatelessWidget`'s immutability <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

The `StatefulBuilder` is a useful tool for simple [[local_vs_global_state_in_flutter | local state management]] and reducing `StatefulWidget` boilerplate <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

## Relation to Inherited Widgets and Other State Management Approaches
Many advanced [[managing_state_in_flutter_applications | state management]] solutions, such as [[inherited_widgets_and_their_usage | InheritedWidget]], [[flutter_state_management_strategies | Block]], and Scoped Model, build upon the concepts of passing data through the [[building_user_interfaces_with_flutter_widgets | widget]] tree.

*   **[[inherited_widgets_and_their_usage | Inherited Widget]]**: A fundamental building block in Flutter that allows data to be passed to any of its descendants, regardless of how deeply nested they are in the [[building_user_interfaces_with_flutter_widgets | widget]] tree <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. While not recommended as a direct [[managing_state_in_flutter_applications | state management]] solution, it's crucial to understand how it works as it's implemented in many other framework features <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **[[firebase_data_streams_and_streambuilder_widget | StreamBuilder]]**: Allows [[building_user_interfaces_with_flutter_widgets | widgets]] to react to data streams, which is a powerful way to manage [[local_vs_global_state_in_flutter | global state]] and repaint only necessary parts of the UI <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   **Block Pattern**: Utilizes [[inherited_widgets_and_their_usage | InheritedWidget]] under the hood to provide an intuitive way to pass state around the [[building_user_interfaces_with_flutter_widgets | widget]] tree <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Flutter Hooks**: Offers an alternative for [[local_vs_global_state_in_flutter | local state management]] that can improve productivity and code reusability by abstracting away boilerplate code, similar to `StatefulWidget` alternatives <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.