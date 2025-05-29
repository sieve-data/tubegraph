---
title: Setting up PDF output for invoice generation
videoId: WfYK1BJd490
---

From: [[theaccountantguy]] <br/> 

This article outlines the process of [[generating_pdfs_for_business_invoices | generating professional invoices]] directly from a Notion database using the PDF output tool <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Components Needed

To generate invoices, you utilize two main components within Notion and a third-party tool:

### Notion Invoice Template
A Notion invoice template is used, featuring "from" and "to" sections <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. Key details like client name, company, address, city, state, and zip are represented as placeholder text enclosed in curly braces (e.g., `{client name}`) <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Any element within curly braces in the template will be replaced by data from a connected database <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

### Notion Database
The Notion database contains the data for each invoice <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. It includes columns such as client name, amount, bank name, client address, and client company <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Each row of information in this database will populate a corresponding invoice template to generate a PDF <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

> [!tip] Placeholder Naming
> Ensure that the names of the placeholder elements in your template exactly match the column names in your database for seamless mapping <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>, <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### PDF Output Tool
The PDF output tool (e.g., "PDF Output") serves as the bridge between your Notion database and template <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This web-based interface allows you to connect and process your data to generate PDF documents <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>, <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

## Setup Process

Follow these steps to set up and use PDF output for invoice generation:

### 1. Enable API Keys
Upon logging into the PDF output interface, navigate to the help section (usually by clicking "H") <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>, <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. There are specific instructions provided to [[setting_up_pdfoutput_with_api_keys | enable the API keys]], which are essential for the setup <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

### 2. Define Connection Name
In the PDF output tool, you will need to define a name for your connection <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. For example, "invoice generation" <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### 3. Select Database and Template
From the dropdown menus, select the specific Notion database (e.g., "professional invoice database") and the corresponding template (e.g., "professional invoice template") that you wish to use <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

### 4. Map Database Elements to Template
After selecting your database and template, click "next" <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. The PDF output tool will load and automatically map the database properties to their corresponding template elements <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. For instance, the "client address" from the database will be connected to the "client address" placeholder in the template <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

> [!warning] Manual Mapping Correction
> If an element from the database does not automatically match a template placeholder, it will appear in gray <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. You can click on the unmatched element and search for the correct value to manually map it <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### 5. Generate and Export PDFs
Once mapping is complete, click "export" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. A "PDF status" column in your Notion database will automatically update (tick) as each PDF file is generated <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>, <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

### 6. Preview and Download
After generation, you can click "preview sample" to view the generated PDF output, ensuring all elements are correctly populated <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>, <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. To download all generated PDF files, click "download all" <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. The downloaded files will be clean and ready for use <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

By following these steps, you can effectively use PDF output to [[using_pdf_output_for_invoice_document_generation | generate professional invoices]] and other [[generating_pdf_documents_for_sales_receipts | PDF documents]] directly from your Notion databases <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.