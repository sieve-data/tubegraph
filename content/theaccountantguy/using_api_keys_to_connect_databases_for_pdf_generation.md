---
title: Using API keys to connect databases for PDF generation
videoId: 5lnQYIpvjnM
---

From: [[theaccountantguy]] <br/> 

This article outlines the process of generating PDF documents in bulk from a Notion template, leveraging a Notion database and an API key with the help of PDFOutput (pdf4put.com) <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This method allows for the dynamic replacement of information from a database into a templated document to create multiple unique PDF files <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Preparing the Notion Template

A professional invoice template created in Notion is used as an example <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.
*   **Template Structure**: The template includes all necessary invoice information <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.
*   **Data Replacement Fields**: Specific information intended for replacement from the database is placed within curly brackets (e.g., `{client name}`, `{client company}`, `{client address}`) <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. These fields in the Notion template must correspond to column names in the database <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
*   **Making the Page Public**: Before use, the Notion page containing the template must be made public. This is done by clicking "Share," then "Publish," and again "Publish" to make the page available for external use <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. The page link can then be copied <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## Preparing the Notion Database

A Notion database containing different invoice-related information is used to populate the template <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. For instance, a database with three records can be used to generate three distinct PDF documents <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. The database holds the actual values that will replace the curly-bracketed fields in the template <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

## [[setting_up_pdfoutput_with_api_keys | Connecting Notion to PDFOutput using API Keys]]

[[connecting_notion_databases_with_external_tools_using_api_keys | Connecting Notion databases with external tools using API keys]] is crucial for this process.
1.  **Sign-in to PDFOutput**: Access pdf4put.com and sign in with your account <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
2.  **Provide Notion Page URL**: Paste the copied Notion template page URL into PDFOutput <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. Click "Load Page" to confirm the template appears correctly <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
3.  **[[configuring_api_keys_for_notion_integration | Create Notion API Key]]**:
    *   In PDFOutput, click the link to "add notion API key" <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This opens a Notion window.
    *   Click "New integration," provide a name (e.g., "new key"), choose your account, and click "Save" <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
    *   Go to "Integrations," click on the newly created key, click "Show," and then "Copy" the API key <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
    *   Paste this API key into PDFOutput <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. This key facilitates [[connecting_notion_databases_with_pdf_generation_tools | connecting Notion databases with PDF generation tools]] <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
4.  **[[connecting_notion_database_to_pdf_generator | Connect Notion Database to API Key]]**:
    *   Go back to your Notion database. Click the three dots on the top right, then "Connections" <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
    *   Search for and select the API key you just created (e.g., "new key") <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. Click "Confirm" to establish the connection <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
5.  **Fetch Database URL**: Copy the URL of the Notion database from your browser's address bar <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. Paste this URL into PDFOutput <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

## [[generating_bulk_pdfs_with_database_integration | Generating Bulk PDFs]]

With the template URL, API key, and database URL provided, the system is ready to generate PDFs <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
1.  **Load Database**: Click "Load Database" in PDFOutput <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
2.  **Choose Naming Column**: Select a database column to name the generated files (e.g., "invoice number") <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
3.  **Select Rows**: Choose to generate PDFs for "all rows," "custom rows" (e.g., fourth through seventh), or a "specific row" <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
4.  **Initiate Generation**: Click "Generate PDF" <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. The system will then begin [[generating_pdfs_from_database_entries | generating PDFs from database entries]], populating the template with data from each record <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
5.  **[[working_with_databases_and_data_replacement in PDF templates | Working with databases and data replacement in PDF templates]]**: As each PDF is generated, values like client name, company, and address are fetched from the database and used to replace the corresponding fields in the template <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

### Customization
*   **Layout Settings**: Adjust paper size (e.g., A4, Letter), orientation (portrait/landscape), and specify which pages to print <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   **Saving Files**: Each PDF is saved with the chosen naming convention (e.g., invoice number) <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

## Key Reminders and Troubleshooting

*   The Notion template page **must be shared and publicly accessible** <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   The Notion database **must be connected to the API key** you created in Notion <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **[[utilizing_api_keys_to_connect_notion_to_pdf_generation_tools | Utilizing API keys to connect Notion to PDF generation tools]] with Relational Properties**: If your database uses relation properties (linking to other databases), **all related databases must also be connected to the same API key** for seamless data fetching <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

For any queries or assistance, you can reach out via email at notionformyuse@gmail.com or use the contact window on the PDFOutput site <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.