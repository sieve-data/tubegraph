---
title: Mapping Notion database elements to template placeholders
videoId: XPSQBVl9mKs
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to [[Connecting Notion databases and templates for PDF creation | generate PDF documents in bulk]] by leveraging a Notion database and a Notion template <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This process involves replacing specific placeholder elements within a template with dynamic data retrieved from a Notion database <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## Core Concept: Template Placeholders and Notion Data

The primary mechanism for [[Personalizing Templates with Notion Data | personalizing templates]] is the use of curly braces around placeholder text in the template, e.g., `{invoice_number}` or `{client_name}` <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. PDF Output automatically fetches information from each row of a Notion database and uses it to replace these corresponding elements in the template <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>, effectively [[utilizing_notion_database_for_document_data | utilizing Notion database for document data]] to fill the template.

For example, in an [[mapping_database_elements_to_invoice_templates | invoice template]], fields like invoice number, date, due date, and terms, when enclosed in curly braces, are replaced with the specific values from the associated Notion database row <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Setup and Preparation

To begin, users need to:
1.  Navigate to PDFoutput.com <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
2.  Log in and access the "Templates" section <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
3.  Select a desired template, such as an [[mapping_database_elements_to_invoice_templates | invoice template]] <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
4.  Duplicate the chosen template to their own Notion workspace by clicking "Start with this template" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
5.  In PDF Output's settings, link the Notion workspace by selecting the relevant templates <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. It's crucial to select the same Notion account where the template was duplicated <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

## [[Mapping database properties to template placeholders | Mapping Database Properties to Template Placeholders]]

After linking the Notion workspace, the system displays the Notion database and template <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. Users then assign a name to their mapping configuration <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

The tool then proceeds to Step 2, which is the [[automatically_mapping_database_properties_to_template_elements | automatic mapping]] phase <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>:
*   **Notion Properties**: On the left side, all properties (columns) from the selected Notion database are displayed <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   **Template Elements**: On the right, the template elements (placeholders within curly braces) are listed <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **Automatic Mapping**: The system attempts to [[automatically_mapping_database_properties_to_template_elements | automatically map]] Notion properties to template elements based on their names <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.
*   **Name Matching**: For successful [[mapping_notion_database_elements_to_templates | mapping]], the name of the placeholder in curly braces in the template *must exactly match* the name of the corresponding Notion database property <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
*   **Manual Mapping**: If there's a name mismatch, the mapping will appear in gray <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. Users can manually click on an unmapped item to select the correct Notion property from a list of available template elements <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.
*   **Search, Sort, Filter**: Options are available to search for specific elements, sort the list, or filter for unmapped properties <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

## PDF Generation

Before exporting, it's important to check the "PDF Status" column in the Notion database <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. Only unchecked rows will be processed and generated into PDF documents <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. Once documents are generated, this column will automatically be checked for those rows <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

After initiating the export <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>, the tool processes the data, replacing template placeholders with Notion database values <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. Upon successful export, users can:
*   **Preview a Sample**: View a single generated PDF document to verify the [[mapping_and_managing_data_fields_between_notion_database_and_pdf_templates | data mapping]] <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. For example, an invoice preview would show the client name, address, invoice number, and date replaced with data from a specific Notion row <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.
*   **Download All**: Download all generated PDF documents at once <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. The tool generates a separate PDF for each applicable row in the Notion database <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

## Re-using Connections

Once a database and template are successfully [[connecting_notion_databases_and_templates | connected]] and mapped, the configuration is saved under the "Connections" window <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. For future use, users can simply select the saved connection to quickly regenerate documents without going through the entire setup process again <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

## Additional Features

*   **Page Format**: Users can select from various page formats under the settings tab <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
*   **Watermarks**: PDF outputs from free accounts include a watermark, which is removed on paid plans <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   **Support**: Feedback and help options are available, including access to video demonstrations <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.