---
title: Using templates to generate PDF invoices
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

This guide demonstrates how to [[using_templates_in_notion_for_pdf_generation | use Notion pages and templates]] to [[generating_pdf_invoices_using_pdf_output_service | generate PDF invoices]] using the PDF Output service <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This process involves leveraging an invoice template from the PDF Output library and connecting it to a Notion database <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Getting Started with PDF Output

To begin, you need to log in to PDF output.com <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Once logged in, you will see an interface that allows you to manage documents <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Selecting and Understanding the Invoice Template

1.  **Access Templates**: Navigate to the "Template" section within PDF Output <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. This section displays a list of templates compatible with PDF Output <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
2.  **Download Invoice Template**: For invoices, locate the "invoices template" and click its download link <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. You can use search, sort, or filter options to find specific templates <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
3.  **Template and Database Overview**: Clicking the download link opens a new page showing both the template and its associated database <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
    *   The template includes elements like client name, company address, invoice number, date, terms, and due date <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
    *   These elements are placeholder texts, enclosed in curly braces, which will be replaced by data from the connected database <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
    *   The database contains corresponding columns for each placeholder, such as invoice number, date, client name, and client company <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Data from each row in the database will populate the template <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## Duplicating the Template to Notion

1.  **Start with Template**: On the PDF Output page displaying the template, click the "Start with this template" option <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
2.  **Duplicate to Notion Workspace**: This action prompts you to duplicate the template into your personal Notion workspace <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Select your desired workspace from the dropdown menu and click "Add to private" <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
3.  **Verify Duplication**: The template, including its database, will now appear in your Notion workspace <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

## Connecting Your Notion Template to PDF Output

1.  **PDF Output Settings**: Return to the PDF Output website and click on "Settings" <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
2.  **Add Template**: Select the option to "add the template" <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
3.  **Select Workspace and Template**: Choose the Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. Then, from the list of available pages in your workspace, select the "invoice generator template" and click "Allow access" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
4.  **Authentication**: PDF Output will authenticate and add the template to your setup <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. A brief syncing process will occur <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

## Customizing Invoice Templates and Databases

The template is fully customizable; you can add, delete, or modify its content <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **Placeholder Naming**: Ensure that all placeholder text elements in the template are enclosed in curly braces <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   **Matching Column Names**: The names of these placeholders must exactly match the column names in your Notion database <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. For example, if the template has `{Invoice Number}`, the database column must also be named "Invoice Number" <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. This ensures correct data mapping during PDF generation <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. This flexibility allows for [[customizing_invoice_templates_using_placeholders | customizing invoice templates using placeholders]].

## Generating PDF Invoices

1.  **Select Database and Template**: In PDF Output, select the correct Notion database and the "professional invoice template" <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. Give your generation a name, e.g., "invoice" <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
2.  **Mapping Properties**: Click "Next" <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. The system will sync and display all Notion properties (database columns) on the left, automatically mapped to their corresponding template elements (placeholders) <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
    *   Mapped elements are shown in green <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
    *   If any property is unmapped, it will be indicated, and you can manually search and map it <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
    *   Sorting, searching, and filtering options are available to manage properties <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
3.  **Exporting**: Once mapping is complete, click "Export" <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
    *   In your Notion database, a "PDF Status" column will be added. As each document is generated, the corresponding row's status will be ticked <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
    *   This demonstrates [[automating_pdf_generation_with_userdefined_templates | automating PDF generation with user-defined templates]].

## Verifying and Downloading Outputs

1.  **Preview Sample**: After successful export, you can click "Preview sample" to view one of the generated invoices <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. Verify details like invoice number, date, and client name against your database <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. This effectively shows how to [[using_a_template_for_invoice_payment_summary | use a template for invoice payment summary]].
2.  **Download All**: Click "Download all" to download all generated PDF invoices <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

### Important Notes for Generation

*   **PDF Status Column**: Before generating output, ensure the "PDF Status" column in your Notion database is unticked for the rows you want to process <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. Ticked rows will be ignored <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

## Additional Features and Support

*   **Other Templates**: You can explore and use other templates available in the PDF Output service for different document types <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
*   **Watermarks**: Free plans may include watermarks on generated PDFs. Upgrading to a paid plan removes these watermarks <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. This is relevant to [[using_pdf_output_software_for_invoice_creation | Using PDF Output software for invoice creation]].
*   **Saved Connections**: After generating output, the connection details (database and template mapping) are saved <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. You can access these connections to reload the same setup without re-mapping <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.
*   **Help Section**: The "Help" section provides a detailed guide on setting up the service for the first time <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **Feedback**: For questions or feedback, you can contact notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.

This process highlights the capability to [[using_a_template_to_generate_pdf_documents_in_notion | use a template to generate PDF documents in Notion]] and showcases [[using_notion_templates_for_pdf_generation | using Notion templates for PDF generation]].