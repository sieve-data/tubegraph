---
title: Customizing invoice templates
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

[[Customizing invoice templates|Customizing invoice templates]] involves utilizing a Notion page and template to generate PDF documents, such as invoices <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This process typically involves mapping data from a Notion database to placeholder elements within a Notion template, which are then used by PDF output to create the final PDF <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

## Accessing and Duplicating Invoice Templates

To begin, users need to log in to PDFoutput.com <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
1.  Navigate to the "Templates" section <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
2.  Locate the desired invoice template. Users can utilize search, sorting, or filter options to find specific templates <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
3.  Click the "Download" link next to the invoice template to open a page displaying both the template and its corresponding database <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
4.  Click "Start with this template" to duplicate it to your personal Notion workspace <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. Select your workspace from the dropdown and click "Add to private" <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

## Connecting the Notion Template to PDF Output

Once the template is duplicated in Notion:
1.  Return to PDFoutput.com and click on "Settings" <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
2.  Select the option to add the template <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
3.  Choose the same Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
4.  Click "Select pages" and then select the "Invoice Generator Template" from your workspace, granting access <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This authenticates and adds the template to your PDF output setup <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

## Customizing Invoice Elements

The template and its connected database are entirely [[customizing_invoice_elements_in_pdf_documents|customizable]]:
*   **Template Customization**: You can add, delete, or modify elements within the template <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. Key elements like client name, company address, invoice number, date, and terms are represented as placeholder text enclosed in curly braces (e.g., `{client_name}`) <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Database Customization**: The corresponding Notion database contains columns (e.g., "Invoice Number," "Date," "Client Name") that match these placeholder names <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
*   **Mapping**: When modifying the template, ensure that any placeholder text within curly braces exactly matches a corresponding column name in your Notion database <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. This ensures correct data population during PDF generation <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. PDF output automatically maps these properties, showing them in green <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. If an element is not mapped, it will be indicated, and you can manually search and map it <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.

### Generating PDF Invoices

Once the template and database are set up and mapped:
1.  In PDF Output, select the professional invoice template and the associated database <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
2.  Click "Next" to sync the elements <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
3.  Click "Export" to start the PDF generation process <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
4.  A "PDF Status" column in your Notion database will automatically update (get checked) as documents are generated <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
5.  After successful export, you can preview a sample or download all generated PDFs <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

> [!CAUTION]
> Before generating output, ensure the "PDF Status" column in your Notion database is unticked for the rows you wish to process. If a row is ticked, it will be ignored <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

### Additional Notes

*   **Watermarks**: If you are on a free plan, the generated PDF will include a watermark. To remove it, an upgrade to a paid plan is required <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
*   **Reusing Connections**: Once a connection is set up and an export performed, the system saves the values, allowing you to automatically load the same database and template without re-mapping for future generations <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Support**: For questions or feedback, users can reach out via email <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.