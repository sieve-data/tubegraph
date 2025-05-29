---
title: Configuring API keys for Notion integration
videoId: 432wMcdqv1w
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to generate PDF documents directly from a Notion database <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. It requires specifying connection details, selecting a Notion database, and choosing a Notion template to create the PDF document <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Prerequisites

Before generating PDFs, you need:
*   A Notion template with placeholder text elements in curly brackets (e.g., `{client name}`) <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. These placeholders will be replaced with data from a Notion database <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   A Notion database containing the information that will populate the template <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The column names in the database should ideally match the placeholder names in the template for automatic mapping <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

## [[setting_up_pdfoutput_with_api_keys | Setting up PDFOutput with API keys]]

To begin, access the settings window in PDF Output by clicking 'S' or pressing 's' on your keyboard <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

### Page Format
In the settings, you can specify the page format for your PDF documents <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. A4 is recommended for the best output, but other options are available <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

### [[setting_up_api_keys_in_notion | Setting up API keys in Notion]] (Notion Private Integration Key)

Currently, PDF Output uses the Notion private integration key <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

1.  **Generate the API Key**: Click on the provided link within PDF Output to get the Notion API key <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. This will redirect you to your logged-in Notion account <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
2.  **Create a New Integration**:
    *   Click on "new integration" <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
    *   Add a name for the integration, such as "new integration window" <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
    *   Select the workspace you want to link <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
    *   Keep the key type as "internal key" <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
    *   Click "Save" <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
3.  **Retrieve Secret Key**:
    *   Click "configure internal integration settings" <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
    *   Click "show" to reveal the secret key <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
    *   Copy this secret key immediately <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
    *   *Important*: Once the window is closed, you will not be able to see this key again, so save it somewhere secure <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
4.  **Paste and Save in PDF Output**: Close the Notion window and paste the copied key into the "notion API key" field in PDF Output <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. Click "Save" <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
    *   You can clear the API key settings by clicking the "clear" button <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

### [[connecting_notion_databases_with_external_tools_using_api_keys | Connecting Notion databases with external tools using API keys]]

After [[setting_up_api_keys_in_notion | setting up API keys in Notion]] through the integration, you need to connect your specific Notion template and database pages to this integration:

1.  **Access Notion Page Settings**: Go to your Notion template page and your Notion database page <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
2.  **Connect Integration**:
    *   On the top right of each page, click the three dots (`...`) <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
    *   Scroll down and find the "connect" option <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
    *   Click "connect" and type the name of the integration you just created (e.g., "new integration") <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
    *   Select your integration from the list to link it <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
3.  Repeat this process for both your Notion template and your Notion database <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. This completes the [[connecting_notion_databases_with_external_tools_using_api_keys | API key setup]] for your Notion pages <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

## Database Property for PDF Generation

In your Notion database, there must be a property named "PDF status" <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. For a PDF to be generated for a specific row of information, this "PDF status" checkbox must be kept unchecked <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. Once the PDF is generated, this checkbox will automatically be ticked <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

## [[utilizing_api_keys_to_connect_notion_to_pdf_generation_tools | Utilizing API keys to connect Notion to PDF generation tools]]

Once the API key is configured and Notion pages are connected:

1.  **Specify Connection Details in PDF Output**:
    *   Enter a connection name (e.g., "invoice generation") <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
    *   Select your Notion database and Notion template from the dropdown lists <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
    *   Click "Next" <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

2.  **Map Properties**:
    *   PDF Output reads information from the template and database and automatically maps Notion properties (column names) to the placeholder elements in your template <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
    *   Ensure the naming convention in your database columns exactly matches the placeholder names in the template (e.g., `client name` in database and `{client name}` in template) <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. This enables automatic mapping <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
    *   If elements are not mapped (shown in gray), you can manually click and select the correct PDF element fetched from the template <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
    *   Sorting and filtering options are available to help find elements quickly <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.

### Export and Download

1.  **Generate PDF**: Click "Export" to start processing the documents <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. The "PDF status" checkboxes in your Notion database will automatically tick once generated <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
2.  **Preview and Download**:
    *   Click "preview sample" to view the generated PDF directly on the web interface <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
    *   Click "download all" to download the PDF files to your local machine <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
    *   On the free plan, a watermark will appear on the generated PDFs <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. Paid plans remove this watermark <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

## Managing Connections and Plans

*   **Saved Connections**: Once a connection is created, it can be loaded again from the "C" (connections) section, allowing you to reuse defined settings without re-entering them <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
*   **Upgrade Options**: An "Upgrade" option shows your current plan (e.g., basic plan with a limit of 1000 documents) <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. You can choose between monthly and yearly Pro or Enterprise plans based on your needs <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
*   **Templates**: Future templates will be available under the "T" (templates) section <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
*   **Feedback and Help**: You can submit feedback through the feedback window <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. A help window will contain tutorial videos <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.

## Customizing Templates

You can [[using_notion_for_invoice_template_creation | customize your own template]] for PDF generation <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>. Ensure that you use curly braces (`{}`) for placeholder text elements and match the names inside the braces exactly with the column names in your Notion database <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. This allows the system to automatically import values from the database into the template <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.