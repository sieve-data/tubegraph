---
title: Creating and using Notion templates for PDFs
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

[[Using Notion for generating PDF documents | PDF Output]] is a tool designed to generate PDF documents in bulk by utilizing a Notion page as a template and a Notion database to supply the elements to be replaced within that template <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## How it Works

The process involves three main steps:
1.  [[Creating and managing templates in Notion | Creating]] and setting up your Notion template and database.
2.  Connecting Notion to the [[PDF document creation with Notion and PDF output | PDF Output]] application.
3.  Mapping the database properties to the template placeholders and generating the PDFs.

### Setting Up Your Notion Template and Database

Before using [[PDF document creation with Notion and PDF output | PDF Output]], you need to [[creating_and_managing_templates_in_notion | create a template and a database from scratch]] within your Notion workspace <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

#### [[creating_and_using_templates_in_notion | Creating a Template Page]]
1.  Navigate to your Notion dashboard <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
2.  Click the "create a new page" icon on the left sidebar <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
3.  Give your template page a name, for example, "Invitation letter template" <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
4.  Optionally, set the page to full width mode <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
5.  Define the content of your template. Crucially, any sections of the template that you want to be replaced by data from your database must be defined inside curly braces <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. For example, `{title}` and `{customer name}` will be replaced with corresponding data <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. These curly-braced sections act as placeholder elements <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

#### [[creating_and_managing_templates_in_notion | Creating a Database]]
1.  Create another new page in Notion <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
2.  Select the "Table" option to create a new database <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
3.  Name your database, e.g., "Invitation letter database" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
4.  Define columns within this database with the *exact same naming convention* as the placeholder elements used in your template <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. For example, if your template uses `{title}` and `{customer name}`, your database should have columns named "Title" and "Customer Name" <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
5.  Populate your database with different rows, each containing unique information for the defined columns <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

### Connecting Notion to PDF Output

1.  Log into the [[PDF document creation with Notion and PDF output | PDF Output]] application <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
2.  You will see sections for "Notion database" and "Notion template" <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
3.  Click on "click here to add database" or "add template" <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
4.  This will direct you to a Notion authorization screen where you select the pages you want to use <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
5.  Ensure you select the correct Notion account/workspace <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
6.  Click "Select pages" and then choose both your template and your database from the list <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
7.  Click "Allow access" to initiate the authorization process, which will automatically fetch the database and template for use <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

### Mapping Properties and Generating PDFs

1.  Once redirected back to [[PDF document creation with Notion and PDF output | PDF Output]], your selected database and template will be displayed <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
2.  Define a connection name (e.g., "Invitation letter") <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
3.  Click "Next" <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
4.  The application will load the template and database. In this section, you define the mapping between your database properties (on the left) and your template placeholders (on the right) <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
    *   If you used the exact same naming convention for database columns and template placeholders (e.g., `title` in both), they will be automatically mapped <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
    *   If the names differ, you will need to manually select the corresponding element for mapping <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
5.  [[Customizing and Using Notion Templates | Sorting]], searching, and filtering options are available to manage your properties <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
6.  Once mapping is complete, click "Create PDF" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
7.  The system will generate the PDF documents, creating one PDF for each row in your database <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
8.  You can preview a sample PDF or download all generated documents <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

### Important Considerations

*   **Placeholder Naming**: Always enclose placeholder text elements in your template within curly braces (e.g., `{Your Element}`) <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   **Exact Naming Convention**: Use the exact same naming convention for the column names in your database as the placeholder elements in your template. This allows for automatic mapping <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. If names differ, manual mapping is required <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

### Additional Features

*   **Connections**: Once a connection between a database and template is established, it's saved under the "Connections" tab in the sidebar. This allows you to quickly load predefined setups without creating a new connection every time <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   **Templates**: The "Templates" section provides access to [[using_predefined_templates_in_notion_for_pdf_generation | predefined templates]] with their corresponding database and template links <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. To use one, click "Start with this template" and duplicate both the database and template to your Notion workspace <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
*   **Upgrade Option**: The free plan includes a watermark ("Made with [[PDF document creation with Notion and PDF output | PDF Output]]") and certain limitations. You can upgrade your subscription to remove these <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
*   **Settings**: Customize page formats and add more templates or databases through the settings tab <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
*   **Feedback**: A feedback section is available to send messages directly to the developer <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Help Section**: A help section contains a demonstration video for guidance <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.