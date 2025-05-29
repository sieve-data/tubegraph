---
title: Creating and using invoice templates in Notion
videoId: WfYK1BJd490
---

From: [[theaccountantguy]] <br/> 

[[creating_professional_invoices_using_notion | Professional invoices]] can be generated directly from a [[generating_professional_invoices_from_notion_database | Notion database]] using a tool called PDF Output <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This process involves setting up both a [[using_notion_for_invoice_template_creation | Notion invoice template]] and a [[using_a_notion_database_and_templates_to_create_pdf_invoices | Notion database]] to work together <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Notion Invoice Template Structure
A [[using_notion_for_invoice_template_creation | Notion invoice template]] defines the layout and content of the invoice, including sections like "from" and "to" <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. Key information, such as client name, company, address, city, state, and zip, are included as placeholder text <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

### Placeholders
Placeholders are crucial for the template's functionality <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. Any element in the [[creating_and_using_notion_templates | template]] that needs to be replaced by data from a database is enclosed in curly braces, for example, `{{client_name}}` <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Notion Invoice Database Structure
The [[generating_professional_invoices_from_notion_database | Notion database]] contains the actual data that will populate the [[creating_and_using_notion_templates | invoice template]] <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Each column in the database corresponds to a placeholder in the [[creating_and_using_notion_templates | template]] <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

Common database columns include:
*   Client Name <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>
*   Amount <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>
*   Bank Name <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>
*   Client Address <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>
*   Client Company <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
*   Item details (e.g., Item One, Amount Column, Terms and Conditions) <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>

For every row of information in the database, a separate [[using_notion_templates_for_invoice_pdfs | PDF invoice]] can be generated <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## Generating PDFs with PDF Output
PDF Output is a tool used to connect a [[using_a_notion_database_and_templates_to_create_pdf_invoices | Notion database]] and a [[creating_and_using_notion_templates | Notion template]] to generate [[using_a_notion_database_and_templates_to_create_pdf_invoices | PDF invoices]] <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

### Steps to Generate Invoices
1.  **Log In and Enable API Keys**: After logging into PDF Output, navigate to the help section (by clicking "H") to complete steps required for API key setup <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
2.  **Define Connection Name**: Assign a name to the connection, such as "invoice generation" <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
3.  **Select Database and Template**:
    *   Choose the relevant [[using_a_notion_database_and_templates_to_create_pdf_invoices | Notion database]] (e.g., "professional invoice database") <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
    *   Select the [[creating_and_using_notion_templates | Notion template]] (e.g., "professional invoice template") <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
4.  **Map Elements**: Click "next" to allow the tool to automatically map [[generating_professional_invoices_from_notion_database | database]] properties to [[creating_and_using_notion_templates | template]] elements <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   Database elements (like "client address") are connected to [[creating_and_using_notion_templates | template]] elements (also "client address") <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
    *   If any elements are not automatically matched (indicated by a gray color), they can be manually selected and mapped <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
5.  **Export and Download**:
    *   Click "export" to begin the PDF generation process <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
    *   A "PDF status" column in the [[using_a_notion_database_and_templates_to_create_pdf_invoices | Notion database]] will tick as each PDF is generated <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
    *   Once generated, you can preview samples and download all the [[using_notion_templates_for_invoice_pdfs | PDF invoices]] <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

The generated [[using_notion_templates_for_invoice_pdfs | PDF invoices]] will reflect all the data from the [[generating_professional_invoices_from_notion_database | Notion database]], accurately replacing the placeholders in the [[creating_and_using_notion_templates | template]] <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

## Customization Tips
*   All elements within the [[creating_and_using_notion_templates | template]] and [[generating_professional_invoices_from_notion_database | database]] are customizable <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   Ensure that all placeholder text elements in the [[creating_and_using_notion_templates | template]] are enclosed in curly braces <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   The name used for a placeholder in the [[creating_and_using_notion_templates | template]] must exactly match the corresponding column name in the [[generating_professional_invoices_from_notion_database | database]] <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.