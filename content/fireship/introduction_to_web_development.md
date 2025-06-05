---
title: Introduction to Web Development
videoId: erEgovG9WBs
---

From: [[fireship]] <br/> 

[[Web development with Ruby on Rails | Web development]] is considered by some to be the best job in the world, building on a platform with nearly 5 billion daily active users <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These users are connected like the neurons of a global, super-intelligent brain <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>, a system capable of curing disease, eliminating poverty, and advancing science, though it's mostly used for sharing memes, creating parasocial relationships, amplifying drama, and making money <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. To get into web development, you'll need to understand many concepts <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## The Internet and The Web

It's important to distinguish between the Internet and the World Wide Web <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### The Internet

The Internet is a network of billions of connected machines <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. It was officially born on January 1, 1983, with the establishment of the Internet Protocol Suite, which standardized how computers communicate <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

Key components of the Internet include:
*   **Internet Protocol (IP)**: Used to identify different computers on the network by assigning each a unique IP address <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   **Transmission Control Protocol (TCP)**: Used to send data back and forth between computers, breaking data into small packets like puzzle pieces, sending them through physical components like fiber optic cables and modems, and then reassembling them at the receiving computer <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
The Internet can be thought of as the hardware foundation <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### The World Wide Web

The World Wide Web is like software that sits on top of the Internet, allowing people to access web pages <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

Key components of the Web include:
*   **Hypertext Transfer Protocol (HTTP)**: Used to access web pages <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. It assigns every page of content a unique Uniform Resource Locator (URL) <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Web Browser**: A tool humans use to access a URL, which then renders the content visually on their screen <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. The browser acts as the *client*, consuming information <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   **Server**: Another computer on the other end of a URL that receives an HTTP request from the client and sends a response containing the webpage content (HTTP messages) <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   **Domain Name**: A unique name for a web page, like `fireship.io` or `example.com` <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. Domain names can be registered via a registrar accredited by ICANN, a non-profit overseeing Internet namespaces <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   **Domain Name System (DNS)**: When you navigate to a domain in a browser, it's routed through DNS, which maps these names to an actual IP address on a server <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. DNS is often called the "phone book of the internet" <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## Core Web Languages

The content you see on a web page is primarily built using three core languages: HTML, CSS, and JavaScript.

### HTML (HyperText Markup Language)

HTML represents the actual content you see on a web page <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Most browsers offer [[Web development tools and browser recommendations | Dev tools]] to inspect the HTML structure <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. To build a web page, you'll typically use a text editor like VS Code <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

*   An HTML document is a collection of **elements** <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. An element consists of an opening and closing tag with content in the middle, such as `<p>` for a paragraph or `<h1>` for a heading <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   Elements like `<select>` and `<input>` handle user input and are used to build forms <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
*   Elements can have **attributes** to change their behavior (e.g., `<input type="text">` or `<input type="number">`) <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   The `<a>` (anchor) tag creates a link, allowing navigation to a different page based on its URL, thus adding "hypertext" to HTML <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   Elements are nested hierarchically to form the **Document Object Model (DOM)** <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   A web page is split into two main parts from its root element:
    *   The `<head>`: Contains invisible content like metadata and a title <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
    *   The `<body>`: Contains the main content visible to the end user <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
*   Wrapping content in tags provides semantic meaning to browsers and bots, helping search engines display results properly and aiding accessibility for devices like screen readers <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
*   The `<div>` (division) element is commonly used to define a section of a web page <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. On its own, a `div` might not appear to do anything, resulting in a plain black and white website <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### CSS (Cascading Style Sheets)

CSS allows you to change the appearance of HTML elements <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

*   **Inline Styles**: Styles can be applied directly to an element using the `style` attribute <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. These styles contain properties and values that change the element's appearance, like `background-color` or `color` <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. Inline styles apply only to that specific element <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
*   **Cascading**: CSS can be applied to multiple elements simultaneously, promoting code reusability <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   **Style Tags**: CSS can be placed within `<style>` tags in the HTML document <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
    *   **Selectors**: Define which elements to target (e.g., targeting all paragraph elements) <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
    *   **Classes**: Provide more granular control, allowing a style to be applied to one or more elements using the `class` attribute <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
    *   **Specificity Rules**: CSS has rules that determine which styles are relevant when multiple styles apply to the same element <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   **External Stylesheets**: Most commonly, CSS is kept in separate files and linked to the web page in the HTML document's `<head>` <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

### Layout and Positioning

The most challenging aspect of CSS is learning layout and positioning <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

*   **Box Model**: Every element is treated like a box, wrapped with padding, border, and margin <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   **Display Property**:
    *   `display: block`: Elements like headings take up all available horizontal space by default <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
    *   `display: inline`: Elements like images line up horizontally side-by-side <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
*   **Position Property**:
    *   `position: relative`: Allows an element to move a certain number of pixels from its normal position <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
    *   `position: absolute`: Position values are relative to the element's nearest ancestor <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
    *   `position: fixed`: Keeps an element on the screen even when the user scrolls, as it's fixed to the entire viewport <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

#### Responsive Layouts

A major challenge is creating responsive layouts that look good on various screen sizes <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
*   **Media Queries**: Allow you to get information about the device rendering the page and apply different styles accordingly <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Layout Tools**:
    *   `display: flex` (Flexbox): Applied to a parent element, it controls the flow of children to easily create rows and columns <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
    *   `display: grid`: Used for more complex layouts, controlling multiple rows and columns simultaneously <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

CSS also includes mechanisms like `calc()` for mathematical operations <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a> and **custom properties** (like variables) that can be reused <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>. Many developers extend vanilla CSS with tools like SAS for additional programmatic features <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

