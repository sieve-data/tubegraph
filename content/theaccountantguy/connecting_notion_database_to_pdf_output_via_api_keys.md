---
title: Connecting Notion database to PDF output via API keys
videoId: Uh1g7uXtr_4
---

From: [[theaccountantguy]] <br/> 

This article explains how to [[generating_pdf_documents_from_notion_database_rows | generate PDF documents]] for each row of a Notion database automatically, utilizing the PDF Output tool and Notion API keys <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This method avoids manual data entry and individual exports <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Preparing Your Notion Database

To begin, you need a Notion database, such as an application form database, where each row contains information you want to convert into a separate PDF document <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

### Creating a Template for PDF Generation

1.  **Design the Template**: Create an application form template that mirrors the fields in your Notion database <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
    *   Use curly brackets `{}` around field names in the template (e.g., `{Full Name}`, `{Date of Birth}`, `{Gender}`, `{Phone Number}`) to act as placeholders <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. These must exactly match the column names in your database <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
2.  **Embed Template in Database Rows**:
    *   For existing rows, open each row and paste the template content into the empty page section at the bottom <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
    *   Alternatively, set up a default template for new rows <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>:
        *   Click the drop-down arrow next to "New" in your database <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
        *   Select "New template" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
        *   Give the template a name (e.g., "Applicant Name") <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
        *   Paste your prepared template content into this new template <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
        *   Click the three dots next to your new template and select "Set as default" for "All views" of the application form database <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. This ensures that every new row automatically includes the template <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

## [[using_api_keys_for_database_and_pdf_tool_connections | Connecting Notion to PDF Output]]

The PDF Output tool is used to [[generating_pdf_documents_using_notion_databases | generate documents in bulk]] from your Notion database <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### Steps to Integrate Databases with API Keys in Notion

1.  **Copy Database URL**: Copy the URL of your Notion database from the browser's address bar <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
2.  **[[setting_up_api_keys_in_notion | Set up an API Key in Notion]]**:
    *   In Notion, go to API key settings (usually via a link provided by PDF Output, or directly in Notion's settings under "Integrations") <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
    *   Click "New integration," provide a name, choose your workspace, and save <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   Once created, click on the new integration and copy the "Internal Integration Secret" <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. This is your API key <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
3.  **Connect Database to API Key**:
    *   Go back to your Notion database.
    *   Click the three dots `...` at the top right of the database <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
    *   Select "Connections" <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
    *   Search for and select the name of the API key (integration) you just created (e.g., "new key") and confirm the connection <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
4.  **Publish the Notion Database**:
    *   In your Notion database, click "Share" <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
    *   Click "Publish" and then "Publish" again to make the database live and accessible to PDF Output <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. This step is crucial for the tool to fetch pages <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

## Generating PDF Documents

With the Notion database prepared and connected, you can now [[generating_pdf_documents_using_notion_databases | generate PDF documents]].

1.  **Input Credentials in PDF Output**:
    *   Paste the copied Notion database URL into the designated field in PDF Output <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
    *   Paste the copied API key into the designated field <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
2.  **Load Database**: Click "Load database" in PDF Output <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
3.  **Configure PDF Naming and Rows**:
    *   Select the column to use as a reference for naming the PDF files (e.g., "Full Name") from the dropdown menu <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
    *   Choose which rows to generate PDFs for: "all rows," a specific "range of rows," or "custom rows" <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
4.  **Generate PDFs**: Click "Generate PDF" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
    *   The tool will process each selected row, automatically populating the template's placeholder fields with the corresponding data from the database <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
    *   On the right side of the PDF Output interface, you can adjust settings like paper size and layout if needed <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
    *   Save each generated PDF file to your desired location <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. The files will be named according to the column chosen earlier <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

## Alternative Method: Using a Separate Notion Page as Template

Instead of embedding the template within each database row, you can use a separate Notion page as the master template <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

1.  **Copy Template Page URL**: Copy the URL of your dedicated Notion template page <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
2.  **Input Page URL in PDF Output**: Paste this template page URL into the Notion page field in PDF Output <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
3.  **Load Page**: Click "Load page" to display the template on the right side <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
4.  **Load Database and Generate**: The remaining steps are similar to the primary method: load your database, select the naming column, and generate PDFs <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. This approach allows you to maintain the template separately from the database rows themselves <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.

## Additional Considerations

*   **Content Flexibility**: While using placeholder fields matching database properties is demonstrated, PDF Output can also convert any notes or documentation within a Notion page into a PDF, even if they don't contain specific placeholder elements <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. It will read the entire content of the page and generate the document <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **Use Cases**: This process is applicable for various document generation needs, such as creating invoices from an invoice database <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Support and Templates**: The PDF Output platform offers a contact section for support <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a> and a templates section with predefined templates for direct use <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.