---
title: Navigating between screens in Flutter apps
videoId: 1xipg02Wu8s
---

From: [[fireship]] <br/> 

Navigating between different screens in a Flutter application can be thought of as managing a stack of pages <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. When a new screen is opened, it's pushed onto the stack; when you go back, it's popped off. For basic navigation, Flutter's Navigator 1.0 is commonly used <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

## Basic Screen Navigation

To add a new screen to the top of the navigation stack, you use `Navigator.push()` <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. This method requires a `BuildContext` and typically takes a `MaterialPageRoute` as its argument <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.

The `MaterialPageRoute` expects a builder function that returns the specific screen (a [[building_user_interfaces_with_flutter_widgets | widget]]) you want to render <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.

```dart
// Example of pushing a new screen
Navigator.push(
  context,
  MaterialPageRoute(builder: (context) => PageTwo()),
);
```
<a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>

Flutter automatically adds a back button to the `AppBar` of the new screen. This back button, when pressed, internally calls the `Navigator.pop()` method, removing the current screen from the stack <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

> To see navigation changes, you'll need to perform a full restart of the application by typing a capital `R` into the command line <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.

## Animated Transitions with Hero Widgets

Flutter offers a `Hero` [[animation_in_flutter | widget]] that provides a "magical" way to animate elements from one screen to another during navigation <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

To implement a Hero animation:
1.  Wrap the element you want to animate on both the source and destination screens with a `Hero` [[building_user_interfaces_with_flutter_widgets | widget]] <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
2.  Assign a unique `tag` (ID) to the `Hero` [[building_user_interfaces_with_flutter_widgets | widget]] on both pages. This `tag` is crucial for Flutter to identify and link the same element across different screens during the animation <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

Flutter uses this `ID` to keep the image in the UI on both pages while the navigation is taking place, resulting in a smooth, automatic animation of the element between the two screens <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>. This feature is particularly impactful when navigating through lists of images <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.