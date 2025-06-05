---
title: Understanding the internet and web infrastructure
videoId: erEgovG9WBs
---

From: [[fireship]] <br/> 

[[Introduction to web development | Web development]] involves building on a platform with nearly 5 billion daily active users, connected like the neurons of a global, super-intelligent brain <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It can be used for various purposes, including curing disease, eliminating poverty, advancing science, sharing memes, creating parasocial relationships, amplifying drama, and making money <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## The Internet: A Global Network

The [[Networking and Web Technologies | Internet]] is defined as a network of billions of machines connected together <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. It was officially born on January 1st, 1983, with the establishment of the Internet Protocol Suite <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This suite standardized how computers communicate <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

Key components and protocols include:
*   **Internet Protocol (IP)**: Used to identify different computers on the network by assigning each a unique IP address <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   **Transmission Control Protocol (TCP)**: Allows computers to send data back and forth by breaking it into small packets, like puzzle pieces <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. These packets are sent through physical components, such as fiber optic cables and modems, before being reassembled by the receiving computer <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

The Internet can be thought of as [[Computer Architecture and Components | hardware]] <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## The World Wide Web: Software on the Internet

The [[History and significance of the worldwide web | World Wide Web]] is distinct from the Internet; it's like software that sits on top of the Internet <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. On the Web, people access web pages using the Hypertext Transfer Protocol (HTTP) <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

Key Web concepts:
*   **Uniform Resource Locator (URL)**: HTTP gives every page of content a unique URL <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Web Browser (Client)**: Humans use a web browser to access a URL, which then renders the content visually on their screen <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. The browser is considered the "client" because it consumes information <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   **Server**: On the other end of a URL is another computer called a server <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. It receives an HTTP request from the client and sends back a response containing the webpage content <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. These are known as HTTP messages <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Domain Name System (DNS)**: Every web page has a unique domain name (e.g., fireship.io) <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. Domain names are registered via registrars accredited by ICANN, a nonprofit overseeing internet namespaces <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. When navigating to a domain, DNS routes these names to an actual IP address on a server <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>; DNS is like the phone book of the internet <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## Webpage Structure: HTML

The actual content seen on a web page is represented by HyperText Markup Language (HTML) <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Web browsers typically have Dev Tools to inspect the HTML structure <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

*   **Elements and Tags**: An HTML document is a collection of elements, defined by an opening and closing tag with content in the middle (e.g., paragraph, heading) <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. Elements like `select` and `input` handle user input and build forms <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
*   **Attributes**: Elements can have attributes to change their behavior, such as an `input` element having a `type` like "text" or "number" <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **Anchor Tag (`<a>`)**: The `a` tag or anchor puts the "hypertext" in HTML, creating links that allow navigation between different pages based on their URL <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Document Object Model (DOM)**: Elements are nested in a hierarchy to form the DOM <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Head and Body**: A web page is split into two parts from the root element:
    *   **Head**: Contains invisible content like metadata and the page title <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
    *   **Body**: Contains the main content that the end user sees <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
*   **Semantic Meaning**: Wrapping content in tags gives browsers and bots hints about the semantic meaning of the page, aiding search engines and accessibility devices like screen readers <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
*   **Div Element (`<div>`)**: A common element used to define a section of a web page <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

## Webpage Styling: CSS

The second language for web developers is Cascading Stylesheets (CSS), which allows changing the appearance of HTML elements <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

*   **Applying Styles**:
    *   **Inline Style**: Using the `style` attribute directly on an element, containing properties and values <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
    *   **Style Tag**: Moving CSS code into a `<style>` tag within the HTML document <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
    *   **External Stylesheet**: Most often, CSS is kept in an external file linked to the web page in the `<head>` of the document <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **Selectors**: Define which elements CSS rules should target, e.g., all paragraph elements or elements with a specific class <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   **Specificity Rules**: CSS uses specificity rules to determine which styles apply when multiple styles target the same element <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   **Layout and Positioning**: This is one of the most challenging aspects of CSS <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
    *   **Box Model**: Every element is treated like a box with padding, border, and margin <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
    *   **Display Property**: Elements have default display properties like `block` (takes up all horizontal space) or `inline` (lines up horizontally) <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
    *   **Position Property**: Controls element positioning: `relative` (moves from normal position), `absolute` (relative to nearest ancestor), `fixed` (stays on screen when scrolling) <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Responsive Layouts**: Tools for adapting designs to different screen sizes:
    *   **Media Queries**: Get device information to apply different styles accordingly <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
    *   **Flexbox**: Allows parents to control child flow for easy rows and columns <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
    *   **CSS Grid**: Controls multiple rows and columns for complex layouts <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
