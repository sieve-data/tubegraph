---
title: Connecting Notion database with API for bulk document generation
videoId: Uh1g7uXtr_4
---

From: [[theaccountantguy]] <br/> 

This article describes how to connect a Notion database with an API-based tool, specifically PDF Output, to generate multiple PDF documents in bulk for each row of a database <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This process avoids the need for manual data entry and individual document export <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Overview and Goal

The primary goal is to [[creating_pdf_documents_from_a_notion_database | create a PDF document]] for each row of information in a Notion database <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. This method can be applied to various document types, such as application forms or invoices <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

## Setting Up the Notion Database and Template

To begin [[setting_up_notion_databases_for_pdf_generation | generating PDF documents from a Notion database]], two main components are required: a Notion database containing the data and a corresponding template.

### Database Structure
The Notion database should contain all the data necessary for the documents, such as candidate profiles and education requirements for an application form <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

### Template Creation
A specific application form template is created that matches the fields in the Notion database <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   Data fields within the template are enclosed in curly brackets (e.g., `{Full Name}`, `{Date of Birth}`, `{Gender}`, `{Phone Number}`) <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. These bracketed fields correspond exactly to the column names in the Notion database <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

### Populating Database Rows with the Template
For each row in the Notion database, the template content needs to be added <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
1.  Open a database row <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
2.  In the empty section, copy the template content (Ctrl+C/Cmd+C) and paste it into the row <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This will automatically populate the row with the template <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
3.  Repeat this process for all desired rows <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

#### Automating Template Population
To avoid manually copying and pasting the template for new rows <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>:
1.  Click the dropdown next to "New" in the database <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
2.  Select "New template" <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
3.  Name the template (e.g., "Applicant Name") and paste the template content into it <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
4.  Click the three dots next to the created template and select "Set as default" for all views of the application form database <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
Now, any new data added to the database will automatically include the template <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

## Utilizing the PDF Output Tool

The PDF Output tool is used to [[generating_pdf_documents_from_notion_database | generate PDF documents from the Notion database]] in bulk <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### Connecting Notion to PDF Output
The Notion database must be connected to PDF Output via an API key <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
1.  **Copy Database URL:** Copy the URL of the Notion database from the browser's address bar <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a> and paste it into the PDF Output tool <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
2.  **[[integrating_notion_with_an_api_key_for_database_access | Integrate Notion with an API key]]**:
    *   Access the API key settings by clicking the provided link in PDF Output <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
    *   Click "New integration," add a name, choose a workspace, and save <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   Copy the "Internal Integration Secret" key <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a> and paste it into the PDF Output tool <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
3.  **Connect Database to API Key:**
    *   In Notion, click the three dots on the database page <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
    *   Go to "Connections" and select the name of the created API key (e.g., "new key") <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
    *   Click "Confirm" to connect the database <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
4.  **Publish the Database:**
    *   In Notion, click "Share," then "Publish," and finally "Publish" again <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. This makes the database accessible to PDF Output and is crucial for fetching pages <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

### Generating the PDFs
1.  In PDF Output, click "Load database" <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
2.  Select the column to use for naming the PDF files (e.g., "Full Name") <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
3.  Choose which rows to process: "All rows," a specific range, or custom rows <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
4.  Click "Generate PDF" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
The tool will automatically populate the template with data from each row, replacing the placeholder elements <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. Users can adjust settings like paper size and layout on the right side of the tool <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. Finally, save each generated PDF file <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

### Output Verification
The generated PDF files will be named according to the selected column (e.g., "Carol Davis.pdf") and will contain all the corresponding data from the Notion database row <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. The output is professional and clean <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

## Alternative Method: Using a Separate Notion Page/Template

While the primary demonstration involved having the template content *inside* each Notion database row, an alternative method exists for [[connecting_notion_databases_and_templates | connecting Notion databases and templates]] without embedding the template in every row <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
1.  Instead of pasting the template into each database row, copy the URL of the standalone template Notion page <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
2.  In PDF Output, paste this template URL into the "Notion Page" section <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
3.  Click "Load page" to load the document <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
4.  Proceed with loading the database and [[generating_pdf_documents_from_notion_database | generating PDF documents from Notion database]] as described above <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

This method allows [[utilizing_notion_database_for_document_data | utilizing Notion database for document data]] while using a separate, central template file for PDF generation <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. It is not mandatory for the template's placeholder text elements to match the content inside the Notion page for the tool to work <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. The tool can read any content inside the page and generate documents <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

## Support and Resources
PDF Output offers predefined templates that can be directly copied, along with associated "how-to-use" videos <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. For further assistance, a contact section is available on the PDF Output homepage <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.