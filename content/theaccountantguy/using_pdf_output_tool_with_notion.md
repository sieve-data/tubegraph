---
title: Using PDF Output Tool with Notion
videoId: Uh1g7uXtr_4
---

From: [[theaccountantguy]] <br/> 

The PDF Output tool facilitates [[generating_pdf_documents_from_notion_using_pdfoutput | generating PDF documents from Notion]] database rows in bulk <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This eliminates the need for manually entering information and [[exporting_pdf_documents_from_notion | exporting documents one by one]] <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Components Needed

To [[integrating_notion_with_pdf_output_for_document_creation | integrate Notion with PDF Output]] for document creation, you need:
1.  A Notion database with structured information <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.
2.  A Notion template matching the database fields, often using curly brackets for placeholders <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
3.  Access to the PDF Output tool <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

## Preparing Your Notion Database

First, ensure your Notion database contains the data you wish to convert into PDFs. For example, an application form database tracks details like candidate profile and education requirements <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

Next, create a template page in Notion that mirrors your database structure <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **Placeholder Fields:** Use curly brackets `{}` around field names in the template (e.g., `{Full Name}`, `{Date of Birth}`, `{Gender}`, `{Phone Number}`) <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. These placeholders must exactly match the column names in your Notion database <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   **Embedding the Template:**
    *   **Manual Method:** For each row in your database, open it and paste the content of your template into the page body <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. This ensures the template is available within each row's page <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
    *   **Automated Method (Recommended):**
        1.  Click the drop-down next to "New" in your database <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
        2.  Select "New template" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
        3.  Name the template (e.g., "Applicant Name") <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
        4.  Paste your template content into this new template page <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
        5.  Click the three dots next to the new template's name, choose "Set as default," and then select "For all views" for your specific database <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
        *   This setup ensures that whenever a new row is added, the template content is automatically populated <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

## [[integrating_notion_database_with_pdfoutput_tool | Integrating Notion with PDFOutput Tool]]

1.  **Sign in to PDF Output:** Access the PDF Output web application <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
2.  **Get Notion Database URL:** Copy the URL of your Notion database from your browser's address bar <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Paste this URL into the designated field in PDF Output <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
3.  **Generate API Key and Connect:**
    *   Click "Click here to add API key" in PDF Output <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
    *   In Notion, go to "Settings & members" > "Integrations" > "Develop integrations" > "New integration" <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   Name your integration, choose your workspace, and save <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
    *   Copy the "Internal Integration Secret" from the newly created integration <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
    *   Paste this API key into the PDF Output tool <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
4.  **Connect Database to API Key:**
    *   In your Notion database, click the three dots menu <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
    *   Select "Connections" and find the name of the API key you just created (e.g., "new key") <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
    *   Click on your API key and confirm <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
5.  **Publish Notion Database:**
    *   In your Notion database, click "Share" > "Publish" > "Publish" <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. This makes the database accessible to PDF Output <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

## [[generating_pdf_documents_from_notion_using_pdfoutput | Generating PDF Documents]]

1.  **Load Database:** In PDF Output, click "Load Database" <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
2.  **Select Naming Column:** Choose a column from your database (e.g., "Full Name") to use as the reference for naming the generated PDF files <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
3.  **Choose Rows:** Select whether to generate PDFs for "All rows," a "Range of rows," or "Custom rows" <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
4.  **Generate PDF:** Click "Generate PDF" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
    *   The tool will then process each selected row, automatically populating the template with the corresponding data from the database <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
    *   You can adjust settings like paper size and layout on the right side of the generation window <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
    *   Save each generated PDF to your desired location <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

The generated PDF files will be professionally formatted, with content from each Notion database row filling the template placeholders <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

## Important Considerations

*   **Template Matching:** Ensure the placeholder fields in your template (e.g., `{Full Name}`) exactly match the column names in your Notion database <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   **Template Availability:** The template file must be present inside the page for each row of the database for the tool to generate files <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. Using the default template option ensures this for new rows <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Flexibility:** While matching placeholder elements with database fields is common, you can also use PDF Output to generate documents from any Notion page content (notes, lectures, general documentation), even if it doesn't strictly match database elements <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. The tool will read the entire content of the page and generate the document <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

## Alternative Method: Using a Notion Page as a Template

Instead of embedding the template within each database row, you can directly use a Notion page URL as the template:
1.  Copy the URL of your main Notion template page <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
2.  In PDF Output, paste this URL into the "Notion Page" field <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
3.  Click "Load Page" to load the document <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
4.  Then, proceed to "Load Database" and select your database and naming column, similar to the first method <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
5.  Click "Generate PDF" <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. This method allows you to use a separate template page without needing to copy its content into every database row <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

This demonstrates two ways to [[creating_pdf_documents_with_notion_templates | create PDF documents with Notion templates]] using PDF Output: either with the template embedded in each database row or by referencing a separate template page <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.

For additional help, the PDF Output website provides a contact section and a template section with predefined templates and associated "how-to-use" videos <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.