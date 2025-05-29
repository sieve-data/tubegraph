---
title: Integration of Notion with PDF generation
videoId: lCyhl8mofjE
---

From: [[theaccountantguy]] <br/> 

This tutorial demonstrates how to use PDFOutput to generate PDF documents, specifically lease agreements, from a [[Notion database and templates for PDF generation | Notion database]] and Notion page template <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Key Components

The process involves two main components within Notion:
*   **Lease Agreement Template** A Notion page serving as a template for the lease agreement <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. This template includes placeholder text elements (e.g., `landlord name`, `tenant name`, `street address`) enclosed in curly braces, which will be replaced with data from the database <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
*   **Lease Agreement Database** A Notion database containing rows of data for each lease agreement, including fields like "landlord name," "tenant name," and "street address" <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. These values will be used to populate the placeholders in the template <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Setting Up PDFOutput

To begin [[connecting_and_setting_up_pdf_output_with_notion | connecting and setting up PDFOutput]]:
1.  **Login to PDFOutput** Log in to the PDFOutput platform <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
2.  **Initial Setup** Refer to the help section within PDFOutput to complete the initial setup steps, including configuring API keys, before generating documents <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
3.  **Specify Details**
    *   Provide a connection name (e.g., "lease agreement") <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
    *   Select the relevant Notion database from the dropdown list (e.g., "lease") <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
    *   Select the corresponding Notion template (e.g., "lease template") <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
4.  **Proceed to Mapping** Click "Next" to load the database and template elements for mapping <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## Mapping Notion Properties to PDF Elements

PDFOutput automatically maps Notion database properties (e.g., "landlord name," "tenant name") to corresponding PDF template elements if their names match <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
*   The left side displays all Notion properties from the database <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   The right side shows the automatically mapped PDF elements from the template <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   If any property is not mapped, it will appear in gray <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>; clicking on it will display unmapped properties in red, allowing manual mapping <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

## Generating PDF Documents

Once mapping is complete:
1.  **Export** Click "Export" to begin the PDF generation process <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
2.  **PDF Status Property** A "PDF status" column will appear in your Notion database <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. This column's purpose is to track which rows are processed <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
    *   Rows that are unticked will be processed <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
    *   Once a PDF is generated for a row, PDFOutput automatically places a tick mark in the "PDF status" column for that row <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
3.  **Preview Sample** After processing, you can click "Preview Sample" to view a generated PDF document with data from the first row of your database <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. For example, a sample PDF might show "Tom Green" as the landlord and "Sarah Blue" as the tenant, as pulled from the database <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
4.  **Download All** Click "Download all" to download all generated PDF files in a single archive <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. You can open individual files to verify their content <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

## Customization and Best Practices

*   **Template Customization** The template can be customized to suit various use cases <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   **Naming Conventions** To ensure smooth automatic mapping, it is crucial that the naming conventions of properties in the Notion database exactly match the placeholder names in the Notion template <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   **Re-download** If you forget to download the files, you can click "Download" again <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

## Further Assistance

Always follow the preliminary steps in the PDFOutput help section to set up the system <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. For any questions, you can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.