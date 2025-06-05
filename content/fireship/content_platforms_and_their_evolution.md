---
title: Content platforms and their evolution
videoId: c_8cplBi_gE
---

From: [[fireship]] <br/> 

Content platforms treat the content on a website or application like data <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Evolution of Content Management Systems (CMS)

In the early days of the web, content was directly embedded in HTML code <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This approach did not scale well <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

The next generation of websites introduced Content Management Systems (CMS), where content is stored in a database and then injected into an HTML template <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This method worked effectively until developers needed to migrate their applications to new [[javascript_frameworks_and_their_updates | JavaScript frameworks]], display the same content across platforms like iOS, Palm OS, and Android, or manage multiple views for content within a single application <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Rise of Headless CMS

These evolving demands led to the emergence of the [[headless_cms_and_its_advantages | headless CMS]] <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. A [[headless_cms_and_its_advantages | headless CMS]] transforms content into a cloud-based API, making it accessible from any application <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

### The Modern Content Platform

Today, a content platform is a vital component of the modern tech stack, serving as a single source of truth for a brand <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Since it is completely decoupled from application code and user databases, content can be easily migrated and reused <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

Key advantages of modern content platforms include:
*   **Custom Content Modeling** The ability to model and tailor content for any situation, building custom schemas with different fields (e.g., text, images) and creating relationships between items similar to a relational database <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   **Benefits for Users** Marketers gain a single, polished interface for content management <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>, while developers can query content from any codebase in a consistent and structured manner <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## [[sanity_as_a_content_platform | Sanity.io]] as a Content Platform

[[sanity_as_a_content_platform | Sanity]] is a popular choice for Jamstack applications, which stands for JavaScript, APIs, and Markup <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. It provides an open-source studio for modeling content with JavaScript and managing it in the browser <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. The content data itself is stored in the cloud within a "content lake," which can be quickly queried from front-end applications via its built-in CDN, also supporting features like GraphQL, webhooks, and real-time updates <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

[[sanity_as_a_content_platform | Sanity]] focuses on structured content, enabling users to manage and deliver content in flexible ways <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Content can encompass various types, including:
*   Blog or portfolio content <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>
*   Video content for course platforms <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>
*   Restaurant menus, hours, and addresses <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>
*   Car manufacturer data (e.g., cars made, sent out, purchased) <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>
*   Music tracks for artists <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>
*   Sporting event times and winners for tournaments <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>

Incorporating a content platform from the beginning can save time in the long run <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### Benefits of Using a Content Platform like [[sanity_as_a_content_platform | Sanity]]

A content platform should provide freedom with content, ensuring true ownership is maintained and allowing content to be delivered wherever and however needed <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. Content should also be structurable and manageable to best fit user needs <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

Key features and benefits exemplified by [[sanity_as_a_content_platform | Sanity]]:

*   **Sanity Studio (Backend UI)**
    *   Built with React, the studio is fully customizable, allowing users to structure content as needed <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
    *   **Portable Text** This feature stores rich text content in JSON format <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. This JSON format enables content reuse across various platforms such as mobile, desktop, and different front-ends, making it more intuitive to pass content to frameworks like React or Vue compared to traditional HTML <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
    *   Treating content as data opens up nearly endless possibilities for where data can go and what it can do <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
    *   Allows full customization of how structured content appears to editors, developers, and anyone manipulating it <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
    *   Provides the ability to reshape and present content in any format <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
    *   Offers a real-time database via the content lake, providing access to content anywhere it's needed <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
    *   Enables easy website redesigns or experimentation with new [[javascript_frameworks_and_their_updates | JavaScript frameworks]] without impacting content <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

### Setting Up a [[sanity_as_a_content_platform | Sanity]] Project

A [[sanity_as_a_content_platform | Sanity]] project can be set up quickly:
1.  Install the [[sanity_as_a_content_platform | Sanity]] CLI globally via npm <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
2.  Run `sanity init` to start a new project, which may prompt for a login (Google, GitHub, or email/password) <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
3.  Choose to create a new project and assign it a name <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
4.  Confirm the use of the default 'production' dataset <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
5.  Select a project template (e.g., movie, e-commerce, blog, or clean project) <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. Pre-built schemas come with templates, while a clean project allows for custom schema building <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
6.  Navigate into the project directory and open it in a text editor <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

#### Project Structure and Schemas

*   **`sanity.json`**: Contains the project ID, essential for connecting front-end applications (e.g., React, Next.js) to the content lake <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   **`schemas` folder**: Houses schema files (e.g., `author.js`, `category.js`, `post.js`) <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   **`schema.js`**: Imports and uses all schema files, acting as a central registry for document types <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

#### Customizing the Studio

Users can customize the [[sanity_as_a_content_platform | Sanity]] Studio by adding new fields to existing schemas or creating entirely new schema types <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>. Validation rules can be applied to fields (e.g., requiring a field, setting maximum values for numbers) to ensure data integrity <a class="yt-timestamp" data-t="00:20:03">[00:20:03]</a>.

### Managing Content and Media

*   **Sanity Studio UI**: After running `sanity start`, the studio becomes accessible locally (e.g., `localhost:3333`) <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>. Users log in with their chosen method and can add other authorized users via `manage.sanity.io` <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
*   **Document Types**: The studio displays defined document types (e.g., Post, Author, Category) <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
*   **References**: Fields can reference other document types (e.g., a "post" referencing an "author") <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
*   **[[integration_of_media_in_mobile_applications | Image Management]]**: Images can be uploaded by dragging and dropping, pasting, or selecting from a local file system <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. [[sanity_as_a_content_platform | Sanity]] allows for single image uploads that work across various aspect ratios <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. The "hotspot" feature ensures a specified area of an image remains in view regardless of the crop or aspect ratio, optimizing for different displays without multiple uploads <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.
*   **Rich Text Editor and Portable Text**: The rich text editor houses Portable Text, [[sanity_as_a_content_platform | Sanity]]'s method of storing rich text <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. This content is saved in a JSON format, allowing it to be easily queried (e.g., finding all blog posts with code blocks) and used across different front-ends like React, Vue, or native apps <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.
*   **Inspecting Content (JSON)**: The raw JSON data for any piece of content, including images and rich text, can be inspected directly in the studio <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
*   **Vision Plugin and Groq**: The Vision plugin allows users to query their content using Groq, [[sanity_as_a_content_platform | Sanity]]'s in-house query language, or GraphQL <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>. This enables powerful data retrieval, such as extracting metadata from images, including dimensions and color palettes, which can be used for accessibility (e.g., determining optimal foreground colors for text overlays) <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.

### Deploying and Live Preview

To deploy the [[sanity_as_a_content_platform | Sanity]] Studio, run `sanity deploy` in the terminal <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>. A unique studio hostname must be chosen <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>. Once deployed, the studio lives at a unique URL (e.g., `yourname.sanity.studio`) <a class="yt-timestamp" data-t="00:22:08">[00:22:08]</a>.

A notable feature is the live preview, where changes made in the local studio are instantly reflected in the deployed version, and vice-versa <a class="yt-timestamp" data-t="00:22:49">[00:22:49]</a>. This real-time synchronization includes the ability to see who made changes and revert them from either interface <a class="yt-timestamp" data-t="00:23:10">[00:23:10]</a>.

With a content lake up and running, JSON content can be queried and used across all platforms, ensuring content is not limited to any single application <a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>.