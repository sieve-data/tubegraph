---
title: Using Notion as a template and database for PDFs
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to [[generating_pdf_documents_from_a_notion_database | generate PDF documents in bulk]] by leveraging a Notion page as a template and a Notion database to supply the content <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## How it Works

The process involves three main steps: [[setting_up_notion_templates_and_databases_for_pdf_generation | setting up Notion templates and databases]], [[connecting_notion_database_and_template_for_pdfs | connecting them to PDF Output]], and then generating the PDFs.

### 1. [[creating_templates_and_databases_in_notion | Creating Templates and Databases in Notion]]

Before using PDF Output, you must [[creating_templates_and_databases_in_notion | create a database and a template from scratch]] within your Notion workspace <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

*   **Template Creation**:
    *   Start by creating a new blank page in Notion <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
    *   Define the content for your template, such as an "invitation letter template" <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
    *   Crucially, any sections of the template that need to be replaced with data from your database must be defined inside curly braces, for example, `{title}` and `{customer name}` <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. These serve as placeholders.

*   **Database Creation**:
    *   Create a new page in Notion and select the "Table" option to create an inline database <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
    *   Define columns in this database with *exact same naming conventions* as the placeholder elements in your template <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. For instance, if your template uses `{title}` and `{customer name}`, your database should have "title" and "customer name" columns <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
    *   Populate the database with rows containing the unique information for each PDF you want to generate <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### 2. [[connecting_notion_database_and_template_for_pdfs | Connecting Notion Database and Template for PDFs]]

Once your Notion template and database are ready:

*   Log into PDF Output. You will see sections to define your Notion database and template <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
*   Click to add your database or template. This will take you to a Notion authorization screen where you select the specific Notion pages (your template and database) you wish to use <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   After granting access, PDF Output automatically fetches the selected database and template <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   Provide a connection name for your setup, e.g., "Invitation Letter" <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
*   **Property Mapping**: On the next screen, the tool automatically loads the template and database and attempts to map properties <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
    *   On the left, you'll see database properties (e.g., "customer name", "title") <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
    *   On the right, you'll see the corresponding elements mapped from the template (e.g., `{customer name}`, `{title}`) <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.
    *   If the naming doesn't exactly match, you might need to manually select and map elements <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. The tool also offers sorting and filtering options for mapping <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

### 3. [[generating_pdf_documents_with_notion | Generating PDF Documents]]

Once the mapping is confirmed:

*   Click "Create PDF" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. The tool will begin to [[creating_pdf_documents_from_notion_database | create the PDF documents]] <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   You can preview a sample PDF to ensure the output is correct <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   Click "Download All" to download all generated PDFs <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. The tool generates individual PDF documents for each row in your Notion database, with the placeholder text replaced by the corresponding database entries <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

## Important Considerations

*   **Placeholder Format**: Always enclose placeholder text elements in your Notion template within curly braces, e.g., `{customer name}` <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
*   **Naming Convention**: Use the exact same naming convention for the column names in your Notion database as the placeholder elements in your template <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. Mismatched names will require manual mapping <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

## Additional Features of PDF Output for Notion Integration

*   **Saved Connections**: Once a connection between a Notion database and template is established, it's saved. You can easily reload predefined database and template connections from the "Connections" sidebar for future use, eliminating the need to create a new connection every time <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   **Predefined Templates**: PDF Output offers predefined templates that users can duplicate directly into their Notion workspace to get started quickly <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. These templates include links to both the template page and a corresponding database <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. Users should duplicate both the template and the database files from the provided links <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
*   **Adding More Templates/Databases**: If you wish to add more Notion templates and databases after the initial setup, you can do so via the settings tab <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
*   **Page Format**: The settings tab also allows you to choose your desired page format for the generated PDFs <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

This integration of Notion as a template and database source with PDF Output streamlines the process of [[using_notion_with_pdf_output | generating PDF documents]] in bulk, allowing for efficient, data-driven document creation.