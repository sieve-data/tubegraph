---
title: Deriving specific period sales data in Notion
videoId: Ty6QpLsE71I
---

From: [[theaccountantguy]] <br/> 

Deriving specific sales data for a particular period in Notion can be achieved using an external tool called `myformula.com`, which allows for Excel-like formulas without needing to understand Notion's [[using_formulas_in_notion | inbuilt formulas]], relations, or rollups <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>, <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>, <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This method simplifies the process of getting values from one Notion database to another <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>, <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

## Setting Up `myformula.com`

To use `myformula.com`, you'll need to establish a connection with your Notion workspace via an API key:

1.  **Log In**: Navigate to `myformula.com` and log in <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
2.  **Create API Key**:
    *   In `myformula.com`, go to `Settings` and click `Get API key` <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
    *   Click `New integration` <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
    *   Give your integration a name (e.g., "sum formula key") <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
    *   Select your Notion workspace <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
    *   Click `Save` <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
3.  **Copy API Key**:
    *   Go back to `Integrations` <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
    *   Click on your newly created integration <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
    *   Click `Show` next to `Internal Integration Secret` <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
    *   Click `Copy` to copy the full API key <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
4.  **Paste API Key in `myformula.com`**:
    *   Paste the copied API key into the `Notion API Key` field on the `myformula.com` main screen <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   Click `Save Settings` <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
5.  **Connect Notion Databases/Pages**:
    *   Ensure all relevant Notion databases are within a single Notion page (e.g., "Sales Dashboard") <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>, <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
    *   In Notion, click the three dots next to the parent page (e.g., "Sales Dashboard") <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
    *   Go to `Connections` <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
    *   Search for and select the integration name you created (e.g., "sum formula key") <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
    *   Click `Confirm` <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This connects the page and all databases within it to the API key <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

## Calculating Total Sales Revenue

This example demonstrates how to find the overall [[tracking_total_earnings_using_notion | total earnings]] or revenue from a sales database.

1.  **Prepare Notion Databases**:
    *   Have a "Sales Database" with fields like `date`, `product`, `category`, `quantity`, `revenue`, `payment method`, and `sales channel` <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
    *   Create a separate database (e.g., "DB Sales Revenue Total") to store the calculated total. This database should have at least two columns: `Description` and `Amount` <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>, <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
    *   Add a row in the new database (e.g., "Total Sales Revenue") <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
2.  **Generate Formula in `myformula.com`**:
    *   Copy the link of your main "Sales Database" from Notion (click the six dots next to the database title, then `Copy link`) <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
    *   Paste this link into the `Database URL` field in `myformula.com` <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
    *   Select `Sum` as the function <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
    *   Select `Revenue` as the `Notion property` <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
    *   Choose `All Rows` for `Row Selection` <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
    *   Remove any default second filter condition if present <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>, <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
    *   Click `Calculate`. The total revenue will appear <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>, <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
3.  **Add to Notion**:
    *   Click `Add to Notion` <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
    *   Copy the link of the "DB Sales Revenue Total" database <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
    *   Paste this link into the `Database URL` field <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.
    *   Select `Amount` for the `Column Name` <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
    *   Select `Total Sales Revenue` for the `Row Name` <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
    *   Click `Save to Notion`. The calculated value will populate in your Notion database <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
4.  **Save Formula**: Give the formula a name (e.g., "Total Sales Revenue") and click `Save` <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>, <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. This formula will now appear in your `Saved Formulas` section <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

## Deriving Specific Period Sales Data: March 2025 Sales Revenue

To find sales revenue for a specific month, like March 2025, you'll add a date filter. This is similar to [[using_periodical_income_analysis_in_notion | periodical income analysis]].

