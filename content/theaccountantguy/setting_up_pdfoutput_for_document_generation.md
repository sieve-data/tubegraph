---
title: Setting up PDFOutput for document generation
videoId: lCyhl8mofjE
---

From: [[theaccountantguy]] <br/> 

This article provides a tutorial on how to use [[introduction_to_pdf_output_tool | PDF Output]] to generate documents, specifically lease agreements, from a Notion database and Notion page. <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>

## Preparation

Before beginning, it is essential to prepare your template and database, and perform the initial setup for [[introduction_to_pdf_output_tool | PDF Output]].

### Setting up Your Notion Template

The document generation process relies on a template with placeholder text elements that will be replaced by data from your database <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   **Template Structure**: Create a template (e.g., a lease agreement) that includes all necessary details <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.
*   **Placeholder Text**: Insert placeholder texts for variable information using curly braces. For example, `{{landlord name}}`, `{{tenant name}}`, and `{{street address}}` <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

### Setting up Your Notion Database

Your Notion database will serve as the source of information for populating the template.
*   **Database Properties**: Ensure your database includes properties (columns) that correspond to the placeholder texts in your template <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. For instance, if your template has `{{landlord name}}`, your database should have a "Landlord Name" property <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **Data Entry**: Each row in the database will represent a unique document to be generated, with specific values for each property <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

> [!tip] Naming Convention
> To facilitate automatic mapping, ensure that the naming convention of your database properties exactly matches the placeholder texts in your template (excluding the curly braces) <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

### Initial [[introduction_to_pdf_output_tool | PDF Output]] Setup

1.  **Log In**: Access the [[introduction_to_pdf_output_tool | PDF Output]] platform <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
2.  **Help Section**: Navigate to the "Help" section within the [[introduction_to_pdf_output_tool | PDF Output]] interface <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
3.  **Follow Tutorial**: Adhere to the setup tutorial provided, which includes instructions for setting up API keys and other preliminary steps necessary for document generation <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

## Connecting Notion with [[introduction_to_pdf_output_tool | PDF Output]]

Once initial setup is complete, you can establish the connection between your Notion assets and [[introduction_to_pdf_output_tool | PDF Output]].

1.  **Connection Name**: Specify a descriptive name for your connection, such as "Lease Agreement" <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
2.  **Select Database**: From the dropdown menu, choose the Notion database you prepared earlier (e.g., "lease") <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This menu displays all databases connected via your API key <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
3.  **Select Template**: Similarly, select your Notion template (e.g., "lease template") <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
4.  **Proceed**: Click "Next" to continue <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## Mapping Database Properties to Template Elements

After proceeding, [[introduction_to_pdf_output_tool | PDF Output]] will load your database and template elements.

*   **Automatic Mapping**: The tool automatically maps Notion properties (from your database, displayed on the left) to the corresponding [[utilizing_pdf_output_for_document_generation | PDF elements]] (template placeholders, displayed on the right) if their names match <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. For example, "Landlord Name" from the database will map to `{{landlord name}}` in the template <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Manual Mapping**: If a field is not automatically mapped, it will appear in gray <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. Clicking on it will show available properties, with unmapped ones highlighted in red <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. You can manually select the correct property to map it <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

## Generating and Downloading Documents

Once mapping is confirmed, you can generate your PDF documents.

1.  **Initiate Export**: Click "Export" to start the document generation process <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
2.  **PDF Status Property**: A new "PDF Status" column will appear in your Notion database <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. This column tracks which rows (documents) have been generated <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
    *   Unticked rows will be generated <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
    *   Once a document is generated for a row, a tick mark will automatically appear <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
3.  **Preview Sample**: After generation, you can click "Preview Sample" to view one of the generated PDF files <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. This allows you to verify that the placeholder texts have been correctly replaced with data from your database <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
4.  **[[bulk_export_of_pdf_documents_using_pdf_output | Download All]]**: To download all generated documents, click "Download All" <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. The files will be downloaded in a single go <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
5.  **Re-download**: If you forget to download the files, you can click "Download" again at any time <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

This process enables the [[using_pdf_output_com_for_pdf_generation | bulk generation]] of customized PDF documents based on your Notion data and template <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

For any further questions, you can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.