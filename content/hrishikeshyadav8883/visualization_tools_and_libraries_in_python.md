---
title: Visualization Tools and Libraries in Python
videoId: fKlEWWmNF_Q
---

From: [[hrishikeshyadav8883]] <br/> 

Effective data visualization is a crucial component of [[Exploratory Data Analysis EDA | EDA]], allowing for the showcasing of insights and patterns from data in an understandable way [00:03:56]. The goal is to make hidden patterns, trends, and behaviors from data clear to both technical and non-technical audiences [00:04:25]. Visualizing data helps in developing hypotheses and making informed decisions [00:04:56].

## Why Visualize Data?
When data is in a table form, it is difficult to understand, but when it is presented in a plot, more insights can be gained [01:46:05]. Visualization helps in:
*   Effectively communicating actionable insights to stakeholders [01:14:17].
*   Enabling better decision-making for corporates [01:22:14].
*   Saving time and resources by providing clear analysis [01:13:10].
*   Positively impacting organizations by informing strategic paths [01:18:18].

## Python Visualization Libraries
[[Python libraries for video editing | Python]] offers powerful libraries for creating various data visualizations:

*   **Matplotlib**
    *   A very basic library for visualization [01:09:37].
    *   Requires explicit specification of almost everything for best visualization [01:08:12].
    *   Its functionalities can be used with other libraries like Seaborn [01:09:47].
*   **Seaborn**
    *   Provides more functionality and an "edge" over Matplotlib [01:09:44].
    *   Assigns different colors to different bars in a bar chart automatically [01:08:29].
    *   Requires less coding compared to Matplotlib [01:08:32].
*   **Plotly**
    *   Considered very useful due to several advantages [01:10:11].
    *   **Interactive**: Allows users to interact with plots (e.g., hovering to see specific values) [01:10:27]. This interactivity helps in finding more hidden insights [01:11:22].
    *   **Better Communication**: Facilitates better communication of insights through interactive dashboards and reports [01:11:28].
    *   Offers extra features and more functionality, such as changing themes and background colors, and includes editing/cropping tools [01:11:48].
*   **Other Libraries**: Bokeh and GGPlot are also available [01:09:17].

## Types of Charts and Their Use Cases
The choice of chart type depends on the specific objective [01:47:11].

*   **Line Chart**: Used when dealing with time-series data, where the x-axis represents time [01:47:42].
    *   *Examples*: Revenue over time, energy consumption over days/time, Google searches over time [01:48:10].
*   **Multiple Line Charts**: Used to display multiple characteristics on a single plot, such as various stock prices over time [01:48:29].
*   **Area Chart**: Similar to a line chart but with the area below the line filled [01:48:57]. Stacked area charts also exist [01:49:04].
*   **Bar Chart**: Suitable when the characteristic names on the y-axis are large, or there are many categories [01:49:10].
*   **Column Chart**: Used when there are fewer categories [01:49:29].
*   **Scatter Plot**: Used to explore the relationship between two features [01:49:52].
    *   *Example*: Displaying the relationship between time spent on a platform and customer churn [01:50:53].
*   **Connected Scatter Plot**: Combines features of line charts and scatter plots by connecting data points [01:52:00].
*   **Card**: Showcases a specific number or aggregated value. Primarily used in sales dashboards. [01:52:24]
    *   *Content*: Can display average, mean, median, or other aggregation functions [01:53:17].
    *   *Examples*: Revenue to date, sign-ups for a promotion [01:53:24]. Helps to understand the status of a metric [01:53:34].
*   **Table Chart (Pivot Table)**: Useful for displaying smaller datasets (e.g., five to ten rows) [01:53:48].
*   **Gauge Chart**: Helps track progress towards a target [01:53:59].
    *   *Mechanism*: An arrow indicates current progress against a target line [01:54:05]. If the arrow is above the target, it indicates profitability [01:54:21].

