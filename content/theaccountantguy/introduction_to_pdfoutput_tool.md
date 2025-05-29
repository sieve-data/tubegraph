---
title: Introduction to PDFOutput tool
videoId: 432wMcdqv1w
---

From: [[theaccountantguy]] <br/> 

PDFOutput is a straightforward tool designed to generate PDF documents directly from a [[notion_with_pdf_output_tool | Notion]] database <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It functions by replacing placeholder text elements within a [[customizing_and_exporting_pdf_documents_with_pdf_output_tool | Notion template]] with data from a [[notion_with_pdf_output_tool | Notion database]] <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## How PDFOutput Works <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>

The PDFOutput interface requires users to specify connection details, select a Notion database, and choose a Notion template for PDF generation <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

### Core Components for PDF Generation

1.  **Notion Template:** A template, such as an invoice template, must be prepared in Notion. This template contains placeholder text elements enclosed in curly brackets (e.g., `{client name}`, `{invoice number}`) <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. These placeholders will be replaced with data from the Notion database <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
2.  **Notion Database:** A Notion database holds the specific data (e.g., client name, company, address, invoice details) that will populate the template <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Each row in the database typically represents a unique set of information for a document <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Setup and Configuration <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>

Before [[using_pdfoutput_features_and_settings | using PDFOutput]], several initial setup steps are required.

### Settings <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>

Access the settings window by clicking 'S' or pressing 's' on the keyboard <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   **Page Format:** Users can specify the desired page format for the PDF document <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. A4 is recommended for optimal output, but other options are available <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Notion API Key:** A crucial step is to set up the Notion API key <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
    *   Currently, [[integrating_notion_with_pdf_output_tool | Notion private integration keys]] are used <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
    *   To obtain the key, click the provided link in PDFOutput, which redirects to the Notion account to create a new integration <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
    *   Name the integration, select the workspace, keep it as an internal key, and save <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
    *   Configure internal integration settings to reveal the secret key, which should be copied and saved immediately as it's not visible after closing the window <a class="yt-timestamp" data-t="00:02:47">[00:03:20]</a>.
    *   Paste the copied API key into the specified field in PDFOutput and click 'Save' <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. Each user needs to create their own integration key <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

### Connecting Notion Pages <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>

Both the Notion template page and the database page must be connected to the created integration <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   In Notion, go to the top right three dots, scroll down to 'Connect', and search for and select the integration name <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. This must be done for both the template and the database <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

### PDF Status Property <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>

Within your Notion database, a property named `PDF status` is used <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   If this checkbox is *unchecked*, PDFOutput will generate a PDF for that row of information <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   If it is *checked*, a PDF will not be generated for that row <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   After successful generation, PDFOutput automatically checks this box <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

## [[using_pdf_output_interface_for_exporting_documents | Using PDF Output Interface]] <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>

After setup, return to the PDFOutput interface.
*   **Connection Name:** Provide a name for your connection <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   **Select Database:** Choose the desired Notion database from the dropdown list (databases connected via the API will appear here) <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   **Select Notion Template:** Select the Notion template that will be used <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   Click 'Next' <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

### Property Mapping <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>

PDFOutput automatically reads information from the template and database to map properties <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   Notion properties (columns from the database) are listed on the left <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   The tool attempts to automatically map these to the placeholder elements in the Notion template, especially if naming conventions are consistent <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. It's recommended that placeholder names (e.g., `client name`) exactly match database column names (`client name`) <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.
*   **Manual Mapping:** If an element is not automatically mapped (it will appear in gray), users can click on it to manually select the correct PDF element fetched from the Notion template <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   **Search, Sort, and Filter:** Options are available to search for specific properties, sort the list, and filter to show only unmapped or mapped properties <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.

## [[exporting_bulk_pdfs_with_pdf_output_tool | Exporting Bulk PDFs]] <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>

After mapping, click 'Export' <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
*   PDFOutput processes the documents, and the `PDF status` checkboxes in the Notion database are automatically ticked for generated PDFs <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **Preview Sample:** Users can preview the generated PDF document directly on the web interface <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Download All:** Click 'Download All' to download the generated PDF files to your local machine <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.
*   **Watermark:** A watermark appears on PDFs generated using the free plan, which is removed with paid plans <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

## Additional Features <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>

*   **Saved Connections:** Once a connection is created, it can be reloaded later, allowing users to reuse previously defined settings without re-specifying them <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
*   **Upgrade Options:** The basic plan allows a certain number of document downloads <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. Users can upgrade to Pro or Enterprise plans (monthly or yearly) for higher limits and features <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   **Templates:** Future updates will include a dedicated 'Templates' section showcasing available templates <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
*   **Feedback:** Users can submit feedback to the developer through the feedback window <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
*   **Help:** A help window will contain tutorial videos for reference <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.
*   **Sign Out:** Option to sign out from the profile icon <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

## Customization Tips <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>

When [[customizing_and_exporting_pdf_documents_with_pdf_output_tool | customizing templates]], ensure that placeholder names in curly braces in the Notion template (e.g., `{client name}`) exactly match the column names in your Notion database (e.g., `client name`) <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. This ensures automatic mapping and correct data import for PDF generation <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.

For assistance, users can reach out via email or social media platforms like Twitter or LinkedIn <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.