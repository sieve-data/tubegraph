---
title: Challenges in causal machine learning compared to traditional methods
videoId: CzL0pV6LyRk
---

From: [[causalpython]] <br/> 

Businesses typically aim to take actions that bring about desired effects, which fundamentally requires understanding problems from a causal perspective <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While traditional machine learning often relies on large datasets to train models for predictions, this data is often observational and susceptible to biases like selection bias <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. To answer business questions that are inherently causal, [[causal_inference_and_machine_learning | causal inference]] is necessary to remove these biases from observational data and enable good actionable decisions <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## Fundamental Challenges

### Assumptions and Trust
One of the primary [[benefits_and_challenges_of_causal_machine_learning | challenges in causal machine learning]] compared to traditional methods lies in the explicit nature of assumptions <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. Deep learning practitioners, for instance, might initially find the numerous assumptions in causal methods daunting, forgetting that their own calculations often rely on inherent assumptions like the Independent and Identically Distributed (IID) assumption <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

> [!NOTE] Assumptions as a Feature, Not a Bug
> Having to make assumptions upfront and think deeply about them is considered a "feature, not a bug" of [[causal_inference_and_machine_learning | causal inference]] <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. This forces practitioners to consider if the data generation process for a specific problem reasonably satisfies these assumptions, or if a different methodology is needed <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

### Controlling for Confounders
A common challenge is controlling for confounders. While ideally all relevant confounders should be measured, this is often impossible <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. Domain knowledge can help prioritize confounders, and sensitivity analysis can be used to set bounds on how much an effect estimate might change if unmeasured confounders were present <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. If these bounds do not intersect zero, it may still be possible to claim a non-zero causal effect <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.

### Engineering Challenges in Causal ML
[[challenges_and_solutions_for_adopting_causal_ml_in_different_fields | Challenges and solutions for adopting causal ML in different fields]] engineering often involve significant additional work to prevent misspecification of variables from leading to large changes in outcomes <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.

*   **Naive Conditioning:** A naive approach might be to condition on all potential confounding variables, which can number in the hundreds or thousands in applications like Spotify <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. However, blindly controlling for many variables can lead to worse estimates, as some may not be confounders but rather colliders between the treatment and outcome <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.
*   **Prior Step of Causal Graphing:** Before engineering, it's crucial to deeply consider the Directed Acyclic Graph (DAG) to identify true confounders and determine the appropriate adjustment set <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
*   **Methodology Choice:** Data characteristics, such as noise and variance, should guide the choice of methodology (e.g., double machine learning vs. inverse propensity weighting) to ensure confidence in causal effect estimates and maximize data utility <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.

## Surprising Revelations and Pitfalls

### Flipping Relative Orderings
A surprising insight from [[impact_of_causal_machine_learning_beyond_academia | applying causal modeling in industry]] is that the relative orderings of actions or treatments, based on their raw correlations with an outcome, can completely flip after controlling for confounding variables <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>. This means a treatment with a smaller raw correlation might have a larger causal effect than one with a big correlation <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>. This contrasts with intuitive assumptions, such as those sometimes found in the Bradford Hill criteria for causality, where consistency and strength of correlation are considered indicators <a class="yt-timestamp" data-t="00:22:38">[00:22:38]</a>.

### Spurious Correlations
Spurious correlations, like the number of drownings correlating with movies featuring Nicholas Cage, highlight the human tendency to seek explanations for observed associations <a class="yt-timestamp" data-t="00:22:51">[00:22:51]</a>. Reichenbach's Principle of Common Cause formalizes this: if two things are correlated, there should be an explanation <a class="yt-timestamp" data-t="00:24:17">[00:24:17]</a>. This explanation could be a common cause in their mutual past, or simply a random statistical fluctuation due to a small number of data points or a specific time scale <a class="yt-timestamp" data-t="00:24:26">[00:24:26]</a>. Changing the time scale of observation might eliminate or weaken the correlation <a class="yt-timestamp" data-t="00:26:44">[00:26:44]</a>.

## Building Trust and Moving Forward

To build trust in [[machine_learning_and_causal_inference_methodologies | causal models]], understanding assumptions and their potential violations is key. Sensitivity analysis, particularly methods that allow for non-parametric assumptions, helps quantify how much causal estimates change if assumptions are slightly violated <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. This allows for setting bounds on causal effects, even if precise point identification isn't possible, providing confidence in the findings <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

The future of [[advances_in_causal_machine_learning_research | advances in causal machine learning research]] in industry involves moving beyond retrospective analysis (e.g., evaluating past product launches) to building new products and driving decisions with [[causal_inference_and_machine_learning | causal inference]] <a class="yt-timestamp" data-t="00:50:04">[00:50:04]</a>. A key area for improvement is Causal Representation Learning, which aims to learn embeddings of users or products based on true causal factors rather than mere correlations, potentially leading to more effective recommendation systems in domains like music streaming and even [[application_of_causal_machine_learning_in_medicine | medicine]] <a class="yt-timestamp" data-t="00:53:24">[00:53:24]</a>.