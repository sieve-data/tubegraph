---
title: Common tech stacks like LAMP MEAN and variations
videoId: Sxxw3qtb3_g
---

From: [[fireship]] <br/> 

When learning to code, it's common to have a startup idea, but before executing it, you need to [[understanding_and_choosing_a_tech_stack | choose a tech stack]] wisely, as changing it later can be difficult <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Every application is essentially a "technology sandwich" <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## What is a Tech Stack?

While there's no official definition, a [[understanding_and_choosing_a_tech_stack | tech stack]] can be broken down into three main layers:
*   **Front-end Layer** This includes tools for building the user interface on the web, often a [[popular_programming_languages_for_web_development | JavaScript]] framework, or for mobile, tools like iOS, Android, or cross-platform options like Flutter <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Backend Layer** This involves a [[backend_development_and_serverside_concepts | serverside runtime]] like [[popular_programming_languages_for_web_development | Node.js]] or [[popular_programming_languages_for_web_development | Python]], along with a [[backend_development_and_serverside_concepts | database]] to store user data <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. Cloud providers are also considered part of this layer due to potential vendor lock-in <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   **APIs** These are tools used to connect the front-end to the back-end, such as REST or GraphQL <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. They also include essential third-party services like Stripe for payments, Twilio for text messaging, and SendGrid for email, which often span both front-end and back-end categories <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## Historical and Popular Stacks

### LAMP Stack

The original [[understanding_and_choosing_a_tech_stack | tech stack]] is LAMP, which emerged in the late 1990s <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. It stands for:
*   **L**inux
*   **A**pache (a [[networking_and_web_technologies | web server]])
*   **M**ySQL
*   **P**HP ([[phps_role_in_web_development | PHP]])

LAMP was a free and open-source alternative to expensive commercial software required for web application development in the 90s, and it led to the creation of web frameworks like WordPress and Joomla <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

### MEAN Stack and Its Variations

In modern times, while building web applications is easier, [[understanding_and_choosing_a_tech_stack | tech stacks]] have become more complicated <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. Some common stacks are known by catchy acronyms, which can influence their popularity <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

*   **MEAN Stack** Stands for:
    *   **M**ongoDB
    *   **E**xpress
    *   **A**ngular
    *   **N**ode <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>

*   **Variations** Because these acronyms don't fully capture all the necessary components of a [[understanding_and_choosing_a_tech_stack | tech stack]], variations exist:
    *   **MERN** Uses React instead of Angular <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
    *   **MEVN** Uses Vue instead of Angular <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

### Other Stacks and Resources

*   The Fireship.io website uses a custom [[understanding_and_choosing_a_tech_stack | tech stack]] called **Fancy**, which stands for Firebase, Hugo, Angular, Node, Stripe, and Express <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   To explore what other successful companies use in their [[understanding_and_choosing_a_tech_stack | tech stacks]], StackShare.io can be used to see popular technologies and the companies employing them <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

## Building a "Hottest of the Hot" Tech Stack (Example)

When building an application like a new Myspace that needs user authentication, a scalable [[backend_development_and_serverside_concepts | database]], and global reach <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>, one approach is to use the [[trends_in_programming_languages_and_web_development | hottest of the hot technologies]] regardless of cost or complexity <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Front-end Layer
For a web-first application with future mobile considerations:
*   **Language:** [[popular_programming_languages_for_web_development | JavaScript]] with TypeScript for type safety <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   **UI Framework:** React, chosen for its popularity and larger developer pool, as well as easy integration with React Native for mobile apps <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **State Management:** Redux, despite its boilerplate, is a popular choice for scaling applications <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   **CSS:** Tailwind CSS for utility classes and SAS (CSS pre-processor) and PostCSS for efficient styling and production preparation <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   **Module Bundler:** Webpack, the most popular option for combining raw [[popular_programming_languages_for_web_development | JavaScript]] files into a single bundle <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

### Backend Layer
The [[backend_development_and_serverside_concepts | backend layer]] is often considered the harder part <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
*   **Database:**
    *   Initially, a NoSQL document [[backend_development_and_serverside_concepts | database]] like MongoDB or Firestore might be considered for ease of learning and scalability <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
    *   However, for complex relationships like a social graph, a relational [[backend_development_and_serverside_concepts | database]] like MySQL is often chosen as the "gold standard" <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
    *   To improve performance at scale, a second [[backend_development_and_serverside_concepts | database]] like Redis can be added as an in-memory cache <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Serverside Runtime and Framework:**
    *   Node.js as the [[backend_development_and_serverside_concepts | serverside runtime]], with Nest framework for the web application, supporting TypeScript <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
    *   An Object-Relational Mapper (ORM) like TypeORM to avoid raw SQL queries <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   **Web Server:** Nginx or Apache to make the server available on the internet <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   **Deployment & Infrastructure:**
    *   Docker for containerization to standardize the environment <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
    *   Kubernetes for orchestrating multiple containers at scale <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
    *   Cloud Provider: Amazon Web Services (AWS) for hosting <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
    *   Infrastructure as Code: Terraform to programmatically create and version infrastructure <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
*   **Source Code & CI/CD:** GitHub for source code hosting and GitHub Actions for continuous integration (CI) pipeline to automatically test and redeploy code <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

### APIs and Third-Party Services
Many complex tasks are outsourced to third-party APIs:
*   **API Communication:** GraphQL with Apollo for secure front-end to back-end communication <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   **Payments:** Stripe for handling payments <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
*   **Authentication:** Auth0 for user authentication <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
*   **Content Moderation:** Amazon Rekognition for image moderation <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Messaging:** Twilio for sending text messages <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

## [[simplifying_and_optimizing_your_tech_stack | Simplifying and Optimizing Your Tech Stack]]

A highly complicated [[understanding_and_choosing_a_tech_stack | tech stack]] is often unnecessary, especially for initial development, as end-users prioritize a good experience over the underlying technology <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. Over-engineering can be counterproductive if the application doesn't first gain traction <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

### The "Petite Fire" Stack (Example of a Simplified Approach)
Starting with a plain HTML file <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>, a simplified approach like the "Petite Fire" stack offers an easier way to build a full-stack web application:

*   **Front-end Simplification:**
    *   **JavaScript Framework:** Petite Vue, a lightweight option with Vue.js-compatible syntax that can be dropped in with a script tag, eliminating the need for a module bundler like Webpack <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.
    *   **CSS:** Bootstrap for quick, decent-looking UI <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
    *   **Mobile App:** Ionic to wrap the web application in a web view for quick deployment to iOS and Android <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

*   **Backend Simplification:**
    *   **Backend-as-a-Service:** Firebase for a document [[backend_development_and_serverside_concepts | database]] that scales without a [[backend_development_and_serverside_concepts | backend server]], and handles user authentication <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. It can be included via a script tag <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.
    *   **Serverless Functions:** Firebase Cloud Functions for writing [[backend_development_and_serverside_concepts | serverside code]] in [[popular_programming_languages_for_web_development | Node.js]], [[popular_programming_languages_for_web_development | Python]], or Go, deploying with a single command without server configuration <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. This approach scales automatically, bypassing the need for Docker, Kubernetes, or Terraform <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
*   **Reduced Complexity:** Continuous Integration is often unnecessary unless daily testing and redeployment are required <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. GraphQL is also often removed as it's better suited for complex applications with multiple APIs to stitch together <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

This [[simplifying_and_optimizing_your_tech_stack | simplified tech stack]] prioritizes ease of development and rapid deployment, making it suitable for many projects, especially at their inception.