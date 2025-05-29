---
title: Notion sinking funds tracker setup
videoId: -V7ovjYG2vg
---

From: [[theaccountantguy]] <br/> 

A [[how to track sinking funds | sinking funds tracker]] can be built using Notion to monitor overall savings needed, amounts saved over time, remaining amounts to save, and percentage contributions over a period <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This tracker allows for monitoring the progress of contributions month-wise, indicating if contributions meet the minimum required criteria <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

The tracker can be set up for various types of sinking funds, such as:
*   Education <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Events <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   Family <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
*   Healthcare <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Transportation <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   Utilities <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>

For each sinking fund, the system tracks:
*   Goal amount <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>
*   Amount saved over time <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
*   Amount left to save <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
*   Contribution made over time (reflected in percentage) <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>
*   Targeted date of making the contribution <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>
*   Required contribution to be made each month <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>

## Required Databases

To build the Notion [[how to track sinking funds | sinking funds tracker]], five databases are utilized <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>:
1.  Sinking Funds Database <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>
2.  Sinking Funds Details Database <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>
3.  Sinking Funds Overview Database <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>
4.  Sinking Fund Summary Database <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>
5.  Total Sinking Funds Database <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>

### 1. Sinking Funds Database

This database holds all the specific details for each sinking fund being created <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>, <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

Key properties include:
*   **Sinking Funds Details (Category):** Categorizes the funds (e.g., Healthcare, Transportation, Utilities, Events, Family, Education) <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Goal Amount:** The targeted savings amount <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Starting Balance:** The initial savings at the start of the journey <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Start Date:** The date when saving began for the fund <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Goal Date:** The targeted end date to build the fund <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Months:** The duration in months between the start and goal dates <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Payment Breakdown:** The required monthly payment towards the fund, calculated as `(Goal Amount - Starting Balance) / Months` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Account:** Specifies the account where the fund is created <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Amount Saved:** A rolled-up value from another database, showing total savings to date <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Amount Left:** The necessary balance to contribute, calculated as `Goal Amount - Amount Saved` <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### 2. Sinking Funds Details Database

This database stores information related to each sinking fund and its contributions <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

Key properties include:
*   **Sinking Fund (Relation):** Links to the specific sinking fund to which a contribution is made <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>, <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
*   **Category:** Helps link different databases together, mirroring the sinking fund name <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Contribution Date:** The date of a specific contribution <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Starting Balance:** The balance at the start of contributing on a specific date, typically the closing balance of the previous month (zero for the first month) <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   **Contribution Amount:** The amount contributed on a specific date <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Closing Balance:** Calculated as `Opening Balance + Contribution Amount` <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. The closing balance of one month is copied to the next month's opening balance <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **Contribution Required Per Month:** Rolled up from the Sinking Funds database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### 3. Sinking Funds Overview Database

This database provides a complete overview of all created sinking funds <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

Key properties include:
*   **Goal Amount:** The targeted sinking fund amount <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Amount Saved:** The total contribution made so far across all sinking funds <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Amount Left:** The further contribution required, calculated as `Goal Amount - Amount Saved` <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Targeted Savings:** The minimum monthly contribution required, rolled up from other databases <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Contribution (Percentage):** Calculated as `Total Amount Saved / Targeted Amount` <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **Goal Date:** The date by which the sinking funds should be established <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### 4. Sinking Fund Summary Database

This database summarizes the targeted goal amount, amount saved, amount left, contribution percentage, targeted goal date, and required monthly contribution for *each individual* sinking fund <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. All amounts are rolled up from earlier databases, creating a concise summary of the tracker <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

### 5. Total Sinking Funds Database

This database calculates the combined total values across all sinking funds <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

It includes:
*   Targeted sinking funds contribution <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>
*   Total amount saved <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>
*   Total amount left <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>
*   Overall contribution percentage (Total Contribution / Targeted Amount) <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>, <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>

All values are rolled up from the previously discussed databases <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

## Primary Dashboard

The primary dashboard provides a centralized view of the sinking funds tracker:

### Summary Section
This section displays the total goal amount, amount saved, amount left, and contribution in percentage across all sinking funds combined <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. It is linked to the Total Sinking Funds database and displayed in a gallery view <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### Sinking Funds Overview
This section provides an overview of all six types of sinking funds <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. It shows the goal amount, amount saved, amount left to save, contribution percentage, end goal date, and the required monthly contribution for each <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. This view is linked to the Sinking Fund Summary database, also presented in a gallery mode <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

### Sinking Funds Progress
This section tracks monthly payments made towards each sinking fund, along with the number of contributions <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   A green tick indicates if a monthly contribution exceeds the minimum required amount <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   A red cross appears if the contribution does not meet the minimum requirement <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
This progress view is linked to the individual Sinking Funds Details database, displayed in a list format <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

The Notion [[how to track sinking funds | sinking funds tracker]] can be downloaded as a template, with the link available in the description of the source video <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.