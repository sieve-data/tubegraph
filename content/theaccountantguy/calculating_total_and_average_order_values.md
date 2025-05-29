---
title: Calculating total and average order values
videoId: zlLWtZdPvLk
---

From: [[theaccountantguy]] <br/> 

This article details how total and average order values are calculated and tracked within a Notion-based purchase order tracker template.

## Purchase Order Database Structure

The purchase order tracker utilizes a database to maintain information about various purchase orders <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Key columns in this database include:
*   Purchase order number <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   Order date <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>
*   Expected delivery date <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>
*   Terms and conditions <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>
*   Company name and address <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   Supplier name <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
*   Description <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   Quantity <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>
*   Unit price <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>

To add more items, description, quantity, and unit price columns can be duplicated <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Subtotal and Total Amount Calculation

### Subtotal Calculation
The subtotal amount for a purchase order is automatically computed within the database <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. It is derived from the summation of the unit price multiplied by the quantity for each described item <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. If additional description/quantity/unit price columns are added, the subtotal formula needs to be updated to include these new values <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

### Total Amount Calculation
The final total amount includes the subtotal, shipping cost, and a tax rate percentage <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Order Summaries

The template provides summary sections to track key metrics automatically computed from the database <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. These summaries are similar to [[using_a_summary_section_to_track_payment_totals | summary sections used for tracking payment totals]].

### Purchase Order Summary
At the top of the tracker, a purchase order summary displays:
*   **Total Purchases**: This value is obtained by summing all purchases recorded in the database <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **Units Ordered**: This is calculated from the quantity columns for all descriptions <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. When new descriptions and quantities are added, the formulas for these summaries must be updated <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   **Average Order Value**: This metric is computed automatically by dividing the total purchases by the total units ordered <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

### Client Summary
The template also includes a client summary, providing insights for individual clients <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. For each client (e.g., ABC Solutions, XYZ Manufacturing, LMN Enterprises) <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, it reflects:
*   Total purchases value <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>
*   Total quantities ordered <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
*   Average order value <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>

> [!TIP]
> The formulas for calculated values in Notion, like subtotals and summaries, need to be manually updated if new columns or data sources are added to ensure accuracy <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a><a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. This applies to various [[different_methods_to_calculate_sums_in_notion | sum calculations in Notion]].

## Generating PDF Documents

The tracker can be integrated with PDF output.com to [[generating_purchase_order_pdfs_in_bulk | generate PDF documents]] for individual or multiple purchase orders <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a><a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. Users can select the desired currency for the PDF output <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. An upcoming Notion integration will allow direct export of PDFs from a Notion database <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.