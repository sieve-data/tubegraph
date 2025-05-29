---
title: Connecting Notion databases and templates
videoId: W_j9W6XedqM
---

From: [[theaccountantguy]] <br/> 

Connecting Notion databases and templates is a process used to generate bulk PDF documents by mapping information from a database to specific fields in a template <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This method utilizes a tool like PDF output.com to facilitate the document generation <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Core Concepts

The core idea involves:
*   A Notion template containing elements enclosed in curly braces (e.g., `{receipt number}`) that act as placeholders <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   A Notion database where each column corresponds to a placeholder in the template, holding the data to be inserted <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Each row in the database typically represents one document to be generated <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Preparing Notion for Connection

Before connecting the Notion components to a PDF generation tool, you need to prepare them within your Notion workspace.

### Duplicating Template and Database
1.  Navigate to the template section of the PDF output tool <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
2.  Find the desired template (e.g., "payment receipts") <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
3.  Click on the "template link" and "database link" provided <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
4.  Once the template page is open, click "Duplicate" and select your Notion workspace to add the template <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
5.  Repeat the duplication process for the database <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This ensures both the template and database are available in your local Notion workspace <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

### Naming Convention for Mapping
To ensure automatic mapping of data, it's crucial that the names within the curly braces in your template exactly match the column names (properties) in your [[creating_a_database_in_notion | Notion database]], including spaces and capitalization <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. For example, if your template has `{company website}`, your database should have a column named `company website` <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

## [[connecting_notion_databases_and_templates_for_pdf_creation | Connecting Notion Databases and Templates]] in PDF Output Tool

Once your Notion template and database are prepared, you can connect them to the PDF generation tool.

1.  Log in to PDF output.com <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
2.  The interface will prompt you to [[connecting_notion_databases_via_api | connect a Notion database]] and a Notion template <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
3.  Click "Click here to add database" or "Add template" <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
4.  This will request permission to access pages in your Notion workspace <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. Select your specific Notion workspace (e.g., "accountant guy") <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
5.  Select both the duplicated template and the duplicated database from the list and click "Allow access" <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
6.  Upon successful authentication, the connected database and template will be displayed <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
7.  Give the connection a name (e.g., "payment receipts") and click "Next" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

## [[mapping_notion_database_elements_to_templates | Mapping Notion Database Elements to Templates]]

After connecting, the tool will load and attempt to map the database properties to the template elements <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

*   **Automatic Mapping:** If the naming conventions of the template placeholders and database column names match exactly, the elements will be automatically mapped <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   **Manual Mapping:** If there are mismatches, an element may appear as unmapped <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. You can click on the unmapped field and search for the corresponding database property to manually connect it <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
*   **Filtering and Sorting:** Options are available to filter for unmapped or mapped properties, and to search or sort the elements <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.

## Generating PDF Documents

Once all elements are correctly mapped:
1.  Click "Create PDF" <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
2.  The tool will read the data from each row in the database and populate the template, generating a PDF document for each row <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
3.  After successful export, you can "Preview a sample" document to verify the output <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
4.  Click "Download all documents" to receive a package of all generated PDFs <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

## Managing Connections and Settings

The PDF output tool offers several features for managing your [[connecting_notion_database_with_api_for_bulk_document_generation | Notion database connections]] and templates.

*   **Connections:** The "Connections" section shows a list of all previously created connections, allowing you to quickly load a database and template combination without manually re-adding them <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. If connections don't load, a "Refresh" button can help <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
*   **Templates:** The "Templates" section provides access to a library of predefined templates for various use cases, such as invoices and payment receipts <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
*   **Upgrade:** Under the free plan, generated PDFs may include a "made with PDF output" watermark <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. Upgrading to paid plans removes this watermark and increases usage limits <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.
*   **Settings:**
    *   **Page Format:** Define the page format for your PDFs (e.g., A4) <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
    *   **Add Templates/Databases:** You can add additional templates and databases from the settings menu <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Feedback:** A feedback window is available for questions or suggestions <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
*   **Custom Templates:** The help section explains how to use custom PDF documents without relying on predefined templates <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.