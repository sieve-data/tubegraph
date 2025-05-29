---
title: Creating and using Notion templates
videoId: 432wMcdqv1w
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to generate PDF documents directly from a Notion database <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It simplifies the process of creating various documents, such as [[using_notion_templates_for_invoice_pdfs | invoice PDFs]], by leveraging Notion's flexible structure.

## Core Requirements for PDF Generation

To use PDF Output effectively, you need:
1.  A Notion template <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a> <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
2.  A Notion database <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

### Notion Template Structure
A Notion template serves as the blueprint for your PDF documents <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. For example, an [[creating_and_using_invoice_templates_in_notion | invoice template]] can include details like from/to addresses, invoice number, date, and due date <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

Critical elements in the template are **placeholder text elements**, which are mentioned in curly brackets (e.g., `{client name}`, `{invoice number}`, `{due date}`) <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a> <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. These placeholders will be automatically replaced with data from your Notion database during PDF generation <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

### Notion Database Structure
Your Notion database holds the specific data that will populate the template's placeholders <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Each row in the database represents a unique set of information, such as client name, company, and address for an invoice <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a> <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

It is recommended that the naming convention for the columns in your Notion database exactly matches the placeholder names in your template to facilitate automatic mapping <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a> <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.

## Setting Up PDF Output

### 1. Configure Settings
Access the settings by clicking 'S' or hitting 's' on your keyboard <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   **Page Format:** Select the desired page format. A4 is generally recommended for best output, but other options are available <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a> <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.
*   **Notion API Key:** Input your Notion API key. Currently, this requires a private integration key <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

### 2. Obtain Notion Private Integration Key
1.  Click "Click here to get the Notion API key" in the settings <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
2.  You will be redirected to your Notion account to create a new integration <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
3.  Click "New integration," provide a name (e.g., "new integration window"), and select the workspace you want to link <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. Keep it as an "internal key" <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
4.  Click "Save," then "Configure internal integration settings" <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
5.  Click "Show" to reveal the secret key <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
6.  **Copy this key immediately** as it will not be visible again once the window is closed <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a> <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
7.  Paste the copied key into the "Notion API key" field in PDF Output's settings and click "Save" <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

### 3. Connect Notion Template and Database
For both your Notion template page and your Notion database:
1.  Navigate to the page/database in Notion <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
2.  Click the three dots in the top right corner <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
3.  Scroll down and select "Connect" <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
4.  Search for and select the integration name you created earlier (e.g., "new integration") <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
This step establishes the connection for [[setting_up_a_notion_database_and_template_for_pdf_generation | setting up a Notion database and template for PDF generation]] <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.

### 4. Add "PDF Status" Property to Database
In your Notion database, ensure there is a checkbox property named "PDF status" <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   If this box is **unchecked**, PDF Output will generate a PDF for that specific row of information <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   If it is **checked**, a PDF will not be generated for that row <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
This property helps track which records have already had PDFs generated <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

## Generating PDF Documents

1.  **Specify Connection Details:** In the PDF Output interface, provide a connection name (e.g., "invoice generation"), select your Notion database from the dropdown, and choose your Notion template <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
2.  **Map Properties:** Click "Next" <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. PDF Output will read information from both your template and database <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
    *   It typically **automatically maps** Notion database properties (columns) to their corresponding placeholder elements in the Notion template if the names match <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a> <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
    *   If an element is not mapped (appears in gray), you can manually click on it and select the correct database property to map <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
    *   The interface provides search, sort, and filter options (for mapped/unmapped properties) to assist in mapping <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. This ensures smooth [[customization_and_adaptability_of_notion_templates | customization and adaptability of Notion templates]] for PDF generation.
3.  **Export:** Click "Export" <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. The tool will process the documents <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
    *   During processing, the "PDF status" checkboxes in your Notion database will automatically tick as PDFs are generated for each row <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. This is how PDF Output facilitates [[using_a_notion_database_and_templates_to_create_pdf_invoices | creating PDF invoices]] directly.
4.  **Preview and Download:** Once export is successful, you can:
    *   Click "Preview sample" to view the PDF directly in the web interface <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
    *   Click "Download all" to download all generated PDFs to your local system <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
    *   Note: Free plans include a watermark on generated PDFs; paid plans remove this <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

## Managing Connections and Subscriptions

*   **Load Saved Connections:** After creating a connection, you can easily load its settings again by clicking the 'C' icon and selecting the saved connection <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. This allows for quick regeneration of documents <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
*   **Upgrade Options:** The "Upgrade" section shows your current plan (e.g., basic plan with a 1000-document limit) <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. You can upgrade to Pro or Enterprise plans (monthly or yearly) for higher limits and features <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. After upgrading, click "Activate subscription" to apply the new plan <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

## Additional Features

*   **Templates:** This section will showcase more available templates in the future, including the demonstrated [[using_notion_for_invoice_template_creation | invoice template]] <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Settings:** Access general settings like page format <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.
*   **Feedback:** Submit feedback directly to the developer <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
*   **Help:** Access tutorial videos and resources <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.
*   **Sign Out:** Log out of your profile <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

## Customizing Notion Templates

You can [[customization_and_adaptability_of_notion_templates | customize your own template]] to suit your specific requirements <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
*   Ensure placeholder text elements are enclosed in curly braces (e.g., `{My Custom Field}`) <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
*   Use the exact same name as a column in your Notion database <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. This allows PDF Output to automatically read and import values from your database into the template's placeholder elements for each row of data <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.

For assistance, you can contact notionformyuse@gmail.com or connect via Twitter/LinkedIn <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.