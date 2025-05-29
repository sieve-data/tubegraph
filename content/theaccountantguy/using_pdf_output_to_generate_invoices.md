---
title: Using PDF output to generate invoices
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

This guide provides a quick demonstration on how to [[generating_pdf_invoices_from_notion_data | generate PDF documents]] using a Notion page and template, specifically focusing on [[generating_pdfs_for_business_invoices | invoice generation]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The process involves utilizing PDFoutput.com, a website designed for creating such documents <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## Getting Started with PDF Output

To begin, log in to PDFoutput.com <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Upon logging in, you will see an interface that allows you to proceed to the "Templates" section <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

### Accessing Invoice Templates

The "Templates" section displays a list of pre-created templates compatible with [[integration_with_pdf_output_tools | PDF Output]] <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. For invoices, locate and click the "download" link next to the invoices template <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

You can also use the search, sorting, or filter options to find specific templates <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. Searching will open a window where you can type a name to find available templates <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Template and Database Structure

After downloading the template, a new page will open showing both the template and its corresponding database <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### Understanding Placeholder Elements
The template includes elements like "client name," "client company address," "invoice number," "date," and "terms," which are enclosed in curly braces <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. These are placeholder text elements that will be replaced with data from the connected Notion database <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

### Notion Database Matching
The Notion database contains columns with the same elements listed in the template, such as "invoice number," "date," "client name," and "client company" <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Each row of the database will replace the corresponding placeholder elements in the template <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### Customization Notes
Both the template and the database are fully customizable; you can add, delete, or modify content <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. However, ensure that all placeholder text elements in curly braces in the template exactly match the column names in the database <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>, including the exact same naming convention <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

## [[setting_up_pdf_output_for_invoice_generation | Connecting Notion with PDF Output]]

To begin [[setting_up_pdf_output_for_invoice_generation | setting up PDF output for invoice generation]]:

1.  **Duplicate the Template**: Click "Start with this template" on the PDF Output website <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. This will prompt you to duplicate the template to your Notion workspace <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Select your desired Notion workspace and click "add to private" <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. The duplicated template, including the invoice database, will appear in your Notion workspace <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
2.  **Add Template to PDF Output**: Return to PDF Output and click on "Settings" <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. Choose the option to add a template <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Select the Notion workspace where you duplicated the template, then choose the "invoice generator template" from the list of available pages and click "allow access" <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. This will authenticate and automatically add the template to your [[managing_and_exporting_pdfs_with_pdfoutput | PDF Output setup]] <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. Wait a few seconds for the database and template elements to sync <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

### Mapping Properties

Once synced, select the database and the professional invoice template within PDF Output <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. The system will then sync all elements, displaying Notion properties (database columns) on the left and template placeholders on the right <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

Most elements will be automatically mapped, indicated by a green bar <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. For example, "client name" from the database will be mapped to the "client name" placeholder in the template <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. If an element is not mapped, you can click on it and search for the corresponding element to map it manually <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>. Sorting, searching, and filtering options are available to manage properties <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

## [[generating_pdf_documents_for_sales_receipts | Generating PDF Documents]]

Once all elements are correctly mapped, click "Export" <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. This initiates the processing of documents <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

### Monitoring Generation
In your Notion database, a "PDF Status" column will be present <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>. As each document is generated, this column will automatically get checked <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. Wait for a few seconds for the template to generate <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. A "successful" message will appear on PDF Output <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

### Preview and Download
You can preview a sample of the generated invoice to verify details such as invoice number, date, and client name <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. To download all generated PDF invoices, click "Download all" <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. Each invoice will be downloaded individually <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.

## Key Considerations

*   **PDF Status Column**: Before generating output, ensure the `PDF Status` row in your Notion database is unticked <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. If it's ticked, that specific row will be ignored during generation <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   **Watermarks**: The free plan of PDF Output will generate templates with a watermark <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. To remove watermarks, an upgrade to a paid plan is required <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   **Connections**: After generating and exporting files, the connection with all saved values will be stored <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. This allows you to automatically load the same database and template without re-mapping for future use <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.
*   **Help and Feedback**: The help section provides detailed setup instructions <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. For questions or feedback, you can reach out via email to notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.