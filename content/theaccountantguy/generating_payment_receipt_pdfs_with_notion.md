---
title: Generating payment receipt PDFs with Notion
videoId: zrr8DW4PWz0
---

From: [[theaccountantguy]] <br/> 

This article details how to [[generating_pdf_documents_from_notion_using_pdfoutput | generate PDF payment receipt documents]] using a Notion database and a Notion template, leveraging the PDFOutput.com service.<a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>

## Getting Started

To begin, you need to log into PDFOutput.com.<a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a> Once logged in, you'll see an interface with a "Templates" option.<a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>

## Accessing and Duplicating the Template

1.  **Navigate to Templates**: Click on the "Templates" link to view a list of available PDF output templates.<a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>
2.  **Find the Payment Receipts Template**: Locate the "Payment Receipts PDF generator" template.<a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a> You can use the search option to find it quickly.<a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a> Filter and sorting options are also available.<a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>
3.  **Download/Open Template**: Click the "download" link next to the "Payment Receipts PDF generator".<a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a> This opens a new page displaying both the payment receipts database and its corresponding template.<a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
4.  **Duplicate to Notion**:
    *   If the template is not yet published to the Notion Gallery, you'll see a "start with this template" option.<a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>
    *   Otherwise, click the "duplicate" option.<a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>
    *   You will be prompted to select the Notion workspace where you want to duplicate the template.<a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a> The template needs to be duplicated to a Notion workspace to be used with PDFOutput.<a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>

## Understanding the Notion Template and Database

The payment receipt template contains predefined elements for the PDF output.<a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>

### Placeholder Elements
Elements enclosed in curly braces (e.g., `{receipt number}`, `{customer name}`) are placeholder text elements.<a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a> These placeholders are automatically replaced by corresponding values from your Notion database.<a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>

### Database Column Matching
Crucially, the exact information within the curly braces in the template **must match** the corresponding column names in your Notion database.<a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a> For example, if the template has `{customer name}`, your database must have a column named `customer name`.<a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a> This ensures proper syncing and error-free PDF generation.<a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>

### Customization
The entire template is customizable.<a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a> You can format elements (e.g., bold text), add spacing, and arrange the layout as needed.<a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a> Just ensure that any placeholder elements intended for replacement from the database remain within curly braces.<a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>

## Connecting Notion to PDFOutput

After duplicating the template to your Notion workspace:

1.  **Go to PDFOutput Settings**: In PDFOutput.com, navigate to the "Settings" section.<a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>
2.  **Add Templates**: Click "click here to add templates".<a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>
3.  **Select Notion Workspace**: Choose the Notion workspace where you duplicated the payment receipt template.<a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>
4.  **Select Pages**: Select the specific "Payment Receipts PDF generator" file.<a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>
5.  **Allow Access**: Click "allow access".<a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a> This allows PDFOutput to read your Notion database and template elements.<a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>

## Mapping and Exporting

1.  **Select Database and Template**: Once authenticated and elements are loaded, refresh the page if necessary.<a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a> From the dropdown menus, select the "payment receipts database" and the corresponding "payment receipt template".<a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>
2.  **Name the Export**: Give your export a name (e.g., "Payment Receipt").<a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>
3.  **Map Properties**: PDFOutput will automatically map Notion properties (database column names) to the template elements if the names match correctly.<a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a> If anything is mismatched, you can manually search and select the correct element to map.<a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a> Filter, search, and sorting options are available here.<a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>
4.  **Export**: Click "export".<a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>
    *   PDFOutput will automatically add a "PDF status" column to your Notion database.<a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>
    *   As each row's PDF is generated, its "PDF status" box will be ticked.<a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>
    *   A message indicating "export has been successful" will appear in PDFOutput.<a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>

## Reviewing Generated PDFs

After a successful export:

*   **Preview Sample**: Click "preview sample" to view a sample of the generated PDF.<a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>
*   **Download All**: Click "download all" to download a ZIP file containing all generated PDF receipts.<a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>
*   Each generated PDF file corresponds to a specific row in your Notion database.<a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>

## PDFOutput Features

*   **Connections**: In the "Connection" section, you can access past connections, allowing you to quickly load the database and template for subsequent generations without re-adding them manually.<a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>
*   **Templates**: You can select multiple [[using_pdf_output_templates_in_notion | templates]] if needed.<a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>
*   **Page Format**: Under settings, you can change the page format of the PDFs.<a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>
*   **Watermark & Upgrades**: On the free plan, generated PDFs will have a PDFOutput watermark.<a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a> You can upgrade your plan to remove the watermark.<a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>
*   **Feedback & Help**: A feedback option allows you to send messages directly to support.<a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a> The help section provides a demonstration video to assist with setup.<a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>

For any questions, you can reach out via email at notionformyuse@gmail.com.<a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>