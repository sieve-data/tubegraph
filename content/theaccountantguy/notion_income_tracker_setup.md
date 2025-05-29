---
title: Notion income tracker setup
videoId: 2MkChIwv0t0
---

From: [[theaccountantguy]] <br/> 

A Notion income tracker is a minimalistic tool designed to help users stay on top of their [[using_notion_for_financial_tracking | finances]] by tracking income [00:00:59] and providing detailed analysis of earnings [00:01:01].

## Key Sections of the Tracker

The Notion income tracker is structured into four main sections:
*   **Total Earnings** Shows the overall earnings for a specific period [00:01:07].
*   **Sources of Income** Displays total earnings for each individual income source (e.g., salary, side hustle) and its percentage of the total income [00:01:12].
*   **Frequency of Income** Indicates how often income is earned, calculating total earnings and the number of sources for each frequency [00:01:21].
*   **Overview Section** Presents monthly income broken down into four quarters, along with each month's earnings percentage relative to the total earnings [00:01:34].

## Required Databases

To build this income tracker, five interconnected databases are necessary [00:01:49]:
1.  **Income Details Database**: Records the specifics of income earned [00:01:53].
2.  **Income Source Database**: Categorizes income by source [00:02:02].
3.  **Frequency of Income Database**: Provides an overview of how often income is received over a period [00:02:10].
4.  **Total Earnings Database**: Reflects the cumulative earnings for a specified period [00:02:19].
5.  **Period Database**: Tracks periodical income earned throughout a year [00:02:27].

## Database Details

### 1. Income Details Database

This database is where income-related details are fed for analysis [00:02:38].
*   **Income Details (Title Property)**: The default property, used to specify different sources of income received during the year [00:02:44].
*   **Period of Income (Relation Property)**: Linked to the Period Database, it reflects monthly incomes per source [00:02:58]. This relation is bidirectional [00:03:05].
*   **Income Source (Relation Property)**: Linked to the Income Source Database, it specifies the source of income (e.g., salary, side hustle, other) [00:03:18]. This relation is bidirectional [00:03:24].
*   **Frequency of Income (Relation Property)**: Linked to the Frequency of Income Database, it specifies how frequently income is earned [00:03:31]. This relation is bidirectional [00:03:38].
*   **Amount (Number Property)**: Shows the amount of income earned for a specific period [00:03:44].
*   **Sum**: A calculation at the bottom showing the sum of income earned during the period [00:03:50].

### 2. Income Source Database

This database analyzes different sources of income [00:03:59].
*   **Name (Title Property)**: Defines distinct income sources like "Salary," "Side Hustle," and "Other Income" [00:04:05].
*   **Earnings (Relation Property)**: Related to the Total Earnings Database [00:04:12].
*   **Income Details (Relation Property)**: Related to the Income Details Database [00:04:22].
*   **Actual Income (Roll-up Property)**: Derived from the Income Details Database, it sums the 'Amount' property to show actual income for each source [00:04:31].
*   **Total Earnings (Roll-up Property)**: Derived from the Earnings Database, it displays the total earnings amount [00:04:51].
*   **Frequency (Roll-up Property)**: Comes from the Income Details Database, extracting the 'Frequency of Income' property [00:05:04].
*   **Earnings in Percentage (Formula Property)**: Calculates the percentage of each source's earnings relative to the total earnings [00:05:19]. This is formatted as a percentage with a green bar [00:05:31].

### 3. Frequency of Income Database

This database provides analysis on how frequently income is earned [00:05:40].
*   **Frequency (Title Property)**: Indicates how frequently income is earned, such as "Monthly Income," "Annual Income," "Quarterly Income," "Half Yearly Income," or "One-Time Income" [00:05:47].
*   **Earnings Associated to Each Frequency of Income (Roll-up Property)**: Derived from the related property (Income Details relation), it calculates the sum of earnings for each frequency [00:06:00].
*   **Relation to Income Details (Relation Property)**: Linked to the Income Details Database, defining all income sources related to each frequency [00:06:23].
*   **Sources of Income (Formula Property)**: Calculates the number of income sources associated with each frequency. It categorizes them as "one source," "two sources," "three sources," or "no source" based on the count [00:06:37].

### 4. Total Earnings Database

This database relates total earnings to the three specified income sources [00:07:07].
*   **Total Earnings (Title Property)**: The name property for this database [00:07:17].
*   **Income Source (Relation Property)**: Established with the Income Source Database, specifying the three income sources [00:07:23].
*   **Total Earnings (Roll-up Property)**: Rolls up values from the Income Source database, calculating the sum of total earnings associated with these income sources [00:07:31].

### 5. Period Database

This final database calculates periodical income for each month and provides further analysis [00:07:46].
*   **Month (Title Property)**: Represents the month of income [00:08:02].
*   **Income Details (Relation Property)**: Related to the Income Details Database, showing income earned [00:08:08].
*   **Earnings (Roll-up Property)**: Rolled up from the Income Details Database, presenting the sum of earnings for each month [00:08:16].
*   **Total Earnings (Roll-up Property)**: Rolled up from the Total Earnings Database, showing the original values of combined total earnings for all months [00:08:29].
*   **Proportion of Earnings (Formula Property)**: Calculates the percentage of each month's earnings relative to the total yearly earnings by dividing monthly earnings by total earnings [00:08:44]. This is formatted as a percentage with a green bar [00:08:54].

## Primary Dashboard Presentation

The databases are presented on a primary dashboard for a comprehensive view [00:09:02].

*   **Total Earnings Display**: This section links to the Total Earnings Database and is displayed in a list view [00:09:08]. It represents the total income earned during the period [00:09:12].
*   **Sources of Income Display**: Presented in a three-column layout [00:09:32], created using the `/three columns` command [00:09:36]. Each column is linked to the Income Source Database and displayed in a gallery format [00:09:41]. It shows the actual income and percentage for each source relative to the total income [00:09:47].
*   **Frequency Display**: Derived from the Frequency of Income Database, also presented in a gallery layout [00:09:53]. It shows total earnings and sources of earnings for each frequency [00:10:01].
*   **Overview Section**: Linked to the Period Database and presented in a gallery mode [00:10:07]. This section is divided into four quarters, with individual months specified within each [00:10:13]. It displays earnings per month and their proportion to total earnings [00:10:19]. Filters are applied to each quarter to display the respective months [00:10:24].