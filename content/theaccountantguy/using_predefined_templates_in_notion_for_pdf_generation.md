---
title: Using predefined templates in Notion for PDF generation
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

This article outlines how to utilize predefined Notion templates with PDF output.com to [[generating_pdf_documents_using_notion | generate PDF documents]] from your Notion databases.

## Getting Started

To begin, log in to PDF output.com <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The interface will display options for connection name, Notion database, and Notion template <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Selecting a Predefined Template

1.  Navigate to the 'Templates' sidebar element <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
2.  Here, you'll find a list of predefined templates such as invoices, payment receipts, and purchase orders <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
3.  You can use the search icon to quickly find a specific template <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
4.  Click the 'Download link' next to your desired template, such as the Purchase Order template, to open its dedicated PDF generator page <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This page includes both a database and a template that you will connect to PDF output <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### Understanding the Template and Database Structure

*   **Template:** The template (e.g., Purchase Order) includes elements like purchase order number, date, supplier, buyer, and item description <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Key elements that will be populated by data are enclosed in curly braces (e.g., {{purchase order number}}) <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
*   **Database:** The accompanying database contains predefined fields (columns) such as supplier name, buyer name, date, and purchase order number <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Each row of information in this database will be used to [[generating_pdf_documents_using_notion | generate a separate PDF document]] <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Customization:** Both the template and database are [[customizing_templates_in_notion | customizable]] <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. You can add, delete, or modify values, but ensure that any values intended for replacement are within curly braces in the template <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. The names of the database columns must exactly match the placeholder names in the template (case-sensitive, no extra spaces or commas) for proper linking <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

## Duplicating the Template to Notion

1.  On the PDF generator page, find the 'Duplicate' option (or 'Start with this template' if already published) <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
2.  Click 'Duplicate' and select your Notion workspace to add the page to your Notion account <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. This action will add the entire page, including the database and template, to your Notion workspace <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## Connecting Notion to PDF output.com

1.  Return to PDF output.com and go to the 'Settings' section <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
2.  You can set the desired page format for your PDFs here <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
3.  Click 'Click here to add templates' <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
4.  Select the Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a> and click 'Select Pages' <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
5.  Choose the duplicated Notion page (e.g., 'Purchase Order PDF generator') from the list <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
6.  Click 'Allow access' to connect the page with PDF output.com <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. A successful authentication will redirect you back to the PDF output page <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

## Mapping Database Properties to Template Elements

1.  After authentication, PDF output.com will load the database and template elements <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
2.  From the drop-down menu, select your Notion database (e.g., 'purchase order database') <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
3.  Select the specific template page (e.g., 'template') from the next drop-down <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
4.  Give your connection a name (e.g., 'purchase order') <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a> and click 'Next' <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
5.  The system will automatically match most elements <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. For any unmatched properties (e.g., due to name mismatches like "total amount" vs. "total amount "), you will need to manually map them <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.
    *   Use the 'Filter unmapped properties' option to quickly identify missing links <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
    *   Click on the unmatched item and search for its corresponding name in the template <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
6.  Once all elements are correctly mapped, click 'Export' <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

## Generating and Downloading PDFs

1.  Upon export, a 'PDF status' column will be added to your Notion database, indicating the generation progress <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. A ticked checkbox means the PDF has been generated <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. To regenerate a page, untick its checkbox <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
2.  Once the export is successful, you can click 'Preview sample' to view a generated PDF <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
3.  To download all generated documents, click 'Download all documents' <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. These will be found in an output folder <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

## Additional Features

*   **Connections:** After generating a PDF document, PDF output.com saves the connection. This allows you to quickly regenerate documents without re-entering database and page information <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   **Upgrade:** Free plan generated PDFs will have a watermark. Paid plans remove the watermark <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Settings:** Define your desired page format and manage connected templates <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **Feedback:** Submit feedback if you encounter any issues <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
*   **Help:** Access a complete demonstration video for setup and troubleshooting <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.