---
title: Automating loan payment notifications
videoId: 8npw7X-61KM
---

From: [[theaccountantguy]] <br/> 

This article outlines a method to [[setting_up_debt_payment_reminders_on_whatsapp | set up debt payment reminders]] that arrive as notifications on WhatsApp <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The system provides an alert on the loan's due date <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a> and can be fully customized for various purposes <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## How it Works

The system sends a notification message, such as "Hi there, this is a reminder for payment of [Loan Type] which is due on [Date] for an amount of [Amount]" <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. These messages can also include a "pay now" link that redirects to a bank portal (e.g., PayPal) for instant repayment <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. Any payment link can be added <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Setting Up Reminders

To receive debt payment reminders on WhatsApp, the primary step is to [[using_templates_for_loan_reminders | create a template for each loan]] <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

### Creating a Loan Template

1.  Access the template creation option from a drop-down menu <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
2.  Input loan details, such as the loan type (e.g., "car loan") and repayment amount (e.g., $3000) <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

### Setting Recurring Reminders

For [[recurring_bill_payment_reminders | recurring bill payment reminders]], each new template can be set to repeat <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. Repetition automatically populates values within the template for a specified period <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

1.  **Frequency**: Set the repetition on a monthly basis to receive information each month <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
2.  **Date and Time**: Select a specific day of the month (e.g., 16th) and a specific time and time zone for the reminder to occur <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
3.  Upon saving, this line item will automatically be added to the database every month on the chosen date <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

### Adjusting Notification Timing

Notifications can be set to arrive a certain number of days before the actual due date <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. For example, by typing "7" in the "days" field, a notification will be received seven days prior to the loan's due date <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Setting this value to "0" will result in the notification date being the same as the due date <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Automation Trigger

Once a recurring template's line item is added to the database each month, it automatically triggers an automation that sends the payment notification message to WhatsApp <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. This process can be automated for any number of loans <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

## Customization and Management

*   **[[customizing_payment_reminder_messages | Custom messages]]** can be created according to user requirements <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   Once a loan is repaid, the corresponding template can be deleted to prevent further repetitions and notifications <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

For detailed instructions and further information, refer to the video provided upon template download <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

For any questions, contact Sanam Biswal, also known as the accountant guide, at notionformyuser@gmail.com <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>, <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.