---
title: Setting up and customizing a Sanity project
videoId: c_8cplBi_gE
---

From: [[fireship]] <br/> 

A content platform treats the content on your website or application like data <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Initially, HTML websites embedded content directly into the code, which did not scale well <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The next generation used Content Management Systems (CMS) where content was stored in a database and injected into HTML templates <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. However, this approach faced challenges when migrating to new JavaScript frameworks or displaying content across multiple platforms (iOS, Palm OS, Android) <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

This led to the rise of the headless CMS, a tool that transforms your content into a cloud-based API, accessible from any application <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. Today, a content platform is a crucial layer in the modern tech stack, serving as a single source of truth for a brand <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Because it is decoupled from application code and user databases, content can be taken anywhere <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. It also allows for modeling and custom tailoring content for any situation, building a schema with different fields for text, images, and relationships between items <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

Developers benefit significantly as they can [[managing_content_as_data_with_sanity | query content]] from any codebase in a consistent and structured manner <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## What is Sanity?

Sanity is a popular choice for Jamstack applications, which stands for JavaScript, APIs, and Markup <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. [[sanity_as_a_content_platform | Sanity]] is a platform for structured content, helping you manage and deliver content in flexible ways <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Content can encompass a wide range of data, from blog posts and portfolios to video content, restaurant menus, car manufacturing statistics, music tracks, or sporting event results <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

A content platform should offer freedom with your content, allowing you to own, deliver, structure, and manage it as needed <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. Content should be treated as data, making it reusable across mobile, desktop, and different front-end frameworks <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. Using structured content allows you to redesign your website or try new frameworks at any time <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

## Setting Up a Sanity Project

To get a Sanity project up and running:

1.  **Install Sanity CLI Globally**: Open your terminal and run `npm install -g @sanity/cli` <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
2.  **Initialize a New Project**: Run the command `sanity init` <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
    *   If you haven't logged in to Sanity on your local machine, you will be prompted to log in using Google, GitHub, or email/password <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. Remember your choice for future logins <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
3.  **Create New Project**: Select "Create new project" <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
4.  **Name Your Project**: Provide a name for your Sanity project <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.
5.  **Choose Dataset**: Use the default dataset (named "production") by typing `y` <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
6.  **Confirm Path**: Confirm the project path <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
7.  **Select Starter Schema**: Choose from options like "movie," "e-commerce," "blog," or "clean project" <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. The "blog" option provides a pre-built schema with no data, while "clean" has nothing, requiring you to build your own schemas <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
8.  **Navigate to Project Directory**: `cd` into your new Sanity project folder <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
9.  **Open in Text Editor**: Open the project in your preferred text editor, e.g., `code .` for VS Code <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
10. **Start Sanity Studio**: In your terminal within the project, run `sanity start` <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
11. **Access Studio**: The studio will live at `localhost:3333` <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. You will need to log in again using the same method chosen during initialization <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.

## Sanity Studio Overview

The Sanity Studio provides a backend UI for managing content <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

*   **File Structure**:
    *   `sanity.json`: Contains your `projectId` and the project name <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. The `projectId` is essential for connecting front-end applications to your content lake <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
    *   `schemas` folder: Houses your schema files (e.g., `author.js`, `category.js`, `post.js`) <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. `schema.js` is where all individual schema files are imported and used <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

*   **Document Types**: Sanity uses schema types, with `document` being one of them <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. Other types include `string`, `slug`, `reference`, and `image` <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. Document types have an array of fields <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.

## Customizing Sanity Content

### Adding Content and References

You can add new documents like "post" or "author" directly in the Sanity Studio <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. When creating a "post," you can reference an "author" document, ensuring consistency and relationships between content items <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

### Image Handling

Sanity offers flexible image uploading and manipulation:

*   **Upload Methods**: Images can be uploaded by clicking the upload button, dragging and dropping, or pasting directly into the field <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.
*   **Cropping and Hotspot**: The "edit details" feature allows for cropping and setting a "hotspot" <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>. The hotspot ensures that a specific part of the image always remains in view, regardless of the aspect ratio the image is displayed in <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. This means you upload an image once, and it works across all aspect ratios <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>.
*   **Image Metadata and Palette**: Using the Vision plugin (accessed via the three dots -> inspect), you can query an image's ID to retrieve its metadata, including dimensions and a color palette <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>. The palette provides colors (e.g., dark muted, light vibrant) present in the image and an optimal foreground color for text, which is great for accessibility <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. Queries can be made using Grok, Sanity's in-house query language, or GraphQL <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.

### Portable Text

Portable Text is Sanity's method of storing rich text in JSON format <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.

*   **JSON Format**: Rich text, like a blog post body, is stored as JSON data <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.
*   **Flexibility**: Unlike embedding HTML into applications which can be unintuitive and lead to loss of control, Portable Text's JSON format makes it intuitive to pass along and reuse across mobile, desktop, React, View, or native applications <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.
*   **Querying**: Because it's stored as data, you can query for content within Portable Text, such as finding all blog posts that contain code blocks <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.

### Adding Custom Fields and Validation

You can customize your studio by adding new fields and schema types:

1.  **Add a Simple Field**: In your schema file (e.g., `post.js`), add a new field object. For example, add a `description` field of type `string` below the `title` field <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>.

    ```javascript
    {
      name: 'description',
      title: 'Description',
      type: 'string',
      description: 'Keep titles short and sweet :)'
    },
    ```

    This will add a new input field to your document in the studio <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>.

2.  **Add a New Schema Type with Validation**:
    *   Find the schema type you want in the Sanity documentation (e.g., `number`) <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>.
    *   Copy the example schema for a number type and paste it into your document's fields array <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>.
    *   Customize the `name`, `title`, and `type`. For example, create a "Time to read" field of type `number` <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>.
    *   Add validation rules. For instance, to ensure the "Time to read" is required and less than 20 minutes, add a `validation` property to the field: <a class="yt-timestamp" data-t="00:20:04">[00:20:04]</a>.

    ```javascript
    {
      name: 'timeToRead',
      title: 'Time to read',
      type: 'number',
      validation: Rule => Rule.required().max(20) // For less than 20. Use lessThan(21) if 20 should be included.
    },
    ```

    This will show a warning in the studio if the number exceeds the specified limit <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>.

## Deploying the Sanity Studio

To deploy your Sanity Studio:

1.  **Run Deploy Command**: In your terminal, run `sanity deploy` <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>.
2.  **Choose Unique Hostname**: Provide a unique hostname for your studio <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>. This name will become part of your public studio URL (e.g., `yourname.sanity.studio`) <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>.
3.  **Access Deployed Studio**: Once deployed, your studio will be accessible at the unique URL you provided <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>. Only authorized users can view it <a class="yt-timestamp" data-t="00:22:14">[00:22:14]</a>. You can manage user authorizations at `manage.sanity.io` <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

## Live Preview and Collaboration

Sanity Studio offers live preview capabilities:

*   **Real-time Sync**: Changes made in your local Sanity Studio are instantly reflected in your deployed version, and vice versa <a class="yt-timestamp" data-t="00:22:52">[00:22:52]</a>.
*   **Change Tracking**: Little pencils appear, indicating a change <a class="yt-timestamp" data-t="00:23:10">[00:23:10]</a>. Clicking on them shows who made the change, and you can review and revert changes from either side <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>. Publishing a document on one side will publish it on both <a class="yt-timestamp" data-t="00:23:39">[00:23:39]</a>.

With your own content lake up and running, you can now [[managing_content_as_data_with_sanity | query against]] the JSON data of your content, which can be used across all platforms without limitations <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>.