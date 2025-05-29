---
title: Generating and downloading PDF documents in bulk
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to [[bulk_pdf_document_generation | generate PDF documents in bulk]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. It leverages a Notion page as a template and a Notion database to supply the data for replacement <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Core Functionality

The process involves defining a Notion database and a Notion template within PDF Output <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. The database holds the elements to be replaced, and the template serves as the structure for the PDF <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Setting Up Your Notion Template and Database

Before using PDF Output, you need to create your template and database in Notion <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

### Creating a Notion Template

1.  Create a new page in your Notion workspace <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
2.  Add your desired content for the template <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. For example, an "Invitation Letter Template" <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
3.  Define sections that will be replaced by data from your database by enclosing them in curly braces, such as `{title}` and `{customer name}` <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. These placeholders will be replaced with specific data during PDF generation <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Creating a Notion Database

1.  Create another new page in Notion and select "Table" <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
2.  Define columns in the database with names that exactly match the placeholders in your template (e.g., `title` and `customer name`) <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
3.  Populate the database with unique information for each row; each row will generate a separate PDF document <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

## Connecting Notion to PDF Output

1.  Log into PDF Output <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
2.  Click "click here to add database" or "add template" <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. This will take you to a Notion authorization screen <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
3.  Select the Notion account you are using <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
4.  Click "Select pages" and choose both your template page and database page <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
5.  Click "Allow access" to authorize PDF Output to fetch your database and template <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
6.  Once redirected to PDF Output, you will see your chosen database and template loaded <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
7.  Provide a connection name (e.g., "invitation letter") <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

## Mapping Properties

1.  Click "Next" to proceed to the mapping section <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
2.  On the left, you'll see database properties (e.g., `customer name`, `title`) <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. On the right, you'll see the corresponding elements from your template that were defined in curly braces <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
3.  If the database column names precisely match the curly brace placeholders in the template, PDF Output will automatically map them <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
4.  If there are naming discrepancies, you will need to manually select and map the elements <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
5.  Mapping options include sorting, searching, and filtering to help manage properties <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

## [[exporting_and_downloading_pdf_documents | Generating and Downloading PDF Documents]]

1.  Once mapping is complete, click "Create PDF" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
2.  PDF Output will process and [[exporting_and_downloading_generated_pdf_documents | generate PDF documents]] <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
3.  You can preview a sample of a generated PDF <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
4.  Click "Download All" to [[exporting_and_downloading_pdf_documents | download all generated PDF documents]] as a zip file <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. Each row in your Notion database will result in a separate PDF <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

## Key Considerations for Generation

*   **Placeholders**: Always put placeholder text elements in your template inside curly braces (e.g., `{placeholder}`) <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   **Naming Convention**: Use the exact same naming convention for your database columns as for your template placeholders to ensure automatic mapping <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. If names differ, manual mapping is required <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## Additional Features

### Connections

The "Connections" tab in the sidebar lists all previously created connections <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. Clicking on a connection name (e.g., "invitation letter") will automatically load the predefined database and template, allowing for quick regeneration without re-setting up <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

### Templates

The "Templates" section provides a list of predefined templates <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. Each template includes a database link and a template link <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. To use a predefined template, click "Start with this template" to duplicate it to your Notion workspace <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. Remember to duplicate both the database and template files <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

### Upgrade Options

*   **Free Plan**: Generated PDFs on the free plan will have a watermark "made with PDF output" and certain limitations <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
*   **Upgrade**: You can upgrade your subscription by clicking the "Upgrade" option <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. After upgrading, click "activate subscription" to activate your plan <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

### Settings

*   **Page Format**: Choose your desired page format (e.g., A4, Letter) <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
*   **Add More Templates**: If you need to add more Notion templates or databases after initial setup, navigate to settings and click "click here to add more templates" <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

### Feedback and Help

*   **Feedback**: You can send feedback directly to the developer through the "PDF feedback" section <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Help**: The "Help" section contains a demonstration video for guidance <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.