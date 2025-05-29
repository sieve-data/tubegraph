---
title: Generating payment receipts PDF using Notion
videoId: zrr8DW4PWz0
---

From: [[theaccountantguy]] <br/> 

This guide explains how to [[payment_receipt_pdf_generation | generate payment receipt documents]] using a Notion database and a Notion template with PDF Output <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Getting Started with PDF Output

1.  **Log In**: Navigate to PDFoutput.com and log in <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.
2.  **Access Templates**: Click on the "templates" option, which will open a new page listing all available templates <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
3.  **Select Payment Receipts Template**: Locate and click on the "payment receipts PDF generator" template <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
    *   You can use the search option to quickly find the document <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
    *   Filter and sorting options are also available <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
4.  **Download Template**: Click the "download link" next to the "payment receipts PDF generator" <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. This opens a new page displaying the payment receipts PDF generator page, which includes both the database and the template <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Understanding the Notion Template and Database

Once the template and database are open:
*   The database contains the raw data <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   The template is pre-defined with elements for the PDF output <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
*   **Placeholders**: Elements within curly braces (e.g., `{receipt number}`, `{customer name}`, `{amount paid}`) are placeholder texts <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. These placeholders will be replaced by corresponding data from the Notion database columns <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   **Matching Naming Convention**: It is crucial that the exact information within the curly braces in the template matches the corresponding column name in the Notion database <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. This ensures proper syncing and error-free PDF generation <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

## Duplicating and Adding the Template to Notion

1.  **Duplicate to Notion**: If the template is not yet published to the Notion Gallery, you'll see a "duplicate" option <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. Click this to duplicate the template to your Notion workspace <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. If published, click "start with this template" <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
2.  **Add to Workspace**: Select your desired Notion workspace (e.g., "add to private") <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. The template will then appear in your Notion workspace <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

## Configuring PDF Output Settings

1.  **Go to Settings**: In PDF Output, navigate to the "settings" section <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
2.  **Add Templates**: Click "click here to add templates" to add your duplicated Notion template to PDF Output <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
3.  **Choose Notion Workspace**: Select the Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
4.  **Select Pages**: Click "select pages" and choose the "payment receipts PDF generator" file <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
5.  **Allow Access**: Click "allow access" to enable PDF Output to read the template and database elements <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. Authentication should be successful <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

## Customizing the Template

The entire template is customizable to your specific requirements <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   You can make elements bold, add spacing, or change any formatting <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   Ensure that any placeholder elements you want to replace from your Notion database are enclosed in curly braces `{}` so they sync properly <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   The naming convention of placeholders in the template must exactly match the column names in your Notion database <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

## Mapping and Generating PDFs

1.  **Select Database and Template**: In PDF Output, refresh the page if needed <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. From the dropdowns, select the "payment receipts database" and the "payment receipt template" <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
2.  **Name the Output**: Give your output a name, e.g., "payment receipt" <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. Click "next" <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
3.  **Automatic Mapping**: PDF Output will automatically map the Notion properties (database elements) to the template elements if the names match <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
    *   If any elements are mismatched, you can manually search and select the correct mapping <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
    *   Filter, search, and sorting options are available in this view to help manage properties <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
4.  **Export**: Click "export" to begin the PDF generation <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
    *   A "PDF status" column will be added to your Notion database, indicating which rows have been generated <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.
    *   Once generated, you'll see an "export successful" message in PDF Output <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
5.  **Preview and Download**:
    *   Click "preview sample" to view a sample of the generated PDF <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
    *   Click "download all" to download all the generated PDF files <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. Each generated file corresponds to a specific row in your Notion database <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

## Additional Features and Tips

*   **Connections**: In the "connection" section of PDF Output, you can view past connections <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. Clicking on a past connection will automatically load the database and template, allowing for quick regeneration without manual setup <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   **Templates Section**: The "templates" section allows you to select multiple templates if needed <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   **Watermark**: On the free plan, generated PDFs will include a PDF Output watermark <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. Upgrading to a paid plan removes this watermark <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   **Page Format**: Under "settings," you can change the page format of the output PDFs <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. Remember to click "save" <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.
*   **Feedback and Help**: A feedback option is available to send messages directly to support <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. The "help" section provides demonstration videos for setting up the process correctly <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

For any questions, contact notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.