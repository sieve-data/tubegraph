---
title: Exporting and managing generated PDF invoices
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

This guide outlines the process of [[using_pdf_output_for_invoice_generation | generating and managing PDF invoices]] using Notion pages and templates in conjunction with PDFoutput.com <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This method allows for the creation of [[creating_bulk_invoice_pdfs | bulk invoice PDFs]] from a Notion database <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Getting Started

1.  **Access PDF Output**: Navigate to PDFoutput.com <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This website is where documents for your use case are created <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
2.  **Log In**: Once logged in, you will see the main interface <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
3.  **Access Templates**: Proceed to the "Template" section <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. Here, you'll find a list of templates compatible with PDF Output <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
    *   You can use search, sorting, or filter options to find specific templates <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
4.  **Download Invoice Template**: For invoice generation, click the download link next to the "Invoices" template <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This opens a new page displaying both the template and its corresponding database <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### Understanding the Invoice Template and Database

The template is designed to generate PDF output from a connected database <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

*   **Template Elements**: The template includes elements like client name, company address, invoice number, date, terms, and due date <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **Placeholder Text**: These elements are enclosed in curly braces, indicating they are placeholder text that will be replaced by data from the connected database <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   **Database Columns**: The database contains columns with the exact same elements (e.g., invoice number, date, client name, client company, client address) <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Each row in the database represents a distinct invoice record <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

> [!IMPORTANT]
> Ensure that all placeholder text elements in the template (inside curly braces) have exact matching names in the database columns to prevent generation problems <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

## Setting Up Your Template

1.  **Duplicate Template**: Click "Start with this template" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. This prompts you to duplicate the template onto your Notion workspace <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
    *   Select your Notion workspace from the dropdown and click "Add to private" <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. The template and its database will then appear in your Notion workspace <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
2.  **Add Template to PDF Output**: Go back to PDF Output and click "Settings" <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
    *   Select "Add template" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
    *   Choose the same Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
    *   Click "Select pages" and then select the "Invoice Generator Template" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   Click "Allow access" to authenticate and add the template to your PDF Output setup <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## Generating PDF Invoices

Once the template is synced, you can proceed to [[exporting_and_managing_pdf_documents | generate and export PDF documents]] <a class="yt-timestamp" data-t="00:03:53">[00:03:55]</a>.

1.  **Select Database and Template**: On the PDF Output screen, select your invoice database and the "Professional Invoice Template" <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
2.  **Name Your Generation**: Provide a name for this generation, e.g., "Invoice Generation" <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
3.  **Map Properties**: Click "Next" <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. PDF Output will sync database elements and template placeholders <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
    *   Notion properties (database column names) are listed on the left <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
    *   Template elements are mapped automatically (shown in green) <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
    *   If any property is unmapped, you can manually click and search for the corresponding element <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
4.  **Export**: Click "Export" to start processing the documents <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
    *   In your Notion database, a "PDF Status" column will be checked as each document is generated <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
    *   If a row's PDF status is already ticked, that row will be ignored during generation <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. Ensure rows are unticked to generate documents from scratch <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

## Managing Generated Invoices

### Preview and Download

After a successful export <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>:

*   **Preview Sample**: Click "Preview sample" to view one of the generated invoices <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   **Download All**: Click "Download all" to [[exporting_and_downloading_pdfs | download all generated PDF outputs]] <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

### Customization and Watermarks

*   **Template Customization**: Both the invoice template and the database are fully customizable <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a> <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. You can add, delete, or modify elements, but remember to maintain consistent naming conventions between the template's placeholder text and the database column names <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a> <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Watermarks**: If you are on the free plan, generated templates will include a PDF output watermark <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. Upgrade to a paid plan to remove watermarks <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

### Connections

*   **Saved Connections**: After an initial export, your connection with the selected database and template is saved <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
*   **Load Previous Settings**: By clicking on "Connections," you can automatically load the same database and template, avoiding the need to map everything again <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>. You can then simply click "Next" to proceed <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

> [!NOTE]
> For further assistance, the "Help" section within PDF Output provides a detailed demonstration of the setup process <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.