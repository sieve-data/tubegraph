---
title: Managing content as data with Sanity
videoId: c_8cplBi_gE
---

From: [[fireship]] <br/> 

## Understanding Content Platforms

[[content_platforms_and_their_evolution | Content platforms]] treat website or app content as data <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

Historically:
*   **Early HTML websites** <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>: Content was directly embedded in code, which did not scale well <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.
*   **Content Management Systems (CMS)** <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>: Content was stored in a database and injected into HTML templates <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. This approach faced challenges when migrating to new frameworks or displaying content across multiple platforms (iOS, Palm OS, Android) or different views within a single application <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   **Headless CMS** <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>: Arose to meet these demands by turning content into a cloud-based API, accessible from any application <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

Today, a content platform is a critical layer of the modern tech stack, serving as a single source of truth for a brand <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Because it is decoupled from application code and user databases, content can be taken anywhere <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

### Benefits of Content Platforms

[[content_platforms_and_their_evolution | Content platforms]] allow users to model and custom-tailor content for any situation, rather than starting with a generic solution <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. You can build your own [[the_role_of_metadata_and_schema_in_seo | schema]] with different fields (e.g., text, images) and create relationships between items, similar to a relational database <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

*   **For Marketers**: Provides a single, polished interface for content management <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
*   **For Developers**: Enables querying content from any codebase in a consistent and structured way <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

A content platform should allow freedom and ownership over content <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. It should facilitate content delivery wherever and however needed, and allow structuring and management to fit specific needs <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

## [[sanity_as_a_content_platform | Sanity]] as a Content Platform

[[sanity_as_a_content_platform | Sanity]] is a popular choice for Jamstack applications, which stands for JavaScript, APIs, and Markup <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. [[sanity_as_a_content_platform | Sanity]] provides the API layer within the Jamstack <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

### Key Components and Features

*   **Open-source Studio**: Allows content modeling with JavaScript and management in the browser <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   **Content Lake**: Cloud-based storage for the actual data, which can be queried from a front-end application <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   **CDN**: Built-in Content Delivery Network for fast content retrieval <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
*   **Support for GraphQL, Webhooks, and Real-time Updates** <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **Structured Content**: [[sanity_as_a_content_platform | Sanity]] is a platform for structured content, helping manage and deliver content in advanced ways <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Sanity Studio (Backend UI)**: Built with React, fully customizable, allowing users to structure content as needed <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Portable Text**: Stores rich text in JSON format, making it reusable across various platforms (mobile, desktop, different frontends) <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. This overcomes challenges of embedding HTML into modern frameworks like React <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.
*   **Real-time Database**: Using [[sanity_as_a_content_platform | Sanity]] and the content lake provides a real-time database for content access <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Redesign Flexibility**: Structured content allows for website redesigns or trying new frameworks at any time, as content is separate <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

Content can be diverse, ranging from blog content, portfolio pieces, video content for courses, restaurant menus, car manufacturer data, music tracks, or sporting event results <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Incorporating a content platform from the start saves time and ensures content is managed effectively <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

## [[setting_up_and_customizing_a_sanity_project | Setting up and Customizing a Sanity Project]]

To get started with [[sanity_as_a_content_platform | Sanity]]:

1.  **Install the Sanity CLI globally**:
    ```bash
    npm install -g @sanity/cli
    ```
    <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>
2.  **Initialize a new Sanity project**:
    ```bash
    sanity init
    ```
    <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>
    *   You may be prompted to log in using Google, GitHub, or email/password <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
    *   Choose to create a new project <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
    *   Name your project (e.g., "fireship") <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
    *   Use the default dataset (named "production") <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
    *   Select a project template: `movie`, `e-commerce`, `blog`, or `clean project` <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. The `blog` template comes with pre-built schemas but no data <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.

3.  **Navigate into your project directory**:
    ```bash
    cd your-project-name
    ```
    <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>
4.  **Open in your text editor** (e.g., VS Code):
    ```bash
    code .
    ```
    <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>

### Project File Structure

*   **`sanity.json`**: Contains the project ID and name <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. The `projectId` is essential for connecting front-end applications to your content lake <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **`schemas` folder**: Stores your content schemas. For a clean project, this folder would be nearly empty <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
*   **`schema.js`**: Imports and registers all your individual [[the_role_of_metadata_and_schema_in_seo | schema]] files (e.g., `blockContent`, `category`, `post`, `author`) <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. Any new [[the_role_of_metadata_and_schema_in_seo | schema]] file must be imported and used here <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Document Types**: [[sanity_as_a_content_platform | Sanity]] uses [[the_role_of_metadata_and_schema_in_seo | schema]] types, with `document` being one of them. Other types include `string`, `slug`, `reference`, and `image` <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

