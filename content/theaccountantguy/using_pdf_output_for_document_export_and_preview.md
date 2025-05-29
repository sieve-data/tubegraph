---
title: Using PDF Output for document export and preview
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

[[integration_with_pdf_output_tools | PDF Output]] is a tool designed to generate PDF documents from Notion databases and templates <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This guide explains how to use [[integration_with_pdf_output_tools | PDF Output]] for document generation, export, and preview.

## Getting Started <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>

To begin, you need to log in to PDF output.com <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Upon logging in, you will see an interface featuring a connection name, Notion database, and Notion template sections <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Selecting and Preparing Templates <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>

1.  **Access Templates:** Click on "Templates" in the sidebar to load a list of predefined templates <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. Examples include [[using_pdf_output_for_invoice_document_generation | invoices]], payment receipts, and purchase orders <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
2.  **Search for Templates:** Use the search icon to quickly find a required template <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
3.  **Download Template:** Click the "download" link next to your desired template (e.g., purchase order) <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This opens a new page for the specific PDF generator, which includes a database and a template <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

### Understanding Templates and Databases <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>

*   **Templates:** These are document layouts (e.g., a purchase order) where certain elements are enclosed in curly braces (e.g., `{purchase order number}`, `{supplier name}`, `{buyer name}`) <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. These curly-braced elements act as placeholders <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **Databases:** These contain the actual data (e.g., supplier names, buyer names, purchase order numbers) in predefined fields <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Replacement Process:** [[integration_with_pdf_output_tools | PDF Output]] replaces the placeholder text in the template with corresponding column values from the database <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

## Connecting Notion to PDF Output <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>

1.  **Duplicate Template to Notion:** On the PDF generator page, click "Duplicate" (or "Start with this template" if already published) <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Select your Notion workspace to add the page <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
2.  **Configure Settings in PDF Output:**
    *   Go to "Settings" in [[integration_with_pdf_output_tools | PDF Output]] <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
    *   Select your desired page format for the PDF <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
    *   Click "Click here to add templates" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
3.  **Connect Workspace and Pages:**
    *   Select your Notion workspace from the dropdown <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
    *   Click "Select Pages" and choose the duplicated Notion page (e.g., "Purchase order PDF generator") <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
    *   Click "Allow access" to connect the Notion page with [[integration_with_pdf_output_tools | PDF Output]] <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
4.  **Select Database and Template:** Once connected, select the Notion database and the specific template page (not the generator page) within [[integration_with_pdf_output_tools | PDF Output]] <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. Give it a name (e.g., "Purchase order") <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

## Mapping Properties <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>

[[integration_with_pdf_output_tools | PDF Output]] automatically matches Notion database properties with template elements <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

*   **Troubleshooting Unmatched Properties:** If properties don't match (e.g., due to extra spaces or commas), they will remain unmapped <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.
    *   Use the "filter unmapped properties" option to quickly identify them <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
    *   Manually map the unmatched properties by clicking on them and selecting the correct corresponding element <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Customization Note:** All template and database elements are customizable <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. Ensure that values to be replaced are inside curly braces in the template and that the name of the database column exactly matches the name inside the curly braces <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

## Exporting and Previewing Documents <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>

1.  **Initiate Export:** Click "Export" <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
2.  **PDF Status Column:** During export, a "PDF status" column is automatically added to your Notion database <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. A ticked checkbox in this column indicates that the PDF document for that row has been generated <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. To regenerate a page, ensure this checkbox is unticked <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
3.  **Preview Sample:** After successful export, you can click "Preview sample" to view a sample of the generated file <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
4.  **Download Documents:** Click "Download all documents" to get all generated PDFs <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. They will be saved to an output folder <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

## Managing Exported Documents and Settings <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>

*   **Connections:** When a PDF document is generated, [[integration_with_pdf_output_tools | PDF Output]] creates and stores a "connection" <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. This allows you to regenerate documents by simply clicking on the connection without needing to re-fill the database and pages <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
*   **[[managing_pdfoutput_settings_and_subscriptions | Settings]]:** In the [[managing_pdfoutput_settings_and_subscriptions | settings]] section, you can define the page format for your PDFs and add new templates to your workspace <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **Upgrade:** Free plan generated templates will have a watermark, while paid plans will not <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. You can upgrade your subscription to remove the watermark <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

## Support <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>

*   **Feedback:** If you encounter any issues, use the feedback option in the sidebar to report them <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
*   **Help Section:** The help section provides a complete demonstration of the setup process for troubleshooting <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.
*   **Contact:** For other solutions or PDF document use cases, you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.