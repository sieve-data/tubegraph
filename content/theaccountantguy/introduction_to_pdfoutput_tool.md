---
title: Introduction to PDFOutput tool
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

[[generating_pdfs_from_notion_using_pdfoutput | PDFOutput]] is a simple tool designed to help users [[using_pdfoutput_com_to_create_bulk_pdf_documents | generate PDF documents in bulk]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. It leverages a Notion page as a template and a Notion database to supply the data for replacement within the template <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Core Functionality

When you log into [[using_pdfoutput_settings_and_subscription_options | PDFOutput]], you'll find sections for a Notion database and a Notion template <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. You need to define which Notion database will be used for PDF generation and select the specific Notion page that will serve as the template <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Steps to Generate PDFs

To [[using_pdfoutput_com_to_create_bulk_pdf_documents | generate PDF documents in bulk]] with [[generating_pdfs_from_notion_using_pdfoutput | PDFOutput]], follow these steps:

### 1. Prepare Notion Template and Database
Before using [[managing_templates_and_databases_within_pdfoutput | PDFOutput]], you need to create a Notion database and a Notion template <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

*   **Create a Notion Template:**
    *   Start a new blank Notion page <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
    *   Define the content for your template, such as an "invitation letter template" <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
    *   Crucially, define sections that will be replaced with data by placing them inside **curly braces** (e.g., `{title}` and `{customer name}`) <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. These serve as placeholder elements <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

*   **Create a Notion Database:**
    *   Create a new Notion page and select the "Table" option <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
    *   Define columns in the database with **exact same naming convention** as the placeholder elements in your template (e.g., "title" and "customer name") <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
    *   Populate the database with rows of unique information that will be used to replace the placeholders in the template <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

### 2. Connect Notion to PDFOutput
*   In the [[using_pdfoutput_settings_and_subscription_options | PDFOutput]] interface, click to add a database or template <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   You will be redirected to Notion to select the specific pages (your template and database) you want to use <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   Ensure you select the correct Notion account/workspace <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   After selecting, click "Allow access" to authorize [[generating_pdfs_from_notion_using_pdfoutput | PDFOutput]] to fetch the database and template <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   Once redirected back to [[using_pdfoutput_settings_and_subscription_options | PDFOutput]], confirm the database and template are correctly loaded <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

### 3. Map Properties and Generate
*   Provide a connection name (e.g., "invitation letter") <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   Click "Next" to load the template and database properties <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   On the left, you'll see database properties, and on the right, mapped template elements <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. If the naming convention is exact, mapping happens automatically <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   If names differ, you will need to manually select the correct element for mapping <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
*   Sorting, searching, and filtration options are available for properties <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
*   Once mapping is complete, click "Create PDF" to start the generation process <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

### 4. Preview and Download
*   After generation, you can click "Preview sample" to review one of the generated documents <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
*   Click "Download all" to download all the generated PDFs <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. Each row from your Notion database will result in a unique PDF document <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

> [!NOTE] Key Naming Convention Rule
> Always ensure your placeholder text elements in the Notion template are enclosed in curly braces (e.g., `{placeholder}`) and use the **exact same naming convention** as the column headers in your Notion database <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. If names differ, you will need to map them manually in the mapping section <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## Sidebar Navigation and Features

The [[using_pdfoutput_settings_and_subscription_options | PDFOutput]] interface includes a sidebar with several useful sections:

*   **Connections:** This section displays all previously created connections. You can load a predefined database and template by selecting an existing connection, eliminating the need to create a new one each time <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   **Templates:** This provides a list of predefined templates available for use <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
    *   For each template, a database link and a template link are provided <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
    *   To use a predefined template, click "Start with this template," which will prompt you to duplicate it onto your Notion workspace <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. Remember to duplicate both the database and the template file <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   [[options_for_upgrading_pdf_output_features_and_settings | **Upgrade Option**]]:
    *   The free plan includes a "made with [[using_pdfoutput_to_generate_pdf_documents_in_bulk | PDFOutput]]" watermark and has certain limitations <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
    *   To upgrade, click this option to manage your subscription and activate your plan <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. [[understanding_pdfoutput_subscription_plans | Current plan and renewal date]] information is available <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.
*   [[using_pdfoutput_settings_and_subscription_options | **Settings**]]:
    *   Allows you to choose different page formats for your PDFs <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
    *   Provides an option to add more templates and databases after the initial setup <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.
*   **Feedback:** Use this section to send messages and feedback directly to the developer for assistance <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Help:** This section provides access to the demonstration video for guidance <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.

The sidebar can also be closed to maximize screen space <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.