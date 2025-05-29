---
title: Using templates and databases to create professional PDFs
videoId: Uh1g7uXtr_4
---

From: [[theaccountantguy]] <br/> 

This guide demonstrates how to [[using_templates_to_create_pdf_documents_in_bulk | generate PDF documents in bulk]] for each row within a database by leveraging templates and a specialized tool called PDF Output <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This method automates the creation of professional documents, such as application forms or invoices, without manual data entry for each file <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Core Concept: Template and Database Interaction

The process revolves around two main components:
1.  **A Database**: This database, such as an application form database, stores all the relevant information in rows, with each row representing a unique record <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. For instance, it might track candidate profiles, education requirements, and other application details <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
2.  **A Template**: A document template is designed to match the database structure. It uses placeholder fields, enclosed in curly brackets (e.g., `{Full Name}`, `{Date of Birth}`), which correspond exactly to the column names in your database <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. This template serves as the blueprint for the final PDF document <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

When the generation process occurs, the data from each database row automatically populates its corresponding placeholder in the template, creating a unique PDF for that record <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

## Preparing the Database with Templates

To ensure successful PDF generation, each row in your database needs to contain the template content.

### Manually Populating Rows

Initially, you can manually copy the content of your template file and paste it into the dedicated content section for each row in your database <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. This involves opening each row, scrolling to the bottom, and pasting the template <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

### Automating Template Population with Default Templates

To streamline the process for new database entries, you can [[customizing_templates_for_pdf_generation | create a default template]] within your database:
1.  Click the drop-down menu next to "New" <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
2.  Select "New template" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
3.  Name the template (e.g., "Applicant Name") <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
4.  Paste your template content into this new template <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
5.  Set this template as the default for all views in your database <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

Once set, any new row added to the database will automatically include this template content, eliminating the need for manual copying and pasting <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. This ensures that every page will have the corresponding template file replicated <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>, [[utilizing_predefined_pdf_templates_for_efficient_workflow | utilizing predefined PDF templates for an efficient workflow]].

## Introducing the Tool: PDF Output

The specific tool used for this demonstration is [[using_pdf_output_tool_for_efficient_document_creation | PDF Output]], which specializes in generating documents in bulk from Notion databases <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

### Connecting Your Notion Database to PDF Output

To use PDF Output, your Notion database must be properly connected:
1.  **Sign in to PDF Output** <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
2.  **Copy Database URL**: Get the URL of your Notion database from the browser's address bar <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Paste this URL into the designated field in PDF Output <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
3.  **Add API Key**:
    *   PDF Output requires a Notion API key for access <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
    *   Navigate to Notion's API settings (via a link in PDF Output) <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
    *   Create a "New integration," give it a name, select your workspace, and save <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   Copy the "Internal Integration Secret" key <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a> and paste it into PDF Output <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
4.  **Connect Database to API Key**: In Notion, open your database, click the three dots (`...`), select "Connections," and search for the name of the API key you just created <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. Select it and confirm <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
5.  **Publish Database**: Finally, click "Share" in your Notion database, then "Publish," and confirm to make the database accessible to PDF Output <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. This step is crucial for the tool to fetch pages within the database <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

## Generating PDFs

Once the database is connected and published:
1.  **Load Database**: In PDF Output, click "Load database" <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
2.  **Select Naming Column**: Choose a database column (e.g., "Full Name") from the dropdown menu to be used as the reference for naming the generated PDF files <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. This helps in [[exporting_and_managing_generated_pdf_documents | exporting and managing generated PDF documents]] efficiently.
3.  **Choose Rows**: Decide whether to generate PDFs for all rows, a specific range, or custom selected rows <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
4.  **Generate PDF**: Click "Generate PDF" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

A preview window will pop up, showing the populated PDF with data from the corresponding database row <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. All blue-marked elements (placeholders) will be replaced with actual data <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. You can adjust settings like paper size and layout on the right side <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. Click "Save" to download the PDF to your desired location <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

## Reviewing the Output

The generated PDFs will be named according to the chosen column (e.g., "Carol Davis.pdf") <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. The documents will appear professional and clean, with all database information accurately inserted into the template structure <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

### Key Requirements for Successful Generation:
*   The template form must have fields matching the database columns, enclosed in curly brackets <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   Each row in the database must contain the template file content <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.

## Alternative Template Usage

While matching placeholder elements to database fields is a common use case, PDF Output offers flexibility <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>:

*   **General Documentation**: You can generate PDFs from any notes or documentation within your database rows, even if the content doesn't strictly match database elements <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. The tool will read the entire page content and generate the document <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **Direct Page URL as Template**: Instead of populating the template within each database row, you can directly use a Notion page's URL as the template. Copy the main URL of your template page, paste it into the Notion Page field in PDF Output, and click "Load page" <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. Then proceed to load your database and generate PDFs as usual <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

This dual approach allows you to either ensure every database row has its own templated content or to use a single external template page to generate documents from a database. This capability facilitates tasks such as [[generating_professional_invoice_pdfs | generating professional invoice PDFs]] or [[generating_professional_invoices_from_a_database | invoices from a database]].

## Additional Resources

PDF Output provides further resources:
*   **Contact Section**: For support or queries <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.
*   **Templates Section**: Offers predefined templates and databases that can be copied and used directly <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>, further simplifying the process of [[using_google_document_templates_for_pdf_generation | using templates for PDF generation]].
*   **How-to Videos**: Associated with each template for guidance <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.