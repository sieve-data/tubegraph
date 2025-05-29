---
title: Notion integration for purchase order management
videoId: zlLWtZdPvLk
---

From: [[theaccountantguy]] <br/> 

This article details a [[notion_overview|Notion]]-based [[purchase_order_tracker_template_in_notion|purchase order tracker template]] and how it integrates with PDF output services to generate purchase order documents.

## [[purchase_order_tracker_template_in_notion|Notion Purchase Order Tracker Template]]

The [[notion_product_order_tracking_template|Notion product order tracking template]] is designed to manage purchase orders efficiently <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

### Database Structure

The core of the tracker is a database that includes key columns for each purchase order <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>:
*   Purchase Order Number <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   Order Date <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   Expected Delivery Date <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>
*   Terms and Conditions <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>
*   Company Name and Address <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   Supplier Name <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>

### Item Details and Calculations

For specific items within a purchase order, the database includes <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>:
*   Description <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   Quantity <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>
*   Unit Price <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>

Additional item descriptions, quantities, and unit prices can be added by duplicating existing columns <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. The subtotal amount is automatically computed as a summation of the quantities and unit prices for all descriptions <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

Other financial fields include:
*   Shipping cost <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Tax rate (in percentage) <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
*   Total amount <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>
*   A section for notes <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>

### Purchase Order Summary

At the top of the tracker, a summary section provides key metrics <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>:
*   **Total Purchase**: Summation of all purchases in the database <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
*   **Units Ordered**: Calculated from the quantity columns <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   **Average Order Value**: Total purchases divided by units ordered, computed automatically <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

### Client Summary

The template also includes a client summary, displaying aggregated data for different clients <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. For example, for clients like ABC Solutions, XYZ Manufacturing, and LMN Enterprises, it shows <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>:
*   Total purchases value <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>
*   Total quantities ordered from each client <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>
*   Average order value for each client <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>

This is a simple template for tracking purchase order expenses <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Further customization can be requested by contacting notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

## [[generating_purchase_order_pdfs_with_notion|Generating Purchase Order PDFs]] with PDF Output.com

PDF output.com offers a solution for [[generating_purchase_order_pdfs_in_bulk_using_notion|generating PDF documents]] for purchase orders <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

### Process for Single PDF Generation

To generate a single PDF document:
1.  Log in to PDF output.com <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
2.  Choose the "Purchase AO template" from the dropdown menu <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
3.  Select the desired currency <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>; new currencies or templates can be requested <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
4.  Ensure you are in "single PDF mode" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
5.  Fill in the template with information copied from your [[notion_product_order_tracking_template|Notion database]] <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
6.  Click "Download PDF" to generate the clean and precise document <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. Currency changes are reflected instantly <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

### Bulk Export Mode

For [[generating_purchase_order_pdfs_in_bulk_using_notion|exporting multiple documents]] at once:
1.  Switch to the "bulk export mode" <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
2.  Fill in details for all desired purchase orders <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>, adding new rows as needed <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
3.  You can download individual documents or select "Download all PDF" to export them all in one go <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

### Upcoming Notion Integration

Future developments will include direct integration with [[notion_overview|Notion databases]] <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. This will allow users to select a [[notion_overview|Notion database]] directly and generate PDFs by reading information from it <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

This system provides a quick and easy way to use the [[purchase_order_tracker_template_in_notion|purchase order tracker template]] and generate PDF documents <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.