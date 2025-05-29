---
title: Customizing invoice layout and settings
videoId: 5lnQYIpvjnM
---

From: [[theaccountantguy]] <br/> 

Customizing invoice layouts and settings is crucial for generating professional and accurate financial documents, especially when creating them in bulk. This process often involves using a template and a database to dynamically populate information, followed by adjusting output preferences.

## Template Preparation
A [[professional_invoice_template_customization | professional invoice template]] can be created using platforms like Notion <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This template should include all necessary invoice information <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. For the template to be used by a generation tool, it must be shared publicly <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### Using Placeholders for Dynamic Content
To allow for dynamic content generation, specific information within the invoice template should be enclosed in curly brackets, e.g., `{client name}` <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. These placeholders, such as client name, client company, and client address, will be replaced with data fetched from a connected database <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>, <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. This process of [[customizing_invoice_elements_using_placeholders | customizing invoice elements using placeholders]] is fundamental for bulk generation. The fields within the curly brackets in the template must correspond to the column names in the database <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

## Generating Invoices
To [[exporting_and_customizing_invoices_in_bulk | export and customize invoices in bulk]] and generate PDF documents from a Notion template and database, a tool like pdf4put.com can be used <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

### Database Connection
A key aspect of [[customizing_invoice_templates_for_bulk_generation | customizing invoice templates for bulk generation]] is connecting your database to the generation tool via an API key <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. The database must be connected to the specific API key created for the integration <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. If the database utilizes relational properties (linking to other databases), all related databases must also be connected to the same API key for seamless data fetching <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

## Output Settings for PDF Generation
When [[setting_up_pdf_output_for_invoice_generation | setting up PDF output for invoice generation]], several customization options are available:

*   **File Naming**: You can choose a specific database column, such as "invoice number", to name the generated PDF files <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   **Row Selection**: Documents can be generated for all database rows, a custom range of rows (e.g., fourth through seventh), or specific individual rows <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   **Layout Settings**:
    *   **Paper Size**: Users can select the desired paper size for the PDF output <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
    *   **Orientation**: Both portrait and landscape modes are available for the document layout <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
    *   **Page Range**: You can specify whether to print all pages of the template or a subset <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.