---
title: Generating lease agreements with PDFOutput
videoId: lCyhl8mofjE
---

From: [[theaccountantguy]] <br/> 

This article explains how to generate lease agreement PDF documents using [[introduction_to_pdfoutput_tool | PDFOutput]] from a Notion database and page. This process involves preparing a template, connecting to your Notion data, and mapping fields for automated document generation.

## 1. Prepare Your Lease Agreement Template

A lease agreement template is used as the base for generating PDF documents <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. This template should include all necessary details such as:
*   Landlord name <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>
*   Tenant name <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>
*   Street address <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>

Key information within the template should be set as placeholder text elements, typically enclosed in curly braces (e.g., `{{landlord_name}}`, `{{tenant_name}}`, `{{street_address}}`) <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. These placeholders will be dynamically replaced with data from your Notion database <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## 2. Prepare Your Notion Database

A Notion database is used to store the specific values for each lease agreement <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. This database should contain columns corresponding to the placeholder text elements in your template, such as:
*   `Landlord Name` <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>
*   `Tenant Name` <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>
*   `Street Address` <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>

Each row in the database represents a unique lease agreement, and [[generating_pdf_documents_in_bulk_using_notion_and_pdfoutput | PDFOutput]] will import values from these individual rows to populate the template <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## 3. Configure PDFOutput

1.  **Log in:** Begin by logging into [[introduction_to_pdfoutput_tool | PDFOutput]] <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
2.  **Initial Setup:** Navigate to the help section within [[introduction_to_pdfoutput_tool | PDFOutput]] to find instructions on setting up API keys and other preliminary steps required before generating PDF documents <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
3.  **Define Connection:** Once the setup is complete, specify the details for your connection. For lease agreements, you might use "Lease Agreement" as the connection name <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
4.  **Select Database and Template:**
    *   Choose the relevant Notion database (e.g., "Lease") from the dropdown list of databases connected via your API key <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
    *   Select your lease agreement template from the template set <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
5.  **Proceed to Mapping:** Click "Next" to load the database and template elements for mapping <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## 4. Map Notion Properties to Template Elements

[[introduction_to_pdfoutput_tool | PDFOutput]] automatically maps Notion properties to the corresponding template elements if their names match <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
*   On the left side, you'll see all your Notion database properties (e.g., `Landlord Name`, `Tenant Name`, `Street Address`) <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   [[introduction_to_pdfoutput_tool | PDFOutput]] attempts to map these to the PDF template elements <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. For example, `Landlord Name` from Notion will map to `landlord_name` in the template <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   If any property is not automatically mapped, it will appear in a grey color <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Click on it to manually map it from the list of unmapped properties, which are often listed in red <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   Ensure that the naming conventions in your database and template match exactly to facilitate automatic mapping <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

## 5. Generate and Download Documents

1.  **Export:** Click "Export" to begin the document generation process <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
2.  **PDF Status Column:** A `PDF Status` property will appear in your Notion database <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. This column defines which rows need to be generated <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
    *   Rows that are unticked will be processed <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
    *   As [[introduction_to_pdfoutput_tool | PDFOutput]] generates PDFs for each row, it will automatically place a tick mark in the `PDF Status` column <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
3.  **Preview Sample:** Once processing is complete, you can click on the "Preview Sample" option to view a generated PDF <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This sample demonstrates how the template placeholders have been replaced with data from a specific Notion row (e.g., Tom Green and Sarah Blue's lease agreement) <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
4.  **Download All:** To download all generated PDF files, click "Download All" <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. The files will be downloaded in a single go, often as a zip archive <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. You can open individual files to verify their contents, ensuring they are exact replicas of your template with the correct data <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

## Need Assistance?

For any questions or further assistance with [[introduction_to_pdfoutput_tool | PDFOutput]], you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.