---
title: Using Notion templates and databases for PDF generation
videoId: W_j9W6XedqM
---

From: [[theaccountantguy]] <br/> 

This article discusses how to generate PDF documents in bulk using a [[using_notion_for_pdf_template_creation | Notion template]] and a [[creating_a_notion_database_for_pdfs | Notion database]] with the help of a tool called PDF output.com <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. The process involves creating a template with placeholder elements and a database containing the data to populate those elements <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Key Components

### Notion Template
A [[using_notion_for_pdf_template_creation | Notion template]] is set up with specific elements enclosed in curly braces, such as `{Receipt Number}`, `{Receipt Date}`, and `{Customer Name}` <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. These curly-braced elements serve as placeholders to be replaced by data from the database <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

### Notion Database
The [[creating_a_notion_database_for_pdfs | Notion database]] contains rows of information, where each row will correspond to a generated PDF document <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Each column in the database should correspond to an element in the template, using the exact same naming convention (including spaces and capitalization) <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## [[Connecting Notion databases with PDF generation tools | Connecting Notion to PDF Output]]

The tool used for this process is PDF output.com <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### Duplicating Template and Database
1.  Log in to PDF output.com <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
2.  Navigate to the "template" section <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
3.  Search for the desired template (e.g., "payment receipts") <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
4.  Each template provides a database link and a template link <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
5.  Click on both the database link and the template link to open them in new windows <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
6.  Duplicate both the template and the database to your local Notion workspace by clicking "Duplicate" and selecting your workspace <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

### Establishing Connection
1.  Once logged into PDF output.com, click "Click here to add database" or "Add template" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
2.  Grant permission by selecting your Notion workspace (e.g., "accountant guy workspace") and clicking "Select pages" <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
3.  Select both the duplicated Notion template and database from your workspace and click "Allow access" <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
4.  The system will authenticate with Notion and connect the selected database and template <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
5.  Optionally, give the connection a name (e.g., "payment receipts") <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

### [[Mapping Notion Database to PDF Templates | Mapping Properties]]
1.  After connecting, the tool will load the database properties and template elements <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
2.  It automatically attempts to map database columns to template elements if the naming conventions (including spaces and capitalization) are identical <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
3.  If there's a mismatch, you can manually map properties by clicking on the unmapped element and searching for the corresponding database column <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
4.  Filter, search, and sorting options are available to manage properties <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.

## [[Bulk PDF generation from Notion databases | Generating and Downloading PDFs]]
1.  Once all properties are correctly mapped, click "Create PDF" <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
2.  The tool will read the database rows and the template to generate PDF documents <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. For example, three rows in the database will generate three PDF documents <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
3.  After successful export, you can preview a sample PDF <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
4.  Click "Download all documents" to download all generated PDFs <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

## Additional Features of PDF output.com

*   **Connections:** View a list of previously created connections to quickly reload a database and template combination without re-adding them <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. If connection fails to load, try clicking refresh <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
*   **Templates:** Access a variety of predefined templates for different use cases, such as [[using_notion_templates_for_invoice_pdfs | invoices]] <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
*   **Upgrade:** Free plans include a "made with PDF output" watermark on PDFs <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. Upgrading to a paid plan removes the watermark and offers higher usage limits <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.
*   **Settings:** Define the page format (default is A4) <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. You can also add more templates and databases here after the initial setup <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Feedback:** Submit questions or feedback through a dedicated window <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
*   **Help:** Find instructions on [[setting_up_a_notion_database_and_template_for_pdf_generation | how to use a custom PDF document with a database]] instead of a predefined template <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.
*   **Sidebar:** The sidebar can be collapsed for a larger view <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.

For questions, reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.