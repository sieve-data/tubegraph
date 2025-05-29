---
title: Purchase order tracker template in Notion
videoId: zlLWtZdPvLk
---

From: [[theaccountantguy]] <br/> 

This article details a [[setting_up_a_purchase_order_template_in_notion | purchase order tracker template]] designed to help users keep track of their purchase orders within Notion <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This template can be used for general [[using_notion_for_order_tracking | order tracking]] and managing expenses <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## Database Structure

The core of the template is a database with several columns to manage purchase order information <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>:

*   **Purchase Order Number** <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   **Order Date** <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   **Expected Delivery Date** <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>
*   **Terms and Conditions** <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>
*   **Company Name** <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   **Company Address** <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>
*   **Supplier Name** <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
*   **Description**, **Quantity**, and **Unit Price**: These columns are crucial for itemizing purchases. The template includes two sets of these columns, but more can be added by duplicating existing ones. Adding more columns requires updating the formula in the subtotal calculation <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a> <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a> <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **Subtotal Amount**: Automatically computed as the sum of `(quantity * unit price)` for all listed descriptions <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a> <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **Shipping Cost Amount** <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   **Tax Rate (percentage)** <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
*   **Total Amount**: The final computed amount <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Notes**: For any additional information <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

## Summary Sections

The template provides an overview of purchase activities:

*   **Purchase Order Summary**:
    *   **Total Purchase**: The sum of all purchases made <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
    *   **Units Ordered**: Calculated from the sum of all quantity columns <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
    *   **Average Order Value**: Computed by dividing the total purchases by the units ordered <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Client Summary**: This section tracks key metrics for different clients, showing:
    *   Total purchases value for each client <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
    *   Total quantities ordered from each client <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
    *   Average order value for each client <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## [[generating_purchase_order_pdfs_using_notion | Generating Purchase Order PDFs Using Notion]]

The template integrates with `PDFoutput.com` to generate PDF documents for purchase orders <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>:

1.  **Login**: Access `PDFoutput.com` <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
2.  **Template Selection**: Choose the "purchase AO template" from the dropdown menu <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a> <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
3.  **Currency Selection**: Select the desired currency; new currencies can be requested <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a> <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
4.  **Single PDF Mode**:
    *   This mode generates PDF documents one by one <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a> <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
    *   Manually fill in the details from the Notion database into the form on `PDFoutput.com` <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
    *   Click "Download PDF" to generate the document <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. The generated PDF will be clean and precise, reflecting the selected currency <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
5.  **Bulk Export Mode**:
    *   Allows exporting multiple documents in one go <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a> <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
    *   Fill in details for multiple purchase orders by adding new rows <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a> <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
    *   Users can download individual documents or all documents by clicking "Download all PDF" <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a> <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
    *   A future Notion integration is planned to allow direct export of PDFs by reading information from the Notion database <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

## Customization and Feedback

For further customization of the template, users can reach out via `notionformyuse@gmail.com` <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. Feedback for `PDFoutput.com` can also be submitted through its feedback window <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.