### Running Sanity Studio Locally

To start the local development server for [[sanity_as_a_content_platform | Sanity]] Studio:
```bash
sanity start
```
<a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>
The studio will run at `localhost:3333` <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. You will need to log in again using the same method chosen during `sanity init` <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. Additional users can be granted access via `manage.sanity.io` <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

### Working with Content in Sanity Studio

The Studio interface allows managing content, searching, and provides access to plugins like Vision <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. Document types like 'post', 'author', and 'category' are displayed <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.

#### Creating a New Post
When creating a new post:
*   **Title**: E.g., "My First Blog Post" <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
*   **Slug**: Can be generated automatically from the title <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.
*   **Author**: A `reference` type that points to an 'author' document. An author must exist in the 'Author' document type to be selectable <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   **Main Image**:
    *   Images can be uploaded from your computer, drag-and-dropped, or pasted from the clipboard <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.
    *   **Hotspot and Cropping**: [[sanity_as_a_content_platform | Sanity]] allows uploading an image once and automatically adapting it for various aspect ratios <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. Hotspot ensures that a specific part of the image (e.g., a cat's nose) always remains in view regardless of the aspect ratio <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. This eliminates the need for multiple uploads for different crops <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>.
*   **Categories**: Field for assigning categories to the post <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.
*   **Body (Portable Text)**: This is a rich text editor where Portable Text lives <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. Portable Text stores rich text content in JSON format, making it highly flexible and reusable across different platforms (mobile, desktop, various front-end frameworks like React or Vue) <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. Because it's stored as data, you can query for specific content, such as all blog posts containing code blocks <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.

#### Inspecting Content as JSON

Every piece of content in [[sanity_as_a_content_platform | Sanity]] can be inspected to view its underlying JSON structure <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>. This JSON includes fields like `mainImage`, `title`, and all rich text content, demonstrating how content is stored as queryable data <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>.

#### Customizing Schema and Fields

You can customize the [[sanity_as_a_content_platform | Sanity]] Studio by adding new fields to existing schemas or creating entirely new [[the_role_of_metadata_and_schema_in_seo | schema]] types.

*   **Adding a Description Field**: To add a `description` field to a `post` schema in `post.js`:
    ```javascript
    {
      name: 'description',
      type: 'string',
      title: 'Description',
      description: 'Keep titles short and sweet :)'
    }
    ```
    <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>
*   **Adding a Number Field with Validation**: To add a `timeToRead` number field and enforce a maximum value:
    ```javascript
    {
      name: 'timeToRead',
      title: 'Time to Read',
      type: 'number',
      validation: Rule => Rule.required().lessThan(20) // Example validation
    }
    ```
    <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>
    This demonstrates how to add validation rules (e.g., `required`, `lessThan`) to ensure data integrity <a class="yt-timestamp" data-t="00:20:03">[00:20:03]</a>.

## Sanity Vision Plugin and GROQ

The Vision plugin allows querying content directly within the [[sanity_as_a_content_platform | Sanity]] Studio <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. You can use either GraphQL or GROQ (Graph-Relational Object Queries), an in-house [[sanity_as_a_content_platform | Sanity]] query language <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.

Example GROQ query to retrieve image metadata:
```groq
*[_id == "image-id-here"]
```
<a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>
This query returns all data for a specific image, including its metadata <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.

### Image Palette Metadata

Under the image's `metadata`, you can find a `palette` object <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. This palette provides details on the colors present in the image, such as:
*   `darkMuted`
*   `darkVibrant`
*   `lightVibrant`
*   `muted`
*   The percentage of the image each color occupies <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>.
*   An `optimalForeground` color for each, suggesting a good text color to place over that part of the image for accessibility <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.

This feature allows developers to programmatically use optimal colors based on image content <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>.

## Deploying Sanity Studio

To deploy your [[sanity_as_a_content_platform | Sanity]] Studio, run the command:
```bash
sanity deploy
```
<a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>
You will need to provide a unique `studio hostname` (e.g., `fireship`). Once deployed, your studio will be accessible at a unique URL like `yourhostname.sanity.studio` <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>.

### Live Preview and Collaboration

A powerful feature of [[sanity_as_a_content_platform | Sanity]] is its live preview capability. When changes are made in a local studio instance, they are instantly reflected in the deployed version, and vice-versa <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>. This real-time synchronization allows for collaborative editing, showing who made changes and providing options to review or revert them <a class="yt-timestamp" data-t="00:23:07">[00:23:07]</a>.

This setup provides a content lake that can be queried, with all content available as JSON and usable across various platforms without limitations <a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>.