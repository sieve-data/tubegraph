---
title: Creating and using an invoice template in Notion
videoId: XPSQBVl9mKs
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to help users [[creating_invoices_in_bulk_using_notion | generate PDF documents in bulk]] from a Notion database using a Notion template <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This guide focuses on [[creating_and_using_templates_for_pdf_generation_in_notion | creating and using an invoice template in Notion]] to produce professional PDF invoices.

## Understanding the Invoice Template

The invoice template used with PDF Output features various placeholders, enclosed in curly braces, such as invoice number, date, due date, and terms <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. These placeholders are designed to be automatically replaced with corresponding data from a Notion database <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Each row in the Notion database provides the information to populate these elements for a distinct PDF invoice <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

### [[customizing_notion_invoice_templates | Customizing Notion Invoice Templates]]

Users can [[customizing_notion_invoice_templates | customize]] the invoice template by adding, deleting, or modifying elements <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. It is crucial to ensure that any elements added within curly braces in the template have corresponding columns with matching names in the Notion database <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

## Getting Started with PDF Output

1.  **Access PDF Output**: Navigate to PDFoutput.com <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
2.  **Find Templates**: Once logged in, select the "Templates" section on the right side of the interface <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Here, you can browse available templates, using search, sorting, or filtration options to find specific templates like an invoice template <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
3.  **Download Template**: Click the "Download" link next to the desired invoice template <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. This will open a new tab displaying both the database and template elements <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
4.  **Duplicate to Notion**: To [[creating_and_using_notion_templates_for_pdfs | use the template]], duplicate it to your personal Notion workspace by clicking "Start with this template" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Select your Notion account and workspace, then click "Add to Private" <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

## Connecting Notion to PDF Output

1.  **Go to Settings**: After duplicating the template, return to PDF Output.com and go to the "Settings" section <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
2.  **Add Templates**: Click "click here to add templates" <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. This will redirect you to your Notion workspace <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
3.  **Select Pages**: Choose the Notion account where you duplicated the template <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. Then, click "Select Pages" and choose the specific invoice generator page (or the relevant Notion page that contains both the database and the template) <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. Click "Allow Access" to authenticate <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

## Mapping Data for PDF Generation

After successful authentication, PDF Output will allow you to fetch your Notion database and template <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

1.  **Select Database and Template**: From the dropdowns in PDF Output, select your "Professional Invoice Database" and the "Invoice Template" page <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
2.  **Name the Generation**: Provide a name for this generation, keeping in mind the 20-character limit <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. Click "Next" <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
3.  **Verify Mapping**: PDF Output will load all elements and display the mapping between Notion properties (from database columns) and template elements (placeholders in curly braces) <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
    *   **Matching Names**: Ensure that the names of the template elements exactly match the names of the columns in your Notion database <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
    *   **Manual Mapping**: If a mapping is not automatically detected (indicated by a gray color), you can manually click on the element and select the corresponding Notion property <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
    *   **Search, Sort, Filter**: Tools are available to search, sort, or filter elements to easily find unmapped properties <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. Green-colored elements indicate successful mapping <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

## [[using_a_template_to_generate_pdf_documents_in_notion | Generating PDF Documents]]

Before generating, check your Notion database:
*   **PDF Status Column**: A "PDF Status" column is added to your Notion database <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. For a row to be included in the PDF output, this column must be unchecked <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. The first time you use the integration, this column will be unchecked by default <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. Once a document is generated, it will automatically become checked <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   **Export**: Click "Export" in PDF Output to start processing the documents <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. As documents are generated, the "PDF Status" column in your Notion database will show a tick mark for each processed row <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
*   **Preview and Download**: After a successful export, you can "Preview Sample" to see one generated invoice (e.g., displaying client name, address, invoice number, and date as replaced from the database) <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>, or "Download All" to get all generated documents <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. The downloaded files will correspond to each row in your Notion database <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

## Re-using Connections

Once an export procedure is completed, the connection is saved in the "Connections" window within PDF Output <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
*   To [[using_templates_in_notion_for_pdf_generation | re-use the same database and template]], simply go to "Connections" and select your previously saved connection <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
*   It will automatically load all elements <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
*   Remember to untick the "PDF Status" checkbox in Notion for any specific rows you wish to regenerate <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

## Account and Settings

*   **Upgrade Options**: Information about your current plan (e.g., Enterprise plan), renewal date, and number of files downloaded is visible under "Upgrade" <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. You can upgrade your subscription and activate the new plan here <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
*   **Watermarks**: New users or those not on a paid plan will see a watermark in the PDF output, which is removed on paid plans <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.
*   **Page Format**: Under the "Settings" tab, you can select different page formats (e.g., A4, Letter) for your PDF documents <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
*   **Feedback**: For questions or issues, use the "Feedback" option to send a direct message <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
*   **Help**: The "Help" window provides access to tutorial videos, including this demonstration <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

For further assistance, you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.