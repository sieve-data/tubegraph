---
title: CSS for Styling and Layout
videoId: erEgovG9WBs
---

From: [[fireship]] <br/> 

The second language a web developer needs to learn is [[CSS and HTML tips for responsive design | Cascading Stylesheets (CSS)]] <a class="yt-timestamp" data-t="03:50:52">[03:50:52]</a>. CSS allows you to change the appearance of HTML elements <a class="yt-timestamp" data-t="03:53:07">[03:53:07]</a>.

## Applying CSS

There are several ways to apply CSS:
*   **Inline Style** An inline style uses the `style` attribute directly on an HTML element <a class="yt-timestamp" data-t="03:57:40">[03:57:40]</a>. The style contains a collection of properties and values that change the element's appearance <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>. This method applies the style only to that specific element <a class="yt-timestamp" data-t="04:12:00">[04:12:00]</a>.
*   **Style Tag** CSS can be placed inside a `<style>` tag within the HTML document <a class="yt-timestamp" data-t="04:21:49">[04:21:49]</a>. To apply styles, a selector is defined to target specific elements <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>.
*   **External Stylesheet** Most often, CSS code is placed in an external stylesheet, which is then linked to the web page in the `<head>` of the document <a class="yt-timestamp" data-t="04:54:57">[04:54:57]</a>.

### CSS Cascading and Specificity

CSS "cascades," meaning it can be applied to multiple elements simultaneously, improving code reusability <a class="yt-timestamp" data-t="04:14:48">[04:14:48]</a>.
A selector can target all paragraph elements on a page <a class="yt-timestamp" data-t="04:28:00">[04:28:00]</a>. For more granular control, a class can be defined and applied to one or more elements using the `class` attribute <a class="yt-timestamp" data-t="04:34:06">[04:34:06]</a>. CSS contains specificity rules that determine which styles are most relevant when multiple styles apply to the same element <a class="yt-timestamp" data-t="04:45:11">[04:45:11]</a>.

## Layout and Positioning

One of the most challenging aspects of CSS is learning layout and positioning <a class="yt-timestamp" data-t="05:00:24">[05:00:24]</a>.

### The Box Model

Think of every HTML element as a box <a class="yt-timestamp" data-t="05:03:04">[05:03:04]</a>. The outside of this box is wrapped with:
*   **Padding**: Space between the content and the border <a class="yt-timestamp" data-t="05:06:00">[05:06:00]</a>.
*   **Border**: A line around the padding <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>.
*   **Margin**: Space outside the border, separating the element from others <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a>.

Elements take up space on the page from top to bottom <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>.

### Display Property

The `display` property dictates how an element behaves in terms of layout:
*   **`display: block`**: Elements like headings have a default display of `block`, meaning they take up all available horizontal space <a class="yt-timestamp" data-t="05:11:43">[05:11:43]</a>.
*   **`display: inline`**: Elements like images are displayed `inline`, allowing them to line up horizontally side-by-side <a class="yt-timestamp" data-t="05:18:14">[05:18:14]</a>.

### Position Property

The default position of elements is often not desirable, but it can be changed by customizing the `position` property <a class="yt-timestamp" data-t="05:27:03">[05:27:03]</a>:
*   **`position: relative`**: Allows an element to move a certain number of pixels from its normal position <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.
*   **`position: absolute`**: Similar to relative, but the position values are relative to its nearest positioned ancestor <a class="yt-timestamp" data-t="05:35:00">[05:35:00]</a>.
*   **`position: fixed`**: Keeps an element on the screen even as the user scrolls, as it's fixed to the entire viewport <a class="yt-timestamp" data-t="05:39:00">[05:39:00]</a>.

### [[responsive_layouts_using_css_grid_and_media_queries | Responsive Layouts]]

A significant challenge for web developers is creating [[responsive_layouts_using_css_grid_and_media_queries | responsive layouts]] that look good on all screen sizes <a class="yt-timestamp" data-t="05:51:24">[05:51:24]</a>. CSS offers several tools to achieve this:
*   **[[responsive_layouts_using_css_grid_and_media_queries | Media Queries]]**: These allow you to get information about the device rendering the web page and apply different styles accordingly <a class="yt-timestamp" data-t="06:01:05">[06:01:05]</a>.
*   **Flexbox (`display: flex`)**: Applying `display: flex` to a parent element enables it to control the flow of its children, making it easy to create rows and columns <a class="yt-timestamp" data-t="06:11:21">[06:11:21]</a>.
*   **[[basics_of_css_grid | CSS Grid]] (`display: grid`)**: For more complex layouts, `display: grid` can be used to control multiple rows and columns simultaneously <a class="yt-timestamp" data-t="06:18:00">[06:18:00]</a>.

## Advanced CSS Features

While CSS is not considered a Turing-complete programming language, it does have mechanisms for advanced functionality:
*   **`calc()`**: Performs mathematical operations within CSS <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>.
*   **Custom Properties (Variables)**: Allows you to define variables that can be reused in multiple places throughout your stylesheet <a class="yt-timestamp" data-t="06:32:00">[06:32:00]</a>.
*   **CSS Preprocessors**: Tools like SASS extend vanilla CSS by adding programmatic features on top of it, such as variables, nesting, and mixins <a class="yt-timestamp" data-t="06:39:00">[06:39:00]</a>.