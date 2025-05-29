---
title: Creating Application Form Templates in Notion
videoId: Uh1g7uXtr_4
---

From: [[theaccountantguy]] <br/> 

This article details how to [[creating_templates_and_databases_in_notion | create templates]] for an application form database in Notion, primarily for the purpose of generating PDF documents for each entry. The process involves setting up a database, designing a corresponding template, and then automating the template's population within new database entries <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## The Application Form Database

The foundation is an "application form database" where information for each applicant is tracked <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This database typically includes fields such as:
*   Candidate profile <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>
*   Education requirements <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>
*   Other general application form requirements <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>

## Designing the Application Form Template

An "application form template" is created to match the fields present in the database <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This template serves as the layout for the final PDF document.

### Linking Template Fields to Database Properties

To dynamically populate the template with data from the database, the template uses placeholder fields enclosed in curly brackets <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. These placeholders must exactly match the column names in the Notion database <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

For example, if the database has columns like "Full Name", "Date of Birth", "Gender", and "Phone Number", the template would include:
*   `{{Full Name}}` <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
*   `{{Date of Birth}}` <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>
*   `{{Gender}}` <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>
*   `{{Phone Number}}` <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>

These placeholders are automatically replaced with the corresponding data from each database row when the PDF is generated <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

## Populating Database Rows with the Template

There are two primary methods for ensuring each row in your database contains the application form template:

### 1. Manual Copy-Pasting

Initially, you can manually copy the entire template content and paste it into the page associated with each row in your database <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
1.  Open a database row <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
2.  Scroll to the bottom of the page content <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
3.  Copy the content from your pre-designed template file <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
4.  Paste the template content into the empty section of the database row's page <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
5.  Repeat this for every existing row <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

### 2. Automating with a Default Template

To avoid manually copying the template for new entries, you can [[creating_and_linking_templates_in_notion | create and set a default template]] for the database <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. This ensures that every new row automatically includes the template <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
1.  Click the drop-down arrow next to the "New" button in your database <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
2.  Select "New template" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
3.  Give the template a name (e.g., "Applicant Name") <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
4.  Paste the application form template content into this new template page <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
5.  Click outside the template page to save it <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
6.  Click the three dots next to your newly created template in the dropdown <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
7.  Select "Set as default" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
8.  Choose "For all views" and select your "Application Form Database" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

Now, whenever a new row is added to the database, the template will be automatically populated within its page <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

## Utilizing Templates for PDF Generation

Once the database rows contain the templates with the correctly linked placeholder fields, a tool like PDF Output can be used to [[creating_pdf_documents_with_notion_templates | generate PDF documents]] in bulk <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>, <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. This tool reads the Notion database, populates the template fields with actual data from each row, and then converts each entry into a separate PDF <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

### Alternative Template Method

Instead of placing the template content directly inside each database row, you can also use a separate Notion page as the main template <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. In this scenario:
1.  Copy the URL of the main template Notion page <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
2.  Provide this template URL to the PDF generation tool <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
3.  The tool will then use this template in conjunction with the database to generate documents, replacing the placeholder elements as needed <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

This method works even if the notes or documentation within the database rows do not perfectly match the exact elements of the template <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. The tool will read the entire content of the page and generate the document <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.