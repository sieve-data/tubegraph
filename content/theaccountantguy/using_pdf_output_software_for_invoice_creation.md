---
title: Using PDF Output software for invoice creation
videoId: WfYK1BJd490
---

From: [[theaccountantguy]] <br/> 

[[pdfoutput_software_setup_for_document_generation | PDF Output]] is a tool designed to [[generating_pdf_invoices_using_pdf_output_service | generate professional invoices]] directly from a Notion database <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It automates the process of populating an [[using_templates_to_generate_pdf_invoices | invoice template]] with data from a database to [[generating_pdf_documents_for_business_purposes | create PDF documents]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Template Setup in Notion
The [[using_templates_to_generate_pdf_invoices | invoice template]] in Notion includes "from" and "to" sections <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. Within the "to" section, placeholders for information such as client name, client company, client address, city, state, and zip are marked using curly braces (e.g., `{client name}`) <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Any element in the template enclosed in curly braces will be replaced with data from a database <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Database Integration
A Notion database holds the data for the invoices, with columns like "client name," "amount," "bank name," "client address," and "client company" <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. For every row of information in this database, [[pdfoutput_software_setup_for_document_generation | PDF Output]] will populate the corresponding fields in the [[using_templates_to_generate_pdf_invoices | invoice template]] and [[generating_pdf_documents_for_business_purposes | generate a PDF]] <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## Using the [[using_pdf_output_interface_for_exporting_documents | PDF Output]] Interface

### Initial Setup
Before using [[pdfoutput_software_setup_for_document_generation | PDF Output]], users must log in and go to the "H" (help) section to complete certain steps for enabling API keys <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Detailed instructions for this setup are provided within the help section <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

### Defining Connection and Linking
1.  **Define Connection Name:** After setup, define a name for the connection, such as "invoice generation" <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
2.  **Select Database and Template:** Choose the specific Notion database (e.g., "professional invoice database") and [[using_templates_to_generate_pdf_invoices | template]] (e.g., "professional invoice template") that will be used <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
3.  **Automatic Mapping:** Upon clicking "next," [[pdfoutput_software_setup_for_document_generation | PDF Output]] automatically loads and maps database elements to the [[using_templates_to_generate_pdf_invoices | template]]'s placeholders <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. For instance, "client address" from the database is connected to the "client address" placeholder in the [[using_templates_to_generate_pdf_invoices | template]] <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
4.  **Manual Mapping Correction:** If any elements are not automatically matched (appearing in gray), they can be manually linked by clicking on them and searching for the correct database column <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. It is crucial that placeholder names in the [[using_templates_to_generate_pdf_invoices | template]] match column names in the database for proper mapping <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

### [[exporting_completed_pdf_invoices | Exporting]] and Generation
After mapping, click "export" to begin the generation process <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. A "PDF status" column in the Notion database will automatically tick as each PDF file is generated <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

### Reviewing and Downloading
Once generated, users can click "preview sample" to view the output and verify that all database elements are correctly replaced in the [[using_templates_to_generate_pdf_invoices | template]] <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. To retrieve all generated files, click "download all" <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. The downloaded files provide clean, professional [[generating_pdf_invoices_using_pdf_output_service | invoice templates]] populated with specific data <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

## Customization
All elements in the [[using_templates_to_generate_pdf_invoices | template]] are customizable <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. The primary rule for customization is to ensure all placeholder text elements are placed inside curly braces and that the same names are used for corresponding columns in the database <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

For questions or assistance, contact notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.