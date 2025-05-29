---
title: Using IFTTT for job alerts on Upwork
videoId: bASS0_vof0c
---

From: [[humblelifeskills]] <br/> 

Manually checking Upwork for new job postings can be inefficient due to the high volume of applicants. Many jobs can accumulate 20 to 50 proposals, making it challenging to receive a response or secure the position <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. A key to successfully landing jobs is to apply early <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

## Automation for Job Search
A system can be set up to send alerts for new job postings that match specific criteria <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This system leverages Upwork's RSS feeds, [[IFTTT for job alerts on Upwork | IFTTT]], and a notification service called Pushover.net.

### Upwork RSS Feeds
Upwork provides RSS feeds for custom job searches and categories <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. To access an RSS feed for a specific job feed category (e.g., "cinemagraph video editing recommended" or "video editing"), click the triple dots next to the feed row and select "RSS feed" <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. This generates a URL for that specific feed <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

*Note: As of December 1st (at the time of the recording), there was an issue where the RSS feed URL might show "feed not found," possibly due to a change in security tokens or passwords, preventing direct access without an updated token <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>, <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.*

### IFTTT Integration
[[getting_early_job_notifications_for_freelance_work | IFTTT (If This Then That)]] is used to monitor the Upwork RSS feed for new items that match specific keywords <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

**Setup in IFTTT:**
1.  Go to "My Applets" in IFTTT <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
2.  Create a new applet with the trigger "RSS Feed: New feed item matches specific keyword" <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>, <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
3.  Enter the desired keyword (e.g., "conference", "video editor", "cinemagraph", "webmaster", "keynote") <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>, <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
4.  Provide the Upwork RSS feed URL <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
5.  For the "Then That" action, select "Pushover: Send a notification" <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>, <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
    *   This action automatically populates with details like "EntryTitle," "EntryUrl," and "EntryContent" from the RSS feed <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>, <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
    *   Customize message priority (e.g., "emergency," "high," "normal") and message sound <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>, <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
    *   Emergency priority can be set to repeat every 30 seconds until acknowledged and bypass quiet hours <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
6.  Save the applet <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. The IFTTT applet will run 24/7, scanning the RSS feed for new items matching the keyword and sending notifications <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

### Pushover.net for Notifications
Pushover.net is a notification service similar to Google or Apple notifications for phones and desktops <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>, <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. It can be connected via command line, Perl, Ruby, or PHP APIs <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

**Using Pushover.net:**
1.  **Sign up for an account** on Pushover.net <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. It offers a free trial for seven days, after which a one-time license can be purchased for $4.99 <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>, <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
2.  **Download a client app:**
    *   Pushover offers a desktop browser version, but for pop-up notifications, a dedicated desktop client is preferred <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
    *   The unofficial open-source client called "Pullovert" is recommended for multi-platform desktop use <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>, <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
    *   Pullovert sits in the system tray (e.g., Mac bar) and displays notifications received by the Pushover account <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>, <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

### Benefits of this System
This setup provides [[getting_early_job_notifications_for_freelance_work | early job notifications for freelance work]] by alerting you within minutes of a new job posting that matches your skills <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. This gives you a significant head start over other applicants, increasing your chances of securing the job, especially for clients who need work done urgently <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>, <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. You can [[optimizing_job_search_on_upwork_with_custom_alerts | customize the notifications]] by fine-tuning keywords to focus on relevant job types (e.g., "Flixel," "animation," "drone footage") <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.