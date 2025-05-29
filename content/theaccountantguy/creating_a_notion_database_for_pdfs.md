---
title: Creating a Notion Database for PDFs
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

[[Setting up PDFOutput for Notion databases | PDF output]] is a tool designed to [[bulk_pdf_generation_from_notion_databases | generate PDF documents in bulk]] by using a Notion page as a template and a Notion database to supply the content that will be replaced in the template <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Setting Up Notion for PDF Generation

Before using [[connecting_notion_database_with_pdf_output | PDF output]], you need to prepare your Notion workspace by creating both a template page and a database <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

### Creating a Notion Template Page

1.  **Start a New Page**: In your Notion workspace, click on the "create a new page" icon <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This will open a blank page <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
2.  **Name the Template**: Give your template a clear name, such as "Invitation Letter Template" <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
3.  **Set Full Width**: It's recommended to put the page in full-width mode <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
4.  **Define Content with Placeholders**: Write the static content of your document. For any sections that need to be dynamically replaced by database information, define them inside curly braces `{}` <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
    *   For example, `{title}` and `{customer name}` would be placeholders for an invitation letter <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
    *   These curly-braced sections will be replaced by data from your Notion database <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

### Creating a Notion Database

1.  **Start a New Page (for Database)**: Again, click on "create a new page" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
2.  **Select Table View**: Choose "table" as the type of page <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
3.  **Name the Database**: Name your database, for instance, "Invitation Letter Database" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
4.  **Define Columns**: Create columns in your database that correspond *exactly* to the placeholder names you used in your template (without the curly braces) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
    *   For the "Invitation Letter Template," you would create columns named "title" and "customer name" <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
    *   Using the exact same naming convention is crucial for automatic mapping <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
5.  **Populate Data**: Fill your database with multiple rows, each containing unique information for the defined columns <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Each row will correspond to a separate PDF document generated.

## Connecting Notion Database with PDF Output

Once your template and database are ready in Notion, you can connect them to [[setting_up_pdfoutput_for_notion_databases | PDF output]]:

1.  **Log In to PDF Output**: Access the [[setting_up_pdfoutput_for_notion_databases | PDF output]] application <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
2.  **Add Database and Template**:
    *   You'll see sections for "notion database" and "notion template" <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
    *   Click "click here to add database" or "add template" to initiate the connection <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
3.  **Authorize Notion Access**:
    *   You will be redirected to Notion to select the pages you want to use <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
    *   Ensure the correct Notion workspace is selected <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   Select both your created database and template pages <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
    *   Click "Allow access" to authorize [[setting_up_pdfoutput_for_notion_databases | PDF output]] to fetch your Notion data <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
    *   [[setting_up_pdfoutput_for_notion_databases | PDF output]] will then sync the selected database and template <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
4.  **Define Connection Name**: Once synchronized, provide a connection name (e.g., "Invitation Letter") <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
5.  **Map Properties**:
    *   The next section displays the database properties (columns) on the left (e.g., "customer name," "title") <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   On the right, it shows the elements from your template (the text inside curly braces) <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
    *   If you followed the naming convention, [[setting_up_pdfoutput_for_notion_databases | PDF output]] will automatically map these <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
    *   If names don't match, you'll need to manually select and map each element <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
    *   Sorting, searching, and filtering options are available to help manage properties <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

## [[generating_pdf_documents_from_notion | Generating PDF Documents from Notion]]

After mapping, you can [[bulk_pdf_generation_from_notion_databases | generate your PDFs]]:

1.  **Create PDF**: Click "Create PDF" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. The tool will process your database and template to create the documents <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
2.  **Preview and Download**:
    *   Once generated, you can preview a sample PDF <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
    *   Click "Download all" to get all the individual PDF documents based on your database rows <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. For example, three rows in a database would produce three distinct PDF files <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

## Key Considerations

*   **Placeholder Text**: Always put the placeholder text elements inside curly braces `{}` in your Notion template <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   **Naming Convention**: Use the exact same naming convention for your database column names as your placeholder text in the template (e.g., `{customer name}` in template, "customer name" as column header in database) <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. This ensures automatic mapping. If names differ, manual mapping will be required <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## Managing Connections and Templates

*   **Connections Tab**: The "Connections" tab shows all previously created connections <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. Selecting an existing connection will automatically load the predefined database and template, allowing you to quickly regenerate documents without creating a new connection <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Templates Tab**: [[setting_up_pdfoutput_for_notion_databases | PDF output]] provides predefined templates for various needs (e.g., boarding passes) <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. Each template comes with a database link and a template link <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
    *   To use a predefined template, click "Start with this template," which prompts you to duplicate it to your Notion workspace <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. Remember to duplicate both the database and template files <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

By following these steps, you can effectively use Notion databases and templates with [[setting_up_pdfoutput_for_notion_databases | PDF output]] to [[using_notion_as_a_database_for_pdf_generation | generate custom PDF documents]] in bulk.