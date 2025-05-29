---
title: Creating PDF Documents from Notion Database
videoId: Uh1g7uXtr_4
---

From: [[theaccountantguy]] <br/> 

This article describes how to [[generating_pdf_documents_with_notion | generate PDF documents]] for each row in a [[notion_database_integration_with_pdf_generation | Notion database]] using the [[using_notion_with_pdf_output | PDF Output]] tool <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This process automates the creation of documents like application forms or invoices, eliminating the need for manual data entry and individual exports <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Preparing Your Notion Setup

To begin the [[setting_up_notion_templates_and_databases_for_pdf_generation | PDF document generation from Notion]], you need a Notion database and a corresponding template.

### 1. The Notion Database
Start with a Notion database where you track information, such as an application form database containing details like candidate profiles and education requirements <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

### 2. The Notion Template
Create an application form template that matches the fields in your database <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Key points for the template:
*   **Placeholder Fields:** All data fields in the template should be enclosed in curly brackets (e.g., `{Full Name}`, `{Date of Birth}`, `{Gender}`, `{Phone Number}`) <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. These placeholders must exactly match the column names in your Notion database <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

### 3. Populating Database Rows with the Template
Each row in your Notion database needs to contain the template content. There are two methods for this:

#### Manual Copy-Pasting (Initial Setup)
For existing database rows, open each row, scroll to the bottom, and paste the copied template content into the empty section <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. The exact same data from the template will appear in the database row <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

#### Setting a Default Template (Automated Future Setup)
To automate this for new rows:
1.  Click the dropdown arrow next to the "New" button in your database <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
2.  Select "New template" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
3.  Name the template (e.g., "Applicant Name") <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
4.  Paste your template content into this new template page <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
5.  Click outside the template editor to save <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
6.  Click the three dots next to the new template's name <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
7.  Select "Set as default" and then "For all views in [Database Name]" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
Now, any new row added to the database will automatically include the template content <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

## [[process_of_exporting_pdfs_from_notion | Generating PDF Documents]] with [[using_notion_with_pdf_output | PDF Output]]

The [[using_notion_with_pdf_output | PDF Output]] tool is used to [[generating_pdf_documents_from_a_notion_database | generate PDF documents in bulk]] from a Notion database <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

### Connecting Notion to [[using_notion_with_pdf_output | PDF Output]]
To connect your Notion database to the tool:

1.  **Copy Database URL:** Copy the URL of your Notion database from the browser's address bar <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Paste this URL into the designated field in [[using_notion_with_pdf_output | PDF Output]] <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.

2.  **Generate API Key (Internal Integration Secret):**
    *   In Notion, go to Settings & Members -> Integrations.
    *   Click "Develop your own integrations" -> "New integration" <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   Give it a name, select your workspace, and save <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
    *   Click on the newly created integration, then click "Show" to reveal the "Internal Integration Secret" <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. This is the API key you need <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. Copy it <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

3.  **[[connecting_notion_database_and_template_for_pdfs | Connect Database with API Key]]:**
    *   In Notion, open your database.
    *   Click the three dots in the top right corner <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
    *   Go to "Add connections" (or "Connections") <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
    *   Search for and select the name of the integration you just created <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
    *   Confirm the connection <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

4.  **Publish the Database:**
    *   In Notion, open your database.
    *   Click "Share" <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
    *   Click "Publish" <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. This makes the database accessible to [[using_notion_with_pdf_output | PDF Output]] <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. It is crucial for the tool to fetch pages from the database <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

### Generating the PDFs

1.  **Load Database in [[using_notion_with_pdf_output | PDF Output]]:** Paste the API key into the designated field in [[using_notion_with_pdf_output | PDF Output]] <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. Click "Load Database" <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

2.  **Select Naming Column:** Choose a column from your database (e.g., "Full Name") to use as the reference for naming the generated PDF files <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

3.  **Choose Rows:** Select whether to [[generating_pdf_documents_from_a_notion_database | generate PDFs]] for all rows, a specific range, or custom selected rows <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

4.  **Generate PDF:** Click "Generate PDF" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. The tool will process each row, automatically populating the template's placeholder fields with the corresponding data from your Notion database <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

### Output and Customization
*   **Preview and Verify:** A preview window will show the populated PDF for each row, allowing you to verify that the data has been correctly replaced <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
*   **Settings:** On the right side of the preview, you can adjust settings like paper size and layout <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
*   **Save:** Save the generated PDF files to your desired location <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. The filenames will correspond to the column selected for naming (e.g., "Carol Davis.pdf") <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

## Alternative Methods and Flexibility

While the primary method involves having the template within each database row, [[using_notion_with_pdf_output | PDF Output]] offers flexibility:

*   **Standalone Template Page:** You can use a dedicated Notion page as a template file directly. In this case, you would copy the URL of the standalone template page and paste it into the "Notion Page" field in [[using_notion_with_pdf_output | PDF Output]]. The tool will then load this page and combine it with data from your database to [[generating_pdf_documents_from_a_notion_database | generate PDFs]] <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

*   **Non-Matching Fields:** The content of your Notion pages does not strictly need to match the exact placeholder elements in your database. The tool can read the entire content of a page and [[generating_pdf_documents_from_a_notion_database | generate documents]] from it, even if placeholder text elements are not present <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. This allows for [[using_notion_as_a_template_and_database_for_pdfs | using Notion for various documentation]], handy notes, or lectures to be converted to PDF <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

## Use Cases and Support

This method of [[generating_pdf_documents_from_a_notion_database | generating PDF documents from a Notion database]] is applicable for any type of document, whether for business or personal use <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. Examples include generating invoices from an invoices database <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

For further assistance, the [[using_notion_with_pdf_output | PDF Output]] homepage provides a contact section and a template section with predefined templates that users can copy and adapt <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.