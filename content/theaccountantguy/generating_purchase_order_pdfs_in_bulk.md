---
title: Generating purchase order PDFs in bulk
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 

This guide explains how to [[using_pdfoutputcom_to_generate_pdf_documents_in_bulk | generate PDF documents in bulk]] for purchase orders using a Notion page and database with PDF output.com <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Template and Database Setup
A purchase order template is used, featuring fields like purchase order number, date, supplier, and buyer name <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Essential details for the PDF are placed inside curly braces (e.g., `{purchase order number}`) within the template <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. These bracketed items are dynamically replaced with data from a Notion database <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

The Notion database contains corresponding fields with the exact same naming convention as the template, and values are placed for each row to generate a PDF document <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Using PDF Output.com for Bulk Generation

### Connecting Notion
1.  **Log In**: First, log in to PDFoutput.com <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. The interface will prompt you to connect a Notion database and template <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
2.  **Access Templates**: Navigate to the "Template" section in the right sidebar navigation <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
3.  **Search and Duplicate**: Search for "purchase order" to find the "Purchase Order PDF Generator" <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. Click on both the database and template links <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
4.  **Duplicate to Notion Workspace**: Select "Start with this template" to duplicate the database and template into your own Notion workspace <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Choose your workspace and click "Add to private" <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
5.  **Authorize Connection**: Go back to PDF Output.com and click on "click here to add database" or "click here to add template" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. Select your Notion workspace and choose the duplicated database and template, then click "Allow access" <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
    *   If the database and template don't appear, click the "refresh" option <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
    *   You can select multiple databases or templates using the dropdowns <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

### Mapping Fields
1.  **Name the Process**: Define a name for the export, such as "Purchase Order" <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
2.  **Automatic Mapping**: In the next step, PDF Output.com loads the database and template elements <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. If the naming convention in your database exactly matches the fields in curly braces in your template, the elements will map automatically <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
3.  **Manual Mapping**: If elements are not automatically mapped (indicated by gray color), you can manually click and choose the correct element to map from the template <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

### Generating and Downloading PDFs
1.  **Create PDF**: Click "Create PDF" to begin processing the documents <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
2.  **Preview and Download**: Once the export is successful, you can "preview sample" to view one of the [[generating_pdf_documents_for_purchase_orders | generated PDF documents]] <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. Then, click "Download All" to [[generating_and_downloading_pdf_documents_in_bulk | download all the documents]] in bulk <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

> [!tip] Customization
> The entire template is [[customizing_and_exporting_purchase_order_templates | customizable]]; you can edit or modify it <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. Just ensure that any data you want replaced by the database remains within curly braces and uses the exact same naming convention as the database <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

## Post-Generation Features and Tips

### Connections
The "Connections" option on the right sidebar shows the exact connection you just created, like "Purchase Order" <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Clicking on it automatically loads the database and template, allowing you to proceed with further exports without re-entering details <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

### Upgrade Options
Under the free plan, exported documents will include a "Made with PDF Output" watermark <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. You can upgrade to a paid subscription to remove the watermark and unlock unlimited PDF generation <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

### Settings
The "Settings" section allows you to manage page format (default is A4) and add more databases and templates beyond the initial setup <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

### Feedback and Help
*   **Feedback**: Use the "Feedback" option to report difficulties or issues <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Help**: The "Help" section includes a video demonstrating how to use a custom template from scratch <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

### Important Note on Relation Properties
If your Notion database uses relation properties, ensure you grant access to those relational databases when connecting your workspace to PDF Output.com <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. This ensures all elements are correctly reflected in the PDF output <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

For further assistance, you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.