---
title: Root cause analysis in causal AI
videoId: bHbqe9q_s-A
---

From: [[causalpython]] <br/> 

Root cause analysis, explanations, and [[causal_discovery_and_inference_in_ai | causal discovery]] are key areas of research, as discussed at the Clear Conference on Causal Learning and Representation <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Will Orchard from the University of Cambridge, who also interned at Amazon, focuses on root cause analysis <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.

## Focus of Work

Will Orchard's work on root cause analysis tackles two main directions:
1.  **Formalization**: How root cause analysis should be formalized as a [[causality_in_ai | causal]] problem <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.
2.  **Real-world Application**: Its application to real-world problems, such as those found in microservice-based applications <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.

### Formalizing Root Cause Analysis

Existing works on root cause analysis have typically not approached it from a [[causal_reasoning_in_ai | causal]] perspective, despite "cause" being in the name <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>. Orchard's approach involves reviewing existing methods to identify a unifying [[causal_reasoning_in_artificial_intelligence | causal]] description for them <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>.

Root cause analysis methods can be classified according to the [[causal_reasoning_in_ai | causal]] hierarchy, based on how they conceptualize a root cause <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>. This includes considering whether it's an associational, interventional, or counterfactual question <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>. Orchard's classification initially involved categorizing existing methods, with a particular interest in the counterfactual approach, influenced by his collaboration with Dominic Janing <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.

## Challenges

Several [[challenges_in_developing_ai_with_causal_understanding | challenges]] exist in this work:
*   **Formalization Intuition**: Determining the best way to formalize a problem that accurately captures the inherent intuition about how it should be asked <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>. [[causality_in_ai | Causality]] can offer compelling answers on whether an explanation for a root cause is good <a class="yt-timestamp" data-t="00:18:58">[00:18:58]</a>.
*   **Real-world Applicability**: Verifying if the formalization works effectively for real-life problems <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>. This requires engaging with engineers who work with the data and have developed their own heuristics, ensuring the formalization captures their experiences <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.

## Key Learnings and Insights

*   **Depth of the Question**: The question "what is a root cause?" is profound and deeply interconnected with other [[causality_in_ai | causal]] questions, including explainability, sufficiency, necessity, and the relationship between anomalous/rare values and interventions <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>.
*   **Engineer Engagement**: It can be challenging to convince engineers of the importance and utility of [[causal_ai_and_its_role_in_experiments | causal]] methods <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>.

## Desired Impact

A significant impact desired for this work is the availability of **standardized public datasets** for evaluating root cause analysis methods <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a>. Currently, many methods are developed without a [[causal_reasoning_in_ai | causal]] perspective, often benchmarked using proprietary simulated data that is not publicly released <a class="yt-timestamp" data-t="00:20:54">[00:20:54]</a>. This makes it difficult to understand how problem formalization is reflected in benchmarking results <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>. Publicly accessible datasets are crucial for demonstrating the importance of [[causal_ai_in_business_applications | causal]] approaches and understanding which methods work best in practice <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>. The hope is that such datasets will lead to a consensus on the best way to approach root cause analysis <a class="yt-timestamp" data-t="00:21:31">[00:21:31]</a>.

## Resources

Will Orchard's work, including the paper, is available on arXiv, and the dataset can be found on a Git repository <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>. Relevant search terms include "Pet Shop data set Amazon" <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.

## Related Concepts/Papers

*   **Score-based [[causal_discovery_and_inference_in_ai | causal discovery]] methods**: Orchard finds inspiration in theoretical work regarding identifiability results and the use of score matching for [[causal_discovery_and_inference_in_ai | causal discovery]], specifically mentioning the Score algorithm and the No-Gan method <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>.
*   **Heavy-tail distributions**: Work on using heavy-tail distributions for [[causal_discovery_and_inference_in_ai | causal discovery]] and identifiability <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.