---
title: Tracking invoice payments in Notion
videoId: IK71-I_O7Vg
---

From: [[theaccountantguy]] <br/> 

This article details how to track invoice payments using a dedicated Notion template and how to generate PDF invoices with an external tool. The template is designed to help businesses monitor their expenditures and client-specific purchases efficiently <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Notion Template Overview

The Notion template provides a comprehensive system for [[using_notion_for_tracking_accounts_receivable_and_payable | tracking invoice payments]] and related financial data. It can be particularly useful as a [[setting_up_a_customer_payments_tracker_in_notion | customer payments tracker]] <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

### Key Performance Indicators (KPIs)

At the top of the template, a quick invoice payment summary displays essential KPIs <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>:
*   **Total Expenses:** The total amount incurred through all invoices <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This value updates automatically based on changes in the database <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. This serves as a form of [[expense_tracking_in_notion | expense tracking]] <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   **Units Purchased:** The combined total of units purchased across all invoices <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This also updates automatically <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   **Average Invoice Price:** The average price paid per invoice <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

These KPIs can be customized or new ones can be added <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

### Client Summary

Below the KPIs, a client summary section provides details on purchases made from each client <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>:
*   Total purchases from a client <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   Total units purchased from a client <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   Average purchase value from each client <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   This summary helps keep track of client-specific purchase data, such as for "11 Enterprises" showing total purchases of $189 and a combined quantity of 44 units <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

### Invoice Database Details

The core of the template is a database where all invoice details are entered <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>:
*   **Invoice Number** <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>
*   **Invoice Date** <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   **Due Date** <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   **Company Name** (the issuer of the invoice) <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>
*   **Bill To** and **Client Address** <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
*   **Item Description:** For items purchased (e.g., "item one," "item two") <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. Additional item columns can be duplicated <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
*   **Quantity** <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
*   **Unit Price** <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
*   **Subtotal:** Calculated by multiplying quantity and unit price <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. Formulas for subtotal and total quantities purchased need to be updated manually if new item columns are added <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **Tax Rate:** Added to the subtotal <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. This can aid in [[using_notion_for_tracking_tax_payments | tracking tax payments]] <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   **Total Amount:** Automatically computed <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Notes:** For details like expected payment receipt or mode of payment <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

This template helps in [[tracking_income_and_expenses_in_notion | tracking income and expenses in Notion]] <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Generating PDF Invoices

The video also demonstrates [[using_notion_for_invoice_generation | using Notion for invoice generation]] in PDF format through an external website, [PDF output.com](https://www.pdfoutput.com/) <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### Single PDF Generation

1.  Log in to PDF output.com <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
2.  Select the "inv" (invoice) template from the dropdown menu <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
3.  Fill in the invoice details (invoice number, company name, address, item details, quantities, unit prices) <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
4.  The currency can be set, and the entire invoice will update accordingly (e.g., to Euro) <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
5.  Click "Download PDF" to generate the invoice <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. The generated PDF will show quantities, unit prices, total value, and any notes <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

### Bulk PDF Generation

PDF output.com also supports bulk PDF generation <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>:
1.  Navigate to the "bulk PDF mode" <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
2.  Currently, direct Notion database integration for bulk export is not available, but users can manually copy-paste rows of information <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
3.  Users can expand column widths and add new rows as needed <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
4.  Click "Download all PDF" to generate multiple invoices one by one <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
5.  Individual PDFs for specific rows can also be generated <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

For any questions or feedback regarding the Notion invoice payments tracker or PDF output.com, users can contact notionformyuse@gmail.com or use the feedback window on the website <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.