---
title: Using templates in PDF Output for generating receipts
videoId: zrr8DW4PWz0
---

From: [[theaccountantguy]] <br/> 

This guide explains how to generate PDF payment receipt documents using a Notion database and a Notion template with PDF Output. <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>

## Getting Started

1.  **Log in to PDF Output**: The first step is to log in to PDFoutput.com. <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>
2.  **Access Templates**: Once logged in, navigate to the "Templates" section. <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a> This page lists all available templates for PDF Output. <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>

## Selecting and Preparing the Template

*   **Search for the Template**: Use the search option to quickly find the "payment receipts PDF generator" template. <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a> Filter and sorting options are also available. <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>
*   **Download the Template**: Click the download link next to the "payment receipts PDF generator" to open its dedicated page, which includes the Notion database and template. <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
*   **Understand the Template Structure**:
    *   The payment receipt template has predefined elements for PDF output. <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>
    *   Elements enclosed in curly braces (e.g., `{receipt number}`, `{customer name}`) are [[customizing_receipt_templates_with_placeholders | placeholder text elements]]. <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>
    *   These placeholders are automatically replaced by corresponding data from your Notion database columns (e.g., `customer name`, `amount paid`, `company address`). <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
    *   It is crucial that the exact information within the curly braces matches the corresponding column names in your Notion database for proper synchronization. <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>
*   **Duplicate the Template to Notion**:
    *   If the template is not yet published to the Notion Gallery, click the "Duplicate" option. <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>
    *   If published, click "Start with this template". <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>
    *   You will be prompted to select a Notion workspace to duplicate the template to, which is necessary to use it with PDF Output. <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>

## Connecting and Customizing

### Integrating Notion with PDF Output

1.  **Go to Settings**: After duplicating the template, navigate to the "Settings" section in PDF Output. <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>
2.  **Add Templates**: Click "click here to add templates" to add the duplicated template to PDF Output. <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>
3.  **Choose Workspace**: Select the Notion workspace where you duplicated the template. <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>
4.  **Allow Access**: Select the "payment receipts PDF generator" file and click "Allow Access". <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a> This process reads the template and database elements. <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>

### Customizing the Template

*   The entire template is [[customizing_templates_for_pdf_document_generation | customizable]] to fit your specific requirements. <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>
*   You can make elements bold, add spacing, or adjust formatting. <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>
*   Always ensure that placeholder elements intended for replacement from the database are placed inside curly braces for proper syncing and output generation. <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>
*   The exact naming convention of placeholder elements must match the corresponding column names in your Notion database. <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>

### Mapping Notion Properties

*   After selecting your Notion database and template within PDF Output (e.g., "payment receipts database" and "payment receipt template"), give it a name and click "Next." <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>
*   PDF Output automatically maps Notion database properties (columns) to the template elements if the names match. <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>
*   If any elements are mismatched or unmapped, you can manually search for and select the correct mapping. <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a> Filter, search, and sorting options are available to manage properties. <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>

## Generating PDF Receipts

*   **Export**: Once everything is set up and mapped, click "Export". <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>
*   **PDF Status Column**: PDF Output automatically adds a "PDF status" column to your Notion database, which indicates which rows have been generated. <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>
*   **Preview and Download**:
    *   After a successful export, you can click "Preview sample" to see a sample of the generated PDF payment receipt. <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>
    *   Click "Download all" to download all generated PDF files. <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>
    *   Each generated file corresponds to a specific row in your Notion database, with all elements placed correctly. <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>

## Additional Features and Settings

*   **Connections**: The "Connections" section shows all past connections, allowing you to quickly load existing database and template setups for future generation without manual re-entry. <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>
*   **Multiple Templates**: You can select and use multiple templates from the template section. <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>
*   **Watermark**: Users on the free plan will have a PDF Output watermark on generated templates. <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a> Upgrading to a paid plan removes the watermark. <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>
*   **Page Format**: In the settings, you can change the PDF page format. <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>
*   **Feedback and Help**: A feedback option is available for direct communication, and a help section provides a demonstration video to guide setup. <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>

This process allows for [[using_templates_to_automate_pdf_creation | automating PDF creation]] for payment receipts directly from your Notion database.