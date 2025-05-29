---
title: Creating templates for loan payment reminders
videoId: 8npw7X-61KM
---

From: [[theaccountantguy]] <br/> 

This article demonstrates how to [[setting_up_automated_debt_payment_reminders_on_whatsapp | set up debt payment reminders that arrive as WhatsApp notifications]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. These notifications alert users on the loan payment due date <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## How Debt Payment Reminders Work

An example scenario involves a car loan of $3,000 due on September 23 <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. The system sends a message similar to this:
> Hi there, this is a reminder for payment of car loan which is due on September 23 for an amount of three thousand dollars. <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>

This message includes a "Pay Now" button, which, when clicked, redirects the user to their bank portal or a specified payment link (e.g., PayPal) to instantly repay the loan <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. Any relevant payment link can be added <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. This feature is an example of [[integrating_payment_links_for_loan_repayments | integrating payment links for loan repayments]] and [[integrating_payment_links_with_reminder_alerts | integrating payment links with reminder alerts]].

## Creating and Customizing Reminder Templates

To receive debt payment reminders on WhatsApp, the first step is to [[creating_and_customizing_reminder_templates | create a template for each loan]] <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. These templates are fully customizable <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

### Steps to Create a Template

1.  **Select "New Template"**: Click on the drop-down menu and select the "new template" option <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
2.  **Enter Loan Details**: Input details such as the loan type (e.g., car loan) and the repayment amount (e.g., $3,000) <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
3.  **Set Repetition**: For each new template, there is an option to set repetition <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. This automatically populates all values within the template for a specific period <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
    *   Choose a monthly repetition <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
    *   Specify the day of the month for the repetition (e.g., 16th) <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
    *   Set a specific time for the entry to be added to the database <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
4.  **Save Information**: Save the template after configuring repetition settings <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

### Configuring Notification Timing

Users can [[customizing_and_configuring_loan_repayment_alerts | customize the timing of notifications]] relative to the actual due date <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. For example, to receive a notification 7 days before the due date, enter '7' in the 'days' field <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. If the notification date and due date should be the same, enter '0' <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

## Automation and Management

Once a recurring template is set for each loan, it will automatically trigger an automation <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. This automation sends the debt payment notification message to WhatsApp <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. The system supports [[using_automated_notifications_for_loan_payments | automated notifications for any number of loans]] <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. For example, an education loan template can be set up to automatically add a new entry to the database, triggering a WhatsApp payment alert <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

After a loan has been repaid, users can simply delete the corresponding template to prevent further repetitions and notifications <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.