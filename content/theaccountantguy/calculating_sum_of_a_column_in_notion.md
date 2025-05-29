---
title: Calculating sum of a column in Notion
videoId: L97DyZ7U_VA
---

From: [[theaccountantguy]] <br/> 

To [[calculating_total_sales_using_sum_function_in_notion | calculate the sum of a column]] in Notion, especially when you need to use that sum for further calculations within the same database, a common method involves creating a secondary database and establishing relationships and rollups between them <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Example Scenario

Consider a database listing salespeople in different rows, with an "adjustment" column showing their sales amounts <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. For example, Harry has $2,100, Eric has $3,400, and Peter has $5,400 <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. The goal is to see the total sum of these amounts (e.g., $10,900) in an adjacent column <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Steps to Calculate the Sum

### 1. Create a Secondary Database

*   Type `/database` to create a new database <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   Name this database, for example, "Total Sales" <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   Delete any default rows or columns that are not needed <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

### 2. Establish a Relationship Between Databases

*   In your *main* database, click the plus button to add a new column <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   Select `Relation` as the property type <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   Select your newly created "Total Sales" database <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   Configure the relationship by naming the columns in both databases:
    *   In the *main* database, name the column "Total Sales" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
    *   In the "Total Sales" database, name the corresponding column "Sales Details" <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   Once created, new columns will appear in both databases <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   In the *main* database, click on the "Total Sales" column cell for each entry and select the single entry from the "Total Sales" database (assuming you only have one entry to represent the overall total) <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Copy this down to all rows <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This links all sales entries to the single total sales record <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

### 3. Use Rollup to Calculate Sum in Secondary Database

*   In the "Total Sales" database, click the plus button to add a new column <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   Select `Rollup` as the property type <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   From the `Relationship` dropdown, select "Sales Detail" (this is the relationship pointing back to your main sales database) <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   From the `Property` dropdown, select the "sales" value column from your main database <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. This will initially show individual values <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   Under `Calculate`, select `Sum` <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. This will display the total sum of the sales column <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
*   Name this column, for example, "Total Sales Rollup" <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

### 4. Convert Rollup to Formula (Crucial Step)

If you intend to use this summed value in the *main* database for further calculations, you cannot directly roll up a rollup property <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

*   In the "Total Sales" database, add another property <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   Name it, for example, "Total Sales" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   Change its type to `Formula` <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   In the formula editor, simply reference the "Total Sales Rollup" property: `prop("Total Sales Rollup")` <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   You can set the number format to Currency (e.g., Dollars) <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

### 5. Rollup the Formula Property into the Main Database

*   Go back to your *main* database.
*   Add another property <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   Select `Rollup` as the property type <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   Select the "Total Sales" relationship again <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
*   Under `Property`, you can now select the "Total Sales" *formula* property from your secondary database <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   Under `Calculate`, select `Sum` (or `Show original` since there's only one value) <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This will display the overall total sales amount in your main database <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   Name this column, for example, "Sales (Total)" <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

## Further Calculations: Sales Percentage

Once you have the total sales in your main database, you can use [[using_formulas_in_notion | Notion formulas]] to perform further calculations, such as determining each salesperson's contribution as a percentage of the total sales <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

### 1. Create a Formula Property for Percentage

*   Add a new `Formula` property in your *main* database <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   Name it, for example, "Sales in Percentage" <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
*   The basic formula to divide an individual's sales by the total sales is: `prop("Sales") / prop("Sales (Total)")` <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

### 2. Round Decimals and Format as Percentage

To format the percentage to two decimal places:

*   Multiply the result by 100, round it, and then divide by 100 <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   The formula becomes: `round(prop("Sales") / prop("Sales (Total)") * 100) / 100` <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   Finally, change the `Number format` of this property to `Percentage` <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

### 3. Customize with a Bar

You can further enhance the visualization by selecting `Bar` as the `Show as` option within the property settings <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. This provides a visual representation of each individual sales contribution relative to the total <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

## Dynamic Updates

Any changes made to the individual sales values in the main database will automatically update the total sales and percentage calculations, ensuring your data remains current <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.