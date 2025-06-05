---
title: Headless CMS and its advantages
videoId: c_8cplBi_gE
---

From: [[fireship]] <br/> 

A **headless CMS** is a content management system that provides content as a cloud-based API, making it accessible from any application <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. It serves as a critical layer in the modern tech stack, acting as a single source of truth for a brand <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Evolution of Content Platforms

Historically, websites began with HTML where content was directly embedded in the code, which was not scalable <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The subsequent generation of websites utilized traditional Content Management Systems (CMS), where content was stored in a database and injected into HTML templates <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

However, traditional CMS faced limitations when migrating applications to new JavaScript frameworks, displaying content on multiple operating systems (like iOS, Palm OS, and Android), or needing multiple views for the same content within a single application <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. These challenges led to the development of the headless CMS <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. This progression showcases the [[content_platforms_and_their_evolution | evolution of content platforms]] towards more flexible solutions.

## Key Advantages of Headless CMS

The decoupled nature of a headless CMS offers numerous benefits:

*   **Content as Data**
    *   Content platforms treat website or app content like data <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.
    *   This approach ensures content can be modeled and custom-tailored for any situation, allowing users to build their own schema with different fields for text and images, and create relationships between items <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
    *   It allows for full customization of how structured content appears to editors, developers, and anyone manipulating the content <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
    *   The ability to treat content as data means it can be reshaped and presented in any format <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
    *   This data-centric approach means content can be queried <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>, for example, to find all blog posts with specific elements like code blocks <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.

*   **Flexibility and Portability**
    *   Content is completely decoupled from the application code and user database, making it portable <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
    *   Developers can query content from any codebase in a consistent and structured way <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
    *   The content can be delivered however and wherever it needs to go <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
    *   This structure allows for easy redesigns of websites or trying new [[pros_and_cons_of_different_full_stack_frameworks | frameworks]] at any time <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

*   **Ownership and Management**
    *   A content platform should allow users true ownership of their content, rather than stealing it <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
    *   Incorporating a content platform early in a project saves time in the long run <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
    *   It offers a single, polished interface for marketers to manage content <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## Sanity as a Headless CMS Example

[[sanity_as_a_content_platform | Sanity]] is a platform for structured content, and a popular choice for JAMstack (JavaScript, APIs, and Markup) applications <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

Key features and capabilities of [[managing_content_as_data_with_sanity | managing content as data with Sanity]] include:

*   **Sanity Studio**: An open-source studio where content can be modeled with JavaScript and managed in the browser <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. It is built with React, allowing for full customization of the UI <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Content Lake**: Actual content data is stored in the cloud in a "content lake" <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>, which functions as a real-time database <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   **Querying Content**: Content can be quickly queried from any front-end application using its built-in CDN, supporting features like GraphQL, webhooks, and real-time updates <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
    *   **GROQ**: [[sanity_as_a_content_platform | Sanity]] uses GROQ, an in-house query language, alongside GraphQL for querying content <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.
*   **Portable Text**: Rich text content is stored in JSON format, making it reusable across various platforms like mobile, desktop, and different front-ends <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. This JSON format is more intuitive for applications like React compared to HTML, as it allows for better control and easier integration into native apps <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.
*   **Image Handling**:
    *   Images can be uploaded via file upload, drag-and-drop, or pasting from a clipboard <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.
    *   [[sanity_as_a_content_platform | Sanity]] supports uploading an image once and having it work for various aspect ratios <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.
    *   **Hotspot and Crop**: Users can define a "hotspot" to ensure a specific part of an image remains in view regardless of the aspect ratio, avoiding the need for multiple uploads for different crops <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.
    *   **Image Metadata (Palette)**: The vision plugin allows querying image metadata, including a color palette that provides dark/light muted/vibrant colors and optimal foreground colors for text overlay, improving accessibility <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.

## Sanity Project Setup and Deployment

### Getting Started
To initialize a [[sanity_as_a_content_platform | Sanity]] project:
1.  Install the [[sanity_as_a_content_platform | Sanity]] CLI globally via `npm install -g @sanity/cli` <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
2.  Run `sanity init` to start a new project <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
3.  If it's your first time, you may be prompted to log in using Google, GitHub, or email/password <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
4.  Choose to create a new project and name it <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
5.  Select the default data set (named "production") <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
6.  Choose a project template (e.g., "blog" for a pre-built schema without data, or "clean" to build schemas from scratch) <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
7.  Navigate into the project directory using `cd [project-name]` <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

### Project Structure and Schema Definition
*   **`sanity.json`**: Contains the project ID, which is essential for a front-end application (like React or Next.js) to connect to the content lake <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   **`schemas` folder**: Houses schema definition files (e.g., `author.js`, `category.js`, `post.js`) <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   **`schema.js`**: Imports and uses all individual schema files <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. When creating a new schema file, it must be imported and used here <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Schema Types**: [[sanity_as_a_content_platform | Sanity]] supports various schema types like `document`, `string`, `slug`, `reference`, `image`, and `number` <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>.
*   **Validation**: Validation rules can be added to schema fields (e.g., `required`, `min`, `max`, `lessThan`) to ensure data integrity <a class="yt-timestamp" data-t="00:20:04">[00:20:04]</a>.

### Running and Deploying the Studio
1.  Start the local studio by running `sanity start` in the project directory <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. It will typically run on `localhost:3333` <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.
2.  Deploy the studio to a unique hostname using `sanity deploy` <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>. This makes the studio accessible online <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>.
3.  **Live Preview**: The local and deployed versions of the studio can be run simultaneously, demonstrating real-time updates and changes across both environments <a class="yt-timestamp" data-t="00:22:49">[00:22:49]</a>. Changes made in one instantly appear in the other, and users can review and revert changes, with visibility on who made them <a class="yt-timestamp" data-t="00:23:09">[00:23:09]</a>.