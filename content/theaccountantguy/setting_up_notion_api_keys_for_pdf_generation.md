---
title: Setting up Notion API keys for PDF generation
videoId: 432wMcdqv1w
---

From: [[theaccountantguy]] <br/> 
PDFOutput is a tool designed to [[generating_pdfs_from_notion_using_pdfoutput | generate PDF documents directly from a Notion database]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. To enable this functionality, [[integration_of_notion_with_pdf_generation | connecting Notion databases]] and templates using an API key is a crucial initial step <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Requirements

Before generating PDFs, ensure you have:
*   A Notion template (e.g., an invoice template with placeholder text in curly brackets) <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   A Notion database (e.g., an invoice database) containing the data that will replace the placeholder text in the template <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## Setting Up the Notion API Key

The first and most important step is to set up your Notion API key within PDFOutput <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

1.  **Access Settings**: In the PDFOutput interface, click on "S" (settings) or press "S" on your keyboard to open the settings window <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
2.  **Page Format**: You can specify the page format, with A4 being recommended for the best output <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
3.  **Obtain Notion API Key**: Locate the field for the Notion API key. Click the provided link ("click here") to be redirected to your Notion account <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
4.  **Create New Integration**: In your Notion account, click on "New integration" <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
    *   Provide a name for your new integration (e.g., "new integration window") <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
    *   Select the workspace you wish to link <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
    *   Keep the key type as "internal key" <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
    *   Click "Save" <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
5.  **Reveal and Copy Secret Key**:
    *   Click "configure internal integration settings" <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
    *   Click "show" to reveal the secret key <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
    *   **Important**: This key is secret and applicable only to the user who creates it; every user needs their own integration key <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
    *   Click "copy" and save this key somewhere safe, as it will not be visible again once the window is closed <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
6.  **Paste Key into PDFOutput**: Return to the PDFOutput settings window and paste the copied key into the "Notion API key" field <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
7.  **Save Settings**: Click "Save" <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

## Connecting Notion Databases and Templates

After setting up the API key in PDFOutput, you must connect your specific Notion database and template to this integration. This is part of [[connecting_and_setting_up_pdf_output_with_notion | connecting and setting up PDF output with Notion]] <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

1.  **Navigate to Notion Database/Template**: Go to your Notion template and database pages <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
2.  **Connect Integration**: On the top right of each page, find and click the three dots (`...`) <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
3.  **Select Connection**: Scroll down and click "Connect" <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
    *   Type the name of the integration you created (e.g., "new integration") and select it from the list <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
    *   Repeat this process for both your Notion database and your Notion template <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

Once these steps are completed, your API key setup is finalized, and your template and database are connected for [[using_notion_database_and_templates_for_pdf_generation | PDF generation]] <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

## PDF Status Property in Notion Database

For successful PDF generation, your Notion database should include a property named "PDF Status" (a checkbox) <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   If this checkbox is **unchecked**, PDFOutput will generate a PDF for that specific row of information <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   Once a PDF is generated for a row, PDFOutput will automatically **check** this box, indicating that the PDF has been produced <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

## Data Mapping and Generation

After [[setting_up_notion_database_for_pdf_document_templates | selecting the Notion database]] and template in PDFOutput, the tool reads information from both <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. It automatically maps Notion database properties (columns) to the corresponding placeholder text elements in the Notion template (e.g., "client name" in the database maps to `{client name}` in the template) <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

### Best Practices for Mapping
*   Ensure that the naming conventions for placeholders in your template (e.g., `{client name}`) exactly match the column names in your Notion database <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. This allows for automatic mapping <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
*   If an element is not automatically mapped (it will appear in gray instead of green), you can manually click on it and select the correct Notion template element from the fetched options <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

## Managing Connections

Once a connection is created, it can be loaded later without specifying all settings again. Click on the "C" (connections) icon in PDFOutput, select your saved connection name (e.g., "invoice generation"), and it will automatically load the previously defined settings <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.

## Future Outlook

Currently, [[using_api_keys_to_connect_notion_databases_with_pdf_output_tools | Notion API access]] relies on private integration keys, requiring each user to create their own <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. However, there is a possibility that Notion public API key access may become available in the future, which could simplify the setup process <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.