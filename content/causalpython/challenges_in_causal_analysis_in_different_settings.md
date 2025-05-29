---
title: Challenges in causal analysis in different settings
videoId: OvmpcL1CKqM
---

From: [[causalpython]] <br/> 

Causal analysis, while crucial for understanding how variables in a system react and making informed decisions <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>, presents several [[challenges_in_causal_inference_and_statistical_analysis | challenges]]. These difficulties span from the fundamental limitations of statistical approaches to practical hurdles in data handling and stakeholder communication.

## Limitations of Pure Statistical Approaches

Early in a career, one might realize that statistics alone is insufficient to answer complex business questions <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. While statistical significance can be observed, it doesn't always translate to meaningful results or explain the underlying data generating process <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. The focus often needs to shift from merely predicting outcomes to understanding who will respond best to an intervention <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

Indeed, formal education in statistics often gives "zero" attention to causal thinking <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>, despite causal inference being a sub-branch of statistics <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. Statistical tools learned primarily focus on statistical associations and do not delve into the data generating process or how things truly operate in real-world scenarios <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.

## Varying Degrees of Confounding Across Settings

One of the significant [[challenges_in_identifying_causal_relationships | challenges in identifying causal relationships]] is controlling for all possible confounders <a class="yt-timestamp" data-t="00:53:30">[00:53:30]</a>. The difficulty of this control varies significantly depending on the setting:
*   **Manufacturing Processes:** These systems tend to be largely isolated from external influences, making it easier to control for most factors <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
*   **Marketing Campaigns or Political Science Research:** These systems are often very open, making it extremely difficult to identify and contain all relevant influences <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.

For instance, in product analytics, users who adopt a certain feature are often more engaged and have a higher initial intent than those who don't <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. This creates a strong sense of confounding, where observed differences in conversion rates might be due to initial user intent rather than the feature itself <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>. While baseline attributes like country or device can be measured, these are often too coarse to capture the full range of user types <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.

## Technical [[challenges_and_methodologies_in_causal_inference | Challenges]] in Data Handling

### Preserving Temporal Information
A key [[challenges_in_causal_inference_and_statistical_analysis | challenge]] arises from the need to preserve temporal information in data. Collapsing data often leads to losing the temporal relation between confounders and the treatment <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This can result in "backwards relationships" where actions that are a *result* of the treatment are mistakenly treated as preceding or causing it, biasing the analysis <a class="yt-timestamp" data-t="00:25:35">[00:25:35]</a>. Controlling for such mediators can make the estimated effect look lower than it should be <a class="yt-timestamp" data-t="00:27:01">[00:27:01]</a>.

### Data Loss and Bias
When structuring data for traditional classification problems, significant data loss can occur. For example, if adoptions and conversions often happen on the same day, framing the problem to ensure adoption precedes conversion can lead to discarding half of conversions and adoptions <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>. This discarding of information is not only about quantity but can also be a biased way of removing crucial data, potentially leading to inaccurate conclusions about feature effectiveness <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>.

### Hidden Confounders
Even with careful temporal structuring, the time criterion alone is not always enough to exclude spurious relations, especially in the presence of hidden confounders <a class="yt-timestamp" data-t="00:29:56">[00:29:56]</a>. This means additional framework development or modeling may be needed to correctly handle such biases <a class="yt-timestamp" data-t="00:30:18">[00:30:18]</a>.

## Practical [[papers_on_practical_challenges_in_causal_research | Challenges]] in Application

### Convincing Stakeholders
One of the biggest [[challenges_in_causal_inference_and_statistical_analysis | challenges]] in applying [[causal_analysis_and_its_importance | causal analysis]] methods is convincing others of their value <a class="yt-timestamp" data-t="00:38:49">[00:38:49]</a>. Organizations already collect and use data for decision-making, so presenting a different aggregation method and demonstrating its value can be difficult <a class="yt-timestamp" data-t="00:39:09">[00:39:09]</a>. It's crucial to set expectations correctly, clarifying that causal methods provide a higher probability of correctness compared to regular associations, rather than an absolute truth <a class="yt-timestamp" data-t="00:40:01">[00:40:01]</a>.

### Building Trust and Transparency
Gaining trust from stakeholders, particularly when results are counterintuitive, is paramount <a class="yt-timestamp" data-t="00:41:54">[00:41:54]</a>. Regardless of how rigorous or sophisticated a method is, if it cannot be clearly tied back to the data, convincing decision-makers becomes very difficult <a class="yt-timestamp" data-t="00:42:25">[00:42:25]</a>. Transparency in calculations, allowing stakeholders to reproduce and verify results, helps foster ownership and belief in the outcomes <a class="yt-timestamp" data-t="00:42:58">[00:42:58]</a>.

## Overcoming [[challenges_of_causal_inference_and_counterfactual_thinking | Challenges]]

Despite the [[challenges_in_causal_inference_and_statistical_analysis | challenges]], [[understanding_and_applying_systematic_processes_in_causal_analysis | understanding and applying systematic processes in causal analysis]] can lead to significant improvements. For example, using methods like survival analysis can address data loss issues related to time-varying treatments and outcomes <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>. This approach allows encoding time-varying covariates, preserving the time dimension, and avoiding discarding valuable information <a class="yt-timestamp" data-t="00:22:18">[00:22:18]</a>.

Working with [[tools_and_frameworks_for_causal_analysis | low resource environments]] means being satisfied with lower degrees of guarantees, but still making estimates "somewhat more causal" which is always better than relying on plain correlations <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>. The goal is to find methods that yield the highest guarantees with the lowest costs <a class="yt-timestamp" data-t="00:35:59">[00:35:59]</a>. Practical successes, such as identifying highly impactful but underutilized features in products, demonstrate the tangible benefits of applying causal analysis despite its complexities <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>.