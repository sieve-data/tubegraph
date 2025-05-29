---
title: Customizing payment alert messages
videoId: 8npw7X-61KM
---

From: [[theaccountantguy]] <br/> 

Sanam Biswal, also known as The Accountant Guide, demonstrates how to set up and [[setting_up_whatsapp_subscription_payment_reminders | customize WhatsApp debt payment reminders]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. These reminders provide a notification on the loan payment due date <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Components of a Customized Alert Message

The debt payment reminder alert is designed to be easily understandable and actionable <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
A typical message includes:
*   A greeting <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
*   The type of loan (e.g., car loan) <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
*   The due date for payment (e.g., September 23) <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   The total amount due (e.g., $3,000) <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
*   An integrated payment link, such as a "pay now" button, which redirects to a bank or payment portal (e.g., PayPal) for instant repayment <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. Any relevant payment link can be added <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

The message is completely modifiable and can be used for various purposes <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. Users can also create a [[customizing_subscription_reminder_alerts | custom message]] as per their requirements <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

## Setting Up Custom Payment Reminders

To receive these debt payment reminders, the first step is to [[creating_templates_for_recurring_payment_reminders | create a template]] for each loan <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

### Creating a New Template
1.  **Access Template Options**: Click on the dropdown menu and select the "new template" option <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
2.  **Enter Loan Details**: Input specific loan information such as the loan type (e.g., car loan) and the repayment amount (e.g., $3,000) <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

### Setting Up Recurring Reminders
After creating a template, an option for "repeating this template" becomes available <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   **Repetition Frequency**: Set the repetition on a monthly basis to ensure the information populates the database each month <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   **Specific Repetition Date**: Choose a specific date in the month (e.g., 16th) and a specific time for the line item to be added to the database automatically <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This acts as the notification date <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### Adjusting Notification Timing
The system allows for flexibility in when the notification is received relative to the actual due date <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   **Early Notification**: To receive a notification a certain number of days before the due date (e.g., 7 days prior), input the desired number of days <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. This will adjust the notification date while retaining the original due date in the message <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **On-Due-Date Notification**: If the notification date should be the same as the due date, set the offset to '0' <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

The essential step is to set a [[creating_recurring_payment_reminders | recurring template]] for each loan <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. Once this is done, the loan information will repeat on the specified schedule, automatically triggering an [[automating_payment_reminder_alerts_using_databases | automation]] that sends the payment notification message to WhatsApp <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. This process can be [[automating_payment_reminder_alerts_using_databases | automated]] for any number of loans <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

## Managing Templates
Once a loan has been repaid, users can delete the corresponding template to prevent further recurring notifications <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.