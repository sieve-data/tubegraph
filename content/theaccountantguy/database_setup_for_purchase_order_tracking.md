---
title: Database setup for purchase order tracking
videoId: zlLWtZdPvLk
---

From: [[theaccountantguy]] <br/> 

This article details the setup and utilization of a database for tracking purchase orders, designed to help monitor expenses and manage order information efficiently <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This [[purchase_order_tracker_template_in_notion|purchase order tracker template]] provides a structured way to input, manage, and summarize purchase data <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Core Database Columns

The purchase order tracker database includes several key columns to capture comprehensive order details <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>:

*   **Purchase Order Number** <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   **Order Date** <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>
*   **Expected Delivery Date** <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>
*   **Terms and Conditions** <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>
*   **Company Name** <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   **Company Address** <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>
*   **Supplier Name** <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
*   **Description**: Details of the items being purchased <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. Multiple description columns can be added by duplicating existing ones <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
*   **Quantity**: The number of units for each described item <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
*   **Unit Price**: The cost per unit for each item <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
*   **Subtotal Amount**: Automatically computed based on the sum of (quantity × unit price) for all descriptions <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. If additional description/quantity/price columns are added, the subtotal formula needs to be updated <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **Shipping Cost**: An additional field to include shipping expenses in the total order value <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   **Tax Rate**: A percentage field for applying taxes to the order <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Total Amount**: The final computed amount, including subtotal, shipping, and tax <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Notes**: A general field for any additional information or comments <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

## Purchase Order Summary and [[client_purchase_summary_and_kpi_tracking|KPI Tracking]]

At the top of the database, a summary section provides key performance indicators (KPIs) for your purchases <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>:

*   **Total Purchase**: The summation of all purchases recorded in the database <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **Units Ordered**: Calculated from the combined quantities of all items across all purchase orders <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   **Average Order Value**: Derived by dividing the total purchases by the total units ordered <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

### Client Summary

The database also features a [[client_purchase_summary_and_kpi_tracking|client summary]] that breaks down purchase data by specific clients, such as ABC Solutions, XYZ Manufacturing, and LMN Enterprises <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. For each client, it displays:

*   Total purchases value <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>
*   Total quantities ordered <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>
*   Average order value <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>

## [[generating_pdf_documents_for_purchase_orders|Generating PDF Documents for Purchase Orders]]

Beyond tracking, this database can be integrated with external tools for [[generating_pdf_documents_for_purchase_orders|generating PDF documents for purchase orders]] <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. One such solution is PDF output.com <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>:

1.  **Accessing the Template**: Log in to PDF output.com and select the "purchase AO template" from the dropdown menu <a class="yt-timestamp" data-t="00:02:56">[00:03:02]</a>.
2.  **Currency Selection**: Choose the desired currency; new currencies can be requested if not available <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
3.  **Data Entry**: Input the purchase order details into the template, such as order date, expected delivery date, company information, item descriptions, quantities, and prices <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. This data can be copied from the purchase order tracker database <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
4.  **PDF Generation**: Click "Download PDF" to generate a clean and precise PDF document of the purchase order in the selected currency <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

### [[exporting_and_managing_purchase_order_data|Bulk Exporting and Managing Purchase Order Data]]

PDF output.com also supports [[exporting_and_managing_purchase_order_data|bulk exporting documents]] <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>:

*   **Bulk Export Mode**: Switch to "bulk export mode" <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Fill Details**: Add multiple rows and fill in all necessary purchase order details from your database <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Download Options**:
    *   **Individual Documents**: Download PDFs one by one <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
    *   **All PDFs**: Download all generated documents in one go <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

### Future [[notion_integration_for_purchase_order_management|Notion Integration]]

A future update for PDF output.com will include [[notion_integration_for_purchase_order_management|Notion integration]], allowing users to directly select their Notion database and export information for PDF generation with a single click <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.