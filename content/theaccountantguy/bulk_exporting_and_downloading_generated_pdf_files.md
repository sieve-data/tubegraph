---
title: Bulk exporting and downloading generated PDF files
videoId: lCyhl8mofjE
---

From: [[theaccountantguy]] <br/> 

The [[PDF Output]] tool facilitates [[exporting_bulk_pdf_documents_from_a_database | bulk export of PDF documents]] by generating them from a Notion database and a Notion page template <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This process involves mapping data from database properties to placeholder elements within a PDF template.

## Setting Up for PDF Generation

### Template and Database Preparation
Before generating PDFs, a lease agreement template with placeholder text elements (e.g., `landlord name`, `tenant name`, `street address` enclosed in curly braces) is used <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. Correspondingly, a Notion database contains the actual values for these fields, such as `landlord name`, `tenant name`, and `street address` <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. These values from each individual row in the database are intended to replace the placeholder text elements in the template <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

### Initial [[Using PDF Output interface for exporting documents | PDF Output Interface]] Setup
To begin, users need to log into [[PDF Output]] <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. It is crucial to visit the help section first to follow the tutorial on setting up the [[PDF Output]] tool, including configuring API keys <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### Connecting Database and Template
Within the [[PDF Output]] interface, a connection name (e.g., "lease agreement") is specified <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. From dropdown menus, the relevant database (e.g., "lease") and template (e.g., "lease template") are selected <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

### Automatic Mapping of Fields
After selecting the database and template, the system loads the database and template elements <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. It automatically maps Notion properties from the database (e.g., `landlord name`, `tenant name`) to corresponding [[PDF Output]] elements in the template if their names match <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. If a field is not automatically mapped, it will appear in a gray color, and users can manually select the correct property from a list, with unmapped items highlighted in red <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

## [[Bulk PDF document generation | Generating Bulk PDFs]]

Once mapping is confirmed, clicking "export" initiates the processing of information <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. A "PDF status" property automatically appears in the Notion database <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. This column's purpose is to indicate which rows need PDF generation; unticked rows are processed, and a tick mark is applied once a PDF is generated for that row <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

## [[Bulk export of PDF documents | Exporting and Downloading Generated Files]]

After the PDFs are generated, the system offers options for review and download:

*   **Preview Sample**: Users can click "preview sample" to view one of the generated PDF files <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This allows verification that the data from the database (e.g., landlord name "Tom Green", tenant name "Sarah Blue", street address) has correctly replaced the placeholders in the template <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **[[Bulk PDF document export process | Download All]]**: To [[exporting_bulk_pdfs_with_pdf_output_tool | export bulk PDFs with PDF Output Tool]], users can click "download all" to download all generated files in one go <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

## Best Practices and Support

To ensure a smooth [[exporting_and_managing_pdf_documents_for_business | exporting and managing PDF documents for business]] process, it's recommended to:
*   Customize the template according to specific use cases <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   Ensure that the naming convention of the database properties matches the template elements exactly to facilitate automatic mapping <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   Always follow the instructions in the help section for initial setup <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

For any questions, users can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.