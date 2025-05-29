---
title: Customizing lease agreement templates
videoId: lCyhl8mofjE
---

From: [[theaccountantguy]] <br/> 

[[generating_lease_agreement_pdfs_using_notion_and_pdfoutput | Generating lease agreement PDFs using Notion and PDFOutput]] allows for the creation of customized lease documents by combining a Notion database with a Notion page acting as a template <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This process leverages placeholder text elements within the template, which are then dynamically filled with data from the database <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. This method is similar to [[customizing_invoice_templates_with_placeholders | customizing invoice templates with placeholders]] or [[customizing_invoice_templates_and_databases | customizing invoice templates and databases]].

## Template and Database Setup

A lease agreement template is created in Notion, containing all necessary details for a lease <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. Key information, such as landlord name, tenant name, and street address, is included as placeholder text elements, typically enclosed in curly braces (e.g., `{{landlord name}}`) <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

Correspondingly, a Notion database is set up with properties (columns) that match the placeholder names in the template (e.g., "landlord name," "tenant name," "street address") <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Each row in the database represents a unique lease agreement, with values for each property <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

> [!tip] Naming Convention
> Ensure that the naming convention of the database properties and the template's placeholder elements matches exactly to facilitate automatic mapping <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a> <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. This principle applies to [[customizing_pdf_templates_for_specific_needs | customizing PDF templates for specific needs]], including [[customizing_sales_receipt_templates | sales receipts]], [[customizing_budget_templates | budgets]], or [[customizing_purchase_order_templates | purchase orders]].

## Generating PDFs with PDF Output

The process involves using the PDF Output tool:

1.  **Login and Setup**
    *   Log into PDF Output <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
    *   Access the "Help" section for initial setup instructions, including API key configuration, which is a prerequisite for generating PDF documents <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

2.  **Connection Details**
    *   Specify a connection name, such as "lease agreement" <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
    *   Select the relevant Notion database (e.g., "lease") from the dropdown menu <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
    *   Select the corresponding lease template <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
    *   Click "Next" <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

3.  **Mapping Properties**
    *   PDF Output automatically attempts to map Notion database properties to the template's PDF elements if their names match <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
    *   The left side displays Notion properties (database columns), and the right side shows the corresponding template elements <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
    *   If any fields are not automatically mapped (indicated by a gray or red color), they can be manually selected from a list of properties <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

4.  **Export and Generation**
    *   Click "Export" to begin the PDF generation process <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
    *   A "PDF Status" property automatically appears in the Notion database <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. This column tracks which rows have had their PDFs generated, with a tick mark appearing once completed <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

## Output and Review

Once generated, users can:

*   **Preview Sample:** View a sample PDF file to ensure the data has been correctly replaced in the template <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. For example, a sample PDF might show a lease agreement for "Tom Green" as landlord and "Sarah Blue" as tenant, with corresponding street address and lease details <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Download All:** Download all generated PDF files, typically in a single compressed archive <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. This creates an exact replica of the agreement template, populated with unique data from each database entry <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

This process allows for efficient creation of various documents, demonstrating the versatility of [[customizing_notion_templates_for_business_needs | customizing Notion templates for business needs]] or even [[customizing_notion_templates_for_home_inventory | customizing Notion templates for home inventory]].

For further assistance, users can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.