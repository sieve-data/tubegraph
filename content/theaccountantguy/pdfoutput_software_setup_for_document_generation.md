---
title: PDFOutput software setup for document generation
videoId: lCyhl8mofjE
---

From: [[theaccountantguy]] <br/> 

[[Introduction to PDFOutput tool | PDFOutput]] is a tool that allows users to [[generating_pdf_documents_for_business_purposes | generate PDF documents]] from a Notion database and page, such as [[creating_pdf_documents_for_business_needs | creating lease agreement documents]] <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Preparing the Template and Database

To [[bulk_pdf_document_generation | generate PDF documents]] using [[Introduction to PDFOutput tool | PDFOutput]], you first need a template and a database:

### Lease Agreement Template
A lease agreement template is used, which includes details like landlord name and tenant name <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. Key information within this template, such as "landlord name," "tenant name," and "street address," is designated as placeholder text using curly braces <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. These placeholders will be replaced with data from the Notion database <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

### Notion Database
A Notion database contains the specific values that will populate the template <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. This database includes fields like "landlord name," "tenant name," and "street address," corresponding to the placeholders in the template <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Each row in the database represents a unique set of information for a document <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Setting Up PDFOutput

### Initial Login and Configuration
1.  **Log In**: The first step is to log into the [[Introduction to PDFOutput tool | PDFOutput]] application <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
2.  **Help Section**: Navigate to the "Help" section within the [[Introduction to PDFOutput tool | PDFOutput]] interface <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This section provides a tutorial on the preliminary steps required to set up [[understanding_pdf_output_settings_and_features | PDFOutput]], including configuring API keys, before you can start [[bulk_pdf_document_generation | generating PDF documents]] <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

### Connecting Database and Template
1.  **Specify Connection Name**: After initial setup, return to the main screen and enter a connection name, for example, "lease agreement" <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
2.  **Select Database**: Use the dropdown menu to select the Notion database connected via the API key, searching for "lease" to find the relevant database <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
3.  **Select Template**: Choose the corresponding "lease template" from the available templates <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
4.  **Proceed**: Click "Next" to load the database and template elements <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

### Automatic Mapping of Properties
[[Using PDFOutput features and settings | PDFOutput]] automatically maps Notion properties (from the database) to the corresponding template elements (placeholder texts) if their names match <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
*   On the left side, all Notion properties from the database, such as "landlord name," "tenant name," and "street address," are listed <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   [[Using PDFOutput features and settings | PDFOutput]] attempts to map these to the PDF template elements automatically (e.g., "landlord name" in Notion maps to "landlord name" in the template) <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   If a property is not automatically mapped, it will appear in gray <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. Clicking on it reveals unmapped properties, which are listed in red, allowing for manual correction <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

## Exporting and Reviewing Documents

### Export Process
1.  **Initiate Export**: Click the "Export" button <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
2.  **PDF Status Column**: During the export, a "PDF Status" column appears in your Notion database <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. This column helps track which rows have had their PDFs generated; unticked rows will be processed, and once a PDF is generated for a row, it receives a tick mark <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

### Review and Download
1.  **Preview Sample**: Once processing is complete, a "Preview Sample" option becomes available, allowing you to view a single generated PDF document to confirm the data replacement (e.g., Tom Green's lease agreement) <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
2.  **Download All**: To download all generated PDF files, click "Download All" <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. This downloads the files in a compressed format <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

### Customization and Best Practices
The generated PDF documents are exact replicas of the agreement template with database information filled in <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. Users can [[customizing_document_settings_and_layout_in_pdf_generation | customize the template]] as per their needs <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. It is crucial to ensure that the naming conventions in the database and the template match exactly to facilitate automatic mapping <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. If you forget to download the files, you can click "Download" again <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

For further assistance, users can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.