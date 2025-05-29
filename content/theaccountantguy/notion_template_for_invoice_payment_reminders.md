---
title: Notion template for invoice payment reminders
videoId: OWAAdB_hzsg
---

From: [[theaccountantguy]] <br/> 

This article explains how to use a Notion template to set up automated [[automating_bill_payment_reminders_using_templates | invoice payment reminders]] for customers <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. The automation utilizes Notion for data storage, Pabbly Connect as a no-code automation tool, and Gmail for sending reminders <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

## Template Overview
The Notion template for invoice payment reminders includes the following columns:
*   **Customer Name**: To enter the customer's name <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.
*   **Email**: For the customer's email address <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   **Invoice Details**: To specify details related to the invoice <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
*   **Invoice Number**: The specific number of the invoice <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   **Invoice Amount**: The total amount of the invoice <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   **Status**: Indicates if the invoice is "Paid" (payment done) or "Due" (payment pending) <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   **Due Date**: The payment due date for the invoice <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   **Invoice (PDF)**: Allows attaching the invoice as a PDF <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## Automated Reminder Message
The automated reminder message sent to customers includes dynamically pulled information from the Notion database <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>:
*   **Sender Name**: Customizable name of the sender <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Subject Line**: Includes the invoice number and states "Invoice [...] is due soon and action is required" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Recipient Email**: The customer's email ID <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Body**: Addresses the customer by name, reminds them of the due date, and provides details such as:
    *   Invoice Number <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>
    *   Purpose of Invoice (from Invoice Details) <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>
    *   Due Date <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>
    *   Total Amount <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>
*   **Customization**: The message body is customizable <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   **Payment Options**: Section for bank account details, Swift Code, and other relevant payment information, which can be customized per business needs <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   **Invoice Attachment**: The PDF invoice is attached for convenience <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

## Automation Setup with Pabbly Connect
Setting up the automation involves three main applications: Pabbly Connect (no-code automation software), Notion (for storing invoice information), and Gmail (for sending reminders) <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

### Initial Steps
1.  **Create Pabbly Connect Account**: Sign up for a free account <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
2.  **Clone Automation Setup**: Clone the pre-built automation workflow onto your Pabbly Connect dashboard <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. Ensure the workflow is set to "active" <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
3.  **Configure Time Zone**: In Pabbly Connect settings, set your preferred time zone <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### Configuring the Workflow
The automation workflow consists of several steps to connect and transfer data between Notion and Gmail via Pabbly Connect.

#### 1. Trigger (Schedule by Pabbly)
*   **Daily Trigger**: The automation is set to trigger daily at a specified time (e.g., 10:00 AM local time) <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   **Database Check**: Each day, it checks the Notion database (e.g., "db_invoice payment reminder") for any invoices with a "Due" status <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

#### 2. Notion Database Connection
*   **Connect Notion**: Link your Notion workspace to Pabbly Connect by updating the connection and selecting the specific Notion database template you're using (e.g., "db_invoice payment reminders") <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Disable Simple Response**: Before testing, ensure the "Simple Response" option is disabled <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.
*   **Test Request**: Click "Save and send test request" to pull all information from the Notion database into Pabbly Connect <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

#### 3. Mapping Data Fields
Each data field from Notion needs to be mapped in Pabbly Connect by clicking "Refresh Fields" and then "Save and send test request" for each corresponding step <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>:
*   **Customer Name**: Captures the customer's name <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
*   **Customer Email**: Captures the customer's email ID <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
*   **Invoice Details**: Captures the service details <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>.
*   **Invoice Number**: Captures the invoice number <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.
*   **Invoice Amount (Raw)**: Captures only the numerical value of the invoice amount (e.g., 150) <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
*   **Invoice Amount (Formatted)**: Formats the amount with a currency symbol (e.g., $150). You can change the currency symbol (e.g., to Euro) as needed <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
*   **Due Date (Raw)**: Captures the due date in its raw format <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.
*   **Due Date (Formatted)**: Formats the due date appropriately for the email (e.g., "February 6 2024") <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.
*   **Invoice Name**: Captures the name of the attached invoice file (e.g., "invoice 3.pdf") <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>.
*   **Invoice URL**: Captures the URL of the attached invoice <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.

#### 4. Gmail Integration
*   **Connect Gmail**: Link your Gmail account to Pabbly Connect. This will be the sender's email ID <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
*   **Send Email Action**: The action event is set to "Send Email" <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.
*   **Test Email**: Click "Save and send test request" to send a test email. An email will be sent to the customer whose invoice is in "Due" status <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.

### How the Automation Functions
Once configured, the automation runs daily <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>. It scans the Notion database for invoices marked "Due". If an invoice is due, an automated reminder email, populated with the latest information from Notion, is sent to the customer <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>. When a customer pays, simply change the invoice status in Notion to "Paid" to stop further reminders for that invoice <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>.

### Important Notes
*   **Gmail Quota**: Gmail provides a free quota of sending up to 100 emails daily <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>.
*   **Support**: For any issues during setup, you can reach out to the Pabbly Connect automation team or the video creator's support email <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a>.