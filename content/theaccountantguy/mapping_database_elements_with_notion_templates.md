---
title: Mapping database elements with Notion templates
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

[[using_notion_templates_and_databases_for_pdf_creation | PDF Output]] is a tool designed to generate PDF documents in bulk by utilizing a Notion page as a template and a Notion database to hold the elements for replacement within that template <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The core of this process involves [[mapping_database_elements_to_template_placeholders | mapping database elements to template placeholders]] <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

## Setting Up Notion for Mapping

Before [[mapping_database_elements_to_template_placeholders | mapping Notion database elements to template placeholders]], you need to prepare both your Notion template and database <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>:

### Creating a Template
1.  In your Notion workspace, [[creating_a_database_in_notion | create a new page]] to serve as your template <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. For instance, an "Invitation Letter Template" <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
2.  Define the static content of your template <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
3.  For any dynamic content that needs to be replaced by database information, define these sections inside curly braces `{}`. These act as placeholders <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. For example, `{title}` and `{customer name}` would be placeholders for an invitation letter <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

### Creating a Database
1.  [[creating_a_database_in_notion | Create a new table]] (database) in Notion <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
2.  Define columns in the database with the *exact same naming convention* as the placeholder names used in your template (e.g., "title" and "customer name") <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>, <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. This ensures automatic mapping <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
3.  Populate the database with the unique information for each row, which will be used to generate individual PDF documents <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

## Connecting Notion to PDF Output

1.  Log into [[using_notion_templates_and_databases_for_pdf_creation | PDF Output]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
2.  Click to add your Notion database and template <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
3.  Select the specific Notion account and then choose the template page and database table you created from your workspace <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>, <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
4.  Click "Allow access" to authorize [[connecting_notion_database_and_templates_to_pdf_output | PDF Output]] to fetch your Notion data <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
5.  Once synced, you will see your selected database and template listed <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

## The Mapping Process

After [[connecting_notion_database_and_templates_to_pdf_output | connecting Notion database and templates to PDF output]], you proceed to the mapping section <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>:

*   **Left Side:** Displays all properties (columns) from your Notion database <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   **Right Side:** Shows the elements (placeholders) defined in your Notion template <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   **Automatic Mapping:** If the database column names are identical to the template placeholders (e.g., both are named "title" and "customer name"), [[mapping_notion_database_elements_to_template_placeholders | PDF Output]] will automatically map them <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   **Manual Mapping:** If there are any discrepancies in naming, the mapping will not be automatic. You will need to manually select the correct database property for each template element <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
*   **Best Practice:** Always put placeholder text elements inside curly braces `{}` in your template and use the exact same naming convention for the corresponding columns in your database for seamless automatic mapping <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

### Mapping Tools
*   **Search:** Quickly find specific elements <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   **Filter:** View only unmapped properties <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
*   **Sort:** Arrange elements alphabetically <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

Once all properties are correctly [[mapping_database_elements_to_template_elements | mapped]], you can proceed to create the PDF documents <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.