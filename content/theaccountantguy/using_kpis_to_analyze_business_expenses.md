---
title: Using KPIs to analyze business expenses
videoId: IK71-I_O7Vg
---

From: [[theaccountantguy]] <br/> 

This article explores how Key Performance Indicators (KPIs) can be utilized to [[tracking_restaurant_business_expenses | track]] and analyze invoice payments, which constitute a significant part of business expenses, using a Notion template. The template provides a comprehensive overview of expenses and client-specific purchasing data. <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>

## Invoice Payment Summary KPIs

The Notion template features a quick invoice payment summary at the top, offering key insights into overall expenses incurred through invoices. <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a> These KPIs help businesses quickly grasp their financial standing related to invoices:

*   **Total Expenses Incurred:** This KPI represents the sum of all expenses incurred through invoices. <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a> For instance, if input values are altered, the total expenses update automatically. <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>
*   **Total Units Purchased:** This metric shows the combined number of units purchased across all invoices. <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a> The units purchased are calculated as the summation of all units recorded in the database. <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>
*   **Average Invoice Price:** This KPI indicates the average price per invoice. <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>

These KPIs are customizable, allowing for existing ones to be updated or new ones to be added as needed for business analysis. <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>

## Client Summary KPIs

Beyond the overall summary, the template also provides a client summary, detailing purchasing activity per client. <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a> This helps in [[analyzing_income_and_expense_reports | analyzing]] expenditure patterns linked to specific clients:

*   **Total Purchases Per Client:** Shows the monetary value of purchases made from each client. <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a> For example, "11 Enterprises" might show a total purchase of $189. <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>
*   **Units Purchased Per Client:** Indicates the number of units bought from each client. <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a> For instance, "11 Enterprises" could reflect 44 units purchased. <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>
*   **Average Purchase Value Per Client:** Calculates the average value of purchases made from each client. <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>

## Invoice Tracking Database

The core of the system is a database where all invoice details are entered. <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a> This database includes fields such as:

*   Invoice number <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>
*   Invoice date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   Due date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   Company name (from whom invoices are received) <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>
*   Bill to section and client address <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
*   Description of purchased items (e.g., Item One, Item Two) <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>
*   Quantity and unit price for each item <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Subtotal (quantity multiplied by unit price) <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>
*   Tax rate <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>
*   Total amount (computed automatically) <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>
*   Notes, such as expected payment receipt or mode of payment <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>

### Updating Formulas for New Items

When adding more items to an invoice beyond the initial two defined columns, it's necessary to:

1.  Duplicate the existing item description, quantity, and unit price columns. <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>
2.  Update the formula for the subtotal to include the new columns. <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
3.  Update the `Total Quantities Purchased` formula to reflect all new quantity columns so that the top-level KPIs update correctly. <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>

## Generating PDF Invoices

The system also supports generating PDF documents for each invoice using an external website, PDFoutput.com. <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>

### Single PDF Generation

To generate a single PDF invoice:

1.  Log in to PDFoutput.com. <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>
2.  Select the "inv" template from the dropdown. <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>
3.  Fill in all necessary invoice details, including company name, address, item descriptions, quantities, unit prices, and desired currency. <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a> The currency change will update the entire invoice. <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>
4.  Click "Download PDF" to generate the document. <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>

### Bulk PDF Generation

PDFoutput.com also offers a bulk PDF mode, where multiple invoice details can be entered into a table format. <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>

*   Users can manually fill in rows of information or copy-paste data. <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a> (Note: Direct Notion database support was not yet added at the time of recording, but is planned). <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>
*   "Add new row" functionality allows for adding more invoices. <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>
*   "Download all PDF" generates individual PDFs for all entered rows. <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>
*   "Download PDF" on a specific row generates a PDF only for that particular invoice. <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>

This invoice payment tracker assists businesses in maintaining detailed records of their expenses and generating professional documents. <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>

For further assistance, users can reach out to notionformyuse@gmail.com or use the feedback window on PDFoutput.com. <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>