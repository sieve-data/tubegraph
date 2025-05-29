---
title: Exporting and downloading bulkgenerated PDFs
videoId: lCyhl8mofjE
---

From: [[theaccountantguy]] <br/> 

This guide outlines how to use PDFOutput to [[generating_pdf_documents_in_bulk | generate bulk PDF documents]], specifically lease agreements, from a Notion database and page <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Initial Setup with PDFOutput
Before generating documents, it's necessary to log into PDFOutput and follow the setup instructions in the help section <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This includes setting up API keys, which are crucial for the process <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## Preparing the Lease Agreement Template and Notion Database
A lease agreement template is used, featuring placeholder text elements enclosed in curly braces for details like landlord name, tenant name, and street address <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. These placeholders will be replaced with data from a Notion database <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. The database contains individual rows, each with values for landlord name, tenant name, and street address <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## Connecting PDFOutput to Notion Data
1.  After logging in, specify a connection name (e.g., "lease agreement") <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
2.  Select the relevant Notion database (e.g., "lease") from the dropdown, which lists all databases connected via the API key <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
3.  Choose the corresponding lease template <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
4.  Click "next" to load the database and template elements <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. PDFOutput automatically maps Notion properties (like landlord name, tenant name, street address) to the corresponding PDF template elements if their names match <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
    *   Unmapped elements will appear gray <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. Clicking on them reveals all properties, with unmapped ones listed in red <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

## [[Using PDFOutput for bulk PDF generation | Generating Bulk PDF Documents]]
Once mapping is confirmed, click "export" <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. A "PDF status" column will appear in the Notion database <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. PDFOutput will automatically generate documents for rows that are unticked in this column <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. As each PDF is generated, the corresponding row in the Notion database will be ticked <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

## Reviewing and [[Exporting and downloading generated PDF documents | Downloading Generated PDFs]]
After the generation process completes, a "preview sample" option becomes available <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. This allows users to view one sample PDF document to verify the replaced information <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. To [[bulk_pdf_document_exportation | download all generated PDFs]], click "download all" <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. The files will be downloaded in a single go <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

## Customization and Best Practices
Users can customize the template as per their specific use case and align the database structure with the template <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. It is important that the naming conventions in the database and template match exactly to facilitate automatic mapping in PDFOutput <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. If files are forgotten, they can be downloaded again by clicking "download" <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

For any questions, contact notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.