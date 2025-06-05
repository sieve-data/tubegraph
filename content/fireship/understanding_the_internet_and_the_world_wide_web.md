---
title: Understanding the Internet and the World Wide Web
videoId: erEgovG9WBs
---

From: [[fireship]] <br/> 

[[Introduction to Web Development | Web development]] is the process of building applications on a platform with nearly 5 billion daily active users, enabling global communication and interaction <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This field involves understanding a multitude of concepts necessary for building full-stack web applications <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## The Internet

The Internet is fundamentally a [[Network communication and cloud computing | network]] of billions of interconnected machines <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. It was officially established on January 1, 1983, with the standardization of the [[Network communication and cloud computing | Internet Protocol Suite]] <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

### Internet Protocol (IP)
The [[Network communication and cloud computing | Internet Protocol (IP)]] is used to identify different computers on the network by assigning each a unique IP address <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

### Transmission Control Protocol (TCP)
Computers send data back and forth using the Transmission Control Protocol (TCP) <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. This protocol breaks data into small packets, sends them through physical components like fiber optic cables and modems, and then reassembles them at the receiving end <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. The Internet can be thought of as the underlying hardware infrastructure <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## The World Wide Web

Distinct from the Internet, the World Wide Web (or simply "the Web") is like software that operates on top of the Internet <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. It's where users access web pages using the [[Understanding HTTP verbs and status codes | Hypertext Transfer Protocol (HTTP)]] <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### Key Components of the Web

*   **Uniform Resource Locator (URL)**: Every piece of content on the Web is uniquely identified by a URL <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Web Browser (Client)**: Humans typically use web browsers to access URLs, which then visually render the content on their screens <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. The browser acts as the "client" because it consumes information <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   **Server**: At the other end of a URL is a "server" computer <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. It receives an [[Understanding HTTP verbs and status codes | HTTP request]] from the client and sends back a response containing the webpage content <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. These communications are known as [[Understanding HTTP verbs and status codes | HTTP messages]] <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Domain Name System (DNS)**: Web pages have unique domain names (e.g., fireship.io) <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. Domain names can be registered through a registrar accredited by ICANN, a non-profit overseeing Internet namespaces <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. When a domain is entered into a browser, the Domain Name System (DNS) routes it by mapping the name to the actual IP address of a server, much like a phone book for the Internet <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## [[HTML and the Document Object Model DOM | HTML (Hypertext Markup Language)]]

The actual content seen on a web page is represented by [[HTML and the Document Object Model DOM | HTML]] <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Most browsers offer developer tools to inspect the structure of HTML <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

### HTML Structure and Elements

*   **Text Editor**: To build a webpage, a text editor like VS Code is used <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   **Elements**: An HTML document is a collection of elements, each consisting of an opening tag, content, and a closing tag (e.g., paragraph `<p>`, heading `<h1>`) <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Elements also handle user input, such as `<select>` and `<input>` elements used for forms <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
*   **Attributes**: Elements can have attributes that modify their behavior, such as an `input` element having a `type` (e.g., "text", "number") to dictate how the browser renders it for appropriate value collection <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **Anchor (`<a>`) Tag**: The `<a>` (anchor) tag is crucial for [[HTML and the Document Object Model DOM | HTML]], as it creates links that allow navigation between different pages based on their URLs <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   **[[HTML and the Document Object Model DOM | Document Object Model (DOM)]]**: Elements are nested hierarchically to form the [[HTML and the Document Object Model DOM | Document Object Model (DOM)]] <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. A webpage is typically split into two parts: the `head` (for invisible content like metadata and title) and the `body` (for the main content visible to the user) <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   **Semantic Meaning**: Wrapping content in tags provides browsers and bots with semantic meaning, which helps search engines display results correctly and improves accessibility for devices like screen readers <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
*   **Div Element**: The `div` (division) is a common element used to define a section of a webpage <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

## CSS (Cascading Style Sheets)

