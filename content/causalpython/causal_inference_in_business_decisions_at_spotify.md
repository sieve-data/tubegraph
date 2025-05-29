---
title: Causal inference in business decisions at Spotify
videoId: CzL0pV6LyRk
---

From: [[causalpython]] <br/> 

At Spotify, [[Causal inference and decision theory | causal inference]] is a critical tool for understanding and driving business decisions, moving beyond simple impact assessments to actively informing strategic actions <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Dr. Kieran Gilligan Lee, Head of the Advanced Causal Inference Lab at Spotify, emphasizes that businesses aim for actions with desired effects, which necessitates a causal understanding of problems <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Why Causal Inference at Spotify?

Most business questions revolve around understanding the effects of actions <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. While large tech companies like Spotify heavily rely on data to train models for optimal actions, this data is often observational <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. Observational data inherently contains biases, such as selection bias, which can distort conclusions about cause and effect <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. To answer fundamental causal questions, [[Causal inference and decision theory | causal inference]] is essential to identify and remove these biases, transforming biased data into actionable insights for business outcomes <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## Applications and Methodologies

Spotify has been applying [[Causal inference and decision theory | causal inference]] to drive actions beyond simply measuring the impact of product launches or new features <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Many of these projects are in their final testing stages <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

### Synthetic Control

One particularly useful methodology at Spotify is **synthetic control** <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. This method is highly effective when an intervention or "treatment" occurs at a precise time for a specific unit (e.g., a user or population) <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. It allows for a clearly defined "before" and "after" treatment period <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

In contexts like Spotify, where identifying and adjusting for all potential confounders can be challenging <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>, synthetic control offers a solution by using similar, unaffected units to construct a "synthetic" counterpart <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. This synthetic control helps understand the impact of the intervention on the treated unit <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. This approach is well-suited for many big tech problems, such as new feature releases on a specific day or a user's fixed interaction with an artist <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

While intuitive <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>, it's crucial to acknowledge that synthetic control doesn't automatically provide causal identification <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

### Combining Synthetic Control with DAGs and Sensitivity Analysis

Historically, synthetic controls were developed by economists, and their assumptions were often semi-parametric (e.g., linear factor models) <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. However, connecting these methods to the structural causal model (SCM) framework, particularly using Directed Acyclic Graphs (DAGs), provides a clearer understanding of underlying assumptions <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

By drawing a DAG for the synthetic control model, researchers can shift from stringent semi-parametric assumptions to non-parametric ones <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a> <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. This allows for the application of tools from proximal [[Causal inference and decision theory | causal inference]], where underlying drivers are treated as proxies without assuming specific functional relationships <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>. This non-parametric approach enables more robust sensitivity analysis <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. Sensitivity analysis helps determine how much confidence one should have in causal estimates if assumptions are slightly violated, allowing for the setting of bounds on causal effects <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a> <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.

## Building Trust in Causal Models

A common concern for machine learning practitioners is the number of assumptions required for causal methods <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. However, having to explicitly state and deeply consider these assumptions is seen as a benefit, as it forces a thorough evaluation of the data generation process <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

Challenges in [[Causal inference and machine learning | causal machine learning]] engineering, compared to traditional ML, involve ensuring that misspecifications of variables don't significantly alter outcomes <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>. A naive approach might be to control for all possible confounders, but this can lead to worse estimates if some variables are not true confounders (e.g., colliders) <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. Therefore, a crucial prior step is to model the causal relationships (e.g., with a DAG) to determine the appropriate adjustment set <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.

To build trust:
*   **Domain Knowledge**: Leverage domain expertise to identify the most important confounders and understand the potential impact of unmeasured ones <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.
*   **Sensitivity Analysis**: If an assumption is violated, sensitivity analysis can quantify how much the causal effect estimate might change, allowing for the establishment of upper and lower bounds <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. This can still lead to valuable conclusions, such as determining if a causal effect is non-zero <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.

## Future of Causal AI at Spotify

Spotify is actively working on projects powered by [[Causal AI in business applications | causal inference]] that aim to drive actions and build new products <a class="yt-timestamp" data-t="00:51:58">[00:51:58]</a> <a class="yt-timestamp" data-t="00:50:05">[00:50:05]</a>. The objective is to apply causal inference in novel ways, moving beyond retrospective analyses to proactive decision-making.

A significant future horizon involves **causal representation learning** <a class="yt-timestamp" data-t="00:53:24">[00:53:24]</a>. Currently, many big tech companies learn embeddings of users and products based on co-occurrence data (correlations) <a class="yt-timestamp" data-t="00:53:31">[00:53:31]</a>. However, for recommendation engines, which aim to find "treatments" (content) to "cause" enjoyment, using correlation-based embeddings might not be ideal <a class="yt-timestamp" data-t="00:54:07">[00:54:07]</a>. The goal is to learn a *causal representation* of users that identifies the underlying latent factors explaining why users are similar or enjoy certain content <a class="yt-timestamp" data-t="00:54:10">[00:54:10]</a>. If successful at Spotify, this approach could then be applied to higher-stakes domains like medicine <a class="yt-timestamp" data-t="00:54:21">[00:54:21]</a>.

This approach views personalized recommendations as similar to medical treatments: finding a song to cause enjoyment is analogous to finding a treatment to decrease symptoms <a class="yt-timestamp" data-t="00:52:47">[00:52:47]</a>. By demonstrating the utility of causal inference in a lower-stakes environment like music recommendations, Spotify aims to pave the way for its wider adoption in more critical areas <a class="yt-timestamp" data-t="00:53:03">[00:53:03]</a>.