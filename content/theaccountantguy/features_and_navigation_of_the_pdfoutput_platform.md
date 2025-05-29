---
title: Features and navigation of the PDFOutput platform
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

PDFOutput is a tool designed to simplify the process of generating bulk PDF documents <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It uses a Notion page as a template and a Notion database to supply the content that replaces placeholder elements in the template <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Core Document Generation Process

When a user logs into PDFOutput, they are presented with sections for Notion database and Notion template selection <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

### Setting Up Notion Components

Before selecting pages within PDFOutput, users must prepare their template and database in Notion <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

*   **Template Creation**: A Notion page serves as the template <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.
    *   To create one, click the "create a new page" icon in Notion <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
    *   Content within the template that needs to be replaced must be enclosed in curly braces (e.g., `{title}`, `{customer name}`) <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. These "placeholder text elements" are crucial for mapping data <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Database Creation**: A Notion database holds the data for replacement <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.
    *   Create a new page and select "table" for the database <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>, <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
    *   The column names in the database must exactly match the placeholder names in the template (e.g., "title" column for `{title}`) for automatic mapping <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>, <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>, <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
    *   The database contains rows of unique information, each corresponding to a PDF document to be generated <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### Connecting Notion to PDFOutput

To connect Notion pages:
1.  Click "click here to add database" or "add template" in PDFOutput <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
2.  This redirects to Notion's authorization screen where you select the specific Notion account and pages (template and database) to be used <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>, <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
3.  Click "Allow access" to authorize the connection <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. PDFOutput will automatically fetch the selected database and template <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
4.  Define a connection name (e.g., "invitation letter") <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

### Mapping Properties and Generating PDFs

1.  After connection, the platform loads the template and database <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
2.  **Property Mapping**: The left side shows database properties (columns), and the right side shows corresponding template elements <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   If column names and placeholder names match exactly, mapping is automatic <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
    *   If names differ, manual selection is required <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>, <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
    *   Options for sorting, searching, and filtering unmapped properties are available <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
3.  **PDF Generation**: Click "Create PDF" to start the generation process <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
    *   PDFOutput will generate a separate PDF for each row in the Notion database <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>, <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
    *   Users can preview a sample PDF before downloading all documents <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
    *   All generated PDFs can be downloaded at once <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

## Platform Navigation and Sidebar Features

The PDFOutput platform includes a sidebar with several key features for navigation and management <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. The sidebar can be closed to maximize screen space <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.

### Connections

The "Connections" section displays all previously created database-template mappings <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   Selecting a saved connection automatically loads the predefined database and template, allowing for quicker re-generation without re-configuring <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>, <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

### Templates

The "Templates" section provides a list of predefined templates available for user requirements <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   Each template entry includes links to its associated Notion database and template, allowing users to view them <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
*   To use any of these predefined templates, click "start with this template" to duplicate both the template and database to your Notion workspace <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>, <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

### Upgrade

The "Upgrade" section manages subscription plans <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
*   The free plan includes a "Made with PDFOutput" watermark and certain limitations <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
*   Users can click "Upgrade Subscription" to change their plan <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   It shows the current plan and renewal date <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.
*   After upgrading, users must click "Activate Subscription" <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

### Settings

The "Settings" tab provides configuration options <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Page Format**: Users can choose their desired page format for the PDFs <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
*   **Add More Templates**: After the initial setup, users can add additional templates and databases by clicking "click here to add more templates" in the settings <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

### Feedback

The "Feedback" section allows users to send direct messages for support or suggestions <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

### Help

The "Help" section contains a demonstration video of the platform's features and usage <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.