---
title: JavaScript and Frontend Development
videoId: erEgovG9WBs
---

From: [[fireship]] <br/> 

## Introduction to Web Development
Web development allows building on a platform with nearly 5 billion daily active users, enabling global connection and communication <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This platform is primarily used for sharing memes, creating parasocial relationships, amplifying drama, and generating significant revenue <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. To create [[front_end_and_back_end_development | full stack web applications]], a wide range of concepts are necessary <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## The Internet and The World Wide Web
The Internet is a network of billions of connected machines <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. It was established on January 1st, 1983, with the standardization of the Internet Protocol Suite <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. The Internet Protocol (IP) identifies computers on the network with unique IP addresses <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Data is sent using the Transmission Control Protocol (TCP), which breaks data into small packets, sends them through physical components like fiber optic cables, and reassembles them at the receiving end <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

While the Internet can be thought of as hardware, the World Wide Web is like software that operates on top of the internet <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. The Web allows access to web pages via the Hypertext Transfer Protocol (HTTP) <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Each page is given a Uniform Resource Locator (URL) <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

### Client-Server Interaction
Web browsers, known as clients, are used to access URLs and render content visually <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. On the other end of a URL is a server, which receives an HTTP request from the client and sends back a response containing the webpage content <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Every web page has a unique domain name, like `fireship.io` <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. When navigating to a domain, the Domain Name System (DNS) maps the name to an IP address on a server <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## Hypertext Markup Language (HTML)
The content seen on a web page is represented by Hypertext Markup Language (HTML) <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Browsers typically have Developer Tools to inspect the HTML structure <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. HTML documents are built using a text editor like VS Code <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

### Elements and Attributes
An HTML document is a collection of elements, defined by opening and closing tags with content in between, such as paragraph (`<p>`) or heading (`<h1>`) tags <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Elements can also handle user input, like `select` and `input` elements used for forms <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. Elements can have attributes that change their behavior, such as an `input` element having a `type` attribute (e.g., `text` or `number`) <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. The `<a>` (anchor) tag creates links that enable navigation between pages based on their URL <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

### Document Object Model (DOM)
HTML elements are nested hierarchically to form the Document Object Model (DOM) <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. A web page is divided into two main parts:
*   **Head:** Contains invisible content like metadata and the page title <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   **Body:** Contains the main visible content for the user <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

HTML tags provide semantic meaning to browsers and bots, which aids search engines in displaying results and improves accessibility for devices like screen readers <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. The `div` (division) element is a common way to define a section of a web page <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

## Cascading Stylesheets (CSS)
[[Front End and Back End Development | Web developers]] use Cascading Stylesheets (CSS) to change the appearance of HTML elements <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

### Styling Methods
*   **Inline Style:** Uses the `style` attribute directly on an element, containing properties and values (e.g., `background-color: black; color: red;`) <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. This applies only to that specific element <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
*   **Style Tag:** CSS code can be placed within a `<style>` tag in the HTML document, requiring a selector to target specific elements (e.g., all paragraph elements) <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **External Style Sheet:** The most common method, linking an external CSS file to the web page in the `<head>` section of the document <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

CSS uses specificity rules to determine which styles apply when multiple styles target the same element <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

### Layout and Positioning
One of the most challenging aspects of CSS is layout and positioning <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. Every element is considered a box, wrapped with padding, border, and margin <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   **Block Display:** Elements like headings have `display: block` by default, taking up all available horizontal space <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   **Inline Display:** Elements like images have `display: inline`, allowing them to line up horizontally <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

The `position` property can be customized:
*   **Relative Positioning:** Moves an element from its normal position <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   **Absolute Positioning:** Position values are relative to its nearest ancestor <a class="yt-timestamp" data="00:05:34">[00:05:34]</a>.
*   **Fixed Positioning:** Keeps an element on the screen even when the user scrolls, as it's fixed to the entire viewport <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

### Responsive Design
Creating responsive layouts is crucial for web developers, ensuring pages look good on various screen sizes <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **Media Queries:** Allow applying different styles based on device information, such as screen width <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Flexbox (`display: flex`):** Enables a parent element to control the flow of its children, easily creating rows and columns <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   **CSS Grid (`display: grid`):** Used for more complex layouts, controlling multiple rows and columns simultaneously <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

CSS supports mathematical operations with `calc()` and custom properties (variables) for reusability <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. Many developers extend vanilla CSS with tools like SAS for additional programmatic features <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

