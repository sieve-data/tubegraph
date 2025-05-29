---
title: Using P Connect for Invoice Automation
videoId: OWAAdB_hzsg
---

From: [[theaccountantguy]] <br/> 

This article outlines how to set up automated invoice payment reminders using a [[Setting up Notion for Invoice Management | Notion]] template, [[Automating notifications with Pabbly Connect | Pabbly Connect]], and Gmail <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This automation workflow automatically checks for due invoices and sends reminders to customers <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Core Applications for Automation

The automation workflow relies on three key applications <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>:
*   **[[Automating notifications with Pabbly Connect | Pabbly Connect]]**: A no-code automation software that orchestrates the entire workflow <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **[[Setting up Notion for Invoice Management | Notion]]**: A note-taking and productivity application used to store all invoice-related information <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   **Gmail**: Utilized for sending automated payment reminders to customers <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

## [[Setting up Notion for Invoice Management | Notion]] Template Structure

The provided [[Setting up Notion for Invoice Management | Notion]] template, named 'db_invoice payment reminders', includes the following columns to manage invoice data <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>:
*   **Customer Name**: To enter the customer's full name <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.
*   **Email**: The customer's email address <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   **Invoice Details**: Specific details about the invoice <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
*   **Invoice Number**: The unique identifier for the invoice <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   **Invoice Amount**: The total amount due for the invoice <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   **Status**: Indicates whether the invoice is 'Paid' (payment done) or 'Due' (payment pending) <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. The automation triggers reminders only for invoices with a 'Due' status <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   **Due Date**: The payment due date for the invoice <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   **Invoice**: A field to attach the invoice as a PDF document <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## Automated Email Reminders

The system generates automated email reminders with dynamic content pulled directly from the [[Setting up Notion for Invoice Management | Notion]] database <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   **Sender**: Customizable sender name <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Subject Line**: Includes the invoice number and a 'due soon' alert (e.g., "Invoice number three is due soon and action is required") <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Email Body**:
    *   Personalized greeting using the customer name <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
    *   Reminders of the invoice number and due date <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
    *   Detailed invoice information: invoice number, service details, due date, and total amount (with customizable currency symbols) <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
    *   Customizable message encouraging prompt payment <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
    *   Section for payment options (e.g., bank account details, Swift Code) <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
    *   Attachment of the invoice PDF for convenience <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   The entire message body is fully customizable to suit specific business requirements <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

## Setting Up the Automation Workflow

Setting up the automation involves three main steps within [[Automating notifications with Pabbly Connect | Pabbly Connect]] <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>:

### Step 1: Create a [[Automating notifications with Pabbly Connect | Pabbly Connect]] Account
*   Sign up for a free account on [[Automating notifications with Pabbly Connect | Pabbly Connect]] through the provided link <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

### Step 2: Clone the Automation Workflow
*   Once logged in, clone the pre-built invoice payment reminder automation onto your [[Automating notifications with Pabbly Connect | Pabbly Connect]] dashboard <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   Ensure the workflow is set to 'active' status by toggling the 'on' button <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
*   Adjust your time zone in the [[Automating notifications with Pabbly Connect | Pabbly Connect]] settings to ensure accurate scheduling <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

### Step 3: Configure the Workflow in [[Automating notifications with Pabbly Connect | Pabbly Connect]]

#### 1. Trigger Setup (Daily Check)
*   The automation is configured to trigger daily <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   You can set the specific time for the daily trigger (e.g., 10:00 a.m.) <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. This ensures that [[Automating notifications with Pabbly Connect | Pabbly Connect]] checks the [[Setting up Notion for Invoice Management | Notion]] database every day for invoices with a 'Due' status <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

#### 2. Connect [[Setting up Notion for Invoice Management | Notion]] Database
*   Link your [[Setting up Notion for Invoice Management | Notion]] database (e.g., 'db_invoice payment reminders') to [[Automating notifications with Pabbly Connect | Pabbly Connect]] <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   Update the connection by selecting the appropriate [[Setting up Notion for Invoice Management | Notion]] workspace and database <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   Disable 'Simple Response' before clicking 'Save and send test request' to ensure all information is captured <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.
*   Refresh fields and save connections for all Notion data points (Customer Name, Email, Invoice Details, Invoice Number, Invoice Amount, Due Date, Invoice Name, Invoice URL) within the workflow <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.
    *   For **Invoice Amount**, the raw number is captured first, then a separate step allows adding a currency symbol (e.g., '$', '€') <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
    *   For **Due Date**, the format is modified to be more readable in the email (e.g., "February 6 2024") <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.

#### 3. Connect Gmail
*   Connect your Gmail account to [[Automating notifications with Pabbly Connect | Pabbly Connect]] <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>. This will be the sender's email ID <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>.
*   Grant necessary access permissions <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.
*   Click 'Save and send test request' to send a test email based on a 'Due' invoice in your [[Setting up Notion for Invoice Management | Notion]] database <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.

### Gmail Quota
*   Gmail provides a free quota of sending up to 100 emails daily through this automation <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>.

## Managing Invoice Status
*   Once a customer pays an invoice, it is crucial to change its status in the [[Setting up Notion for Invoice Management | Notion]] database from 'Due' to 'Paid' <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>. This prevents the system from sending any further automated reminders for that specific invoice <a class="yt-timestamp" data-t="00:22:40">[00:22:40]</a>.

## Support
For any issues with setting up the workflow, users can reach out to the [[Automating notifications with Pabbly Connect | Pabbly Connect]] automation team <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a>.