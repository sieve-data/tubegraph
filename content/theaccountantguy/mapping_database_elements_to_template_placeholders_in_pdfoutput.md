---
title: Mapping database elements to template placeholders in PDFOutput
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

[[using_pdfoutput_for_document_generation | PDFOutput]] is a tool designed to generate PDF documents in bulk by using a Notion page as a template and a Notion database to hold the data that will replace elements within that template <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This process relies on effectively mapping database elements to specific placeholders in your template.

## Defining Placeholders in Templates

To create a template in Notion for use with [[setting_up_and_configuring_pdfoutput | PDFOutput]], you define sections or words that need to be replaced by data from a database. These placeholders are identified by enclosing them within curly braces, for example, `{title}` or `{customer name}` <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. The content inside these curly braces indicates that these parts will be dynamically replaced by corresponding database values <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## Preparing the Notion Database

For seamless [[mapping_notion_database_fields_to_pdf_templates | mapping Notion database fields to PDF templates]], the Notion database columns should have the *exact same naming convention* as the placeholders defined in the template <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. For instance, if your template has a placeholder `{title}`, your database should have a column named "title" <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

## The Mapping Process in PDFOutput

Once you have selected your Notion database and template within [[setting_up_and_configuring_pdfoutput | PDFOutput]], the application guides you to a mapping section <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

On the left side of this section, you will see all the properties (column names) from your selected Notion database <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. On the right side, [[setting_up_and_configuring_pdfoutput | PDFOutput]] displays the elements identified in your template that were enclosed in curly braces <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

*   **Automatic Mapping**: [[mapping_database_elements_to_template_fields | PDFOutput]] automatically maps template placeholders to database properties if they share the exact same name <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   **Manual Mapping**: If there are any discrepancies in naming between the database columns and the template placeholders, [[setting_up_and_configuring_pdfoutput | PDFOutput]] will not automatically map them <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. In such cases, you will need to manually select the corresponding element from a dropdown menu for accurate mapping <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

### Mapping Section Features
The mapping section also provides utility features to assist with the process:
*   **Sorting**: You can sort all elements in alphabetical order <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **Searching**: A search option allows you to quickly find specific elements <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
*   **Filtering**: A filtration option helps identify properties that have not yet been mapped <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

Once the mapping is complete and accurate, you can proceed to [[creating_and_using_templates_for_pdf_generation | create PDFs]] <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. The generated PDFs will show the template with the placeholders replaced by the corresponding data from each row of your Notion database <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

## Key Considerations for Mapping
*   Always enclose placeholder text elements in your template within curly braces <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   Use the exact same naming convention for placeholder elements in the template and column names in your Notion database for automatic mapping <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   If names differ, manual mapping in the dedicated section is required <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.