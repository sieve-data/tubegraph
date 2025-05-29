---
title: Dashboard and summary views for sinking funds in Notion
videoId: -V7ovjYG2vg
---

From: [[theaccountantguy]] <br/> 

This article details the dashboard and summary views for a [[notion_sinking_funds_tracker_setup | sinking funds tracker]] built using [[using_notion_for_financial_tracking | Notion]] <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. The tracker allows users to monitor their overall savings progress and the status of individual sinking funds <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Overview of the Sinking Funds Tracker

The [[notion_sinking_funds_tracker_setup | sinking funds tracker]] is designed to track several key financial metrics over a period of time <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>:
*   The total amount of savings needed <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   The amount saved to date <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   The remaining amount to save <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   The contribution made as a percentage of the total goal <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

The tracker categorizes sinking funds into six types: Education, Events, Family, Healthcare, Transportation, and Utilities <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. For each individual sinking fund, the system tracks:
*   The goal amount <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   The amount saved over time <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   The amount left to save <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   Contribution made over time, reflected in percentage <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   The targeted date for the contribution <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   The required monthly contribution <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

The tracker also displays the overall progress of each sinking fund, showing monthly contributions and indicating whether they meet the minimum contribution criteria <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Underlying Databases for Display

The [[notion_sinking_funds_tracker_setup | sinking funds tracker]] uses five interconnected databases <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>:
1.  **Sinking Funds Database**: Holds details for each sinking fund <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
2.  **Sinking Funds Details Database**: Stores information related to each sinking fund and its contributions <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>, <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
3.  **Sinking Funds Overview Database** <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
4.  **Sinking Fund Summary Database** <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
5.  **Total Sinking Funds Database** <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

### Sinking Funds Overview Database

This database provides a comprehensive overview of all created sinking funds <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. It includes the following properties:
*   **Goal Amount**: The targeted sinking fund amount <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Amount Saved**: The total contributions made across all sinking funds <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Amount Left**: The remaining contribution needed (Goal Amount less Amount Saved) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Targeted Savings**: The minimum required monthly contribution (rolled up from another database) <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Contribution in Percentage**: Total amount saved divided by the targeted amount <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **Goal Date**: The target date for achieving the sinking fund goal <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### Sinking Fund Summary Database

This database presents a summarized view of individual sinking funds <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. It tracks:
*   Targeted goal amount <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.
*   Amount saved so far <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
*   Amount left to contribute <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
*   Contribution made in percentage <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
*   Targeted goal date <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
*   Contribution required for each month <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
All these amounts are rolled up from earlier databases <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

### Total Sinking Funds Database

This database calculates the combined total values across all sinking funds <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. It provides:
*   Total targeted sinking funds contribution <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
*   Total amount saved <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   Total amount left <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   Total contribution in percentage <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
The contribution percentage is calculated as the total contribution divided by the total targeted amount <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. These values are derived by rolling up respective values from previous databases <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

## The Primary Dashboard Layout

The primary dashboard provides a centralized view of all [[budgeting_and_saving_with_notion | financial data]] related to sinking funds <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### Summary Section
This section displays the aggregated financial status of all sinking funds <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. It shows:
*   Goal amount <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   Amount saved <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
*   Amount left <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
*   Contribution in percentage <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
This data is the sum total of all sinking funds combined <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a> and is linked to the `Total Sinking Funds` database, displayed in a gallery view <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### Sinking Funds Overview
This section provides an overview of the six types of sinking funds <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. It displays:
*   Goal amount <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
*   Amount saved <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   Amount left to save <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
*   Contribution in percentage <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   End goal date <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   Required contribution for each month <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
These details are linked to the `Sinking Fund Summary` database and presented in a gallery layout <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

### Sinking Funds Progress
This section tracks monthly payments made towards each sinking fund <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. It shows:
*   The number of contributions made <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
*   A green tick if the monthly contribution exceeds the minimum required <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   A red cross if the contribution does not meet the minimum required <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
This view is linked to the `Individual Sinking Funds Details` database and displayed in a list format <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

This [[notion_sinking_funds_tracker_setup | Notion sinking funds tracker setup]] provides a comprehensive tool for [[budgeting_and_saving_with_notion | budgeting and saving]] by offering clear dashboard and summary views of all financial goals <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.