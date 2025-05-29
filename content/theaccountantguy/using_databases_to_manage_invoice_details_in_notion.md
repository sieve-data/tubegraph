---
title: Using databases to manage invoice details in Notion
videoId: IK71-I_O7Vg
---

From: [[theaccountantguy]] <br/> 

This article explores how a Notion database can be used to [[managing_invoices_and_payment_statuses_in_notion | track invoice payments]] and manage invoice details effectively <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. It also demonstrates how to generate professional PDF invoices from the stored data.

## Notion Invoice Payment Tracker Template

The Notion template provides a comprehensive system for managing invoices <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

### Invoice Payment Summary (KPIs)
At the top of the template, a quick summary displays key performance indicators (KPIs) <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>:
*   Total expenses incurred through invoices <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   Total units purchased from all combined invoices <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   Average invoice price <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
These KPIs can be customized or additional ones can be added <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

### Client Summary
A client summary section shows purchase details against each client, including <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>:
*   Total purchases <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   Number of units purchased <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   Average purchase value from each client <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

### Invoice Details Database
The core of the system is a database where all invoice details are entered <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This database allows users to [[setting_up_a_database_in_notion | fill in details]] such as <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>:
*   Invoice number <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>
*   Invoice date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   Due date <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   Company name (issuer) <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>
*   Bill-to section and client address <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
*   Description of items purchased (e.g., "item one," "item two") <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>
*   Quantity of items <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
*   Unit price <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
*   Notes, such as expected payment receipt time or mode of payment <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>

#### Calculations within the Database
The database includes [[creating_a_database_in_notion_for_calculations | calculations]] for financial figures <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>:
*   **Subtotal**: Calculated by multiplying unit price and quantity <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   **Tax rate**: Applied to the subtotal <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   **Total amount**: Computed by adding the subtotal and tax <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

To add more items to an invoice, users can duplicate existing columns for item description, quantity, and unit price, and then update the main formula to include these new columns <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Changes in input values automatically update the total expenses and units purchased displayed in the summary <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### Tracking and Updating
The database includes additional properties, such as "total quantities purchased," which are used to populate values in the summary sections <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. When adding more quantities, it is important to update the relevant formulas for accurate reflection <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. The client summary dynamically displays total purchases and quantities based on the data entered for each client <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

## Generating PDF Invoices using PDFoutput.com

Beyond tracking, the system can also be used to [[generating_professional_invoices_from_notion_database | generate a PDF document]] for each invoice <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. This functionality is supported by an external website, PDFoutput.com <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

### Steps to Generate a Single PDF Invoice
1.  **Log in**: Access PDFoutput.com <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
2.  **Select Template**: In the top left dropdown, search for "inv" to find the invoice template <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
3.  **Fill in Details**: Manually enter invoice details such as invoice number, company name, address, and item values <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. The desired currency can be set, and the entire invoice will update accordingly <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
4.  **Download PDF**: Click "Download PDF" to generate and download the invoice document <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. The generated PDF will show quantities, unit prices, total computed values, and any added notes <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

### Bulk PDF Generation
PDFoutput.com also offers a bulk PDF generation mode <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. While direct integration with a [[using_a_notion_database_and_templates_to_create_pdf_invoices | Notion database]] for bulk data import is not yet available, users can manually fill in rows of information <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   Users can copy and paste details from their Notion database into the bulk mode <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   "Download all PDF" button generates multiple PDF documents one by one <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
*   New rows can be added to input more invoice data <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   Individual PDFs can be generated for specific rows by clicking "Download PDF" on that row <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

## Support and Feedback

For any questions or queries regarding the use of the invoice payments tracker in Notion or utilizing PDFoutput.com for invoice generation, support can be reached via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. A feedback window is also available on the platform for direct communication <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.