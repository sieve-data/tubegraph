---
title: Tracking savings goals and progress
videoId: -V7ovjYG2vg
---

From: [[theaccountantguy]] <br/> 

A sinking funds tracker is a tool, often built using Notion, designed to help monitor and manage savings for specific future expenses <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. It allows users to [[setting_net_worth_goals_and_tracking_progress | track]] the total savings needed for a period, the amount already saved, the remaining amount to save, and the percentage of the goal contributed over time <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Components Tracked
For each individual sinking fund, the tracker monitors:
*   The goal amount <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>
*   The amount saved over time <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
*   The amount left to save <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
*   The contribution made over time, reflected as a percentage <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>
*   The targeted date for making the contribution <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>
*   The required contribution to be made each month <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>

The tracker also provides an overall progress view of each sinking fund, showing month-wise contributions and indicating whether they meet the minimum required contribution criteria <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Common Sinking Fund Categories
Common categories for sinking funds include:
*   Education <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>, <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>, <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>
*   Events <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>, <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>, <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>
*   Family <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>, <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>, <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>
*   Healthcare <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>, <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>, <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>
*   Transportation <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>, <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>, <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>
*   Utilities <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>, <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>, <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>

## Building the Tracker in Notion

Building a sinking funds tracker in Notion requires the use of five interconnected databases <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

### 1. Sinking Funds Database
This database holds all the specific details for each sinking fund being created <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Sinking Fund Details:** Categories such as Healthcare, Transportation, Utilities, Events, Family, and Education <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Goal Amount:** The targeted amount of savings to achieve <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Starting Balance:** The initial savings available at the beginning of the journey <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Start Date:** The date when saving for the sinking fund began <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Goal Date:** The targeted end date by which the sinking fund should be fully built <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Months:** The duration in months between the start date and the goal date <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Payment Breakdown:** The monthly payment required for the sinking fund, calculated as (Goal Amount - Starting Balance) / Months <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. This is analogous to [[payment_tracking_and_debt_progression | tracking payment progression]].
*   **Account:** Specifies the account where the sinking fund is held <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Amount Saved:** The total savings accumulated so far, rolled up from another database <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. This directly relates to [[setting_savings_targets_and_goals_in_notion | setting and tracking savings targets]].
*   **Amount Left:** The goal amount minus the amount saved, representing the remaining balance needed <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### 2. Sinking Funds Details Database
This database stores information related to each specific sinking fund and its contributions <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   **Sinking Fund:** The specific fund to which contributions are being made <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Category:** Links different databases together by matching the sinking fund name <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Contribution Date:** The date on which a contribution is made <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Starting Balance:** The balance at the beginning of the contribution period, which is the closing balance of the previous month (zero for the first month) <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   **Contribution Amount:** The amount contributed on a specific date <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Closing Balance:** Calculated as Starting Balance + Contribution Amount <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. The closing balance of one month becomes the opening balance of the next <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **Contribution Required Per Month:** Rolled over from the Sinking Funds Database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### 3. Sinking Funds Overview Database
This database provides a complete overview of all created sinking funds <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   **Goal Amount:** The total targeted amount across all sinking funds <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Amount Saved:** The total contributions made so far for all types of sinking funds <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Amount Left:** Indicates further contributions needed, calculated as Goal Amount - Amount Saved <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Targeted Savings:** The minimum contribution required each month, rolled up from other databases <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Contribution in Percentage:** Total amount saved divided by the targeted amount <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **Goal Date:** The target date for completing the sinking funds <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### 4. Sinking Fund Summary Database
This database summarizes key metrics for each individual sinking fund <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   Targeted goal amount <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>
*   Amount saved so far <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>
*   Amount left to contribute <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>
*   Contribution made in percentage <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>
*   Targeted goal date <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>
*   Contribution required for each month <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>

All these values are rolled up from the earlier databases to create a summarized view of the tracker <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

### 5. Total Sinking Funds Database
This database calculates the combined total values of all sinking funds <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   Total targeted sinking funds contribution <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>
*   Total amount saved <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>
*   Total amount left <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>
*   Total contribution in percentage (total contribution divided by targeted amount) <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>, <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>

These values are also calculated by rolling up respective values from the previous databases <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

## Primary Dashboard Overview
The primary dashboard integrates these databases to provide a comprehensive view of the sinking funds.
*   **Summary Section:** Displays the aggregate goal amount, amount saved, amount left, and contribution percentage for all sinking funds combined. This links to the Total Sinking Funds database in a gallery view <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
*   **Sinking Funds Overview:** Presents an overview of all six types of sinking funds, showing their individual goal amounts, saved amounts, remaining amounts, contribution percentages, goal dates, and monthly required contributions. This is linked to the Sinking Fund Summary database in a gallery mode layout <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   **Sinking Funds Progress:** Details monthly payments made towards each sinking fund and tracks the number of contributions. It visually indicates whether monthly contributions meet the minimum required amount (green tick for meeting, red cross for not meeting) <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. This is linked to the individual Sinking Funds Details database in a list format <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

This Notion-based system serves as a detailed [[setting_net_worth_goals_and_tracking_progress | personal finance tracker]] and a way to [[setting_savings_targets_and_goals_in_notion | manage savings goals]] effectively.