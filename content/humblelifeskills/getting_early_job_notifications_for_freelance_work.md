---
title: Getting early job notifications for freelance work
videoId: bASS0_vof0c
---

From: [[humblelifeskills]] <br/> 

Finding freelance work on platforms like Upwork can be challenging due to high competition <a class="yt-timestamp" data-t="01:10:10">[01:10:10]</a>. Many job postings receive 20 to 50 proposals, making it difficult to get a response or secure a job <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. To gain a competitive edge, freelancers can [[optimizing_job_search_on_upwork_with_custom_alerts | set up custom alerts]] to receive notifications for new job postings quickly <a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>.

## The Upwork Job Search Challenge

When actively searching for jobs on Upwork, users typically have to visit the site daily to look for new opportunities <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>. Jobs that are older or have many proposals can be harder to secure <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>. For example, a social media marketer position was viewed by the client a day ago and had 5 to 10 proposals without any interviews, highlighting the need for faster application <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>.

## Automated Notification System Overview

An effective way to get a head start on job applications for [[earning_money_through_online_platforms | earning money through online platforms]] is to set up an automated system that sends alerts when new, relevant jobs are posted <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>. This system involves:
1.  Utilizing Upwork's RSS feeds for job categories <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>.
2.  Using [[using_ifttt_for_job_alerts_on_upwork | IFTTT]] (If This Then That) to monitor these feeds for specific keywords <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>.
3.  Sending [[integrating_push_notifications_with_upwork_job_feeds | push notifications]] via Pushover to a desktop or mobile device <a class="yt-timestamp" data-t="03:06:00">[03:06:06]</a>.

## Accessing Upwork RSS Feeds

Upwork provides RSS feeds for specific job searches and categories, which update every five minutes <a class="yt-timestamp" data-t="05:59:00">[05:59:00]</a>.

To find the RSS feed for a specific job category or saved search:
1.  Navigate to your job feeds on Upwork <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>.
2.  Look for the triple dots icon next to the feed title <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.
3.  Clicking on the dots will reveal options including "RSS" and "Atom feeds" <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>.
4.  Right-click on "RSS feed" to copy the URL <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>. This URL provides an RSS feed of all jobs in that category <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>.

### Note on RSS Feed Accessibility
As of December 1st, there have been instances where Upwork's RSS feeds show "feed not found" or require a security token for access <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>. This may indicate changes in how Upwork handles feeds, possibly related to updated security tokens <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>.

## Setting Up IFTTT Applets for Job Alerts

[[using_ifttt_for_job_alerts_on_upwork | IFTTT]] (If This Then That) is a service that allows you to create automated actions based on specific triggers.

### Creating an IFTTT Applet:
1.  Log in to IFTTT and go to your applets <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.
2.  Create a new applet or edit an existing one <a class="yt-timestamp" data-t="04:55:00">[04:55:00]</a>.
3.  Set the trigger ("If This") to "New feed item matches" <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>.
4.  Enter desired keywords (e.g., "conference", "video editor", "cinemagraph") <a class="yt-timestamp" data-t="05:02:00">[05:02:00]</a>.
5.  Paste the copied Upwork RSS feed URL into the "Feed URL" field <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>.
6.  Set the action ("Then That") to "Send a Pushover notification" <a class="yt-timestamp" data-t="05:24:00">[05:24:00]</a>.
7.  Configure the Pushover notification details. It automatically pulls the entry title, URL, and content from the RSS feed to create the message <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>.
8.  Choose a message priority (e.g., "emergency", "high"), set repeat intervals, or bypass quiet hours if needed <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>. You can also select a custom message sound <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a>.
9.  Save the applet. It will run 24/7, scanning the RSS feed for new items matching your keywords and sending notifications <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>.

## Pushover for Instant Notifications

Pushover.net is a notification service that delivers alerts to your phone or desktop <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>. It functions similarly to Google or Apple notifications <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>.

### Pushover Features:
*   **Multi-Platform:** Available as a web client, desktop application, and mobile app <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>.
*   **API Connectivity:** Can be connected using command line, Perl, Ruby, or PHP for programmers <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>.
*   **Cost:** Free to try for 7 days, then requires a one-time license purchase of $4.99 for unlimited notifications <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>. There is also an option for SMS delivery <a class="yt-timestamp" data-t="07:22:00">[07:22:00]</a>.

For desktop notifications, an unofficial, open-source client called **Pullover** is recommended <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>. Pullover sits in your system tray (e.g., Mac bar) and receives notifications from your Pushover account <a class="yt-timestamp" data-t="04:18:00">[04:18:00]</a>. This client is often preferred over Pushover's official desktop browser version for its direct notification pop-ups <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>.

## Benefits of Early Notifications

The primary benefit of this system is getting in early on job applications <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a>. If a new job for a "Video Editor" is posted and hits the RSS feed, which updates every five minutes, you will receive a notification within that timeframe <a class="yt-timestamp" data-t="05:59:00">[05:59:00]</a>. This gives you a significant head start over other applicants, increasing your chances of securing the job, especially if the client is in urgent need of a freelancer <a class="yt-timestamp" data-t="06:05:00">[06:05:00]</a>.

## Fine-Tuning Keywords

To make the notifications even more relevant, you can [[setting_up_rss_feeds_for_upwork_job_notifications | set up RSS feeds]] for very specific keywords or recent searches <a class="yt-timestamp" data-t="07:58:00">[07:58:00]</a>. For example, instead of a broad "cinemagraph" search, you might look for "flixel", "animation", or "drone footage" if those are your specialties <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>. This allows you to drill down into highly specific job requirements and only receive alerts for opportunities that are truly relevant to your skills <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>.