1.  **Create New Database**: Create a new Notion database (e.g., "DB Sales Revenue March 2025") with `Description` and `Amount` columns <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>, <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. Add a row like "Sales Revenue March 2025" <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
2.  **Generate Formula with Date Filter**:
    *   In `myformula.com`, click `New Formula` <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.
    *   Copy the "Sales Database" link and paste it <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.
    *   Select `Sum` for `Function` and `Revenue` for `Notion property` <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
    *   Under `Conditions`, select `Date` property <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
    *   Choose `is between` for the filter <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
    *   Enter the start and end dates (e.g., March 1, 2025, to March 31, 2025) <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
    *   Click `Calculate` <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. The filtered sum will be displayed <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
3.  **Add to Notion**:
    *   Click `Add to Notion` <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
    *   Copy the link of your "DB Sales Revenue March 2025" database <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.
    *   Paste it into the `Database URL` field <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
    *   Select `Amount` for the `Column Name` and "Sales Revenue March 2025" for `Row Name` <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.
    *   Click `Save to Notion` <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.
4.  **Save Formula**: Save the formula with a descriptive name (e.g., "Total Sales Revenue for March 2025") <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.

## Deriving Specific Period Sales Data: Q1 2025 Sales for Software Category

This example adds another condition (category) to the date filter, which is useful for [[calculating_profit_and_loss_in_notion | calculating profit and loss]] by category.

1.  **Create New Database**: Create another Notion database (e.g., "DB Sales Category Q1 2025") with `Description` and `Amount` columns <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>. Add a row like "Q1 2025 Sales for Software" <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>.
2.  **Generate Formula with Multiple Conditions**:
    *   In `myformula.com`, click `New Formula` <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.
    *   Copy the "Sales Database" link and paste it <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
    *   Select `Sum` for `Function` and `Revenue` for `Notion property` <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.
    *   **Condition 1 (Date)**:
        *   Select `Date` property <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.
        *   Choose `is between` <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>.
        *   Enter the start and end dates for Q1 (e.g., January 1, 2025, to March 31, 2025) <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>.
    *   **Condition 2 (Category)**:
        *   Ensure the `AND` operator is selected between conditions <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>, <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.
        *   Click `+` to add a new condition <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.
        *   Select `Category` property <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.
        *   Choose `is` and enter `Software` <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.
    *   Click `Calculate`. The filtered sum will be displayed <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>, <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>.
3.  **Add to Notion**:
    *   Click `Add to Notion` <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.
    *   Copy the link of your "DB Sales Category Q1 2025" database <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>.
    *   Paste it into the `Database URL` field <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>.
    *   Select `Amount` for the `Column Name` and "Q1 2025 Sales for Software" for `Row Name` <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>.
    *   Click `Save to Notion` <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>.
4.  **Save Formula**: Save the formula with a descriptive name (e.g., "Q1 2025 Sales for Software") <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.

## Refreshing and Dynamic Updates

After setting up these formulas, `myformula.com` offers dynamic updates:

*   **Refresh All**: If you make changes in your original sales database, click `Refresh All` in the `Saved Formulas` section of `myformula.com`. This will automatically recompute and update all saved formulas in your Notion databases <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>, <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>, <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>. This is critical for [[monthly_and_yearly_financial_overviews_in_notion | monthly and yearly financial overviews]] and keeping [[using_notion_to_analyze_financial_data | financial data analysis]] up to date.
*   **Specific Refresh**: If you only want to update a single formula, click the `Refresh` icon next to that specific formula in the `Saved Formulas` list <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

## Benefits

Using `myformula.com` allows you to generate custom formulas without needing to understand Notion's [[using_formulas_in_notion | formulas]] or complex relation/rollup properties <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>, <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>. It provides a dynamic and easy-to-use solution for [[finance_templates_in_notion | finance templates]] and [[sales_transactions_and_customization_in_notion | sales transactions and customization]].

For further queries, you can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:22:31">[00:22:31]</a>. Future videos will cover more Excel formulas in this context <a class="yt-timestamp" data-t="00:22:52">[00:22:52]</a>.