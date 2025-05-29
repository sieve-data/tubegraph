---
title: Notion invoice payment reminder setup
videoId: OWAAdB_hzsg
---

From: [[theaccountantguy]] <br/> 

This article outlines how to set up automated invoice payment reminders using a Notion template in conjunction with Pabbly Connect and Gmail <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This system automates the process of sending reminders to customers for outstanding invoices <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Overview

The core of this automation relies on a Notion database that tracks invoice details <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. Pabbly Connect, a no-code automation software, is used to connect Notion and Gmail, triggering automated email reminders when invoices are marked as "due" <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. The system can send up to 100 emails daily through Gmail's free quota <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>.

## Template Structure

The Notion template used for [[invoicing_and_payment_tracking_through_notion | invoicing and payment tracking]] includes the following columns <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>:
*   **Customer Name**: To enter the customer's name <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
*   **Email**: The customer's email address <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
*   **Invoice Details**: Specific details about the invoice <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
*   **Invoice Number**: The unique invoice identifier <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   **Invoice Amount**: The total amount of the invoice, which can be in any preferred currency <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   **Status**: Indicates whether the invoice is 'Paid' (payment done) or 'Due' (payment pending) <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   **Due Date**: The payment due date for the invoice <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   **Invoice**: A field to attach the invoice as a PDF <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Automated Reminder Message Example

The automated reminder email is customizable <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a> and dynamically pulls information from the Notion database <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
An example message includes:
*   Sender's Name <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   Subject line with Invoice Number and "due soon" notification (e.g., "Invoice Number Three is due soon and action is required") <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   Customer's email ID <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   Body text addressing the customer by name <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   Reminder of the invoice due date <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   Details like Invoice Number, Invoice Details (e.g., service provided), Due Date, and Total Amount <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   Customizable payment options (e.g., bank account details, Swift Code) <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   An attached invoice PDF <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

The message body, business details, and currency symbol for the invoice amount can all be customized <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>, <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>, <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

## Required Applications

To set up this [[customizing_invoice_reminders_in_notion | invoice reminder automation]], you will need:
*   **Pabbly Connect**: A no-code automation software to create the workflow <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **Notion**: For storing and tracking invoice information in a database <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   **Gmail**: For sending the automated payment reminders <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

## Setup Process

The setup involves three main steps within Pabbly Connect <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

### Step 1: Create Pabbly Connect Account
Create a free Pabbly Connect account <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

### Step 2: Clone Automation Workflow
A pre-built automation workflow can be cloned directly into your Pabbly Connect dashboard <a class="yt-timestamp" data-t="00:04:57">[00:05:01]</a>. Click the "Try now" button to clone the workflow <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. The workflow will appear on your dashboard, likely named "invoice payment reminder" <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### Step 3: Enable Workflow & Set Time Zone
Ensure the workflow is enabled by checking the "on" button <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
Set your specific time zone in the Pabbly Connect settings panel (e.g., GMT +5 hours 30 minutes) <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. Save the time zone setting <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

### Step 4: Configure Daily Trigger
The automation needs to be triggered daily to check for due invoices <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   In the trigger step, select "Every Day" from the schedule options <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   Set a specific time for the daily trigger (e.g., 10:00 AM local time) <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. Save the setting <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. This ensures the automation runs automatically at the set time each day <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

### Step 5: Link Notion Database
Connect your Notion database template to Pabbly Connect <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   Click "Connect" in the Notion step <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   Click the three dots, then "Update connection" <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   Check the box and click "Connect with Notion" <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
*   Select your Notion account and choose the specific Notion template (e.g., "DB - Invoice Payment Reminder") that you copied to your workspace <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
*   Click "Allow access" <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
*   Once connected, click "Update" and then "Save" <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
*   Disable the "Simple Response" option before clicking "Save and Send Test Request" <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>. This will pull all data from your Notion database into Pabbly Connect for mapping <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.

### Step 6: Configure Data Mapping (Iterator Steps)
For each subsequent step in the workflow (e.g., Customer Name, Customer Email, Invoice Details, Invoice Number, Invoice Amount, Due Date, Invoice Name, Invoice URL), perform the following:
*   Click "Refresh Fields" <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
*   Click "Save and Send Test Request" to capture the data from Notion <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
*   Click "Save" <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>.
    *   For the Invoice Amount, you can modify the currency symbol (e.g., change from dollar to Euro) in the "replace field" <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.
    *   The Due Date will be formatted appropriately for the email <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.

This process maps each piece of information from your Notion database to the corresponding fields in the automation workflow <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.

### Step 7: Connect Gmail & Send Emails
The final step is to connect your Gmail account, which will be used to send the automated reminders <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
*   In the Gmail step, ensure the action event is set to "Send Email" <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.
*   Click "Connected", then the three dots, and "Update connection" <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>.
*   Check the box and click "Connect with Gmail" <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.
*   Select the specific Gmail account you want to use as the sender <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>.
*   Grant all necessary access by clicking "Continue" <a class="yt-timestamp" data-t="00:18:54">[00:18:54]</a>.
*   Click "Update" and then "Save" <a class="yt-timestamp" data-t="00:18:59">[00:19:01]</a>.
*   Click "Refresh Fields" and then "Save and Send Test Request" <a class="yt-timestamp" data-t="00:19:07">[00:19:15]</a>. This will send a test email to the customer whose invoice is marked as "due" in your Notion database <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>.

## Usage and Maintenance

Once the automation is set up:
*   As you make changes to the [[setting_up_and_customizing_notion_database_for_invoices | Notion invoice database]], such as updating the status or due date, the automation will automatically send [[tracking_invoice_payments_in_notion | invoice payment reminders]] to customers with a "Due" status <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>.
*   When a customer pays an invoice, remember to change its status in Notion from "Due" to "Paid" <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>. This prevents further reminders from being sent for that invoice <a class="yt-timestamp" data-t="00:22:40">[00:22:40]</a>.

## Support

If you encounter any issues during setup, you can reach out to the Pabbly Connect automation team for assistance <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a>.