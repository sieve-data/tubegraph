---
title: Building a Notion Income Tracker
videoId: 2MkChIwv0t0
---

From: [[theaccountantguy]] <br/> 

This guide outlines how to build a minimalistic income tracker using [[Setting Up Notion Databases for Income Tracking | Notion]] to stay on top of your finances <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

## Tracker Sections

The [[Setting Up Notion Databases for Income Tracking | Notion]] income tracker is structured into four main sections:
*   **Total Earnings** <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>: Displays the total amount of earnings for a specified period <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
*   **Sources of Income** <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>: Shows total earnings for each individual income source (e.g., salary, side hustle, other) and its percentage of the total income <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Frequency of Income** <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>: Indicates how frequently income is earned, calculating total earnings and the number of sources for each frequency <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
*   **Overview Section** <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>: Segregates monthly income into four quarters, displaying the percentage of monthly earnings relative to total earnings <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

## Required Databases

To build this income tracker, five databases are required <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>:
1.  **Income Details Database**: Stores the specific details of income earned <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
2.  **Income Source Database**: Tracks income earned with respect to each source <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
3.  **Frequency of Income Database**: Provides an overview of how frequently income is earned during a period <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
4.  **Total Earnings Database**: Reflects the total earnings within a given period <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
5.  **Period Database**: Displays periodical income earned throughout a year <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## Database Construction

### Income Details Database

This database is used to input income details and generate related analysis <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Income Details**: A default title property where different sources of income received during the year are specified <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **Period of Income**: A relation property linked to the Period Database, reflecting monthly incomes per income source <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   **Income Source**: A relation property linked to the Income Source Database, specifying sources like salary, side hustle, and other income <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   **Frequency of Income**: A relation property linked to the Frequency of Income Database, indicating how frequently income is earned <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Amount**: A number property showing the income earned for a specific period <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. The sum of income earned during the period is displayed at the bottom <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

### Income Source Database

This database analyzes different sources of income <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   **Name**: Defines different income sources (e.g., salary, side hustle, other income) <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **Earnings Database**: A relation property linked to the Total Earnings Database, added to the three specified income sources <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **Income Details Property**: A relation property linked to the Income Details Database <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Actual Income**: A roll-up property derived from the Income Details Database, summing the 'Amount' property <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Total Earnings**: A roll-up property derived from the Earnings Database, calculating the amount from the earnings database as original values <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Frequency**: A roll-up property from the Income Details Database, extracting the 'Frequency of Income' property as original values <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   **Earnings in Percentage**: A formula property that calculates the percentage of earnings relative to the total earnings <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>, displayed as a green percentage bar <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

### Frequency of Income Database

This database provides analysis related to income frequency <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   **Frequency**: A title column indicating how frequently income is earned (e.g., monthly, annual, quarterly, half-yearly, one-time) <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **Earnings Associated to Each Frequency of Income**: A roll-up property derived from the related property in the next column, calculating the sum of earnings amounts <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Relation Property (Income Details)**: A relation property linked to the Income Details Database, defining all income sources related to each frequency <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Sources of Income**: A formula property that calculates the number of sources. It displays "one source", "two sources", "three sources", or "no source" based on the count <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### Total Earnings Database

This database links total earnings to all three income sources <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   **Total Earnings**: A title property <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **Income Source**: A relation property linked to the Income Source Database, specifying the three income sources <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **Total Earnings (Roll-up)**: A roll-up property that aggregates values from the income sources and calculates their sum to represent total earnings <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

### Period Database

This final database calculates periodical income and performs further analysis <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   **Month**: A title property representing the month of income <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Income Details**: A relation property linked to the Income Details Database, showing income earned <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   **Earnings**: A roll-up property from the Income Details Database, summing the earnings amount for each month <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Total Earnings**: A roll-up property from the Total Earnings Database, representing the total earnings for all months combined with original values <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   **Proportion of Earnings**: A formula property calculating the percentage of each month's earnings to the total earnings, displayed as a green percentage bar <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

## Primary Dashboard Presentation

The primary dashboard integrates all the databases for a comprehensive overview <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

*   **Total Earnings**: Presented as a linked view of the Total Earnings Database in a list format <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   **Sources of Income**: Presented in a three-column layout (created using `/three columns`) linked to the Income Source Database with a gallery format <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. This displays actual income and the percentage of each source relative to total income <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   **Frequency**: Derived from the Frequency of Income Database, presented in a gallery format <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. It shows total earnings and sources of earnings for each frequency <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   **Overview Section**: Linked to the Period Database with a gallery mode of presentation <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Information is divided into four quarters, specifying individual months for each <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. It displays earnings for each month and their proportion to total earnings <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>. Filters are applied to specify respective months for each quarter <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

> [!INFO]
> This tracker provides a comprehensive way to monitor and analyze income flow in [[Setting Up Notion Databases for Income Tracking | Notion]] <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.