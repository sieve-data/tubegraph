---
title: Using a sales receipts tracker in Notion
videoId: p9M2n3vwLMs
---

From: [[theaccountantguy]] <br/> 

This article details how to utilize a [[sales_performance_tracking_with_notion | sales receipts tracker template]] in Notion to keep a comprehensive record of sales <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. It also covers generating PDF sales receipts using an external tool, PDFoutput.com. This tracker helps in [[tracking_income_and_expenses_using_notion | tracking income]] and is a specific application of [[expense_tracking_in_notion | Notion for financial tracking]].

## Sales Receipts Database

The core of the template is a sales receipts database designed to track all necessary sales information <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Key properties (columns) include:

*   **Receipt Number** <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   **Receipt Date** <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>
*   **Payment Method:** A selectable dropdown for various payment types <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
*   **Business Name** <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>
*   **Address** <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>
*   **Customer Details:** A relational property linked to another database containing client information <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   **Description:** For details about what was sold <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   **Quantity of Sales** <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>
*   **Unit Price** <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>

For a single sale, multiple descriptions, quantities, and unit prices can be added using separate rows within the entry <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

Calculated fields automatically sum up values:
*   **Subtotal Column:** Calculates the total amount for individual items sold in a particular receipt <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   **Tax Rate:** Applied to the subtotal <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Total Amount:** Computed based on subtotal and tax <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

A **Notes** column is available for any additional information related to the payment <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. There are also additional columns linked to other databases that are not necessary for direct input <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## Sales Receipt Summary

Located at the top of the tracker, the sales receipt summary provides key performance indicators (KPIs) drawn directly from the database entries:
*   **Total Sales:** The sum of all sales values <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **Units Sold:** The total quantity of items sold <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. If additional columns for descriptions and quantities are added, the formulas for the subtotal and total amount need to be updated accordingly <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Similarly, for the "Quantity Sold" column, if more quantities are added for corresponding descriptions, they must be included in its formula <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Average Sales Value:** Calculated by dividing total sales by units sold <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## Client Summary

This section provides a breakdown of sales per client:
*   **Total Sales for Each Client** <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   **Total Quantity of Sales Made to Each Client** <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
*   **Average Sales Price for Every Client** <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

This client summary can be customized to specific requirements <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. For further customization, contact `notionformyuse@gmail.com` <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

## Generating PDF Sales Receipts with PDFoutput.com

Beyond tracking in Notion, users can generate PDF sales receipts using the external tool PDFoutput.com <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

### Steps to Generate Individual PDFs

1.  **Access PDFoutput.com:** Navigate to `PDFoutput.com` <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
2.  **Select Template:** Click on the "template selection" dropdown at the top and choose the "sales receipts" template <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
3.  **Fill Information:** Populate the template fields with details like:
    *   Receipt Number <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>
    *   Receipt Date <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>
    *   Payment Method (selectable) <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>
    *   Business Name and Address <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>
    *   Item Description, Quantity, and Unit Price <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>
    *   Tax Rate <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>
    *   Notes <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>
    *   Currency (e.g., US Dollars, Euro) <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
4.  **Download PDF:** Click "Download PDF" to generate and download the sales receipt document <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

### Bulk Export Mode

For generating multiple PDFs simultaneously, use the "bulk export mode" <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
1.  **Enter Database Information:** Input all sales receipt details into a database format within the tool <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
2.  **Adjust Layout:** Columns and row heights can be resized for readability <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
3.  **Manage Rows:** Use "add new row" to add entries or icons to delete specific rows or items <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
4.  **Download Options:**
    *   **Download All PDFs:** Click this option to download all generated PDFs in one go <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
    *   **Individual Row Download:** Click on an individual row to download a specific PDF <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
5.  **Currency Conversion:** The currency can be changed for all generated PDFs, and they will automatically update <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

### Template Requests and Feedback

If a specific template is needed, users can click "request template" which sends a direct message to the developer <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. A "feedback window" is also available for general feedback <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

For any queries regarding the Notion database or PDFoutput.com, contact `notionformyuse@gmail.com` or use the feedback window <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.