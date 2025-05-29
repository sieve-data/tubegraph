---
title: Setting up Notion API keys for PDF document creation
videoId: 432wMcdqv1w
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to [[generating_pdf_documents_from_notion_database | generate PDF documents directly from a Notion database]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. To enable this functionality, the first essential step is to [[setting_up_api_keys_for_notion | set up the Notion API key]] <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## Initial Setup and Requirements
Before proceeding with [[creating_pdf_documents_from_a_notion_database | PDF document creation]], ensure you have:
*   **A Notion template**: This template will be used for PDF generation <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Placeholder text elements within the template (e.g., `{{client name}}`, `{{invoice number}}`) are marked with curly brackets and will be replaced by data from your Notion database <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   **A Notion database**: This database contains the information that will populate the PDF <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Each row of information represents a unique set of data <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## [[setting_up_api_keys_for_notion | Setting up the Notion API Key]]
The process involves configuring settings within the PDF Output interface:
1.  **Access Settings**: Click the "S" button or press 'S' on your keyboard to open the settings window <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
2.  **Page Format**: Specify the desired page format for the PDF; A4 is recommended for best output, though other options are available <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
3.  **Obtain API Key**:
    *   Click the provided link in the settings to get the Notion API key <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
    *   This will redirect you to your Notion account <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
    *   Click "New Integration" <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
    *   Provide a name for the new integration <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
    *   Select the Notion workspace you wish to link <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
    *   Keep the key type as "internal key" <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
    *   Click "Save" <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
4.  **Retrieve Secret Key**:
    *   Click "Configure internal integration settings" <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
    *   Click "Show" to reveal the secret key <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
    *   **Important**: Copy this key immediately and save it somewhere secure, as it will not be visible again once the window is closed <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
    *   Each user must create their own integration key, as it is secret and applicable only to the creator <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
5.  **Paste and Save in PDF Output**:
    *   Close the Notion integration window <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
    *   Paste the copied secret key into the "Notion API key" field in the PDF Output settings <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
    *   Click "Save" <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

### Connecting Notion Pages to the API Key
After [[setting_up_api_keys_for_notion | setting up the API key]] in PDF Output, you must connect your specific Notion template and database to this integration:
1.  **Navigate to Notion Page**: Go to your Notion template page or database page <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
2.  **Access Connection Options**: Click the three dots located in the top-right corner of the Notion page <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
3.  **Connect Integration**:
    *   Scroll down and select the "Connect" option <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
    *   Type or select the name of the integration you just created (e.g., "new integration") <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
    *   Click on it to establish the connection <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
4.  **Repeat for Database**: Follow the same steps for your Notion database to connect it to the integration <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

## Database Property for PDF Generation
For [[generating_pdf_documents_from_notion_database | PDF documents to be generated]] for specific rows in your Notion database, a "PDF status" property is crucial:
*   **PDF Status Property**: On the far right of your Notion database, you will find a property named "PDF status" <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   **Control Generation**: If this checkbox is checked, the PDF will **not** be generated for that row <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. If it is unchecked, PDF Output will generate a PDF for that row <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Ensure Unchecked**: Always ensure this "PDF status" checkbox in your database is unchecked for rows you wish to convert to PDF <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

## Mapping Notion Properties to Template Placeholders
Once the API key is set up and connections are made, PDF Output automatically reads information from your template and database:
*   **Automatic Mapping**: The tool automatically maps Notion database properties (columns) to the corresponding placeholder text elements in your Notion template <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   **Naming Convention**: To ensure automatic mapping, the naming convention for placeholder text in your template (e.g., `{{client name}}`) should exactly match the column names in your Notion database <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
*   **Manual Mapping (if needed)**: If an element is not automatically mapped (it will appear in gray), you can manually click on it and select the correct corresponding PDF element fetched from the Notion template <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. This step is important for a smooth PDF output <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
*   **Search and Filter**: You can use search <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a> and filter options (e.g., "unmapped properties," "mapped properties") <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a> to quickly find and manage properties.

Once all details are specified and mapped, you can click "Export" to begin [[creating_pdf_documents_from_a_notion_database | generating the PDF documents]] <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. After successful export, the "PDF status" checkboxes in your database will automatically be ticked <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.