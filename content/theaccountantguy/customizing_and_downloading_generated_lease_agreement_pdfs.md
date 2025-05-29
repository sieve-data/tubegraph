---
title: Customizing and downloading generated lease agreement PDFs
videoId: lCyhl8mofjE
---

From: [[theaccountantguy]] <br/> 

PDFOutput can be utilized to [[generating_lease_agreement_pdfs_using_notion_and_pdfoutput | generate lease agreement documents in PDF format]] directly from a Notion database and page <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This process involves setting up a template, connecting to a Notion database, and then generating, previewing, and downloading the customized PDF files.

## Setting Up the Lease Agreement Template

A lease agreement template is prepared with specific details, including landlord name, tenant name, and other relevant information <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. Key details are inserted as [[using_placeholder_text_elements_in_lease_agreement_templates | placeholder text elements]], enclosed within curly braces (e.g., `{landlord name}`, `{tenant name}`, `{street address}`) <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. These placeholders are designed to be dynamically replaced with values from a Notion database <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Connecting Notion to PDFOutput

Before generating documents, users need to log into PDFOutput and follow the setup tutorial in the help section to configure API keys <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. Once configured:
1.  Assign a connection name, such as "lease agreement" <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
2.  Select the relevant Notion database (e.g., "lease") from the dropdown menu <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
3.  Select the corresponding lease agreement template <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

After selection, PDFOutput loads the database and template elements, automatically mapping Notion properties (like landlord name, tenant name, street address) to their corresponding PDF template elements if the names match <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. If any elements are not automatically mapped, they can be manually selected from a list of available properties <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

## Generating Lease Agreement PDFs

To [[generating_and_downloading_pdf_documents | generate the PDF documents]]:
1.  Click the "Export" button <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
2.  A "PDF status" property will appear in the Notion database <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
3.  PDFOutput processes the information, and for any unticked rows in the "PDF status" column, it automatically generates the corresponding PDF and then ticks the box <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. This indicates that the PDF for that row has been successfully generated <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

## Previewing and Downloading Generated PDFs

Once the generation process is complete:
*   **Preview Sample**: Users can click "Preview Sample" to view one of the generated PDF files <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This allows verification that the placeholders have been correctly replaced with data from the Notion database (e.g., "Tom Green" for landlord, "Sarah Blue" for tenant, and the correct street address) <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Download All**: To [[exporting_and_downloading_pdfs | download all generated PDFs]], click "Download All" <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. This downloads all files in a single go, typically in a compressed format <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. Individual PDF files can then be opened and reviewed <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>, confirming they are exact replicas of the original agreement template with customized details <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

### Customization and Naming Conventions
Users can [[customizing_templates_for_pdf_generation | customize the template]] according to their specific use case <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. It is crucial to ensure that the naming conventions of the Notion database properties and the template placeholders match exactly to facilitate automatic mapping in PDFOutput <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

If files were not downloaded initially, they can be downloaded again by clicking the "Download" button <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. For further assistance, refer to the instructions in the Help section or contact notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.