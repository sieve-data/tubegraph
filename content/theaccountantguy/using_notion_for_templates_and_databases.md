---
title: Using Notion for templates and databases
videoId: W_j9W6XedqM
---

From: [[theaccountantguy]] <br/> 

This article outlines how to generate bulk PDF documents using a Notion template and a Notion database, specifically focusing on payment receipts, with the help of PDF output.com <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## Core Components: Notion Template and Database

The process relies on two key Notion components:

1.  **Notion Template**: This is the base document for the PDF <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. It contains specific elements enclosed in curly braces (e.g., `{receipt number}`, `{customer name}`) which act as placeholders <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. These placeholders will be replaced with data from the database <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

2.  **Notion Database**: This database holds the information that will populate the template <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Each column in the database corresponds to an element in the Notion template (e.g., "receipt number" column for `{receipt number}`) <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Each row of information in the database will generate a separate PDF document <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. It is crucial to use the exact same naming convention, including spaces and capitalization, for database columns as for the elements in curly braces within the template to ensure automatic mapping <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

The tool used for this process is PDF output.com <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Step-by-Step Guide to Generating Bulk PDFs

### 1. Accessing and Duplicating Notion Components

Before generating PDFs, you need to duplicate the provided template and database to your own Notion workspace <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

*   **Log in to PDF output.com**: Navigate to PDF output.com and log in <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   **Locate Templates**: Go to the "Template" section on PDF output.com <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Find Specific Template**: Search for the desired template, for example, "payment receipts" <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   **Download/Duplicate Links**: Each template will have a "database link" and a "template link" <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. Click these links to open the Notion pages.
*   **Duplicate to Notion Workspace**:
    *   For both the template and the database, click the "Duplicate" button within Notion <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
    *   Select your desired Notion workspace (e.g., "accountant guy workspace") and click "Add to private" <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. This will add copies of the [[connecting_notion_database_and_template_for_pdfs | Notion template]] and database to your personal workspace <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

### 2. Connecting Notion Database and Template to PDF output.com

Once duplicated, connect your Notion components to PDF output.com:

*   **Add Database/Template**: On the PDF output.com interface, click "Click here to add database" or "Add template" <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   **Grant Notion Access**: You will be prompted to grant access to pages in Notion. Select the workspace where you duplicated the template and database <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   **Select Pages**: Choose both the duplicated Notion template and the Notion database from the list <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. Click "Allow access" <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Confirm Connection**: PDF output.com will authenticate and display the connected database and template <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
*   **Name Connection**: Provide a name for this connection, such as "Payment Receipts," and click "Next" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

### 3. Mapping Database Properties to Template Elements

After connecting, PDF output.com will load the database properties and template elements:

*   **Automatic Mapping**: If you maintained the exact naming convention for database columns and template placeholders (e.g., "company website" in the database for `{company website}` in the template), the system will automatically map them <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **Manual Mapping (if needed)**: If there's a mismatch, an element might show as "unmapped." Click on it and search for the corresponding database property to map it manually <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   **Filter and Sort**: Options are available to filter by unmapped or mapped properties, and to search or sort elements <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.

### 4. Generating and Downloading PDFs

Once all elements are correctly mapped:

*   **Create PDF**: Click "Create PDF" <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. The system will read the database rows and the template to generate the PDFs <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   **Preview Sample**: After successful export, you can preview a sample PDF to check the output <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   **Download All Documents**: Click "Download all documents" to receive a zip file containing all generated PDFs <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. Each row from your Notion database will result in a unique PDF document <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

## Additional Features of PDF output.com

*   **Connections**: The "Connections" section displays a list of previously created database-template pairings <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. Clicking on a saved connection will automatically load the database and template, bypassing the need to manually add them again <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.
*   **Templates**: This section provides access to various pre-defined templates for different use cases, such as invoices, besides payment receipts <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
*   **Upgrade**: The free plan includes a "Made with PDF output" watermark <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. Upgrading to a paid plan removes this watermark and offers higher generation limits <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.
*   **Settings**:
    *   **Page Format**: Allows defining the output PDF page format (e.g., A4 is default) <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
    *   **Add More Templates/Databases**: Provides an option to connect additional [[notion_finance_templates_and_databases | Notion templates and databases]] for future use <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Feedback**: A dedicated window to submit questions or feedback to the support team <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
*   **Custom Templates**: A help section explains how to use a custom PDF format for generating documents, independent of the predefined templates and databases <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
*   **Sidebar**: A small arrow icon allows collapsing the sidebar window for more screen space <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.

For any questions, you can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.