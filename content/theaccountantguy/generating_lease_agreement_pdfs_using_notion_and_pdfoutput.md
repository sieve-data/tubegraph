---
title: Generating lease agreement PDFs using Notion and PDFOutput
videoId: lCyhl8mofjE
---

From: [[theaccountantguy]] <br/> 

This guide outlines how to use [[using_pdf_output_tool_with_notion | PDFOutput]] to [[generating_pdf_documents_from_notion_using_pdfoutput | generate lease agreement documents]] in [[generating_pdf_documents_from_notion_using_pdfoutput | PDF]] format from a [[generating_pdf_documents_from_notion_using_pdfoutput | Notion database]] and a [[creating_pdf_documents_with_notion_templates | Notion page]] template. <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>

## Key Components

### Lease Agreement Template in Notion
A [[creating_pdf_documents_with_notion_templates | lease agreement template]] is set up in [[generating_pdf_documents_from_notion_using_pdfoutput | Notion]] with all necessary details such as landlord name, tenant name, and street address. <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a> Important fields within this template are formatted as placeholder text elements, enclosed in curly braces (e.g., `{landlord name}`, `{tenant name}`, `{street address}`). <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a> These placeholders will be dynamically replaced with data. <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>

### Notion Database
A [[generating_pdf_documents_from_notion_using_pdfoutput | Notion database]] contains the specific data for each lease agreement, including columns for landlord name, tenant name, and street address. <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a> Each row in this database represents a unique lease agreement. <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>

## Setting Up [[using_pdf_output_tool_with_notion | PDFOutput]]

1.  **Login to [[using_pdf_output_tool_with_notion | PDFOutput]]:** Access the [[using_pdf_output_tool_with_notion | PDFOutput]] platform. <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
2.  **Initial Setup:** Navigate to the help section within [[using_pdf_output_tool_with_notion | PDFOutput]] to follow instructions on setting up the tool, including configuring API keys. <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a> This step is crucial before [[generating_pdf_documents_from_notion_using_pdfoutput | generating the PDF documents]]. <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>
3.  **Specify Connection Details:**
    *   Assign a connection name (e.g., "lease agreement"). <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>
    *   Select the relevant [[generating_pdf_documents_from_notion_using_pdfoutput | Notion database]] (e.g., "lease") from the dropdown menu, which displays all databases connected via the API key. <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>
    *   Choose the [[creating_pdf_documents_with_notion_templates | lease template]] from the template set. <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
4.  **Map Properties:** Click "Next" to allow [[using_pdf_output_tool_with_notion | PDFOutput]] to load and automatically map the database properties to the template elements. <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>
    *   The left side displays [[generating_pdf_documents_from_notion_using_pdfoutput | Notion]] properties from the database (e.g., "landlord name," "tenant name," "street address"). <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>
    *   [[using_pdf_output_tool_with_notion | PDFOutput]] automatically maps these to corresponding [[generating_pdf_documents_from_notion_using_pdfoutput | PDF]] elements in the template if their names match. <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>
    *   If a property is not mapped, it will appear in gray. Clicking on it reveals unmapped properties in red, allowing manual mapping. <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>

## Generating [[exporting_pdf_documents_from_notion | PDF Documents]]

1.  **Export:** After ensuring all fields are correctly mapped, click "Export." <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>
2.  **[[generating_pdf_documents_from_notion_using_pdfoutput | PDF Status]] Property:** Upon clicking "Export," a "[[generating_pdf_documents_from_notion_using_pdfoutput | PDF status]]" property will appear in your [[generating_pdf_documents_from_notion_using_pdfoutput | Notion database]]. <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>
    *   This column indicates which rows need [[generating_pdf_documents_from_notion_using_pdfoutput | PDF]] generation (unticked rows). <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>
    *   As [[using_pdf_output_tool_with_notion | PDFOutput]] processes each row, it automatically places a tick mark in this column, signifying that the [[generating_pdf_documents_from_notion_using_pdfoutput | PDF]] for that row has been generated. <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>
3.  **Preview and Download:**
    *   Once all [[exporting_pdf_documents_from_notion | PDFs]] are generated, a "preview sample" option becomes available, allowing you to view a single generated [[generating_pdf_documents_from_notion_using_pdfoutput | PDF]] document. <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>
    *   The "download all" option enables you to [[generating_pdfs_in_bulk_with_notion | download all generated PDFs]] in a single archive. <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>

## Customization Tips
To ensure smooth automatic mapping, it is essential that the naming conventions of properties in your [[generating_pdf_documents_from_notion_using_pdfoutput | Notion database]] exactly match the placeholder text elements in your [[creating_pdf_documents_with_notion_templates | Notion template]]. <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>

## Support
For further assistance, you can reach out via email at `notionformyuse@gmail.com`. <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>