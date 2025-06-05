---
title: Sanity as a content platform
videoId: c_8cplBi_gE
---

From: [[fireship]] <br/> 

[[content_platforms_and_their_evolution | Content platforms]] are designed to treat the content of websites and applications as data <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This approach ensures content can be managed and delivered effectively across various platforms and applications <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## Evolution of Content Platforms

Initially, websites used HTML where content was directly embedded in the code, which did not scale well <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The next generation involved [[content_platforms_and_their_evolution | Content Management Systems (CMS)]] that stored content in a database and injected it into HTML templates <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. While effective for single-channel delivery, this model became problematic when applications needed to migrate to new frameworks (e.g., JavaScript frameworks) or display content across multiple platforms (e.g., iOS, Palm OS, Android) or different views within a single application <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

These challenges led to the rise of the [[headless_cms_and_its_advantages | headless CMS]] <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. A [[headless_cms_and_its_advantages | headless CMS]] transforms content into a cloud-based API, making it accessible from any application <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Today, a [[content_platforms_and_their_evolution | content platform]] like Sanity serves as a critical layer in the modern tech stack, acting as a single source of truth for a brand <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Sanity's Role and Advantages

Sanity is a platform for structured content, designed to help users manage and deliver content in flexible ways <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. It addresses the needs of developers and content creators by providing significant advantages:

*   **Content as Data** <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>: Sanity treats content as data, enabling it to be queried and reused across various platforms (mobile, desktop, different frontends) <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. This means content can be structured and managed to fit specific needs <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
*   **Decoupled Architecture** <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>: Sanity is completely decoupled from application code and user databases, allowing content to be used with any frontend or framework <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This flexibility allows for easy redesigns or framework migrations without affecting content <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   **Customizable Schema** <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>: Unlike "cookie-cutter" solutions, Sanity allows users to model and custom-tailor content by building custom schemas with different fields (e.g., text, images) and creating relationships between items, similar to a relational database <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   **Developer-Friendly** <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>: Developers can query content from any codebase in a consistent and structured way <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **Jamstack Compatibility** <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>: Sanity is a popular choice for Jamstack applications (JavaScript, APIs, and Markup) <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
*   **Sanity Studio** <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>: It provides an open-source, React-based UI for modeling content with JavaScript and managing it in the browser <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. The studio is fully customizable <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
*   **Content Lake** <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>: The actual data is stored in a cloud-based "content lake," which can be quickly queried by frontend applications <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This provides a real-time database <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   **Portable Text** <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>: Sanity uses "portable text" to store rich text in JSON format <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. This JSON format is reusable across various platforms (mobile, desktop, different frontends) <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a> and makes passing text to applications more intuitive than HTML <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.
*   **Image Handling** <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>: Sanity allows for single image uploads that work across various aspect ratios <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>. Features like "hotspot" ensure that a specific part of an image remains in view regardless of the aspect ratio <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. It also provides image metadata, including a palette of colors present in the image and optimal foreground colors for text overlay, aiding accessibility <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.
*   **Real-time Updates** <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>: Sanity supports features like GraphQL, webhooks, and real-time updates <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **Live Collaboration** <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>: Changes made in a local Sanity Studio instance are reflected instantly in a deployed version, and vice-versa, with visible indicators of who made changes and the ability to revert them <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>.

## [[setting_up_and_customizing_a_sanity_project | Setting Up a Sanity Project]]

To [[setting_up_and_customizing_a_sanity_project | set up]] a new Sanity project:

1.  Go to `sanity.io` and click "Get Started" <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
2.  Install the Sanity CLI globally using `npm install -g @sanity/cli` <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
3.  Run `sanity init` in your terminal to initialize a new project <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
4.  If prompted, log in using Google, GitHub, or email/password <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
5.  Choose to "Create new project" <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
6.  Name your project (e.g., "fireship") <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.
7.  Use the default dataset, which will be called "production" <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
8.  Select a project template (e.g., "blog" for a pre-built schema without data, or "clean project" to build schemas from scratch) <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
9.  Navigate into your project directory using `cd [project-name]` <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
10. Open the project in your code editor <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

### Project Structure and Schemas

Key files in a Sanity project include:

*   `sanity.json`: Contains the `projectId` and project name. The `projectId` is essential for connecting frontend applications to the content lake <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   `schemas` folder: Contains individual schema files (e.g., `author.js`, `category.js`, `post.js`) <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   `schema.js`: This file imports and registers all individual schema files for use in the Sanity Studio <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

Sanity uses various schema types, including `document`, `string`, `slug`, `reference`, `image`, and `number` <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>.

## [[managing_content_as_data_with_sanity | Managing Content as Data with Sanity]]

Sanity Studio provides a user-friendly interface for content management. To start the Studio locally, run `sanity start` <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. It will typically run at `localhost:3333` <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.

### Adding and Customizing Content

Users can create new document types (e.g., a "post") and populate fields such as title, slug, and author <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

*   **References**: Document types can reference other document types (e.g., a `post` referencing an `author`) <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
*   **Images**: Images can be uploaded by clicking, dragging, or pasting <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. The Studio's image editing features include cropping and "hotspot" functionality to ensure critical parts of an image remain visible across different aspect ratios <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.
*   **Portable Text Editor**: This rich text editor stores content in a JSON format, allowing for greater flexibility and reusability than traditional HTML <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
*   **Customizing the Studio**: New fields can be added to existing schemas, such as a `description` to a `title` field <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>. New schema types, like a `number` field for "time to read," can also be added <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>.
*   **Validation Rules**: Validation rules can be added to schema fields (e.g., requiring a field to be present or setting a maximum value for a number) to ensure data integrity <a class="yt-timestamp" data-t="00:20:04">[00:20:04]</a>.

### Querying Content with Vision Plugin

The Vision plugin in Sanity Studio allows developers to query content using either [[core_features_and_capabilities | Grok]] (Sanity's in-house query language) or GraphQL <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. For example, a query can fetch all metadata for an image, including its dimensions and a "palette" of colors present in the image, along with optimal foreground colors for text overlay <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.

## Deploying Sanity Studio

To deploy a Sanity Studio to the cloud:

1.  Run `sanity deploy` in the terminal <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>.
2.  Provide a unique `studio hostname` (e.g., `fireship.sanity.studio`) <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>.
3.  Once deployed, the Studio will be accessible at the specified URL, and users can be authorized to view and manage content <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>.

The deployed Studio provides a live preview feature, allowing real-time synchronization between local and cloud instances, facilitating collaborative content management <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>.

Sanity provides a robust and flexible content platform that treats content as data, allowing for extensive customization, multi-platform delivery, and efficient content management for both marketers and developers <a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>.