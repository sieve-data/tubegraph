---
title: Customizing and managing a purchase order database
videoId: zlLWtZdPvLk
---

From: [[theaccountantguy]] <br/> 

A purchase order tracker template can be utilized to keep track of purchase orders efficiently <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This template primarily consists of a database designed to manage all relevant information.

## Purchase Order Database Structure

The core of the purchase order tracker is a database that includes several key columns:
*   Purchase order number <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   Order date <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>
*   Expected delivery date <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>
*   Terms and conditions <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>
*   Company name <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   Company address <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>
*   Supplier name <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>

### Item Details and Calculations

For specific items within a purchase order, the database includes:
*   Description <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   Quantity <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   Unit price <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>

The template automatically computes a subtotal amount based on the sum of quantity multiplied by unit price for all descriptions <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Additional costs such as shipping and a tax rate percentage are also included to calculate the total amount <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. A "Notes" column is available for any additional information <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

### Customizing Item Rows

To add more item descriptions, quantities, and unit prices, existing columns can be duplicated <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. After duplicating, update the subtotal formula to include the new columns' values, ensuring accurate computation <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## Database Summaries

The template provides summarized views to track overall purchase order data:

### Purchase Order Summary
At the top of the database, a summary displays:
*   Total purchases made <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>
*   Total units ordered, calculated from the quantity columns <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>
*   Average order value (Total purchases divided by units ordered) <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>

> [!CAUTION]
> When adding more descriptions and quantities, ensure that all relevant formulas within the database are updated to reflect the changes accurately <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

### Client Summary
A client summary section tracks data for different clients, such as "ABC Solutions," "XYZ Manufacturing," and "LMN Enterprises" <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. For each client, it shows:
*   Total purchases value <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>
*   Total quantities ordered <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>
*   Average order value <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>

This template offers a simple way to [[using_notion_to_manage_purchase_orders | keep track of purchase order expenses]] <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

## PDF Document Generation

The purchase order tracker can be used in conjunction with PDF output tools to [[generating_and_exporting_pdf_documents_for_purchase_orders | generate PDF documents for purchase orders]] <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

### Single PDF Generation
Using a platform like PDF output.com, users can select a "purchase order template" from a dropdown menu <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. In "single PDF mode," data from the purchase order database can be manually entered into the template fields <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. Once all information is filled, including details like order date, expected delivery date, and item descriptions, the PDF can be downloaded <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. The currency can also be instantly updated before generation <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

### [[generating_purchase_order_pdfs_in_bulk | Bulk Export Mode]]
For [[generating_purchase_order_pdfs_in_bulk | exporting multiple documents]], the "bulk export mode" allows users to fill in details for multiple purchase orders by adding new rows <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. After entering all information, individual documents can be downloaded, or all documents can be downloaded in one go <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

### Future Notion Integration
An upcoming integration will allow users to directly select a [[managing_sales_data_with_databases | Notion database]] and export PDFs, streamlining the process of pulling information directly from the purchase order tracker <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

For further customization or [[feedback_and_updates_for_purchase_order_tracker_templates | feedback]], users can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.