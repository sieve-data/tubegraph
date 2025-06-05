---
title: Local vs global state in Flutter
videoId: 3tm-R7ymwhc
---

From: [[fireship]] <br/> 

In Flutter, **state** refers to data that changes over the lifecycle of an application <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. In a reactive framework like Flutter, the UI can be thought of as the return value of a function, with state as its argument <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. [[flutter_state_management_strategies | State management]] involves choosing an ideal strategy for your app <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Local State

Local state refers to data that is self-contained within a single widget <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. Flutter provides built-in tools for managing this type of state, which is generally straightforward <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

### StatefulWidget

The `StatefulWidget` is a fundamental building block for managing local state <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. When you run `flutter create`, the starter code provided uses a `StatefulWidget` to increment a counter <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

To create a `StatefulWidget`, two classes are needed <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>:
1.  **The `StatefulWidget` itself**: This class implements a `createState` method, which returns the second class <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
2.  **An extension of the `State` class**: This is where the core logic resides <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
    *   It defines properties that represent the widget's data state, like a `counter` integer <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
    *   A method, such as `incrementCounter`, calls `setState` to tell the widget to re-render when a value changes <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
    *   The `build` function defines the actual widgets that will be rebuilt every time `setState` is called <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

While `StatefulWidget` is effective for local state <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>, it has some drawbacks:
*   It requires defining two separate classes, which can be confusing and add boilerplate <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   Calling `setState` extensively throughout the code does not scale well, especially with many properties to update <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

### StatefulBuilder

`StatefulBuilder` is one of several builder widgets in Flutter that allow you to react to changes <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. It simplifies `StatefulWidget` code <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

When using `StatefulBuilder`:
*   You typically extend a `StatelessWidget` <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   The `StatefulBuilder` takes a `builder` function, which provides access to the `BuildContext` and a `setState` function <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
*   Calling `setState` within this builder tells the `StatefulBuilder` to rebuild all widgets inside its function <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

> [!CAUTION] Mutability and Stateless Widgets
> When using `StatefulBuilder` within a `StatelessWidget`, directly incrementing a class property (like `counter`) violates the immutability contract of a `StatelessWidget` <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. It's recommended to set up data as a `Map` or `List` because values within these data structures can be mutated without breaking the contract <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

`StatefulBuilder` is a useful tool that helps avoid `StatefulWidget` boilerplate and is ideal for simple local [[flutter_state_management_strategies | state management]] <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

## Global State (App State)

Global state, or app state, refers to data that needs to be shared throughout the widget tree <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. While data can easily be passed from parent to child, passing data from child to parent or between siblings is not practical <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. Almost every non-trivial app will require some form of shared state <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

### InheritedWidget

The `InheritedWidget` is a fundamental building block in Flutter, implemented in many framework features <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. It allows context to be passed to any of its descendants, regardless of how deeply nested they are <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

Typically, an `InheritedWidget` is placed high in the widget tree <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   It extends Flutter's built-in `InheritedWidget` and takes a child widget <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   The `updateShouldNotify` method is overridden to determine if descendants need to rebuild when the inherited widget is rebuilt <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   A conventional static `of` method is implemented to easily access the inherited widget from descendants <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   Since `InheritedWidget` is immutable, it can be wrapped in a `StatefulWidget` to trigger rebuilds, or mutable data structures like `Maps` can be used to hold the state directly within the inherited widget <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

Any descendant widget can access the values from the `InheritedWidget` using `of(context)`, even if it's many levels deep, without direct passing through each constructor <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. While important to understand, direct use of `InheritedWidget` for [[managing_state_in_flutter_applications | state management]] is generally not recommended as better alternatives exist that abstract its functionality <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

### Streams and RxDart (BehaviorSubject)

Using a special type of stream called a `BehaviorSubject` from RxDart is a powerful way to manage global state <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

