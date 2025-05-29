---
title: Integrating Gmail with Notion for Invoicing
videoId: OWAAdB_hzsg
---

From: [[theaccountantguy]] <br/> 

This article details how to leverage a Notion template with automation tools to send automated invoice payment reminders to customers via Gmail. This system uses Notion for [[setting_up_notion_for_invoice_management | invoice management]] and Pabbly Connect as the no-code automation software <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

## Notion Template Structure for Invoicing

The core of this automation is a Notion database template designed for invoice tracking. This template includes the following columns:
*   **Customer Name** <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   **Email** (of the customer) <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>
*   **Invoice Details** (description of the service/product) <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>
*   **Invoice Number** <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>
*   **Invoice Amount** <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>
*   **Status** (Paid or Due) <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>
    *   "Paid" means the payment has been completed <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
    *   "Due" means the payment is still pending <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **Due Date** (of the payment) <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>
*   **Invoice** (attached as a PDF) <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>

## Automated Reminder Message

The system generates a customizable email reminder <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>, pulling specific details from the Notion database:
*   **Sender Name**: Configured in the Gmail connection <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Subject Line**: Dynamically includes the invoice number and status, e.g., "Invoice number [Invoice Number] is due soon and action is required" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Recipient**: Customer email ID from the Notion database <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Email Body**: Personalizes with the customer's name and details about the invoice:
    *   Customer name <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>
    *   Invoice number <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>
    *   Due date <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>
    *   Invoice details (e.g., "service 3") <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>
    *   Total amount (currency sign is customizable) <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>
*   **Payment Options**: Section for bank account details, Swift Code, etc., customizable for business needs <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   **Invoice Attachment**: The PDF invoice attached from the Notion database <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

## Setting Up the Automation Workflow

The automation workflow relies on three applications:
1.  **Pabbly Connect**: A no-code automation software that orchestrates the workflow <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
2.  **Notion**: The productivity app where [[tracking_invoice_payments_in_notion | invoice information is stored]] <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
3.  **Gmail**: Used to send automated payment reminders <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Step-by-Step Configuration

1.  **Create a Pabbly Connect Account**: Sign up for a free account <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
2.  **Clone the Automation Workflow**: Use the provided link to clone the pre-built invoice payment reminder automation to your Pabbly Connect dashboard <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
3.  **Enable the Workflow**: Ensure the workflow is set to "On" or "Active" in your Pabbly dashboard <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
4.  **Set Pabbly Connect Time Zone**: Go to Pabbly Connect settings and set your preferred time zone <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.
5.  **Configure Daily Trigger**:
    *   Set the trigger to run "Every Day" <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
    *   Choose a specific time for the automation to run daily (e.g., 10:00 AM) <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. This means Pabbly Connect will check the Notion database daily at the specified time for invoices with "Due" status <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
6.  **Connect Notion Database**:
    *   In the Notion step of the workflow, click "Connected" <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
    *   Click the three dots and select "Update connection" <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
    *   Check the checkbox and click "Connect with Notion" <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
    *   Select your Notion account and specifically select the invoice payment reminder database template that you copied to your workspace <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
    *   Click "Allow access" <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
    *   Disable "Simple response" and click "Save and send test request" to pull data from Notion <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.
7.  **Map Notion Fields**: Go through each subsequent step in the workflow (Iterator, Customer Name, Customer Email, Invoice Details, etc.). For each step, click "Refresh Fields" and then "Save and send test request" to ensure the data is correctly captured and mapped <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. This process only needs to be done once <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
    *   The invoice amount field will capture only the number; a subsequent step allows adding the currency symbol (e.g., dollar or euro) <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
    *   The due date format can be adjusted <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.
8.  **Connect Gmail Account**:
    *   In the Gmail step of the workflow, click "Connected" and then "Update connection" <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>.
    *   Check the checkbox and click "Connect with Gmail" <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.
    *   Select the Gmail account you want to use as the sender <a class="yt-timestamp" data-t="00:18:39">[00:18:39]</a>.
    *   Grant the necessary access <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>.
    *   Click "Refresh Fields" and then "Save and send test request" to send a test email <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.

## Functionality and Usage

Once set up, the automation will:
*   Run daily at the configured time <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   Check the Notion database (e.g., "DB - Invoice Payment Reminders") <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.
*   Identify all invoices where the "Status" is "Due" <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>.
*   For each "Due" invoice, it will automatically send an email reminder to the customer, populated with the relevant invoice details from Notion <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>.

To stop sending reminders for a paid invoice, simply change its "Status" in Notion from "Due" to "Paid" <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>.

### Important Considerations
*   **Gmail Quota**: Gmail offers a free quota of sending up to 100 emails per day <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>.
*   **Support**: If you encounter any issues during setup, you can reach out to the Pabbly Connect automation team or the provided support contact <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a>.