---
title: Explainable AI and feature importance
videoId: bHbqe9q_s-A
---

From: [[causalpython]] <br/> 

Explainable AI (XAI) focuses on making the decisions of AI models understandable to humans. A core aspect of this is understanding the importance of different features in a model's prediction or classification <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

## Sufficiency and Necessity in Explanations

Oja B, a PhD student at Munster Technological University, presented research on how Explainable AI frameworks convey the sufficiency and necessity of features <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

**Key Concepts:**
*   **Sufficiency:** A feature is sufficient if its presence alone is enough to maintain a specific classification <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
*   **Necessity:** A feature is necessary if changing its value would alter the classification <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.

Many State-of-the-art XAI frameworks, such as SHAP, LIME, and DiCE (a [[counterfactual_explanations_and_model_explainability | counterfactual]] library), provide feature importance scores <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. However, these scores can be interpreted in various ways, leading to ambiguity regarding what to infer from a feature importance ranking <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

### The Explanandum Concept
To address this ambiguity, the concept of "explanandum" was developed <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. The explanandum defines what exactly needs to be interpreted from a given feature importance ranking <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. The research aimed to determine if the top-ranked features by frameworks like SHAP truly convey sufficiency or necessity <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.

### Impact of Neighborhoods
XAI frameworks are highly sensitive to the "neighborhoods" (samples) they use for explanations, and different neighborhoods can produce different, sometimes false, explanations <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.
*   **Finding:** Neighborhoods based on samples **outside the decision boundary** performed well in helping frameworks like SHAP convey feature sufficiency and necessity <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

### Takeaway for Practitioners
People should define a specific explanandum before using XAI frameworks to ensure the frameworks are able to convey the desired explanation <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>. If not, experimenting with different neighborhoods can help find relevant answers <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.

> [!WARNING] No Freelance Theorem in Explainable AI
> There is no single XAI framework that will universally work and be reliable in all contexts <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>. It is crucial to be clear about **explanatory requirements** and the target audience <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>. Without clear definitions, explanations can become ambiguous and useless, turning into a "checkbox exercise" for ethical permissions rather than genuinely representing the model <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. Using multiple XAI frameworks with different neighborhood contexts is important to understand the full picture of a model <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.

### Real-World Application in Medicine
Discussions with nephrologists explored developing a more complex explanandum in the medical domain <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>. This involved using feature importance rankings to answer questions like:
*   "Do I need to do further diagnostic tests as per the machine learning model?" <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>
*   "Which is the next most important diagnostic test to perform according to the model?" <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>

This highlights the need for more targeted explanations with clearly defined explananda, moving beyond mere framework development to focusing on what actions stakeholders can take based on the explanations <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.

## Relationship to [[Root cause analysis in causal AI]]
Will Orchard's work on [[root_cause_analysis_in_causal_ai | root cause analysis]] also touches on explainability <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>. The question of "what is a root cause?" is deeply intertwined with concepts of explainability, sufficiency, and necessity <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>. Classifying root cause analysis methods can be done according to the [[causal_ai_and_its_role_in_experiments | causal hierarchy]], depending on whether they treat the problem as an associational, interventional, or [[counterfactual_explanations_and_model_explainability | counterfactual]] question <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>. The challenge lies in formalizing these problems in a way that truly captures human intuition and works effectively in real-world scenarios <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>.

## Recommended Paper
Oja B recommends:
*   "Dear XAI Community" <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>. This paper discusses the lack of standardization in XAI, the need for clear definitions, and the importance of the explanandum, emphasizing the audience and actionable insights from explanations <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>.