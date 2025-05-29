---
title: Creating and using templates in Notion
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

This article outlines how to [[creating_and_using_notion_templates_for_pdfs | create and use Notion templates]] in conjunction with PDFout.com to generate PDF documents from a Notion database <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The demonstration focuses on generating PDF invoices using a Notion invoice template <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Accessing and Downloading Templates

To begin, navigate to PDFout.com <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. After logging in, you will access the template section <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. This section displays a list of pre-created templates compatible with PDFout.com <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

For this demonstration, the [[creating_professional_invoice_templates_in_notion | invoice template]] is downloaded by clicking its download link <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. You can use search, sorting, or filter options to find specific templates <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## Understanding Template and Database Structure

Upon downloading, a new page opens, displaying both the template and its associated database <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

The [[creating_and_managing_templates_in_notion | Notion template]] contains placeholder text elements, such as `client name`, `client company address`, `invoice number`, `date`, and `terms`, enclosed in curly braces <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. These placeholders will be replaced with data from the connected database <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

The corresponding database lists these same elements as columns (e.g., `invoice number`, `date`, `client name`, `client company`, `client address`) <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Each row in the database provides data for a specific invoice, which will populate the placeholders in the template <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### Customizing Templates and Databases

Both the template and the database are fully [[customizing_templates_in_notion | customizable]] <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. You can add, delete, or modify content in the template <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. It is crucial that the placeholder text within curly braces in the template exactly matches the column names in the database <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. For example, `invoice number` in the template must correspond to an `invoice number` column in the database <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. This ensures correct data mapping during PDF generation <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

## Setting Up in Notion and PDFout.com

### Duplicating the Template to Notion

1.  Click the "Start with this template" option on PDFout.com <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
2.  Duplicate the template to your Notion workspace <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Select your desired workspace from the dropdown menu and click "Add to private" <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
3.  The template and its associated database will now appear in your Notion workspace <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

### Adding the Template to PDFout.com Settings

1.  Return to PDFout.com and navigate to the "Settings" section <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
2.  Select the option to "Add template" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
3.  Choose the same Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
4.  Click "Select pages" and then select the specific template (e.g., "invoice generator template") <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
5.  Click "Allow access" to authenticate the template and add it to your PDFout.com setup <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. PDFout.com will then sync all database and template elements <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

## Generating PDFs

1.  On the PDFout.com screen, select your Notion database and the specific [[using_predefined_templates_in_notion_for_pdf_generation | Notion template]] you wish to use <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
2.  Give the generation a name (e.g., "invoice") <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
3.  Click "Next" to begin syncing the database and template elements <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
4.  The system will display a mapping of Notion properties (database column names) to the template's placeholder elements <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. Correctly mapped elements will show in green <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. If any are unmapped, you can manually map them <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
5.  Once mapping is complete, click "Export" <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
6.  In your Notion database, a "PDF Status" column will be present; it will automatically tick as each document is generated <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

## Viewing and Downloading Output

After successful export, you can:
*   **Preview Sample**: Click "Preview sample" to view a single generated PDF (e.g., the first invoice) <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   **Download All**: Click "Download all" to download all generated PDF documents <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. Each row from the database will generate a separate PDF <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

### Important Notes

*   For new PDF generations, ensure the "PDF Status" row in your Notion database is unticked <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. Ticked rows will be ignored <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   On a free plan, generated PDFs will include a "PDFout.com" watermark <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. Upgrade to a paid plan to remove it <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   The "Connections" section saves your previous database and template mappings, allowing you to quickly reload them without remapping <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

## Help and Support

The "Help" section on PDFout.com provides a demonstration of the setup process <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. For further questions or feedback, you can reach out via email at notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.