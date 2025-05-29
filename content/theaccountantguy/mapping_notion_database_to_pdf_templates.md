---
title: Mapping Notion Database to PDF Templates
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to [[using_notion_templates_and_databases_for_pdf_generation | generate PDF documents in bulk]] by combining a Notion page as a template and a Notion database containing the data to be inserted into the template <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## How it Works <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>

The process involves defining a Notion database for PDF generation and selecting a Notion template for the document <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

### Creating Notion Components

Before using PDF Output, you need to [[setting_up_a_notion_database_and_template_for_pdf_generation | create a database and a template in Notion]] from scratch <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

1.  **[[using_notion_for_pdf_template_creation | Creating a Template Page]]**:
    *   Create a new Notion page and name it (e.g., "Invitation Letter Template") <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
    *   Set the page to full width mode if desired <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
    *   Define the content of your template <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
    *   Crucially, any sections that need to be replaced with data from the database must be enclosed in curly braces (e.g., `{title}`, `{customer name}`) <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. These "placeholder texts" will be automatically mapped to database elements <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

2.  **[[creating_a_notion_database_for_pdfs | Creating a Database]]**:
    *   Create a new Notion page and select the "Table" option <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
    *   Name your database (e.g., "Invitation Letter Database") <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
    *   Define columns in the database with names that exactly match the placeholder texts used in your template (e.g., `title`, `customer name`) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This exact naming convention is vital for automatic mapping <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
    *   Populate the database with rows of unique information <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

### [[connecting_notion_database_with_pdf_output | Connecting Notion to PDF Output]]

1.  **Add Database and Template**:
    *   In PDF Output, click to add your Notion database and template <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
    *   Select the correct Notion account/workspace <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   Choose the specific template and database pages you created in Notion <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
    *   Click "Allow Access" to authorize PDF Output to fetch your Notion data <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
    *   Give your connection a name (e.g., "Invitation Letter") <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

2.  **[[mapping_notion_database_elements_to_pdf_templates | Mapping Properties]]**:
    *   After adding, the tool will automatically load the template and database <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
    *   The left side shows your Notion database properties (columns), and the right side shows the corresponding elements mapped from your template <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   If you used the exact same naming convention for placeholder texts in the template and column names in the database, the mapping will occur automatically <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
    *   If there are any naming differences, you will need to manually select the correct database property for each template element <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
    *   Sorting, searching, and filtering options are available to help manage properties <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

### Generating PDFs

1.  **Create PDF**: Once mapping is complete, click "Create PDF" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
2.  **Preview and Download**:
    *   The tool will generate the PDFs, substituting the placeholder texts in the template with data from each row of your Notion database <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
    *   You can preview a sample PDF <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
    *   Click "Download All" to get all generated PDF documents <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. Each row in the database will result in a separate PDF file <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

## Important Notes & Best Practices

*   Always enclose placeholder text elements in your Notion template inside curly braces `{}` <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   Use the exact same naming convention for column headers in your Notion database as the placeholder texts in your template for automatic mapping <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   If column names differ, you will need to manually map them in the mapping section <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## Additional Features of PDF Output

*   **Connections**: Once a connection is created, you can easily load predefined database and template setups from the "Connections" tab for future use, avoiding the need to create a new connection every time <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   **Templates**: PDF Output provides predefined templates that you can use. To use them, you must duplicate both the database and the template file from the provided links into your Notion workspace <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   **Upgrade**: The free plan includes a "Made with PDF Output" watermark and certain limitations. You can upgrade your subscription to remove these <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
*   **Settings**: Adjust page format for your PDFs <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. You can also add more templates and databases subsequently from this section <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
*   **Feedback**: Provide feedback directly to the developer <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Help**: Access the demonstration video within the application <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.