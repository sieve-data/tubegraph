---
title: Introduction to Tech Stacks
videoId: Sxxw3qtb3_g
---

From: [[fireship]] <br/> 

When learning to code, it's common to have a startup idea, but before executing it, choosing a tech stack is crucial. This decision is significant because changing a tech stack later can be difficult <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. An application can be thought of as a "technology sandwich" <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## What is a Tech Stack?
There is no official definition for a tech stack <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>, but it can be broken down into three main layers:
1.  **Front End Layer**: Includes tools for building the user interface that end-users interact with <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. For web applications, this often means a [[javascript_fundamentals_and_practical_concepts | JavaScript]] framework, while for mobile, it might involve iOS, Android, or cross-platform tools like Flutter <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
2.  **Back End Layer**: Consists of server-side runtimes (e.g., Node.js, Python) and a database to store user-generated data <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. Cloud providers providing infrastructure (like AWS) are also considered part of this layer <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
3.  **APIs (Application Programming Interfaces)**: These are the tools used to connect the front end to the back end <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. This can include technologies like REST or GraphQL, but mostly involves essential third-party services for app functionality, such as Stripe for payments, Twilio for messaging, or SendGrid for email <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. These services often bridge both front-end and back-end categories <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

## Evolution of Tech Stacks
### The LAMP Stack
The original (OG) tech stack was LAMP, which emerged in the late 1990s <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. LAMP is an acronym for:
*   **L**inux
*   **A**pache
*   **M**ySQL
*   **P**HP <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>

In the 1990s, building a web application was more complex and often required expensive commercial software <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. LAMP offered a free and open-source alternative, which eventually led to the development of web frameworks like WordPress and Joomla <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

### Modern Complexity
While building a web application today is much easier, tech stacks have become significantly more complicated due to the vast number of companies offering development tools and services <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## [[popular_tech_stack_acronyms | Popular Tech Stack Acronyms]]
Many modern tech stacks are known by catchy acronyms, which can influence their popularity in the tech industry <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Examples include:
*   **MEAN Stack**: MongoDB, Express, Angular, Node.js <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>
*   **MERN Stack**: MongoDB, Express, React, Node.js <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>
*   **MEVN Stack**: MongoDB, Express, Vue, Node.js <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>

However, these acronyms often do not fully capture all the technologies actually needed in a comprehensive tech stack <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. Websites like StackShare.io can provide insights into the technologies used by successful companies <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

## Designing a Tech Stack
When designing a tech stack, the first question to consider is where customers will consume the application (e.g., web, iOS, Android, desktop, IoT) <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

### Example: An Over-Engineered Tech Stack
For an application like a social media platform needing user authentication and a globally scalable database, an "over-engineered" approach might involve:

*   **Front End**:
    *   **Language**: TypeScript (adds a type system to [[javascript_fundamentals_and_practical_concepts | JavaScript]] for bug catching and reliability) <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>
    *   **UI Framework**: React (chosen for its popularity and large developer pool, making it easier to hire and potentially add React Native for mobile apps) <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>
    *   **State Management**: Redux (a popular, albeit boilerplate-heavy, option for scalable applications) <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>
    *   **Styling**: Tailwind CSS (for utility classes to style quickly) <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>, with SAS (CSS pre-processor for efficient coding) <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a> and PostCSS (to purge unused styles for production) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
    *   **Module Bundler**: Webpack (to combine raw [[javascript_fundamentals_and_practical_concepts | JavaScript]] files into a single bundle for the browser) <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

*   **Back End**:
    *   **Primary Database**: MySQL (a relational database, chosen for its strength in handling relationships, despite being less flexible and potentially more expensive than NoSQL options) <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
    *   **Caching Database**: Redis (added as a second database for caching, storing data in memory for faster reads to improve performance at scale) <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
    *   **Server-side Runtime & Framework**: Node.js and Nest (for writing code to access and send data, with Nest supporting TypeScript) <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
    *   **ORM (Object Relational Mapper)**: TypeORM (to avoid writing raw SQL queries) <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
    *   **Web Server**: Nginx or Apache (to make the server available online) <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
    *   **Containerization**: Docker (to standardize the environment for code deployment) <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
    *   **Container Orchestration**: Kubernetes (for orchestrating multiple containers as the app scales) <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
    *   **Cloud Provider**: Amazon Web Services (AWS) (to host infrastructure, chosen for its complexity) <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
    *   **Infrastructure as Code**: Terraform (to programmatically create and version infrastructure for reliability) <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
    *   **Source Code Hosting & CI**: GitHub and GitHub Actions (for hosting source code and setting up continuous integration pipelines for automated testing and deployment) <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

*   **APIs & Third-Party Services**:
    *   **API Protocol**: GraphQL with Apollo (for secure front-end to back-end communication) <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
    *   **Payments**: Stripe (for collecting payments via SDKs) <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
    *   **User Authentication**: Auth0 (for handling user authentication) <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
    *   **Content Moderation**: Amazon Rekognition (for deep learning content detection) <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
    *   **Messaging**: Twilio (for sending text messages) <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

### Example: A Simplified Tech Stack (Petite Fire Stack)
Users don't care what technology is used; they care about a good experience <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. An overly complex stack can be counterproductive if the application doesn't first achieve market traction <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. A more practical approach might be:

*   **Front End**:
    *   **UI Framework**: Petite Vue (a lightweight option compatible with Vue.js syntax, easily dropped in with a script tag, eliminating the need for a module bundler like Webpack) <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.
    *   **Styling**: Bootstrap (a quick way to achieve a decent-looking UI, though more "cookie cutter" than Tailwind) <a class="yt-timestamp" data-t="00:09:58">[00:10:00]</a>.
    *   **Mobile App Development**: Ionic (to wrap the web application in a web view for quick deployment to iOS and Android) <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

*   **Back End & Services**:
    *   **Backend as a Service**: Firebase (provides a scalable document database without needing a backend server, handles user authentication, and can be included via a script tag) <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
    *   **Serverless Functions**: Firebase Cloud Functions (for server-side code, allowing development in Node.js, Python, or Go, and automatic scaling without worrying about server configuration, Docker, Kubernetes, or Terraform) <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
    *   **Continuous Integration**: Initially forgo CI unless daily testing and redeploying becomes necessary <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
    *   **APIs**: Avoid GraphQL initially if the app is not complex or does not need to stitch together multiple APIs <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

This simplified approach, known as the "Petite Fire Stack," can be a very easy way to build a [[pros_and_cons_of_different_full_stack_frameworks | full stack web application]] <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.