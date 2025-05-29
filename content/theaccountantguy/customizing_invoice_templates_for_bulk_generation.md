---
title: Customizing invoice templates for bulk generation
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

This article demonstrates how to generate PDF documents, specifically invoices, in bulk using a Notion page and template with PDF Output.

## Getting Started with PDF Output <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>

To begin, log in to PDFoutput.com <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. The interface displays various options for document creation <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

### Accessing Templates <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>

Navigate to the "Templates" section <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Here, you'll find a list of pre-created templates compatible with PDF Output <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. For this demonstration, the "Invoices" template is used and can be downloaded via its dedicated link <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. A search, sort, or filter option is available to find specific templates <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## Understanding the Notion Template and Database <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>

Downloading the template opens a new page displaying both the template and its corresponding database <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### Template Structure <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>

The invoice template includes elements like client name, company, address, invoice number, date, and terms <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. These are designed as [[customizing_invoice_elements_using_placeholders | placeholder text elements]], enclosed in curly braces `{{ }}` <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>, <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

### Database Connection <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>

These [[customizing_templates_and_databases_for_document_generation | placeholder elements]] in the template are designed to be replaced by data from a connected Notion database <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. The database contains columns with the same names as the placeholders, such as invoice number, date, client name, and client company <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Each row in the database will correspond to a unique invoice PDF <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## Duplicating and Connecting the Template <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>

1.  **Duplicate the Template**: Click "Start with this template" on PDF Output, which prompts you to duplicate the template to your Notion workspace <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>, <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Select your Notion workspace and click "Add to private" <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>, <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. The template and its associated database will then appear in your Notion <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
2.  **Add Template to PDF Output**: Go back to PDF Output and click "Settings" <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. Select the specific template that was duplicated from your Notion workspace <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Ensure you choose the correct workspace where the template was duplicated <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
3.  **Allow Access**: Click "Select pages" and then choose the "Invoice Generator template" from your workspace <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>, <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. Click "Allow access" to authenticate the template with PDF Output <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. The template will be added to your PDF Output setup <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

## Customizing Templates and Databases <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>

Both the template and the database are fully customizable <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. You can add, delete, or modify elements in the template <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

*   **Template Customization**: When modifying the template, ensure that all [[customizing_invoice_elements_using_placeholders | placeholder text elements]] remain inside curly braces `{{ }}` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   **Database Customization**: The corresponding elements in the Notion database columns must have the exact same naming convention as the placeholders in the template <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>, <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. For example, if the template has `{{invoice number}}`, the database column must also be named "invoice number" <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. This ensures accurate data mapping for output generation <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

## Mapping Properties for Generation <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>

After selecting the database and the [[professional_invoice_template_customization | professional invoice template]], click "Next" <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. PDF Output will sync the database and template elements <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

*   **Notion Properties List**: All Notion properties (database columns) are listed on the left <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. These are automatically mapped to their corresponding elements in the template <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Mapped elements are indicated by a green bar <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
*   **Manual Mapping (if needed)**: If an element is not automatically mapped, you can click on it and search for the correct property to map it manually <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>. Sorting, searching, and filtering options are available to manage properties <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

## Bulk PDF Generation <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>

Once all properties are mapped, click "Export" <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

### Tracking Progress in Notion <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>

As documents are generated, a "PDF Status" column in your Notion database will automatically update, getting checked for each row processed <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>, <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

### Viewing and Downloading Outputs <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>

After a successful export <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>:

*   **Preview Sample**: You can preview a sample of the generated PDF <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   **Download All**: Click "Download All" to download all the generated PDF invoices as a batch <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>, <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. Each row from the database will produce a separate PDF <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

### Important Note for Regeneration <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>

Before regenerating documents, ensure that the "PDF Status" column in your Notion database for the desired rows is *unticked* <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. If a row is ticked, it will be ignored during the generation process <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

## Additional Features <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>

*   **Other Templates**: You can explore other template options for different document types <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
*   **Pricing**: A free plan includes a PDF Output watermark <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. To remove the watermark, upgrade to a paid plan <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   **Feedback**: A feedback option is available to send messages or suggestions <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
*   **Re-using Connections**: Once a connection is set up and files are exported, it is saved under the "Connections" section <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. This allows you to quickly load the same database and template without re-mapping for future generations <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.
*   **Help Section**: The help section provides a detailed demonstration on initial setup <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.