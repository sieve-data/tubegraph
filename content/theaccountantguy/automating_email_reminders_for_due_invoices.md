---
title: Automating Email Reminders for Due Invoices
videoId: OWAAdB_hzsg
---

From: [[theaccountantguy]] <br/> 

This article details how to set up an automated system for sending invoice payment reminders to customers using Notion and [[using_p_connect_for_invoice_automation | P Connect]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. The entire process is designed for automation, ensuring reminders are sent without manual intervention <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Template Overview: Notion Database for Invoices

The system utilizes a Notion template to manage invoice information <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This template includes several key columns:
*   **Customer Name**: To enter the customer's name <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
*   **Email**: The customer's email address <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
*   **Invoice Details**: Specific information related to the invoice, such as the service provided <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
*   **Invoice Number**: The unique identifier for the invoice <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   **Invoice Amount**: The total amount due <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. The currency can be customized <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.
*   **Status**: Indicates whether the invoice is 'Paid' or 'Due' <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. If the status is 'Due', the payment is pending <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Once a customer pays, changing the status to 'Paid' stops further reminders <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a>.
*   **Due Date**: The payment due date for the invoice <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   **Invoice PDF**: An option to attach the invoice as a PDF <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Automated Reminder Message Content

The automated email reminder includes dynamic fields pulled directly from the Notion database <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>:
*   **Sender Name**: Customizable <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>.
*   **Subject Line**: Includes the invoice number and states it's "due soon and action is required" <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.
*   **Recipient Email ID**: Automatically pulled from the Notion database <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.
*   **Body Message**: Begins with a personalized greeting including the customer's name <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>. It reminds the customer that the invoice is due for payment by a specific date <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a>.
*   **Invoice Details in Body**: Lists the invoice number, details (e.g., service provided), due date, and total amount <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>.
*   **Call to Action**: Kindly requests prompt payment to maintain service levels <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>. This message is entirely customizable <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>.
*   **Payment Options**: Section for bank account details, Swift Code, and other relevant payment information, which can be customized per business needs <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>.
*   **Invoice Attachment**: The PDF invoice attached to the Notion entry is also attached to the email for convenience <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>.

## Setting Up the Automation Workflow

The [[using_p_connect_for_invoice_automation | P Connect]] workflow orchestrates the entire automation <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>. It requires three applications:
1.  **[[using_p_connect_for_invoice_automation | P Connect]]**: A no-code automation software to set up the workflow <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>.
2.  **Notion**: For storing all invoice-related information <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>.
3.  **Gmail**: For sending automated payment reminders <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>.

### Step-by-Step Configuration

1.  **Create a [[using_p_connect_for_invoice_automation | P Connect]] Account**: Sign up for a free account <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>.
2.  **Clone the Automation Workflow**: Access and clone the pre-built automation setup onto your [[using_p_connect_for_invoice_automation | P Connect]] dashboard <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>. Ensure the workflow is set to 'Active' status <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>.
3.  **Configure [[using_p_connect_for_invoice_automation | P Connect]] Settings**:
    *   Go to the settings panel in your [[using_p_connect_for_invoice_automation | P Connect]] dashboard <a class="yt-timestamp" data-t="06:49:00">[06:49:00]</a>.
    *   Set the time zone to your preferred location <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>.
4.  **Set up the Daily Trigger**:
    *   The automation is scheduled to trigger daily at a specified time (e.g., 10:00 a.m. local time) <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>.
    *   Each day, [[using_p_connect_for_invoice_automation | P Connect]] checks the Notion database for invoices with a 'Due' status <a class="yt-timestamp" data-t="07:40:00">[07:40:00]</a>.
5.  **Connect Notion Database**:
    *   Link your Notion database (e.g., `db_invoice payment reminder`) to [[using_p_connect_for_invoice_automation | P Connect]] <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>.
    *   Update the connection, select your Notion account, and allow access to the specific template where your invoice data is stored <a class="yt-timestamp" data-t="10:02:00">[10:02:00]</a>.
    *   Disable 'Simple Response' before saving and sending a test request to capture all database information <a class="yt-timestamp" data-t="11:49:00">[11:49:00]</a>.
6.  **Map Notion Fields**:
    *   Go through each field in the workflow (e.g., Customer Name, Customer Email, Invoice Details, Invoice Number, Invoice Amount, Due Date, Invoice Name, Invoice URL) <a class="yt-timestamp" data-t="12:33:00">[12:33:00]</a>.
    *   For each field, click 'Refresh Fields' and then 'Save and send test request' to ensure [[using_p_connect_for_invoice_automation | P Connect]] correctly captures the data from Notion <a class="yt-timestamp" data-t="12:36:00">[12:36:00]</a>. This mapping only needs to be done once <a class="yt-timestamp" data-t="14:11:00">[14:11:00]</a>.
    *   For invoice amount, the system separates the numerical value from the currency symbol, allowing for customization of the currency <a class="yt-timestamp" data-t="14:26:00">[14:26:00]</a>.
    *   The due date format is also adjusted for readability in the email <a class="yt-timestamp" data-t="16:06:00">[16:06:00]</a>.
7.  **Connect Gmail**:
    *   Connect your Gmail account from which reminders will be sent <a class="yt-timestamp" data-t="18:10:00">[18:10:00]</a>. This will be the sender's email ID <a class="yt-timestamp" data-t="18:34:00">[18:34:00]</a>.
    *   Select the appropriate Gmail account and grant necessary access <a class="yt-timestamp" data-t="18:46:00">[18:46:00]</a>.
    *   Gmail offers a free quota of 100 emails per day for this automation <a class="yt-timestamp" data-t="19:52:00">[19:52:00]</a>.

Once configured, the system will automatically send [[automating_payment_reminder_alerts_using_databases | payment reminder alerts]] for all invoices listed with a 'Due' status in Notion, pulling all relevant and customized details into the email <a class="yt-timestamp" data-t="22:28:00">[22:28:00]</a>. This streamlines the process of ensuring [[benefits_of_automated_payment_reminders_for_timely_payments | timely payments]] from customers <a class="yt-timestamp" data-t="03:02:44">[03:02:44]</a>.

> [!TIP]
> If you encounter any issues during setup, [[using_p_connect_for_invoice_automation | P Connect]]'s automation team can provide support <a class="yt-timestamp" data-t="23:07:00">[23:07:00]</a>.