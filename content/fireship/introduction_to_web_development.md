---
title: Introduction to web development
videoId: erEgovG9WBs
---

From: [[fireship]] <br/> 

Web development involves building on a platform with nearly 5 billion daily active users, connecting them like neurons of a global superintelligent brain <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. While this system has the potential to cure disease, eliminate poverty, and advance science, it's primarily used for sharing memes, creating parasocial relationships, amplifying drama, and making money <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. To get into web development, a wide range of concepts need to be understood <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## The Internet and the Web

The internet is a network of billions of machines connected together <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. It was officially born on January 1st, 1983, with the establishment of the Internet Protocol Suite, which standardized how computers communicate <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

*   **Internet Protocol (IP)**: Used to identify different computers on the network by assigning each a unique IP address <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   **Transmission Control Protocol (TCP)**: Allows computers to send data back and forth by breaking data into small packets, sending them through physical components like fiber optic cables and modems, and reassembling them at the receiving end <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

The internet can be thought of as hardware <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. In contrast, the World Wide Web is like software that sits on top of the internet, allowing people to access web pages <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

*   **Hypertext Transfer Protocol (HTTP)**: Used to access web pages, giving every page a unique Uniform Resource Locator (URL) <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   **Web Browser**: A tool used by humans to access a URL, where content is rendered visually <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. The browser acts as the *client*, consuming information <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   **Server**: Another computer at the other end of a URL that receives an HTTP request from the client and sends a response containing the webpage content <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. These interactions are called HTTP messages <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Domain Name**: A unique name for a web page (e.g., fireship.io) <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. Domain names can be registered via a registrar accredited by ICANN, a nonprofit overseeing internet namespaces <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   **Domain Name System (DNS)**: Maps domain names to actual IP addresses on a server, functioning like the internet's phone book <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

For more on these foundational concepts, see [[understanding_the_internet_and_web_infrastructure | Understanding the Internet and Web Infrastructure]] and [[networking_and_web_technologies | Networking and Web Technologies]].

## Front-End Development

Front-end development focuses on the user interface and experience of a web application.

### HTML (HyperText Markup Language)

HTML represents the actual content seen on a web page <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Web browsers often include developer tools to inspect HTML structure <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. A text editor like VS Code is used to build web pages <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

*   **Elements**: An HTML document is a collection of elements, each consisting of an opening and closing tag with content in the middle (e.g., paragraph, heading) <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   **User Input**: Elements like `<select>` and `<input>` are used to build forms and handle user input <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
*   **Attributes**: Elements can have attributes that change their behavior, such as an `<input>` element having a `type` attribute like "text" or "number" <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   **Anchor Tag (`<a>`)**: The `a` tag (anchor) creates links that allow navigation between different pages based on their URL <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   **Document Object Model (DOM)**: HTML elements are nested hierarchically to form the DOM <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   **Structure**: A web page is split into two parts:
    *   **Head**: Contains invisible content like metadata and a title <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
    *   **Body**: Contains the main content visible to the end user <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
*   **Semantics**: HTML tags provide hints to browsers and bots about the semantic meaning of a web page, aiding search engine display and accessibility for devices like screen readers <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
*   **Div Element (`<div>`)**: A common element used to define a section of a web page <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

### CSS (Cascading Style Sheets)

CSS allows developers to change the appearance of HTML elements <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

*   **Inline Style**: Achieved with the `style` attribute on an element, containing properties and values that change its appearance (e.g., `background-color`, `text-color`) <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. These styles apply only to that specific element <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
*   **Cascading Nature**: CSS can be applied to multiple elements simultaneously, improving code reusability <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   **Style Tags**: CSS code can be moved into a `<style>` tag within the HTML document <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Selectors**: Define which elements to target with CSS rules <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. A selector can target all elements of a certain type (e.g., all paragraph elements) or be more granular by defining a `class` <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
*   **Specificity Rules**: CSS has rules to determine which styles are applied when multiple styles target the same element <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   **External Stylesheet**: Most often, CSS is stored in a separate file and linked to the web page in the `<head>` of the document <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **Layout and Positioning**: One of the most difficult aspects of CSS <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
    *   **Box Model**: Every element is like a box wrapped with padding, border, and margin <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
    *   **Display Property**: Elements take up space from top to bottom. `display: block` elements take up all available horizontal space (e.g., headings), while `display: inline` elements line up horizontally (e.g., images) <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
    *   **Position Property**: Changes an element's position:
        *   `relative`: Moves an element a certain number of pixels from its normal position <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
        *   `absolute`: Position values are relative to its nearest ancestor <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
        *   `fixed`: Keeps an element on the screen even when the user scrolls, as it's fixed to the viewport <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
*   **Responsive Layouts**: Creating layouts that look good on various screen sizes <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
    *   **Media Queries**: Allow applying different styles based on device information (e.g., screen width) <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
    *   **Flexbox (`display: flex`)**: Allows a parent element to control the flow of its children, easily creating rows and columns <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
    *   **CSS Grid (`display: grid`)**: Used for more complex layouts, controlling multiple rows and columns simultaneously <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   **Advanced CSS Features**:
    *   `calc()`: Performs mathematical operations <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
    *   Custom Properties (CSS Variables): Reusable variables <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
