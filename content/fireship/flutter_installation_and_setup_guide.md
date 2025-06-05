---
title: Flutter installation and setup guide
videoId: 1xipg02Wu8s
---

From: [[fireship]] <br/> 

[[introduction_to_flutter_for_javascript_developers | Flutter]] is a popular cross-platform framework known for its excellent developer experience and ability to ship high-quality applications across multiple platforms, including iOS, Android, web, and desktop <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Installation
To begin, the most important skill for any developer is following directions <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   **Official Documentation** Visit `flutter.dev` and follow the install instructions specific to your system <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
*   **DartPad** For an easier start, DartPad allows you to edit and run [[introduction_to_flutter_for_javascript_developers | Flutter]] code directly in the browser <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## Project Creation
1.  Open your terminal <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
2.  Create a new project by running the command `flutter create` <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## Development Environment Setup
1.  Open the newly created project in VS Code <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
2.  Ensure you have the [[introduction_to_flutter_for_javascript_developers | Flutter]] extension installed in VS Code <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
3.  At the bottom of the VS Code interface, you will find an option to select a device, such as Windows, Chrome, or a mobile emulator <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## Running the Application
You can run your [[introduction_to_flutter_for_javascript_developers | Flutter]] application from the command line by executing `flutter run` <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## Hot Reload
[[introduction_to_flutter_for_javascript_developers | Flutter]] features a "hot reload" capability that allows you to instantly see UI changes without rebuilding the entire application <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
*   To perform a hot reload, save your file and then type a lowercase `r` into the terminal <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

### Productivity Boosters
*   **Refactor Tool** Refactoring code is significantly faster by hitting `control + period` (or right-clicking) to access the refactor tool <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. This tool can automatically wrap widgets, among other things <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **Code Completion** When typing after a period, the IDE provides automatic code completion, which is a key factor in [[introduction_to_flutter_for_javascript_developers | Flutter]]'s productivity <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   **Trailing Commas** Adding a trailing comma after every code block, though not required, helps keep your code nicely formatted <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. If you right-click and choose "Format Document," it will format the code into multiple lines <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

### Core Concepts
*   **Material Design Package** Importing the `flutter/material` package provides access to hundreds of pre-built widgets, from low-level building blocks like `Text` to complex UI elements like `PageView` <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Widgets** As a [[introduction_to_flutter_for_javascript_developers | Flutter]] developer, you'll combine widgets into a tree-like structure to create complex UIs <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   **`main` function** This is where the program execution starts <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   **`runApp` function** A global [[introduction_to_flutter_for_javascript_developers | Flutter]] function that takes a single widget as an argument and inflates it to the screen <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
*   **Stateless Widget** A UI element that does not have any internal mutable data; it simply paints pixels to the screen <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. You can use the `st` snippet to quickly create one <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **`build` method** This method returns a widget and is called whenever [[introduction_to_flutter_for_javascript_developers | Flutter]] needs to rebuild the UI <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
*   **`MaterialApp`** Used as the root of the application, allowing configuration of themes and routes <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **`Scaffold`** Allows building screens with common UI elements like an app bar <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Widget Parameters** Every pre-built widget has numerous named parameters to customize its appearance <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. You can see all options by placing your cursor inside a widget and hitting `control + spacebar` <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

## Layout Widgets
*   **`Container`** A fundamental way to lay out a widget, similar to a `div` in HTML or a `View` in Android. It takes one child widget and can be customized with dimensions, margin, padding, and decorations <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   **`Center`** Centers a widget in the middle of the screen <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
*   **`Padding`** Use this widget specifically for applying padding, rather than a `Container` <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   **`SizedBox`** Use this widget when creating a container with a fixed width and height <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   **Flex Layout (`Row` and `Column`)**
    *   `Row` and `Column` widgets are used to lay out multiple children horizontally or vertically <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
    *   Unlike a `Container`, they take multiple children as a list <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
    *   The direction of flow is called the **main axis**, and the opposite is the **cross axis** <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. Spacing and alignment can be adjusted using `crossAxisAlignment` and `mainAxisAlignment` <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
    *   Children have a default flex value of one <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
    *   **`Flexible`** or **`Expanded`** widgets can wrap a child to control its space <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>. `Expanded` tells a child to take up any available space, and its flex value can be modified for more space <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.
