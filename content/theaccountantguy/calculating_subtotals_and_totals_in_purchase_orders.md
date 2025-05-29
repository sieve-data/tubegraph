---
title: Calculating subtotals and totals in purchase orders
videoId: zlLWtZdPvLk
---

From: [[theaccountantguy]] <br/> 

This article explains how subtotals and totals are calculated within a purchase order tracker template, and how these calculations are reflected in generated documents. This template is designed to help users [[setting_up_a_purchase_order_tracking_database | keep track of purchase orders]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Purchase Order Database Structure

The core of the purchase order tracker is a database that includes several key columns for tracking purchases <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Important columns for calculations include:
*   **Description** <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   **Quantity** <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   **Unit Price** <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>

Initially, the template provides two sets of description, quantity, and unit price fields <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Subtotal Calculation

The subtotal amount is automatically computed based on the items listed <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. It is a summation of the unit price multiplied by the quantity for each description listed <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

### Adding More Items to Subtotal
If more items need to be added to a purchase order, users can duplicate the existing description, quantity, and unit price columns <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. To ensure these new items are included in the subtotal calculation, the respective formula for the subtotal column must be updated <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## Total Amount Calculation

Beyond the subtotal, the template also includes fields for additional costs and taxes:
*   **Shipping Cost Amount:** This cost is added to the purchase order <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   **Tax Rate (in percentage):** A tax rate is applied <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

These elements combine with the subtotal to generate the final total amount for the purchase order <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## Purchase Order Summary

At the top of the database, a purchase order summary provides aggregated insights <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>:
*   **Total Purchase:** This is derived from the summation of all purchases within the database <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **Units Ordered:** This value is calculated by summing the quantities from all quantity columns <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. If more quantity columns are added, these formulas must be updated to reflect the new data <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   **Average Order Value:** This is automatically computed by dividing the total purchases by the units ordered <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## Client Summary

The template also includes a client summary, which provides a breakdown of purchase metrics per client <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. For each client (e.g., ABC Solutions, XYZ Manufacturing, LMN Enterprises) <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, it displays:
*   Total purchases value <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>
*   Total quantities ordered <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
*   Average order value <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>

## Generating PDF Documents with Calculated Totals

The calculated totals and subtotals from the purchase order tracker are directly reflected when [[generating_purchase_order_pdfs_using_notion | generating PDF documents]] using PDFoutput.com <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
After inputting the purchase order details, including descriptions, quantities, and unit prices, the total amount is automatically displayed and will appear in the generated PDF <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. The tool also allows for [[integrating_currency_options_in_sales_receipts | selecting desired currencies]] <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>, which instantly updates the displayed and PDF-generated totals <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

Future integration with Notion databases is planned, which will allow for direct export of information and PDF generation from Notion data <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.