---
title: Mapping database elements to invoice templates
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

This article demonstrates how to utilize a Notion page and template to generate PDF documents, specifically invoice PDFs, using a Notion database through the PDF Output.com platform <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Getting Started with PDF Output.com

To begin, users need to log in to PDF Output.com <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Upon logging in, users can access the "template" section <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

### Selecting and Duplicating Templates

The "template" section displays a list of pre-created templates available for use with PDF Output <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. For invoice generation, the invoice template can be downloaded <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. Users can also utilize search, sort, or filter options to find specific templates <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

After selecting the invoice template, users click a download link which opens a new page displaying both the template and the corresponding database <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. To begin [[creating_and_using_invoice_templates_in_notion | creating and using invoice templates in Notion]], click the "start with this template" option, which prompts duplication of the template onto the user's Notion workspace <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. The template will then be added to the user's list of templates in Notion, including the invoice template and its associated database <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

### Connecting Notion Template to PDF Output

Once the template is duplicated, navigate back to PDF Output and select "settings" <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. Here, users can add the specific template that was duplicated <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. It's crucial to select the correct Notion workspace where the template was duplicated <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. After selecting the template (e.g., "invoice generator template"), allow access to authenticate the connection <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. The template will then be added to the PDF Output setup <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

## Understanding Template and Database Structure

The template used for PDF generation is customizable <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
Elements within the template, such as client name, client company address, invoice number, date, and terms, are placed inside curly braces <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. These are placeholder text elements that will be replaced with data from the connected database <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. This allows for [[customizing_invoice_elements_using_placeholders | customizing invoice elements using placeholders]].

The Notion database contains corresponding elements listed as columns, such as invoice number, date, client name, and client company <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. For every row in the invoice database, these elements will replace the corresponding placeholders in the template <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

> [!CAUTION] Matching Naming Conventions
> All placeholder text elements in the template must be inside curly braces, and the exact same elements must be listed out in the Notion database with identical naming conventions <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a> <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. This ensures correct [[mapping_notion_database_elements_to_pdf_templates | mapping of Notion database elements to PDF templates]] and seamless output generation <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

## Generating PDF Invoices

After syncing the database and template elements, Notion properties (database columns) are listed on the left side of the PDF Output interface, automatically mapped to their corresponding template elements <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. For example, "Client Name" from the database is mapped to "Client Name" in the template <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

*   **Mapping Verification**: Mapped elements are indicated by a green bar <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
*   **Manual Mapping**: If an element is not automatically mapped, users can click on it and search for the correct corresponding element to map it manually <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
*   **Export**: Once mapping is confirmed, click "export" to start processing the documents <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

### Monitoring and Downloading Outputs

As the documents are generated, a "PDF status" column in the Notion database will automatically become checked for each processed row <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
Upon successful export, a sample PDF can be previewed <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. All generated PDF outputs can be downloaded by clicking "download all" <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. This demonstrates [[using_a_notion_database_and_templates_to_create_pdf_invoices | using a Notion database and templates to create PDF invoices]].

## Customization and Best Practices

Both the template and the database can be customized as per requirements before generating the output <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. When generating new documents, ensure that the "PDF status" row in the Notion database is unticked for the desired rows, otherwise, ticked rows will be ignored <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. This allows for [[customizing_invoice_templates_for_bulk_generation | customizing invoice templates for bulk generation]].

## Additional Features and Support

*   **Other Templates**: Users can access a list of different template elements available on the platform <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
*   **Watermark**: On the free plan, generated templates will include a PDF Output watermark; users can upgrade to a paid plan to remove it <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
*   **Feedback**: A feedback option is available for sending messages or suggestions <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
*   **Connections**: After an initial export, connections with all saved values can be viewed and reloaded, eliminating the need to remap the database and template for future generations <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Help Section**: A help section provides a detailed demonstration on initial setup <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

For any questions or feedback, users can reach out to notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. This entire process demonstrates [[using_notion_templates_for_invoice_pdfs | using Notion templates for invoice PDFs]] and [[using_databases_to_manage_invoice_details_in_notion | using databases to manage invoice details in Notion]].