---
title: Creating and updating KPIs in Notion for invoices
videoId: IK71-I_O7Vg
---

From: [[theaccountantguy]] <br/> 

[[tracking_invoice_payments_in_Notion | Tracking invoice payments in Notion]] involves utilizing a template that provides a quick invoice payment summary <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This summary highlights key performance indicators (KPIs) related to your invoices.

## Invoice Payment Summary KPIs

The Notion template includes a section at the top displaying a quick invoice payment summary <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This summary includes three primary KPIs:

*   **Total Expenses** The total expenses incurred through invoices <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   **Units Purchased** The combined total of units purchased from all invoices <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   **Average Invoice Price** The average price of invoices <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

These three metrics serve as foundational KPIs for your business <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Client Summary Metrics

In addition to the overall invoice summary, the template also offers a client summary <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This section details performance metrics for individual clients, including:

*   Total purchases made against each client <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
*   The number of units purchased from each client <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   The average purchase value from each client <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Customizing and Updating KPIs

The Notion template is designed to be flexible, allowing for the addition of new KPIs or the modification of existing ones <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

### Updating Total Expenses and Units Purchased

The "total expenses" and "units purchased" KPIs at the top of the template are dynamically derived from the underlying database <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. Any alterations to input figures in the database, such as the total amount of an invoice, will automatically update the displayed total expenses <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. Similarly, the units purchased KPI will reflect changes in the quantities recorded in the database <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

### Adding New Items and Their Impact on Totals

When adding more items to an invoice beyond the existing two default items in the database <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>:

1.  **Duplicate Columns** Simply duplicate the existing item description, quantity, and unit price columns <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
2.  **Update Formulas** Ensure that the formulas used for calculating subtotals and totals are updated to include these new columns <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
3.  **Update Total Quantities Purchased Formula** The "total quantities purchased" property, which feeds data to the top-level KPIs, also needs its formula updated to include any newly added quantity columns <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

Once these updates are made, all related metrics and KPIs will automatically reflect the changes <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### Managing Invoice Details

The [[using_databases_to_manage_invoice_details_in_Notion | database at the bottom of the template]] allows you to fill in detailed invoice information such as invoice number, date, due date, company name, items, quantity, unit price, tax rate, and notes <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. The subtotal for each item is automatically computed by multiplying the unit price and quantity <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>, and the total amount is calculated by adding the tax rate to the subtotal <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. This structured data entry ensures that the KPIs are accurately derived.