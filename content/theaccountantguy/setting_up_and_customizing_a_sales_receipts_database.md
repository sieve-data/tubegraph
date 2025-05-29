---
title: Setting up and customizing a sales receipts database
videoId: p9M2n3vwLMs
---

From: [[theaccountantguy]] <br/> 

A sales receipts tracker template can be utilized to keep track of sales data <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This system primarily revolves around a sales receipts database designed to store and manage all necessary information for sales tracking <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This article specifically focuses on [[using_a_sales_receipts_tracker_in_notion | using a sales receipts tracker in Notion]] for managing sales.

## Sales Receipts Database Overview

The core of the system is the sales receipts database, which contains various properties to track sales <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>:

*   **Receipt Number**: A unique identifier for each receipt <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.
*   **Receipt Date**: The date the payment was cleared <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   **Payment Method**: Allows selecting from several predefined payment methods <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.
*   **Business Name and Address**: Fields to enter your business details <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
*   **Customer Details**: A relational property linked to another database containing detailed client information <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   **Description**: Details of what was sold <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. Multiple descriptions can be added for a single sale <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   **Quantity of Sales**: The number of units sold for each described item <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   **Unit Price**: The price per unit of the item sold <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
*   **Subtotal Column**: Automatically sums the total amount for individual items listed under descriptions <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   **Tax Rate**: Applied to the subtotal <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   **Total Amount**: Computed automatically based on subtotal and tax <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Notes Column**: For any relevant notes regarding payments <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

Some additional columns are also present, which are linked to other databases and serve to help understand the connections within the system <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

### Important Note on Formulas
If you add more columns for descriptions and quantities, ensure you update the formulas calculating the subtotal amount <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Similarly, for the "Quantity Sold" column, if more quantity columns are added, update the formula to include them <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

## Sales Receipt Summary

A summary section at the top of the tracker provides key performance indicators (KPIs) drawn directly from the sales database <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>:

*   **Total Sales**: The aggregate sales value <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   **Units Sold**: The total quantity of items sold <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   **Average Sales Value**: Calculated by dividing total sales by units sold, offering essential business insights <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## Client Summary

The client summary section provides a breakdown of sales performance by client <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>:

*   **Total Sales per Client**: Shows the total revenue generated from each customer <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   **Total Quantity of Sales per Client**: Displays the total number of units sold to each client <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **Average Sales Price per Client**: Provides the average price of items sold to each customer <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

## Customization and Support

The sales receipts template can be [[customization_and_feedback_for_sales_receipt_templates | customized]] to meet specific requirements <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. For further [[customization_and_feedback_for_sales_receipt_templates | customization]] assistance or any queries regarding the database, you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

## Generating Sales Receipts as PDF Documents

The information stored in this database can be utilized with external tools like PDFoutput.com to [[generating_sales_receipts_as_pdf_documents | generate sales receipts as PDF documents]] <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. This tool allows for individual PDF generation <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a> or bulk export of multiple receipts from a database <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. The generated PDFs reflect the currency selected within the tool <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.