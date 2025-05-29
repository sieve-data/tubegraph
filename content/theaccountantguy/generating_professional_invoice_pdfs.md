---
title: Generating Professional Invoice PDFs
videoId: r6IYxPK0iz8
---

From: [[theaccountantguy]] <br/> 

This article details how to [[generating_professional_invoices_from_a_database | generate professional invoice PDF]] documents in bulk using a Notion template and a Notion database with PDFoutput.com <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Core Components

The process relies on two main Notion elements:

1.  **Professional Invoice Template**:
    *   This template defines all the necessary elements for an invoice <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.
    *   Elements placed inside curly braces `{}` will be replaced with corresponding data from a Notion database <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Examples include `{client name}`, `{client company}`, and `{client address}` <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
2.  **Notion Database**:
    *   This database contains the information that will populate the template <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
    *   For every element in the template, there is a corresponding entry in the database, such as `client name`, `client company`, and `client address` <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
    *   The system can [[bulk_pdf_invoice_generation | generate PDF documents in bulk]] for multiple rows in the database <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Step-by-Step Process for [[generating_pdf_invoices_using_pdfoutput | Generating PDF Invoices using PDFoutput]]

The software used for this process is PDFoutput.com <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

### 1. Log In to PDFoutput.com

*   Navigate to PDFoutput.com and log in <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   Upon successful login, you'll see a connection details screen where you define your PDF generation process <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

### 2. Duplicate Notion Template and Database

Before connecting, you need to copy the desired template and database to your local Notion workspace <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

*   On PDFoutput.com, click on "Templates" to view a list of pre-added templates <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   Search for "invoice" to find the "Professional Invoices" template <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   Click on both the "database link" and "template link" associated with it <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   For both the template and the database, click the "Duplicate" option in the top right of the opened Notion tabs <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   Select your Notion workspace (e.g., "the accountant guy workspace") and click "Add to private" to duplicate them <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. This ensures you have local copies to work with <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

### 3. Connect Notion Database and Template in PDFoutput

*   Once duplicated, return to PDFoutput.com.
*   Click on "Add Database" (or "Add Template") <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   Choose your Notion workspace (e.g., "the accountant guy") <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   Select both the "Professional Invoice Database" and "Professional Invoice Template" you just duplicated <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   Click "Allow access" <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. PDFoutput will then automatically load these into its portal <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>, <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   Define a connection name, such as "Invoice Template," and click "Next" <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

### 4. Map Data Properties

*   PDFoutput will load the database properties on the left and attempt to map them to the corresponding elements in the template <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   If the database property names exactly match the template element names (e.g., `client name` in database and `{client name}` in template), they will automatically map <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   If names differ, an element will show a gray icon <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. Click on it and manually search for the correct property to map <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

### 5. [[bulk_pdf_invoice_generation | Generate PDF Invoices]]

*   Once all elements are correctly mapped, click "Create PDF" <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   The system will start [[bulk_pdf_invoice_generation | generating PDF documents]] for each row in your database <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   After successful generation, you can preview a sample PDF <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a> or download all generated documents as a zip file <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>, <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. Each PDF will accurately reflect the data from its respective database row <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>, <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

## Customization and Best Practices

*   **Template Customization**: The invoice template is fully customizable to your requirements <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   **Naming Convention**: Ensure that any data you want to use from the database is enclosed in curly braces `{}` in the template and uses the *exact same name* as the property in your Notion database <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. This ensures automatic mapping <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
*   **Relational Properties**: If your invoice database contains relational properties linked to *another* Notion database (e.g., for line items), ensure you also connect that relational database when setting up your connections in PDFoutput <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>, <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

## PDFoutput.com Features

PDFoutput.com offers several features to streamline your document generation process:

*   **Connections**: View and reuse previously created connections. This allows you to quickly load an existing database and template setup to [[setting_up_and_using_pdf_output_for_invoices | generate new PDFs]] without re-configuring <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   **Templates**: Access a library of pre-added templates for various use cases, including invoices, [[generating_sales_receipts_as_pdf_documents | sales receipts]], and [[generating_pdf_documents_for_purchase_orders | purchase orders]] <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>, <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Upgrade**: Information on subscription plans. The free plan includes a "Made with PDFoutput" watermark, which is removed with a paid subscription <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Settings**: Define page format (default is A4) <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a> and add more databases and templates after initial login <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
*   **Feedback**: Send messages or queries to the support team <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   **Help**: Access detailed guides on [[using_templates_and_databases_to_create_professional_pdfs | how to connect custom PDF templates and databases]] for generation <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

For questions or assistance, you can contact notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.