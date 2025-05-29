---
title: Generating PDFs from Notion using PDFOutput
videoId: 432wMcdqv1w
---

From: [[theaccountantguy]] <br/> 

PDFOutput is a straightforward tool designed to [[generating_pdf_documents_in_bulk_using_notion_and_pdfoutput | generate PDF documents directly from a Notion database]] <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It allows users to specify connection details, select a Notion database, and choose a Notion template to create PDF documents <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Requirements

To utilize PDFOutput, you need two main components in Notion:

1.  **A Notion Template**: This template serves as the layout for your PDF document <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. It can be, for instance, an invoice template containing details like sender and recipient addresses, invoice number, date, and due date <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Within the template, certain elements, such as `client name`, `client company`, `client address`, `invoice number`, and `due date`, are marked as placeholder text elements using curly brackets (e.g., `{client name}`) <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>, <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. These placeholders will be replaced by data from your Notion database <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
2.  **A Notion Database**: This database holds the information that will populate the placeholders in your template <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. For an invoice example, it would contain columns like "Client Name", "Client Company", and "Client Address", with each row representing unique information for a specific invoice <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## [[Connecting and setting up PDF output with Notion | Connecting Notion to PDFOutput]]

Before generating PDFs, you need to configure PDFOutput's settings:

1.  **Access Settings**: Click the 'S' button or press 's' on your keyboard to open the settings window <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>, <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
2.  **Page Format**: Select the desired page format. A4 is recommended for the best output, though other options are available <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>, <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>, <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.
3.  **Notion API Key Setup (Private Integration)**:
    *   Click the provided link to get your Notion API key <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. This redirects you to your Notion account <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
    *   Create a new integration by clicking "New Integration" <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
    *   Give it a name (e.g., "New Integration Window") <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
    *   Select the workspace you want to link <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
    *   Keep it as an "internal key" and click "Save" <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
    *   Click "Configure internal integration settings" and then "Show" to reveal your secret key <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. This key is unique and only accessible to the user who created it <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
    *   **Important**: Copy this secret key immediately, as it will not be visible again once the window is closed <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>, <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
    *   Paste the copied key into the "Notion API Key" field in PDFOutput and click "Save" <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>, <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. You can clear the API key settings by clicking "Clear" <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
4.  **Connect Notion Pages**:
    *   In both your Notion template and database, click the three dots on the top right <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>, <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
    *   Scroll down and select "Connect" <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>, <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
    *   Type or select the name of the integration you just created (e.g., "new integration") <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
    *   Ensure both the template and the database are connected to the same integration <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>, <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

## Preparing the Notion Database for [[generating_pdf_invoices_in_bulk_using_a_notion_database | PDF Generation]]

For PDFOutput to function correctly, your Notion database needs a specific property:

*   **PDF Status Property**: Add a checkbox property named "PDF status" to your database <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
    *   If this checkbox is *unchecked*, PDFOutput will generate a PDF for that specific row of information <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
    *   If it's *checked*, a PDF will not be generated for that row <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
    *   Always ensure this checkbox is *unchecked* for rows you want to convert to PDF <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

## [[Integrating Notion with PDF generation | Generating PDFs]]

Once connected and set up:

1.  **Enter Details in PDFOutput**:
    *   Provide a "Connection Name" (e.g., "invoice generation") <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
    *   Select your "Notion Database" from the dropdown list (databases connected via the API will appear here) <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
    *   Select your "Notion Template" <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
2.  **Map Properties**: Click "Next" <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
    *   PDFOutput reads information from both the template and database <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
    *   On the left, you'll see all Notion properties from your database (e.g., "Client Name", "Client Company", "Client Address") <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
    *   PDFOutput automatically maps these properties to the corresponding placeholder elements in your Notion template <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
    *   **Recommendation**: Ensure the naming conventions in your template placeholders (e.g., `{client name}`) exactly match the column names in your database (e.g., "Client Name") for automatic mapping <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
    *   If an element isn't mapped (appears in gray), you can manually click on it and select the correct Notion property from the fetched PDF elements list <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>, <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
    *   The interface includes search, sort, and filter options to manage properties (e.g., filter for unmapped or mapped properties) <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
3.  **Export and Download**:
    *   Click "Export" <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
    *   PDFOutput processes the documents, and the "PDF status" checkboxes in your Notion database will automatically tick as PDFs are generated for each row <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>, <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
    *   Once successful, you have two options:
        *   **Preview Sample**: View the generated PDF document directly in the web interface <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>, <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. The preview will show how data from the database has replaced the template placeholders <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. A watermark will be present on the free plan, but it is removed on paid plans <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
        *   **Download All**: Download all generated PDF files to your local machine <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>, <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
    *   You can download the documents multiple times if needed <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.

## Managing Connections and Subscriptions

*   **Saved Connections**: Once a connection is successfully created, it is saved. You can access it by clicking "C" (for Connections), which will display your previously created connections <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>, <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. Selecting a saved connection automatically loads its settings, allowing for quicker re-generation of documents <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.
*   **Upgrade Options**: PDFOutput offers a basic free plan with a limit (e.g., 1000 documents) <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. Once this limit is reached, you need to upgrade your subscription <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. The "Upgrade" option shows various monthly and yearly pricing plans (Pro, Enterprise) <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>, <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>. After upgrading, click "Activate subscription" to apply the new plan <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.
*   **Templates Section**: A future "Templates" section will display more pre-built templates, such as the invoice template demonstrated <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

## Customizing Templates

Users can [[using_notion_database_and_templates_for_pdf_generation | customize their own templates]] according to their specific requirements <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>. The key is to use curly braces (e.g., `{Client Name}`) for placeholder text in the template and ensure the exact same name is used as the column name in the Notion database <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. This ensures PDFOutput can automatically read and import values from the database into the template's placeholder elements <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.