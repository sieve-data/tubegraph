---
title: Syncing and exporting documents using PDF output
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 
This article outlines the process of [[setting_up_and_using_pdf_output_for_invoices | syncing and exporting documents]] as PDFs using [[using_pdfoutputcom_for_bulk_pdf_generation | PDF Output]] by integrating with a Notion database and template.

## Overview
[[Utilizing PDF output for bulk PDF generation | PDF Output]] allows users to [[automating_document_exports_using_pdf_output | automate document exports]] by leveraging Notion pages and templates to generate PDF documents <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The process is demonstrated using an invoice template <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Getting Started

1.  **Access [[using_pdfoutputcom_for_bulk_pdf_generation | PDF Output]]**: Log in to PDFoutput.com <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
2.  **Navigate to Templates**: From the interface, proceed to the "Templates" section <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. This section lists various templates compatible with [[using_pdf_output_tool_for_efficient_document_creation | PDF Output]] <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. You can use search, sort, or filter options to find specific templates <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
3.  **Download Template**: For an invoice demonstration, download the invoice template by clicking its download link <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

### Understanding the Template and Database
Downloading a template opens a page displaying both the template and its associated database <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

*   **Template Structure**: The template includes placeholder text (e.g., client name, invoice number, date, terms) enclosed in curly braces <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. These placeholders will be dynamically replaced with data from the connected database <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   **Database Structure**: The corresponding database contains columns (e.g., invoice number, date, client name, client company, client address) that match the placeholder names in the template <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Each row in the database provides data for a unique PDF output <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

### Duplicating and Connecting the Template

To begin [[steps_to_set_up_and_export_pdfs_using_pdf_output | setting up and exporting PDFs]]:

1.  **Duplicate Template**: Click "Start with this template" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. This prompts you to duplicate the template to your Notion workspace <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Select your desired workspace and "add to private" <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. The template and its database will then appear in your Notion <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
2.  **Add Template to [[using_pdfoutputcom_for_bulk_pdf_generation | PDF Output]]**: Go back to [[using_pdfoutputcom_for_bulk_pdf_generation | PDF Output]] and click on "Settings" <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. Select the option to "add template" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
3.  **Select Notion Template**: Choose the Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>, then click "Select pages" and pick the "invoice generator template" <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. Click "Allow access" to authenticate and add the template to your [[using_pdfoutputcom_for_bulk_pdf_generation | PDF Output]] setup <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

## Customizing Templates and Databases
Both the template and database are fully customizable <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. You can add, delete, or modify elements <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **Placeholder Consistency**: Ensure that any changes to placeholder text within curly braces in the template are exactly matched by the column names in the Notion database <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. This consistency is crucial for proper data mapping during PDF generation <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

## Exporting Documents
Once the template is added and synced:

1.  **Select Database and Template**: On the [[using_pdfoutputcom_for_bulk_pdf_generation | PDF Output]] screen, select the relevant database and professional invoice template <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. Give your export a name <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
2.  **Map Properties**: Click "Next" <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. [[Using PDFOutput for bulk document generation | PDF Output]] will sync the database and template elements <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. Notion properties (database columns) are automatically mapped to the corresponding template elements <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. Unmapped properties will be indicated, allowing you to manually map them <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
3.  **[[Exporting PDF documents using a database | Exporting PDFs]]**: Click "Export" <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. A "PDF status" column in your Notion database will automatically tick as documents are generated <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
    *   **Note**: For successful generation, ensure the "PDF status" row in Notion is unticked for any documents you wish to generate <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. Ticked rows will be ignored <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
4.  **Preview and Download**: Once export is successful, you can "preview sample" <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a> or "download all" generated PDFs <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

## Additional Features

*   **Paid Plan**: While on a free plan, PDFs will include a watermark <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. Upgrade to a paid plan to remove it <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
*   **Saved Connections**: After an initial export, your connection settings (database and template) are saved <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>. You can access these saved connections under the "Connections" section to quickly load and proceed with future exports without re-mapping <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Help Section**: The "Help" section provides a detailed demonstration of the setup process <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
*   **Feedback**: Users can provide feedback via the feedback option <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a> or by emailing notionforuse@gmail.com <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.