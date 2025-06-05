---
title: HTML and the Document Object Model DOM
videoId: erEgovG9WBs
---

From: [[fireship]] <br/> 

[[Introduction to Web Development | Web development]] involves building on a platform used by nearly 5 billion daily active users globally <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. To build full-stack web applications, a foundational understanding of many concepts is required <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## The World Wide Web

The internet is a network of billions of connected machines, established on January 1st, 1983, with the standardization of the Internet Protocol Suite <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. While the internet can be thought of as hardware, the World Wide Web is like software that sits on top of it, allowing access to web pages via the Hypertext Transfer Protocol (HTTP) <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. Every web page has a unique Uniform Resource Locator (URL) <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

Web browsers act as "clients" to access these URLs and render content visually <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. On the other end, "servers" receive HTTP requests from clients and send back responses containing web page content <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## Hypertext Markup Language (HTML)

When you view a web page, the content you see is represented by Hypertext Markup Language (HTML) <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Most browsers include Dev Tools that allow users to inspect the structure of the HTML at any time <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. To create your own web page, a text editor like VS Code is commonly used <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

### HTML Elements and Attributes

An HTML document is a collection of elements <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. An element consists of an opening and closing tag with content in the middle, such as a paragraph (`<p>`) or a heading (`<h1>`) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. HTML also includes elements for user input, like `<select>` and `<input>` elements, which are used to build forms <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

Elements can have one or more **attributes** to modify their behavior <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. For instance, an `<input>` element can have a `type` attribute (e.g., `text` or `number`), which the browser renders differently to collect the appropriate value <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

The `<a>` tag, or **anchor**, is crucial as it creates links, enabling one page to navigate to another based on its URL <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

A common element is `<div>`, or division, used to define a section of a web page <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. On its own, a `div` might not appear to do anything, resulting in a plain black and white website <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. This highlights the need for [[CSS for Styling and Layout | CSS]] to style and enhance the appearance of HTML elements <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

### Document Object Model (DOM)

HTML elements are nested hierarchically to form the **Document Object Model (DOM)** <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. From its root element, a web page is typically divided into two main parts:
*   **Head**: Contains invisible content like metadata and the page title <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   **Body**: Holds the main content that the end-user actually sees <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

The use of tags in HTML provides browsers and bots with hints about the semantic meaning of the web page <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. This semantic structure is vital for:
*   **Search Engines**: Allows search engines to display results correctly <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   **Accessibility**: Helps devices like screen readers interpret content, making it accessible to individuals regardless of disability <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

### Interaction with JavaScript

While technically not required to build a website, most developers use [[JavaScript fundamentals and practical concepts | JavaScript]] to make the user interface more interactive <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

[[Using JavaScript on web and server environments | JavaScript]] code can be embedded directly within `<script>` tags in an HTML document <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. The browser interprets the HTML from top to bottom, executing the [[JavaScript fundamentals and practical concepts | JavaScript]] code when it encounters it in the DOM <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. More commonly, [[JavaScript fundamentals and practical concepts | JavaScript]] is written in a separate file and linked to the HTML via the `src` attribute on the `<script>` tag <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. The `defer` attribute is often used to ensure the [[JavaScript fundamentals and practical concepts | JavaScript]] code runs only after the DOM content has fully loaded <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

[[JavaScript fundamentals and practical concepts | JavaScript]] primarily interacts with HTML by handling events (like clicks or form inputs) emitted by the browser <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. Browser APIs, such as `document.querySelector`, allow [[JavaScript fundamentals and practical concepts | JavaScript]] to select and manipulate HTML elements based on [[CSS for Styling and Layout | CSS]] selectors <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. An event listener, a function assigned to an element, will execute whenever the specified event occurs on that element <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

Front-end frameworks like React, Vue, Svelte, and Angular simplify [[JavaScript fundamentals and practical concepts | JavaScript]]'s interaction with the DOM <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. These frameworks represent the UI as a tree of components, where a component can encapsulate HTML, [[CSS for Styling and Layout | CSS]], and [[JavaScript fundamentals and practical concepts | JavaScript]] into a format that resembles its own [[using_web_components_in_modern_web_development | custom HTML element]] <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. This approach leads to more declarative code, which is easier to manage than the imperative code typically written with plain [[JavaScript fundamentals and practical concepts | JavaScript]] <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.