---
title: CSS Variables and State Management
videoId: Qhaz36TZG5Y
---

From: [[fireship]] <br/> 

## CSS Variables (Custom Properties)

[[CSS_for_styling_and_layout|CSS]] custom properties, also known as variables, offer a powerful way to make code more flexible and manageable, significantly simplifying refactoring efforts <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. Traditionally, if the same color value is used in multiple places, changing it would require modifying every single line that references it <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

A more effective approach is to define a global variable on the root selector <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. This variable can then be referenced wherever that value is needed <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. With this method, changing the value only requires modifying one line of code <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

### Variable Cascading and Composition

Like other [[CSS_for_styling_and_layout|CSS]] properties, variables cascade, meaning they can be overridden by redefining them deeper within the document tree <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. This allows for localized modifications to global values.

Variables can also be combined to compose more complex values <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>. For example, an RGB color can be defined based on the values of three other variables <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. This flexibility is particularly useful for quickly swapping out different themes for a website <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

### Integration with `calc()` for Dynamic Values

[[CSS_for_styling_and_layout|CSS]], while not a traditional programming language, can perform basic calculations using the `calc()` function <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. A key feature of `calc()` is its ability to combine different units, such as subtracting pixels from a viewport width <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

This functionality, combined with variables, enables sophisticated dynamic effects. For instance, to stagger animation delays for a series of elements, an inline [[CSS_for_styling_and_layout|CSS]] variable can define each item's order <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. The `animation-delay` can then be calculated as the order variable multiplied by a specific time unit (e.g., 100 milliseconds) <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. This approach allows handling an infinite number of elements without increasing the [[CSS_for_styling_and_layout|CSS]] footprint <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

## CSS State Management Mechanisms

[[CSS_for_styling_and_layout|CSS]] possesses built-in state management capabilities, allowing for tracking a running count or managing UI states without requiring [[JavaScript for interactivity and frameworks|JavaScript]] <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a> <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

### CSS Counters

For numbering headings in HTML, a naive approach involves manually adding numbers in the HTML <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. However, this becomes problematic if new headings are inserted, as it necessitates renumbering everything manually <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

A more intelligent solution is to use a [[CSS_Tools_and_Preprocessors#CSS Counters|CSS counter]] <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. A counter can be created using the `counter-reset` property, assigning it any desired name <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. It can then be incremented whenever a specific selector is applied (e.g., starting from 0 and adding 1 to every `h1` element in the DOM) <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. This eliminates the need for manual numbering in the HTML <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

### `focus-within` Pseudo-class for UI State

When building complex UI components like drop-down menus, it's often assumed that [[JavaScript for interactivity and frameworks|JavaScript]] is required to manage their open and closed [[State and props in React|state]] <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. However, much can be achieved with pure [[CSS_for_styling_and_layout|CSS]] <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

The `focus` pseudo-class is applied to an element when it's focused, such as a form input or button <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. A common issue with using `focus` for dropdowns is that clicking an item *inside* the menu causes the menu to lose focus and close, typically prompting developers to resort to [[JavaScript for interactivity and frameworks|JavaScript]] for [[State and props in React|state]] management <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.

In contrast, the `focus-within` pseudo-class remains active if *any* of its children also have focus <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. This single feature can significantly reduce the amount of [[JavaScript for interactivity and frameworks|JavaScript]] needed to toggle UI states <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.