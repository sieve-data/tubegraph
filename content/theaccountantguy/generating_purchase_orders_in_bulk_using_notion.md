---
title: Generating purchase orders in bulk using Notion
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 

This article explains how to [[generating_purchase_order_pdfs | generate purchase order PDFs]] in bulk using a Notion page and a Notion database, facilitated by the PDF output platform <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## The Purchase Order Template

The process utilizes a specific purchase order template <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This template includes fields such as purchase order number, date, supplier, buyer name, and other relevant details <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Key items within the template that are meant to be replaced by data from a database are enclosed in curly braces, for example, `{purchase order number}` <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## The Notion Database

A Notion database is used to store the information for each purchase order <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This database contains columns corresponding to the fields in the template, such as purchase order number, date, supplier name, and buyer name <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. The naming convention for columns in the database should exactly match the names inside the curly braces in the template for automatic mapping <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Each row in the database represents a unique purchase order for which a PDF document will be generated <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Bulk PDF Generation with PDF output

To [[generating_pdfs_in_bulk_with_notion | generate PDFs in bulk]] from your Notion database and template, follow these steps using PDF output.com:

1.  **Log In**: Access PDF output.com <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
2.  **Locate Template and Database**:
    *   Navigate to the "Template" section in the sidebar <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
    *   Search for "purchase order" to find the predefined "purchase order PDF generator" <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
    *   Click on both the "database link" and "template link" provided <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
3.  **Duplicate to Notion Workspace**:
    *   Click "Start with this template" to duplicate the database and template onto your Notion workspace <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
    *   Select your Notion workspace and click "Add to private" <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
    *   Repeat this duplication process for both the database and the template <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
4.  **Connect Notion to PDF output**:
    *   Return to PDF output and click "Click here to add database" or "Click here to add template" <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
    *   Select your Notion workspace and choose the duplicated database and template from the list <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
    *   Click "Allow access" to connect <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   Once connected, the database and template will appear in the PDF output interface <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. If not, click "refresh" <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
5.  **Define Output Name and Map Fields**:
    *   Give a name to the generated PDF documents (e.g., "purchase order") and click "next" <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
    *   The platform will load database elements and template elements (those within curly braces) <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
    *   If database properties and template fields have the exact same naming convention, they will automatically map <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. Otherwise, you can manually map them by clicking on the gray fields and selecting the correct element <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
6.  **Create and Download PDFs**:
    *   Click "Create PDF" <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
    *   PDF output will process documents for each row in your database <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
    *   After successful export, you can "preview sample" of a generated PDF <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
    *   Click "Download all" to get all generated purchase order PDFs <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

### Template Customization and Best Practices

The duplicated template is fully customizable; you can edit or modify it as needed <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. Ensure that any dynamic content meant to be replaced by database values remains inside curly braces <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. Maintain consistent naming conventions between the template and the database columns for automatic field mapping <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. If using relation properties in your Notion database, grant PDF output access to those related databases during the connection process <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

### Additional PDF output Features

*   **Connections**: The "Connections" tab lists previously created connections, allowing you to quickly reload your database and template for subsequent bulk exports without re-entering details <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
*   **Upgrade**: Free plans include a "Made with PDF output" watermark on generated documents <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. Upgrading to a paid subscription removes the watermark and any limits on PDF generation <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   **Settings**: Default page format is A4 <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. You can also add more databases and templates via the settings <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Feedback**: A feedback option is available to report issues or provide suggestions <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Help**: The help section includes a video demonstrating how to use a custom template from scratch, if you prefer not to use the predefined ones <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

For further assistance, you can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.