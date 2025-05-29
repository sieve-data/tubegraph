---
title: Establishing relationships between databases
videoId: L97DyZ7U_VA
---

From: [[theaccountantguy]] <br/> 

In Notion, you can establish relationships between different databases to perform calculations and aggregate data, such as summing values from a column across multiple entries <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. This process involves [[creating_and_linking_notion_databases | creating and linking databases]] using relationship and rollup properties.

## Steps to Establish Database Relationships

### 1. Create the Secondary Database
Begin by creating a new database that will be used to aggregate information.
*   Type `/database` to create a new database <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   Name this database (e.g., "Total Sales") <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   Remove any default rows if necessary <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

### 2. Connect Databases with a Relationship Property
Next, [[connecting_a_database_in_notion | connect the primary and secondary databases]] using a relationship property.
*   In one of the databases, click the `+` button to add a new property <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   Select "Relation" as the property type <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   Choose the other database you wish to link (e.g., "Total Sales") <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   Configure the column names for the relationship in both databases (e.g., "Total Sales" for the first database and "Sales Details" for the "Total Sales" database) <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   A new column will appear in both databases, indicating the established relationship <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

### 3. Link Entries Between Databases
Once the relationship is established, link the specific rows in the primary database to an entry in the secondary database.
*   In the primary database, click on the new relationship column (e.g., "Total Sales") <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   Select the relevant entry from the secondary database (e.g., the single row in the "Total Sales" database) <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
*   Copy this selection down to apply it to all relevant rows in the primary database <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This action automatically feeds the linked information into the secondary database <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

### 4. Aggregate Data with Rollup Properties
Use a rollup property in the secondary database to perform calculations on the linked data.
*   In the secondary database (e.g., "Total Sales"), add a new property by clicking `+` <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   Select "Rollup" as the property type <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   Choose the relationship you just established (e.g., "Sales Detail") <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   Select the property from the primary database whose values you want to aggregate (e.g., "sales value") <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   Under "Calculate," select "Sum" to get the total of all sales values <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   Rename this rollup column (e.g., "Total Sales Rollup") <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

### 5. Display Aggregated Data in the Primary Database
To display the aggregated sum back in the primary database, an intermediate step is required because rollup values from another database cannot be directly rolled up.
*   **Convert Rollup to Formula:** In the secondary database, create a new "Formula" property <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. Name it (e.g., "Total Sales") <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. Link this formula to the "Total Sales Rollup" property by entering `prop("Total Sales Rollup")` into the formula field <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. Format it as currency if applicable <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Rollup the Formula:** In the primary database, add another "Rollup" property <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. Select the same relationship (e.g., "Total Sales") <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Now, select the newly created "Total Sales" formula property from the secondary database <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. Under "Calculate," select "Sum" again <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This will display the total sales value from the second database onto the first <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.

### 6. Perform Further Calculations (Optional)
Once the total is available, you can perform additional calculations, such as percentage contribution.
*   Add a new "Formula" property (e.g., "Sales in Percentage") <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   Divide the individual sales amount by the total sales (e.g., `prop("Sales") / prop("Sales Total")`) <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   To format to two decimal places, use `round(prop("Sales") / prop("Sales Total") * 100) / 100` <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   Change the number format to "Percentage" <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   You can further customize the display by selecting "Bar" for a visual representation <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

Any changes made to individual sales values in the primary database will automatically update the total sales and percentage calculations <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This method is useful for [[managing_customer_databases | managing customer databases]], [[setting_up_databases_for_income_tracking | income tracking]], and [[creating_and_managing_databases_in_notion | creating and managing complex data structures]] within Notion. Future uses of database integration include [[exporting_pdf_documents_using_a_database | exporting PDF documents using a database]], [[integrating_databases_with_templates_in_notion | integrating databases with templates]], and [[connecting_notion_templates_with_a_database_for_automation | connecting Notion templates with a database for automation]], potentially leveraging [[steps_to_integrate_databases_with_api_keys_in_notion | API keys]].