---
title: Front End and Back End Development
videoId: Sxxw3qtb3_g
---

From: [[fireship]] <br/> 

When embarking on a coding journey, especially with a startup idea, one crucial decision is choosing a technology stack, commonly known as a tech stack <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Changing a tech stack later can be a significant challenge <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. Every application functions like a "technology sandwich" <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## What is a Tech Stack?

While there's no official definition, a tech stack can be broken down into three primary layers <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>:

1.  **Front-End Layer**: Tools for building the user interface for the end-user <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
2.  **Back-End Layer**: Includes server-side runtimes and databases to store user-generated data <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. Cloud providers are also considered part of this layer due to vendor lock-in <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
3.  **APIs Layer**: Tools that connect the front-end to the back-end <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. This often includes essential third-party services necessary for the app's operation <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## Historical Context: The LAMP Stack

The original and foundational tech stack was LAMP, which emerged in the late 1990s <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. LAMP stands for:

*   **L**inux
*   **A**pache
*   **M**ySQL
*   **P**HP

Building web applications in the 90s was complex and often required expensive commercial software <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. LAMP offered a free and open-source alternative, leading to the development of web frameworks like WordPress and Joomla <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Modern Tech Stack Complexity

While modern web application development is easier than in the past, tech stacks have become significantly more complicated due to the proliferation of tools and services <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

Common modern tech stacks often have catchy acronyms, though these don't always capture the full scope of tools needed <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>:

*   **MEAN**: MongoDB, Express, Angular, Node <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
*   **MERN**: MongoDB, Express, React, Node <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>
*   **MEVN**: MongoDB, Express, Vue, Node <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>
*   **Fancy**: Firebase, Hugo, Angular, Node, Stripe, Express <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>

Websites like stackshare.io allow users to explore popular technologies and the companies that use them <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

## Architecting a Complex Tech Stack (Example)

Let's consider building a complex application, like a social media platform similar to Myspace, requiring user authentication and a globally scalable database <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### Front-End Layer

The primary consideration is where customers will consume the application (web, iOS, Android, desktop, IoT) <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. For web-first applications, the programming language will almost always be [[javascript_and_frontend_development | JavaScript]] <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

*   **Language**: [[javascript_and_frontend_development | JavaScript]], often augmented with TypeScript for a type system to catch bugs and improve code reliability <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **UI Framework**: React is a popular choice due to its large developer community and ease of integrating [[crossplatform_mobile_app_development | React Native]] for mobile applications <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. Alternatives include [[using_svelt_for_front_end_development | Svelte]] and Vue.js <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **State Management**: For scalable applications, a state management solution like Redux is often used, though it can involve more boilerplate code <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
*   **Styling**:
    *   Vanilla CSS is difficult to manage on its own <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
    *   Tailwind CSS provides utility classes for rapid styling <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
    *   CSS pre-processors like SAS (Sass) offer extra syntax for efficient code <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
    *   PostCSS can purge unused styles and prepare CSS for production <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
*   **Module Bundler**: Tools like Webpack combine raw [[javascript_and_frontend_development | JavaScript]] files into a single bundle for browser use <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

### Back-End Layer

The database choice is critical for user-generated data <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

*   **Databases**:
    *   **NoSQL Document Databases**: MongoDB or Firestore are easy to learn, inexpensive, and scalable, but may struggle with complex relationships like social graphs <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
    *   **Relational Databases**: MySQL or PostgreSQL are popular for handling relationships but can be less flexible and more expensive to operate <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. MySQL is a common "gold standard" choice <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
    *   **Caching**: Redis is often used as a cache, storing data in memory for faster reads <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
    *   **Graph Databases**: More exotic options exist for highly interconnected data <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   **Server-Side Runtime/Frameworks**: The choice often depends on the developer's comfort with a programming language <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
    *   Python: Flask, Django <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>
    *   [[web_development_with_ruby_on_rails | Ruby on Rails]] <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>
    *   PHP: Laravel <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>
    *   Java: Spring <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>
    *   [[javascript_and_frontend_development | JavaScript]]: Node.js with a framework like NestJS, which supports TypeScript <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
*   **Object-Relational Mapper (ORM)**: Tools like TypeORM help avoid writing raw SQL queries <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   **Web Server**: Nginx or Apache make the server available on the internet <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   **Deployment & Infrastructure**:
    *   **Containerization**: Docker standardizes the code environment for deployment <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
    *   **Orchestration**: Kubernetes manages multiple containers as the application scales <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
    *   **Cloud Provider**: Amazon Web Services (AWS) is a popular, though complex, choice for hosting infrastructure <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
    *   **Infrastructure as Code**: Terraform programmatically creates and versions infrastructure for reliability <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
*   **Source Code Management**: GitHub is a common platform for hosting source code <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   **Continuous Integration (CI)**: GitHub Actions can automate testing and redeployment of code updates <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

### APIs and Third-Party Services

APIs bridge the front-end and back-end, and third-party services handle complex functionalities:

*   **API Communication**: GraphQL with a library like Apollo allows the front-end to securely communicate with the back-end <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. REST is another common option <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **Payments**: Stripe provides SDKs for both server and front-end to collect payments <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
*   **User Authentication**: Auth0 handles user authentication <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
*   **Content Moderation**: Amazon Recognition offers deep learning capabilities, such as for content detection <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Messaging**: Twilio assists with sending text messages <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

These APIs help manage tasks that are too complex to build from scratch <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.

## Simplified and Practical Tech Stack

Over-engineering a tech stack can lead to unnecessary complexity <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. Users prioritize a good experience and won't know the underlying technology <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. It's often better to start with a simpler approach.

### Simplified Front-End

*   **HTML**: Start with a plain HTML file <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
*   **[[javascript_and_frontend_development | JavaScript]] Framework**: Petite Vue offers Vue.js-compatible syntax and can be dropped in with a script tag, eliminating the need for a module bundler like Webpack <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   **Styling**: Bootstrap provides a quick way to achieve a decent UI <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   **[[crossplatform_mobile_app_development | Crossplatform mobile app development]]**: Ionic can wrap the web application in a web view, enabling quick deployment to iOS and Android <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

### Simplified Back-End

*   **Backend as a Service (BaaS)**: Firebase provides a document database that scales without a dedicated backend server, handles user authentication, and can be included via a script tag <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
*   **Serverless Functions**: Firebase Cloud Functions allow writing server-side code in Node.js, Python, or Go, deployed with a single command without server configuration worries <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. It scales automatically, bypassing the need for Docker, Kubernetes, or Terraform <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
*   **Continuous Integration**: For simpler applications, CI/CD might not be necessary unless daily testing and redeployment occur <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   **APIs**: GraphQL can be omitted for simpler apps, as it's better suited for complex applications with multiple APIs to stitch together <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

This simplified approach, dubbed the "petite Fire stack," can be an easy way to build a full-stack web application <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

```ad-note
For more information on various tech stacks, consider exploring resources like stackshare.io to see what successful companies use <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
```