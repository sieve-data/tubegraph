---
title: Creating PDF documents from a Notion database
videoId: Uh1g7uXtr_4
---

From: [[theaccountantguy]] <br/> 

This guide details how to [[generating_pdf_documents_from_notion_database | generate PDF documents]] for each row in a Notion database using the [[using_pdf_output_tool_with_notion | PDF Output]] tool. This method is useful for creating consistent documents, such as application forms or invoices, without manual entry for each one <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Setting Up Your Notion Database and Template

To begin, you need a Notion database containing the information you wish to convert into PDFs and a corresponding template.

### 1. Notion Database Structure
Your Notion database should track all the necessary information, such as an "Application Form database" tracking candidate profiles and educational requirements <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. For example, columns might include "Full Name," "Date of Birth," "Gender," and "Phone Number" <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

### 2. Creating the Template
Create a template that mirrors the fields in your database. This template will contain placeholders for your database content <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **Placeholder Fields**: Ensure that each field in your template that corresponds to a database column is enclosed in curly brackets, e.g., `{Full Name}`, `{Date of Birth}`, `{Gender}`, `{Phone Number}` <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. These will be automatically populated with data from your database <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### 3. Populating Database Rows with the Template
Each row in your database needs to contain the content of this template.
*   **Manual Copy-Pasting**: For existing rows, open each database entry, scroll to the bottom, and paste the template content <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   **Automating with Default Template**: To automatically apply the template to new rows:
    1.  Click the drop-down menu next to the "New" button in your database <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
    2.  Select "New template" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
    3.  Give your template a name (e.g., "Applicant Name") <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
    4.  Paste the template content into this new template page <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
    5.  Click outside the template to save it <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
    6.  Click the three dots next to your newly created template and select "Set as default" > "For all views and [database name]" <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
    Now, any new row added to the database will automatically include the template content <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

## Connecting Notion to PDF Output

The next step involves connecting your Notion database to the [[using_pdf_output_tool_with_notion | PDF Output]] tool.

### 1. Access PDF Output
Go to the [[using_pdf_output_tool_with_notion | PDF Output]] website and sign in <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

### 2. Obtain Notion Database URL
Copy the URL of your Notion database from your browser's address bar <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. Paste this URL into the designated field in PDF Output <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

### 3. Generate Notion API Key
[[setting_up_notion_databases_for_pdf_generation | PDF Output]] requires an API key to access your Notion data <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   Click the "click here to add API key" link in [[using_pdf_output_tool_with_notion | PDF Output]] <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   This will take you to your Notion API settings. Click "New integration" <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   Give it a name, select your workspace, and click "Save" <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   Once created, click on the integration name and reveal the "Internal Integration Secret" by clicking "Show" <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. Copy this key <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   Paste the copied API key into the corresponding field in [[using_pdf_output_tool_with_notion | PDF Output]] <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

### 4. Connect Database to API Key
You must explicitly connect your Notion database to the newly created API key.
*   In Notion, click the three dots (`...`) at the top right of your database <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
*   Go to "Connections" and search for the name of the API key you created (e.g., "new key") <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   Select it and click "Confirm" <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

### 5. Publish Notion Database
For [[using_pdf_output_tool_with_notion | PDF Output]] to access the database, it must be published.
*   In Notion, click "Share" at the top right of your database <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   Click "Publish" and then "Publish" again <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. This makes the database live and accessible to [[using_pdf_output_tool_with_notion | PDF Output]] <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

## Generating PDF Documents

With your Notion database and [[using_pdf_output_tool_with_notion | PDF Output]] connected, you can now [[bulk_pdf_document_generation_using_notion | generate PDF documents]] in bulk.

### 1. Load Database in PDF Output
In [[using_pdf_output_tool_with_notion | PDF Output]], click "Load database" <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

### 2. Configure PDF Generation
*   **Naming Convention**: Select a database column to use as the reference for naming the generated PDF files (e.g., "Full Name") <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
*   **Row Selection**: Choose which rows you want to generate PDFs for: "All rows," a "Range of rows," or "Custom rows" <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

### 3. Generate and Save PDFs
*   Click "Generate PDF" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   A preview window will appear for each document, showing the data populated from your database into the template <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. You can adjust settings like paper size and layout on the right side <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   Click "Save" for each PDF to download them to your desired location <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

### Output Verification
The generated PDFs will be named according to your selected column (e.g., "Carol Davis.pdf") <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. Each PDF will contain the template structure with the corresponding data from its Notion database row, creating professional-looking documents <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

## Alternative Method: Using a Separate Notion Page as Template

While the primary demonstration involves the template being inside each database page, [[using_pdf_output_tool_with_notion | PDF Output]] also supports using an external Notion page as the template for generation.

*   Instead of copying the template into each database row, you can provide [[using_pdf_output_tool_with_notion | PDF Output]] with the URL of the standalone Notion template page <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
*   Paste the template URL into the "Notion Page" field in [[using_pdf_output_tool_with_notion | PDF Output]] <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
*   Click "Load page" to load the template <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   Then, proceed to load your Notion database URL and generate PDFs as described above <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

This flexibility allows you to [[connecting_notion_databases_and_templates_for_pdf_creation | connect Notion databases and templates]] in a way that best suits your workflow, whether for [[generating_pdf_invoices_from_notion_database | generating PDF invoices]] or any other documentation <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. Note that it's not strictly necessary for the template's placeholder elements to match exact column names; [[using_pdf_output_tool_with_notion | PDF Output]] can read general content from the page as well <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

For more detailed guides and predefined templates, visit the [[using_pdf_output_tool_with_notion | PDF Output]] website's template section <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.