### Effective Visualization Principles
*   **Clarity and Simplicity**: Presentations should be clear, simple, and concise, allowing the visualization itself to explain what is happening without additional verbal explanation [01:17:08].
*   **Focus on Key Insights**: If dealing with many labels, focus on the top five or ten major distributions [01:17:35]. For example, a bar chart is often preferred over a pie chart when there are many categories, as pie charts can be cluttered and difficult to interpret percentages [01:55:51]. Pie charts are recommended for displaying top six or eight categories [01:56:09].

## Business Intelligence (BI) Tools
Beyond [[Python libraries for video editing | Python]] libraries, Business Intelligence (BI) tools are widely used for data analysis and visualization, especially in organizational settings [01:58:18]. These tools are geared towards decision-making and are particularly useful for generating dashboards and reports for businesses [01:58:23].

*   **Excel**: A traditional and still highly valued tool for all types of analysis and visualization [01:34:31]. Mastering Excel is crucial as much raw organizational data exists in spreadsheet form [01:37:14].
*   **Tableau**: A popular BI tool widely used in organizations [01:57:47]. Often requires a license for use [01:59:59].
*   **Power BI**: Another highly popular BI tool [01:57:49].
    *   Often preferred if an organization doesn't have a Tableau license [02:01:05].
    *   Developed by Microsoft, offering a familiar environment to Excel users, including Power Query Editor and DAX queries [02:01:25].
    *   Provides numerous built-in [[Visualization Techniques in Data Analysis | visualization techniques]] (e.g., 30 in the free version) and community-contributed types [01:59:09].
    *   More than 500 Fortune companies reportedly use Power BI as a major tool [02:00:46].
*   **Data Studio (Google Looker Studio)**: Provided by Google, can be run on a browser without download [01:57:56]. While convenient, it may have fewer functionalities compared to Tableau and Power BI [01:58:08].
*   **Looker**: Part of Google Cloud Platform (GCP), used for big data analytics [01:57:24].
*   **Google BigQuery**: Works in conjunction with Looker [01:58:12].

These BI tools are increasingly integrating machine learning capabilities, particularly for regression and time series analysis [02:03:28].

## Automated [[Exploratory Data Analysis EDA | EDA]] Tools
[[Auto EDA Tools and Techniques | Automated EDA]] tools automate the process of data loading, cleaning, pre-processing, analysis, and visualization [01:18:19]. They perform data analysis tasks automatically using algorithms and software [01:19:06].

*   **Libraries**: Sweetviz, D-tale, Pandas Profiling, AutoViz, and EDAViz are [[Python libraries for video editing | Python]] libraries for [[Auto EDA Tools and Techniques | automated EDA]] [01:20:27].
*   **Pros**:
    *   **Time-saving**: Automates time-consuming and repetitive tasks, especially for large and complex datasets [01:21:01].
    *   **Ease of Use**: Easily accessible for non-technical users [01:21:18].
    *   **Standardization**: Helps reduce errors and improves reliability of analysis [01:20:18].
    *   **Efficiency**: Faster in cleaning, processing, and analyzing data [01:21:41].
*   **Cons**:
    *   **Over-reliance Risk**: Should not be overly relied upon as it can impact critical thinking [01:21:51].
    *   **Limited Customization**: Designed for predefined data analysis tasks and lacks customization [01:22:17].
    *   **Lack of Domain Expertise**: Algorithms lack the domain expertise required for nuanced analysis [01:23:01].
    *   **Data Quality Issues**: May not always detect or correct all data quality issues like missing or incorrect data [01:23:35].

While [[Auto EDA Tools and Techniques | automated EDA tools]] provide quick overviews and help in understanding data distributions and correlations, human analysis is often preferred for deeper, customized insights [01:23:51]. However, using [[Auto EDA Tools and Techniques | Auto EDA]] to understand data initially and then performing detailed manual [[Exploratory Data Analysis EDA | EDA]] can be very useful [01:24:17].