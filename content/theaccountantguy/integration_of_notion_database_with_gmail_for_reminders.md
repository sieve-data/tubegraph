---
title: Integration of Notion database with Gmail for reminders
videoId: OWAAdB_hzsg
---

From: [[theaccountantguy]] <br/> 

This guide outlines how to use a [[notion_template_setup_for_invoice_reminders]] to set up automated invoice payment reminders to customers via Gmail <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This automation workflow automatically checks the status of invoices and sends reminders when payments are due <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Notion Template Overview

The provided Notion template, named `DB - Invoice Payment Reminder`, is structured with the following columns to manage invoice details <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>:

*   **Customer Name** <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>
*   **Email** (customer's email address) <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>
*   **Invoice Details** (description of the service or product) <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>
*   **Invoice Number** <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>
*   **Invoice Amount** <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>
*   **Status**:
    *   "Paid" indicates the payment has been completed <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
    *   "Due" indicates the payment is still pending <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **Due Date** of the payment <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>
*   **Invoice** (attached as a PDF) <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>

## Automated Reminder Message Example

The automated reminder email sent to customers is customizable <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a> and includes several dynamic fields pulled directly from the Notion database <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>:

*   **Sender Name**: Visible in the email header <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Subject Line**: Includes the invoice number and states "due soon" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Recipient Email ID**: Pulled from the customer's email ID in Notion <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Greeting**: Addresses the customer by name (e.g., "Dear Customer 3") <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Invoice Details in Body**:
    *   Invoice number <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>
    *   Due date <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>
    *   Details for what the invoice was raised <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>
    *   Total amount (currency can be customized, e.g., $150 or €150) <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>
*   **Payment Options**: Section for bank account details, Swift Code, etc., which can be customized <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   **Invoice Attachment**: The PDF invoice linked in Notion is attached to the email <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   **Customizable Body**: The main text of the reminder message can be entirely customized <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

## Automation Setup Process

The automation is set up using three key applications <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>:

1.  **Pabbly Connect**: A no-code automation software that facilitates the workflow <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
2.  **Notion**: Used as the database to store all invoice information <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
3.  **Gmail**: Used to send the automated payment reminders to customers <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Steps to Configure the Automation Workflow

Follow these steps to set up the automation:

1.  **Create a Pabbly Connect Account**: Sign up for a free account <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
2.  **Clone the Automation Workflow**: Use the provided link to clone the pre-built "Invoice Payment Reminder" automation setup onto your Pabbly Connect dashboard <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
3.  **Enable the Workflow**: Ensure the workflow is set to "On" status in your Pabbly Connect dashboard for it to run <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
4.  **Set Time Zone**: In Pabbly Connect settings, configure your specific time zone (e.g., 5 hours 30 minutes GMT) and click "Save" <a class="yt-timestamp" data-t="00:06:51">[00:07:12]</a>.

### Workflow Configuration

The workflow consists of several steps within Pabbly Connect:

1.  **Trigger (Scheduler)**:
    *   This step schedules the automation to run daily <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
    *   It checks the Notion database daily for any invoices with a "Due" status <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
    *   You can set the specific time for the daily trigger (e.g., 10:00 AM) <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.

2.  **Notion (Action - Query Database Items)**:
    *   **Connect Notion Database**: Link your Notion account to Pabbly Connect <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
        *   Click "Update connection" <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>, check the box, and "Connect with Notion" <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
        *   Select the specific `DB - Invoice Payment Reminder` template from your Notion workspace <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.
        *   Click "Allow access" <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
    *   **Disable Simple Response**: Before testing, disable the "Simple Response" option in this step <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.
    *   **Save and Send Test Request**: This will pull all data from your Notion database into Pabbly Connect <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.

3.  **Data Extraction and Mapping (Iterators/Formatters)**:
    *   For each subsequent step (e.g., extracting customer name, email, invoice details, etc.), click "Refresh Fields" and then "Save and send test request" <a class="yt-timestamp" data-t="00:12:11">[00:12:22]</a>. This ensures that the automation captures the latest information from the Notion database dynamically.
    *   **Invoice Amount**: Note that the raw invoice amount is captured as a number <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>. A separate step is used to add the desired currency symbol (e.g., dollar sign `$`, Euro `€`) <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.
    *   **Due Date**: The raw due date is formatted into a readable format (e.g., "February 6, 2024") in a subsequent step <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.
    *   **Invoice Name and URL**: The name and direct URL of the attached PDF invoice are also captured <a class="yt-timestamp" data-t="00:16:35">[00:17:20]</a>.

4.  **Gmail (Action - Send Email)**:
    *   **Connect Gmail Account**: Link the Gmail account from which you want to send the reminders <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>. This will be the sender's email ID <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>.
    *   **Grant Access**: Allow Pabbly Connect the necessary access to your Gmail account <a class="yt-timestamp" data-t="00:18:54">[00:18:54]</a>.
    *   **Refresh Fields and Test**: Click "Refresh Fields" and then "Save and send test request" <a class="yt-timestamp" data-t="00:19:07">[00:19:16]</a>. This will trigger an email to the customer whose invoice is in "Due" status in your Notion database <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>.
    *   **Gmail Quota**: Gmail has a free quota of sending up to 100 emails per day <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>.

## Automation in Action

Once set up, the automation runs at the scheduled time daily <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>. Any changes made to the Notion database, such as updating customer names, invoice details, amounts, or due dates for invoices marked as "Due," will be automatically reflected in the sent email reminders <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>.

To stop sending reminders for a specific invoice, simply change its "Status" in the Notion database from "Due" to "Paid" <a class="yt-timestamp" data-t="00:22:36">[00:22:38]</a>.

## Support

If you encounter any issues setting up the workflow, you can reach out to the Pabbly Connect automation team for support <a class="yt-timestamp" data-t="00:23:02">[00:23:14]</a>.