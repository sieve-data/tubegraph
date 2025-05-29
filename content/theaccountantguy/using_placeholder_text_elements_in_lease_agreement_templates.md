---
title: Using placeholder text elements in lease agreement templates
videoId: lCyhl8mofjE
---

From: [[theaccountantguy]] <br/> 

[[Generating lease agreement PDFs using Notion and PDFOutput | PDF Output]] can be utilized to generate lease agreement documents from a Notion database and a Notion page <a class="yt-timestamp" data-t="00:00:03"></a>.

## Template Setup with Placeholders
A lease agreement template typically contains all necessary details, such as landlord name and tenant name <a class="yt-timestamp" data-t="00:00:21"></a>. To enable dynamic content generation, specific details within this template are formatted as placeholder text elements <a class="yt-timestamp" data-t="00:00:34"></a>. These placeholders are typically enclosed in curly braces, for example:
*   `{landlord name}` <a class="yt-timestamp" data-t="00:00:40"></a>
*   `{tenant name}` <a class="yt-timestamp" data-t="00:00:42"></a>
*   `{street address}` <a class="yt-timestamp" data-t="00:00:44"></a>

## Integrating with a Notion Database
These placeholder elements in the template are designed to be automatically replaced by corresponding values from a Notion database <a class="yt-timestamp" data-t="00:00:45"></a>. The database contains rows with properties like "landlord name," "tenant name," and "street address," which supply the specific data for each unique lease agreement <a class="yt-timestamp" data-t="00:00:50"></a>. Each individual row in the database provides the values used to populate a distinct PDF document <a class="yt-timestamp" data-t="00:00:54"></a>.

## Generating Lease Agreements with PDF Output
The process of [[generating_lease_agreement_pdfs_using_notion_and_pdfoutput | generating lease agreement PDFs]] involves several steps within the [[generating_lease_agreement_pdfs_using_notion_and_pdfoutput | PDF Output]] platform:

1.  **Initial Setup:** Log into [[generating_lease_agreement_pdfs_using_notion_and_pdfoutput | PDF Output]]. Before proceeding, it is essential to follow the instructions in the help section to set up the API keys and other preliminary steps required for the application to function correctly <a class="yt-timestamp" data-t="00:01:03"></a>.
2.  **Connection Configuration:**
    *   Specify a connection name, such as "Lease Agreement" <a class="yt-timestamp" data-t="00:01:29"></a>.
    *   Select the Notion database (e.g., "Lease") that contains the tenant and landlord information <a class="yt-timestamp" data-t="00:01:36"></a>.
    *   Select the Notion template (e.g., "Lease Template") that contains the placeholder elements <a class="yt-timestamp" data-t="00:01:40"></a>.
3.  **[[mapping_database_elements_to_template_placeholders | Mapping Database Elements to Template Placeholders]]:**
    *   Click "next" to initiate the loading of database and template elements <a class="yt-timestamp" data-t="00:01:48"></a>.
    *   [[mapping_database_elements_to_template_placeholders | PDF Output]] will automatically map Notion database properties (displayed on the left) to the corresponding template elements (displayed on the right) if their names match <a class="yt-timestamp" data-t="00:02:04"></a>. For instance, "landlord name" from the database will map to the "landlord name" placeholder in the template <a class="yt-timestamp" data-t="00:02:21"></a>.
    *   If an element is not automatically mapped, it will appear in gray or red <a class="yt-timestamp" data-t="00:02:28"></a>. Users can manually click to select and map the correct properties <a class="yt-timestamp" data-t="00:02:35"></a>.
4.  **Export and Generation:**
    *   Click "export" to begin the document generation process <a class="yt-timestamp" data-t="00:02:44"></a>.
    *   A "PDF status" column will appear in the Notion database. Unticked rows indicate documents that need to be generated <a class="yt-timestamp" data-t="00:02:54"></a>. As PDFs are generated, the corresponding rows in Notion will be marked as "ticked" <a class="yt-timestamp" data-t="00:03:10"></a>.
5.  **Review and [[customizing_and_downloading_generated_lease_agreement_pdfs | Download]]:**
    *   Once generation is complete, a "preview sample" option allows users to view a generated PDF (e.g., a lease agreement for Tom Green and Sarah Blue) <a class="yt-timestamp" data-t="00:03:25"></a>.
    *   Users can then click "[[customizing_and_downloading_generated_lease_agreement_pdfs | download all]]" to obtain all generated PDF files, typically in a single archive <a class="yt-timestamp" data-t="00:03:55"></a>. The downloaded PDFs will be exact replicas of the template, with all placeholder information replaced by the data from the Notion database (e.g., an agreement for Alice Brown and Bob White) <a class="yt-timestamp" data-t="00:04:07"></a>.

## Important Considerations
For seamless operation, it is crucial that the naming convention of the properties in the Notion database precisely matches the naming convention of the placeholder text elements in the template <a class="yt-timestamp" data-t="00:04:24"></a>. This ensures that the automatic mapping process functions correctly and efficiently <a class="yt-timestamp" data-t="00:04:27"></a>.

For any questions or further assistance, users can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:04:51"></a>.