---
title: Analyzing income sources and earnings
videoId: 2MkChIwv0t0
---

From: [[theaccountantguy]] <br/> 

The Notion income tracker is designed to help users stay on top of their finances by providing a detailed breakdown and analysis of their income. It offers a minimalistic yet comprehensive approach to understanding where income comes from, how frequently it's earned, and its overall contribution to total earnings <a class="yt-timestamp" data-t="00:57:00">[00:57:00]</a>.

This tracker is built with four key sections:
*   **Total Earnings** Provides the aggregate amount earned for a specific period <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>.
*   **Sources of Income** Details total earnings for each individual income source (e.g., salary, side hustle) and its percentage of the total income <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>.
*   **Frequency of Income** Shows how often income is earned, including total earnings and the number of sources for each frequency <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>.
*   **Overview Section** Displays monthly income segregated into four quarters, along with the percentage of monthly earnings relative to total earnings <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>.

## Core Databases for Income Analysis

To construct this income tracker, five interconnected databases are utilized <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>:

1.  **Income Details Database** <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>
2.  **Income Source Database** <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>
3.  **Frequency of Income Database** <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>
4.  **Total Earnings Database** <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>
5.  **Period Database** <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>

### Income Details Database

This database serves as the primary input point for all income-related data <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.
*   **Income Details Property (Title)**: Specifies different income sources received throughout the year <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.
*   **Period of Income (Relation)**: Links to the Period Database, reflecting monthly incomes per source <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>.
*   **Income Source (Relation)**: Links to the Income Source Database, identifying the specific source (e.g., salary, side hustle) <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>.
*   **Frequency of Income (Relation)**: Connects to the Frequency of Income Database, indicating how often income is earned <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>.
*   **Amount**: Records the numerical income earned for a particular period <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>. The sum of this property at the end shows the total income earned during the period <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>.

### Income Source Database

This database is crucial for analyzing the performance of different income streams <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>.
*   **Name**: Defines the distinct sources of income like salary, side hustle, or other income <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>.
*   **Earnings Database (Relation)**: Linked to the Total Earnings Database <a class="yt-timestamp" data-t="04:12:00">[04:12:00]</a>.
*   **Income Details Property (Relation)**: Connected to the Income Details Database <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.
*   **Actual Income (Roll-up)**: Derived from the Income Details Database, it calculates the sum of the `Amount` property for each source <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>.
*   **Total Earnings (Roll-up)**: Derived from the Earnings Database, it displays the total earnings relevant to the income source <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.
*   **Frequency Property (Roll-up)**: Extracts the frequency of income from the Income Details Database <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>.
*   **Earnings in Percentage (Formula)**: Calculates the percentage contribution of each source's earnings to the total earnings, displayed with a percent format and a green bar <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>.

### Frequency of Income Database

This database provides analysis on how frequently income is earned <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>.
*   **Frequency (Title)**: Indicates frequencies like monthly, annual, quarterly, half-yearly, or one-time income <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>.
*   **Earnings Associated to each frequency of income (Roll-up)**: Calculates the sum of earnings for each frequency from related properties <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>.
*   **Relation property**: Links to the Income Details Database, defining all sources of income related to each frequency <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>.
*   **Sources of income (Formula)**: Determines the number of income sources associated with each frequency (e.g., "one source", "two sources", "no source") <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>.

### Total Earnings Database

This database consolidates the total earnings from all income sources <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a>.
*   **Total Earnings (Title)**: A simple name property <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>.
*   **Income Source (Relation)**: Linked to the Income Source Database, incorporating the three specified income sources <a class="yt-timestamp" data-t="07:23:00">[07:23:00]</a>.
*   **Total Earnings (Roll-up)**: Rolls up values from the income sources to calculate the sum of total earnings associated with them <a class="yt-timestamp" data-t="07:31:00">[07:31:00]</a>.

### Period Database

The Period Database analyzes periodical income for each month <a class="yt-timestamp" data-t="07:46:00">[07:46:00]</a>.
*   **Month (Title)**: Represents the month of income <a class="yt-timestamp" data-t="08:02:00">[08:02:00]</a>.
*   **Income Details (Relation)**: Links to the Income Details Database, showing the income earned in that period <a class="yt-timestamp" data-t="08:08:00">[08:08:00]</a>.
*   **Earnings (Roll-up)**: Rolls up the earnings `Amount` from the Income Details Database, presented as a sum <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>.
*   **Total Earnings (Roll-up)**: Rolls up data from the Total Earnings Database, representing overall earnings <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a>.
*   **Proportion (Formula)**: Calculates the percentage of each month's earnings to the total yearly earnings, formatted as a percentage with a green bar <a class="yt-timestamp" data-t="08:42:00">[08:42:00]</a>.

## Primary Dashboard Presentation

The primary dashboard serves as the main interface for [[analyzing_income_and_expenses_with_the_dashboard | analyzing income and expenses with the dashboard]], presenting the aggregated data in an easily digestible format <a class="yt-timestamp" data-t="09:02:00">[09:02:00]</a>.

*   **Total Earnings**: Displays the total income earned during the period, linked directly from the Total Earnings database in a list view <a class="yt-timestamp" data-t="09:10:00">[09:10:00]</a>.
*   **Sources of Income**: Presented in a three-column layout using a gallery format, linked to the Income Source database. This section highlights the actual income and percentage contribution of each source <a class="yt-timestamp" data-t="09:32:00">[09:32:00]</a>.
*   **Frequency**: Derived from the Frequency of Income database and displayed in a gallery format, showing total earnings and sources for each frequency <a class="yt-timestamp" data-t="09:53:00">[09:53:00]</a>.
*   **Overview Section**: Linked to the Period database with a gallery mode presentation. This section divides information into four quarters, specifying individual months within each. It shows monthly earnings and their proportion to total earnings, with filters applied for respective months in each quarter <a class="yt-timestamp" data-t="10:05:00">[10:05:00]</a>.

This structured approach allows for comprehensive [[tracking_income_and_expenses | tracking income and expenses]] and [[using_dynamic_reporting_for_personal_finance_analysis | dynamic reporting for personal finance analysis]], providing a clear picture of an individual's financial inflows.