---
title: Managing Templates and Databases in PDFOutput
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed for generating PDF documents in bulk <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. It uses a Notion page as a template and a Notion database to hold the elements that will be replaced in the template <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## How PDF Output Works

To utilize PDF Output, users define a Notion database for PDF generation and select a Notion page as the template <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

### [[creating_and_using_templates_for_pdf_generation | Creating and Using Templates and Databases]]

Before generating PDFs, users must create a Notion page to serve as the template and a Notion database to supply the data <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

#### Creating a Template
A template is a Notion page containing content with specific sections defined inside curly braces <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. These "placeholder" elements will be replaced by data from the database <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. For example, `{{title}}` and `{{customer name}}` are placeholders <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

#### Creating a Database
The database is a Notion table with columns that precisely match the names of the placeholder elements in the template <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. For instance, if the template has `{{title}}` and `{{customer name}}`, the database should have "title" and "customer name" columns <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Each row in the database will represent a unique PDF document to be generated <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

#### Connecting Notion to PDF Output
To connect your Notion pages and databases to PDF Output:
1.  Click "Click here to add database" or "Add template" within PDF Output <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
2.  You will be redirected to Notion to select the specific pages (templates and databases) to grant access <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
3.  Select the desired template and database and click "Allow access" <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
4.  PDF Output will automatically fetch and display the selected database and template <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
5.  Define a connection name (e.g., "Invitation Letter") for future use <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

### [[mapping_database_elements_to_templates_for_pdf_generation | Mapping Database Elements to Templates]]

After selecting the database and template, the next step is to map their properties <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   The left side displays all database properties (columns) <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   The right side displays the corresponding elements from the template (those in curly braces) <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   If the naming conventions are exact, elements will map automatically <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   If names differ, you will need to manually select the correct database property for each template element <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
*   Options for sorting, searching, and filtering are available to help manage mappings <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

> [!important] Naming Convention
> Always put placeholder text elements inside curly braces (e.g., `{{placeholder}}`) and use the exact same naming convention for the corresponding column in your Notion database <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. This ensures automatic and accurate mapping <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

### Generating PDFs
Once mappings are confirmed, click "Create PDF" to generate the documents <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   You can preview a sample PDF before downloading all <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   All generated PDFs can be downloaded at once <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. Each PDF will be populated with data from a different row of your Notion database <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

## [[managing_connections_and_templates_in_pdf_output | Managing Connections and Templates]]

PDF Output offers several features to manage your connections, templates, and settings.

### Connections
The "Connections" sidebar allows you to view and reload all previously created connections <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. Selecting an existing connection will automatically load its predefined database and template, eliminating the need to create a new connection each time <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

### Templates
The "Templates" sidebar provides access to a list of predefined templates <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   For each template, a database link and a template link are provided <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
*   To use a predefined template, click "Start with this template," which prompts you to duplicate it (along with its associated database) to your Notion workspace <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

### [[managing_pdf_output_templates_and_settings | Settings]]
The "Settings" tab provides various options:
*   **Page Format:** Choose your desired page format for the generated PDFs <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
*   **Add More Templates:** Subsequently add more Notion databases and templates to PDF Output <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.
*   **Upgrade Option:** Details about plan limitations (e.g., watermark on free plans) and options to upgrade your subscription <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
*   **Feedback:** A section to send direct feedback to the developer <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Help:** Access to this demonstration video and other resources <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.