---
title: Generating purchase order PDFs in bulk using Notion
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 

This article outlines how to [[generating_pdf_documents_for_purchase_orders | generate purchase order PDF documents]] in bulk utilizing a Notion page as a template and a Notion database, facilitated by the PDF Output tool <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This method enables [[bulk_pdf_document_generation_using_notion | bulk PDF document generation using Notion]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Template and Database Structure

The process employs a dedicated [[purchase_order_tracker_template_in_notion | purchase order template]] <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This template contains fields such as purchase order number, date, supplier, and buyer name, along with other essential details for the PDF document <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

Elements within the template that are meant to be dynamically replaced by database information are enclosed in curly braces, such as `{purchase order number}`, `{date field}`, `{supplier name}`, and `{buyer name}` <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. A Notion database is used to provide the values for these fields, with columns like "purchase order number", "date field", "supplier name", and "buyer name" <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Each row in the database corresponds to a separate PDF document to be generated <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. It is crucial that the naming convention for the fields in the Notion database exactly matches the names used within the curly braces in the template <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Step-by-Step Generation Process

To [[generating_pdf_documents_in_bulk_using_notion_and_pdf_output | generate PDF documents in bulk using Notion and PDF Output]]:

1.  **Log In to PDF Output**: Begin by logging into PDFoutput.com <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
2.  **Access Templates**: Navigate to the "template" section located in the sidebar navigation <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
3.  **Search and Select**: Search for "purchase order" to find the relevant template <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. Click on both the database link and the template link provided <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
4.  **Duplicate to Notion**: Use the "start with this template" option to duplicate both the database and the template into your Notion workspace <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Select your desired Notion workspace and click "add to private" when prompted <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
5.  **Connect to PDF Output**: Return to PDF Output and click on "click here to add database" or "click here to add template" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. This will prompt you to select the duplicated database and template from your Notion workspace and grant access <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
    *   If you are using any relation properties in your Notion database, ensure you also grant access to those related databases during this step <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
6.  **Name the Configuration**: Once connected, define a name for your configuration, such as "purchase order" <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
7.  **Map Elements**: The system will load the database elements and template elements (defined in curly braces) <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. If the naming conventions match exactly between the database properties and template fields, the elements will map automatically <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. If not, manual mapping is required by selecting the corresponding elements <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
8.  **Create and Download PDFs**: Click "create PDF" <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. PDF Output will process each row in your database, generating a separate PDF document for each <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. After successful export, you can preview a sample file <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a> and then click "download all" to retrieve all generated documents <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

## Customization and Features

### Template Customization
The [[purchase_order_tracker_template_in_notion | purchase order template]] is fully customizable <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. You can edit, modify, or make any changes to the template once it's duplicated to your Notion workspace <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. Remember to keep any content that should be populated from the database inside curly braces and maintain the exact same naming convention in both the template and the database <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

### PDF Output Features

*   **Connections**: The "connections" option on the right sidebar shows previously created configurations (e.g., "purchase order") <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Clicking on an existing connection automatically loads the associated database and template, allowing for quick re-exports without re-entering details <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   **Upgrade Options**: Users on the free plan will find a "made with PDF output" watermark on exported documents <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. Upgrading to a paid subscription removes the watermark and any limits on PDF document generation <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   **Settings**: The "settings" section allows for adjusting the page format (default is A4) <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. You can also add more databases and templates from here after the initial setup <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Feedback**: A feedback option is available for users to report difficulties, issues, or provide suggestions <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Help**: The "help" section includes a video demonstrating how to use a custom template from scratch, if you prefer not to use the predefined templates <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

For any further questions, you can reach out at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.