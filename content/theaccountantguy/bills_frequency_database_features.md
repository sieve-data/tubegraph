---
title: Bills frequency database features
videoId: RqN1qUpTkSI
---

From: [[theaccountantguy]] <br/> 

The Bills Frequency Database is a key component in a Notion bills tracker, designed to categorize and analyze bills based on their periodicity of expense <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

## Key Features and Calculations

This database utilizes roll-up properties from the primary Bills Database to derive various financial metrics:

*   **Budgeted Expense**
    *   This value is rolled up from the Bills Database, showing the budgeted amount for expenses <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Actual Expense**
    *   Similar to budgeted expense, this value is rolled up from the Bills Database, reflecting the actual incurred expenses <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **Change**
    *   Calculated as the budgeted expense less the actual expense <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Upcoming Bill**
    *   Rolled up from the Bills Database to display the earliest upcoming due date <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **Bills Paid (Count)**
    *   Rolls up the number of bills that have been marked as paid by specifying a "checked" condition in the roll-up values <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Total Bills**
    *   Rolled up from the description column of the Bills Database, counting all bills together <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Bills Paid in Percentage**
    *   Calculated by dividing the "Bills Paid (Count)" by the "Total Bills" <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   **Textual Representation of Bills Paid**
    *   A formula with an "if" condition calculates and displays how many bills have been paid out of the total bills in a text format <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. This provides a clear summary of the total bills paid at the end <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

This database completes the Bill's frequency tracking within the Notion system <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. For additional categorization, refer to the [[bills_priority_and_category_database | Bills Category Database]] and [[bills_priority_and_category_database | Bills Priority Database]] <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.