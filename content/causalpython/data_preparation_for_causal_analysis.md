---
title: Data preparation for causal analysis
videoId: Q7sinHrknC8
---

From: [[causalpython]] <br/> 

Data preparation is a critical and complex phase in [[Causal analysis and decision making|causal analysis]], demanding as much expertise in causality as the development and application of causal methods themselves <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>. This stage involves transforming raw data into a structured format suitable for causal inference, typically a matrix of covariates, treatments, and outcomes <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>.

## Importance of Proper Data Analysis
Improper data analysis is considered ineffective and a waste of resources used to gather data <a class="yt-timestamp" data-t="00:24:46">[00:24:46]</a>. It is also seen as disrespectful to the patients or individuals who contributed their time and hopes to the data collection process <a class="yt-timestamp" data-t="00:49:42">[00:49:42]</a>. Analyzing data properly involves respecting the data generating process <a class="yt-timestamp" data-t="00:49:16">[00:49:16]</a>.

## Challenges in Data Preparation
[[Challenges in implementing causal analysis in practice|Challenges in implementing causal analysis in practice]] regarding data preparation include:
*   **Data Origin and Purpose** <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>: Most databases (e.g., insurance claims, electronic health records, marketing events, banking transactions) are not curated for research. They are created for different purposes, such as audits, which means they do not inherently fit the needs of a causal analysis <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>.
*   **Fitting Data to Causal Models** <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>: It is difficult to take existing raw data and reshape it to be consumed by causal inference machinery <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.
*   **Specific Data Requirements** <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>: Analysts need to determine which covariates to select for adjustment, ensuring they are measured at a specific point in time (e.g., before treatment). Defining follow-up times and "Time Zero" for observations is also complex <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>.
*   **Expectations from Machine Learning** <a class="yt-timestamp" data-t="00:29:53">[00:29:53]</a>: The "deep learning revolution" has fostered an expectation that models can "figure it out" from raw data without extensive feature engineering or careful data input considerations <a class="yt-timestamp" data-t="00:29:53">[00:29:53]</a>. However, [[Assumptions in causal inference|identification]] in causal inference cannot be fully automated and always requires metadata <a class="yt-timestamp" data-t="00:30:17">[00:30:17]</a>. This often leads to disappointment among practitioners who expect an "easy solution" and instead face the need for rigorous understanding of the underlying data generating processes <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>.

## Key Steps and Considerations

### Understanding the Domain
Before even looking at the data, it's crucial to understand the domain <a class="yt-timestamp" data-t="00:21:14">[00:21:14]</a>. This involves interviewing domain experts, such as doctors or physicians in healthcare settings, to:
*   Set up the problem <a class="yt-timestamp" data-t="00:21:37">[00:21:37]</a>.
*   Identify the questions to be answered <a class="yt-timestamp" data-t="00:21:43">[00:21:43]</a>.
*   Understand the complexities in answering those questions <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>.
*   Guide the selection of data to collect and the estimate to pursue <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>.

Extracting this knowledge and distilling it into a sensible format for causal analysis (e.g., a directed acyclic graph or DAG) is a communication-heavy and slow process <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>. For example, physicians often have a better understanding of the treatment decision process than what determines an outcome <a class="yt-timestamp" data-t="00:22:27">[00:22:27]</a>, which can reveal crucial covariates for adjustment <a class="yt-timestamp" data-t="00:23:21">[00:23:21]</a>.

### Data Structuring for Causal Inference
A proposed solution to make data preparation easier is to automate the process of taking event-based databases and converting them into the matrix format required for causal analysis <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a>. This would be more beneficial than simply developing new methodologies <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>.

### High-Throughput Analysis Considerations
In projects like drug repurposing, where hundreds of drug candidates might be evaluated, high-throughput analysis is necessary <a class="yt-timestamp" data-t="00:35:11">[00:35:11]</a>. This implies:
*   **Automation:** Using tools like Docker to run analyses in parallel for efficiency <a class="yt-timestamp" data-t="00:35:25">[00:35:25]</a>.
*   **Multiplicity Issue:** Accounting for the large number of comparisons in the analysis <a class="yt-timestamp" data-t="00:35:34">[00:35:34]</a>.
*   **Standardization vs. Tailoring:** It's often impossible to tailor a specific DAG design for each treatment-outcome pair when dealing with hundreds of candidates <a class="yt-timestamp" data-t="00:35:55">[00:35:55]</a>. Trust in data richness (e.g., comprehensive patient diagnostics, tests, and prescriptions) is key to capturing the inherent health state of patients <a class="yt-timestamp" data-t="00:36:05">[00:36:05]</a>.
*   **Variable Selection:** Incorporating variable selection methods and proximal [[Causal analysis and decision making|causal inference]] methodologies can increase confidence in estimates <a class="yt-timestamp" data-t="00:36:32">[00:36:32]</a>.
*   **Triangulation:** Results from observational analyses, especially high-throughput ones, should always be triangulated with evidence from other sources (e.g., scientific literature, large language models trained on medical publications) to gain more confidence in promising candidates <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>.