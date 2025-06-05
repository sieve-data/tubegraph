---
title: HTML structure and syntax
videoId: erEgovG9WBs
---

From: [[fireship]] <br/> 

Hypertext Markup Language (HTML) is the language used to represent the actual content seen on a webpage <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>. On its own, HTML typically produces a plain black and white website <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>. Most web browsers include DevTools that allow users to inspect the structure of HTML at any time <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>.

## HTML Documents and Elements

To create your own webpage, a text editor like VS Code is recommended <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>. An HTML document is a collection of elements <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>.

### Tags and Content
An HTML element consists of an opening tag, a closing tag, and some content in the middle <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>. Examples include:
*   Paragraphs (`<p>`) <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>
*   Headings (`<h1>` to `<h6>`) <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>
*   Elements for user input, such as `<select>` and `<input>` elements, which are used to build forms <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a>.

### Attributes
Elements can have one or more attributes that modify their behavior <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>. For instance, an `<input>` element can have a `type` attribute (e.g., `text` or `number`), which causes the browser to render it differently to collect the appropriate value <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.

### The Anchor Tag (Hypertext)
The `<a>` tag, or anchor tag, is the element that provides the "hypertext" functionality in HTML <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>. It functions as a link, enabling one page to navigate to another based on its Uniform Resource Locator (URL) <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.

## Document Object Model (DOM)

HTML elements are nested together in a hierarchy to form the Document Object Model (DOM) <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>.

### Head and Body
From the root element, a webpage is typically divided into two main parts:
*   **Head**: Contains invisible content such as metadata and the page's title <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>.
*   **Body**: Contains the main content that the end-user actually sees <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>.

### Semantic Meaning
The practice of wrapping content in tags provides browsers and bots with hints about the semantic meaning of the webpage <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>. This is crucial for:
*   Search engines to display results properly <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.
*   Accessibility, as it aids devices like screen readers, ensuring content can be enjoyed by individuals regardless of disability <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>.

## Common Elements
One of the most frequently used elements is the `<div>` (division) tag, which defines a section of a webpage <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>. On its own, a `div` may not appear to do anything <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>. To style HTML elements, [[css_for_styling_and_layout | CSS]] is required <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>.