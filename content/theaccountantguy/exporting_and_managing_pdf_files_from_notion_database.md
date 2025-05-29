---
title: Exporting and managing PDF files from Notion database
videoId: zrr8DW4PWz0
---

From: [[theaccountantguy]] <br/> 

This article outlines how to generate payment receipt PDF documents using a Notion database and a Notion template with the PDFOutput tool.
[[generating_pdf_documents_from_notion_using_pdfoutput | Generating PDF documents from Notion using PDFOutput]] allows for efficient bulk generation of documents. <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>

## Getting Started with PDFOutput

To begin, log in to PDFOutput.com. <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a> The main interface provides access to various templates. <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>

### Selecting and Duplicating a Template

1.  **Navigate to Templates:** Click on the "Templates" option on the PDFOutput interface. <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a> This page lists all available templates. <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>
2.  **Search for a Template:** Use the search option to find a specific template, such as "payment receipts PDF generator". <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a> Filter and sort options are also available. <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>
3.  **Download/Duplicate:** Click the "download link" next to the desired template. <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a> This opens a new page showcasing the template's Notion database and template. <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>
4.  **Duplicate to Notion Workspace:** If the template is not yet published to the Notion Gallery, click the "duplicate" option. <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a> If it is published, click "start with this template". <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a> You will be prompted to select a Notion workspace to duplicate the template into. <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a> This step is crucial for [[integrating_notion_databases_with_pdfoutput | integrating Notion databases with PDFOutput]]. <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>

### Understanding Notion Template and Database Structure

*   **Template Design:** The Notion template defines the layout of the PDF. Elements meant to be replaced by database information are enclosed in curly braces (e.g., `{receipt number}`, `{customer name}`). <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>
*   **Database Integration:** These curly-braced placeholders directly correspond to column names in your Notion database. <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a> For successful [[generating_pdfs_in_bulk_with_notion | generating PDFs in bulk with Notion]], the exact information in the curly braces must match the corresponding column name in the database. <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>
*   **Customization:** The template is fully customizable within Notion. You can modify formatting (e.g., bold text, spacing) as needed. <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a> Ensure that placeholder elements remain within curly braces to sync properly. <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>

## Connecting Notion to PDFOutput

After duplicating the template to your Notion workspace:

1.  **Go to PDFOutput Settings:** Navigate back to PDFOutput and click on "settings". <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>
2.  **Add Templates:** Click "click here to add templates". <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>
3.  **Select Notion Workspace:** Choose the Notion workspace where you duplicated the template. <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>
4.  **Allow Access:** Select the specific Notion pages (templates) you want to use and click "allow access". <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a> This authorizes PDFOutput to read your template and database elements. <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>

### Mapping Database Properties to Template Elements

1.  **Select Database and Template:** In PDFOutput, select the relevant Notion database (e.g., "payment receipts database") from the dropdown. <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a> Then, select the corresponding template (e.g., "payment receipt template"). <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>
2.  **Name Your Export:** Give your export a name (e.g., "payment receipt"). <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>
3.  **Automatic Mapping:** PDFOutput will load and automatically map Notion database properties (columns) to the template elements if their names match correctly. <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>
4.  **Manual Mapping (if needed):** If any elements are mismatched, you can manually select the correct corresponding property from the dropdown. <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a> Filter, search, and sorting options are available to assist with mapping. <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>

## Generating PDF Documents

Once mapping is complete:

1.  **Export:** Click "export". <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>
2.  **PDF Status Column:** PDFOutput will automatically add a "PDF status" column to your Notion database. <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a> As each row's PDF is generated, its corresponding checkbox in this column will be ticked. <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>
3.  **Success Confirmation:** Upon successful export, a confirmation will appear in PDFOutput. <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>
4.  **Preview and Download:** You can then preview a sample PDF or download all generated files. <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a> Each generated file corresponds to a row in your Notion database. <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>

This process demonstrates [[exporting_pdf_documents_from_notion | exporting PDF documents from Notion]] and [[exporting_notion_data_to_pdf | exporting Notion data to PDF]].

## Managing Connections and Settings

PDFOutput offers features for managing your generation process:

*   **Connections:** The "Connections" section lists all past configurations, allowing you to quickly reload a database and template setup without manual re-entry. <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>
*   **Multiple Templates:** You can select and manage multiple templates. <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>
*   **Watermarks and Plans:** Free plans include a PDFOutput watermark. To remove it, you can upgrade to a paid subscription. <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>
*   **Page Format:** In settings, you can change the page format (e.g., A4, Letter) of the generated PDFs. <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>
*   **Feedback and Help:** A feedback option is available to send messages directly to support, and the "Help" section provides a demonstration video for setup assistance. <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>

By following these steps, you can effectively use PDFOutput for [[bulk_generating_pdf_documents_from_notion_database | bulk generating PDF documents from a Notion database]] and [[creating_templates_and_databases_in_notion_for_pdf_generation | creating templates and databases in Notion for PDF generation]].