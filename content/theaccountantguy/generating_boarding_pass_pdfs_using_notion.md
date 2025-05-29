---
title: Generating boarding pass PDFs using Notion
videoId: alrxkhJzbuw
---

From: [[theaccountantguy]] <br/> 

This guide demonstrates how to generate boarding pass PDF documents using Notion as a database and template, in conjunction with PDFOutput <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. This process allows for [[generating_pdf_documents_from_a_notion_database | PDF document generation from a Notion database]] using a predefined template.

## Prerequisites

To generate boarding pass PDFs, you need two main components within Notion:
*   **Boarding Pass Database** A database containing all the necessary details for each boarding pass, serving as the data source <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.
*   **Boarding Pass Template** A pre-designed template that will be used to format the PDF documents <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. [[using_notion_as_a_template_and_database_for_pdfs | Notion is utilized as both the template and database]] for this process <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

## Process for Generating PDFs

The generation of boarding pass PDFs is facilitated by PDFOutput, which connects to your Notion database and template <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

1.  **Input Connection Details**
    *   In PDFOutput, type "boarding pass" into the connection details field <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
2.  **Connect the Database**
    *   Specify the [[using_boarding_pass_database_in_notion | boarding pass database]] as the data source for PDFOutput <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
3.  **Select the Template**
    *   Choose the "boarding pass template" from your Notion setup <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
4.  **Load Information**
    *   Upon selection, PDFOutput begins loading all information from the specified database and template <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
5.  **Export Documents**
    *   Once the information is fully loaded, click "export" to start [[generating_pdf_documents_with_notion | generating the PDF documents]] based on the data <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
    *   The system will generate multiple PDF documents for your use <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Output and Review

*   **Export Confirmation**
    *   After the export is successful, you can preview a sample of the generated PDF <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
*   **Review Generated PDFs**
    *   The preview will show the boarding pass with all details populated from the database <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
    *   You can then download the generated files <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
    *   Upon opening, you will see individual PDF outputs, each with different names and contexts, corresponding to the entries in your Notion database <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

This method illustrates how [[using_notion_with_pdf_output | Notion can be used with PDFOutput]] to efficiently [[pdf_document_generation_from_notion | generate PDF documents from a Notion database]] <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.