---
title: Flutter state management strategies
videoId: 3tm-R7ymwhc
---

From: [[fireship]] <br/> 

[[managing_state_in_flutter_applications | State management]] is a topic that often elicits strong opinions among developers <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This article explores various strategies for handling state in Flutter applications, ranging from built-in tools for local state to advanced libraries for global app state <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## What is State?

In a reactive framework like Flutter, the User Interface (UI) can be thought of as the return value of a function that takes "state" as its argument <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Therefore, state is simply data that changes over the lifecycle of an application <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

### Local vs. Global State

*   **Local State**: Data that is self-contained within a single widget <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. Managing local state is generally straightforward <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   [[local_vs_global_state_in_flutter | Global State]] (App State): Data that needs to be shared throughout the widget tree <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. While data can be passed from parent to child, passing data from child to parent or between siblings is not practical <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. Almost every non-trivial app will eventually require some form of shared state <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

## Strategies for State Management

### 1. [[stateful_and_stateless_widgets | Stateful Widget]]

This is the default approach provided by Flutter when creating a new project <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   **Structure**: Requires two classes: the `StatefulWidget` itself, which implements a `createState` method, and a separate `State` class where the primary logic and data (`counter` property) reside <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Re-rendering**: To update the UI, a method (e.g., `incrementCounter`) calls `setState`, which tells the widget to re-render when its value changes <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. The `build` function then defines the widgets that will be rebuilt <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   **Pros**: Great for managing local state <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   **Cons**: Involves defining two separate classes, which can be confusing and add boilerplate <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Calling `setState` extensively does not scale well, especially with many properties <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

### 2. Stateful Builder

A `StatefulBuilder` widget allows simplification of stateful widget code <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   **Usage**: It can be used within a [[stateful_and_stateless_widgets | StatelessWidget]] <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. It takes a builder function that provides access to `BuildContext` and a `setState` function <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. Calling this `setState` rebuilds only the widgets within the `StatefulBuilder`'s function <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   **Considerations**: Modifying properties directly within a [[stateful_and_stateless_widgets | StatelessWidget]] (which is immutable) is a violation of Flutter's rules <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. It's recommended to set up data as a map or list, as values within these structures can be mutated without breaking the immutable contract <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
*   **Pros**: Helps avoid the boilerplate of a [[stateful_and_stateless_widgets | StatefulWidget]] <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. Ideal for simple local state management <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

### 3. Inherited Widget

The `InheritedWidget` is a fundamental building block in Flutter, though not typically recommended as a direct state management solution <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **Purpose**: Allows passing context (data) to any of its descendants, regardless of nesting depth, without direct constructor passing <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
*   **Implementation**: Placed higher in the widget tree (e.g., `InheritedCounter` wrapping `HomePage`) <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. It overrides `updateShouldNotify` to determine if descendants need to rebuild <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. A static `of` method is conventionally implemented to easily access the widget's context <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Limitations**: `InheritedWidget` is immutable. To manage mutable state, it typically needs to be wrapped in a [[stateful_and_stateless_widgets | StatefulWidget]] or manage its internal data as mutable structures like maps or lists <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. There are better alternatives that abstract its complexities <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

### 4. [[streambased_state_management_with_behaviorsubject | Stream-based State Management with BehaviorSubject]]

Leveraging `BehaviorSubject` from RxDart is a personal favorite for managing global state <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
*   **BehaviorSubject Features**:
    *   Always has a current value that can be read <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
    *   Can be treated as a stream, allowing new values to be added <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
    *   It is a broadcast stream by default, allowing multiple widgets to listen <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Decoupling**: Business logic can be implemented independently of the widget tree, making it easier to test and reason about <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
*   **Widget Integration**:
    *   A `StreamBuilder` widget is used in the `build` method, passed the `BehaviorSubject`'s stream <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
    *   Every time a new value is added to the `BehaviorSubject`, the `StreamBuilder` will rebuild <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
    *   This allows repainting less of the UI compared to previous examples, by nesting the `StreamBuilder` deeper in the widget tree <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
    *   `StreamBuilder` automatically unsubscribes from the stream when the widget is disposed, preventing memory leaks <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   **Singleton Management with GetIt**: To avoid global namespace instantiation (which is generally frowned upon), a library like GetIt can be used to register the `BehaviorSubject`-based state class as a singleton <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>. This simplifies testing and guarantees a single instance <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

