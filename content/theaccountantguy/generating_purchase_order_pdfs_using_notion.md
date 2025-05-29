---
title: Generating purchase order PDFs using Notion
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

This article details the process of [[generating_pdf_documents_with_notion | generating PDF documents]] for [[using_notion_to_manage_purchase_orders | purchase orders]] using a Notion database and template, leveraging the PDFOutput.com service <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Getting Started with PDFOutput.com

To begin, log into PDFOutput.com <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The interface will display options for a connection name, Notion database, and Notion template <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

### Accessing Predefined Templates

On the right sidebar, click on "Templates" <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. This will load a list of predefined templates available for [[pdf_document_generation_from_notion | PDF document generation from Notion]], including [[creating_bulk_invoices_with_notion | invoices]], [[generating_payment_receipts_pdf_using_notion | payment receipts]], and [[using_the_purchase_order_tracker_template_in_notion | purchase orders]] <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. You can use the search icon to quickly find the "purchase order" template <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

Once found, click the "Download" link next to the desired template <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This opens a new page dedicated to the [[generating_and_exporting_pdf_documents_for_purchase_orders | purchase order PDF generator]], which includes both a database and a template <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

### Understanding the Notion Template and Database

The purchase order template contains elements like purchase order number, date, supplier, buyer, and item description <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
Elements enclosed in curly braces, such as `{{purchase order number}}` or `{{supplier name}}`, are placeholders that will be replaced by data from your Notion database <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

The accompanying Notion database contains columns like "Supplier Name," "Buyer Name," "Date," and "Purchase Order Number," with predefined values <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Each row in the database will correspond to a separate PDF document generated <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## Duplicating to Your Notion Workspace

On the purchase order PDF generator page, you will find an option to "Duplicate" or "Start with this template" <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Click this option to duplicate the page (including the template and database) into your Notion workspace <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. Select your desired Notion workspace when prompted <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

## Connecting Notion to PDFOutput

After duplicating the template to your workspace:
1.  Go back to PDFOutput.com and navigate to the "Settings" section <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
2.  Here, you can select the desired page format for your PDFs (e.g., A4, Letter) <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
3.  Click "Click here to add templates" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
4.  A new window will open asking you to connect your Notion workspace <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. Select the workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
5.  Click "Select Pages" and choose the "Purchase Order PDF Generator" page (which contains both the database and template) <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
6.  Click "Allow access" to connect the page with PDFOutput <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. Wait for the authentication to be successful <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

## Mapping Database Properties to Template Placeholders

Once the connection is established and the database and template elements are loaded:
1.  On the PDFOutput interface, select the "Purchase Order database" from the first dropdown menu <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
2.  From the second dropdown, select the "Template page" within your "Purchase Order PDF Generator" <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
3.  Give your connection a name, e.g., "Purchase Order" <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
4.  Click "Next" <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

PDFOutput will automatically match most of the database properties (Notion properties) to the template elements <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
You might find some elements unmatched, often due to minor discrepancies like extra spaces in names <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.
To identify unmatched properties, use the "Filter unmapped properties" option <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. Manually select the corresponding database property for any unmapped template element <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

<br>

> [!CAUTION] Matching Names
> Ensure that the names of your database columns exactly match the placeholder text within the curly braces in your Notion template (e.g., `TotalAmount` in the template should match `Total Amount` in the database if there's a space, or vice-versa) <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. Mismatches can prevent correct linking, though they can be manually corrected in the mapping step <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

## Exporting and Reviewing PDFs

Once all properties are correctly mapped, click "Export" <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
PDFOutput will automatically add a "PDF Status" column to your Notion database. When a PDF document is generated for a row, this checkbox will be ticked <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. If you need to regenerate a PDF for a specific row, ensure this checkbox is unticked <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

After successful export, you can preview a sample of the generated PDF <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. The generated PDFs will reflect the data from your Notion database in the template structure <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
Finally, you can [[generating_purchase_order_pdfs_in_bulk | download all the generated PDF documents]] <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

## Customization and Other Features

### Template and Database Customization
Both the template and the database are fully customizable <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. You can add, delete, or modify any values and columns as per your requirements <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. The key is to ensure that values meant to be replaced in the PDF are placed inside curly braces in the template and that their names match the database column names <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

### PDFOutput Sidebar Options
The PDFOutput sidebar provides several options:
*   **Connections:** Stores previously generated PDF document connections, allowing you to quickly regenerate documents without re-filling database and page details <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   **Upgrade:** Explains subscription plans. Free plans will have a watermark on generated templates, while paid plans will not <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Settings:** Where you can define the page format for your PDFs and manage connected templates <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **Feedback:** An option to send feedback or report issues <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
*   **Help:** Contains a complete demonstration video for setup and troubleshooting <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

For any specific PDF document generation needs or further assistance, you can reach out via email at `notionformyuse@gmail.com` <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.