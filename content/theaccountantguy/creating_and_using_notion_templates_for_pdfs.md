---
title: Creating and using Notion templates for PDFs
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to generate PDF documents in bulk using a Notion page as a template and a Notion database to supply the data for replacement elements <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## How PDF Output Works
The process involves selecting a Notion database and a Notion template within the PDF Output interface <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. The tool then replaces specific elements in the template with data from the database to generate individual PDF documents <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Setting Up Your Notion Template and Database

### [[creating_and_using_templates_for_pdf_generation_in_notion | Creating a Notion Template]]
First, you need to create a new page in your Notion workspace to serve as your template <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. For example, an "Invitation Letter Template" can be set to full-width mode <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

#### Placeholders
Sections of the template that will be replaced by database content must be enclosed in curly braces, such as `{title}` and `{customer name}` <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. These serve as placeholder elements <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

### [[creating_pdf_documents_from_a_notion_database | Creating a Notion Database]]
Next, create a new Notion database <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. This database will hold the information that replaces the placeholders in your template <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

#### Naming Convention
The column names in your database must precisely match the placeholder names used in your template (e.g., a "Title" column for `{title}` and a "Customer Name" column for `{customer name}`) <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. The database should contain rows with unique information for each PDF you wish to generate <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

## [[connecting_notion_databases_and_templates_for_pdf_creation | Connecting Notion to PDF Output]]

### Adding Database and Template
Within the PDF Output application, click "Click here to add database" or "Click here to add template" <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

### Authorization
You will be redirected to Notion to select the specific pages (your template and database) that PDF Output will use <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. Ensure you select the correct Notion account/workspace <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. After selecting and allowing access, PDF Output will automatically fetch the database and template <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

## Mapping Properties
After selecting your database and template, you'll need to define a connection name (e.g., "Invitation Letter") <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. The next step involves mapping database properties to template elements <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

### Automatic Mapping
If the database column names exactly match the placeholder names in the template, PDF Output will automatically map them <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

### Manual Mapping
If there are any naming discrepancies, the properties will not be automatically mapped <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. In such cases, you must manually select the corresponding database element for each template placeholder <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. Sorting, searching, and filtering options are available to assist with mapping <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

## Generating and Downloading PDFs
Once mapping is complete, click "Create PDF" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. PDF Output will generate the documents based on your database rows <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

### Previewing Samples
You can preview a sample PDF to ensure the output is correct <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

### Downloading All
After previewing, click "Download All" to receive a zip file containing all generated PDFs, with each PDF reflecting a row from your Notion database <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

## [[customizing_notion_templates_for_pdf_documents | Important Considerations]]
*   **Placeholder Text**: Always enclose placeholder text elements within curly braces in your Notion template <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.
*   **Naming Conventions**: Use the exact same naming convention for your database column names as your template placeholder names to enable automatic mapping <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. If names differ, manual mapping is required <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## Additional Features of PDF Output

### Connections
The "Connections" sidebar section allows you to save and quickly load previously defined database and template configurations, eliminating the need to set up new connections each time <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

### Predefined Templates
PDF Output offers a list of predefined templates in the "Templates" sidebar section <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. To use one, click "Start with this template" which will prompt you to duplicate both the database and template files into your Notion workspace <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

### Upgrade Options
The free plan includes a "Made with PDF Output" watermark and certain limitations <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. Upgrading your subscription removes the watermark and unlocks more features <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

### Settings
The "Settings" tab allows you to:
*   Choose a desired page format for your PDFs <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
*   Add more templates and databases after initial setup <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

### Feedback and Help
You can provide feedback through the "Feedback" section <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a> or find the demonstration video in the "Help" section <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. The sidebar can be closed to maximize screen space <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.