---
title: Tracking invoice payments in Notion
videoId: IK71-I_O7Vg
---

From: [[theaccountantguy]] <br/> 

This article details a Notion template designed for [[managing_invoices_and_payment_statuses_in_notion | tracking invoice payments]] and provides a solution for generating PDF invoices.

## Notion Template Overview
The Notion template offers a comprehensive system for [[managing_invoices_and_payment_statuses_in_notion | tracking invoice payments]] with a summary at the top and a detailed database below <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

### Invoice Payment Summary (KPIs)
The top section of the template provides key performance indicators (KPIs) related to invoice payments <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>:
*   **Total Expenses:** The total amount incurred through invoices <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   **Units Purchased:** The combined total of units purchased across all invoices <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   **Average Invoice Price:** The average price of invoices <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
These KPIs can be customized or updated to suit specific business needs <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Values update automatically when inputs are altered in the database <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### Client Summary
A client summary section displays purchase details for each client <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>:
*   Total purchases made against each client <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
*   Number of units purchased from each client <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
*   Average purchase value from each client <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

### Invoice Database
The main database allows users to input and manage invoice details <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>:
*   **Invoice Details:** Invoice number, invoice date, due date, company name (issuer), bill-to section, client address <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   **Item Details:** Description of items purchased (e.g., "item one," "item two"), quantity, and unit price <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   **Calculations:**
    *   **Subtotal:** Calculated automatically as the multiplication of unit price and quantity for each item <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
    *   **Total Amount:** Computed by adding the tax rate to the subtotal <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   **Notes:** Fields for adding notes, such as expected payment receipt time or mode of payment <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   **Customization:** Users can duplicate columns to add more items and must update formulas to include these new columns for accurate calculations <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Additional properties, like "total quantities purchased," can be displayed and require formula updates if new quantity columns are added <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## Generating PDF Invoices with PDF Output.com
The template integrates with PDF Output.com for generating PDF documents for each invoice <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

### Process for Single PDF Generation
1.  **Access the Website:** Navigate to PDF Output.com and log in <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
2.  **Select Template:** Use the drop-down menu on the top left, search for "inv" to find the "invoice" template <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
3.  **Fill Details:** Input invoice details such as invoice number, company name, address, and item specifics (quantity, unit price) <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
    *   The desired currency can be set, which will update the entire invoice <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
4.  **Download:** Click "Download PDF" to generate and download the invoice <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. The PDF will display quantities, unit prices, total computed values, and any added notes <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

### Bulk PDF Generation
PDF Output.com also supports generating multiple PDFs simultaneously <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>:
1.  **Bulk PDF Mode:** Switch to the "bulk PDF mode" <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
2.  **Input Data:** Users can fill in rows of information, potentially by copy-pasting from the Notion database (though direct Notion database support is planned for the future) <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
3.  **Download All:** Click "Download all PDF" to generate all invoices one by one <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
4.  **Row-Specific Download:** It is also possible to download a PDF for a particular row by clicking "download PDF on a particular row" <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

For questions or feedback regarding the invoice payments tracker or PDF generation, users can contact `notionformyuse@gmail.com` or use the feedback window on the website <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.