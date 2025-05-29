---
title: Generating PDF documents from Notion database rows
videoId: Uh1g7uXtr_4
---

From: [[theaccountantguy]] <br/> 

This article outlines how to [[generating_pdf_documents_using_notion_databases | generate PDF documents for each row in a Notion database]] automatically, without manually entering information or exporting documents one by one <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. The process involves setting up a Notion database and template, and then using a third-party tool called PDF Output <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

## Notion Database Setup

### Creating the Application Form Database
The demonstration uses an "application form database" where each row tracks application form requirements, such as candidate profile and education details <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

### Designing the Template
To facilitate PDF generation, an application form template is created that matches the database structure <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **Placeholder Fields**: Key data fields like "full name", "date of birth", "gender", and "phone number" are placed inside curly brackets `{}` within the template <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. These curly-bracketed fields correspond directly to the column names in the Notion database <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

### Populating Database Rows with the Template
Each row in the Notion database needs to contain this template <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
1.  **Manual Copy-Paste**: For existing rows, open each row, scroll to the bottom, and paste the template content <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
2.  **Automating with a Default Template**: To avoid manual repetition, especially for new rows, create a default template for the database <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>:
    *   Click the dropdown next to "New" in the database <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
    *   Select "New template" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
    *   Name the template (e.g., "applicant name") and paste the template content into it <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
    *   Set this template as default for all views of the application form database <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
    *   Now, whenever a new row is added, the template will automatically populate it <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

## Connecting Notion to PDF Output

The tool used for this process is PDF Output, which requires a Notion database to [[generating_pdf_documents_in_bulk_with_notion | generate documents in bulk]] <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. This step focuses on [[setting_up_and_connecting_notion_database_for_pdf_creation | setting up and connecting Notion database for PDF creation]].

### 1. Copy the Database URL
Obtain the Notion database URL from the browser's address bar <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### 2. Set Up Notion API Key
The database must be connected to PDF Output via an API key, which is private and confidential <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   In PDF Output, click the link to add an API key, which directs to Notion's API settings <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   Create a new integration, name it, select your workspace, and save <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   Once created, click on the integration and copy the "internal integration secret" (API key) <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
*   Paste this key into the designated field in PDF Output <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

### 3. Connect Database with API Key
The Notion database itself needs to be explicitly connected to the newly created API key <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   In your Notion database, click the three dots (`...`) menu <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   Go to "Connections" and select the name of the API key (e.g., "new key") you just created <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   Confirm the connection <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

### 4. Publish the Notion Database
For PDF Output to fetch pages inside the database, the database must be published <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
*   In Notion, click "Share" <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   Click "Publish" <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. This makes the database live and accessible to PDF Output <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

## Generating PDFs with PDF Output

This process demonstrates [[pdf_document_creation_with_notion_and_pdf_output | PDF document creation with Notion and PDF Output]].

1.  **Load Database**: In PDF Output, click "Load database" after entering the URL and API key <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
2.  **Name PDF Files**: Select a column from your database (e.g., "full name") to use as a reference for naming the generated PDF files <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
3.  **Select Rows**: Choose which rows to generate PDFs for: "all rows," a "range of rows," or "custom rows" <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
4.  **Generate PDF**: Click "Generate PDF" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
    *   The tool will automatically populate the template placeholders with the corresponding data from each Notion database row <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
    *   Users can adjust settings like paper size and layout on the right side of the interface <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
    *   Save each generated PDF file to your desired location <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

### Output
The generated PDF files will be named according to the selected column (e.g., "Carol Davis.pdf") and will contain the data from the corresponding Notion database row, formatted according to the template <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

## Key Takeaways and Additional Information

*   The crucial steps are to create a template with curly-bracketed placeholders matching database fields and ensure each database row contains this template (either manually or via a default template) <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   This method is applicable for [[generating_pdf_invoices_from_notion | generating PDF invoices from Notion]], or any other form of document for business or personal use <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

### Flexibility in Template Design
While matching placeholders to database fields is demonstrated, it's not strictly mandatory <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. PDF Output can read any content within a Notion page and [[generating_pdf_documents_using_notion | generate PDF documents using Notion]] from it, even if placeholder elements don't entirely match database content <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. This allows for [[using_notion_for_generating_pdf_documents | using Notion for generating PDF documents]] for notes, lectures, or other documentation <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

### Alternative Method: Using a Standalone Notion Page URL
Instead of embedding the template within each database row, you can directly provide PDF Output with the URL of a standalone Notion template page <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
1.  Copy the URL of the main template page <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
2.  In PDF Output, paste this URL into the "notion page" field <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
3.  Click "Load page" to load the template content on the right side <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
4.  Then, load the database URL as before, select the naming column, and generate PDFs <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. This method also works for [[integrating_notion_database_with_pdf_output | integrating Notion database with PDF Output]] and generating documents <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

### Resources
PDF Output offers a contact section for support and a template section with predefined templates for various use cases, complete with "how-to-use" videos <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. These resources can aid in [[setting_up_and_managing_notion_databases_for_pdf_generation | setting up and managing Notion databases for PDF generation]].