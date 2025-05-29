---
title: Using Notion to manage purchase orders
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 

This article outlines how to use a purchase order template with a [[Using Notion for business tracking | Notion]] database to generate purchase order PDF documents in bulk via PDF Output.com <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Purchase Order Template Overview

The purchase order template includes fields such as purchase order number, date, supplier, buyer name, and other relevant details <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Items enclosed in curly braces within the template, like `{purchase order number}`, `{date field}`, `{supplier name}`, and `{buyer name}`, act as placeholders <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. These placeholders are designed to be replaced with data from a [[Using the purchase order tracker template in Notion | Notion]] database when generating PDF documents <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The entire template is customizable, allowing users to edit or modify its contents <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

## Notion Database for Purchase Orders

The [[Using Notion for business tracking | Notion]] database mirrors the template, containing properties (columns) with the exact same naming conventions as the placeholders in the template <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. Each row in the database represents a unique purchase order, with values placed for each field <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. This setup allows for the generation of a separate PDF document for each row using the defined template <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Generating Purchase Order PDFs in Bulk

To [[generating_purchase_order_pdfs_using_notion | generate purchase order PDFs]] using PDF Output.com, follow these steps:

1.  **Log In to PDF Output**: Access the platform, which will prompt you to connect a [[Using Notion for business tracking | Notion]] database and template <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
2.  **Duplicate Templates**:
    *   Navigate to the "Template" section on the right sidebar <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
    *   Search for "purchase order" to find the predefined template <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
    *   Click on both the "database link" and "template link" provided <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
    *   Select "Start with this template" to duplicate both the database and the template into your [[Using Notion for business tracking | Notion]] workspace <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
3.  **Connect Notion to PDF Output**:
    *   Return to PDF Output and click "Click here to add database" or "Click here to add template" <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
    *   Select your [[Using Notion for business tracking | Notion]] workspace, then choose the duplicated database and template <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
    *   Click "Allow access" to connect them <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   If the database and template don't appear, click the "refresh" button <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
4.  **Define Output Name**: Enter a name for the PDF output, such as "purchase order" <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
5.  **Map Elements**: The system will load database and template elements <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. If naming conventions are exact, elements will map automatically <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. Otherwise, you may need to manually map them by clicking on grayed-out fields <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
6.  **Create and Download PDFs**: Click "Create PDF" to process documents for each row in your database <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. After processing, you can "Preview sample" to see an example <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>, then click "Download all" to get all generated files <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

### Customization and Considerations

*   **Custom Templates**: You can use custom templates if the predefined ones don't suit your needs <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
*   **Naming Convention**: Ensure that the names of properties in your [[Using Notion for business tracking | Notion]] database exactly match the placeholders (text inside curly braces) in your template for automatic mapping <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
*   **Relation Properties**: If your database uses relation properties, ensure you grant access to the related database when selecting pages for access <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Saved Connections**: Once a connection is established (database and template linked), it will appear under the "Connections" section, allowing you to quickly reload them for future exports without re-entering details <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
*   **Page Format**: The default page format for exported PDFs is A4 <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   **Watermark and Limits**: Free plans include a "Made with PDF Output" watermark <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. Upgrading to a paid subscription removes the watermark and eliminates limits on PDF generation <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   **Feedback and Help**: Users can provide feedback or seek assistance via the "Feedback" option or by reviewing the "Help" section for videos on using custom templates <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.