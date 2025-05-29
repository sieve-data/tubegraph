---
title: Using Notion for invoice generation
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

This guide demonstrates how to [[using_notion_for_generating_pdf_documents | generate PDF documents]] using a Notion page and template, specifically focusing on [[creating_professional_invoice_templates_in_notion | invoice templates]] and [[generating_pdf_invoices_from_notion | generating invoice PDFs]] from a Notion database <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Getting Started with PDF Output.com

To begin, you need to log in to PDFoutput.com <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Once logged in, navigate to the 'Templates' section <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

### Selecting an Invoice Template

In the templates section, you will find a list of available templates <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. For invoice generation, download the 'Invoices template' <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. You can use search, sort, or filter options to find specific templates <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

### Understanding the Template and Database Structure

The selected template displays placeholder text elements, such as `client name`, `client company`, `address`, `invoice number`, `date`, `terms`, and `due date` <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>, <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. These placeholders are enclosed in curly braces and will be replaced by data from a Notion database <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>, <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

The Notion database contains corresponding columns like `invoice number`, `date`, `client name`, `client company`, and `client address` <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. The values from each row in the database will populate the respective placeholders in the template <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. It's crucial that the naming conventions for placeholders in the template match the column names in your Notion database <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>, <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

### Duplicating the Template to Notion

1.  On the template page, click "Start with this template" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
2.  You will be prompted to duplicate the template to your Notion workspace <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Select your desired workspace and click "Add to private" <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>, <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. The template and its associated database will then appear in your Notion workspace <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

### Connecting Notion to PDF Output.com

1.  Return to PDFoutput.com and go to 'Settings' <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
2.  Click on 'Add template' <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
3.  Select the Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>, <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
4.  Choose the 'Invoice Generator Template' from the list of available pages and click "Allow access" <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>, <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
5.  PDF Output will then authenticate and add the template to your setup, syncing the database and template elements <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>, <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

### Mapping Properties and Generating Invoices

1.  Once synced, select the Notion database (e.g., 'Invoice Generator Template database') and the corresponding 'Professional Invoice Template' <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>, <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. Give your connection a name, like "Invoice Generator" <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
2.  Click 'Next' <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. The system will display all Notion properties (database columns) on the left, automatically mapped to their corresponding template elements <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>, <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
    *   Unmapped properties will be highlighted, and you can manually map them by searching for the correct element <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>, <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
3.  Click 'Export' to start [[generating_pdf_invoices_from_notion | processing the documents]] <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

### Tracking and Downloading Generated Invoices

As documents are generated, a 'PDF status' column in your Notion database will automatically be checked for each completed invoice <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>, <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

*   You can preview a sample of the generated invoice <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   Click 'Download all' to download all generated PDF invoices <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

### Customization and Important Considerations

*   **Customization**: Both the invoice template and the database columns in Notion are fully customizable <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>, <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. Ensure that any changes to placeholder text in curly braces in the template are reflected with exact matching column names in the Notion database <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>, <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **PDF Status**: Before generating documents, make sure the 'PDF status' column for the relevant rows in your Notion database is unticked. Ticked rows will be ignored during generation <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>, <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   **Watermarks**: On the free plan, generated PDFs will have a watermark <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. To remove it, you need to upgrade to a paid plan <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

### Reusing Connections

Once an output has been generated and exported, the connection details (database and template selection) are saved under the 'Connections' section. This allows you to quickly load the same setup without re-mapping everything <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>, <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

### Support

For any questions or feedback, you can reach out via email to notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. Additional setup guidance can be found in the 'Help' section <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.