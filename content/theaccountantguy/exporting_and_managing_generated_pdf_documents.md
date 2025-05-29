---
title: Exporting and managing generated PDF documents
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

[[Exporting and managing generated PDF documents | Exporting and managing generated PDF documents]] through PDFOutput allows users to create various PDF documents, such as purchase orders, invoices, and payment receipts, by integrating Notion databases and templates <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This process involves connecting a Notion database and a Notion template to the PDFOutput platform <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Getting Started with PDFOutput

To begin, users must log in to [PDFOutput.com](http://PDFOutput.com) <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The interface displays options for connection name, Notion database, and Notion template <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Selecting and Customizing Templates

PDFOutput provides a list of predefined templates in the sidebar, including invoices, payment receipts, and purchase orders <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. Users can search for specific templates <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a> and download the desired one to their Notion workspace <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

The templates feature placeholder elements enclosed in curly braces (e.g., `{purchase order number}`, `{date}`) <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. These placeholders are replaced by corresponding values from a Notion database <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. Users have the flexibility to customize templates and databases by adding, deleting, or modifying values, as long as the database column names precisely match the template's placeholder names (including spaces and commas) <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

## Connecting Notion to PDFOutput

After duplicating the chosen template page to a Notion workspace <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>, users proceed to the "Settings" section in PDFOutput <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. Here, they can:
*   Select the desired page format for the PDF document <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
*   Click "Click here to add templates" to connect the Notion workspace and select the duplicated template page <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   Grant access to PDFOutput to connect the page <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

Once authenticated, PDFOutput loads the database and template elements, automatically matching most fields <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. Unmatched properties can be identified using the filter option <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a> and manually mapped to ensure all data is correctly linked <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

## [[Exporting and downloading generated PDF documents | Exporting and Downloading Generated PDF Documents]]

To initiate the [[bulk_pdf_document_exportation | bulk PDF document exportation]], click "Export" <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. PDFOutput automatically adds a "PDF status" column to the Notion database, which is ticked once a PDF document is generated for that row <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. To regenerate a page, the corresponding checkbox in this column must be unticked <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

After successful export, users can preview a sample of the [[generating_pdf_documents_in_bulk | generated PDF]] <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>, confirming that all data from the database has accurately populated the template <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. The generated documents can then be downloaded as a batch <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

## Managing Connections and Subscriptions

### Connections
PDFOutput stores connections, allowing users to regenerate documents without re-filling database and page details <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. Clicking on an existing connection automatically populates the database and template elements, enabling immediate re-export <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. This feature is particularly useful for [[bulk_export_of_pdf_documents_from_database | bulk export of PDF documents from database]].

### Upgrade Options
Free plans include a watermark on generated PDFs, while paid plans remove the watermark <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. Users can upgrade their subscription via the "Upgrade" section to remove watermarks <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

### Settings
The "Settings" section allows users to define and save their preferred PDF page format <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

### Feedback and Help
PDFOutput offers a feedback option for reporting issues <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. A "Help" section provides a complete demonstration video for setup and troubleshooting <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.