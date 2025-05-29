---
title: Creating and using application form templates
videoId: Uh1g7uXtr_4
---

From: [[theaccountantguy]] <br/> 

This article details how to create and use application form templates within Notion to generate PDF documents in bulk for each entry in a database, using the PDF Output tool <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Application Form Database Setup

An application form database is used to track various requirements, including candidate profiles and education details <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. The goal is to create a PDF document for each row of information without manual entry and individual exporting <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Creating and Customizing the Template

An application form template is created to match the structure of the application form database <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

### Placeholder Fields
The template includes specific fields (e.g., full name, date of birth, gender, phone number) enclosed within curly brackets (e.g., `{full name}`) <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. These bracketed fields correspond exactly to the column names in the Notion database, facilitating [[mapping_database_properties_to_templates | mapping database properties to templates]] when generating documents <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

### Adding the Template to Database Rows

Initially, the template content can be manually copied and pasted into the empty page section of each database row <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

### Automating Template Population
To avoid manually copying the template for new entries, a default template can be created within the Notion database:
1.  Click the drop-down arrow next to the "New" button in the database <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
2.  Select "New template" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
3.  Name the template (e.g., "applicant name") <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
4.  Paste the template content into the new template page <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
5.  Click outside the template to save it <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
6.  Click the three dots next to the created template and select "Set as default" for all views of the application form database <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

This ensures that whenever a new row is added, the template content is automatically populated, streamlining the [[creating_and_managing_templates_in_notion | creation and management of templates in Notion]] <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

## Generating PDFs with PDF Output

The PDF Output tool requires a Notion database to generate documents in bulk <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

### Connecting Notion to PDF Output

1.  **Copy Database URL**: Copy the URL of your Notion database from the browser's address bar <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
2.  **Generate API Key**:
    *   In PDF Output, click "click here to add API key" <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
    *   Create a new integration, name it, choose your workspace, and save <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   Copy the "Internal Integration Secret" key <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
3.  **Connect Database with API Key**:
    *   In Notion, click the three dots on the database <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
    *   Go to "Connections" and select the API key you just created <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
4.  **Publish Database**:
    *   Click "Share" on your Notion database <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
    *   Click "Publish" <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
    *   This step is crucial for PDF Output to fetch pages <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

### Generating PDF Documents

1.  **Load Database**: In PDF Output, paste the database URL and API key, then click "Load Database" <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
2.  **Select Naming Column**: Choose a database column (e.g., "Full name") to use as the reference for naming the generated PDF files <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
3.  **Select Rows**: Choose to generate PDFs for "all rows," a "range of rows," or "custom rows" <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
4.  **Generate PDF**: Click "Generate PDF" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. The tool will process each row, populate the template with data from the corresponding database fields, and display a preview <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
5.  **Save PDFs**: Save each generated PDF document <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. The files will be named according to the selected column <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

## Template Flexibility

While it's ideal for placeholder elements in the template to match database fields, it's not strictly mandatory <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. PDF Output can still read the entire content inside a Notion page and generate documents, even if it's just notes or other documentation <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. This allows for [[creating_and_using_notion_templates_for_pdfs | creating and using Notion templates for PDFs]] beyond strict form filling.

## Alternative Workflow

Instead of ensuring the template file is available within each database row, you can directly use the main Notion page URL of your template file in PDF Output's "notion page" field <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. This allows [[using_templates_and_databases_to_create_professional_pdfs | using templates and databases to create professional PDFs]] where the template is kept separate from the database content <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

## Additional Resources

PDF Output offers a "Templates" section with predefined templates that can be directly copied, along with instructional videos <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. This provides resources for [[utilizing_predefined_pdf_templates_for_efficient_workflow | utilizing predefined PDF templates for efficient workflow]] <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.