---
title: Mapping database properties to template placeholders
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to generate PDF documents in bulk by utilizing a Notion page as a template and a Notion database to supply the content for replacement within that template <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Setting Up Your Notion Template and Database

Before using PDF Output, you need to prepare your Notion workspace by creating both a template and a database.

### Creating a Template

1.  Start by creating a new blank page in Notion <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
2.  Give it a name, such as "Invitation Letter Template" <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
3.  Set the page to "full width" mode <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
4.  Define your template content. Crucially, any sections that need to be replaced with data from your database should be enclosed in curly braces `{}` <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
    *   For example, `{title}` and `{customer name}` would be placeholders for dynamic content <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

### Creating a Database

1.  Create another new page in Notion and choose the "Table" format <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
2.  Name your database, e.g., "Invitation Letter Database" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
3.  Define the columns (properties) in your database. The names of these columns **must exactly match** the placeholder text defined in curly braces within your template <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>, <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
    *   For instance, if your template has `{title}` and `{customer name}`, your database should have columns named "title" and "customer name" <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
4.  Populate your database with the data you want to use for PDF generation <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

## Connecting Notion to PDF Output

1.  Log into PDF Output. You will see sections for "Notion database" and "Notion template" <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
2.  Click "Click here to add database" or "Click here to add template" <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
3.  You will be redirected to Notion to select the pages. Ensure you select the correct Notion account/workspace <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
4.  Choose both your created template page and your database page <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
5.  Click "Allow access" to authorize PDF Output to fetch your chosen database and template <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
6.  PDF Output will then sync these elements automatically <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
7.  Define a "Connection name" (e.g., "Invitation Letter") for this setup <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
8.  Click "Next" <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

## [[mapping_notion_database_elements_to_templates | Mapping Notion Database Elements to Templates]]

This section allows you to define how the database properties will be mapped to the template placeholders.

*   On the left side, you will see all the properties (column names) from your Notion database <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   On the right side, you will see the corresponding elements from your template that were enclosed in curly braces <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

### Automatic Mapping

*   If the database property names perfectly match the template placeholder names (e.g., "customer name" in the database maps to `{customer name}` in the template), PDF Output will [[automatically_mapping_database_properties_to_template_elements | automatically map database properties to template elements]] <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>, <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

### Manual Mapping

*   If there are discrepancies in naming between the database and the template, the mapping will not be accurate <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. In such cases, you will need to manually click on each unmapped element and select the correct corresponding property from the database <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>, <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

### Mapping Section Features

The mapping section includes useful features:
*   **Sorting**: Sorts elements alphabetically <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **Search**: Allows you to quickly search for specific elements <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
*   **Filtration**: Can filter to show only unmapped properties <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

### Key Rule for Placeholders
*   Always put placeholder text elements inside curly braces `{}` in your Notion template <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   Use the exact same naming convention for these placeholders as you use for your database column names <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

## Generating PDFs

Once the mapping is complete and accurate, click "Create PDF" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. The tool will then generate individual PDF documents for each row of data in your database, with the placeholder text [[replacing_placeholder_text_in_templates_with_database_values | replaced by database values]] <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. You can preview a sample or download all generated PDFs <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>, <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

## [[managing_and_using_predefined_templates | Managing and Using Predefined Templates]] and Connections

PDF Output offers features to streamline your workflow:

### Connections
*   The "Connections" sidebar section displays all previously created database-template mappings <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   Clicking on a saved connection will automatically load the predefined database and template, allowing you to bypass the initial setup steps and proceed directly to PDF generation <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

### Predefined Templates
*   The "Templates" sidebar section provides access to a list of predefined templates <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   Each predefined template comes with a database link and a template link <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
*   To use a predefined template, click "Start with this template" <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. This will prompt you to duplicate both the template and its associated database into your Notion workspace <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>, <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

## Additional Features
*   **Page Format**: Under the settings tab, you can choose different page formats for your generated PDFs <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
*   **Adding More Templates**: If you need to add more templates and databases after initial setup, you can do so via the settings tab <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   **Feedback**: A feedback section allows you to send messages directly to the developer for assistance or suggestions <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.