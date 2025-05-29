---
title: Creating templates and databases in Notion
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to generate PDF documents in bulk by [[using_notion_for_templates_and_databases | using a Notion page as a template]] and a [[creating_database_in_notion | Notion database]] to hold the elements to be replaced in that template <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This process requires users to define both a Notion database and a Notion template within the PDF Output interface for PDF generation <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## [[creating_templates_and_databases_in_notion | Creating Templates and Databases in Notion]]

To begin, you will need to [[creating_and_setting_up_a_database_in_notion | create a database and a template]] from scratch in Notion <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

### Creating a Notion Template

1.  **Create a New Page**: In your Notion workspace, click on the "Create a new page" icon on the left sidebar <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This will open a blank page <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
2.  **Name the Template**: Give your page a descriptive name, such as "Invitation letter template" <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
3.  **Set to Full Width (Optional)**: You can set the page to full width mode for better content display <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
4.  **Define Content and Placeholders**: Add the main content of your template <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
    *   **Placeholders**: Sections of the template that will be replaced by data from your database must be defined inside curly braces `{}` <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. For example, to replace a title and customer name, you would include `{title}` and `{customer name}` in your template <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. These placeholders indicate the specific elements that will be replaced using the database <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Creating a Notion Database

1.  **Create a New Page**: Similar to creating a template, click on the "Create a new page" icon in Notion <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
2.  **Select Table View**: Choose the "Table" option to [[creating_a_database_in_notion | create a database]] <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
3.  **Name the Database**: Name your database, for instance, "Invitation letter database" <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
4.  **Define Columns**: Add columns to your database that correspond exactly to the placeholders in your template <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
    *   **Matching Column Names**: The naming convention for database columns (e.g., "title", "customer name") must precisely match the placeholder names in the template (e.g., `{title}`, `{customer name}`) <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. This ensures automatic mapping within PDF Output <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
5.  **Populate Data**: Fill your database with rows of unique information that will replace the placeholders in your template <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## Connecting Notion to PDF Output

Once your template and database are set up in Notion, you can connect them to PDF Output for generation.

### Selecting Database and Template

1.  **Add Notion Pages**: In PDF Output, click to add your Notion database or template <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
2.  **Authorize Notion**: You will be redirected to Notion to select the specific pages (your template and database) you wish to use <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. Ensure you select the correct Notion workspace <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
3.  **Allow Access**: After selecting, click "Allow access" to authorize PDF Output to fetch your chosen database and template <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
4.  **Define Connection Name**: Provide a connection name (e.g., "invitation letter") for future use <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

### Mapping Properties

1.  **Automatic Mapping**: If your database column names exactly match your template placeholder names, PDF Output will automatically map the properties <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
2.  **Manual Mapping**: If there are any naming differences, you will need to manually select the correct corresponding element for mapping <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
    *   The left side displays database properties, while the right side shows elements from the template <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
3.  **Sorting and Filtration**: Options are available to sort, search, or filter properties, which is helpful if some properties are not mapped <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

## Generating PDFs

Once all properties are mapped, click "Create PDF" to generate the documents <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. PDF Output will create individual PDF documents for each row of data in your Notion database, filling in the template's placeholders <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. You can preview a sample before downloading all generated PDFs <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

## Important Considerations

*   **Placeholder Naming**: Always enclose placeholder text elements in curly braces `{}` within your Notion template <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Exact Naming Convention**: Use the exact same naming convention for your database column headers as you do for your template placeholders <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   **Reusing Connections**: Once a connection is created, you can easily load predefined databases and templates from the "Connections" sidebar without recreating them <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

### Using Pre-defined Templates

PDF Output offers pre-defined templates that users can utilize <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

*   **Access Templates**: In the sidebar, click on "Templates" to see a list of available templates <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
*   **Duplicate to Notion**: To use a pre-defined template, click on "Start with this template" <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. This will prompt you to duplicate the template and its corresponding database into your own Notion workspace <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
*   **Workspace Selection**: Select your Notion workspace and click "Add to private" to add the duplicated page to your Notion account <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

[!NOTE]
When using pre-defined templates, remember to duplicate both the database and the template file from the provided links within PDF Output <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.