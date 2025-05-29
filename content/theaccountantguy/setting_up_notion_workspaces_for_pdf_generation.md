---
title: Setting Up Notion Workspaces for PDF Generation
videoId: zrr8DW4PWz0
---

From: [[theaccountantguy]] <br/> 

To generate PDF documents, such as payment receipts, using a [[using_pdf_output_with_notion_templates | Notion database]] with a Notion template via PDF Output, certain setup steps within your Notion workspace are required <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Duplicating a Template to Notion <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>

The initial step involves duplicating a chosen template into your Notion workspace <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>:

1.  **Access Templates**: Log in to PDFoutput.com <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a> and click on "Templates" <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This will display a list of available templates <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
2.  **Select Template**: Search for or locate the desired template, for example, the "Payment Receipts PDF Generator" <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
3.  **Download/Open**: Click on the "download link" next to the chosen PDF file <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. This opens a new page showcasing the associated database and template <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
4.  **Duplicate to Workspace**:
    *   If the template is not yet published to the Notion Gallery, you will see a "duplicate" option <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
    *   If it is published, click "start with this template" <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
    *   In both cases, you will be prompted to select the Notion workspace where you want to duplicate the template <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
5.  **Confirmation**: Once selected, the template will be added to your chosen Notion workspace <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

## Configuring the Notion Template and Database <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>

For successful PDF generation, the Notion template and its corresponding database must be correctly configured <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>:

*   **Placeholder Elements**: In the Notion template, elements that will be replaced by data from your database must be enclosed in curly braces, e.g., `{receipt number}`, `{receipt date}`, `{customer name}` <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **Exact Matching**: These placeholder texts must **exactly match** the corresponding column names in your Notion database <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. For example, if the template has `{customer name}`, your database must have a column named "customer name" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This precise naming convention ensures proper syncing and output without errors <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Customization**: You can customize the template's appearance within Notion, such as making elements bold or adding spacing, but ensure placeholders remain in curly braces <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

## Connecting Notion to PDF Output <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>

After setting up the template in Notion, you need to connect your Notion workspace to PDF Output:

1.  **Go to Settings**: In PDF Output, navigate to the "Settings" section <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
2.  **Add Templates**: Click on "click here to add templates" <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
3.  **Select Workspace**: Choose the **same Notion workspace** where you duplicated your template <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. If you have multiple workspaces, use the dropdown to select the correct one <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
4.  **Select Pages**: Click "select pages" to allow PDF Output to access the specific Notion template and database pages <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
5.  **Allow Access**: Click "allow access" <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. The system will then read your template and database elements <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. Authentication success means PDF Output can now access your Notion data <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

## Mapping Database Properties to Template Elements <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>

Once connected, PDF Output will map the data:

1.  **Select Database and Template**: On the PDF Output screen, select your [[setting_up_notion_database_for_pdf_document_templates | Notion database]] and the corresponding Notion template from the dropdown menus <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
2.  **Automatic Mapping**: If your template placeholders exactly match your database column names, PDF Output will automatically map the "Notion properties" (database columns) to the "template elements" <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
3.  **Manual Correction**: If anything is mismatched, it will be indicated, allowing you to manually search for and select the correct corresponding element <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

With these steps complete, your Notion workspace is set up to [[generating_pdfs_from_notion_using_pdfoutput | generate PDF documents]] using PDF Output <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.