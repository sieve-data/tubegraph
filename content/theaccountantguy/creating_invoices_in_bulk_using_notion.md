---
title: Creating invoices in bulk using Notion
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

This guide demonstrates how to [[generating_pdf_documents_in_bulk_using_notion_and_pdf_output | generate PDF documents in bulk]] using a Notion page and template, specifically focusing on [[generating_professional_invoices_using_notion | creating professional invoice templates in Notion]] and [[generating_pdf_invoices_from_notion_database | generating PDF invoices from a Notion database]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The process utilizes PDF Output.com <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## Getting Started with PDF Output

1.  **Log in to PDF Output.com**: Navigate to PDF Output.com and log in to access the interface <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
2.  **Access Templates**: Proceed to the "Template" section <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Here, you'll find a list of pre-created templates compatible with PDF Output <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
    *   For this demonstration, the "Invoices" template is used <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
    *   You can use search, sort, or filter options to find specific templates <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
3.  **Download the Template**: Click the download link next to the "Invoices" template to open a new page displaying both the template and its associated database <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

## Understanding the Notion Template and Database

The template contains placeholder text elements, such as client name, company address, invoice number, date, and terms, which are enclosed in curly braces (e.g., `{client name}`) <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. These placeholders will be automatically replaced with data from the connected Notion database <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

The Notion database contains columns with the exact same elements (e.g., "Invoice Number," "Date," "Client Name," "Client Company," "Client Address") <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Each row in the database corresponds to a specific invoice, and its data will populate the corresponding placeholders in the template <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## Setting Up the Template in Notion

1.  **Duplicate the Template**: On the template page, click "Start with this template" to duplicate it to your own Notion workspace <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. Select your desired workspace and click "Add to private" <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
2.  **Connect to PDF Output**:
    *   Go back to PDF Output.com and navigate to "Settings" <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
    *   Click "Add Template" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
    *   Select the Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
    *   Click "Select Pages" and choose the "Invoice Generator Template" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   Click "Allow access" to authenticate and add the template to your PDF Output setup <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## Customizing and Mapping Data

### Customizing the Notion Template and Database

*   The Notion template is fully customizable: you can add, delete, or modify elements <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **Crucial Rule**: Ensure that all placeholder text elements in the template (inside curly braces) have the exact same naming convention as their corresponding columns in the Notion database <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. For example, if the template has `{Invoice Number}`, the database column must also be "Invoice Number" <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

### Mapping Properties in PDF Output

1.  **Select Database and Template**: In PDF Output, ensure the correct database and the "Professional Invoice Template" are selected <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
2.  **Sync Elements**: Click "Next." PDF Output will sync the database elements and the template <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
3.  **Verify Mapping**:
    *   Notion properties (database columns) are listed on the left <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
    *   The system automatically maps these to corresponding template elements (indicated by green bars) <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
    *   If any property is not mapped, it will be highlighted, and you can manually search and map it <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.

## Generating and Downloading PDFs

1.  **Export**: Once all elements are correctly mapped, click "Export" <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
2.  **Monitor Status**: In your Notion database, a "PDF Status" column will appear. As each document is generated, its corresponding row will be checked <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
    *   **Important**: Before regenerating documents, ensure the "PDF Status" checkbox for the desired rows in Notion is unticked; otherwise, those rows will be ignored <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
3.  **Preview Sample**: After successful export, you can click "Preview Sample" to view a generated invoice <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
4.  **Download All**: Click "Download All" to download all generated PDF invoices <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

## Additional Features and Tips

*   **Connections**: Once you've generated an output, the connection (database and template mapping) is saved under the "Connections" section <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. This allows you to quickly load the same setup without re-mapping <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.
*   **Watermark**: On the free plan, generated PDFs will include a "PDF Output" watermark. To remove this, you need to upgrade to a paid plan <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
*   **Help Section**: The "Help" section provides a detailed demonstration of the initial setup process <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **Feedback**: For questions or feedback, you can reach out to notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.