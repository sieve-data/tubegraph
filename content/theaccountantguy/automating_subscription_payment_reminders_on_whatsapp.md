---
title: Automating subscription payment reminders on WhatsApp
videoId: GU6dhqxW6nQ
---

From: [[theaccountantguy]] <br/> 

This guide demonstrates how to [[receiving_timely_payment_reminders_through_whatsapp | receive subscription payment reminders]] directly on WhatsApp <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The process involves [[setting_up_subscription_reminders_using_a_database | setting up these reminders through a database]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## Setting Up a New Subscription Reminder

To set up a subscription reminder alert:
1.  **Create a New Template**: Click on the dropdown menu in the database and select "create a new template" <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. You will find an option for "setting up the subscription reminder alert" <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
2.  **Specify Subscription Details**:
    *   Enter the name of the subscription, e.g., "Spotify" <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
    *   Specify the subscription amount, e.g., $150 <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
    *   Click "background" to add the new template <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
3.  **Set Repetition**:
    *   Click on the three dots next to the newly added template <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
    *   Click on "repeat" and choose the desired mode of repetition <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. For example, to [[scheduling_and_repeating_notifications_monthly | repeat every month]], select "every month" <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. This will ensure the reminder for the specified subscription and amount is sent each month <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
4.  **Specify Time and Start Date**:
    *   After selecting the repetition mode, a new window will open where you can specify the exact time and date for the reminder to start <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
    *   For example, you can set the time to 11:56 AM <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a> and set it to repeat every month on the 23rd <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
5.  **Save**: Click "Save" to finalize the settings <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. A repetition arrow will appear, indicating that the Spotify subscription reminder alert will automatically repeat every month on the 23rd at 11:56 AM <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

## How the System Works

Once the reminder is set:
*   A new line item will automatically be added to the database at the scheduled time (e.g., 11:56 AM on the 23rd of every month) <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
*   After this, a notification alert will be automatically received on WhatsApp <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   The WhatsApp notification will serve as a payment reminder for the specified amount (e.g., $150 for Spotify) <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   The message also includes a "pay now" link, allowing you to [[integrating_payment_links_with_reminder_alerts | pay the amount directly through the provided link]] <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

### Customization
The reminder alerts received on WhatsApp are fully customizable to meet individual requirements <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. There is no fixed template <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. Instructions and a guide are available upon downloading the template to help set up the automation <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

> For further questions, you can contact sanat biswal at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.