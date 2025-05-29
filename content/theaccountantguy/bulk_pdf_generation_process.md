---
title: Bulk PDF Generation Process
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

[[pdfoutput_for_bulk_document_generation | PDF Output]] is a tool designed to help users [[bulk_pdf_document_generation_process | generate PDF documents in bulk]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. It achieves this by using a Notion page as a template and a Notion database to hold the data elements that will be replaced in the template <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This process facilitates [[bulk_pdf_generation_from_notion_databases | bulk PDF generation from Notion databases]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## How to [[generating_bulk_pdfs_with_database_integration | Generate Bulk PDFs with Database Integration]]

The process involves several steps, starting with setting up your Notion workspace and then configuring [[pdfoutput_for_bulk_document_generation | PDF Output]].

### 1. [[creating_and_using_templates_for_pdf_generation | Creating and Using Templates for PDF Generation]]

Before using [[pdfoutput_for_bulk_document_generation | PDF Output]], you need to create a template and a database in Notion <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

*   **Create a New Page:** Start by creating a new page in Notion <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   **Define Template Content:** Populate this page with your desired content. For example, an invitation letter template can be created <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Placeholder Text:** Key sections of the template that will be replaced by database information must be enclosed within curly braces `{}` <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. These placeholders define the elements to be replaced <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. For example, `{title}` and `{customer name}` would be placeholders <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

### 2. Creating a Notion Database

*   **Create a New Page:** Create another new page in Notion and convert it into a table (database) <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Define Columns:** Add columns to the database that correspond *exactly* to the placeholder names used in your template <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. For instance, if your template has `{title}` and `{customer name}`, your database must have columns named "title" and "customer name" <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
    *   💡 **Tip:** Using the exact same naming convention for columns in the database as the placeholders in the template ensures automatic mapping <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Populate Database:** Fill the database with the unique information for each PDF document you wish to generate <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Each row in the database will correspond to one generated PDF <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

### 3. Connecting Notion to [[pdfoutput_for_bulk_document_generation | PDF Output]]

*   **Log In:** Access your [[pdfoutput_for_bulk_document_generation | PDF Output]] account <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
*   **Add Database/Template:** Within the [[pdfoutput_for_bulk_document_generation | PDF Output]] interface, click on "Click here to add database" or "add template" <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   **Select Notion Pages:** This action will redirect you to Notion, where you must select the specific Notion database and template pages you created <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. Ensure you select the correct Notion account/workspace <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   **Allow Access:** Click "Allow access" to authorize [[pdfoutput_for_bulk_document_generation | PDF Output]] to fetch the selected database and template <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. [[pdfoutput_for_bulk_document_generation | PDF Output]] will automatically sync these <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Define Connection Name:** Once synced, provide a connection name (e.g., "Invitation Letter") <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

### 4. Mapping Properties

*   **Automatic Mapping:** If the database column names exactly match the template placeholder names (inside curly braces), [[pdfoutput_for_bulk_document_generation | PDF Output]] will automatically map them <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   **Manual Mapping:** If names differ, you will need to manually select and map the database properties to the template elements <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Mapping Interface:** The left side of the interface shows database properties (e.g., "customer name," "title"), and the right side shows corresponding template elements <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   **Sorting and Filtering:** Options are available to sort or filter properties, for example, to view unmapped properties <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

### 5. [[generating_bulk_pdfs_with_database_integration | Generating Bulk PDFs]]

*   **Create PDF:** After verifying the mapping, click "Create PDF" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. [[pdfoutput_for_bulk_document_generation | PDF Output]] will begin [[bulk_exporting_pdf_documents | exporting PDF documents]] for each row in your database <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   **Preview and Download:** Once generated, you can preview a sample PDF <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. Then, click "Download all" to download all the generated PDFs <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. Each row in the database will result in a unique PDF document <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

---

### Important Considerations for [[bulk_pdf_document_generation_process | Bulk PDF Document Generation Process]]

*   **Placeholders:** Always enclose placeholder text elements in your template within curly braces `{}` <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   **Naming Convention:** Use the exact same naming convention for placeholder texts in your template and for the corresponding column names in your Notion database <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. If names differ, manual mapping will be required <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   **Use Cases:** This process can be used for various documents, such as [[using_pdf_output_to_generate_invoices | generating invoices]] or [[generating_pdfs_for_business_invoices | business invoices]] <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

### [[pdfoutput_for_bulk_document_generation | PDF Output]] Features Overview

The sidebar in [[pdfoutput_for_bulk_document_generation | PDF Output]] provides additional functionalities:

*   **Connections:** Shows all previously created connections. Selecting a connection will automatically load the predefined database and template, allowing for quicker regeneration without setting up a new connection each time <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   **Templates:** Provides a list of predefined templates <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
    *   Each template has a database link and a template link <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
    *   To use a predefined template, click "Start with this template" to duplicate it to your Notion workspace <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. Remember to duplicate both the database and the template file <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   **Upgrade:** Under the free plan, generated PDFs will have a "Made with [[pdfoutput_for_bulk_document_generation | PDF Output]]" watermark and certain limitations <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. Users can upgrade their subscription plan via this section <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   **Settings:**
    *   Allows choosing different page formats for PDFs <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
    *   Provides an option to add more templates and databases after the initial setup <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.
*   **Feedback:** Users can submit feedback directly to the developer <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Help:** Contains a demonstration video for user assistance <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
*   **Sidebar Toggle:** The sidebar can be closed to maximize screen space <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.