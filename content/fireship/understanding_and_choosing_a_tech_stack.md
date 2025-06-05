---
title: Understanding and choosing a tech stack
videoId: Sxxw3qtb3_g
---

From: [[fireship]] <br/> 

When learning to code, it's common to have an idea for a startup, but before execution, one must [[choosing_the_right_technology_stack_and_tools_for_productivity | choose a tech stack]] wisely, as changing it later can be difficult <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Every application can be visualized as a "technology sandwich" <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## What is a Tech Stack?

While there's no official definition, a [[technical_details_of_the_websites_tech_stack | tech stack]] can be broken down into three main parts:
1.  **Front-end Layer** <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>: Includes tools for building the user interface that the end-user interacts with <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. For web applications, this typically involves a [[choosing_the_right_javascript_framework_for_your_project | JavaScript framework]] <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>, while for mobile, it might be iOS, Android, or cross-platform tools like Flutter <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
2.  **Back-end Layer** <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>: Comprises a server-side runtime (e.g., Node.js, Python) and a database for storing user-generated data <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Infrastructure purchased from cloud providers can also be considered part of this layer <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
3.  **APIs (Application Programming Interfaces)** <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>: Tools used to connect the front-end to the back-end <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. This can include self-rolled solutions like REST or GraphQL, but often involves essential third-party services like Stripe for payments, Twilio for text messaging, or SendGrid for email <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. These tools can span both front-end and back-end categories <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

## Common Tech Stacks

In the late 1990s, the [[common_tech_stacks_like_lamp_mean_and_variations | OG Tech stack]] was LAMP, standing for Linux, Apache, MySQL, and PHP <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. LAMP was free and open-source, leading to web frameworks like WordPress and Joomla <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. While web application development is easier today, [[technical_details_of_the_websites_tech_stack | tech stacks]] have become more complex due to the multitude of available tools <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

Other [[common_tech_stacks_like_lamp_mean_and_variations | common tech stacks]] often have catchy acronyms <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>:
*   **MEAN**: MongoDB, Express, Angular, and Node <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Its popularity stemmed from its catchy acronym <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   **MERN**: A variation of MEAN that uses [[features_and_trade_offs_of_react_angular_and_vue | React]] instead of Angular <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
*   **MEVN**: Another variation that uses [[features_and_trade_offs_of_react_angular_and_vue | Vue]] instead of Angular <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

These acronyms often don't fully capture all the necessary components of a [[technical_details_of_the_websites_tech_stack | tech stack]] <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. For insights into what successful companies use, websites like StackShare.io can be helpful <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

## Architecting a Complex Tech Stack (Over-Engineered Example)

When architecting a [[technical_details_of_the_websites_tech_stack | tech stack]] for a scalable application like a social media platform, one might initially choose the "hottest" technologies regardless of cost or complexity <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### Front-end Layer <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>
The primary question is where customers will consume the application (web, iOS, Android, etc.) <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. For web applications, the [[choosing_the_right_programming_language | programming language]] is almost always JavaScript <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

*   **Language**: TypeScript, which adds a type system on top of JavaScript for earlier bug detection and more reliable code <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
*   **UI Framework**: [[features_and_trade_offs_of_react_angular_and_vue | React]], chosen for its popularity and larger developer pool, as well as the ability to easily add React Native for mobile apps <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. Building complex UIs with vanilla JavaScript is difficult <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **State Management**: Redux, a popular option for scalable apps, though it can involve more boilerplate code <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   **Styling**:
    *   Tailwind CSS: Provides utility classes for quick styling <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
    *   SAS (CSS pre-processor): Offers extra syntax for efficient code writing <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
    *   PostCSS: Used to purge unused styles and prepare CSS for production <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Module Bundler**: Webpack, to combine raw JavaScript files into a single bundle for the browser <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

### Back-end Layer <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>
The database is a crucial decision for user-generated data <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

*   **Database**:
    *   MySQL: A relational database chosen as the "gold standard" for handling relationships, despite being less flexible and generally more expensive than NoSQL <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
    *   Redis: Added as a second database for caching, storing data in memory for faster reads <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Server-Side Runtime**: Node.js, chosen as the runtime for JavaScript developers <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
*   **Server-Side Framework**: Nest, a framework that supports TypeScript out-of-the-box for handling server-side web applications <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   **Object Relational Mapper (ORM)**: TypeORM, to avoid writing raw SQL queries <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   **Web Server**: Nginx or Apache, to make the server available online <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   **Containerization**: Docker, to standardize the environment for code deployment <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
*   **Orchestration**: Kubernetes, for orchestrating multiple containers as the app scales <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
*   **Cloud Provider**: Amazon Web Services (AWS), for hosting infrastructure <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   **Infrastructure as Code**: Terraform, to programmatically create and version infrastructure for better reliability <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
*   **Source Code Hosting**: GitHub, for hosting source code in the cloud <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   **Continuous Integration**: GitHub Actions, to automatically test and redeploy code upon updates <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

### APIs and Third-Party Services <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>
For functions too complex to handle from scratch, APIs and third-party services are integrated:
*   **API Protocol**: GraphQL with Apollo library, to build an API for secure communication between front-end and back-end <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
*   **Payments**: Stripe, providing SDKs for server and front-end to collect payments <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **User Authentication**: Auth0 <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
*   **Content Moderation**: Amazon Rekognition, for deep learning-based content detection <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Messaging**: Twilio, for sending text messages <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

## Simplifying the Tech Stack <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>
An overly complicated [[technical_details_of_the_websites_tech_stack | tech stack]] is often unnecessary, as end-users prioritize a good experience over the underlying technology <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. Initial focus should be on building a good experience, rather than over-engineering for scale that may never be reached <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

To [[simplifying_and_optimizing_your_tech_stack | simplify]], one can start with a basic HTML file <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

### Simplified Front-end
*   **UI Framework**: Petite-Vue, a lightweight option compatible with [[features_and_trade_offs_of_react_angular_and_vue | Vue.js]] syntax, which can be included via a script tag, eliminating the need for a module bundler like Webpack <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Styling**: Bootstrap, a quick way to achieve a decent-looking UI <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   **Mobile App Wrapper**: Ionic, to wrap the web application in a web view for quick deployment to iOS and Android <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

### Simplified Back-end
*   **Backend as a Service**: Firebase, which provides a document database that scales without a dedicated backend server <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. It also handles user authentication and can be included with a script tag <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
*   **Serverless Functions**: Firebase Cloud Functions, a serverless option for writing server-side code in Node.js, Python, or Go, deploying with a single command without server configuration <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. It scales automatically, removing the need for Docker, Kubernetes, or Terraform <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
*   **Continuous Integration**: Initially, this can be omitted unless daily testing and redeploying are necessary <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   **API Protocol**: GraphQL can be removed if the app is less complex and doesn't involve stitching together multiple APIs <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

This simplified approach leads to the "Petite Fire stack," which is presented as an easy way to build a full-stack web application <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.