*   **CSS Preprocessors**: Tools like SAS extend vanilla CSS with programmatic features <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

### JavaScript

JavaScript (JS), formally known as ECMAScript, is a **programming language** standardized in all major browsers, primarily used to make user interfaces more interactive <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

*   **Execution**: JS code can be written within `<script>` tags in HTML, or more commonly, in a separate file referenced by the `src` attribute on the `<script>` tag <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. The `defer` attribute can be used to ensure the code runs after the DOM content has loaded <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   **Variables**: Declared using `let` (for reassignable variables) or `const` (for variables that cannot be reassigned) <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   **Dynamic Typing**: JS is dynamically typed, meaning type annotations are not necessary <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   **TypeScript**: Many developers use TypeScript as an alternative to add static typing on top of JavaScript <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   **Event Handling**: A common use case for JavaScript is handling events triggered by user actions (e.g., click, mouse move, form input change) <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
    *   **Browser APIs**: APIs like `document` provide methods such as `querySelector` to select HTML elements using CSS selectors <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.
    *   **Event Listener**: A function assigned to an element that is called when a specific event occurs (e.g., a button click) <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Data Structures**:
    *   **Array**: Represents a collection of values <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
    *   **Object**: The most fundamental data structure, also called a dictionary or hashmap <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. Non-primitive types inherit functionality from the `Object` class <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **Prototypal Inheritance**: JavaScript relies on prototypal inheritance, where objects can be cloned to create a chain of ancestors from which children inherit properties and methods <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. While JavaScript supports classes, they are syntactic sugar for prototypal inheritance <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
*   **Front-End Frameworks**: Most developers use front-end [[comparison_of_web_development_frameworks | web development frameworks]] like React, Vue, Svelte, or Angular to abstract away low-level details of JavaScript <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. These frameworks represent the UI as a tree of components, encapsulating HTML, CSS, and JavaScript into custom HTML-like elements <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>. They produce declarative code, which describes what the UI does, making it easier to work with than imperative vanilla JavaScript <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

## Back-End Development

The back-end stack handles server-side logic and data management.

### Node.js

[[introduction_to_nodejs | Node.js]] is a server-side runtime based on JavaScript <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. It's popular because it uses the same language as the browser and is based on the V8 engine that powers the Chromium browser <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. Node.js runs code in a single-threaded, non-blocking event loop, allowing it to handle many simultaneous connections efficiently <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.

*   **Node Package Manager (NPM)**: Allows developers to share and reuse code remotely through packages (also called modules) <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. A module is a file with an `export` statement, consumable by other files using an `import` statement <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

### Website Delivery Strategies

How a website is delivered from the server to the client <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>:

*   **Server-Side Rendering (SSR)**: The client makes a `GET` request for a URL <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. The server generates all the HTML and sends it back as a response <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. HTTP methods like `POST` and `PATCH` are used to modify data <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. Responses include a status code (e.g., `200` for success, `404` for "not found") <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   **Single-Page Application (SPA)**: The server initially renders only a shell for the root URL <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. JavaScript handles rendering for all other pages entirely client-side in the browser, making the website feel like a native application <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. When more data is needed, an HTTP request is made for minimal data in JSON format, which is a data interchange format understood by any programming language <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. SPAs can be difficult for bots (like search engines) to understand <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.
*   **Static Site Generation (SSG)**: Every web page is uploaded to a server in advance, allowing bots to easily get information <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. A front-end JavaScript framework then "hydrates" the HTML to make it interactive and behave like an SPA <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

### Performance and Tools

Performance is crucial. Tools like Lighthouse are used to optimize metrics such as "first contentful paint" and "time to interactive" <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

### Full-Stack Frameworks

Many developers use full-stack [[comparison_of_web_development_frameworks | web development frameworks]] like [[developing_web_apps_with_nextjs | Next.js]], Ruby on Rails, or Laravel to abstract away tedious tasks <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.

*   **Module Bundlers**: Tools like Webpack package JavaScript, CSS, and HTML for browser compatibility <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.
*   **Linters**: Tools like ESLint warn when code doesn't follow style guidelines <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.

### Data Storage and User Management

*   **Databases**: Essential for storing application data, such as user information <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   **User Authentication**: The process of allowing users to log in <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

## Deployment

Before deploying code, it needs to be tested with a web server <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.

*   **Web Servers**: Tools like Nginx and Apache create HTTP servers <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>, though frameworks often handle this by serving files on `localhost`, making your own IP address behave like a remote web server <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
*   **Cloud Providers**: For deployment, large cloud providers like AWS are commonly used <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.
*   **Containerization**: Most applications are containerized with Docker, making them easy to scale up and down based on traffic <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.
*   **Platform as a Service (PaaS)**: Many [[web_application_tools_for_developers | web application tools]] function as a PaaS to manage infrastructure <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Decentralized Hosting**: Applications can also be hosted on a decentralized blockchain with Web3 <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.

Understanding all these concepts represents about 1% of what a full-stack web developer needs to know <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. Most developers frequently use search engines to figure things out <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.