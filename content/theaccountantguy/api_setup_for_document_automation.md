---
title: API setup for document automation
videoId: lCyhl8mofjE
---

From: [[theaccountantguy]] <br/> 

PDF Output facilitates the [[generating_pdf_documents_for_businesses | generation of PDF documents]] for businesses, particularly for tasks like creating lease agreements from Notion databases. This process relies on a foundational API (Application Programming Interface) setup to connect your data source (Notion) with the document generation tool <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Initial Setup of API Keys

Before you can begin [[generating_bulk_pdf_documents_using_google_docs_and_notion | generating documents]], it's essential to set up the API keys.

1.  **Log In**: Begin by logging into the PDF Output platform <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
2.  **Access Help Section**: Navigate to the "Help" section within the PDF Output interface. This section contains comprehensive instructions required for setting up the PDF output system, including the crucial step of setting up the API keys <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. Following these preliminary steps is vital for the system to function correctly <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

## Connecting Databases and Templates

Once the API keys are set up, you can establish the connection for document generation:

1.  **Define Connection Name**: Specify a name for your connection, such as "lease agreement" <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
2.  **Select Database**: From a dropdown menu, choose the Notion database that is connected via the API key. This menu displays all databases linked through your configured API key <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. For example, selecting a database named "lease" <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
3.  **Select Template**: Choose the document template that corresponds to your database. For instance, a "lease template" <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

## Automatic and Manual Mapping

After selecting the database and template, the system proceeds to map the data fields:

*   The system automatically loads database and template elements and attempts to map them if their names match <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   On the left side, you'll see all Notion properties (e.g., landlord name, tenant name, street address) from your database <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   Corresponding to these properties, the PDF elements from your template are automatically mapped <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   **Important Naming Convention**: To ensure seamless auto-mapping, the naming convention of your Notion database properties and the placeholder text elements within your template (e.g., `{landlord name}`) should match exactly <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>, <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>, <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   If any mapping is incorrect or incomplete (indicated by a gray or red color), you can manually click and select the correct properties to map them <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

## Document Generation and Tracking

Once mapping is confirmed, you can generate your documents:

1.  **Export**: Click the "export" button to begin the processing of information and [[generating_and_downloading_pdf_documents_in_bulk | bulk document generation]] <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
2.  **PDF Status Property**: A "PDF status" property will appear in your Notion database. This column defines which rows need to be generated <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Rows that are unticked will be processed, and once generated, a tick mark will automatically appear, indicating completion <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
3.  **Preview and Download**:
    *   After generation, you can click on "preview sample" to view a single example of the generated PDF, verifying that information from the database (e.g., landlord name, tenant name, street address) has correctly replaced the placeholders <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   Finally, click "[[generating_and_downloading_pdf_documents_in_bulk | download all]]" to download all the generated PDF files in one go <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. You can also re-download files if forgotten <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

This streamlined process, enabled by the API setup, allows for efficient [[using_templates_and_placeholders_for_document_creation | creation of documents]] from Notion databases, whether for [[generating_pdf_documents_from_invoices | invoices]], lease agreements, or other business documents.