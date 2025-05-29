---
title: Customizing invoice templates using placeholders
videoId: WfYK1BJd490
---

From: [[theaccountantguy]] <br/> 

This article explores how to create and customize professional invoice templates using placeholders in Notion, specifically for generating PDF documents directly from a Notion database with the help of a tool called PDF output <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Understanding Placeholders in Invoice Templates

When setting up an invoice template, certain elements are designated as "placeholder text" <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. These placeholders are designed to be replaced with actual data from your Notion database.

*   **Syntax**: Every element intended for replacement must be enclosed within curly braces (e.g., `{client name}`, `{client company}`, `{client address}`) <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   **Purpose**: These curly-braced elements indicate where data from your Notion database will be dynamically inserted when generating the PDF invoice <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

For instance, an [[creating_and_using_an_invoice_template_in_notion | invoice template]] might include sections like "from" and "to," with the "to" section containing placeholders for `{client name}`, `{client company}`, `{client address}`, `{city}`, `{state}`, and `{zip}` <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Connecting Templates to Notion Databases

To enable [[replacing_placeholder_text_in_templates_with_database_values | replacing placeholder text in templates with database values]], the Notion database must contain corresponding data elements.

*   **Database Elements**: Your Notion database will have columns for data such as client name, amount, bank name, client address, and client company <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   **Population**: For every row of information in the database, the corresponding data will populate the placeholders in the template, generating a PDF <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## Automatic Mapping and Manual Adjustments

When using PDF output to [[using_templates_to_generate_pdf_invoices | use templates to generate PDF invoices]], the system attempts to [[mapping_database_elements_to_invoice_templates | map database elements to invoice templates]] automatically.

1.  **Connection Setup**: After setting up API keys, you define a connection name (e.g., "invoice generation"), select your Notion database (e.g., "professional invoice database"), and choose the corresponding template (e.g., "professional invoice template") <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
2.  **Automatic Mapping**: The tool automatically loads database elements and template values, then maps each database element to its corresponding template placeholder <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. For example, the "Client Address" database property will be connected to the `{client address}` placeholder in the template <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
3.  **Troubleshooting Mismatches**: If a placeholder element does not match a column name in the database, it will appear in gray <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. You can manually click on it and search for the exact matching value from your database to map it correctly <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

> [!tip] Matching Names
> When building your connection, ensure that the element names used in the template's placeholders exactly match the column names in your Notion database <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. This simplifies the mapping process and ensures accurate data population.

## Key Customization Guidelines

The elements within your invoice templates are highly [[customizing_notion_invoice_templates | customizable]] to fit your specific requirements <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

*   **Placeholder Format**: Always ensure that all placeholder text elements are enclosed within curly braces (e.g., `{Total Amount}`) <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   **Database Naming**: Use the exact same name for the corresponding column in your Notion database as you do for the placeholder <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

By following these steps, you can effectively [[customizing_notion_invoice_templates | customize Notion invoice templates]] to generate professional PDF documents automatically from your Notion database <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.