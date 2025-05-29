---
title: Using PDF output templates in Notion
videoId: zrr8DW4PWz0
---

From: [[theaccountantguy]] <br/> 

This article explains how to generate PDF documents, such as payment receipts, using a Notion database and a Notion template with the help of [[using_pdf_output_tool_with_notion | PDFOutput]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Getting Started with PDFOutput

To begin, you need to log in to PDFoutput.com <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. After logging in, you will see an interface with various options <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

### Accessing Templates

To find available templates, click on the "Templates" option within [[using_pdf_output_tool_with_notion | PDFOutput]] <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This will open a new page displaying all the templates available for [[using_pdf_output_tool_with_notion | PDFOutput]] <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

You can search for specific documents using the search option <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. There are also filter and sorting options available <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. For generating payment receipts, select the "payment receipts PDF generator" template <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a> and click its download link <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. This opens a new page showing the payment receipts PDF generator template and its associated database <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Understanding Notion Templates and Databases for PDF Generation

When using a Notion template for PDF generation, such as the payment receipt template, it includes predefined elements <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. Some elements, like `receipt number`, `receipt date`, `customer name`, and `customer email`, are enclosed in curly braces (e.g., `{customer name}`) <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. These are placeholder text elements that will be replaced by corresponding data from your Notion database <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

For example, the `customer name` placeholder in the template will be replaced by the data from the "customer name" column in your database <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. It is crucial that the exact naming of these placeholder elements in the template matches the corresponding column names in your database <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### Duplicating the Template to Notion

If the template is not yet published to the Notion Gallery, you will see a "start with this template" option <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. Otherwise, click on the "duplicate" option <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. You will be prompted to choose which Notion workspace to duplicate the template to <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. The template must be duplicated to a Notion workspace to be used with [[using_pdf_output_tool_with_notion | PDFOutput]] <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### Customizing the Notion Template

The entire template is customizable to your specific requirements <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. You can format elements (e.g., bold text) and adjust spacing as needed <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. However, ensure that any placeholder elements intended to be replaced from your database are kept within curly braces for proper syncing and PDF output generation <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. The exact naming convention of these placeholders must match the database column names <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

## Integrating Notion with PDFOutput

After duplicating the template to your Notion workspace, navigate to the settings section in [[using_pdf_output_tool_with_notion | PDFOutput]] <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

1.  Click "click here to add templates" <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
2.  Choose the specific Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
3.  Select the relevant pages, such as the "payment receipts PDF generator" file <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
4.  Click "Allow access" <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. [[using_pdf_output_tool_with_notion | PDFOutput]] will then read the template and database elements from Notion <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

Once authentication is successful, you will be redirected back to [[using_pdf_output_tool_with_notion | PDFOutput]] <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

### Mapping Database Properties to Template Elements

In [[using_pdf_output_tool_with_notion | PDFOutput]], select your Notion database (e.g., "payment receipts database") from the dropdown menu <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>, and then select the corresponding Notion template (e.g., "payment receipt template") <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. Give your export a name, like "payment receipt" <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

[[using_pdf_output_tool_with_notion | PDFOutput]] will automatically map Notion database properties (columns) to the template elements if the naming conventions match <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. If any elements are mismatched or unmapped, you can manually search for and select the correct mapping <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

## Exporting PDF Documents from Notion

After mapping is complete, click "Export" <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. [[using_pdf_output_tool_with_notion | PDFOutput]] will automatically add a "PDF status" column to your Notion database <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. As each row's PDF is generated, its status will be ticked in this column <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

Once the export is successful, you can preview a sample PDF <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a> or download all generated files <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>. Each generated PDF file corresponds to a specific row in your Notion database <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

## Additional Features of PDFOutput

*   **Connections:** The "Connections" section in [[using_pdf_output_tool_with_notion | PDFOutput]] displays all your past connections <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. Clicking on a connection will automatically load the associated database and template, allowing for quick regeneration <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   **Templates:** You can select multiple templates in the templates section <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   **Pricing Plans:** The free plan includes a [[using_pdf_output_tool_with_notion | PDFOutput]] watermark on generated PDFs <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. Upgrading to a paid plan removes this watermark <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
*   **Settings:** You can change the page format of the PDFs in the settings <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   **Feedback:** A feedback option is available to send messages directly to the support team <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   **Help Section:** The help section provides a demonstration video to guide you through the setup process <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

For any questions, you can reach out via email to notion for my use@gmail.com <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.