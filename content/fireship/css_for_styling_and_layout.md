---
title: CSS for styling and layout
videoId: erEgovG9WBs
---

From: [[fireship]] <br/> 

Cascading Stylesheets (CSS) is the second language a web developer learns, and it enables the modification of [[HTML structure and syntax | HTML]] element appearances <a class="yt-timestamp" data-t="03:53:07">[03:53:07]</a>.

## Applying CSS
CSS can be applied in various ways:
*   **Inline Style** Directly on an element using the `style` attribute. This approach applies styles only to that specific element and contains properties and values that dictate its appearance <a class="yt-timestamp" data-t="03:57:48">[03:57:48]</a>. For example, setting background and text color <a class="yt-timestamp" data-t="04:07:22">[04:07:22]</a>.
*   **Style Tag** CSS code can be placed within a `<style>` tag in the [[HTML structure and syntax | HTML]] document. This requires defining a selector to target specific elements <a class="yt-timestamp" data-t="04:20:53">[04:20:53]</a>.
*   **External Stylesheet** Most commonly, CSS is written in a separate external stylesheet file and linked to the web page within the `<head>` of the [[HTML structure and syntax | document]] <a class="yt-timestamp" data-t="04:52:03">[04:52:03]</a>.

### Selectors and Specificity
To apply styles to specific elements, CSS uses selectors <a class="yt-timestamp" data-t="04:25:39">[04:25:39]</a>:
*   **Element Selectors** Can target all instances of an [[HTML structure and syntax | element]] on a page, such as all paragraph elements <a class="yt-timestamp" data-t="04:28:44">[04:28:44]</a>.
*   **Class Selectors** Offer more granularity by defining a class that can be applied to one or more elements using the `class` attribute <a class="yt-timestamp" data-t="04:33:02">[04:33:02]</a>.

When multiple classes apply different styles to the same element, CSS employs "specificity rules" to determine which styles are relevant <a class="yt-timestamp" data-t="04:44:09">[04:44:09]</a>. CSS also "cascades," meaning it can be applied to multiple elements, enhancing code reusability <a class="yt-timestamp" data-t="04:14:01">[04:14:01]</a>.

## Layout and Positioning
The most challenging aspect of CSS is learning layout and positioning <a class="yt-timestamp" data-t="04:59:04">[04:59:04]</a>.

### [[Understanding the CSS Box Model | CSS Box Model]]
Every [[HTML structure and syntax | element]] is conceptualized as a box. This box is surrounded by padding, border, and margin, which affect how it occupies space on the page <a class="yt-timestamp" data-t="05:04:47">[05:04:47]</a>. Elements typically take up space from top to bottom <a class="yt-timestamp" data-t="05:08:53">[05:08:53]</a>.

### Display Properties
*   **`display: block`** Elements like headings take up all available horizontal space by default <a class="yt-timestamp" data-t="05:10:48">[05:10:48]</a>.
*   **`display: inline`** Elements like images line up horizontally side-by-side <a class="yt-timestamp" data-t="05:17:34">[05:17:34]</a>.

### Position Property
The default positioning of elements is often undesirable and can be altered using the `position` property <a class="yt-timestamp" data-t="05:25:30">[05:25:30]</a>:
*   **`relative`** Allows an element to move a certain number of pixels from its original position <a class="yt-timestamp" data-t="05:28:38">[05:28:38]</a>.
*   **`absolute`** Similar to relative, but position values are relative to its nearest ancestor <a class="yt-timestamp" data-t="05:35:46">[05:35:46]</a>.
*   **`fixed`** Keeps an element on the screen even when the user scrolls, as it is fixed to the entire viewport <a class="yt-timestamp" data-t="05:39:41">[05:39:41]</a>.

## Responsive Layouts
A significant challenge for web developers is creating [[Responsive Design with Media Queries and CSS Functions | responsive layouts]] that look good across diverse screen sizes <a class="yt-timestamp" data-t="05:49:03">[05:49:03]</a>. CSS provides several [[CSS Tools and Preprocessors | tools]] to achieve this:
*   [[Responsive Design with Media Queries and CSS Functions | **Media Queries**]] Allow developers to gather information about the device rendering the web page and apply different styles accordingly <a class="yt-timestamp" data-t="06:01:03">[06:01:03]</a>.
*   [[Using Flexbox and CSS Grid for Layout | **Flexbox**]] By applying `display: flex` to a parent element, it can control the flow of its children, making it easy to create rows and columns <a class="yt-timestamp" data-t="06:11:03">[06:11:03]</a>.
*   [[Using Flexbox and CSS Grid for Layout | **CSS Grid**]] Used for more complex layouts, `display: grid` enables control over multiple rows and columns simultaneously <a class="yt-timestamp" data-t="06:17:31">[06:17:31]</a>.

## Advanced CSS Features and Tools
While not a Turing-complete language, CSS offers mechanisms like:
*   **`calc()`** To perform mathematical operations <a class="yt-timestamp" data-t="06:27:03">[06:27:03]</a>.
*   [[CSS Variables and State Management | **Custom Properties**]] Function as variables that can be reused in multiple places <a class="yt-timestamp" data-t="06:31:54">[06:31:54]</a>.

Many developers extend vanilla CSS with [[CSS Tools and Preprocessors | tools]] like SAS to add programmatic features <a class="yt-timestamp" data-t="06:38:00">[06:38:00]</a>.