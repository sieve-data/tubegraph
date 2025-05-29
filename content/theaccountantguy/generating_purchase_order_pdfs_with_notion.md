---
title: Generating purchase order PDFs with Notion
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

This article details the process of [[generating_purchase_order_pdfs | generating purchase order PDF]] documents using a Notion database and a Notion template, leveraging the PDF output.com platform <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Getting Started with PDFOutput.com

To begin, log in to PDF output.com <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. The interface will display options for connection name, Notion database, and Notion template <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

### Accessing Templates

On the right sidebar, click on "templates" <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This will load a list of predefined templates for [[exporting_pdf_documents_from_notion | generating PDF documents]] <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>, including invoices, [[generating_payment_receipt_pdfs_with_notion | payment receipts]], and [[generating_purchase_order_pdfs | purchase orders]] <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. You can use the search icon to quickly find a specific template <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Sorting and filtering options are also available <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

### Downloading the Purchase Order Template

To add a template to PDF Output, click the "download link" next to the desired template <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. This opens a new page, which serves as the [[generating_purchase_order_pdfs | purchase order PDF]] generator, containing both a database and a template <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## Understanding the Notion Template and Database

The purchase order template includes elements such as purchase order number, date, supplier, buyer, and item description <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Placeholder elements within the template are enclosed in curly braces (e.g., `{purchase order number}`, `{date}`, `{supplier name}`, `{buyer name}`) <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. These placeholders will be automatically replaced with data from a corresponding Notion database <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

The Notion database will contain fields like supplier name, buyer name, date, and purchase order number, with multiple rows of information <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. For each row in the database, a separate PDF document will be generated <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. The column values from the database replace the placeholder text elements in the template <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. To ensure proper functionality, the names of the database properties must exactly match the placeholder text in the template, avoiding extra commas or spaces <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. Both the template and database are fully customizable <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

## Connecting Notion to PDFOutput.com

### Duplicating the Template to Notion

On the [[generating_purchase_order_pdfs | PDF generator page]], select the "duplicate" or "start with this template" option <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. You will be prompted to select your Notion workspace to duplicate the page <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. Once duplicated, the "purchase order PDF generator" page, including its database and template, will appear in your Notion workspace <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

### Adding the Template to PDFOutput.com

Return to PDF output.com and navigate to the "settings" section <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. Here, you can define the PDF's page format <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. Click "click here to add templates" <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. A new window will appear, asking you to connect your Notion pages. Select your Notion workspace from the dropdown menu <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. Then, choose the "purchase order PDF generator" page that you duplicated <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. Click "allow access" to connect this page with PDF output <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

After successful authentication, PDF Output will redirect you back to its main page <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. Give it a few seconds to load all database and template elements <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

## Mapping Database Properties to Template Elements

Once loaded, select the "purchase order database" from the dropdown <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. Then, select the specific "template page" <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a> and give it a name like "purchase order" <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. Click "next" <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

The system will automatically match most of the database properties (Notion properties) to the template elements <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. If any elements are unmatched, it's usually due to a slight mismatch in naming (e.g., an extra space) <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. You can use the "filter unmapped properties" option to quickly identify these <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Manually click on the unmatched property and select the corresponding element from the template <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. A search and sorting option is also available to navigate properties <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

## Generating and Exporting PDFs

Once all elements are correctly mapped, click "export" <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. During export, a "PDF status" column will be automatically added to your Notion database <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. When a PDF document is generated for a row, its checkbox in this column will be ticked <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. To regenerate a PDF, ensure this checkbox is unticked <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

After successful export, you can click "preview sample" to view a generated PDF <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. All generated documents can be downloaded into an output folder <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

## Additional Features of PDFOutput.com

*   **Connections**: Once a PDF is generated, a connection is created and stored, allowing you to quickly regenerate documents without re-filling database and page information <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   **Templates**: Access predefined templates for various document types like invoices and [[generating_payment_receipt_pdfs_with_notion | payment receipts]] <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.
*   **Upgrade**: Free plans will have watermarks on generated PDFs, while paid plans remove them <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Settings**: Define your preferred page format for the PDFs <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **Feedback**: Report any issues or provide feedback through the dedicated option <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
*   **Help**: Find a complete demonstration video for setup and troubleshooting <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

For further assistance or other PDF document solutions, you can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.