## JavaScript
[[JavaScript fundamentals and practical concepts | JavaScript]] is the third essential language for web developers <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. While not strictly required to build a website, most developers use it to make the user interface interactive <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

### Execution and Structure
[[Using JavaScript on web and server environments | JavaScript code]] can be run on a web page by opening a `<script>` tag and writing code inside <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. The browser interprets HTML from top to bottom and executes the script when encountered in the DOM <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. Typically, JavaScript is written in a separate file and referenced using the `src` attribute on the script tag <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. The `defer` attribute ensures the code runs after the DOM content has loaded <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. JavaScript, formally known as ECMAScript, is standardized across major browsers <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.

### Variables and Types
Variables can be declared using:
*   `let`: For variables that might be reassigned <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   `const`: For variables that cannot be reassigned <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.

JavaScript is a dynamically typed language, meaning type annotations are not necessary <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. However, many developers use TypeScript to add static typing on top of JavaScript for better development practices <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

### Event Handling
A primary use of JavaScript is to handle events <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. When a user interacts with a web page (e.g., click, mouse move, form input), the browser emits an event <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. Browser APIs, such as `document.querySelector()`, allow selecting an element with a CSS selector <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>. An event listener, which is a function, can then be assigned to the element to be called whenever the event occurs <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

### Data Structures and Inheritance
[[JavaScript fundamentals and practical concepts | JavaScript]] includes built-in data structures like arrays for collections of values <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. The most fundamental data structure is the object, also known as a dictionary or hashmap <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. Non-primitive types inherit functionality from the `Object` class <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

JavaScript uses prototypal inheritance, where an object can be cloned to create a chain of ancestors, allowing children to inherit properties and methods <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. Although JavaScript supports `class` syntax, these are merely syntactic sugar for prototypal inheritance <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.

## JavaScript Frontend Frameworks
Most developers utilize [[javascript_frameworks_and_their_updates | frontend frameworks]] like React, Vue, [[using_svelt_for_front_end_development | Svelte]], and Angular <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. These frameworks represent the UI as a tree of components <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>. A component can encapsulate HTML, CSS, and JavaScript into a custom HTML-like element <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. They produce declarative code, which describes the UI's behavior, making it easier to work with compared to imperative vanilla JavaScript <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

## Frontend Rendering Strategies

### Server-Side Rendering (SSR)
In classic Server-Side Rendering, the client makes a GET request for a URL <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. The server receives the request, generates all the HTML, and sends it back to the client as a response <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. Responses include a status code, such as `200` for success or `404` for a page not found <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

### Single Page Application (SPA)
With a Single Page Application, the server initially renders only a shell for the root URL <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. JavaScript then handles the rendering of all other pages client-side in the browser, making the website feel like a native application <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. When more data is needed, the app makes an HTTP request for a minimal amount of data, often in JSON format <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. SPAs offer a great user experience but can be difficult for bots like search engines to understand <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

### Static Site Generation (SSG)
Static Site Generation involves uploading every web page to a server in advance <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. This allows bots to easily access the necessary information <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. A [[javascript_trends_and_frameworks | frontend JavaScript framework]] typically "hydrates" the HTML, making it interactive and behave like a Single Page Application <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

## Development Tools and Practices
Performance is crucial, and tools like Lighthouse help optimize metrics such as "first contentful paint" and "time to interactive" <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

Many developers use [[choosing_the_best_javascript_framework | full-stack frameworks]] like Next.js, Ruby on Rails, or Laravel, which abstract away tedious tasks <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. These often include:
*   **Module Bundlers:** Tools like Webpack that package JavaScript, CSS, and HTML for browser compatibility <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.
*   **Linters:** Tools like ESLint that warn when code doesn't follow style guidelines <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.

To store data for a full stack web application, a database is essential <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>. User authentication is required for users to log in and access data <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

Before deployment, code needs to be tested with a web server <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>. Frameworks often handle this by serving files on `localhost`, which makes your IP address behave like a remote web server <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.

For deployment, developers often use cloud providers like AWS <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>. Applications are frequently containerized with Docker, allowing them to scale up and down based on traffic <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. Platform-as-a-Service (PaaS) tools manage this infrastructure <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>, or applications can be hosted on decentralized blockchains using Web3 <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.

> [!info] Note
> The world of web development, especially [[front_end_and_back_end_development | full stack]], is vast and constantly evolving <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. Most developers continuously learn and use resources like Google to solve problems on the fly <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.