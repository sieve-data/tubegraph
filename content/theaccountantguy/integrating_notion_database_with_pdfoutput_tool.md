---
title: Integrating Notion database with PDFoutput tool
videoId: 6PR3AESuBoA
---

From: [[theaccountantguy]] <br/> 

[[using_pdf_output_tool_with_notion | PDFoutput.com]] is a tool designed to [[generating_pdf_documents_from_notion_using_pdfoutput | generate PDF documents in bulk]] by utilizing Google Documents as templates and drawing data from a Notion database <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This integration allows for efficient creation of personalized documents such as invitation letters <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

## Getting Started with PDFoutput

To begin, navigate to [[using_pdf_output_tool_with_notion | PDFoutput.com]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

1.  **Sign In:** Click "create PDF" and sign in with a Google account <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.
2.  **Grant Access:** Enable the checkbox to give [[using_pdf_output_tool_with_notion | PDFoutput]] access to specific files, then click continue to be redirected to the homepage <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
3.  **Select Google Document Template:** Choose an existing Google Document from your Google Drive to serve as the template <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This template will contain placeholders (e.g., `{{first name}}`, `{{last name}}`) that will be replaced with data from Notion <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## Preparing the Notion Database

A Notion database is used to store the dynamic data that will populate your PDF documents <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

1.  **Create a New Page and Database:**
    *   In Notion, create a new page (e.g., "PDF output database") <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
    *   Type `/database` and select "inline" to create a new database <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
    *   Name the database (e.g., "database PDF output") <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
2.  **Define Columns:** Rename columns to match the placeholders in your Google Document template (e.g., "first name," "last name") <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
3.  **Populate Data:** Add rows to the database with the information you want to include in your PDFs (e.g., "Priya Sharma," "Miller Stark," "John quotes") <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## Connecting Notion to PDFoutput

Connecting your Notion database to [[using_pdf_output_tool_with_notion | PDFoutput]] requires a database URL and an API key <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

1.  **Obtain Database URL:** In Notion, with the database open, click "Share" and then "Copy link" to get the database URL <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. Paste this URL into the designated field in [[using_pdf_output_tool_with_notion | PDFoutput]] <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
2.  **Generate API Key:**
    *   In [[using_pdf_output_tool_with_notion | PDFoutput]], click "add API key" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. This will prompt you to create an API key in Notion's integration settings.
    *   Create a new internal integration (e.g., "notion PDF output connection") <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
    *   Copy the generated API key value <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. Paste this key into the API key field in [[using_pdf_output_tool_with_notion | PDFoutput]] <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
3.  **Connect Database to API Key:** Back in Notion, for your database, click the three dots, select "Connections," and choose the "PDF output connection" you just created <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Confirm the connection <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
4.  **Load Properties:** In [[using_pdf_output_tool_with_notion | PDFoutput]], click "Load properties" to fetch all column headers (properties) from your Notion database <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

## Configuring Output and Mapping Fields

Once connected, configure how your PDFs will be generated.

1.  **Output File Name:** Select a Notion property (e.g., "first name") from the dropdown to be used as the file name for the generated PDFs <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
2.  **Output Folder:**
    *   Choose between saving files to your Google Drive or your desktop's downloads folder <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
    *   To save to Google Drive, create a new folder (e.g., "invitation documents") in your Drive <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. Then, in [[using_pdf_output_tool_with_notion | PDFoutput]], click "add folder" and select the newly created Google Drive folder <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
3.  **Map Placeholders:** Replace the placeholder text in your Google Document template with the corresponding Notion properties. Click the property name in [[using_pdf_output_tool_with_notion | PDFoutput]] to copy it, then paste it into your Google Document (e.g., `{{First Name}}`, `{{Last Name}}`) <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

## Generating PDF Documents

With everything configured, you can now [[generating_pdf_documents_from_notion_using_pdfoutput | generate PDF documents from Notion using PDFOutput]] <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

1.  **Export PDF:** Click the "Export PDF" button in [[using_pdf_output_tool_with_notion | PDFoutput]] <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
2.  **Monitor Progress:** The tool will display a count of generated PDFs as it processes the documents <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
3.  **View Generated Documents:** Once complete, click "view in Google drive" to open the folder containing your newly created, personalized PDF documents <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. The documents will show the data from your Notion database inserted into the template <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

> [!TIP]
> The more information you add to your Notion database, the more documents [[using_pdf_output_tool_with_notion | PDFoutput]] can generate for your use case <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

## Additional Features

*   **Templates:** [[using_pdf_output_tool_with_notion | PDFoutput]] offers predefined templates that you can use for various purposes <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **History:** The "History" option allows you to view all documents generated in the past <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Upgrade:** You can upgrade to a specific plan by clicking the "Upgrade" option <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Contact:** For questions or queries, a contact section is available at the bottom of the page <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.