### JavaScript

JavaScript is the third essential language for web developers <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. While not strictly required to build a website, most developers use it to make the user interface more interactive <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

*   JavaScript code can be run on a web page by opening a `<script>` tag and writing code inside <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. The browser interprets HTML from top to bottom and runs the code when encountered <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
*   In most cases, JavaScript is written in a separate file and referenced using the `src` attribute on the `<script>` tag <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. It's often preferred for this code to run after the DOM content has loaded, achieved with the `defer` attribute <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   JavaScript is formally known as ECMAScript and is standardized across all major browsers <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
*   **Variables**: Can be declared using `let` (for reassignment) or `const` (for no reassignment) <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   **Dynamic Typing**: JavaScript is dynamically typed, meaning type annotations are not necessary <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. Many developers choose TypeScript as an alternative to add static typing on top of JavaScript <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   **Event Handling**: A common use for JavaScript is to handle events <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. When a user interacts with a web page (e.g., click, mouse move, form input), the browser emits an event <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. Developers can tap into these events using browser APIs like `document.querySelector` to grab an element and then assign an **event listener**, which is a function called anytime the event occurs <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.
*   **Data Structures**: JavaScript has built-in data structures like arrays (collections of values) <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. The most fundamental is the **object**, also called a dictionary or hashmap <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. Anything not a primitive type (string, number) inherits functionality from the `Object` class <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Prototypal Inheritance**: JavaScript relies on this technique, where an object can be cloned to create a chain of ancestors, with the child inheriting properties and methods from its ancestors <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. While JavaScript supports classes, they are syntactic sugar for prototypal inheritance <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.

#### Front-End Frameworks

To abstract away low-level details like prototypal inheritance, many developers use front-end frameworks like React, Vue, Svelte, or Angular <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. These frameworks represent the UI as a tree of **components** <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. A component encapsulates HTML, CSS, and JavaScript into a format that resembles its own custom HTML element <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. They produce **declarative code** that describes what the UI does, which is easier to work with than imperative code from vanilla JavaScript <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

## Back-End Concepts

After understanding the front-end (what the user sees), it's necessary to learn about the back-end (what happens on the server).

### [[Introduction to Nodejs | Node.js]]

[[Introduction to Nodejs | Node.js]] is a server-side runtime based on JavaScript <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. While server-side code can run in many languages, [[Introduction to Nodejs | Node.js]] is popular because it uses the same language as the browser <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. It's based on the V8 engine (which powers the Chromium browser) and runs code in a single-threaded, non-blocking event loop, allowing it to handle many simultaneous connections efficiently <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

*   **Node Package Manager (NPM)**: Allows developers to share work remotely <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. A **package** (or **module**) is a file containing code with an `export` statement so it can be used in another file via an `import` statement <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

### Website Delivery Models

The method of delivering the website from the server to the client varies:

1.  **Server-Side Rendering (SSR)**:
    *   The client makes a GET request for a URL <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. HTTP methods like GET retrieve data, while POST and PATCH modify data <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
    *   The server receives the request, generates all the HTML on the server, and sends it back as a response <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
    *   Responses include status codes (e.g., 200 for success, 400/500 levels for errors) <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. A common example is a 404 status code if the page doesn't exist <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
    *   SSR is very popular but may not always be fast enough <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.

2.  **Single Page Application (SPA)**:
    *   The server only renders a minimal shell for the root URL <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
    *   JavaScript handles the rendering for all other pages on the website <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
    *   HTML is generated almost entirely client-side in the browser, making the website feel like a native iOS or Android app <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.
    *   When the app needs more data, it makes an HTTP request but only for a minimal amount of data as JSON (a data interchange format understood by any programming language) <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
    *   While providing a great user experience, SPAs can be difficult for bots (like search engines and social media link previews) to understand content <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

3.  **Static Site Generation (SSG)**:
    *   Every web page is uploaded to a server in advance, allowing bots to get the necessary information easily <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
    *   A front-end JavaScript framework typically "hydrates" the HTML to make it fully interactive and behave like a single page application <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.

### Performance

Performance is crucial. Tools like Lighthouse help optimize metrics such as First Contentful Paint and Time to Interactive <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

### Full Stack Frameworks and Tools

To implement these patterns, developers often use full stack frameworks like Next.js, [[Web development with Ruby on Rails | Ruby on Rails]], or Laravel <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. These abstract away tedious tasks, including:

*   **Module Bundlers**: Tools like Webpack that package JavaScript, CSS, and HTML to work in a browser <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.
*   **Linters**: Like ESLint, they warn when code doesn't follow proper style guidelines <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
*   **Databases**: Essential for storing data, such as user information, in a full stack web application <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.
*   **User Authentication**: The process of allowing users to log in <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

### Deployment

Before deploying code, you'll need to test it with a web server <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.
*   Tools like Nginx and Apache can create an HTTP server <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.
*   Your framework will likely serve files on `localhost`, making your own IP address behave like a remote web server <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
*   For deployment, large cloud providers like [[Introduction to Amazon Web Services AWS | AWS]] are commonly used <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.
*   Most applications are containerized with Docker, making them easy to scale up and down based on traffic <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.
*   Platform as a Service (PaaS) tools manage this infrastructure for you <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   Alternatively, you might host your app on a decentralized blockchain with Web3 to avoid vendor lock-in with large tech corporations <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

This covers about 1% of what you need to know to be a full stack web developer <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. If it seems overwhelming, don't worry—most developers learn by using Google to figure things out on the fly <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.