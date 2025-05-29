---
title: Generating PDF invoices from Notion database
videoId: WfYK1BJd490
---

From: [[theaccountantguy]] <br/> 

This article details how to [[generating_professional_invoices_using_notion | generate professional invoices]] directly from a Notion database using PDF Output <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This process streamlines [[generating_pdf_documents_from_notion_database | PDF document generation]] by linking your [[notion_database | Notion database]] and template to the PDF Output tool.

## Notion Setup for Invoices

To [[setting_up_notion_databases_for_pdf_generation | set up Notion for PDF generation]], two main components are required: an invoice template and a database.

### Invoice Template
The invoice template is designed with specific placeholders that will be dynamically filled with data from your Notion database <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   It includes sections like "from" and "to" <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
*   Placeholder text, such as `client name`, `client company`, `client address`, `city`, `state`, and `zip`, must be enclosed in curly braces (`{}`) <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
*   Examples of template elements include `item one`, `terms`, and `amount three` <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   All elements in the template are customizable according to your requirements <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

### Invoice Database
The Notion database holds the data for each invoice <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   It contains columns such as `client name`, `amount`, `bank name`, `client address`, and `client company` <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   Each row in the database provides the information that will populate a single invoice template to [[creating_pdf_documents_from_a_notion_database | create a PDF document]] <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   Crucially, the column names in the database must exactly match the placeholder names used in the template <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   A `PDF status` column in the database is used by PDF Output to track which PDFs have been generated, automatically ticking the box once a PDF is created <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

## Integrating Notion with PDF Output for Invoices

PDF Output is the tool used to bridge Notion and PDF generation <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

### Initial Setup
1.  **Log In:** Access the PDF Output interface <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
2.  **API Keys:** Navigate to the "help" section (by clicking 'H') to find instructions for enabling the necessary API keys <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. These steps must be completed to use the setup <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

### Defining the Connection
1.  **Connection Name:** Define a name for your connection, such as "invoice generation" <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
2.  **Select Database:** From the dropdown menu, select your Notion invoice database (e.g., "professional invoice database") <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
3.  **Select Template:** Similarly, select your Notion invoice template (e.g., "professional invoice template") <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
4.  **Proceed:** Click "next" to load and map the data <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### Automatic Mapping
*   PDF Output automatically maps database properties (listed on the left) to the corresponding template elements (listed on the right) <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   For example, `client address` from the database is connected to the `client address` placeholder in the template <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   If a mapping is incorrect or missing, it will appear in a gray color <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. You can manually click on it and search for the correct value <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

## Generating PDF Invoices

Once the mapping is complete, you can begin [[generating_pdf_documents_in_bulk_using_notion_and_pdf_output | generating PDF documents in bulk]].
1.  **Export:** Click on "export" to start the PDF generation process <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
2.  **Status Tracking:** Observe the `PDF status` column in your Notion database; it will tick as each PDF is generated <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
3.  **Preview:** You can click "preview sample" to view a clean output of a generated invoice, confirming all database elements are correctly placed <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
4.  **Download:** To download all generated PDF invoices, click "download all" <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. The files will be downloaded, ready for use <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

> [!tip] Customization
> All template elements are fully customizable. Just remember that placeholder text elements must be enclosed in curly braces, and these names must match the corresponding column names in your Notion database <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

For any questions or assistance, feel free to reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.