---
title: Creating templates and databases in Notion for PDF generation
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to [[generating_pdfs_in_bulk_with_notion | generate PDF documents in bulk]] by using a Notion page as a template and a Notion database to hold the elements for replacement within that template <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Setting Up Notion for PDF Generation

To begin [[generating_professional_invoice_pdfs_using_notion | professional invoice PDFs using Notion]], or any other PDF, you need to [[setting_up_notion_templates_and_databases_for_invoices | set up Notion templates and databases for invoices]] first <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. This involves [[creating_templates_and_databases_in_notion | creating templates and databases in Notion]] from scratch <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

### Creating a Notion Template Page

1.  Navigate to your Notion dashboard or workspace <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
2.  Click on the "Create a new page" icon on the left sidebar <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
3.  Give the new page a title, such as "Invitation Letter Template" <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
4.  Set the page to "full width mode" for better visibility <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
5.  Define the content for your template <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
6.  For sections that will be replaced by data from a database, enclose them in curly braces (e.g., `{title}` and `{customer name}`) <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. These "placeholder text elements" are crucial for mapping data <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

### Creating a Notion Database

1.  Click on "Create a new page" again <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
2.  Select "Table" to [[creating_a_database_in_notion | create a database in Notion]] <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
3.  Name your database, for example, "Invitation Letter Database" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
4.  Define column names in the database that **exactly match** the placeholder names used in your template (e.g., `title` and `customer name`) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This exact naming convention is vital for automatic mapping <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
5.  Populate the database with rows of unique information for each PDF you want to generate <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

## Connecting Notion to PDF Output

After [[setting_up_and_using_databases_in_notion | setting up and using databases in Notion]] and templates, you can connect them to the PDF Output tool:

1.  Log into PDF Output <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
2.  In the Notion Database section, click "click here to add database" (or similar for the Notion Template section) <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
3.  You will be redirected to Notion to select the pages you want to use <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
4.  Ensure you select the correct Notion account/workspace <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
5.  Select both your template page and your database page <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
6.  Click "Allow access" to authorize PDF Output <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. The tool will then automatically fetch the selected database and template <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
7.  Define a connection name (e.g., "Invitation Letter") <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

## Mapping Database Properties to Template Placeholders

Once connected, you'll define the mapping:

1.  On the left, you'll see all your database properties (columns) <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
2.  On the right, you'll see the elements mapped from your template (the text inside curly braces) <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
3.  If your database column names and template placeholder names are identical, mapping should occur automatically <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
4.  If names differ, you will need to manually select the corresponding element for mapping <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
5.  Sorting, searching, and filtering options are available to help manage properties <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

## Generating PDFs

Once mapping is complete:

1.  Click "Create PDF" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. The tool will begin generating the PDF documents <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
2.  You can preview a sample PDF <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
3.  Click "Download all" to [[exporting_and_managing_pdf_files_from_notion_database | export and manage PDF files from Notion database]] <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. Each row from your database will result in a separate PDF document <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

## Reusing Connections and Predefined Templates

*   **Connections**: Once a database and template connection is set up, it's saved under the "Connections" sidebar <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. You can select an existing connection to quickly load the predefined database and template without setting it up again <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   **Predefined Templates**: The "Templates" section in the sidebar offers a list of ready-to-use templates <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. Each template has a corresponding database link <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. To [[using_pdf_output_templates_in_notion | use PDF output templates in Notion]]:
    1.  Click "Start with this template" <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
    2.  Duplicate both the template and its associated database into your Notion workspace <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.

For generating specific PDF documents like invoices, this process enables [[creating_pdf_documents_with_notion_templates | creating PDF documents with Notion templates]] efficiently <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.