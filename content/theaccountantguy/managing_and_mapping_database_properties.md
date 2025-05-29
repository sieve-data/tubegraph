---
title: Managing and Mapping Database Properties
videoId: W_j9W6XedqM
---

From: [[theaccountantguy]] <br/> 

This article explains how to manage database properties and map them to template fields for bulk PDF document generation using PDF output.com and Notion. The core idea is to replace specific elements within a template with data from a database <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Understanding Database Properties and Template Elements

A payment receipt template is used as an example, featuring elements enclosed in curly braces, such as `{{receipt_number}}` or `{{company_website}}` <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. These are the template elements that will be replaced.

A corresponding database contains columns (properties) with information for each record, such as "receipt number," "receipt date," "receipt time," "company website," and so forth <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. Each column in the database ideally corresponds to a template element <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

For instance, if the template has `{{Company Website}}` inside curly braces, the database should have a column named "Company Website" <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

## Setting Up Notion Database Properties and Templates

To begin, users need to duplicate both the example [[setting_up_notion_database_properties | Notion database]] and the Notion template into their local Notion workspace <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. This ensures that the structure for [[managing_and_editing_loan_details | managing and editing loan details]] (or in this case, payment receipts) is readily available.

Once duplicated, the database and template are then connected to PDF output.com. This involves giving PDF output.com permission to access the selected Notion pages (template and database) within the specified workspace <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

## [[mapping_notion_database_fields_to_templates | Mapping Notion Database Fields to Templates]]

After connecting, PDF output.com loads the database properties and template elements <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

The tool attempts to automatically [[mapping_database_elements_to_template_elements | map database elements to template elements]] <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. This automatic [[mapping_database_elements_to_template_fields | mapping of database elements to template fields]] occurs if the naming convention in the database columns precisely matches the naming convention of the template elements (including spaces and capitalization) <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

For example, if the template uses `{{Company Website}}`, the database column must be named "Company Website" for automatic mapping <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

### Manual Mapping

If there's a mismatch in naming conventions between the database and the template, the system will not automatically map the elements <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. In such cases, users need to manually select the corresponding database property for each unmapped template element <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

The interface provides options to filter for unmapped or mapped properties and includes search and sorting functions to facilitate this process <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

### Best Practices for Naming

To ensure seamless and automatic mapping, it is crucial to:
*   Enclose all elements in the template within curly braces (e.g., `{{Element Name}}`) <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
*   Use the exact same naming convention for database column headers as used for the template elements, including spaces and capitalization <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. This avoids the need for manual mapping during the second step of the PDF generation process <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

## Generating Bulk PDFs

Once the database properties and template elements are correctly mapped, the tool can generate PDF documents in bulk <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. For every row of information in the database, a separate PDF document is created by populating the template with the respective data <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

For instance, if the database has three rows of payment receipt information, three distinct PDF payment receipts will be generated <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. The output documents will reflect the data from each row, ensuring all fields are correctly populated (e.g., customer name, email, receipt number) <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. This process is useful for various applications, including [[using_databases_for_invoice_management | invoice management]] and [[customizing_and_managing_sales_data | customizing and managing sales data]].

## Managing Connections and Templates

After creating a connection, it is saved under the "Connections" section, allowing users to quickly reload previously configured database and template pairs without needing to manually re-add them <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

The "Templates" section provides access to a variety of predefined templates for different use cases, such as invoices <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Users can also add custom templates and databases via the settings <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. This flexibility supports various needs, including [[creating_a_database_with_number_properties_in_notion | creating a database with number properties in Notion]] for specific data types.