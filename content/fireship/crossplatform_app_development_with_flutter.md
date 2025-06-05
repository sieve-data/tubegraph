---
title: Crossplatform app development with Flutter
videoId: 1xipg02Wu8s
---

From: [[fireship]] <br/> 

[[introduction_to_flutter_for_javascript_developers | Flutter]] is rapidly gaining popularity as a [[crossplatform_mobile_app_development | cross-platform]] framework due to its excellent developer experience and capability to ship high-quality applications across various platforms <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. It supports deployment on iOS, Android, the web, and desktop <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. While it offers a unique approach to app development, it does have a steeper learning curve <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Getting Started with Flutter

To begin, developers should visit `flutter.dev` and follow the installation instructions for their specific system <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. For an easier start, [[introduction_to_flutter_for_javascript_developers | DartPad]] allows editing and running [[introduction_to_flutter_for_javascript_developers | Flutter]] code directly in the browser <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

### Project Setup and Development Tools
A new project can be created by running `flutter create` in the terminal <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. It is recommended to open the project in VS Code with the [[introduction_to_flutter_for_javascript_developers | Flutter]] extension installed <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Developers can select a device (e.g., Windows, Chrome, mobile emulator) from the VS Code interface <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a> or run the app from the command line using `flutter run` <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

### Productivity Boosters
[[performance_and_developer_experience_in_react_native_and_flutter | Flutter]] development is highly productive due to its powerful IDE tooling <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. Key features include:
*   **Autocompletion**: The IDE provides autocompletion for code after typing a period <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   **Hot Reload**: Typing a lowercase 'r' in the terminal performs a hot reload, instantly reflecting UI changes without a full app rebuild <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   **Refactor Tool**: Hitting `Control + Period` (or right-clicking) brings up a refactor tool, significantly speeding up code refactoring <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This tool can, for example, automatically wrap a widget with a `Center` widget <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   **Trailing Commas**: Using a trailing comma after every code block helps maintain nicely formatted code, especially when formatting the document <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

## [[building_user_interfaces_with_flutter_widgets | Building User Interfaces with Flutter Widgets]]

[[building_user_interfaces_with_flutter_widgets | Flutter]] uses a hierarchical "widget tree" structure to compose complex UIs from smaller, reusable components <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

### Core Concepts
*   **Material Package**: Importing `flutter/material.dart` provides access to hundreds of pre-built widgets, from basic building blocks like `Text` to complex UI elements like `PageView` <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   **`main` Function**: The program's execution begins in the `main` function <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   **`runApp`**: This global function takes a single widget as an argument and inflates it to the screen <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
*   **`MaterialApp`**: Used as the root of the application, allowing configuration of themes and routes <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   **`Scaffold`**: Enables building screens with common UI elements such as an app bar <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>, floating action button <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>, bottom bar <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>, and a drawer that animates from the left <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

### Widget Types
*   **[[building_mobile_app_components_with_flutter | StatelessWidget]]**: Used for UI elements that do not have any internal, mutable data. They simply paint pixels to the screen <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   **[[building_mobile_app_components_with_flutter | StatefulWidget]]**: Provides mutable data (state) to a widget. It is composed of two classes: an immutable widget class and a state class for mutable data <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

### Layout Widgets
[[building_mobile_app_components_with_flutter | Flutter]] provides several widgets for precise UI layout:
*   **`Container`**: A fundamental layout widget, similar to an HTML `div`, that can hold a single child widget. It allows customization of dimensions (margin, padding, height, width), color, and decoration (border, gradient, shape, shadow) <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   **`Center`**: Wraps a widget to center it on the screen <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **`Padding`**: Used to apply padding around a child widget, often preferred over using a `Container` solely for padding <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   **`SizedBox`**: Used for creating a fixed-width and height container, an alternative to `Container` for this specific use case <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   **Flex Layout (`Row` and `Column`)**:
    *   **`Row`**: Lays out multiple children horizontally <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
    *   **`Column`**: Lays out multiple children vertically <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
    *   **Main and Cross Axis**: The direction of flow is the main axis; the opposite is the cross axis. Spacing and alignment can be controlled with `crossAxisAlignment` and `mainAxisAlignment` <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
    *   **`Flexible` and `Expanded`**: Used to control how children occupy space within a `Row` or `Column`. `Expanded` tells a child to take up all available space and its `flex` value can prioritize space distribution among siblings <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   **`Stack`**: Allows widgets to overlap, useful for elements like a floating button over other UI elements <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. Children are rendered in the order they appear in the list <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.
*   **`Positioned`**: Used within a `Stack` to move a widget to a specific spot, similar to absolute positioning in CSS <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
*   **`Align`**: Modifies a widget's positioning relative to its parent within a `Stack` (e.g., top-left, bottom-right, center) <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

### Debugging Layout Issues
If widgets overflow their parent's bounds, a "red screen of death" or "black and yellow error tape" appears <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. The terminal output links to [[introduction_to_flutter_for_javascript_developers | Flutter]]'s debugger, which provides layout information <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   **Scrollable Views**: [[introduction_to_flutter_for_javascript_developers | Flutter]] views do not automatically scroll. A widget like `ListView` is needed to enable scrolling for a list of children <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. `ListView` supports both horizontal and vertical scrolling and can garbage collect off-screen items for performance <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.
*   **Dynamic Widgets with Builders**: Many widgets can be built dynamically using `Builders`, which are functions that map a list of data to a list of widgets. This allows for infinitely long, scrollable lists where children are rendered lazily, maintaining UI smoothness and speed <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

## State Management

State refers to the data that changes throughout an app's lifecycle <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
*   **`StatelessWidget` vs. `StatefulWidget`**: As implied by the name, a [[building_mobile_app_components_with_flutter | StatelessWidget]] has no mutable state <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. To introduce mutable data, a widget must be converted to a [[building_mobile_app_components_with_flutter | StatefulWidget]] <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
*   **`setState`**: The built-in `setState` function is used within a [[building_mobile_app_components_with_flutter | StatefulWidget]]'s state class to change mutable data, which then automatically triggers a re-render of the widget to reflect the latest data <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.
*   **Lifecycle Hooks**:
    *   **`initState`**: Called once when the widget is first initialized, useful for fetching data <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.
    *   **`dispose`**: Runs when the widget is removed from the UI <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
*   **Alternative State Management Solutions**: While `setState` is fundamental, [[introduction_to_flutter_for_javascript_developers | Flutter]] offers many other approaches for state management, including packages like `provider`, `BLoC`, and `Cubit`, which allow sharing real-time data throughout the widget tree without always needing a [[building_mobile_app_components_with_flutter | StatefulWidget]] <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.

## [[navigating_between_screens_in_flutter_apps | Navigating Between Screens in Flutter Apps]]

[[navigating_between_screens_in_flutter_apps | Flutter]] navigation can be thought of as a stack where screens are pushed and popped <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   **`Navigator.push`**: Used to add a new screen to the top of the navigation stack. It typically takes a `MaterialPageRoute` which expects a builder function that returns the screen to render <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
*   **`Navigator.pop`**: The back button automatically added to the app bar by [[introduction_to_flutter_for_javascript_developers | Flutter]] internally calls `Navigator.pop` to remove the current screen from the stack <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.
*   **`Hero` Widget**: This widget enables animating elements from one screen to another during navigation. By wrapping an element on both screens with a `Hero` widget and providing them with the same `tag` (ID), [[introduction_to_flutter_for_javascript_developers | Flutter]] smoothly animates the element between routes <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. This feature is particularly impactful for lists of images <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.