---
title: Creating and using templates for PDF generation in Notion
videoId: 432wMcdqv1w
---

From: [[theaccountantguy]] <br/> 

[[generating_pdf_documents_from_notion_database | PDF output]] is a tool designed to [[generating_pdf_documents_from_notion_database | generate PDF documents directly from a Notion database]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. It allows users to [[using_templates_in_notion_for_pdf_generation | create PDF documents]] by specifying a connection, selecting a Notion database, and choosing a Notion template <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Requirements for PDF Generation

To [[using_notion_templates_for_pdf_generation | generate PDF documents]] using [[generating_pdf_documents_from_notion_database | PDF output]], two primary components are needed:

1.  **A Notion Template**: This template will serve as the structure for the PDF document <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
    *   **Placeholder Text**: The template should include placeholder text elements enclosed in curly brackets (e.g., `{{client name}}`, `{{invoice number}}`) <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. These placeholders will be dynamically replaced with data from the Notion database <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
    *   An example is an [[creating_and_using_an_invoice_template_in_notion | invoice template]] with fields for from/to addresses, invoice number, date, terms, and due date <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
2.  **A Notion Database**: This database holds the data that will populate the template <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
    *   **Column Names**: The column names in the database (e.g., "Client Name", "Client Company", "Client Address") must exactly match the placeholder names specified in the template <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. This ensures automatic mapping of data during the generation process <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
    *   Each row in the database represents a unique set of information that will be used to generate a separate PDF document <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
    *   **PDF Status Property**: The database should include a property named "PDF Status" (a checkbox) <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. For a PDF to be generated for a specific row, this checkbox must be unchecked <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. Once the PDF is generated, this property is automatically ticked <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

## Setting Up PDF Output

### 1. Configure Settings

*   Access settings by clicking 'S' or hitting 's' on the keyboard <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   **Page Format**: Select the desired page format (e.g., A4 for best output) <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>, <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.
*   **Notion API Key**: Input your Notion API key <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
    *   Currently, a Notion private integration key is required <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
    *   To obtain the key, click the provided link which redirects to your Notion account <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
    *   [[creating_professional_invoice_templates_in_notion | Create a new integration]], give it a name (e.g., "New Integration Window") <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>, select the workspace <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>, and ensure it's an internal key <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
    *   After saving, configure internal integration settings and click "Show" to reveal the secret key <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. This key is user-specific <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
    *   Copy and save the key immediately, as it cannot be viewed again once the window is closed <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
    *   Paste the copied key into the Notion API key field in PDF Output and click "Save" <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
    *   To clear the key, click the "Clear" button <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

### 2. Connect Notion Database and Template

*   In your Notion workspace, for both the template page and the database page, click the three dots (`...`) in the top right corner <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   Scroll down and select "Connect" <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   Type the name of the integration you created (e.g., "New Integration") and select it to establish the connection <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   Repeat this step for both your Notion template and your Notion database <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

## Generating PDF Documents

1.  **Specify Connection Details**:
    *   Enter a connection name (e.g., "Invoice Generation") <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
    *   Select your Notion database from the dropdown list <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
    *   Select your Notion template from the dropdown list <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
2.  **Map Properties**:
    *   Click "Next" <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. PDF Output will read information from both the template and database <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
    *   The left side displays Notion properties (database column names) <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
    *   The tool automatically maps these properties to the corresponding elements (placeholders) in the Notion template <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
    *   **Recommendation**: Ensure that the naming convention in the template (placeholders) exactly matches the column names in the database for automatic mapping <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.
    *   **Manual Mapping**: If elements are not automatically mapped (appearing in gray), click on them to manually select the correct PDF element from the Notion template <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
    *   Sorting and filtering options are available to help find elements quickly <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.
3.  **Export and Download**:
    *   Click "Export" <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. The tool will process the documents <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
    *   The "PDF Status" checkboxes in the Notion database will automatically tick once the PDFs are generated <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
    *   After successful export, you can "Preview Sample" on the web interface <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>, or click "Download All" to save the PDF files to your computer <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
    *   The generated PDFs will have the placeholder text replaced with the actual data from the database <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
    *   A watermark will appear on PDFs generated with the free plan, which is removed in paid plans <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

## Features and Management

*   **Saved Connections**: Once a connection is created, it can be easily reloaded by clicking the 'C' icon, which automatically loads previously defined settings, allowing for subsequent [[bulk_pdf_document_generation_using_notion | generation of more documents]] without re-specifying details <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
*   **Upgrading Plan**: Users on the basic plan have a limit (e.g., 1000 documents) <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. An "Upgrade" option is available to view and subscribe to monthly or yearly Pro or Enterprise plans <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
*   **Templates Section**: A dedicated "Templates" section will show available templates, including the explained [[creating_and_using_an_invoice_template_in_notion | invoice template]] <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
*   **Feedback**: Users can submit feedback directly to the developer to help improve the tool <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
*   **Help**: A "Help" window will provide a reference video tutorial <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   **Sign Out**: A profile icon offers the option to sign out <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

## [[customizing_notion_templates_for_pdf_documents | Customizing Templates]]

Users can [[customizing_notion_templates_for_pdf_documents | customize their own templates]] according to their requirements <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>. The key is to:

1.  Use curly braces for placeholder names (e.g., `{{Client Name}}`) <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
2.  Use the exact same name for the corresponding column in the Notion database <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. This enables the tool to automatically read and import values from the database into the template's placeholder elements for each row of data <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.