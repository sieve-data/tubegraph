---
title: Using PDF output com for bulk PDF generation
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

This article details how to [[using_pdf_outputcom_for_bulk_pdf_generation | generate purchase order PDF documents]] using a Notion database and Notion template with PDF Output.com <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Getting Started

To begin, you must log in to PDF Output.com <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Upon logging in, you will see an interface that includes sections for connection name, Notion database, and Notion template <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

### Accessing Predefined Templates

On the right side of the interface, click on "Templates" in the sidebar <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This will load a list of predefined templates available for [[generating_pdf_documents_in_bulk | generating PDF documents]] <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Examples include invoices, payment receipts, and purchase orders <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. You can search for a specific template using the search icon <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

### Downloading a Template

To add a desired template to PDF Output, click the "Download" link next to it <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This opens a new page, such as the Purchase Order PDF Generator page, which contains both a database and a template <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. These will be connected to PDF Output <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Understanding Templates and Databases

### The Template

The template defines the structure of your document, including elements like purchase order number, date, supplier, buyer, and item description <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Placeholder elements that will be replaced by database values are enclosed in curly braces, such as `{purchase order number}` or `{supplier name}` <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

### The Database

The database contains the actual data for each document, with predefined fields like supplier name, buyer name, date, and purchase order number <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. Each row in the database represents a unique document to be generated <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. The system replaces the placeholder text in the template with these column values <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

> [!TIP] Customization
> All template and database elements are customizable <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. Ensure that values to be replaced are within curly braces and that the database column name exactly matches the placeholder name in the template (avoid extra commas or spaces) <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

## Duplicating the Template to Notion

On the PDF generator page, you'll find an option to "Duplicate" or "Start with this template" <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Clicking this will prompt you to duplicate the page to your Notion workspace <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. Select your desired Notion workspace and click "Add to private" <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. The page, including its database and template, will then appear in your Notion workspace <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## Connecting Notion to PDF Output

1.  Return to PDF Output.com and go to the "Settings" section <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
2.  Here, you can select the desired page format for your PDFs <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
3.  Click "Click here to add templates" <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
4.  A new window will open, prompting you to connect the documents <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. Select your Notion workspace from the dropdown list <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
5.  Click "Select Pages" to view all templates in your workspace <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. Choose the duplicated purchase order PDF generator page <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
6.  Click "Allow access" to connect the Notion page with PDF Output <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. After successful authentication, you will be redirected back to PDF Output.com <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

## Mapping Properties

Once redirected, refresh the PDF Output.com page <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
1.  In the database dropdown, select the "Purchase Order Database" <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
2.  In the template dropdown, select the "template page" itself (not the main generator page) <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
3.  Give the connection a name, like "Purchase Order" <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
4.  Click "Next" <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. The system will automatically attempt to match database properties (left) with template elements (right) <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
5.  If any elements are unmatched, use the "Filter unmapped properties" option to identify them <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. Manually select the corresponding database property for the unmatched template element <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. For example, if "total amount" in the template doesn't match "Total Amount" in the database due to a space difference, you would manually link them <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

## [[generating_pdf_documents_in_bulk | Generating PDF Documents in Bulk]]

1.  After mapping all properties, click "Export" <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
2.  During export, a "PDF status" column will be automatically added to your Notion database <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. When a PDF document is generated for a row, its checkbox in this column will be ticked <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. To regenerate a page, ensure this checkbox is unticked <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
3.  Once the export is successful, you can click "Preview Sample" to see a sample of a generated PDF <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
4.  Click "Download all the documents" to save the generated PDFs to an output folder <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. Each PDF will correspond to a row in your Notion database <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## Additional Features

*   **Connections:** After [[using_pdf_outputcom_for_bulk_pdf_generation | generating a PDF document]], a connection is saved <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. You can use this to quickly regenerate documents without re-filling database and page details <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   **Templates:** This sidebar option shows predefined templates available for [[generating_pdf_documents_for_business_needs | generating PDF documents for business needs]] like invoices and receipts <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.
*   **Upgrade:** Free plans include a watermark on generated templates <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. Paid plans remove this watermark <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Settings:** Define your page format (e.g., A4, Letter) and add duplicated templates to your workspace <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **Feedback:** If you encounter issues, use the feedback option to select a problem type and send a message for assistance <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
*   **Help:** The help section provides a complete demonstration video for setup and troubleshooting <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

For further assistance or specific use cases for [[using_pdfoutput_for_document_generation | PDF document generation]], you can reach out via email <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.