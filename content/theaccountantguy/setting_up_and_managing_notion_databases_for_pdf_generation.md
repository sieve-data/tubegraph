---
title: Setting up and managing Notion databases for PDF generation
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to [[generating_pdf_documents_using_notion_databases | generate PDF documents in bulk]] by combining a Notion page as a template and a Notion database containing elements to be replaced in the template <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Initial Setup in PDF Output

Upon logging into PDF Output, you will find sections for "Notion Database" and "Notion Template" <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. Here, you need to define the Notion database and select the specific template that will be used for PDF generation <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## [[creating_and_managing_databases_in_notion | Creating and Managing Databases in Notion]]

Before connecting Notion to PDF Output, you must first [[creating_databases_in_notion | create a database]] and a template from scratch within your Notion workspace <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

### Creating a Notion Template

1.  **Create a New Page:** In your Notion workspace, click on the "Create a new page" icon <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This will open a blank page <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
2.  **Name the Template:** Give your template a descriptive name, such as "Invitation Letter Template" <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
3.  **Set Full Width Mode:** Optionally, set the page to full width mode <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
4.  **Define Content:** Add the static content for your template <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
5.  **Add Placeholder Elements:** For sections that will be replaced by data from your database, enclose them in curly braces, e.g., `{title}` and `{customer name}` <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. These "placeholder text elements" will be automatically mapped to database properties with the exact same name <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

### [[setting_up_a_database_in_notion | Setting up a Database in Notion]]

1.  **Create a New Page (Table):** Click on "Create a new page" again <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>, and select "Table" as the database type <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
2.  **Name the Database:** Name your database, for example, "Invitation Letter Database" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
3.  **Define Columns:** Define columns (properties) that correspond exactly to the placeholder elements in your template <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. For instance, if your template has `{title}` and `{customer name}`, your database should have columns named "Title" and "Customer Name" <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
    *   **Important:** Using the exact same naming convention for columns in the database and placeholders in the template is crucial for automatic mapping <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
4.  **Populate Data:** Add rows to your database, each containing unique information for the defined columns <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. Each row will correspond to a separate PDF document <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

## [[setting_up_and_connecting_notion_database_for_pdf_creation | Setting up and Connecting Notion Database for PDF Creation]]

1.  **Add Database and Template in PDF Output:** In PDF Output, click "Click here to add database" or "add template" <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
2.  **Select Notion Account and Pages:** You will be redirected to Notion to select the workspace and the specific pages (template and database) you intend to use <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
3.  **Allow Access:** Click "Allow access" to authorize PDF Output to fetch the selected Notion database and template <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. PDF Output will then automatically sync these <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
4.  **Define Connection Name:** Once redirected back to PDF Output, confirm that your database and template are available <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. Define a connection name (e.g., "Invitation Letter") for easy future access <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

## Mapping Database Properties to Template Placeholders

After defining the connection and clicking "Next" <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>:

*   **Automatic Mapping:** PDF Output will automatically load and map database properties (left side) to corresponding template elements (right side) if their names match exactly <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   **Manual Mapping:** If there are naming differences, you will need to manually select the correct database property for each template element <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Mapping Options:** The mapping section offers sorting, searching, and filtration options to manage properties <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

## [[generating_pdf_documents_from_notion_database_rows | Generating PDF Documents from Notion Database Rows]]

1.  **Create PDF:** Once all properties are correctly mapped, click "Create PDF" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. The tool will then generate the PDF documents <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
2.  **Preview Sample:** You can click "Preview Sample" to see an example of a generated document based on one of your database rows <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
3.  **Download All:** Click "Download all" to download all generated PDFs <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. Each row from your database will result in a separate PDF file <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

## Managing Connections and Templates

*   **Saved Connections:** Once a connection is created, it saves your database and template selection <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. You can access it later from the "Connections" sidebar option to quickly regenerate documents without re-selecting everything <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   **Predefined Templates:** PDF Output also provides a library of predefined templates <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
    *   To use a predefined template, click "Start with this template" <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
    *   You will be prompted to duplicate the template and its associated database into your Notion workspace <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. Select your workspace and click "Add to private" <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
    *   Remember to duplicate both the database and the template file from the respective links provided <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

## Additional Settings

*   **Page Format:** Under the "Settings" tab, you can choose different page formats for your PDFs <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
*   **Adding More Templates/Databases:** If you need to add more templates or databases after the initial setup, go to "Settings" and click "Click here to add more templates" <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   **Feedback:** A feedback section is available to send messages directly to the developer <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.