### 5. Block Pattern (Business Logic Component)

The Block pattern provides an explicit one-way data flow, similar to Redux <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. The `flutter_block` library is highly recommended for implementation <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.
*   **Underlying Mechanism**: Extends the `InheritedWidget` to pass state around the widget tree in a more intuitive way <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
*   **Data Flow**:
    1.  An **Event** (e.g., user click) is dispatched to a Block <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
    2.  The **Block** reduces the next state and emits it as a stream <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
    3.  A `StreamBuilder` (or `BlocBuilder`) consumes the stream to update the UI <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
*   **Implementation Steps**:
    1.  Add `BlockProvider` to the root of the application, defining the Block type <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. Descendants can then access this Block's state <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
    2.  Define **Events** (e.g., an `enum` for `CounterEvent`) that users can dispatch <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
    3.  Create the **Block** class (e.g., `CounterBlock`) by extending `Block`, defining the initial state, and implementing `mapEventToState` (a reducer function) to determine how state changes based on events <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
    4.  In the UI widget, access the Block using `BlockProvider.of(context)` <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
    5.  Use a `BlocBuilder` to rebuild the UI when the Block's state changes, similar to a `StreamBuilder` <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
    6.  To change state, dispatch an action to the Block (e.g., `_block.add(CounterEvent.increment)`), rather than mutating state directly <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.
*   **Pros**: Separates business logic from the UI, making widgets only concerned with rendering and dispatching actions <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>. A solid solution for the long run <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.

### 6. Redux

Redux has been a de facto state management library in the React world and is also available on Flutter <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.
*   **Concepts**: Follows similar concepts to the Block pattern <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.
*   **Usage**: Typically involves a single store provider for the entire app, which is then connected to different widgets as needed <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
*   **Recommendation**: For newcomers to state management, Block is often recommended first. However, for those experienced with Redux, it's a familiar option <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

### 7. MobX

Another library originating from the React world that is now available in Flutter <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
*   **Principles**: Adheres to similar principles as Redux and Block <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.
*   **Developer Experience**: Offers extra abstractions to make the process more developer-friendly <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
*   **Code Generation**: Includes a code generation package to eliminate boilerplate code <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.
*   **Use Cases**: Useful for applying powerful state management patterns with small teams or when rapid prototyping <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.

### 8. Scoped Model

Scoped Model is a lightweight state management approach described in the official Flutter documentation <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
*   **Mechanism**: Uses an `InheritedWidget` to pass state around the tree <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.
*   **Simplicity**: It doesn't require writing custom reducer functions, actions, or other boilerplate code <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.
*   **Usage**: Define data and mutations within a "model," scope that model somewhere in the widget tree, and then use a builder to rebuild the UI when the model changes <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.
*   **Pros**: A relatively simple way to handle shared state <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.

### 9. Flutter Hooks

Flutter Hooks offers a promising approach to improve productivity and code reusability <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>, drawing inspiration from React Hooks.
*   **Benefits**: Hooks can handle common setup tasks like state and action dispatching (e.g., `useReducer` hook) <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
*   **Use Cases**: A nice alternative to the [[stateful_and_stateless_widgets | StatefulWidget]] and other approaches for local state <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

### 10. [[state_management_with_flutter_and_firebase | Firebase]]

Many developers might not realize that [[state_management_with_flutter_and_firebase | Firebase]] itself functions as a highly advanced state management system <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.
*   **Capabilities**: While not a solution for every state management need, it can handle complex aspects like user authentication, persisting data to a backend database, remote configuration, and file uploads <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.
*   **Integration with Flutter**: The [[state_management_with_flutter_and_firebase | Firebase]] SDK exposes everything as streams or futures, which integrates seamlessly with Flutter's reactive framework <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.

> [!NOTE]
> Often, apps are over-engineered with large [[advanced_data_management_techniques_in_flutter_apps | state management libraries]] that aren't truly necessary <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Even the creators of these libraries might suggest you don't always need them <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. Consider the pros and cons of various libraries and focus on fundamental building blocks first <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.