CSS is the second language a web developer needs to learn, enabling changes to the appearance of [[HTML and the Document Object Model DOM | HTML]] elements <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

### Styling Methods

*   **Inline Style**: An inline style applies directly to an element using the `style` attribute, containing properties and values that modify appearance (e.g., `background-color: black; color: red;`) <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. This only affects the specific element <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
*   **Cascading Nature**: CSS "cascades," allowing styles to be applied to multiple elements simultaneously, enhancing code reusability <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   **Style Tags**: Styles can be moved into a `<style>` tag within the HTML document <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. A "selector" is defined to target specific elements (e.g., all paragraph elements, or elements with a specific `class` attribute) <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   **Specificity Rules**: CSS has specificity rules that determine which styles are applied when multiple styles target the same element <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   **External Stylesheets**: Most commonly, an external stylesheet is used, linked to the webpage in the `head` of the document <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

### Layout and Positioning

*   **Box Model**: Every element in CSS is considered a box, with properties like padding, border, and margin wrapping its content <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   **Display Property**:
    *   `display: block`: Elements like headings take up all available horizontal space by default <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
    *   `display: inline`: Elements like images can line up horizontally <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
*   **Position Property**: The `position` property allows customization of an element's placement <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>:
    *   `relative`: Moves an element a certain number of pixels from its normal position <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
    *   `absolute`: Positions values relative to its nearest ancestor <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
    *   `fixed`: Keeps an element on the screen even when the user scrolls, as it's fixed to the viewport <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

### Responsive Design and Layout Tools

*   **Responsive Layouts**: A major challenge for web developers is creating responsive layouts that look good on various screen sizes <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **Media Queries**: Allow applying different styles based on information about the device rendering the webpage <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   **Flexbox (`display: flex`)**: Controls the flow of child elements within a parent, making it easy to create rows and columns <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   **CSS Grid (`display: grid`)**: Used for more complex layouts, controlling multiple rows and columns simultaneously <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

### Advanced CSS Features

*   **`calc()` Function**: Performs mathematical operations within CSS <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
*   **Custom Properties (Variables)**: Allow reusing values in multiple places <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
*   **Pre-processors**: Tools like SAS extend vanilla CSS with programmatic features <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

## JavaScript

JavaScript is the third essential language for web developers, primarily used to make the user interface interactive <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

### Execution and Variables

*   **Script Tags**: JavaScript code is run on a webpage by opening a `<script>` tag and writing code inside it <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. The browser interprets HTML from top to bottom and runs the JavaScript code when encountered in the [[HTML and the Document Object Model DOM | DOM]] <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
*   **External Files**: JavaScript is typically written in a separate file and referenced via the `src` attribute on the script tag <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. The `defer` attribute ensures the code runs after the [[HTML and the Document Object Model DOM | DOM]] content has loaded <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   **ECMAScript**: JavaScript is formally known as ECMAScript and is standardized across major browsers <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
*   **Variables**:
    *   `let`: For variables that may be reassigned <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
    *   `const`: For variables that cannot be reassigned <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Dynamic Typing**: JavaScript is dynamically typed, meaning type annotations are not necessary <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. TypeScript is an alternative that adds static typing on top of JavaScript <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

### Event Handling and Data Structures

*   **Event Handling**: JavaScript is commonly used to handle events triggered by user actions (e.g., clicks, mouse movements, form input changes) <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. Browser APIs like `document` provide methods such as `querySelector` to select elements using CSS selectors, and `addEventListener` to assign functions that are called when an event occurs <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
*   **Data Structures**:
    *   **Array**: Represents a collection of values <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
    *   **Object**: The most fundamental data structure, also known as a dictionary or hashmap <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. Anything not a primitive type (like string or number) inherits from the `Object` class <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **Prototypal Inheritance**: JavaScript relies on prototypal inheritance, where objects can be cloned to create a chain of ancestors, with children inheriting properties and methods <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. While JavaScript supports classes, they are syntactic sugar for prototypal inheritance <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.

