---
title: Frontend and backend development layers
videoId: Sxxw3qtb3_g
---

From: [[fireship]] <br/> 

Every application is structured as a "technology sandwich," requiring choices for its [[technical_details_of_the_websites_tech_stack | tech stack]] <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. While building web applications was simpler in the 1990s, modern [[technical_details_of_the_websites_tech_stack | tech stacks]] have become more complicated due to the proliferation of tools and services <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

A [[technical_details_of_the_websites_tech_stack | tech stack]] can be broken down into three main parts <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>:

## The Frontend Layer

The [[frontend_ui_libraries_and_frameworks | frontend layer]] includes the tools necessary to build a user interface (UI) for the end-user <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

*   **Purpose**
    *   To be consumed by customers on various platforms like web, iOS, Android, desktop, or IoT <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   **Programming Language**
    *   For web applications, the primary language is almost always JavaScript <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
    *   TypeScript, which adds a type system, is often used to catch bugs earlier and deliver more reliable code <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **UI Frameworks and Libraries**
    *   Building complex UIs with vanilla JavaScript is difficult, leading to the use of [[frontend_ui_libraries_and_frameworks | UI frameworks]] <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
    *   Popular options include React (known for its popularity and developer pool) <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>, Angular, and Vue <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
    *   Petite Vue is a lightweight option compatible with Vue.js syntax <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
    *   For state management in large applications, libraries like Redux are common, though they can increase boilerplate code <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
*   **Styling**
    *   Vanilla CSS can be challenging to work with <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
    *   [[front_end_development_aids | Tailwind]] CSS provides pre-built utility classes for rapid styling <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
    *   CSS pre-processors like SAS offer additional syntax for efficient coding <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
    *   PostCSS is used to purge unused styles and prepare CSS for production <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
    *   Bootstrap offers a quick way to achieve a decent-looking UI <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   **Module Bundlers**
    *   These tools combine raw JavaScript files into a single bundle for browser use <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
    *   Webpack is a popular option <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
    *   Lightweight [[frontend_ui_libraries and frameworks | frameworks]] like Petite Vue may not require a module bundler <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.
*   **Mobile App Development**
    *   For mobile apps, platforms like iOS, Android, or cross-platform tools like Flutter or React Native can be used <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
    *   Ionic can wrap a web application in a web view for quick deployment to iOS and Android <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

## The Backend Layer

The [[backend_development_and_serverside_concepts | backend layer]] includes server-side runtimes and databases <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

*   **Databases**
    *   Crucial for storing user-generated data <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
    *   **NoSQL document databases:** Such as MongoDB or Firestore, are easy to learn, inexpensive, and scalable, but may struggle with complex relationships <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
    *   **Relational databases:** Including MySQL or PostgreSQL, excel at handling relationships but are less flexible and generally more expensive to operate <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. MySQL is considered a "gold standard" <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
    *   **In-memory caches:** Redis is often used as a cache to improve performance by storing data in memory rather than on disk <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
    *   Firebase provides a document database that scales without a backend server <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
*   **Server-Side Runtimes and Frameworks**
    *   Used to write code that accesses data and sends it to the frontend <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
    *   Choices often depend on the programmer's comfort language <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
    *   Examples include:
        *   Python with Flask or Django <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>
        *   Ruby on Rails <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>
        *   Laravel for PHP <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>
        *   Spring for Java <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>
        *   Node.js with frameworks like Nest (supporting TypeScript) <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>
    *   **Object-Relational Mappers (ORMs):** Tools like TypeORM help avoid writing raw SQL queries <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
    *   **Serverless options:** Firebase Cloud Functions allow writing and deploying code in Node.js, Python, or Go without managing server configurations <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   **Web Servers**
    *   Required to make the server available on the internet, such as Nginx or Apache <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   **Deployment and Infrastructure**
    *   **Containerization:** Docker standardizes the environment for code deployment by creating standard Linux environments <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
    *   **Orchestration:** Kubernetes orchestrates multiple containers as applications scale <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
    *   **Cloud Providers:** Large providers like Amazon Web Services (AWS) host infrastructure <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
    *   **Infrastructure as Code:** Terraform allows programmatic creation and versioning of infrastructure for better reliability <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
    *   **Source Code Hosting:** Platforms like GitHub host source code in the cloud <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
    *   **Continuous Integration (CI):** Tools like GitHub Actions automate testing and redeployment of code upon updates <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. For simpler projects, CI might be unnecessary <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

## APIs (Application Programming Interfaces) Layer

[[APIs and thirdparty services in web development | APIs]] are tools that connect the frontend to the backend <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. They can be custom-rolled or leverage essential third-party services <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

*   **Communication Protocols**
    *   REST (Representational State Transfer) <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
    *   GraphQL, often used with libraries like Apollo, helps build secure APIs for frontend-backend communication <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. GraphQL is more suited for complex applications with multiple APIs to stitch together <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
*   **Third-Party Services**
    *   Many services handle complex functionalities that are difficult to build from scratch <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
    *   Stripe for payment processing <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
    *   Twilio for text messaging <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
    *   SendGrid for email <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
    *   Auth0 for user authentication <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
    *   Amazon Recognition for image analysis, like content moderation <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

## Evolution of Tech Stacks

*   **LAMP Stack:** An original [[technical_details_of_the_websites_tech_stack | tech stack]] from the late 1990s, standing for Linux, Apache, MySQL, and PHP <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. It was free and open-source, leading to frameworks like WordPress and Joomla <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   **MEAN Stack:** Stands for MongoDB, Express, Angular, and Node.js. It gained popularity due to its catchy acronym <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Variations include MERN (using React) and MEVN (using Vue) <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
*   **Fancy Stack:** A custom [[technical_details_of_the_websites_tech_stack | tech stack]] consisting of Firebase, Hugo, Angular, Node, Stripe, and Express <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   **Petite Fire Stack:** Considered an easy way to build a full-stack web application, using Petite Vue for the frontend and Firebase for the backend <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

Developers can use resources like StackShare.io to see popular technologies and which companies use them <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. When choosing a [[technical_details_of_the_websites_tech_stack | tech stack]], it's important to choose wisely, as changing it later can be difficult <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. While advanced technologies like Kubernetes exist, end-users do not care about the underlying technology; they only want a good experience <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. Simple solutions can often be more effective for initial development <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.