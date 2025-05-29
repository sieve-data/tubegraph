---
title: Bulk Document Generation in Notion
videoId: Uh1g7uXtr_4
---

From: [[theaccountantguy]] <br/> 

This article details a method for generating bulk PDF documents from a Notion database using a third-party tool called PDF Output <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This process allows users to create individual PDF files for each row of a database, eliminating the need for manual data entry and one-by-one exports <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Core Components and Setup

The process relies on two main components within Notion:
1.  **A Notion Database**: This database stores the information to be used in the documents, such as application form requirements from candidate profiles to education details <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
2.  **A Notion Template**: This template defines the structure and content of the PDF documents <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

### Template Structure

The template uses placeholders in curly brackets (e.g., `{Full Name}`, `{Date of Birth}`, `{Gender}`, `{Phone Number}`) that correspond exactly to the column names in the Notion database <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. When the documents are generated, these placeholders are replaced with the actual data from each respective database row <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Populating Database Rows with the Template

There are two primary ways to ensure each database row contains the template content:

1.  **Manual Copy-Pasting (Initial Setup)**: For existing rows, the template content can be manually copied and pasted into the empty page section of each database entry <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
2.  **Automating Template Addition (for New Rows)**: To prevent manual repetition for new entries, a default template can be set for the database <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
    *   Click the dropdown next to "New" in the database <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
    *   Select "New template" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
    *   Give the template a name (e.g., "Applicant Name") <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
    *   Paste the template content into this new template <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
    *   Click outside to save <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
    *   Click the three dots next to the template name, select "Set as default," and choose "For all views and [database name]" <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
    *   Now, any new database entry will automatically include the template content <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

## Connecting Notion to PDF Output

The PDF Output tool is used to perform the [[generating_pdf_documents_with_notion | bulk PDF generation]] <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### Steps for Connection

1.  **Sign in to PDF Output**: Access the dashboard of the PDF Output tool <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
2.  **Copy Database URL**: Obtain the URL of your Notion database from the browser's address bar <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
3.  **Paste Database URL**: Paste the copied URL into the designated field in PDF Output <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
4.  **Generate Notion API Key**:
    *   Click "Click here to add API key" in PDF Output <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
    *   This redirects to Notion's API key settings <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
    *   Click "New integration," add a name, choose your workspace, and save <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   Locate the newly created key, click "Show" to reveal the "Internal integration secret," and copy it <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
5.  **Paste API Key**: Return to PDF Output and paste the copied API key <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
6.  **Connect Database to API Key**:
    *   In Notion, go to your database <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
    *   Click the three dots `...` (page menu) <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
    *   Select "Connections" and choose the name of your created API key (e.g., "new key") <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
    *   Confirm the connection <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
7.  **Publish Notion Database**:
    *   In Notion, click "Share" on the database <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
    *   Click "Publish" and then "Publish" again <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. This step is crucial for PDF Output to fetch database pages <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

## Generating the PDF Documents

Once connected, you can proceed with [[generating_pdf_documents_from_a_notion_database | generating PDF documents from a Notion database]]:

1.  **Load Database**: In PDF Output, click "Load Database" <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
2.  **Select Naming Column**: Choose a column from the dropdown (e.g., "Full Name") to use as the file name for the generated PDFs <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
3.  **Choose Rows**: Select whether to generate PDFs for "All Rows," a "Range of Rows," or "Custom Rows" <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
4.  **Generate PDF**: Click "Generate PDF" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
5.  **Review and Save**: A preview window will appear, showing the populated PDF with data from the corresponding Notion row <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. Users can adjust settings like paper size and layout if needed <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. Save each generated PDF to your desired location <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

The generated PDF files will be professionally formatted, with the file names matching the chosen naming column from the database <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

## Flexibility and Other Use Cases

*   **Diverse Document Types**: This method is applicable for [[generating_pdf_documents_with_notion | generating PDF documents with Notion]] for any form of document, such as [[creating_bulk_invoices_with_notion | creating bulk invoices with Notion]] <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Non-Matching Templates**: While matching placeholders to database fields is demonstrated, it's not strictly mandatory <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. The tool can also generate PDFs from general notes or documentation within Notion pages, even if they don't contain specific placeholder elements <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

## Alternative Template Method

Instead of embedding the template within each Notion database row, a separate Notion page can serve as the primary template <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>:

1.  Copy the URL of the Notion page containing the template <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
2.  In PDF Output, paste this URL into the "Notion Page" field <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
3.  Click "Load Page" to display the template <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
4.  Then, proceed to "Load Database" and follow the same steps for naming and generating PDFs <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>. This method still allows for [[generating_pdf_documents_from_a_notion_database | generating PDF documents from a Notion database]] <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

### PDF Output Resources
*   **Contact**: The PDF Output homepage includes a contact section for user support <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.
*   **Templates**: A template section offers predefined templates and databases for direct use, each with an associated instructional video <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.