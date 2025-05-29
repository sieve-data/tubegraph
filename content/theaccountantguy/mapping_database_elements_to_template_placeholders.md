---
title: Mapping database elements to template placeholders
videoId: WfYK1BJd490
---

From: [[theaccountantguy]] <br/> 

[[using_notion_templates_and_databases_for_pdf_creation | PDF Output]] is a tool that allows users to generate professional documents, such as invoices, directly from a Notion database by [[mapping_database_elements_to_template_placeholders | mapping database elements to template placeholders]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This process streamlines the creation of customized PDF documents for each entry in a database.

## Template and Database Structure

To use [[creating_and_using_templates_for_document_generation | templates]] and databases for document generation:
*   **Template Design** An invoice template, for example, features placeholder text for elements like client name, client company, client address, city, state, and zip <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. These placeholders are enclosed within curly braces (e.g., `{client name}`) <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. Any text within curly braces in the template is designated to be replaced by corresponding data from the database <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   **Database Content** The Notion database contains columns (or properties) such as "client name," "amount," "bank name," "client address," and "client company" <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Each row of information in this database will be used to populate a unique document based on the template <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## Connecting and Mapping with PDF Output

### Initial Setup
1.  **Log In**: Access the [[managing_templates_and_databases_within_pdfoutput | PDF Output]] interface <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
2.  **API Key Configuration**: Navigate to the "H" (help) section to complete the necessary steps for enabling API keys, which are essential for the integration <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Instructions for this setup are provided within the help section <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
3.  **Define Connection**: Assign a name for the connection (e.g., "invoice generation") <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
4.  **Select Database and Template**: Specify the Notion database (e.g., "professional invoice database") <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a> and the Notion template (e.g., "professional invoice template") to be used <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

### Automatic Mapping Process
Once the database and template are selected, clicking "next" initiates the loading and [[mapping_database_elements_to_template_elements | automatic mapping]] of database elements to template placeholders <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   The system loads all database properties, displayed on the left side of the interface <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   Each database property is then connected to a corresponding template element <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. For example, "client address" from the database is mapped to the "client address" placeholder in the template <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

### Mapping Requirements and Troubleshooting
For successful [[mapping_database_elements_to_template_elements | mapping]], the names of the placeholder elements in the template must precisely match the column names in the Notion database <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. If a match is not found, the unmapped element will appear in gray <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. Users can manually click on these gray elements to search for and select the correct corresponding database column <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### Document Generation
After [[synchronizing_database_elements_with_templates | synchronizing database elements with templates]], clicking "export" begins the document generation process <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   A "PDF status" column in the Notion database is automatically ticked as each PDF file is generated <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   Users can preview a sample of the generated PDF documents to verify the output <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   All generated files can be downloaded in a single action by clicking "download all" <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

### Customization
All elements within the template are [[customizing_pdf_templates_with_placeholder_elements | customizable]] to fit specific requirements <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. The key is to ensure that all placeholder text elements are enclosed in curly braces and that their names match the corresponding column names in the database <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.