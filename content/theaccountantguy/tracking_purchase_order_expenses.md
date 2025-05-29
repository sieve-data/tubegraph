---
title: Tracking purchase order expenses
videoId: zlLWtZdPvLk
---

From: [[theaccountantguy]] <br/> 

A purchase order tracker template can be utilized to [[tracking_expenses_against_a_budget | keep track of]] purchase orders <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This template helps to maintain a database of all purchase-related information and provides summary analytics.

## Purchase Order Tracker Template Overview

The template includes a database designed to maintain detailed records of purchase orders <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### Database Columns
Key columns in the database include <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>:
*   Purchase Order Number <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   Order Date <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>
*   Expected Delivery Date <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>
*   Terms and Conditions <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>
*   Company Name <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   Company Address <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>
*   Supplier Name <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
*   Description (for items) <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   Quantity (for items) <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>
*   Unit Price (for items) <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>

Additional description, quantity, and unit price columns can be duplicated as needed to accommodate multiple items <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

### Calculations
The template automatically computes several values:
*   **Subtotal Amount:** This is calculated as the summation of the unit price multiplied by the quantity for each description <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. If new description columns are added, the subtotal formula needs to be updated <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **Total Amount:** This is derived by adding the shipping cost and applying the tax rate percentage to the subtotal <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
*   **Shipping Cost:** A dedicated field is available to include shipping expenses <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   **Tax Rate:** A tax rate in percentage can be applied <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Notes:** A section for additional notes is available <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Summary and Analytics
The template provides an immediate overview of purchase activities:

### Purchase Order Summary
Displayed at the top, this summary includes <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>:
*   **Total Purchase:** The sum of all purchases recorded in the database <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Units Ordered:** The total number of units across all quantity columns <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. Users must ensure formulas are updated if more quantity columns are added <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **Average Order Value:** Calculated by dividing the total purchases by the units ordered <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

### Client Summary
A summary dedicated to clients reflects their purchasing behavior <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. For example, for clients like ABC Solutions, XYZ Manufacturing, and LMN Enterprises, the summary shows <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>:
*   Total Purchases Value <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>
*   Total Quantities Ordered from each client <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
*   Average Order Value for each client <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>

This template is a simple tool for [[tracking_expenses_against_a_budget | tracking purchase order expenses]] <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. For further customization, one can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

## Generating PDF Documents for Purchase Orders

PDF documents for purchase orders can be generated using PDFoutput.com <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

### Process for Single PDF Generation
1.  Log in to PDFoutput.com <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
2.  Choose "Purchase Order Template" from the dropdown menu <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
3.  Select the desired currency; new currencies can be requested if not available <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
4.  Ensure "Single PDF mode" is selected <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
5.  Fill in all the purchase order details, which mirror the database columns <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
6.  Click "Download PDF" to generate the document <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. The generated PDF will reflect the chosen currency <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

### Process for Bulk Export
1.  Switch to "Bulk Export Mode" <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
2.  Fill in details for multiple purchase orders by adding new rows <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>, <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
3.  Individual PDFs can be downloaded by clicking on specific entries <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
4.  All documents can be downloaded at once by clicking "Download All PDF" <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

### Future Integrations
Soon, PDFoutput.com will support Notion database integration, allowing direct export of PDFs from Notion data <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

The platform continuously adds new templates and welcomes feedback through its feedback window to improve the product <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.