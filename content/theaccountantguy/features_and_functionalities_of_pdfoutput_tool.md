---
title: Features and functionalities of PDFOutput tool
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

[[PDF Output Software Features | PDFOutput]] is a straightforward tool designed to [[using_pdfoutput_for_bulk_document_generation | generate PDF documents in bulk]] by leveraging a Notion page as a template and a Notion database to supply the elements for replacement within that template <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Core Functionality

Upon logging into [[PDF Output Software Features | PDFOutput]], users encounter sections for Notion database and Notion template. The user must define a Notion database and select a specific Notion template for PDF generation <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

### [[Steps to set up and export PDFs using PDF Output | Setting Up and Exporting PDFs]] (Invitation Letter Use Case)

To use [[PDF Output Software Features | PDFOutput]], a template and a database must first be created in Notion <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

1.  **Creating a Notion Template**:
    *   Start by creating a new blank page in your Notion workspace <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
    *   Give it a name, such as "invitation letter template" <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
    *   Set the page to "full width" mode <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
    *   Define the content of your template, including sections that will be replaced with data. These dynamic sections, or placeholders, must be enclosed within curly braces, e.g., `{title}` and `{customer name}` <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

2.  **Creating a Notion Database**:
    *   Create another new page in Notion and select the "table" format <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
    *   Name this database, for example, "invitation letter database" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
    *   Crucially, the column names in this database must *exactly match* the placeholder names used in the template (e.g., "title", "customer name") <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
    *   Populate the database with the unique information for each document you wish to generate <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

3.  **Connecting Notion to [[PDF Output Software Features | PDFOutput]]**:
    *   In the [[PDF Output Software Features | PDFOutput]] interface, click on "Click here to add database" or "Click here to add template" <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
    *   This will redirect you to the Notion authorization screen <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
    *   Ensure the correct Notion account/workspace is selected <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   Select both your created template and database, then click "Allow access" <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
    *   [[syncing_and_exporting_documents_using_pdf_output | PDFOutput]] will then automatically fetch and synchronize the selected Notion database and template <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

4.  **Mapping Properties**:
    *   After synchronization, define a connection name (e.g., "invitation letter") <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
    *   The system automatically loads the template and database <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
    *   On the left, you'll see database properties (e.g., "customer name", "title") <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   On the right, the mapped template elements are displayed <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. If the naming conventions for placeholders in the template and columns in the database are identical, the mapping will occur automatically <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. Otherwise, manual mapping is required <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
    *   Sorting, searching, and filtration options are available for properties <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

5.  **[[generating_pdf_invoices_using_pdfoutput | Generating PDFs]]**:
    *   Once mapping is complete, click "Create PDF" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
    *   [[PDF Output Software Features | PDFOutput]] will generate individual PDF documents for each row in your Notion database, with the placeholders replaced by the corresponding data <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
    *   Users can preview a sample PDF before downloading all generated documents <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

### Key Considerations for Template and Database Creation

*   Always enclose placeholder text elements in Notion templates within curly braces (e.g., `{placeholder}`) <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   Use the exact same naming convention for Notion database column headers as your template's placeholder names to ensure automatic mapping <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

## Additional Features and Functionalities

[[using_pdf_output_tool_for_efficient_document_creation | PDFOutput]] includes several features accessible via a sidebar:

### Connections
The "Connections" tab lists all previously created document generation setups. Clicking on a connection will automatically load the predefined database and template, allowing for quick regeneration of documents without re-setting up the connection every time <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

### Templates
The "Templates" section provides a list of predefined templates available for various requirements <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. Each template comes with links to its corresponding database and template Notion pages <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. To use a predefined template, click "Start with this template" to duplicate both the template and database into your Notion workspace <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

### Upgrade Option
Under the free plan, generated PDFs include a "Made with [[PDF Output Software Features | PDFOutput]]" watermark and have certain limitations <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. Users can upgrade their subscription plan to remove watermarks and access full features via the "Upgrade" section <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

### Settings
The "Settings" tab allows users to:
*   Choose desired page formats for PDF output <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
*   Add more templates and databases after initial setup <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.

### Feedback and Help
*   **Feedback**: Users can provide feedback directly through the "PDF feedback" section <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Help**: A "Help" section provides access to demonstrations and guides on [[using_pdfoutputcom_for_bulk_pdf_generation | how to use the tool]] <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.

The sidebar can be closed to maximize screen space <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.