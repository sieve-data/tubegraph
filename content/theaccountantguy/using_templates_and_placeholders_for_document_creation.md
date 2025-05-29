---
title: Using templates and placeholders for document creation
videoId: lCyhl8mofjE
---

From: [[theaccountantguy]] <br/> 

This guide outlines how to use templates and placeholders to generate documents, specifically focusing on creating lease agreements from a Notion database using the PDF Output application <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>, <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Understanding Templates and Placeholders

A template is a pre-designed document structure containing common text and designated placeholder elements <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. These placeholders, often enclosed in curly braces (e.g., `{landlord_name}`), act as dynamic fields that will be replaced with specific data during document generation <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

For a lease agreement, a template would include placeholder elements for details such as:
*   Landlord name <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>, <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>
*   Tenant name <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>, <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>
*   Street address <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>

This allows for the creation of multiple, personalized documents from a single template structure, with varying information drawn from a database <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## Setting up PDF Output for Document Generation

To begin [[creating_and_using_templates_for_document_generation | generating PDF documents]], you need to set up the PDF Output application <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

1.  **Log In**: Access the PDF Output application <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
2.  **Initial Setup**: Navigate to the "Help" section within the application to follow instructions on setting up necessary components, such as API keys <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>, <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>, <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. This step is crucial before attempting to [[using_templates_to_generate_pdf_documents | generate PDF documents]] <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## Connecting Notion Database and Template

After the initial setup, you can connect your Notion database and template to the PDF Output application:

1.  **Specify Connection Name**: Provide a name for your connection, such as "Lease Agreement" <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>, <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
2.  **Select Database**: From the dropdown menu, choose the Notion database that is connected via API key (e.g., "lease") <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>, <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. This database should contain the data to populate your documents (e.g., landlord names, tenant names, street addresses) <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
3.  **Select Template**: Choose the corresponding Notion page template (e.g., "lease template") <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>, <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. This template includes the placeholder elements to be filled <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Mapping Database Elements to Template Placeholders

Once the database and template are selected, the application loads their elements:

*   **Automatic Mapping**: The system automatically maps Notion properties (database fields) to the PDF template's placeholder elements if their names match <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>, <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Review and Adjust Mapping**:
    *   Notion properties are listed on the left side of the interface <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
    *   Corresponding template elements are displayed on the right <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
    *   If any mapping is missing or incorrect (indicated by a gray or red-colored element), you can manually select the correct property from the dropdown <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>, <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>, <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>, <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. It is recommended that the naming convention of the database and template matches exactly to facilitate automatic mapping <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

## Generating and Downloading Documents

With the mapping confirmed, you can proceed to generate the documents:

1.  **Initiate Export**: Click the "Export" button <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
2.  **PDF Status Property**: A "PDF status" column will appear in your Notion database <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>, <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. This column tracks which rows (documents) have been generated. Unticked rows are processed, and a tick mark indicates successful generation <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>, <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>, <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
3.  **Preview Sample**: Once processing is complete, you can click "Preview Sample" to view one of the generated documents <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>, <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. This allows you to verify that the placeholder text has been correctly replaced with the database values (e.g., landlord name "Tom Green" and tenant name "Sarah Blue") <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>, <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>, <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
4.  **Download All**: To download all generated documents, click "Download All." This will typically download them in a single archive file <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>, <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. You can open individual files to confirm their content, such as a lease agreement for "Alice Brown" and "Bob White" <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>, <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>, <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

This process enables efficient [[creating_notion_templates_and_databases_for_pdf_generation | bulk document generation]] by [[customizing_pdf_templates_with_placeholder_elements | customizing PDF templates with placeholder elements]] and [[mapping_database_elements_to_template_placeholders | mapping database elements to template placeholders]].