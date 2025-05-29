---
title: Using application form templates in Notion
videoId: Uh1g7uXtr_4
---

From: [[theaccountantguy]] <br/> 

This article outlines a method for generating PDF documents from an application form database in Notion, leveraging a template and an external tool called PDF Output <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. This process automates the creation of individual PDF documents for each database entry without manual data entry <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Setting Up the Notion Application Form Database

The first step involves setting up a Notion database to track application form requirements <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. This database typically includes columns for candidate profiles, education requirements, and other relevant information <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

### Creating the Application Form Template

An application form template is created to match the fields in the Notion database <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **Placeholders**: Data fields from the database, such as "full name," "date of birth," "gender," and "phone number," are represented in the template using curly brackets (e.g., `{full name}`) <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. These placeholders will be automatically populated with data from the corresponding database columns <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Integrating the Template into Database Rows

To ensure each row in the database can generate a PDF, the template needs to be present within each row's page <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

#### Manual Copy-Paste Method
Initially, you can manually copy the content of the template and paste it into each individual database row's page <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. When pasted, the template's content, including the curly bracket placeholders, will appear in the page <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

#### Automating Template Integration with a Default Template
To avoid manually copying the template for every new row, you can [[using_templates_and_buttons_in_notion | create a default template]] within the database <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>:
1.  Click the drop-down arrow next to the "New" button in the database <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
2.  Select "New template" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
3.  Name the template (e.g., "Applicant Name") <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
4.  Paste the application form template content into this new template <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
5.  Click outside the template editor to save <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
6.  Set this template as default for all views in the application form database by clicking the three dots next to the template name and selecting "Set as default" <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

With a default template, any new row added to the database will automatically include the template content, ensuring it's ready for PDF generation <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

## Connecting Notion to PDF Output

PDF Output is a tool that allows generating documents in bulk from Notion databases <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
1.  **Sign in to PDF Output**: Access the PDF Output dashboard <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
2.  **Copy Database URL**: Copy the URL of your Notion application form database from your web browser's address bar <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
3.  **Paste Database URL in PDF Output**: Paste the copied URL into the designated field in PDF Output <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
4.  **Connect via API Key**:
    *   Click the link in PDF Output to add an API key, which directs you to Notion's API settings <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
    *   Create a new integration, provide a name, choose your workspace, and save <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
    *   Copy the "Internal Integration Secret" from the newly created integration <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.
    *   Paste this API key into PDF Output <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
5.  **Connect Database to API Key**: In Notion, open your application form database, click the three dots menu, go to "Connections," and add the integration (your API key's name) you just created <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
6.  **Publish Database**: To allow PDF Output to access the database pages, click "Share" then "Publish" on your Notion database <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. This step is crucial for fetching pages <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

## Generating PDF Documents

Once connected, you can generate PDFs:
1.  **Load Database**: In PDF Output, click "Load Database" <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
2.  **Select Naming Column**: Choose a database column (e.g., "Full Name") to use as the file name for the generated PDFs <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
3.  **Select Rows**: Decide whether to generate PDFs for "all rows," a "range of rows," or "custom rows" <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
4.  **Generate PDF**: Click "Generate PDF" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
5.  **Review and Save**: A window will pop up showing the populated PDF for each selected row. You can review the populated data, which automatically replaces the placeholder elements from the template <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>. You can also adjust settings like paper size and layout <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. Save each generated PDF to your desired location <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

The resulting PDF files will be professionally formatted, with the data from the Notion database automatically inserted into the template <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

## Key Considerations and Flexibility

*   **Template Structure**: While matching database fields with curly bracket placeholders is common, the template doesn't strictly need to match all database elements <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. PDF Output can read any content within the page and generate a document <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **Alternative Method (External Template URL)**: Instead of the template being *inside* each database page, you can use a separate Notion page as the master template. In PDF Output, you would provide the URL of this separate template page, along with the database URL. The tool will then combine the template with the database rows to generate PDFs <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
*   [[creating_professional_invoice_templates_in_notion | This process can be applied to any document generation]], such as [[creating_and_using_an_invoice_template_in_notion | creating invoices]] from an invoices database <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

## Additional Resources

PDF Output provides a templates section with predefined templates for various use cases, which users can directly copy and use <a class="yt-timestamp" data-t="00:57:57">[00:57:57]</a>. Each template often includes an associated "how-to-use" video <a class="yt-timestamp" data-t="01:10:09">[01:10:09]</a>. For support, a contact section is available on the PDF Output homepage <a class="yt-timestamp" data-t="01:43:43">[01:43:43]</a>.