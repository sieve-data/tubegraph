---
title: Customizing invoice templates and databases
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

Generating PDF documents from Notion pages can be achieved efficiently using PDFoutput.com, particularly for creating invoices from a Notion database. This process involves [[customizing_invoice_templates_with_placeholders | customizing invoice templates with placeholders]] and [[using_databases_for_invoice_management | managing invoice data in databases]]. <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>

## Setting Up the Invoice Template and Database

To begin, users need to log in to PDFoutput.com. <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a> From the website's interface, navigate to the "template" section to access a list of available templates. <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a> For invoices, select and download the "invoices template." <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>

Once the template is selected, the platform displays both the template and a corresponding database. <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a> To integrate this into a personal workspace, click "Start with this template," which prompts duplication of the template onto your Notion workspace. <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a> After duplication, the template and database will appear in your Notion account. <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>

Next, go back to PDFoutput and add the duplicated Notion template by selecting it from your Notion workspace under the "settings" section. <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a> This step authenticates and adds the template to your PDF output setup. <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>

## Customizing Templates and Databases

The template is fully [[customizing_invoice_templates_with_placeholders | customizable]] to fit specific requirements. <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>
*   **Template Customization**: Elements like client name, company address, invoice number, date, and terms are represented as "placeholder text elements" enclosed in curly braces (e.g., `{client name}`). <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a> These placeholders will be replaced with data from the connected database. Users can add, delete, or modify values within the template, ensuring that placeholder texts remain within curly braces. <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>
*   **Database Customization**: The Notion database linked to the template contains columns corresponding to the placeholders in the template (e.g., "Invoice Number," "Date," "Client Name"). <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a> It is crucial that the naming convention for database columns precisely matches the placeholder names in the template to ensure correct data mapping and PDF generation. <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>

## Generating Invoice PDFs

Once the template and database are prepared and linked, the system syncs all elements. <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a> PDFoutput automatically maps Notion properties (database columns) to the corresponding template elements. <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a> Mapped elements are shown in green, while unmapped properties can be manually searched for and connected. <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>

To generate the PDFs, click "Export." <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a> The database will have a "PDF status" column that automatically checks off as documents are generated. <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a> Generated PDFs can be previewed or downloaded individually or all at once. <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>

### Important Considerations
*   Before generating, ensure that the "PDF status" row in the database is unchecked. A ticked row will be ignored during generation. <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>
*   For outputs without watermarks, a paid plan is required. <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>

The setup with a specific database and template can be saved as a connection for future use, eliminating the need to remap elements repeatedly. <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>

This process, part of [[using_templates_and_databases_for_pdf_generation | using templates and databases for PDF generation]], also applies to other types of documents, as various templates are available on the platform. <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>