*   **Advanced Features**: CSS has `calc` for mathematical operations and custom properties (variables) for reuse <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. Tools like SAS extend CSS with additional programmatic features <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

## Webpage Interactivity: JavaScript

JavaScript is the third language often used by web developers to make the user interface more interactive <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

*   **Execution**: JavaScript code can be written within `<script>` tags in HTML or in separate files referenced by the `src` attribute on the script tag <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. The `defer` attribute ensures the script runs after DOM content has loaded <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   **ECMAScript**: JavaScript is formally known as ECMAScript and is standardized across major browsers <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
*   **Variables**: Declared with `let` (reassignable) or `const` (not reassignable) <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   **Typing**: JavaScript is dynamically typed, but TypeScript can be used to add static typing <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   **Event Handling**: JavaScript handles events emitted by the browser when a user interacts with a page (e.g., click, mouse move, form input) <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. Browser APIs like `document.querySelector` allow grabbing elements to attach event listeners, which are functions called when an event occurs <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.
*   **Data Structures**: Built-in structures include arrays (collections of values) and objects (dictionaries/hashmaps) <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   **Prototypal Inheritance**: JavaScript relies on prototypal inheritance, where objects can be cloned to create a chain of ancestors from which children inherit properties and methods <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. While JavaScript supports classes, they are syntactic sugar for prototypal inheritance <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
*   **Front-end Frameworks**: To simplify development, many developers use front-end frameworks like React, Vue, Svelte, or Angular <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. These frameworks represent the UI as a tree of components, encapsulating HTML, CSS, and JavaScript into custom HTML-like elements, producing declarative and easier-to-manage code <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

## [[Backend development and serverside concepts | Backend Development]]

[[Backend development and serverside concepts | Backend development]] involves server-side logic and data management.

*   **[[Backend development and serverside concepts | Node.js]]**: A server-side runtime based on JavaScript, popular because it uses the same language as the browser <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. It uses the V8 engine (from Chromium browser) to run code in a single-threaded, non-blocking event loop, allowing it to handle many simultaneous connections efficiently <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
*   **Node Package Manager (NPM)**: Allows developers to share work remotely <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. A package (module) is a file with an export statement to be used in another file via an import statement <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

## Website Delivery Strategies

Different approaches exist to deliver website content from the server to the client:

*   **Server-Side Rendering (SSR)**: The client makes a GET request for a URL <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. The server generates all HTML on the server and sends it as a response <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. HTTP requests have methods like GET (retrieve data), POST, and PATCH (modify data) <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. Responses include status codes (e.g., 200 for success, 404 for page not found) <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   **Single Page Application (SPA)**: The server only renders a shell for the root URL <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. JavaScript handles rendering for all other pages client-side in the browser, making the website feel like a native app <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. SPAs make HTTP requests for minimal data as JSON (a data interchange format) <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. However, SPAs can be difficult for bots (like search engines) to understand <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.
*   **Static Site Generation (SSG)**: Every web page is uploaded to a server in advance, allowing bots to get necessary information <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. A front-end JavaScript framework then "hydrates" the HTML to make it interactive like an SPA <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Performance Optimization**: Tools like Lighthouse are used to optimize metrics such as "first contentful paint" and "time to interactive" <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

## Deployment and Tools

*   **Full Stack Frameworks**: Developers use frameworks like Next.js, Ruby on Rails, and Laravel to [[Abstraction layers in web development | abstract away]] tedious tasks <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
*   **Module Bundlers**: Tools like Webpack take JavaScript, CSS, and HTML and package it for browser compatibility <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.
*   **Linters**: Tools like ESLint warn when code doesn't follow style guidelines <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
*   **Databases**: Essential for storing data, such as user information, in a full stack web application <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   **User Authentication**: A process to allow users to log in and access data <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.
*   **Web Servers**: Before deployment, code is tested with a web server <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>. Tools like Nginx and Apache create HTTP servers <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>, or frameworks can serve files on Localhost, making one's own IP address behave like a remote web server <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
*   **Cloud Providers**: For deployment, large cloud providers like AWS are commonly used <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.
*   **Containerization**: Most applications are containerized with Docker, allowing them to scale up and down based on traffic <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.
*   **Platform as a Service (PaaS)**: Many tools function as PaaS to manage infrastructure <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>. Alternatively, apps can be hosted on decentralized blockchains with Web3 <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.