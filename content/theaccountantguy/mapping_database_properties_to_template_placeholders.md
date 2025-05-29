---
title: Mapping database properties to template placeholders
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

[[using_templates_and_databases_to_create_professional_pdfs | PDF Output]] is a tool designed to generate PDF documents in bulk by using a Notion page as a template and a Notion database to hold the elements that will replace placeholders in that template <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The core process involves [[mapping_database_elements_to_template_placeholders | mapping database properties to template placeholders]] <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

## Preparing the Template and Database

To enable [[mapping_database_elements_to_template_placeholders | mapping database elements to template placeholders]], you first need to create a Notion database and a Notion template <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

### Template Creation
Define the content of your template, ensuring that sections intended for replacement are enclosed within curly braces (e.g., `{title}`, `{customer name}`) <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. These curly-braced sections act as specific placeholders that will be replaced by data from your database <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Database Creation
Create a database with columns that match the exact naming convention of the placeholders defined in your template <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. For example, if your template has `{title}` and `{customer name}`, your database should have columns named "title" and "customer name" <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

## The Mapping Process in PDF Output

After setting up your template and database in Notion, you integrate them with [[integrating_databases_with_templates_in_notion | PDF Output]]:

1.  **Select Database and Template**: In [[connecting_notion_templates_with_a_database_for_automation | PDF Output]], you define the Notion database and the specific Notion template that will be used for PDF generation <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
2.  **Define Connection Name**: Assign a connection name to this mapping, such as "invitation letter" <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
3.  **Map Properties**: The tool will then present a section for [[mapping_database_properties_to_templates | mapping database properties to templates]] <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>:
    *   On the left side, you'll see all the database properties (columns) that you defined <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   On the right side, you'll see the elements mapped from the template <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
    *   If you used the exact same naming convention for both database columns and template placeholders, [[mapping_database_elements_to_invoice_templates | PDF Output]] will automatically map them <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
    *   If there are differences in naming, the mapping will not be accurate, and you will need to manually select and map the corresponding elements <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
    *   Sorting, searching, and filtering options are available to assist in finding and mapping properties <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

### Key Rules for Effective Mapping

> [!tip] Placeholder and Column Naming
> Always put the placeholder text elements inside curly braces within your template <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. Use the exact same naming convention for these placeholders as you do for the corresponding columns in your database <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. This ensures automatic mapping and avoids manual adjustments <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## Generating PDFs

Once the mapping is correctly defined, click "create PDF" to generate the documents <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. The tool will generate individual PDFs for each row in your database, with the placeholder text replaced by the corresponding database entries <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

For instance, if your database has three rows with unique customer names, three distinct PDF documents will be generated, each personalized with the respective customer's information <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

## Reusing Connections

After creating a connection between a template and a database, it is saved under the "connections" tab <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. You can select an existing connection to automatically load the predefined database and template, allowing you to quickly generate documents without setting up a new connection every time <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

[[customizing_templates_and_databases_in_Notion | PDF Output]] also offers pre-defined templates that can be duplicated into your Notion workspace, complete with associated database links to help you get started <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.