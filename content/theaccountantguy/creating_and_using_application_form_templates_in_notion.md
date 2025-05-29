---
title: Creating and using application form templates in Notion
videoId: Uh1g7uXtr_4
---

From: [[theaccountantguy]] <br/> 

This article explains how to create and use application form templates in Notion to generate PDF documents in bulk for each row in a database <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. The process involves setting up a Notion database with specific fields, creating a template that uses these fields as placeholders, and then utilizing an external tool like "PDF output" to automate the PDF generation process <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Setting Up Your Notion Database and Template

To begin, you need an application form database in Notion where you track information such as candidate profiles and education requirements <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

Next, create an application form template that corresponds to your database <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This template should include fields from your database, such as "full name," "date of birth," "gender," and "phone number," placed inside curly brackets (e.g., `{Full Name}`) <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. These curly-bracketed fields act as placeholders that will be automatically populated with data from your database rows <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

### Populating Database Rows with Template Content

There are two primary ways to ensure your database rows contain the template information:

1.  **Manual Copy-Pasting**:
    For each row in your database, open the row and scroll to the bottom <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Copy the content of your prepared template (Ctrl+C or Command+C) and paste it into the empty section of the row <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. This will automatically bring the template's structure into that specific database row <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

2.  **[[creating_and_using_notion_templates | Creating and Setting a Default Notion Template]]**:
    To automate this process for new rows, you can [[creating_and_using_notion_templates | create a template]] within the database itself <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
    *   Click the drop-down arrow next to "New" in your database <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
    *   Select "New template" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
    *   Give your template a name, like "Applicant Name" <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
    *   Scroll to the bottom and paste your application form template content here <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
    *   Click outside the template to save it <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
    *   Click the three dots next to your newly created template in the drop-down menu <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
    *   Select "Set as default" and choose "For all views in application form database" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
    Now, whenever you add a new row, the template will be automatically populated, eliminating the need for manual copying and pasting <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

## Generating PDFs with "PDF output"

The "PDF output" tool is used to generate documents in bulk from your Notion database <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### Connecting Notion to PDF output

1.  **Copy Database URL**: Copy the URL of your Notion database from the browser's address bar <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
2.  **[[creating_and_using_notion_templates | Create an API Key/Integration]]**:
    *   In Notion, go to "Settings & members" > "Integrations" <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
    *   Click "Develop your own integrations" <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
    *   Click "+ New integration" <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   Provide a name for your integration, choose your workspace, and save <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
    *   Once created, click on the integration's name, then click "Show" next to "Internal Integration Secret" to reveal the API key <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. Copy this key <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
3.  **Paste Information into PDF output**:
    *   Paste the copied database URL into the "Database URL" field in PDF output <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
    *   Paste the API key into the "API Key" field <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
4.  **Connect Database to API Key**:
    *   In Notion, click the three dots at the top right of your database <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
    *   Go to "Connections" and select the API key you just created (e.g., "new key") <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. Confirm the connection <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
5.  **Publish Database**:
    *   Click "Share" at the top right of your Notion database <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
    *   Click "Publish" and then "Publish" again to make the database live and accessible to PDF output <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. This step is crucial for the tool to fetch pages <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

### Generating the PDFs

1.  **Load Database**: In PDF output, click "Load Database" <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
2.  **Select Naming Column**: Choose a column from your database (e.g., "Full Name") to use as the reference for naming the generated PDF files <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
3.  **Select Rows**: Decide whether to generate PDFs for "all rows," a "range of rows," or "custom rows" <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
4.  **Generate PDF**: Click "Generate PDF" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. A window will pop up, displaying the populated application form for each row, replacing the placeholder elements with corresponding data from the database <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
5.  **Save PDFs**: You can adjust settings like paper size and layout on the right side of the window <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. Save each generated PDF file <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

## Output Review

The generated PDF files will be named according to the column you selected (e.g., "Carol Davis.pdf") <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. The content of each PDF will be clean, professional-looking, and accurately populated with data from its respective Notion database row <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

### Key Requirements for Success

*   The template form must have fields enclosed in curly brackets that exactly match the column names in your Notion database <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
*   The template file must be present inside each of the database rows for which you want to generate a PDF <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   [[creating_and_using_notion_templates | Setting a default template]] for new rows automates this process <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.

## Alternative Template Usage

While this demonstration focused on matching placeholder elements, PDF output can also generate documents from any Notion page content, even if it doesn't contain matching placeholders <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. It will read the entire content of the page and generate a document <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. This allows you to generate PDFs of notes, lectures, or any other documentation stored in Notion <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

### Using a Direct Template URL

Instead of having the template content within each database page, you can directly use the template file's URL in PDF output <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
*   Copy the URL of your main template page <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
*   Paste this URL into the "Notion Page" field in PDF output <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
*   Click "Load Page" to load the template content <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   Then, proceed with loading your database and generating PDFs as before <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

## Additional Resources

The "PDF output" website also features a [[creating_and_using_notion_templates | template section]] with predefined templates that can be directly copied and used with their corresponding databases <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. These templates often include associated "how-to-use" videos for guidance <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.