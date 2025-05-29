---
title: Customizing templates and databases in Notion
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

This article demonstrates how to leverage Notion pages and [[creating_and_using_templates_in_notion | Notion templates]] alongside databases to [[customizing_pdf_templates_in_notion | generate PDF documents]] using PDFoutput.com. The primary example used is an invoice template. <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>

## Getting Started with PDFoutput.com

To begin, users need to log in to PDFoutput.com. <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a> Upon logging in, an interface will appear, from which users should proceed to the "template section" <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a> to view a list of [[creating_and_managing_templates_in_notion | available templates]]. <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a> The video specifically uses the invoice template for demonstration. <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a> Users can utilize search, sorting, or filter options to find specific templates. <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>

## Understanding Notion Templates and Databases

Once a template, such as the invoice template, is selected for download, it opens a new page displaying both the template and its associated database. <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>

### Notion Template Structure

The template contains placeholder text elements, such as "client name," "client company address," "invoice number," "date," "terms," and "due date." <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a> These placeholders are enclosed in curly braces, indicating they will be replaced with data from a connected database. <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>

### Notion Database Structure

Correspondingly, the Notion database features columns with the exact same names as the placeholder elements in the template (e.g., "invoice number," "date," "client name," "client company," "client address"). <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a> Each row in the database will provide the specific data to populate a corresponding PDF invoice. <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>

## Connecting Notion with PDFoutput.com

1.  **Duplicate the Template**: Click "start with this template" on PDFoutput.com. <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a> This action prompts the user to duplicate the template into their personal Notion workspace. <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>
2.  **Add Template to PDFoutput.com Settings**:
    *   Navigate to the "settings" section within PDFoutput.com. <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>
    *   Select the specific Notion workspace where the template was duplicated. <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>
    *   Choose the duplicated template (e.g., "invoice generator template") and grant access. <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a> PDFoutput.com will then authenticate and add the template to its setup. <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>

## Customizing Templates and Databases

Both the [[customizing_templates_in_notion | Notion template]] and the [[creating_and_managing_databases in_notion | Notion database]] are entirely [[customizing_and_using_notion_templates | customizable]] to fit specific requirements. <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>

**Crucial Rule for Integration**:
When [[customizing_templates_in_notion | modifying the template]] or [[creating_databases_in_notion | the database]], ensure that all placeholder text elements within curly braces in the template have **exact matching names** in the corresponding columns of the database. <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a> <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a> This ensures seamless data mapping and correct PDF generation. <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>

## Mapping Database Properties for PDF Generation

After selecting the database and template within PDFoutput.com, the system automatically begins syncing elements. <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a> Notion properties (database column names) are listed on the left and are automatically mapped to the corresponding template elements (placeholder text in curly braces). <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a> <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a> Mapped elements are indicated by a green bar. <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a> If any properties are not automatically mapped, they can be manually searched for and mapped. <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>

## Generating PDF Documents

Once all elements are correctly mapped, click "export." <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a> As documents are generated, a "PDF status" column in the Notion database will automatically update (check) to indicate completion for each row. <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a> <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>

PDFoutput.com allows users to:
*   **Preview Samples**: See a sample of the generated PDF. <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>
*   **Download All**: Download all generated PDF outputs. <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a> Each row in the database will result in a separate PDF document. <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>

### Important Tip for Regeneration
To ensure a row is processed for PDF generation, its "PDF status" column in the Notion database must be unchecked/unticked. If a row is already ticked, it will be ignored during generation. <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>

## Additional Features and Support

*   **Other Templates**: Users can access and [[creating_and_managing_templates in_notion | utilize other templates]] available on PDFoutput.com. <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>
*   **Paid Plans**: A paid plan is required to remove watermarks from generated PDFs. <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>
*   **Feedback Option**: Users can provide feedback directly. <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>
*   **Saved Connections**: After generating output, the connection details (database and template) are saved, allowing for quick reloading without re-mapping. <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>
*   **Help Section**: A help section provides a full demonstration of the setup process. <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>

For further assistance, users can contact notionforuse@gmail.com. <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>