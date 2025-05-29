---
title: Automation of Document Export in Notion
videoId: Uh1g7uXtr_4
---

From: [[theaccountantguy]] <br/> 

This article explains how to [[Process of exporting PDFs from Notion | generate PDF documents]] for each row in a [[Notion]] database, automating what would otherwise be a manual export process <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The process involves setting up a database and a template in [[Notion]], and then using a third-party tool called [[Using Notion with PDF output | PDF output]] to [[Bulk Document Generation in Notion | generate PDF documents in bulk]] <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Notion Database and Template Setup

The demonstration uses an "application form database" where each row tracks applicant information like candidate profile and education requirements <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. The goal is to [[Generating PDF documents with Notion | create a PDF document]] for each of these rows without manually entering and exporting data <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

### Creating the Application Form Template
An application form template is created to match the database <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This template includes fields like full name, date of birth, gender, and phone number <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   **Placeholders:** All data fields in the template are placed inside curly brackets, for example, `{full name}`, `{date of birth}`, `{gender}`, and `{phone number}` <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. These placeholders must exactly match the column names in the [[Notion]] database <a class="yt-timestamp" data-t="01:01:03">[01:01:03]</a>.

### Applying the Template to Database Rows
Initially, the template can be manually copied and pasted into each row's page within the database <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   Open a database row <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   Scroll down to the empty section and paste the copied template content <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

### Automating Template Population for New Rows
To avoid manual copying for new entries, a default template can be set up <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>:
*   Click the drop-down next to "New" in the database <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   Select "New template" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
*   Name the template (e.g., "Applicant Name") <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
*   Paste the application form template into this new template <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   Click the three dots next to the template name and select "Set as default" for all views in the database <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   Now, any new row added to the database will automatically include this template <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## [[PDF document generation from Notion | Generating PDF Documents with PDF output]]

The tool used for [[Generating PDF documents from a Notion database | bulk document generation]] is [[Using Notion with PDF output | PDF output]] <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### Connecting Notion to PDF Output
1.  **Sign In:** Access the [[Using Notion with PDF output | PDF output]] dashboard <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
2.  **Copy Database URL:** Copy the URL of the [[Notion]] database from the browser's address bar <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Paste this URL into the designated field in [[Using Notion with PDF output | PDF output]] <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
3.  **Generate API Key:**
    *   In [[Notion]], navigate to "Settings & members" > "Integrations" > "Develop your own integrations" <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
    *   Click "New integration," provide a name, select the workspace, and save <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
    *   Copy the "Internal Integration Secret" key <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
    *   Paste this API key into the API key field in [[Using Notion with PDF output | PDF output]] <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
4.  **Connect Database to API Key:**
    *   In [[Notion]], open the database, click the three dots menu, and select "Connections" <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
    *   Search for and connect to the API key created earlier <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
5.  **Publish Database:** For [[Using Notion with PDF output | PDF output]] to access the database, it must be published <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
    *   In [[Notion]], click "Share" > "Publish" > "Publish" <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

### Generating the PDF Files
1.  **Load Database:** In [[Using Notion with PDF output | PDF output]], click "Load Database" <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
2.  **Select Naming Column:** Choose a column from the database (e.g., "Full Name") to use as the file name for the generated PDFs <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
3.  **Select Rows:** Choose which rows to generate PDFs for: "All rows," "Range of rows," or "Custom rows" <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
4.  **Generate PDF:** Click "Generate PDF" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
    *   [[Using Notion with PDF output | PDF output]] will populate the template with data from each selected row, replacing the curly bracket placeholders <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
    *   Settings like paper size and layout can be adjusted on the right side of the preview window <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
    *   Save each generated PDF to the desired location <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

The generated PDF files will be professionally formatted and named according to the selected column <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

### Alternative Method: Using a Standalone Notion Page as Template
Instead of embedding the template within each database row's page, you can use a separate [[Notion]] page as the main template <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
1.  Copy the URL of the standalone template page <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
2.  In [[Using Notion with PDF output | PDF output]], paste this template URL into the "Notion Page" field <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
3.  Click "Load Page" to display the template content <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
4.  Then, proceed with loading the database and generating PDFs as described above <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

## General Use Cases and Considerations
This method of [[PDF document generation from Notion | generating PDF documents]] can be applied to various scenarios beyond application forms, such as creating invoices from an invoice database <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

It is important to remember that the template file must be present within the database rows (or linked as a standalone page) for the generation to work <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. However, it's not mandatory for the notes or documentation within a [[Notion]] page to strictly match the database elements; [[Using Notion with PDF output | PDF output]] can still read the entire content and generate documents <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. This means you can also [[how_notion_can_assist_with_import_and_export_management | generate PDFs]] from pages containing general notes, lectures, or any other information <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

For assistance or pre-defined templates, the [[Using Notion with PDF output | PDF output]] website offers a contact section and a template section <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.