---
title: Calculating percentages in Notion
videoId: L97DyZ7U_VA
---

From: [[theaccountantguy]] <br/> 

[[calculating_sum_of_a_column_in_notion | Calculating the sum of a column]] in Notion allows for further calculations, such as determining percentages of individual sales amounts against a total. This process involves creating a relational database setup to derive a total sales figure, which can then be used in a formula to calculate percentages.

## Prerequisites: Obtaining Total Sales Value

Before calculating percentages, you need a single total sales value available in your primary database. This is achieved by creating a second database and linking them.

### Database Setup
1.  **Create a Main Sales Database:** Start with a database listing salespeople and their sales amounts. For example, Harry ($2,100), Eric ($3,400), and Peter ($5,400) [00:00:05].
2.  **Create a Second Database:** Type `/` and select `database` to create a new database [00:00:27]. Name this database "Total Sales" [00:00:35].
3.  **Establish a Relationship:**
    *   In your main sales database, add a new column and select `Relation` as the property type [00:01:01].
    *   Select the "Total Sales" database to link it [00:01:04].
    *   Configure the relationship properties: "Total Sales" in the main database and "Sales Details" in the "Total Sales" database [00:01:14].
    *   In the main sales database, for each entry, link it to the single row in the "Total Sales" database. This will feed all sales information into the "Total Sales" database [00:01:33].

### Calculating the Sum with Rollup
1.  **Add a Rollup Property (in "Total Sales" database):** In the "Total Sales" database, add a new property, select `Rollup` [00:01:50].
2.  **Configure Rollup:**
    *   Select the `Sales Detail` relationship [00:01:55].
    *   Select the `Sales` property from the linked database [00:02:00].
    *   Under "Calculate", choose `Sum` [00:02:26]. This will display the sum of all sales values (e.g., $10,900) [00:02:31]. Name this property "Total Sales Rollup" [00:02:40].

### Converting Rollup to a Formula Property
A rollup property cannot be directly rolled up to another database. You must convert its value into a formula property first [00:03:16].
1.  **Create a Formula Property (in "Total Sales" database):** Add another property in the "Total Sales" database, name it "Total Sales", and set its type to `Formula` [00:03:22].
2.  **Link to Rollup:** In the formula editor, simply select the `Total Sales Rollup` property [00:03:31]. You can format this as currency (e.g., Dollars) [00:03:37].

### Rolling Up Total Sales to the Main Database
1.  **Add a Rollup Property (in Main Sales Database):** In your main sales database, add a new column and select `Rollup` [00:02:50].
2.  **Configure Rollup:**
    *   Select the `Total Sales` relationship [00:03:01].
    *   Select the *new formula property* called `Total Sales` (the one you just created) [00:03:52].
    *   Under "Calculate", choose `Sum` [00:03:56].
    *   Name this column "Sales Total" [00:04:06]. This column will now display the grand total of all sales for each row [00:03:58].

## Calculating Percentages

Now that you have the individual `Sales` amount and the `Sales Total` (sum of all sales) in the same database, you can calculate percentages.

1.  **Add a New Formula Property:** In your main sales database, add a new property and select `Formula` as its type [00:04:26]. Name it "Sales in Percentage" [00:04:26].
2.  **Input the Formula:**
    *   The basic calculation is `prop("Sales") / prop("Sales Total")` [00:04:34].
    *   To round this to two decimal places, use the following formula:
        ```notion
        round(prop("Sales") / prop("Sales Total") * 100) / 100
        ```
        This multiplies by 100, rounds to a whole number, and then divides by 100 to get two decimal places [00:04:53].
3.  **Format as Percentage:** Click on the property header, select `Edit property`, then change the `Number format` to `Percentage` [00:05:07].
4.  **Add a Bar (Optional):** To visualize the percentage, you can further customize the property by selecting `Bar` under `Show as` in the property settings [00:05:19].

## Dynamic Updates
Any changes made to individual sales values in the main database will automatically update the "Sales Total" and "Sales in Percentage" columns [00:05:15].