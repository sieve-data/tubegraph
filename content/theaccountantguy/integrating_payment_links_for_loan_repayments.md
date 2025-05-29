---
title: Integrating payment links for loan repayments
videoId: 8npw7X-61KM
---

From: [[theaccountantguy]] <br/> 

This system allows users to [[using_automated_notifications_for_loan_payments | automate loan repayment notifications]] and integrate direct payment links, primarily delivered via WhatsApp. The setup is highly [[customizing_and_configuring_loan_repayment_alerts | customizable]] for various loan types and personal preferences <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## Key Features

*   **WhatsApp Notifications** Users receive a notification on their WhatsApp account on the due date of a loan payment <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.
*   **Direct Payment Integration** The notification message includes a "pay now" button or link that redirects the user to their bank portal or a specified payment gateway (e.g., PayPal) for instant repayment <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. This link is fully customizable <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   **Customizable Alerts** The content of the debt payment reminder alert is modifiable to suit individual needs <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. For example, a reminder for a $3,000 car loan due on September 23 would state: "Hi there, this is a reminder for payment of car loan which is due on September 23 for an amount of three thousand dollars" <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
*   **Automation for Multiple Loans** The system can be automated for any number of loans a user manages <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

## Setting Up Repayment Reminders

To receive [[debt_payment_tracking_and_analysis | debt payment]] reminders on WhatsApp, the first step is to [[creating_templates_for_loan_payment_reminders | create a template]] for each loan <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

### Creating Loan Templates

1.  **Add Loan Details** Select the "new template" option and input the loan details, such as loan type (e.g., car loan) and repayment amount (e.g., $3,000) <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
2.  **Configure Repetition**
    *   Enable the "repeating template" option for each new template <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
    *   Set the repetition frequency, for example, "every month" <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
    *   Specify the exact day of the month and time for the reminder to occur (e.g., the 16th of every month at a specific time) <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This ensures the loan item is automatically added to the database <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
3.  **Adjust Notification Timing**
    *   Users can choose to receive notifications a set number of days before the actual loan due date <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. For instance, setting "7 days" will trigger a notification seven days prior to the due date <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
    *   If the notification date and the due date should be the same, simply set this value to "0" <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

Once a recurring template is set for each loan, it will automatically trigger an automation to send the payment notification message to WhatsApp each month <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

## Automation in Action

The system can automatically add new loan entries and trigger notifications. For example, if an "education loan" is set to occur at 3:55 PM on September 16, a new loan entry will automatically populate in the database at that exact time, followed by a payment alert on WhatsApp <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

## Managing Templates

After a loan has been fully repaid, users can simply delete the corresponding template to prevent further recurring notifications <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.