---
title: Customizing templates and databases for document generation
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

[[using_templates_to_automate_pdf_creation | Automating PDF creation]] from [[using_notion_templates_and_databases_for_pdf_generation | Notion templates and databases]] involves using a service like PDFOutput.com. This process leverages [[customizable_pdf_templates | customizable PDF templates]] and structured databases to generate various documents, such as purchase orders, invoices, or payment receipts <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Getting Started with PDFOutput

1.  **Log in to PDFOutput.com**: The initial step is to log into PDFOutput.com <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The interface displays options for connection name, Notion database, and Notion template <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.
2.  **Select a Template**: Navigate to the "Templates" sidebar element to view a list of predefined [[customizable_pdf_templates | templates]], including invoices, payment receipts, and purchase orders <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. Templates can be searched, sorted, or filtered <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
3.  **Download and Duplicate**: Select the desired template (e.g., Purchase Order) and click its download link <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This opens a dedicated page for the template and its associated database <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. Duplicate this page to your Notion workspace <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

## Understanding Templates and Databases

A typical document generation setup involves two core components:

*   **Template**: This is the design of your document, containing static text and placeholder elements. Placeholders are enclosed in curly braces (e.g., `{purchase order number}`, `{supplier name}`) <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. These placeholders will be replaced with actual data from your database <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **Database**: This holds the dynamic information for your documents. Each row in the database represents a unique document, and each column contains specific data fields (e.g., "Supplier Name", "Buyer Name", "Date", "Purchase Order Number") <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. The system will generate a PDF document for each row of data <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## [[Customizing templates for PDF document generation | Customizing Templates]] and [[working_with_databases_and_data_replacement_in_pdf_templates | Working with Databases]]

[[customizable_pdf_templates | Templates]] and databases are [[customizing_templates_for_pdf_document_generation | customizable]] to fit specific requirements <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>:

*   **Template Modification**: You can add, delete, or modify any elements within the template. Ensure that all dynamic values intended for replacement are placed inside curly braces <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **Database Matching**: The names of database columns must *exactly* match the placeholder text within the template, including case and spaces. Mismatches can prevent proper linking, though these can be manually corrected during the mapping step <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

## Connecting and Mapping Data

Once the template is duplicated to Notion:

1.  **Connect Notion to PDFOutput**: In PDFOutput settings, select the page format and click "Click here to add templates" <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. Choose your Notion workspace and the duplicated template page to allow access <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. This authentication connects the Notion page with PDFOutput <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
2.  **[[mapping_database_elements_to_templates_for_pdf_generation | Map Database Elements to Templates]]**: After connecting, select the appropriate Notion database and template page in PDFOutput <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. PDFOutput automatically matches most elements <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. Unmatched properties (e.g., due to spacing differences like "total amount" vs. "totalamount") can be manually mapped using filters <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. The left side shows Notion database properties, and the right displays template elements <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

## Generating and Managing Documents

1.  **Exporting PDFs**: Click "Export" to begin generating PDFs <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. A "PDF status" column will be added to your Notion database, ticking entries as PDFs are generated <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. To regenerate a PDF, ensure this checkbox is unticked <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
2.  **Preview and Download**: Once exported, you can preview samples of the generated PDFs and then download all documents <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
3.  **[[managing_templates_and_databases_in_pdfoutput | Managing Templates and Databases]]**:
    *   **Connections**: PDFOutput saves generated connections, allowing you to quickly regenerate documents without re-entering database and page details <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
    *   **Templates**: Access and manage your [[creating_and_using_templates_for_pdf_generation | templates for PDF generation]] via the sidebar <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.
    *   **Upgrade**: Free plans include watermarks; paid plans remove them <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
    *   **Settings**: Define page format (e.g., A4, Letter) for generated PDFs <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
    *   **Feedback/Help**: Options are available for reporting issues or accessing setup demonstrations <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.

This process enables efficient [[customizing_invoice_templates_for_bulk_generation | bulk generation of customized PDF documents]] by linking Notion databases to structured templates.