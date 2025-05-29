---
title: Bulk Generating PDF Documents from Notion Database
videoId: Uh1g7uXtr_4
---

From: [[theaccountantguy]] <br/> 

This article details how to [[generating_pdf_documents_from_notion_using_pdfoutput | generate PDF documents]] in bulk from a Notion database using the PDFOutput tool <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This process avoids manual entry and exporting of individual documents <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Notion Database and Template Setup

To begin, you need a Notion database containing your data and a template that PDFOutput will use to structure the PDFs <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

### Creating the Template
Create a Notion page to serve as your template <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. For dynamic content from your database, include fields within curly brackets, e.g., `{Full Name}`, `{Date of Birth}`, `{Gender}`, `{Phone Number}` <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. These placeholder names must exactly match your database column names <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

### Populating Database Rows with the Template
There are two primary methods to ensure your database rows contain the template content:

1.  **Manual Copy-Pasting (Initial Setup):**
    For existing rows, open each row, scroll to the bottom, and paste the template content into the page body <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. This step ensures the template is available within each database entry <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

2.  **Automating with a Default Template:**
    To automatically include the template for new database entries, create a database template:
    *   Click the dropdown next to the "New" button in your database <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
    *   Select "New Template" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
    *   Name the template (e.g., "Applicant Name") <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
    *   Paste your template content into this new template page <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
    *   Click the three dots next to the template name in the dropdown and choose "Set as default" for "All views" and your specific database <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
    *   Now, any new row added to the database will automatically include the template content <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

> [!TIP]
> The template does not strictly need to have placeholder elements matching database fields. Any content within a Notion page can be converted to PDF <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. However, placeholders are necessary for dynamic data population.

## Integrating Notion with PDFOutput

[[integrating_notion_databases_with_pdfoutput | PDFOutput]] is the tool used for bulk PDF generation <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### Steps to Connect Notion and PDFOutput:
1.  **Sign in to PDFOutput:** Access the PDFOutput dashboard <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
2.  **Copy Database URL:** Copy the URL of your Notion database from your browser's address bar <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a> and paste it into the designated field in PDFOutput <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
3.  **Generate Notion API Key:**
    *   In PDFOutput, click "click here to add API key" <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
    *   This will take you to Notion's API settings. Click "New integration" <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   Give your integration a name, select your workspace, and save it <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
    *   Once created, click on the new integration and copy the "Internal Integration Secret" key <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
    *   Paste this key back into PDFOutput <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
4.  **Connect Database to API Key:**
    *   In your Notion database, click the three dots (`...`) at the top right <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
    *   Select "Connections" and search for the name of the API key you just created <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
    *   Click on the key name and confirm the connection <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
5.  **Publish Database:**
    *   Click the "Share" button in your Notion database <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
    *   Click "Publish" <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
    *   This makes the database accessible to PDFOutput <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. Publishing and connecting to the API key are crucial for PDFOutput to fetch database pages <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

## Generating PDF Documents

Once connected, you can proceed with [[exporting_pdf_documents_from_notion | generating PDF documents]]:

1.  **Load Database in PDFOutput:** Click "Load Database" in PDFOutput <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
2.  **Select Naming Column:** Choose a column from your database (e.g., "Full Name") to use as the filename for the generated PDFs <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
3.  **Select Rows to Generate:** You can choose to generate PDFs for all rows, a specific range, or custom selected rows <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
4.  **Generate and Save:** Click "Generate PDF" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. PDFOutput will then process each selected row:
    *   It populates the template placeholders with corresponding data from the database <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
    *   You can adjust settings like paper size and layout on the right side of the screen <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
    *   Save each generated PDF to your desired location <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. The files will be named according to your selected naming column <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

> [!INFO]
> This method of [[generating_pdf_invoices_in_bulk_with_notion | generating PDF invoices in bulk with Notion]] can be applied to any type of document, such as application forms, invoices, or personal notes <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

## Alternative Method: Using a Template URL Directly

Instead of embedding the template within each database row, you can link to a separate template page:

1.  **Copy Template URL:** Copy the URL of your main template Notion page <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
2.  **Paste in PDFOutput:** In PDFOutput, paste this template URL into the "Notion Page" field <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
3.  **Load Page:** Click "Load Page" <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. This will load the template content <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
4.  **Load Database:** Then, proceed to load your Notion database URL as described above <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
5.  **Generate PDFs:** Select the naming column and rows, then click "Generate PDF" <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. PDFOutput will use the externally linked template to populate data from your database rows <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

> [!NOTE]
> Both methods allow for [[exporting_notion_data_to_pdf | exporting Notion data to PDF]]. The first method ensures the template is embedded in each database entry, while the second uses a central template page <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.

## Additional Resources

*   [[exporting_and_managing_pdf_files_from_notion_database | Exporting and managing PDF files from Notion database]]: This process makes managing PDF files from Notion databases efficient.
*   [[creating_templates_and_databases_in_notion_for_pdf_generation | Creating templates and databases in Notion for PDF generation]]: Understanding the setup of templates and databases is key to successful generation.
*   [[creating_pdf_documents_with_notion_templates | Creating PDF documents with Notion templates]]: Templates are fundamental to structuring your PDF output.
*   PDFOutput provides a templates section with predefined options you can use <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>.
*   For further assistance, you can contact PDFOutput through their homepage contact section <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.