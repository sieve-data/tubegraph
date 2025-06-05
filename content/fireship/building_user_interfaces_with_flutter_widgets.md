---
title: Building user interfaces with Flutter widgets
videoId: 1xipg02Wu8s
---

From: [[fireship]] <br/> 

Flutter is rapidly becoming a popular [[crossplatform_app_development_with_flutter | crossplatform framework]] due to its exceptional developer experience and ability to create high-quality applications across multiple platforms, including iOS, Android, web, and desktop <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While it offers a unique approach to UI development, it also has a steeper learning curve <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## The Core of Flutter UI: Widgets

In Flutter, the user interface is built by combining various "widgets" into a tree-like structure <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. These widgets range from low-level building blocks like `Text` to complex UI elements such as `PageView` that handle [[animation_in_flutter | animation]] and layout <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Stateless vs. Stateful Widgets
When creating UI elements, you'll primarily use two types of widgets:
*   **Stateless Widget:** Used for UI elements that do not have any internal, mutable data. They simply paint pixels to the screen based on their initial configuration <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. You can quickly generate a stateless widget snippet by typing `St` in your editor <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Stateful Widget:** Used for UI elements that have mutable data (state) that can change throughout the app's lifecycle <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a> <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. You can convert a stateless widget to a stateful one using the refactor tool <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. A stateful widget separates the widget itself (which remains immutable) from its `State` class, where mutable data can be manipulated <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. The `build` method is called whenever Flutter needs to rebuild the UI, for example, when data changes <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a> <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. The `initState` method is called once when the widget is first initialized, while `dispose` runs when the widget is removed from the UI <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

### The `main` Function and Root Widget
Every Flutter application starts executing from a `main` function <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Inside `main`, the `runApp` global function takes a single widget as its argument, which is then inflated onto the screen of the device it's running on <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### Essential Root Widgets: `MaterialApp` and `Scaffold`
*   **`MaterialApp`**: This widget serves as the root of a Flutter application and allows you to configure themes and routes <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **`Scaffold`**: Used to build screens with common UI elements, such as an app bar at the top <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. It provides many named parameters to customize its appearance <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

## Basic UI Elements and Customization

### `Container` and its Customization
The `Container` widget is a fundamental way to lay out a widget <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. It takes one child widget and positions it, by default, in the top-left corner of the screen <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. You can customize its dimensions by adding `margin` and `padding`, and also change its `height`, `width`, and `color` <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. For more advanced styling, the `decoration` property takes a `BoxDecoration` widget, allowing customization of the border, gradient, shape, and shadow <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

### Specialized Sizing Widgets
While `Container` is versatile, Flutter offers more focused widgets for specific tasks:
*   **`Center`**: Wraps a widget to center it in the middle of the screen <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **`Padding`**: If you only need to apply padding, use the `Padding` widget instead of a `Container` <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **`SizedBox`**: For creating a widget with a fixed width and height, use `SizedBox` <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

## Arranging Widgets with Layouts

### Flex Layout: `Row` and `Column`
Flutter uses Flex layout for arranging multiple related widgets.
*   **`Row`**: Lays out multiple child widgets horizontally <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **`Column`**: Lays out multiple child widgets vertically <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
Both `Row` and `Column` take a `children` property, which is a list of widgets <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. The direction they flow is called the `main axis`, and the opposite is the `cross axis` <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. You can control spacing and alignment with `crossAxisAlignment` and `mainAxisAlignment` <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

By default, children in a Flex layout have a `flex` value of one, meaning they occupy the same space <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. To change this, wrap a child in `Flexible` or `Expanded`. `Expanded` tells a child to take up any available space, and you can give it more space than other children by modifying its `flex` value <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

### Overlapping Widgets: `Stack`
When you need one widget to overlap another, such as a floating button, use a `Stack` widget <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. Like `Row` and `Column`, `Stack` takes a list of `children` as an argument. Widgets appear in the order they are listed, so a widget listed after another will appear on top <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
*   **`Positioned`**: Moves a widget to a specific spot within the stack, similar to absolute positioning in CSS <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
*   **`Align`**: Modifies a widget's positioning relative to its parent within the stack (e.g., top-left, bottom-right, center) <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

## Interactive and Pre-built UI Components
Flutter provides many UI elements out of the box that handle common interactions and layouts:
*   **`FloatingActionButton`**: Magically appears at the bottom right of the screen when added to a `Scaffold` <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. It has an `onPressed` event handler to define an anonymous function for gesture handling <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   **`BottomNavigationBar`**: Used to add navigation icons to the `Scaffold` <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   **`Drawer`**: Animates out from the left side of the screen when added to the `Scaffold` <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

## Handling Layout Issues and Scrolling

### Debugging Overflow Errors
Sometimes, widgets may overflow the bounds of their parent, leading to a "red screen of death" or a black and yellow error tape <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. The terminal output will link to Flutter's built-in debugger, providing more information to help resolve these issues <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

### Scrollable Views with `ListView`
Unlike some frameworks, Flutter views do not automatically scroll <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. To make content scrollable, you need to use a widget like `ListView` <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. `ListView` takes a list of `children` and scrolls between them, supporting both horizontal and vertical scrolling <a class="yt="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. It can also garbage collect items no longer on the screen to optimize performance <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

### Dynamic Widget Generation
Many Flutter widgets can be built dynamically using "Builders." These are functions that map a list of data to a list of widgets <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. This allows for creating infinitely long scrollable lists where children are rendered lazily, maintaining a smooth and fast UI <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

## Developer Productivity Tools
Flutter development is highly productive, largely thanks to its integrated tooling:
*   **Refactor Tool (`Control + Period`)**: Allows for quick code refactoring, such as wrapping a widget with `Center` or converting a stateless widget to stateful <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a> <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   **Autocompletion (`Control + Spacebar`)**: When typing after a period in the IDE, everything is autocompleted <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. Placing the cursor inside a widget and hitting `Control + Spacebar` brings up all available parameters and options <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
*   **Hot Reload (`lowercase 'r' in terminal`)**: Instantly shows UI changes without rebuilding the entire app <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   **Full Restart (`capital 'R' in terminal`)**: Reruns the application from scratch <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
*   **Trailing Commas**: While not required, adding a trailing comma after every block of code helps keep the code nicely formatted into multiple lines when the document is formatted <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Excellent Documentation**: Flutter's documentation is comprehensive and often includes links to videos for further explanation <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

For more advanced topics such as [[managing_state_in_flutter_applications | state management]] with packages like Provider, Block, or Cubit, or [[navigating_between_screens_in_flutter_apps | navigating between screens]] using features like the Hero widget for [[animation_in_flutter | animating]] elements between pages, additional resources are available <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a> <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a> <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.