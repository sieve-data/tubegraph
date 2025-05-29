---
title: Gmail email automation for invoices
videoId: OWAAdB_hzsg
---

From: [[theaccountantguy]] <br/> 

This article details how to set up an automated system for sending invoice payment reminders to customers via Gmail, utilizing a Notion template and Pabbly Connect. This process ensures that customers receive timely reminders for outstanding invoices <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Notion Template Structure

The core of this automation is a Notion template designed to manage invoice information <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This template includes the following columns:
*   **Customer Name** <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   **Email** (of the customer) <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>
*   **Invoice Details** (to specify what the invoice is for) <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>
*   **Invoice Number** <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>
*   **Invoice Amount** <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>
*   **Status**:
    *   "Paid" - Payment has been received <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
    *   "Due" - Payment is still pending <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **Due Date** (for the payment) <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>
*   **Invoice Attachment** (as a PDF) <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>

## Automated Email Breakdown

The automated reminder email sent to customers is customizable <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a> and includes several dynamic fields pulled directly from the Notion database:
*   **Sender Name**: Customizable name of the sender <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Subject Line**: Dynamically includes the invoice number and states "is due soon and action is required" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Customer Email ID** <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Greeting**: Addresses the customer by name, e.g., "Dear Customer 3" <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Body**: A customizable message reminding the customer that the invoice is due <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>, including:
    *   Invoice number <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>
    *   Due date <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>
    *   Invoice details (what it was raised for) <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>
    *   Total amount (with customizable currency symbol) <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>
*   **Payment Options**: Section for bank account details, Swift Code, and other relevant information <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   **Invoice Attachment**: The PDF invoice is attached for convenience <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

## Setting Up the Automation Workflow

The automation is set up using Pabbly Connect, Notion, and Gmail <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

### Required Applications
*   **Pabbly Connect**: A no-code automation software <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **Notion**: For storing and managing invoice information <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   **Gmail**: For sending the automated payment reminders <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Step-by-Step Setup
1.  **Create Pabbly Connect Account**: Sign up for a free account <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
2.  **Clone Automation Workflow**: Access a pre-built automation workflow by clicking a provided link, which clones it to your Pabbly dashboard <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
3.  **Enable Workflow**: Ensure the workflow is enabled (status set to "on" or "active") in your Pabbly dashboard <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
4.  **Configure Time Zone**: In Pabbly settings, set the time zone to your local requirement <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
5.  **Set Up Daily Trigger**:
    *   The automation is scheduled to run daily <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
    *   Select "Every Day" from the schedule options <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
    *   Set the desired time for the automation to run, e.g., 10:00 AM <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.
6.  **Connect Notion Database**:
    *   Link your Notion database (e.g., "db_invoice payment reminder") to Pabbly <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
    *   Update the connection, select the Notion account, and specifically choose the invoice template from your Notion workspace to grant access <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
    *   Disable "Simple Response" before sending a test request <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.
    *   Click "Save and Send Test Request" to retrieve data from Notion <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
7.  **Map Notion Data Fields**:
    *   For each subsequent step (Iterator, Customer Name, Email, Invoice Details, etc.), click "Refresh Fields" and then "Save and Send Test Request" <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>. This maps the data from Notion to the automation workflow.
    *   The [[notion_invoice_payment_reminder_setup|Notion invoice payment reminder setup]] ensures customer name <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>, email <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>, invoice details <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>, invoice number <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>, invoice amount (raw number and formatted with currency) <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>, due date (raw and formatted) <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>, invoice name <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>, and invoice URL are correctly captured <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.
8.  **Connect Gmail**:
    *   In the Gmail action step, click "Connected" and "Update Connection" <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>.
    *   Select the Gmail account you wish to use as the sender for the invoice reminders <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>.
    *   Grant access to Pabbly Connect <a class="yt-timestamp" data-t="00:18:54">[00:18:54]</a>.
    *   Click "Save and Send Test Request" to send a test email <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.

## How the Automation Functions

Once set up, Pabbly Connect runs daily at the specified time <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. It queries the Notion database to find any invoices with a "Due" status <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. For each invoice marked "Due", it automatically sends a customized payment reminder email to the corresponding customer using Gmail <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>.

### Managing Invoice Status
*   When a customer pays an invoice, simply update its status in the Notion database from "Due" to "Paid" <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>. This will prevent further automated reminders from being sent for that specific invoice <a class="yt-timestamp" data-t="00:22:40">[00:22:40]</a>.
*   You can continue to add new invoices to the Notion database, setting their status as "Due" for automated reminders to be sent <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>.

Gmail provides a free quota of 100 emails per day for this automation <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>.

## Troubleshooting and Support

If you encounter any issues during the setup process, Pabbly Connect's support team is available to assist <a class="yt-timestamp" data-t="00:23:07">[00:23:07]</a>. Support email IDs are provided to help with any workflow configuration challenges <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>.