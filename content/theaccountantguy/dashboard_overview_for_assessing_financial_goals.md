---
title: Dashboard overview for assessing financial goals
videoId: -V7ovjYG2vg
---

From: [[theaccountantguy]] <br/> 

A Notion-based sinking funds tracker dashboard helps to [[setting_budget_goals_and_tracking_progress | track financial goals]] by providing a comprehensive overview of savings progress <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. It allows users to monitor the overall amount of savings needed, the amount saved over time, the remaining amount to save, and the percentage of contribution made <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The dashboard also displays the overall progress of contributions made on a month-wise basis, indicating if contributions meet the minimum required criteria <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Sinking Fund Categories <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>

The tracker organizes sinking funds into six main categories:
*   Education <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Events <a class="yt="00:01:02">[00:01:02]</a>
*   Family <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
*   Healthcare <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Transportation <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Utilities <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>

For each category, the dashboard tracks the goal amount, the amount saved, the amount left to save, the contribution made in percentage, the targeted date for contribution, and the required monthly contribution <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## Database Foundation <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>

Building this tracker requires the use of five databases:
1.  **Sinking Funds Database**: Holds all the core details for each sinking fund, including the goal amount, starting balance, start date, goal date, duration in months, and the required monthly payment <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
2.  **Sinking Funds Details Database**: Stores information about individual contributions to each fund, including the contribution date, starting balance, contribution amount, and closing balance <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
3.  **Sinking Funds Overview Database**: Provides a summary of all sinking funds, showing goal amounts, amounts saved, amounts left, targeted savings, and contribution percentages <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
4.  **Sinking Fund Summary Database**: Offers a summarized view of key metrics for each individual sinking fund, such as goal amount, amount saved, amount left, contribution percentage, targeted goal date, and monthly required contribution <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
5.  **Total Sinking Funds Database**: Calculates the combined total values across all sinking funds for targeted contributions, amount saved, amount left, and overall contribution percentage <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

Data is linked and rolled up from these databases to populate the dashboard views <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>, <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

## Dashboard Components <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>

The primary dashboard consists of several sections that provide different perspectives on the sinking funds:

### Summary Section <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>
This section presents the aggregated totals for all sinking funds, showing the total goal amount, the total amount saved, the total amount left to save, and the overall contribution in percentage <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. This section is linked to the "Total Sinking Funds" database and displayed in a gallery view <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### Sinking Funds Overview <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>
This section provides a detailed overview of all six types of sinking funds <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. For each fund, it displays the goal amount, amount saved, amount left to save, contribution percentage, end goal date, and the required monthly contribution <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. This overview is linked to the "Sinking Fund Summary" database and displayed in a gallery mode layout <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

### Sinking Funds Progress <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>
This component visualizes the monthly payments made towards each sinking fund <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. It indicates whether the contribution for any given month meets the minimum required contribution using a green tick for satisfactory contributions and a red cross for contributions that fall short <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. This section is linked to the "Sinking Funds Details" database and presented in a list format <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.