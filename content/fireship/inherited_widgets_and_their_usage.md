---
title: Inherited widgets and their usage
videoId: 3tm-R7ymwhc
---

From: [[fireship]] <br/> 

[[managing_state_in_flutter_applications | State management]] in Flutter is a complex topic that brings out strong opinions among developers <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. While many advanced libraries exist, understanding fundamental building blocks like the `InheritedWidget` is crucial <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

## What is an Inherited Widget?
An `InheritedWidget` is a fundamental building block in Flutter's framework <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. Its primary purpose is to allow data (context) to be passed to any of its descendants in the widget tree, regardless of how deeply nested they are <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. This solves the problem of "prop drilling," where data needs to be manually passed through multiple intermediary widgets to reach a distant descendant.

## How Inherited Widgets Work
To use an `InheritedWidget`, it's typically placed high up in the widget tree, often near the root of the application <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

An `InheritedWidget` implementation involves:
*   **Extending `InheritedWidget`**: Your custom inherited widget class extends Flutter's built-in `InheritedWidget` <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   **Constructor**: It takes a `child` widget as an argument to its constructor, which represents the subtree that will have access to its context <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **`updateShouldNotify` Method**: This method must be overridden and is called when the `InheritedWidget` itself is rebuilt <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. Its return value determines whether dependent descendant widgets need to rebuild <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. While it can be set to `true` to always rebuild, it's typically used to compare the `oldWidget` and `newWidget` to optimize re-renders <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   **`of` Static Method (Convention)**: It's conventional to implement a static `of` method that uses `BuildContext.inheritFromWidgetOfExactType` (or `context.dependOnInheritedWidgetOfExactType`) to retrieve the inherited widget instance and its data from the nearest ancestor <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### Example: `InheritedCounter`
A simplified `InheritedCounter` example demonstrates its core functionality:
1.  **Placement**: The `InheritedCounter` is placed as a parent to the `HomePage` widget <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
2.  **Immutability**: `InheritedWidget`s are immutable <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. To allow its data to change, it would typically be wrapped in a [[stateful_and_stateless_widgets | stateful widget]] <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. Alternatively, a map or list can be used for the internal data, as these data structures can be mutated without breaking the contract of an immutable [[stateful_and_stateless_widgets | stateless widget]] wrapper <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>, <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
3.  **Data Access**: Descendant widgets, such as `HomePage`, can then access the values from the `InheritedCounter` by calling `of(context)` <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. This allows deeply nested widgets (e.g., 20 levels deep) to access data without explicit passing through constructors <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

## Usage and Recommendations
While `InheritedWidget` is fundamental, directly using it as a primary [[managing_state_in_flutter_applications | state management]] solution is generally not recommended <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. This is because many other Flutter features and external libraries, such as `BlockProvider` within the `flutter_bloc` library, already implement similar functionality in more intuitive and less awkward ways <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>, <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. Even `ScopedModel`, an officially described state management approach, leverages inherited widgets internally <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.

Understanding `InheritedWidget` remains important because it underpins how many other parts of the Flutter framework and popular state management solutions function <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.