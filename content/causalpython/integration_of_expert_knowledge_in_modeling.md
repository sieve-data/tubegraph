---
title: Integration of expert knowledge in modeling
videoId: Hc3rIGmX59k
---

From: [[causalpython]] <br/> 

The integration of expert knowledge into modeling is a crucial aspect of developing more robust and reliable systems, especially in the context of causality and machine learning. This approach moves beyond purely data-driven models to incorporate human understanding and domain-specific insights, leading to more informed decisions and better performance in dynamic environments <a class="yt-timestamp" data-t="00:27:29">[00:27:29]</a>.

## Importance and Benefits

Expert knowledge plays a vital role in several areas:
*   **Guiding Models** Expert knowledge helps in defining the structure of causal models, such as building Directed Acyclic Graphs (DAGs) <a class="yt-timestamp" data-t="00:55:28">[00:55:28]</a>. It can provide a "very precise idea" of where to focus, like knowing that gold pockets are at the bottom of a hill, which can steer a model to look in specific areas <a class="yt-timestamp" data-t="00:53:31">[00:53:31]</a>.
*   **Constraining Search Space** In fields like [[advancements_in_causal_modeling_and_ai | causal discovery]], where the search space grows "super exponentially" with the number of nodes, expert knowledge can significantly reduce this space by excluding certain edges or parameters <a class="yt-timestamp" data-t="00:55:41">[00:55:41]</a>. For [[personalized_models_in_experimental_research | optimal experimentation]], it helps by "contracting this search space" for parameters <a class="yt-timestamp" data-t="00:56:01">[00:56:01]</a>.
*   **Improving Model Accuracy and Reliability** By integrating expert knowledge, especially "physics knowledge," models can exclude "physically inconclusive or nonsensical" regions in the parameter space, enhancing realism <a class="yt-timestamp" data-t="00:53:47">[00:53:47]</a>. This ensures that models are not just statistically sound but also scientifically plausible <a class="yt-timestamp" data-t="00:54:02">[00:54:02]</a>.
*   **Slicing the Polytop** In the context of partial identification, expert knowledge acts as a "cost assumption" that helps "slice down a cube" (representing the causal problem) by removing parts, thereby lowering the upper bound of a causal effect and tightening the bounds, bringing the estimate closer to the true effect <a class="yt-timestamp" data-t="00:49:51">[00:49:51]</a>, <a class="yt-timestamp" data-t="00:58:07">[00:58:07]</a>.

## Challenges and Considerations

Despite its benefits, the integration of expert knowledge presents challenges:
*   **Cost of Expert Knowledge** Obtaining high-quality expert knowledge can be expensive. The amount spent on acquiring and integrating this knowledge directly impacts the quality of the results <a class="yt-timestamp" data-t="00:56:53">[00:56:53]</a>.
*   **Subjectivity and Correctness** Expert knowledge can be subjective or even wrong <a class="yt-timestamp" data-t="00:58:18">[00:58:18]</a>. Methods are needed to "recover from that" if the expert knowledge is incorrect. Bayesian approaches can mitigate this by allowing true data to "overrule the wrong expert knowledge" as more data is collected, though this comes at the cost of data acquisition <a class="yt-timestamp" data-t="00:58:26">[00:58:26]</a>.
*   **Preference Elicitation** The process of formally incorporating expert knowledge into a model is known as "preference elicitation" <a class="yt-timestamp" data-t="00:56:13">[00:56:13]</a>. Tuning parameters in surrogate models used for Bayesian optimization can be linked to expert knowledge to find optimal solutions more efficiently <a class="yt-timestamp" data-t="00:53:26">[00:53:26]</a>.

## Applications and Future Directions

The trend is moving away from purely "Big Data" models that aim to explain everything, towards models that strategically incorporate expert knowledge <a class="yt-timestamp" data-t="00:57:21">[00:57:21]</a>. This is particularly relevant for:
*   **Material Science** Applying these methods to Material Science involves integrating the knowledge of material scientists into the model to optimize processes like designing microcomputer chips, leading to cheaper and more advanced technologies <a class="yt-timestamp" data-t="00:54:15">[00:54:15]</a>.
*   **Causal Bounding Questions** In cases of partial identification, expert knowledge, particularly about "edges whether they're directed or bidirected," significantly impacts the bounds of causal effects <a class="yt-timestamp" data-t="00:57:42">[00:57:42]</a>.
*   **Beyond Generative Models** While generative models like GPT and Llama have been successful with associative methods, they often fail when the "world changes" because they lack [[Integration of Causal Thinking in Machine Learning | causal thinking]] <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>. Integrating expert knowledge addresses this by bringing human insight into the model, recognizing that experts "know these things better than a machine" <a class="yt-timestamp" data-t="00:57:29">[00:57:29]</a>.

Ultimately, integrating expert knowledge is seen as a way to "be smart as smart as you can be" in scientific inquiry, leading to more defensible and practical causal results <a class="yt-timestamp" data-t="00:56:21">[00:56:21]</a>.