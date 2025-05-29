---
title: Assets and Liabilities Database Setup
videoId: G2UuEnUUCos
---

From: [[theaccountantguy]] <br/> 

The [[Tracking income expenses assets and liabilities | Net Worth Tracker]] in Notion requires the use of five types of databases, starting with the assets and liabilities database <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>. This database serves as the primary record for all assets and liabilities for each specific month during the year <a class="yt-timestamp" data-t="01:42:19">[01:42:19]</a>.

## Database Structure

The assets and liabilities database includes the following key properties <a class="yt-timestamp" data-t="01:49:51">[01:49:51]</a>:

*   **Asset/Liability Description**: Specifies the type of asset or liability. Five types of assets are mentioned <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>.
*   **Opening Balance**: A number property representing the balance at the start of the month <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>.
*   **Amount**: Shows the addition or deletion of assets or liabilities for the specific period <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>.
*   **Closing Balance**: Calculated as the opening balance added to the amount during the month <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>.

For each month, this database tracks the opening balance, the amount of change, and the closing balance for assets and liabilities <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>.

## Database Maintenance

To maintain continuity and accuracy, the closing balance of each month must be copied and pasted onto the opening balance of the subsequent month for all assets <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>. This same process is repeated for the liabilities database <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>.

## Integration with Other Databases

This foundational database feeds data into other components of the [[Tracking income expenses assets and liabilities | Net Worth Tracker]]:

*   **[[Asset financials and depreciation | Assets Breakdown]] and [[Asset maintenance details | Liabilities Breakdown]]**: These databases pull the total amount of each asset and liability, respectively, from the assets and liabilities database using a rolled-up formula <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>.
*   **[[Tracking income expenses assets and liabilities | Net Worth Database]]**: The total assets and total liabilities within the [[Tracking income expenses assets and liabilities | Net Worth Database]] consider the closing balance of assets and liabilities from this database for each month <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>. All amounts in the [[Tracking income expenses assets and liabilities | Net Worth Database]] are rolled over from this database <a class="yt-timestamp" data-t="04:06:00">[04:06:00]</a>.
*   **[[Tracking income expenses assets and liabilities | Net Worth Summary]]**: Values for calculations like total net worth are pulled from the databases discussed, including the assets and liabilities database <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a>.
*   **Primary Dashboard**: The summary section, monthly net worth overview, [[Asset financials and depreciation | assets breakdown]], and [[Asset maintenance details | liabilities breakdown]] sections of the primary dashboard are all linked to their respective databases, drawing information initially recorded in the assets and liabilities database <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.