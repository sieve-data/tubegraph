---
title: Synthetic control methods in causal analysis
videoId: CzL0pV6LyRk
---

From: [[causalpython]] <br/> 

Synthetic control is a causal inference methodology particularly useful for understanding the impact of interventions on a specific unit over time <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. It is considered a quasi-experimental method <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

## When to Use Synthetic Control

This methodology is effective when a treatment or intervention has been administered at a precise time to a unit (e.g., a user, a population, or a product) and you want to understand its effect on that unit <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. It allows for a clearly defined "before treatment" and "after treatment" period <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

It is especially useful in situations where:
*   An intervention happens at a fixed point in time, such as a new feature release or a specific user interaction with an artist <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   It is difficult to identify all relevant confounders to adjust for various factors, or some confounders might be hidden <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. Instead, the method relies on finding a set of "similar enough" units that were not impacted by the treatment to construct a synthetic control <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

## Advantages

*   **Intuitiveness**: Synthetic control is considered a very intuitive method, making it easy for non-experts to grasp the core concept of causality <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

## Challenges and Integration with Causal Frameworks

While intuitive, the method's simplicity can also be a disadvantage, as it might lead to a naive belief that it automatically provides causal identification <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. Traditional synthetic controls, originally developed by economists, often relied on semi-parametric assumptions, such as linear factor models generating time series evolution <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. This semi-parametric form made it challenging to perform [[evaluation_and_systematic_testing_of_causal_models | sensitivity analysis]] to understand what happens if these assumptions are slightly violated <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

### Combining with Directed Acyclic Graphs (DAGs)

To address these limitations, a significant advance involves combining synthetic control with the framework of [[machine_learning_and_causal_inference_methodologies | directed acyclic graphs (DAGs)]] <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. Historically, DAGs were not typically drawn for synthetic control models in the literature <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>. However, drawing a DAG for synthetic control allows for a clearer understanding of the underlying graphical assumptions <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

This integration leads to:
*   **Non-parametric Assumptions**: By conceptualizing underlying drivers as "proxies" rather than relying on specific linear factor models, non-parametric assumptions can be settled upon <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. This approach leverages ideas from proximal causal inference <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
*   **Sensitivity Analysis**: With clear non-parametric assumptions, it becomes possible to build [[evaluation_and_sysetmatic_testing_of_causal_models | sensitivity analysis]] around violations of these assumptions <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. This helps in understanding how much confidence to place in causal estimates if some assumptions are misspecified <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. It allows for setting upper and lower bounds on effect estimates, which can still be sufficient for [[causal_analysis_and_decision_making | business applications]] even if point identification is not possible <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.

## Practical Applications

Synthetic control methods are broadly applicable in big tech companies like Spotify, where interventions happen at fixed points in time <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

### Spotify

At Spotify, synthetic control is used to understand the impact of interventions on specific units, such as a new feature release affecting users or a user interacting with an artist <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. The Advanced Causal Inference Lab at Spotify, headed by Dr. Kieran Gilligan Lee, is having success applying [[application_of_causal_methods_in_industry | causal inference]] beyond just measuring the impact of product launches or features to truly [[causal_analysis_and_decision_making | drive actions]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. These applications are currently in late-stage testing and expected to be publicly discussed soon <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Recommended Resources for Practitioners

For practitioners interested in familiarizing themselves with methods that allow for causal inference even when assumptions are violated, Dr. Kieran Gilligan Lee recommends:
*   "Sense and Sensitivity Analysis" paper by Victor Chernozhukov and collaborators <a class="yt-timestamp" data-t="00:45:33">[00:45:33]</a>. This paper provides a clear introduction to [[evaluation_and_systematic_testing_of_causal_models | sensitivity analysis]], its importance, and how to illustrate it graphically for easy understanding by non-experts <a class="yt-timestamp" data-t="00:45:42">[00:45:42]</a>.
*   Papers and packages by Carlos Cinelli, which are useful for performing sensitivity analyses <a class="yt-timestamp" data-t="00:46:15">[00:46:15]</a>.
*   "Equality Constraints and Causal Inference" by Judea Pearl and his collaborators <a class="yt-timestamp" data-t="00:46:27">[00:46:27]</a>. This resource helps understand where certain assumptions, like equality constraints, appear in various [[machine_learning_and_causal_inference_methodologies | causal inference]] cases and how to derive sensitivity bounds when they are violated <a class="yt-timestamp" data-t="00:46:31">[00:46:31]</a>.