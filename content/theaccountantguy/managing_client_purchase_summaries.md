---
title: Managing client purchase summaries
videoId: IK71-I_O7Vg
---

From: [[theaccountantguy]] <br/> 

This article details a Notion template designed to track invoice payments and manage client purchase summaries, along with an external tool for generating invoice PDFs.

## Invoice Payment Summary
The template provides a quick summary of invoice payments at the top <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Key Performance Indicators (KPIs) include:
*   Total expenses incurred through invoices <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   Total units purchased from all combined invoices <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   Average invoice price <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

These KPIs can be updated or new ones can be added <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Altering input details in the database, such as unit price or quantity, automatically updates the total expenses and units purchased displayed in the summary <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## Client Summary
A client summary section shows:
*   Purchase amounts against each client <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   Units purchased from each client <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   Average purchase value from each client <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

This summary is automatically computed based on the data entered in the invoice database <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. For example, purchases and quantities against specific clients like "11 Enterprises" are reflected here <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

## Invoice Payments Tracker Database
The core of the template is a database where all invoice details are entered <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
Fields within the database include:
*   Invoice number, invoice date, and due date <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   Company name (who is ordering/issuing the invoice) <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   Bill-to section and client address <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   Description of items being purchased (e.g., Item one, Item two) <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   Quantity and unit price for each item <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   Subtotal, which is derived from the multiplication of unit price and quantity <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   Tax rate and the computed total amount <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   Notes, such as expected payment receipt time or mode of payment <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### Customizing the Database
To add more items beyond the default two, users can duplicate existing item columns <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. When adding new columns for items, it's crucial to update the formula for the subtotal to include these new columns <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Similarly, the "total quantities purchased" property, which contributes to the dashboard's unit summary, also requires formula updates when new quantity columns are added <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

## Generating Invoice PDFs
The template integrates with an external website, `pdfoutput.com`, for generating invoice PDF documents <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### Single PDF Generation
1.  Navigate to `pdfoutput.com` and log in <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
2.  Select the "invoice template" from the dropdown menu by searching for "inv" <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
3.  Fill in the invoice details, including invoice number, company name, address, and item specifics (quantity, unit price) <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
4.  The desired currency can be set, which updates the entire invoice <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
5.  Click "Download PDF" to generate the invoice document <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

### Bulk PDF Generation
The website also supports [[generating_purchase_order_pdfs_in_bulk | bulk PDF generation]] for multiple invoices <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
1.  Switch to the "bulk PDF mode" <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
2.  Users can fill in rows of information, potentially by copy-pasting from the Notion database (support for direct Notion database integration is noted as a future addition) <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
3.  The column width can be expanded for better [[customizing_and_managing_a_purchase_order_database | data entry]] <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
4.  Click "Download all PDF" to generate all invoices one by one, or "Download PDF" on a specific row to generate only that invoice <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

## Support and Feedback
For any questions or queries regarding the invoice payments tracker or utilizing `pdfoutput.com`, users can contact `notionformyuse@gmail.com` <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. There is also a feedback window available directly on the platform for sending queries or [[feedback_and_updates_for_purchase_order_tracker_templates | feedback]] <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.