---
title: Using the purchase order tracker template in Notion
videoId: zlLWtZdPvLk
---

From: [[theaccountantguy]] <br/> 

The [[using_product_order_tracker_templates_in_notion | purchase order tracker template]] in [[using_notion_to_manage_purchase_orders | Notion]] is designed to help users efficiently manage and track their [[using_notion_to_manage_purchase_orders | purchase orders]] and related expenses <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Database Structure

The core of the template is a database that includes several key columns for tracking [[using_notion_to_manage_purchase_orders | purchase order]] details <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>:

*   **Purchase Order Number** <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   **Order Date** <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>
*   **Expected Delivery Date** <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>
*   **Terms and Conditions** <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>
*   **Company Name** <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   **Company Address** <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>
*   **Supplier Name** <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
*   **Description** <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   **Quantity** <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>
*   **Unit Price** <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>
*   **Shipping Cost** <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   **Tax Rate (in percentage)** <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
*   **Notes** <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>

### Managing Line Items and Costs

The template automatically computes the **subtotal amount** for purchase items <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. This subtotal is a summation of the quantity multiplied by the unit price for each described item <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

To add more items, users can duplicate existing "description," "quantity," and "unit price" columns <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. After duplicating, the formula for the subtotal amount needs to be updated to include the new columns <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. The template also incorporates shipping costs and a tax rate percentage to calculate the **total amount** <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## Purchase Order Summary

At the top of the database, a summary section provides a quick overview of the overall purchase data <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>:

*   **Total Purchases**: The sum of all purchases recorded in the database <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   **Units Ordered**: Calculated from the quantity columns of all descriptions <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. Ensure formulas are updated if new quantity columns are added <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
*   **Average Order Value**: Derived by dividing the total purchases by the units ordered <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## Client Summary

The template includes a client summary section, demonstrating tracking for specific clients like ABC Solutions, XYZ Manufacturing, and LMN Enterprises <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. For each client, the template displays:

*   Total purchases value <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   Total quantities ordered <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   Average order value <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## [[generating_purchase_order_pdfs_using_notion | Generating Purchase Order PDFs]]

The video demonstrates how to [[generating_purchase_order_pdfs_using_notion | generate PDF documents]] for [[using_notion_to_manage_purchase_orders | purchase orders]] using PDFoutput.com <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

### Process for Generating Single PDFs

1.  **Login**: Access PDFoutput.com <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
2.  **Select Template**: Choose the "purchase AO template" from the dropdown menu <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
3.  **Choose Currency**: Select the desired currency; new currencies can be requested <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
4.  **Input Data**: Fill in all the [[using_notion_to_manage_purchase_orders | purchase order]] details, mirroring the information from the Notion database <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
5.  **Download PDF**: Click the "Download PDF" button to generate the document <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. The generated PDF will reflect the selected currency <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

### Bulk Export Mode

For exporting multiple [[using_notion_to_manage_purchase_orders | purchase order]] documents simultaneously:

1.  **Switch Mode**: Select the "bulk export mode" <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
2.  **Fill Details**: Input details for all [[using_notion_to_manage_purchase_orders | purchase orders]] into the provided interface, adding multiple rows as needed <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
3.  **Download**: Users can download individual documents or click "Download all PDF" to get all documents at once <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

### Future Notion Integration

Future updates to PDFoutput.com plan to include direct integration with [[using_notion_to_manage_purchase_orders | Notion]] databases <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. This will allow users to directly export PDFs by reading information from their [[using_notion_to_manage_purchase_orders | Notion]] database without manual input into PDFoutput.com <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.