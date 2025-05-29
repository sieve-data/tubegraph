---
title: Generating PDF documents in bulk with Notion
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

[[pdf_document_creation_with_notion_and_pdf_output | PDF Output]] is a tool designed to help users [[generating_pdf_documents_using_notion | generate PDF documents]] in bulk <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. It utilizes a Notion page as a template and a [[generating_pdf_documents_using_notion_databases | Notion database]] to supply the elements that need to be replaced within the template <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## How it Works

The process involves three main steps: preparing your Notion template and database, connecting them to [[pdf_document_creation_with_notion_and_pdf_output | PDF Output]], and generating the documents.

### 1. Preparing Notion Pages

Before [[using_notion_for_generating_pdf_documents | generating PDF documents]], you need to set up two key components within your Notion workspace: a template page and a database <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

#### Creating a Notion Template
The template is a Notion page that defines the layout and static content of your PDF documents <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.
*   **Create a new page:** Start by creating a new, blank Notion page <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   **Set to full width:** It's recommended to set the template page to "full width" mode <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   **Define content:** Add the static content for your document <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
*   **Placeholder elements:** For dynamic content that will be pulled from your database, enclose the text in curly braces, e.g., `{title}` or `{customer name}` <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. These placeholders will be replaced with data from your database <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

#### Creating a Notion Database
The database holds the unique information for each PDF document you want to generate <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.
*   **Create a new table database:** Add a new table database in Notion <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   **Column naming convention:** The column names in your database **must exactly match** the placeholder names defined in your template (excluding the curly braces) <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. For example, if your template has `{title}` and `{customer name}`, your database should have columns named "title" and "customer name" <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Populate rows:** Each row in the database will correspond to a single PDF document <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

### 2. Connecting to [[pdf_document_creation_with_notion_and_pdf_output | PDF Output]]

Once your Notion template and database are ready, connect them to [[pdf_document_creation_with_notion_and_pdf_output | PDF Output]]:
*   **Log in:** Access the [[pdf_document_creation_with_notion_and_pdf_output | PDF Output]] platform <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
*   **Add database/template:** Click on "click here to add database" or "add template" within the tool <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   **Select Notion pages:** You will be redirected to Notion to select the specific database and template pages you wish to use <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. Ensure you select the correct Notion account/workspace <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   **Allow access:** Grant access to [[pdf_document_creation_with_notion_and_pdf_output | PDF Output]] <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. The tool will automatically fetch the selected database and template <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
*   **Define connection name:** Provide a name for this connection, e.g., "invitation letter" <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   **Map properties:** [[pdf_document_creation_with_notion_and_pdf_output | PDF Output]] will automatically try to map database properties (columns) to template placeholders if their names match exactly <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. If names differ, you will need to manually select the correct mappings <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. Sorting and filtering options are available for mapping <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

### 3. Generating PDF Documents

Once mapping is complete:
*   **Create PDF:** Click on "create PDF" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. The tool will then generate a PDF for each row in your [[generating_pdf_documents_from_notion_database_rows | Notion database rows]], replacing the placeholders with the corresponding data <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Preview and Download:** You can preview a sample PDF <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a> and then download all generated documents <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. Each row from the database will result in a unique PDF document <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

### Important Note
Always put the placeholder text elements inside curly braces in your Notion template, and use the exact same naming convention for your database column names <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

## Features and Settings

[[pdf_document_creation_with_notion_and_pdf_output | PDF Output]] includes several helpful features:

*   **Connections:** All previously created connections (template-database pairs) are saved. You can load a predefined connection to quickly regenerate documents without re-selecting pages <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   **Templates:** The platform offers a list of predefined templates. Users can duplicate these templates and their corresponding databases to their Notion workspace to get started quickly <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.
*   **Upgrade Options:**
    *   **Free plan:** Includes a "made with [[pdf_document_creation_with_notion_and_pdf_output | PDF Output]]" watermark and certain limitations <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
    *   **Paid plan:** Allows for watermark removal and removes limitations <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.
*   **Settings:**
    *   **Page Format:** Choose your desired page format (e.g., A4, Letter) for the generated PDFs <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
    *   **Add more templates/databases:** Allows for adding additional Notion templates and databases to your account beyond the initial setup <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   **Feedback:** Users can submit feedback directly to the developer <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Help Section:** Provides access to demonstrations and tutorials <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.