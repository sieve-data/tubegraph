---
title: Tracking invoice payments in Notion
videoId: IK71-I_O7Vg
---

From: [[theaccountantguy]] <br/> 

This article details how to [[using_notion_for_documenting_invoices | track invoice payments]] using a dedicated Notion template and how to generate PDF documents for these invoices using an external tool called PDF Output.com <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Notion Invoice Payment Tracker Template

The Notion template provides a comprehensive system for managing invoice payments <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

### Key Performance Indicators (KPIs)
At the top of the template, a quick summary section displays key metrics <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>:
*   Total [[tracking_expenses_with_notion | expenses]] incurred through invoices <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   Total units purchased across all invoices <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   Average invoice price <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

These KPIs are designed to provide quick insights into your business's invoice activity and can be customized or updated <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. For example, altering input values in the database will automatically reflect changes in total expenses and units purchased <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

### Client Summary
Below the KPIs, a client summary section shows purchase details per client <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>:
*   Total purchases made from each client <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   Number of units purchased from each client <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   Average purchase value from each client <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

For instance, for "11 Enterprises," the total purchase might be $189 with 44 units purchased <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

### Invoice Database Details
The core of the template is a database where you can input detailed invoice information <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>:
*   **Invoice Number** <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>
*   **Invoice Date** <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   **Due Date** <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   **Company Name** (the issuer of the invoice) <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>
*   **Bill To Section** and **Client Address** <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
*   **Description of Items Purchased**: Includes fields for "Item 1" and "Item 2" descriptions <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   **Quantity** and **Unit Price** for each item <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   **Subtotal**: Calculated as the multiplication of unit price and quantity <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   **Tax Rate**: Applied to the subtotal <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   **Total Amount**: Automatically computed after tax <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Notes**: Such as expected payment receipt time or mode of payment <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### Customizing the Template
To add more items beyond the pre-set two, simply duplicate the existing item columns (description, quantity, unit price) and update the corresponding formulas to include the new columns <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. The formulas for total quantities purchased also need to be updated to reflect changes in unit calculations for the KPIs <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

## Generating PDF Invoice Documents with PDF Output.com

The template can be used in conjunction with PDF Output.com to generate PDF versions of your invoices <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

To use this feature, navigate to PDF Output.com and log in <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

### Single PDF Generation
1.  **Select Template**: Use the drop-down menu on the top left and search for "inv" to find the "invoice template" <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
2.  **Fill in Details**: Manually enter all invoice details like invoice number, company name, address, item descriptions, quantities, and prices <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
3.  **Set Currency**: You can change the desired currency, and the entire invoice will update accordingly <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
4.  **Download PDF**: Click "Download PDF" to generate the invoice document <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

### Bulk PDF Generation
PDF Output.com also supports generating multiple invoices in bulk <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>:
1.  **Switch to Bulk Mode**: Access the "bulk PDF mode" <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
2.  **Add Rows**: Click "add new row" to create entries for multiple invoices <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
3.  **Fill Details**: Copy and paste or manually fill in information for each invoice row <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. Support for direct Notion database integration is planned <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
4.  **Download All PDFs**: Click "download all PDF" to generate all invoices one by one <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. You can also download a PDF for a specific row by clicking "download PDF" on that row <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

### Support
For any questions or assistance regarding the Notion invoice payments tracker or using PDF Output.com, you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a> or use the feedback window on the website <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.