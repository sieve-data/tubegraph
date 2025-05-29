---
title: Integrating Notion pages and databases with PDFOutput
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

[[using_pdf_output_tool_with_notion | PDFOutput]] is a tool designed to [[generating_pdf_documents_from_notion_using_pdfoutput | generate PDF documents in bulk]] by leveraging a Notion page as a template and a Notion database to supply the data for replacement elements <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This enables efficient [[integrating_notion_with_pdf_output_for_document_creation | document creation]] from structured Notion data.

## How PDFOutput Works

PDFOutput integrates with Notion by:
*   Using a Notion page as a template <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.
*   Utilizing a Notion database that contains the data to replace elements in the template <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

Upon logging into [[using_pdf_output_tool_with_notion | PDFOutput]], users define their Notion database and Notion template within dedicated sections <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## [[creating_templates_and_databases_in_notion_for_pdf_generation | Creating Templates and Databases in Notion]]

Before linking to [[using_pdf_output_tool_with_notion | PDFOutput]], a Notion template and database must be created from scratch <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

### Designing the Notion Template
1.  **Create a New Page:** In your Notion workspace, click "create a new page" <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
2.  **Name the Template:** For example, "Invitation Letter Template" <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
3.  **Define Content:** Add the static content of your document <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
4.  **Add Placeholder Elements:** Critical sections that will be replaced by database information must be enclosed within curly braces, e.g., `{Title}` and `{Customer Name}` <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. These placeholders will be dynamically populated from the database <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Setting Up the Notion Database
1.  **Create a New Page:** Create another new page in Notion and select "Table" as the database type <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
2.  **Name the Database:** For example, "Invitation Letter Database" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
3.  **Define Columns:** The column names in the database **must exactly match** the placeholder names defined in the template (e.g., `Title`, `Customer Name`) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This ensures correct mapping <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
4.  **Populate Data:** Add rows to the database, with each row representing a unique set of information for a PDF document <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

## [[integrating_notion_databases_with_pdfoutput | Integrating Notion with PDFOutput]]

1.  **Add Database and Template:** In [[using_pdf_output_tool_with_notion | PDFOutput]], click to add your Notion database or template <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
2.  **Authorize Notion:** You will be redirected to Notion to select the specific pages (template and database) and grant access to your Notion account/workspace <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
3.  **Syncing:** [[using_pdf_output_tool_with_notion | PDFOutput]] will automatically fetch and sync the selected database and template for use <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
4.  **Define Connection Name:** Provide a name for the connection, such as "Invitation Letter" <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

## Mapping Properties

After establishing the connection, [[using_pdf_output_tool_with_notion | PDFOutput]] presents a mapping interface:
*   **Database Properties:** The left side displays all properties (columns) from your selected Notion database <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   **Template Elements:** The right side shows elements identified from your template, specifically those enclosed in curly braces <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   **Automatic Mapping:** If the database column names precisely match the template placeholder names, [[using_pdf_output_tool_with_notion | PDFOutput]] will automatically map them <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   **Manual Mapping:** If names differ, you can manually select and map the corresponding elements <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Utility Options:** Sorting, searching, and filtration options are available to manage properties efficiently <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

## [[generating_pdf_documents_from_notion_using_pdfoutput | Generating PDF Documents]]

Once properties are mapped:
1.  **Create PDF:** Click "Create PDF" to initiate the document generation process <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
2.  **Preview Sample:** A preview of a sample document (based on one row of your database) can be viewed <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
3.  **Download All:** You can then download all generated PDF documents, with each document corresponding to a row in your Notion database <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. For instance, three unique PDFs were generated for three rows of data in the demonstration <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

> [!warning] Important Note on Naming Conventions
> Always put placeholder text elements inside curly braces in your Notion template (e.g., `{Customer Name}`) <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. Ensure you use the **exact same naming convention** for the corresponding column headers in your Notion database <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. If names differ, manual mapping will be required in the mapping section <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## Additional Features and Navigation

[[using_pdf_output_tool_with_notion | PDFOutput]] provides a sidebar with various features:

*   **Connections:** This section displays all previously created database-template connections, allowing you to quickly reload and reuse them without setting up a new connection each time <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   **Templates:** Access a list of predefined templates. For any template, you can find a database link and a template link <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. To use a predefined template, you must duplicate both the database and the template file to your Notion workspace <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   **Upgrade:** Details on subscription plans. The free plan includes a "Made with [[using_pdf_output_tool_with_notion | PDFOutput]]" watermark and certain limitations <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
*   **Settings:**
    *   **Page Format:** Choose different PDF page formats <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
    *   **Add More Templates:** Subsequently add additional Notion templates and databases to [[using_pdf_output_tool_with_notion | PDFOutput]] <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   **Feedback:** Send direct messages to the developer for assistance or suggestions <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Help:** Access the full demonstration video <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.

The sidebar can be closed to maximize screen space <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.