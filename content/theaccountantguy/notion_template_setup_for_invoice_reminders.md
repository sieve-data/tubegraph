---
title: Notion template setup for invoice reminders
videoId: OWAAdB_hzsg
---

From: [[theaccountantguy]] <br/> 

This article details how to use a Notion template to automate invoice payment reminders for customers, leveraging [[notion_templates_and_automation_features | Notion's template]] and automation capabilities <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This setup helps in [[automating_invoice_payment_reminders_using_notion | automating invoice payment reminders using Notion]] for efficient financial management.

## Invoice Reminder Template Columns

The template used for this automation includes several columns to manage invoice information <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>:
*   **Customer Name** <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   **Email** of the customer <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>
*   **Invoice Details** to specify related information <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>
*   **Invoice Number** <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>
*   **Invoice Amount** <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>
*   **Status** of the invoice:
    *   "Paid" indicates payment has been made <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
    *   "Due" indicates payment is still pending <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **Due Date** of the payment <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>
*   **Invoice (PDF)**: An attached PDF of the invoice <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

This [[using_notion_for_invoice_template_creation | Notion template for invoice creation]] allows for [[creating_professional_invoices_using_notion | creating professional invoices using Notion]] and managing their status.

## Automated Reminder Message Example

The automated reminder message is customizable and pulls specific data from the Notion database <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. An example message includes:
*   Sender Name <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   Subject Line: "Invoice [Invoice Number] is due soon and action is required" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   Customer Email ID <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   Body:
    *   Greeting with Customer Name <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
    *   Reminder of Invoice Number and Due Date <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
    *   Detailed invoice information: Invoice Number, service description (Invoice Details), Due Date, and Total Amount <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
    *   The invoice amount can be set to any preferred currency <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
    *   Payment options (bank account details, Swift Code) can be customized <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
    *   An attached invoice PDF, e.g., "Invoice 3.pdf" <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

## Automation Setup Overview

This automation workflow requires three applications <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>:
1.  **Pabbly Connect**: A no-code automation software to set up the workflow <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
2.  **Notion**: The note-taking and productivity app used to store all invoice information <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
3.  **Gmail**: Used to send the automated payment reminders to customers <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Step-by-Step Configuration

1.  **Create a Pabbly Connect Account**: Sign up for a free account <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
2.  **Clone the Automation Workflow**: Access a pre-built automation clone for invoice payment reminders and add it to your Pabbly dashboard <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
3.  **Enable the Workflow**: Ensure the automation workflow is set to "On" or "Active" status in Pabbly Connect <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
4.  **Set Time Zone**: In Pabbly Connect settings, adjust the time zone to your specific location <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
5.  **Schedule the Trigger**: Configure the automation to trigger daily, checking the database for invoices with a "Due" status <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. The time of day for this trigger can be customized <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
6.  **Connect Notion Database**: Link the Notion database (e.g., "DB - Invoice Payment Reminder") to Pabbly Connect <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
    *   Update the connection and allow Pabbly Connect access to your Notion workspace and the specific template <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
    *   Disable "Simple Response" before saving and sending a test request to capture all data <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.
7.  **Configure Data Mapping**: Map Notion fields to Pabbly Connect for accurate data capture <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>:
    *   **Customer Name**: Refresh fields and save <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.
    *   **Customer Email**: Refresh fields and save <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
    *   **Invoice Details**: Refresh fields and save <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>.
    *   **Invoice Number**: Refresh fields and save <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.
    *   **Invoice Amount (Raw)**: Captures only the numerical value. Refresh fields and save <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
    *   **Invoice Amount (Formatted)**: Add a currency symbol (e.g., "$", "€") to the raw amount. Refresh fields and save <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.
    *   **Due Date (Raw)**: Captures the date as is. Refresh fields and save <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.
    *   **Due Date (Formatted)**: Transforms the date into a desired format (e.g., "February 6, 2024"). Refresh fields and save <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.
    *   **Invoice Name**: Captures the name of the attached PDF (e.g., "Invoice 3.pdf"). Refresh fields and save <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>. This contributes to [[using_notion_templates_for_invoice_pdfs | using Notion templates for invoice PDFs]].
    *   **Invoice URL**: Captures the direct link to the attached invoice. Refresh fields and save <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>. This is part of [[using_a_notion_database_and_templates_to_create_pdf_invoices | using a Notion database and templates to create PDF invoices]].
8.  **Connect Gmail**: Link your desired Gmail account from which reminders will be sent <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>. This will be the sender's email ID <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>.
    *   Grant Pabbly Connect access to your Gmail account <a class="yt-timestamp" data-t="00:18:54">[00:18:54]</a>.
    *   Refresh fields and save the connection <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>.
9.  **Test and Run Automation**: Click "Save and Send Test Request" to verify the setup. The system will check the database for "Due" invoices and send an email to the corresponding customer <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.

## Key Features and Benefits

*   **Daily Checks**: The automation runs daily at a specified time to identify due invoices <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   **Automatic Reminders**: Sends automated [[using_notion_for_bill_reminders | bill reminders]] via email to customers with due invoices <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>.
*   **Customization**: The reminder message, currency, and other details are fully customizable <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   **Gmail Quota**: Gmail provides a free quota of 100 emails per day for automation <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>.
*   **Status Update**: Once a customer pays, updating the invoice status to "Paid" in Notion will stop further reminders for that invoice <a class="yt-timestamp" data-t="00:22:35">[00:22:35]</a>.

This setup offers a comprehensive [[notion_finance_templates | Notion finance template]] solution for managing and automating invoice payment reminders.

## Support

If you encounter any issues while setting up this workflow, you can reach out to the Pabbly Connect automation team for support. Support email IDs may be provided in the video description <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a>.