---
title: Setting up Notion databases for PDF generation
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to [[generating_pdf_documents_from_notion_database | generate PDF documents]] in bulk, using a Notion page as a template and a Notion database to supply the elements for replacement within that template <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Getting Started with PDF Output
Upon logging into PDF Output, users will find sections for "Notion database" and "Notion template" <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. The Notion database section requires defining the database for PDF generation, while the Notion template section requires selecting the specific template to be used <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Creating a Notion Template
Before [[connecting_notion_databases_and_templates_for_pdf_creation | connecting the database and template]] within PDF Output, they must first be created in Notion <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
To create a new template:
1.  Navigate to your Notion dashboard <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
2.  Click on the "create a new page" icon <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
3.  Name the new page (e.g., "Invitation Letter Template") <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
4.  Optionally, set the page to "full width mode" <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
5.  Define the content for your template <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
6.  Crucially, define sections that will be replaced by database content inside curly braces, such as `{title}` and `{customer name}` <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. These curly-braced elements serve as placeholders for the data <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

## [[setting_up_a_database_in_notion | Setting up a Notion Database]]
The database will hold the information that replaces the placeholders in the template <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
To create a new database:
1.  Click on the "create a new page" icon in Notion <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
2.  Select "table" to create a new table database <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
3.  Name the database (e.g., "Invitation Letter Database") <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
4.  Define columns within the database with exact same naming conventions as the placeholder elements in the template (e.g., "title" and "customer name") <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This precise naming ensures automatic mapping between the template and database <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
5.  Populate the database with rows of unique information for each PDF document you wish to generate <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

## [[setting_up_notion_api_keys_for_pdf_document_creation | Connecting Notion to PDF Output]]
Once the template and database are prepared in Notion:
1.  Return to PDF Output <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
2.  Click on "click here to add database" or "add template" <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
3.  You will be redirected to Notion to select the pages for use <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. Ensure the correct Notion account is selected <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
4.  Click "Select pages" and choose both the template and the database you created <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
5.  Click "Allow access" to begin the authorization and syncing process, which will automatically fetch the database and template <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
6.  Once redirected back to PDF Output, the selected database (e.g., "Invitation database") and template (e.g., "Invitation letter template") should be available <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
7.  Define a connection name (e.g., "invitation letter") <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

## Mapping Properties for PDF Generation
After setting the connection name, click "next" <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
1.  This section defines the properties to map between the database and template <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
2.  On the left, you'll see database properties (e.g., "customer name" and "title") <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
3.  On the right, the corresponding template elements (defined in curly braces) should be automatically mapped if the naming convention is exact <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
4.  If names do not match, manual mapping is required by clicking on the element and selecting the correct property <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
5.  Sorting, searching, and filtration options are available to manage properties <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

## [[generating_pdf_documents_from_notion_database | Generating PDF Documents]]
Once mapping is complete, click "create PDF" to start the PDF generation process <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. After generation, you can "preview sample" to check a generated document (e.g., for "Dr. Harry") <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. Click "download all" to save all generated PDFs <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>, which will produce individual PDF files for each row in the database <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

### Important Considerations:
*   Always put placeholder text elements in the template inside curly braces (e.g., `{placeholder}`) <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   Use the exact same naming convention for columns in your Notion database as the placeholder text in your template <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. If names differ, manual mapping will be necessary <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## Managing Connections and Templates
*   **Connections**: In the sidebar, the "Connections" section shows all previously created connections <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. Selecting a connection (e.g., "invitation letter") automatically loads its predefined database and template, allowing for quicker document generation without re-creating a new connection <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Templates**: The "Templates" section provides a list of pre-defined templates <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. Each template includes a database link and a template link <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. To [[using_notion_templates_for_pdf_generation | use one of these templates]], click the "start with this template" option, which prompts you to duplicate the template and its associated database into your Notion workspace <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

## Additional Features
*   **Upgrade Option**: The free plan includes a watermark ("Made with PDF Output") and certain limitations <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. Users can upgrade their subscription plan <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   **Settings**: This tab allows selection of different page formats for the generated PDFs <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. It also provides an option to add more templates and databases after the initial setup <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.
*   **Feedback**: Users can provide feedback directly through a dedicated section <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Help**: A "Help" section contains a demonstration video for user guidance <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.