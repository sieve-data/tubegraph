---
title: PDFOutput for bulk document generation
videoId: lCyhl8mofjE
---

From: [[theaccountantguy]] <br/> 

PDFOutput is a tool used to generate PDF documents in bulk from a Notion database and Notion page template <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This process involves creating a template with placeholder text elements and then populating these elements with data from each row of a database <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Key Concepts

### Template Preparation
A template, such as a lease agreement, is prepared with specific details and placeholder text elements <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. These placeholders, like "landlord name" or "tenant name", are enclosed in curly braces (e.g., `{landlord name}`) <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. These will be replaced by actual data from the database <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

### Database Integration
A Notion database holds the data corresponding to the template's placeholders <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. For example, a database for lease agreements would include columns for "landlord name," "tenant name," and "street address" <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Each row in the database represents a unique document to be generated <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Steps for [[generating_bulk_pdfs_with_database_integration | Bulk PDF Generation]]

1.  **Log In and Setup**: Log into the PDFOutput platform <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. It's crucial to visit the help section first to follow initial setup instructions, including setting up API keys <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
2.  **Specify Connection Details**:
    *   Provide a "connection name" (e.g., "Lease Agreement") <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
    *   Select the Notion database from a dropdown menu <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. The dropdown lists databases connected via the API key <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
    *   Select the corresponding template <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
3.  **Automatic Mapping**: After clicking "next," PDFOutput automatically loads and maps Notion database properties to the template's PDF elements, especially if their names match <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
    *   Notion properties (e.g., "landlord name") are listed on the left <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
    *   Corresponding template elements are mapped on the right <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
    *   Unmapped elements appear in gray; clicking them reveals available properties, with unmapped ones in red <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
4.  **[[bulk_exporting_pdf_documents | Exporting PDFs in Bulk]]**:
    *   Click "Export" <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
    *   A "PDF Status" property appears in the Notion database <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. This column tracks which rows have had PDFs generated <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Unticked rows are generated, and then ticked <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
    *   Once processing is complete, a "preview sample" option becomes available to view a single generated PDF <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   Click "Download all" to download all generated PDF files in one go <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. The download option remains available if you forget to download them initially <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

### Important Considerations
*   **Naming Convention**: Ensure that the naming conventions of the Notion database properties and the template's placeholder elements match exactly to facilitate automatic mapping <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>, <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   **Initial Setup**: Always refer to the help section for preliminary setup steps required before generating documents <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

For any questions, support can be reached at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.