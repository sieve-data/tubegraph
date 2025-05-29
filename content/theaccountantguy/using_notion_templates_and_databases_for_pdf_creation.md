---
title: Using Notion templates and databases for PDF creation
videoId: 432wMcdqv1w
---

From: [[theaccountantguy]] <br/> 

[[Using Notion database and templates for PDF generation | PDF Output]] is a tool designed to generate PDF documents directly from a Notion database <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. It functions by specifying connection details, selecting a Notion database, and choosing a Notion template to create the PDF document <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Requirements for PDF Generation
To [[connecting_notion_database_and_templates_to_pdf_output | connect Notion database and templates to PDF output]] for document generation, two main components are required:
*   A Notion template <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   A Notion database <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

### Notion Template Structure
Templates, such as an invoice template, contain placeholders for specific information like client name, address, invoice number, and due date <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. These placeholders are indicated by text enclosed in curly brackets (e.g., `{client name}`) <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. When a PDF is generated, these placeholder texts are replaced by data from the Notion database <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. Users can [[customizing_pdf_documents_using_notion_database_elements | customize their own templates]], ensuring that placeholder names in curly braces exactly match the column names in the database <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.

### Notion Database Structure
The Notion database (e.g., an invoice database) stores the actual data that will populate the template <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Each row in the database typically represents a unique set of information, such as a single invoice <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### PDF Status Property
For PDF generation, it is crucial that the database includes a property named "PDF Status" <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. This checkbox property, when unchecked, signals to [[generating_pdf_invoices_in_bulk_using_a_notion_database | PDF Output]] that a PDF for that specific row has not yet been generated <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. Once a PDF is generated for a row, this checkbox is automatically ticked <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

## Setting Up PDF Output
Before generating PDFs, the PDF Output tool needs to be configured.

### 1. Configure Settings
*   **Page Format**: The ideal page format is A4, though other options are available <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
*   **Notion API Key**: A Notion private integration key is required <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
    *   To obtain this, navigate to Notion's integrations settings <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
    *   Create a "New integration," provide a name, select the workspace, and ensure it's an "internal key" <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
    *   After saving, configure the internal integration settings and click "Show" to reveal the secret key <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
    *   **Important**: Copy and save this key immediately, as it will not be visible again once the window is closed <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
    *   Paste the copied key into the "Notion API key" field in PDF Output settings <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

### 2. Connect Notion Pages to Integration
Both the Notion template page and the database page must be connected to the newly created integration <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   On the top right of the Notion page, click the three dots (`...`) <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   Scroll down and select "Add connections" or "Connect" <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   Search for and select the name of the integration created earlier <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   Repeat this step for both the template and the database <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

## Generating PDF Documents
Once the setup is complete, PDF documents can be generated.

### 1. Specify Connection Details
*   In the [[using_pdf_output_with_notion_templates | PDF Output]] interface, provide a connection name (e.g., "Invoice Generation") <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   Select the Notion database and the Notion template from the respective dropdown lists <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

### 2. Map Properties
*   After clicking "Next," [[connecting_notion_templates_with_pdf_output | PDF Output]] automatically reads information from the template and database <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
*   It automatically maps Notion database properties (e.g., "Client Name") to the corresponding placeholder elements in the template (e.g., `{client name}`) <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   For optimal results, ensure the naming convention for placeholders in the template exactly matches the column names in the database <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.
*   If any elements are not automatically mapped (appearing in gray), they can be manually mapped by clicking on them and selecting the correct Notion property <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. Sorting and filtering options are available to help manage properties <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.

### 3. Export and Download
*   Click "Export" to start the PDF generation process <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   The "PDF Status" checkboxes in the Notion database will automatically be ticked as PDFs are generated for each row <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
*   After successful export, users can "Preview sample" of the generated PDF directly in the web interface or click "Download all" to download the files <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   The generated PDFs will replace all template placeholders with the corresponding database values <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
*   Note: Free plans will display a watermark on the generated PDFs <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. Paid plans remove this watermark <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

## Additional Features
*   **Saved Connections**: Once a connection is created, it can be re-used by clicking the "C" icon, which loads the previously defined settings, allowing for subsequent document generation without re-entering details <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
*   **Upgrade Options**: Users can upgrade their subscription from the basic plan (which includes a 1000-document limit and watermark) to Pro or Enterprise plans for more features and no watermark <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
*   **Templates Library**: A "Templates" section provides access to pre-made templates, such as the invoice template demonstrated <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
*   **Feedback & Help**: Users can submit feedback to improve the tool's performance <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>, and a "Help" section provides tutorial videos <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.
*   **API Key Evolution**: Currently, Notion API access requires private integration keys, meaning each user must create their own <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. This process may change with the availability of a public API key access <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.