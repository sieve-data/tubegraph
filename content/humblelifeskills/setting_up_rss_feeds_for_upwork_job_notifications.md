---
title: Setting up RSS feeds for Upwork job notifications
videoId: bASS0_vof0c
---

From: [[humblelifeskills]] <br/> 

To effectively [[optimizing_job_search_on_upwork_with_custom_alerts | optimize job search on Upwork]], it's beneficial to receive notifications for new job postings quickly. Upwork often sees 20-50 applicants per job, making it difficult to secure work if you apply too late <a class="yt-timestamp" data-t="01:10:17">[01:10:17]</a>. [[getting_early_job_notifications_for_freelance_work | Getting early job notifications for freelance work]] can provide a significant advantage <a class="yt-timestamp" data-t="05:54:57">[05:54:57]</a>. This article outlines a system using Upwork RSS feeds, IFTTT, and Pushover for real-time alerts.

## Upwork RSS Feeds

Upwork provides RSS feeds for job categories and search results, which automatically update every five minutes <a class="yt-timestamp" data-t="06:01:04">[06:01:04]</a>.

### Locating Your Job Feed RSS URL
1.  Navigate to your customized job feed on Upwork (e.g., "cinemagraph video editing" or "video editing") <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.
2.  Look for the triple dots icon above the main feed row <a class="yt-timestamp" data-t="02:20:24">[02:20:24]</a>.
3.  Clicking this will reveal options including "RSS" and "Atom feeds" <a class="yt-timestamp" data-t="02:24:26">[02:24:26]</a>.
4.  Right-click on "RSS feed" to copy the URL <a class="yt-timestamp" data-t="02:27:28">[02:27:28]</a>. This URL can then be subscribed to <a class="yt-timestamp" data-t="02:31:34">[02:31:34]</a>.

### Current RSS Feed Issues
As of December 1st, 2023, there have been instances where the Upwork RSS feed shows "feed not found" <a class="yt-timestamp" data-t="02:39:41">[02:39:41]</a>. This might be due to changes in how the feed is handled or security token requirements <a class="yt-timestamp" data-t="02:43:55">[02:43:55]</a>.

## [[using_ifttt_for_job_alerts_on_upwork | Using IFTTT for Job Alerts on Upwork]]

[[using_ifttt_for_job_alerts_on_upwork | IFTTT (If This Then That)]] is an automation service that can monitor RSS feeds and trigger actions based on criteria.

### Setting up an IFTTT Applet
1.  Go to your IFTTT services and applets <a class="yt-timestamp" data-t="01:45:51">[01:45:51]</a>.
2.  Create a new applet or edit an existing one. The "If This" trigger should be "New feed item matches" <a class="yt-timestamp" data-t="04:59:50">[04:59:50]</a>.
3.  Enter your desired keywords (e.g., "conference," "video editor," "cinemagraph") <a class="yt-timestamp" data-t="05:02:04">[05:02:04]</a>.
4.  Paste the Upwork RSS feed URL into the "Feed URL" field <a class="yt-timestamp" data-t="05:04:07">[05:04:07]</a>.

## [[integrating_push_notifications_with_upwork_job_feeds | Integrating Push Notifications with Upwork Job Feeds]] via Pushover

Pushover (.net) is a notification service that delivers alerts to your phone or desktop <a class="yt-timestamp" data-t="03:06:09">[03:06:09]</a>. It functions similarly to Google or Apple notifications <a class="yt-timestamp" data-t="03:13:17">[03:13:17]</a>.

### Pushover Features
*   **Platform Support**: Runs as a web client, desktop application, and mobile app <a class="yt-timestamp" data-t="03:19:22">[03:19:22]</a>.
*   **API Integration**: Connects via command line, Perl, Ruby, PHP, and other APIs <a class="yt-timestamp" data-t="03:30:37">[03:30:37]</a>.
*   **Cost**: Free to try for 7 days, then a one-time license purchase of $4.99 for unlimited messages <a class="yt-timestamp" data-t="04:04:08">[04:04:08]</a>. SMS delivery is also an option <a class="yt-timestamp" data-t="07:24:26">[07:24:26]</a>.

### Desktop Client: Pullover
While Pushover has an official desktop client, an open-source, unofficial version called "Pullover" is available and preferred by some users for its notification display <a class="yt-timestamp" data-t="04:15:18">[04:15:18]</a>. Pullover runs in the system tray (e.g., Mac's menu bar) and receives notifications automatically when logged into your Pushover account <a class="yt-timestamp" data-t="04:18:41">[04:18:41]</a>.

### Configuring Pushover in IFTTT
1.  For the "Then That" action in IFTTT, select "Send a Pushover notification" <a class="yt-timestamp" data-t="05:25:26">[05:25:26]</a>.
2.  Customize the notification details:
    *   **Title**: Entry Title <a class="yt-timestamp" data-t="05:40:42">[05:40:42]</a>
    *   **URL**: Entry URL <a class="yt-timestamp" data-t="05:41:42">[05:41:42]</a>
    *   **Content**: Entry Content <a class="yt-timestamp" data-t="05:42:42">[05:42:42]</a>
3.  Set a **Message Priority** (e.g., "emergency" for immediate, repeating alerts, or "high-bypass quiet hours" if working long shifts) <a class="yt-timestamp" data-t="06:27:36">[06:27:36]</a>.
4.  Select a **Message Sound** <a class="yt-timestamp" data-t="06:42:44">[06:42:44]</a>.
5.  Save the IFTTT applet <a class="yt-timestamp" data-t="06:44:47">[06:44:47]</a>.

This setup ensures that IFTTT scans the Upwork RSS feed 24/7, and any new job posting matching your keywords will trigger an immediate push notification to your devices via Pushover <a class="yt-timestamp" data-t="06:47:50">[06:47:50]</a>. This allows you to apply for jobs within minutes of them being posted, giving you a significant head start over other applicants <a class="yt-timestamp" data-t="06:04:05">[06:04:05]</a>.

## Fine-Tuning Your Notifications

You can create multiple Upwork job feeds based on specific keywords (e.g., "Flixel," "animation," "drone footage") to receive highly relevant notifications <a class="yt-timestamp" data-t="08:11:42">[08:11:42]</a>. This allows you to avoid constantly checking the Upwork site for all jobs and instead focus on those most relevant to your skills <a class="yt-timestamp" data-t="08:30:32">[08:30:32]</a>.

## Summary of Tools
*   **Upwork**: For job feeds and RSS URLs <a class="yt-timestamp" data-t="07:51:55">[07:51:55]</a>
*   **Pushover.net**: For notification delivery (sign up for an account) <a class="yt-timestamp" data-t="07:03:05">[07:03:05]</a>
*   **Pullover App**: (Optional) Unofficial multi-platform desktop client for Pushover <a class="yt-timestamp" data-t="07:33:40">[07:33:40]</a>
*   **IFTTT**: To connect the Upwork RSS feed with Pushover notifications <a class="yt-timestamp" data-t="07:48:48">[07:48:48]</a>