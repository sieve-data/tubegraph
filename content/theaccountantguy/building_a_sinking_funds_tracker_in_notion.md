---
title: Building a sinking funds tracker in Notion
videoId: -V7ovjYG2vg
---

From: [[theaccountantguy]] <br/> 

This guide details how to [[tracking_personal_finances_in_notion | build a sinking funds tracker]] using Notion, designed to monitor various savings goals <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. The tracker helps visualize the overall savings needed, the amount already saved, the remaining balance, and the percentage of contribution made over time <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Tracker Overview

The sinking funds tracker categorizes savings into six types: Education, Events, Family, Healthcare, Transportation, and Utilities <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. For each fund, it tracks:
*   The goal amount <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>
*   Amount saved over time <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
*   Amount left to save <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
*   Contribution made over time, reflected in percentage <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>
*   The targeted date for making the contribution <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>
*   The required contribution to be made each month <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>

Additionally, the tracker provides an overall progress view for each sinking fund, showing month-wise contributions and indicating whether they meet the minimum contribution criteria <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Required Databases

To build this sinking funds tracker, five distinct Notion databases are utilized <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

### 1. Sinking Funds Database

This database stores all the primary details for each sinking fund <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   **Sinking Fund Details:** Categorized as Healthcare, Transportation, Utilities, Events, Family, and Education <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Goal Amount:** The targeted savings amount <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Starting Balance:** Initial savings at the beginning of the journey <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Start Date:** The date when saving began for the fund <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Goal Date:** The targeted end date by which the fund should be built <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Months:** Duration between the start and goal dates, calculated in months <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Payment Breakdown:** Required monthly payment towards the fund, calculated as (Goal Amount - Starting Balance) / Months <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Account:** Specifies the account where the fund is held <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Amount Saved:** Rolled up from another database, indicating total savings to date <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Amount Left:** Goal Amount minus Amount Saved, showing the remaining balance needed <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### 2. Sinking Funds Details Database

This database stores information related to each sinking fund and its contributions <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   **Sinking Fund:** The specific sinking fund to which the contribution is being made (e.g., Education, Events, Family, Healthcare, Transportation, Utilities) <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Category:** Helps link different databases together, mirroring the sinking fund name <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Contribution Date:** The date when the contribution is made <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Starting Balance:** The balance at the start of contributing on a specific date, typically the closing balance of the previous month (zero for the first month) <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Contribution Amount:** The amount contributed on the specific date <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Closing Balance:** Starting Balance plus Contribution Amount <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. This closing balance is then copied to the next month's opening balance <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **Contribution Required Per Month:** Rolled up from the Sinking Funds Database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### 3. Sinking Funds Overview Database

This database provides a comprehensive overview of all created sinking funds <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   **Goal Amount:** The targeted total for all sinking funds <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Amount Saved:** Total contributions made across all funds <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Amount Left:** Indicates the further contribution required (Goal Amount - Amount Saved) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Targeted Savings:** Minimum monthly contribution required, rolled up from other databases <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Contribution in Percentage:** Total amount saved divided by the targeted amount <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **Goal Date:** The target date by which all sinking funds should be met <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### 4. Sinking Fund Summary Database

This database summarizes the targeted goal amount, saved amount, remaining amount, percentage contribution, goal date, and required monthly contribution for each individual sinking fund <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. All amounts are rolled up from earlier databases, providing a summarized view of the entire tracker <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

### 5. Total Sinking Funds Database

This database calculates the combined total values across all sinking funds <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **Targeted Contribution:** The total targeted amount for all funds <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
*   **Amount Saved:** The total amount saved across all funds <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Amount Left:** The total remaining amount needed <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Contribution in Percentage:** Total contribution divided by the targeted amount <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

All these values are calculated by rolling up respective values from the previously discussed databases <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

## Primary Dashboard Layout

The main dashboard provides an intuitive interface for viewing and managing the sinking funds.

### Summary Section

This section displays the overall goal amount, amount saved, amount left, and contribution in percentage, representing the sum total of all sinking funds combined <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. It is linked to the Total Sinking Funds database and displayed in a gallery view <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### Sinking Funds Overview

This section presents an overview of all six types of sinking funds, showing the goal amount, amount saved, amount left to save, contribution in percentage, end goal date, and the required monthly contribution for each <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. This section is linked to the Sinking Fund Summary database and displayed in a gallery mode <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

### Sinking Funds Progress

This section tracks monthly payments made towards each sinking fund, along with the number of contributions <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. It visually indicates progress: a green tick signifies that the contribution for a month meets or exceeds the minimum required, while a red cross indicates it does not <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. These insights are linked to the individual Sinking Funds Details database, displayed in a listical format <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

---

> [!NOTE]
> A Notion template for this sinking funds tracker is available for download <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.