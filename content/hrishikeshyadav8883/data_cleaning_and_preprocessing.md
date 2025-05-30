---
title: Data Cleaning and Preprocessing
videoId: fKlEWWmNF_Q
---

From: [[hrishikeshyadav8883]] <br/> 

Data cleaning and preprocessing are essential parts of any data science or machine learning project <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. They fall under the "data preparation" stage of the machine learning process <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>, where data is prepared before it is sent to a model <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>. This process involves dealing with missing values, performing preprocessing, and analyzing the data <a class="yt-timestamp" data-t="00:24:57">[00:24:57]</a>.

## Importance in Data Analysis

Data cleaning and preprocessing are crucial for several reasons:
*   **Identify Data Quality** It helps to identify if the provided data is valid and to address issues like missing values <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
*   **Improve Model Accuracy** By cleaning data and selecting relevant features, the accuracy of a model is enhanced <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Standardization** These steps help to standardize columns <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a> and entire datasets for better prediction <a class="yt-timestamp" data-t="00:23:09">[00:23:09]</a>.

## Data Cleaning Techniques

### Handling Missing Values
Missing values are a common data quality issue <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. Strategies for dealing with them include:
*   **Elimination** If a significant portion of a column (e.g., more than 60%) contains null values, it might be best to drop that column entirely <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.
*   **Filling** For smaller numbers of missing values (e.g., 200-300 rows in a 35,000-row dataset), methods like mean, median, or mode can be used to fill the gaps <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>.

### Identifying and Dealing with Outliers
Outliers are data points that exhibit unusual behavior compared to other data points in the dataset <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>.
*   **Identification** Outliers can be visualized using a [[Visualization Techniques in Data Analysis | box plot or whisker plot]] <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>. Points that are far away from the main range of the data are considered outliers <a class="yt-timestamp" data-t="00:27:48">[00:27:48]</a>.
*   **Elimination** While outliers can be useful for understanding specific events, they typically need to be eliminated when building a model to prevent significant impact on predictions <a class="yt-timestamp" data-t="00:32:01">[00:32:01]</a>. Techniques for elimination include:
    *   Interquartile Range (IQR) method <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>.
    *   Z-score method <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>.

## Data Preprocessing Techniques

Data transformation is a key part of preprocessing <a class="yt-timestamp" data-t="00:37:53">[00:37:53]</a>.
*   **Converting Data Types** Ensuring data types are correct (e.g., converting a numerical column recognized as an object) is crucial <a class="yt-timestamp" data-t="00:37:55">[00:37:55]</a>.
*   **Feature Engineering** This involves creating new features from existing ones to gain better insights or improve model performance <a class="yt-timestamp" data-t="00:38:15">[00:38:15]</a>. For example, an "age" column can be transformed into "age bins" (Young, Adult, Senior) to better understand user segments <a class="yt-timestamp" data-t="00:39:06">[00:39:06]</a>.
*   **Encoding Categorical Data** Models cannot directly process string labels (e.g., Male/Female). These need to be encoded into numbers:
    *   **Label Encoding** Assigns a unique number to each category (e.g., Male=0, Female=1) <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>.
    *   **One-Hot Encoding** Creates new binary columns for each category (e.g., 'Male' column and 'Female' column, with 1 indicating presence and 0 indicating absence) <a class="yt-timestamp" data-t="00:33:13">[00:33:13]</a>. This is particularly useful for [[Building Fashion Assistance using RAG | recommendation systems]] or finding frequent item sets <a class="yt-timestamp" data-t="00:33:39">[00:33:39]</a>.
*   **Standardization/Normalization** Scaling data to a common range (e.g., using Min-Max Scaler) is often done to help models with prediction <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.

## Role in Machine Learning Workflow

Data cleaning and preprocessing are integral to the overall machine learning workflow. They primarily occur in the "data preparation" stage, which follows business understanding and data understanding, and precedes modeling, evaluation, and deployment <a class="yt-timestamp" data-t="00:24:46">[00:24:46]</a>. [[Exploratory Data Analysis EDA | EDA]] itself is considered part of this data preparation phase <a class="yt-timestamp" data-t="00:25:51">[00:25:51]</a>.

## Tools and Libraries

These tasks can be performed using various tools:
*   **Traditional Tools** Excel is a powerful tool for all types of analysis and visualization <a class="yt-timestamp" data-t="00:34:31">[00:34:31]</a>.
*   **Programming Libraries** Python libraries like NumPy (for numerical operations) <a class="yt-timestamp" data-t="01:08:47">[01:08:47]</a> and Pandas (for data manipulation and DataFrames) <a class="yt-timestamp" data-t="01:09:04">[01:09:04]</a> are widely used.
*   **Business Intelligence (BI) Tools** Tools like Tableau and Power BI allow for [[Visualization Techniques in Data Analysis | data analysis]] and visualization without extensive coding, often using an Excel-like environment with features like DAX queries <a class="yt-timestamp" data-t="00:35:17">[00:35:17]</a>. These are popular in organizations for creating interactive dashboards and reports <a class="yt-timestamp" data-t="00:36:23">[00:36:23]</a>.
*   **[[Auto EDA Tools and Techniques | Auto EDA Tools]]** Libraries like Sweetviz, D-tale, Pandas Profiling, AutoViz, or EDAViz can automate many of the data cleaning and analysis tasks, generating comprehensive reports with minimal code <a class="yt-timestamp" data-t="01:20:27">[01:20:27]</a>. While efficient for large datasets or quick insights, over-reliance can hinder critical thinking and customization <a class="yt-timestamp" data-t="01:21:51">[01:21:51]</a>.