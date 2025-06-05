---
title: JavaScript for interactivity and frameworks
videoId: erEgovG9WBs
---

From: [[fireship]] <br/> 

While it's technically possible to build a website without [[javascript_basics_and_history | JavaScript]], most developers choose to use it to make the user interface more interactive <a class="yt-timestamp" data-t="06:48:07">[06:48:07]</a>.

## Integrating [[javascript_basics_and_history | JavaScript]] into Web Pages

To run [[javascript_basics_and_history | JavaScript]] code on a web page, you can open a `<script>` tag and write the code inside it <a class="yt-timestamp" data-t="06:53:49">[06:53:49]</a>. The browser interprets the HTML from top to bottom and executes the [[javascript_basics_and_history | JavaScript]] code when it encounters it in the DOM (Document Object Model) <a class="yt-timestamp" data-t="06:59:16">[06:59:16]</a>.

In most cases, [[javascript_basics_and_history | JavaScript]] is written in a separate file and referenced as the `src` on the `<script>` tag <a class="yt-timestamp" data-t="07:04:08">[07:04:08]</a>. It's often preferred for this code to run after the DOM content has loaded, which can be achieved with the `defer` attribute <a class="yt-timestamp" data-t="07:09:47">[07:09:47]</a>.

## Core Concepts of [[javascript_basics_and_history | JavaScript]]

[[javascript_basics_and_history | JavaScript]] is formally known as ECMAScript and is standardized across all major browsers <a class="yt-timestamp" data-t="07:14:48">[07:14:48]</a>.

### Variables and Typing
Variables in [[javascript_basics_and_history | JavaScript]] can be declared using:
*   `let` for variables that might be reassigned <a class="yt-timestamp" data-t="07:23:25">[07:23:25]</a>.
*   `const` for variables that cannot be reassigned <a class="yt-timestamp" data-t="07:26:27">[07:26:27]</a>.

It is a dynamically typed language, meaning explicit type annotations are not necessary <a class="yt-timestamp" data-t="07:29:43">[07:29:43]</a>. However, many developers choose TypeScript as an alternative to add static typing on top of [[javascript_basics_and_history | JavaScript]] <a class="yt-timestamp" data-t="07:33:57">[07:33:57]</a>.

### Event Handling
One of the primary reasons to use [[javascript_basics_and_history | JavaScript]] is to handle events <a class="yt-timestamp" data-t="07:39:46">[07:39:46]</a>. When a user interacts with a web page (e.g., clicks, mouse moves, form input), the browser emits an event <a class="yt-timestamp" data-t="07:43:08">[07:43:08]</a>. These events can be listened to using browser APIs like `document`, which provides methods such as `querySelector` to target specific elements with a CSS selector <a class="yt-timestamp" data-t="07:51:24">[07:51:24]</a>. An event listener, which is a function, can then be assigned to an element to be called or re-executed when the event occurs <a class="yt-timestamp" data-t="08:01:05">[08:01:05]</a>.

### Data Structures and Inheritance
[[javascript_basics_and_history | JavaScript]] includes built-in data structures like arrays for collections of values <a class="yt-timestamp" data-t="08:11:03">[08:11:03]</a>. The most fundamental data structure is the object, also known as a dictionary or hashmap <a class="yt-timestamp" data-t="08:16:03">[08:16:03]</a>.

[[javascript_basics_and_history | JavaScript]] relies on prototypal inheritance, where an object can be cloned to create a chain of ancestors, allowing children to inherit properties and methods <a class="yt-timestamp" data-t="08:27:07">[08:27:07]</a>. While [[javascript_basics_and_history | JavaScript]] supports classes, they are syntactic sugar for prototypal inheritance <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>.

## [[frontend_ui_libraries_and_frameworks | Frontend Frameworks]]

Many developers avoid directly manipulating the `prototype` and instead use [[frontend_ui_libraries_and_frameworks | front-end frameworks]] <a class="yt-timestamp" data-t="08:49:09">[08:49:09]</a>. Popular examples include:
*   [[overview_of_lesser_known_javascript_frameworks_like_svelte_lit_and_mithril | React]]
*   [[overview_of_lesser_known_javascript_frameworks_like_svelte_lit_and_mithril | Vue]]
*   [[overview_of_lesser_known_javascript_frameworks_like_svelte_lit_and_mithril | Svelte]]
*   [[overview_of_lesser_known_javascript_frameworks_like_svelte_lit_and_mithril | Angular]] <a class="yt-timestamp" data-t="08:54:02">[08:54:02]</a>

These frameworks primarily represent the UI as a tree of components <a class="yt-timestamp" data-t="08:56:01">[08:56:01]</a>. A component can encapsulate HTML, CSS, and [[javascript_basics_and_history | JavaScript]] into a format that resembles its own custom HTML element <a class="yt-timestamp" data-t="09:01:04">[09:01:04]</a>.

### Declarative vs. Imperative Code
[[comparison_of_javascript_frameworks | Frameworks]] produce declarative code, which describes exactly what the UI does, making it easier to work with than the imperative code typically found with plain [[building_applications_with_vanilla_javascript | vanilla JavaScript]] <a class="yt-timestamp" data-t="09:09:02">[09:09:02]</a>.

### Node.js for Backend [[javascript_basics_and_history | JavaScript]]
[[javascript_basics_and_history | JavaScript]] is also used on the backend with Node.js, a server-side runtime <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>. Node.js is popular because it uses the same language as the browser and is based on the V8 engine (which powers the Chromium browser) <a class="yt-timestamp" data-t="09:31:00">[09:31:00]</a>. This allows it to run code in a single-threaded, non-blocking event loop, handling many simultaneous connections efficiently <a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a>.