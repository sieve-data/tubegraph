---
title: Types of Sinking Funds for personal finance
videoId: -V7ovjYG2vg
---

From: [[theaccountantguy]] <br/> 

A [[sinking_funds_tracker | sinking funds tracker]] in Notion can be used to track specific savings goals [00:00:45]. This tracker helps manage the overall amount of savings needed, the amount saved over time, the remaining amount to save, and the percentage of contribution made over a period [00:00:48].

## Categories of Sinking Funds

The [[sinking_funds_tracker | sinking funds tracker]] is designed to manage various savings categories, referred to as "sinking funds" [00:01:00]. Six types of sinking funds are typically created within this system:
*   Education [00:01:02]
*   Events [00:01:02]
*   Family [00:01:03]
*   Healthcare [00:01:04]
*   Transportation [00:01:04]
*   Utilities [00:01:04]

## Tracking Each Sinking Fund Type

For each specific sinking fund category, the tracker monitors several key metrics:
*   **Goal Amount** The targeted amount of savings [00:01:10], representing the desired final savings for that particular fund [00:02:12].
*   **Amount Saved Over Time** The total savings accumulated to date for that fund [00:01:11]. This value is rolled up from other databases [00:03:00].
*   **Amount Left to Save** The remaining balance needed to reach the goal [00:01:12], calculated as the goal amount minus the amount saved [00:03:11].
*   **Contribution Made (Percentage)** The proportion of the goal amount that has been saved [00:01:14], calculated as the total amount saved divided by the targeted amount [00:05:31].
*   **Targeted Date** The planned date by which the contribution should be completed [00:01:16], also referred to as the "goal date" [00:02:30].
*   **Required Monthly Contribution** The amount that needs to be contributed each month to reach the goal [00:01:18]. This is derived from the difference between the goal amount and the starting balance, divided by the number of months in the saving period [00:02:49].

### Additional Details for Each Sinking Fund
The [[sinking_funds_tracker | sinking funds tracker]] also tracks specific details for each fund type:
*   **Starting Balance** The initial savings available at the beginning of the saving journey [00:02:17].
*   **Start Date** The date when saving began for a specific sinking fund [00:02:23].
*   **Months** The duration of the saving period between the start and goal dates, calculated in months [00:02:35].
*   **Account** The financial account where the sinking fund is established [00:02:56].

## Overall Progress Tracking
The tracker provides an [[tracking_savings_goals_with_a_sinking_funds_tracker | overall progress overview]] for each sinking fund [00:01:22]. This includes monthly contribution progress, indicating whether contributions meet the minimum required criteria [00:01:26]. If a monthly contribution exceeds the minimum, it's marked with a green tick; if it falls short, a red cross is shown [00:07:34].

## Database Structure for Tracking
To build this [[sinking_funds_tracker | sinking funds tracker]] in Notion, five distinct databases are utilized [00:01:39]:
1.  **Sinking Funds Database**: Holds all details for each sinking fund [00:01:43], including categories like Healthcare, Transportation, Utilities, Events, Family, and Education [00:02:06].
2.  **Sinking Funds Details Database**: Stores information related to each sinking fund and its contributions [00:01:49], including the contribution date, starting balance for that contribution, contribution amount, and closing balance [00:03:58].
3.  **Sinking Funds Overview Database**: Provides a summary of all sinking funds created, showing the overall goal amount, total amount saved, amount left, targeted monthly savings, and contribution percentage [00:01:50].
4.  **Sinking Fund Summary Database**: Offers a detailed summary for each individual sinking fund, including its targeted goal, saved amount, remaining amount, percentage contributed, goal date, and monthly required contribution [00:01:52].
5.  **Total Sinking Funds Database**: Calculates the combined total values for all sinking funds, including targeted contribution, total amount saved, total amount left, and overall contribution percentage [00:01:54].

> [!INFO] Data Roll-up
> Many values in the tracker, such as the amount saved, contribution required per month, and summarized totals, are calculated by "rolling up" data from these interlinked databases [00:03:00], [00:04:42], [00:06:03], [00:06:40].