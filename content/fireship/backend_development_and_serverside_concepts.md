---
title: Backend development and serverside concepts
videoId: erEgovG9WBs
---

From: [[fireship]] <br/> 

Backend development focuses on the server-side logic and database interactions that power web applications, enabling the [[frontend_and_backend_development_layers | front-end]] to function dynamically.

## The Internet and World Wide Web

The Internet is a vast network of billions of machines connected globally <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>. It officially began on January 1st, 1983, with the establishment of the Internet Protocol Suite, which standardized computer communication <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>. The Internet Protocol (IP) identifies computers on the network by assigning each a unique IP address <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>. Data is sent back and forth using the Transmission Control Protocol (TCP), which breaks data into small packets, transmits them through physical components like fiber optic cables, and reassembles them at the receiving end <a class="yt-timestamp" data-t="00:59:00">[00:59:00]</a>.

While the Internet can be thought of as hardware, the World Wide Web is like software that operates on top of the Internet, allowing users to access web pages via the Hypertext Transfer Protocol (HTTP) <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>. HTTP assigns a Uniform Resource Locator (URL) to every page of content <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>.

## Client-Server Architecture

In [[introduction_to_web_development | web development]], the interaction between a user's browser and a website's content is governed by a client-server model:
*   **Client** The web browser is referred to as the client because it consumes information <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>.
*   **Server** On the other end of a URL is a server, another computer that receives an HTTP request from the client and sends a response containing the web page content <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>. These interactions are known as HTTP messages <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.

### Domain Names and DNS
Every web page has a unique domain name (e.g., fireship.io) <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>. When a domain is accessed in a browser, it is routed through the Domain Name System (DNS), which maps these names to an actual IP address on a server <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>. DNS acts as "the phone book of the internet" <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>.

### HTTP Methods and Status Codes
HTTP requests have various methods, with `GET` used to retrieve data from a server, and methods like `POST` and `PATCH` used to modify data <a class="yt-timestamp" data-t="10:10:00">[10:10:00]</a>. When a server responds, it includes a status code:
*   `200`: Success <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>
*   `4xx`/`5xx`: Errors (e.g., `404` for a page that doesn't exist) <a class="yt-timestamp" data-t="10:29:00">[10:29:00]</a>

## Server-Side Technologies

The [[frontend_and_backend_development_layers | backend]] stack processes requests, interacts with databases, and generates responses.

### [[JavaScript serverside with Nodejs | Node.js]]
[[JavaScript serverside with Nodejs | Node.js]] is a server-side runtime based on JavaScript <a class="yt-timestamp" data-t="09:22:00">[09:22:00]</a>. It is widely popular because it uses the same language as the browser, allowing developers to share code between the [[frontend_and_backend_development_layers | front-end]] and [[frontend_and_backend_development_layers | backend]] <a class="yt-timestamp" data-t="09:30:00">[09:30:00]</a>. [[JavaScript serverside with Nodejs | Node.js]] is built on the V8 engine, which powers the Chromium browser, and runs code in a single-threaded, non-blocking event loop, enabling it to handle many simultaneous connections efficiently <a class="yt-timestamp" data-t="09:35:00">[09:35:00]</a>.

The Node Package Manager (NPM) allows developers to share and reuse code through packages or modules <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a>.

### Data Handling: Databases
A database is essential for any full-stack web application to store data, such as user information <a class="yt-timestamp" data-t="12:12:00">[12:12:00]</a>. To access this data, user authentication is often required <a class="yt-timestamp" data-t="12:19:00">[12:19:00]</a>.

## Website Rendering Strategies

Different strategies exist for delivering content from the server to the client:

*   **Server-Side Rendering (SSR)**: In this classic approach, the client sends a `GET` request, and the server generates all the HTML for the page and sends it back as a response <a class="yt-timestamp" data-t="10:06:00">[10:06:00]</a>.
*   **Single-Page Application (SPA)**: The server initially renders only a minimal shell for the root URL, with JavaScript then handling the rendering for all other pages entirely client-side in the browser <a class="yt-timestamp" data-t="10:45:00">[10:45:00]</a>. When more data is needed, the app makes an HTTP request for a minimal amount of data, typically in JSON format <a class="yt-timestamp" data-t="11:01:00">[11:01:00]</a>.
*   **Static Site Generation (SSG)**: Every web page on the site is pre-built and uploaded to a server in advance <a class="yt-timestamp" data-t="11:22:00">[11:22:00]</a>. A [[frontend_and_backend_development_layers | front-end]] JavaScript framework often "hydrates" the HTML to make it interactive and behave like a SPA <a class="yt-timestamp" data-t="11:30:00">[11:30:00]</a>.

## Full-Stack Frameworks and Deployment

To implement these patterns, many developers use full-stack frameworks like [[developing_web_apps_with_nextjs | Next.js]], Ruby on Rails, or Laravel <a class="yt-timestamp" data-t="11:45:00">[11:45:00]</a>. These frameworks abstract away tedious tasks, including module bundlers (like webpack) that package code for browsers <a class="yt-timestamp" data-t="11:52:00">[11:52:00]</a>.

Before deployment, code is typically tested with a web server (e.g., Nginx, Apache), though frameworks often provide this functionality locally <a class="yt-timestamp" data-t="12:25:00">[12:25:00]</a>. For live deployment, developers often use cloud providers like AWS <a class="yt-timestamp" data-t="12:38:00">[12:38:00]</a>. Applications are frequently containerized with Docker to enable easy scaling based on traffic <a class="yt-timestamp" data-t="12:42:00">[12:42:00]</a>. Platform-as-a-Service (PaaS) tools can manage this infrastructure <a class="yt-timestamp" data-t="12:49:00">[12:49:00]</a>. Alternatively, apps can be hosted on decentralized blockchains with Web3 <a class="yt-timestamp" data-t="12:55:00">[12:55:00]</a>.