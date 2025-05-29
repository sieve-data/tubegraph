---
title: Setting up an invoice payment summary
videoId: IK71-I_O7Vg
---

From: [[theaccountantguy]] <br/> 

This article outlines how to set up an [[tracking_invoice_payments_in_notion | invoice payment summary]] within Notion to effectively [[managing_invoices_and_payment_statuses | manage invoice and payment statuses]] for your business <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Overview of the Invoice Payment Summary

The core of the Notion template is a quick [[overview_of_payment_summary_and_quarterly_sections | invoice payment summary]] displayed at the top <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This summary provides key performance indicators (KPIs) to help you understand your business's invoice-related financial status <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

### Key Performance Indicators (KPIs)

The default KPIs shown in the summary include:
*   **Total expenses** incurred through invoices <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   **Total units purchased** across all invoices <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   **Average invoice price** <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

These KPIs are customizable, allowing for additions or updates to better suit specific business needs <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. For example, if an input value is altered, the total expenses and units purchased will automatically update in the summary <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### Client Summary

Below the main summary, there is a [[creating_and_managing_client_summaries | client summary]] section that breaks down purchases by client <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This section shows:
*   Total purchases made against each client <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   The number of units purchased from each client <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   The average purchase value from each client <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

This [[creating_and_managing_client_summaries | client summary]] also automatically reflects changes in the underlying invoice data <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

## Invoice Database Structure

The foundation of the summary is a database located at the bottom of the template <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Users can fill in comprehensive details for each invoice, including:
*   Invoice number <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   Invoice date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   Due date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   Company name (issuer) <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   Bill-to section and client address <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   Description of items purchased <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   Quantity and unit price for each item <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

### Item Details and Calculation

For each item, the database computes the subtotal value by multiplying the unit price and quantity <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. The tax rate is then added to this subtotal to calculate the total amount <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Additional notes, such as expected payment receipt time or mode of payment, can also be included <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### Expanding Items and Updating Formulas

To add more items beyond the initial two, users can duplicate existing columns for description, quantity, and unit price <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. It's crucial to update the formulas that calculate subtotals and total quantities to include these new columns so that the summary reflects accurate figures <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>, <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

> [!INFO]
> The "Total quantities purchased" property, which drives the units purchased KPI, is initially hidden but can be displayed by clicking the three-dot menu and selecting "display more properties" <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. Remember to update its formula when adding new quantity columns <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

## [[generating_and_managing_pdf_invoices | Generating and Managing PDF Invoices]]

While the Notion template excels at [[tracking_invoice_payments_in_notion | tracking invoice payments in Notion]], users might also need to [[generating_and_managing_pdf_invoices | generate PDF documents]] for invoices <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. An external solution, PDF4Put.com, is suggested for this purpose <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### Using PDF4Put.com

1.  **Log in** to PDF4Put.com <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
2.  **Select the invoice template** by searching for "inv" in the template dropdown <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
3.  **Fill in invoice details** such as invoice number, company name, address, items, quantity, and unit price <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. The desired currency can also be set <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
4.  **Download PDF** to generate a single invoice document <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

### Bulk PDF Generation

PDF4Put.com also supports bulk PDF generation <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. Users can fill in multiple rows of invoice information (currently via copy-pasting, with Notion database support planned) <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Clicking "Download all PDF" will generate all invoices one by one <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. Individual PDFs for specific rows can also be generated <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

## Support and Feedback

For any questions or queries regarding the [[setting_up_a_customer_payments_tracker_in_notion | invoice payments tracker]] or using PDF4Put to [[configuring_pdf4put_for_invoice_creation | generate invoice documents]], you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. A feedback window is also available for direct queries <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.