*   **`Stack`** Used when you want one widget to overlap another <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. It takes a list of children <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
    *   **`Positioned`** Moves a widget to a specific spot within a `Stack`, similar to absolute positioning in CSS <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
    *   **`Align`** Modifies a widget's positioning relative to its parent, moving it to top, bottom, left, right, or center <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

## Common UI Elements and Interactions
*   **`FloatingActionButton`** A common UI element that magically appears at the bottom right of the screen when added to a `Scaffold` <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. It has an `onPressed` event handler for gestures <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
*   **`BottomNavigationBar`** Adds navigation icons to the `Scaffold` <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   **`Drawer`** Animates out from the left when added to the `Scaffold` <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.

### Debugging Overflow Issues
When widgets overflow their parent bounds, you'll encounter the "red screen of death" or a black and yellow error tape <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. The terminal output will link to [[introduction_to_flutter_for_javascript_developers | Flutter]]'s debugger for more information <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   **`ListView`** Things don't scroll automatically in [[introduction_to_flutter_for_javascript_developers | Flutter]]. If your parent is not a scrollable view, you need to use a widget like `ListView` <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. It takes a list of children and enables scrolling both horizontally and vertically. It can also garbage collect items not on screen <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
*   **Dynamic Lists** Many widgets can be built dynamically using `Builders`, which are functions that map a list of data to a list of widgets <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. This allows for infinitely long scrollable lists where children are rendered lazily, maintaining UI smoothness and speed <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.

## State Management
State refers to data that changes throughout the life cycle of an application <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   **Stateful Widget** A widget with mutable data. You can convert a stateless widget to a stateful one by right-clicking, going to the refactor tool, and choosing the conversion option <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. This creates two classes: an immutable widget and a mutable state class <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
    *   Variables can be defined on the state class and changed using the built-in `setState` function <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. When `setState` is called, the widget automatically re-renders to reflect the latest data <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
    *   **`initState` method** Called once when the widget is first initialized, useful for fetching data <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
    *   **`dispose` method** A lifecycle hook that runs when the widget is removed from the UI <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Advanced State Management** There are many approaches to state management in [[introduction_to_flutter_for_javascript_developers | Flutter]] <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.
    *   **Provider** A package that allows sharing real-time data throughout the widget tree without needing a stateful widget <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
    *   **Bloc and Cubit** Full-blown state management solutions <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

## Navigation (Navigator 1.0)
Navigation in [[introduction_to_flutter_for_javascript_developers | Flutter]] can be thought of like a stack where you push and pop different screens <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
*   **`Navigator.push`** To add a new screen to the top of the stack, use `Navigator.push` with the `BuildContext` <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. It takes a `MaterialPageRoute` which expects a builder function that returns the screen you want to render <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
*   **Full Restart** After implementing navigation, perform a full restart of the application by typing a capital `R` into the command line <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   **`Navigator.pop`** [[introduction_to_flutter_for_javascript_developers | Flutter]] automatically adds a back button to the app bar when navigating, which under the hood calls the `Navigator.pop` method <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

### Hero Widget for Animated Transitions
The `Hero` widget can animate elements from one screen to another <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.
1.  Wrap the image or element in a `Hero` widget <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
2.  The `Hero` widget requires an `id` to identify it when animated to another page <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
3.  [[introduction_to_flutter_for_javascript_developers | Flutter]] uses this ID to keep the image in the UI on both pages while navigation takes place <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
4.  On the target screen, also use a `Hero` widget with the same ID around the corresponding image <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
When navigating to this route, the image itself will animate between the two screens automatically <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.