Key features of `BehaviorSubject`:
*   Always has a current value that can be read in Flutter's `build` methods <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   Can be treated as a stream, allowing new values to be added to it <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
*   Is a broadcast stream by default, meaning multiple widgets can listen to the same stream <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   Business logic can be implemented independently of the widget tree, making it easier to test and reason about <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

To consume this state in a widget:
*   A `StreamBuilder` widget is used, passed the stream from the `BehaviorSubject` <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   Every time a new value is added to the `BehaviorSubject`, the `StreamBuilder`'s widget will rebuild <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   `StreamBuilder` automatically unsubscribes from the stream when the widget is disposed, preventing memory leaks <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   This approach allows less of the UI to be repainted compared to previous examples, as the `StreamBuilder` can be nested deeper <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

### GetIt (Service Locator)

To manage global access to services like a counter service using `BehaviorSubject`, a service locator library like GetIt can be used <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.
*   Register a singleton instance of the service (e.g., `Counter`) in the `main` function <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   This ensures the counter class is instantiated only once <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
*   It makes the state easier to mock for integration tests <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

### BLoC Pattern

The BLoC (Business Logic Component) pattern is a robust [[flutter_state_management_strategies | state management]] solution, particularly when using the `flutter_bloc` library <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. This library extends `InheritedWidget` to intuitively pass state around the widget tree <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

BLoC promotes a one-way data flow:
1.  **Event**: A user action (e.g., clicking a button) dispatches an event <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
2.  **Block**: The event is dispatched to a block <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
3.  **State**: The block reduces the event to the next state and emits it as a stream <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

Implementation steps:
*   Install `bloc` and `flutter_bloc` <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.
*   Add a `BlocProvider` to the root of the application, which allows all descendants to access the block's state <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
*   Define `events` (actions) that users can dispatch to the block, often as an enum <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.
*   Create a `Bloc` class that extends `Bloc`, defining the initial state and overriding `mapEventToState` (the reducer function) <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. This function takes the current state and an event to determine the next state <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
*   In the UI, use a `BlocBuilder` (similar to `StreamBuilder`) to rebuild the UI when the block's state changes <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
*   To change state, dispatch an action to the block (e.g., `_counterBloc.add(CounterEvent.increment)`) <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.

The BLoC pattern separates business logic from the UI, making the widget responsible only for rendering and dispatching actions <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>. While it involves more code, it's a solid [[flutter_state_management_strategies | state management]] solution for the long term <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.

### Other Global State Strategies

Several other powerful [[flutter_state_management_strategies | state management]] libraries exist, many originating from the [[react_native_vs_flutter_comparison | React]] world:

*   **Redux**: The "godfather" of [[managing_state_in_flutter_applications | state management]], it follows concepts similar to the BLoC pattern <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>. It typically involves a single store provider for the entire app, connected to different widgets as needed <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. It's recommended for those already experienced with Redux <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   **MobX**: Also from the [[react_native_vs_flutter_comparison | React]] world, MobX shares principles with Redux and BLoC but offers additional abstractions for a more developer-friendly process <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. It includes a code generation package to eliminate boilerplate, useful for small teams or rapid prototyping <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.
*   **Scoped Model**: Considered a simpler alternative to heavyweight libraries like MobX, Redux, and BLoC <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. It's described in official Flutter documentation <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a> and uses an `InheritedWidget` to pass state <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>. It allows defining data and mutations within a model, which is then scoped in the widget tree, with a builder rebuilding the UI when the model changes <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **Flutter Hooks**: A promising library for improving productivity and code reusability <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. Hooks, like `useReducer`, can set up state and action dispatching, providing a nice alternative to `StatefulWidget` for local state <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.
*   **Firebase**: Often overlooked as a [[managing_state_in_flutter_applications | state management]] system, Firebase is highly advanced <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>. While not a solution for every state need, it can handle complex aspects like user authentication, persisting data to a backend database, remote config, and file uploads <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>. The Firebase SDK exposes everything as streams or futures, which aligns perfectly with a reactive framework like Flutter <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.