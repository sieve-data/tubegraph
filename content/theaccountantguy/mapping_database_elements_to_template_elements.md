---
title: Mapping database elements to template elements
videoId: W_j9W6XedqM
---

From: [[theaccountantguy]] <br/> 

[[mapping_database_elements_to_template_placeholders | Mapping database elements to template placeholders]] is a core process within PDFOutput.com that enables the bulk generation of PDF documents from a Notion template and database <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This process involves replacing specific placeholders in a template with corresponding data from a database <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Core Concept: Placeholders and Database Fields

A template, such as a payment receipt template, contains "elements" enclosed in curly braces, e.g., `{receipt number}`, `{receipt date}`, `{receipt time}`, `{company website}` <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. These curly-braced elements serve as placeholders <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

A corresponding database contains columns (properties) with the exact same names as these placeholders <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a> <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Each row in the database holds specific information for these columns <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. When a PDF document is generated, the data from each database row is used to replace the corresponding curly-braced elements in the template <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## The Mapping Process with PDFOutput.com

[[using_notion_templates_and_databases_for_pdf_creation | Using Notion templates and databases for PDF creation]] involves several steps:

1.  **Connecting Template and Database**: After logging into PDFOutput.com, the first step is to connect your Notion database and Notion template <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This requires granting PDFOutput access to the relevant Notion pages <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
2.  **Loading Elements**: Once connected, PDFOutput loads the properties (columns) from your database and the elements from your template <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
3.  **Automatic Mapping**: If the naming convention between your database columns and template placeholders is exact (including spaces and capitalization), PDFOutput will automatically [[mapping_database_elements_to_template_placeholders | map database elements to template placeholders]] <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a> <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. Every column from the database will be matched to its corresponding template element <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
4.  **Manual Mapping (for Mismatches)**: In cases where there's a mismatch in naming or if an element isn't automatically mapped, you can manually select the correct database property from a dropdown menu <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a> <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
5.  **Generating PDFs**: Once all elements are correctly mapped, you can proceed to generate PDF documents in bulk <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. PDFOutput reads each row of the database and applies the mapped data to the template to create individual PDFs <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a> <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

### Key Considerations for Mapping

*   **Exact Naming Convention**: To ensure seamless automatic mapping and avoid manual correction, it is crucial that the names of your database columns precisely match the names of the placeholders within the curly braces in your template, including any spaces and capitalization <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a> <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Bulk Generation**: The primary benefit of [[mapping_notion_database_elements_to_template_placeholders | mapping Notion database elements to template placeholders]] is the ability to generate many documents at once <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a> <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. For every row of information in your database, a separate PDF document will be generated <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

### Resulting PDF Documents

The successful [[synchronizing_database_elements_with_templates | synchronizing database elements with templates]] results in clean, populated PDF documents where all placeholders are replaced with the correct data from the database <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a> <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. For example, a payment receipt will show the correct receipt number, date, time, customer name, and email as pulled from the database <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

This functionality is central to [[using_templates_and_placeholders_for_document_creation | using templates and placeholders for document creation]] and enables efficient [[using_templates to generate PDF documents | using templates to generate PDF documents]] in various use cases, such as invoices or payment receipts <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.