### Front-End Frameworks

Most developers use front-end frameworks like React, Vue, Svelte, or Angular <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. These frameworks represent the UI as a tree of components, encapsulating [[HTML and the Document Object Model DOM | HTML]], CSS, and JavaScript into custom elements <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>. They produce declarative code, which describes what the UI does, making it easier to work with than imperative vanilla JavaScript <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

## Backend Development

Backend development involves server-side logic and data management.

### Node.js

[[Network communication and cloud computing | Node.js]] is a popular server-side runtime based on JavaScript, allowing web application code to run on the server <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. It uses the same V8 engine that powers the Chromium browser, running code in a single-threaded, non-blocking event loop, which allows it to efficiently handle many simultaneous connections <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

### Node Package Manager (NPM)

[[Network communication and cloud computing | Node.js]] enables developers to share work remotely using the Node Package Manager (NPM) <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. A "package" or "module" is a file containing code with an `export` statement to be used elsewhere, and consumed by an `import` statement <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

## Website Delivery and Rendering Strategies

### Server-Side Rendering (SSR)

In classic server-side rendering, the client makes an [[Understanding HTTP verbs and status codes | HTTP GET request]] for a URL <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. The server generates all the [[HTML and the Document Object Model DOM | HTML]] on the server and sends it back as a response <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. The response includes an [[Understanding HTTP verbs and status codes | HTTP status code]] (e.g., `200` for success, `404` for not found, `500` for server errors) <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

### Single-Page Application (SPA)

A single-page application (SPA) approach means the server renders only a minimal shell for the root URL <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>. JavaScript then handles the rendering for all other pages entirely client-side in the browser, providing a user experience similar to a native app <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. When more data is needed, the app makes an [[Understanding HTTP verbs and status codes | HTTP request]] for a minimal amount of data in JSON format, a data interchange format understood by any programming language <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. While offering a great user experience, SPAs can be difficult for bots (like search engines) to understand <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

### Static Site Generation (SSG)

Static site generation involves uploading every webpage to a server in advance, allowing bots to easily access information <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. A front-end JavaScript framework typically "hydrates" the [[HTML and the Document Object Model DOM | HTML]] to make it fully interactive and behave like a single-page application <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

## Development Tools and Deployment

*   **Performance Optimization**: Tools like Lighthouse are used to optimize performance metrics such as "first contentful paint" and "time to interactive" <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.
*   **Full-Stack Frameworks**: Frameworks like Next.js, Ruby on Rails, and Laravel abstract away tedious development tasks <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
*   **Module Bundlers**: Tools like Webpack package JavaScript, CSS, and [[HTML and the Document Object Model DOM | HTML]] to work efficiently in a browser <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.
*   **Linters**: Linters like ESLint warn developers when code doesn't adhere to style guidelines <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
*   **Databases**: A database is essential for storing data, such as user information, in a full-stack web application <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   **User Authentication**: Users need a way to log in via user authentication <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.
*   **Web Servers**: Before deployment, code is tested with a web server, using tools like Nginx or Apache, or built-in framework features to serve files on "Localhost" (making one's IP address behave like a remote web server) <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.
*   **Cloud Providers**: For deployment, large [[Network communication and cloud computing | cloud providers]] like AWS are commonly used <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.
*   **Docker**: Many applications are containerized with Docker for easy scaling based on traffic <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.
*   **Platform as a Service (PaaS)**: Many tools function as PaaS to manage infrastructure <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   [[Web3 and decentralized internet | Web3 and decentralized internet | Decentralized Blockchain]]: Alternatively, applications can be hosted on a decentralized blockchain with [[Web3 and decentralized internet | Web3]] <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>.

While the scope of [[Introduction to Web Development | web development]] is vast, most developers learn by using resources like Google to figure things out on the fly <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.