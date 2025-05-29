---
title: Causality in marketing and data science
videoId: bTTSg91pFUk
---

From: [[causalpython]] <br/> 

Dr. Juan Orus, a leading advocate for using [[causality_in_marketing_and_product_insight | causality in marketing]], emphasizes that [[causality_in_marketing_and_product_insight | causality]] is not merely a trend but a fundamental framework for better decision-making in various industries. His journey from pure mathematics to data science has equipped him with a unique perspective on applying rigorous thinking to real-world business problems <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Dr. Juan Orus's Journey to Data Science and Causality

Born and raised in Bogota, Colombia, Dr. Orus pursued a PhD in geometric analysis in Berlin, focusing on pure math before geometric deep learning became popular <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. Despite attending prestigious conferences, he realized that pure math didn't bring him happiness <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This led him to transition into data science in 2016 <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

His diverse academic background, including physics and mathematics, provided him with a crucial skillset:
*   **Problem-solving**: Math teaches how to learn and solve problems by breaking them down into manageable steps, preventing overwhelm <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **Strong Toolbox**: Fundamental knowledge like linear algebra is highly applicable, as most industry problems can be reduced to linear algebra problems <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

Dr. Orus's interest in [[causality_in_marketing_and_product_insight | causality]] was sparked by practical necessity. In his early roles in marketing analytics, he observed that traditional methods like linear regression often led to biased estimations when trying to optimize media efficiency or budget <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. He encountered the concept of [[causality_in_marketing_and_product_insight | causality]] through Bayesian modeling, particularly Richard McElreath's "Statistical Rethinking," which dedicates a chapter to DAGs and confounders <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. He saw [[causality_in_marketing_and_product_insight | causality]] as a powerful tool to solve problems he had previously faced <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

## Causal Approach vs. Traditional Approach in Marketing

In marketing, traditional methods often involve throwing all available data into a model, hoping for the best <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. However, the marketing funnel is complex, with channels like TV and paid social creating awareness, and others like search acting as mediators before a final conversion <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. Simply including all variables can lead to biased estimations because of these mediator effects <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

The causal approach, in contrast, requires explicitly identifying which channels and exposures (causes) are relevant. This involves drawing a Directed Acyclic Graph (DAG) that maps out the assumed causal relationships <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. For instance, to get unbiased estimates for media efficiency, certain channels might need to be intentionally excluded from a model to prevent them from masking true effects <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>. Communicating this counter-intuitive idea to marketeers is a significant challenge <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.

## Communicating and Evaluating Causal Models

Pure theory or fundamental arguments are often unsuccessful in convincing stakeholders <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>. Dr. Orus advocates using **simulations** as a powerful communication tool <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. By controlling the "truth" in a simulated environment, one can demonstrate how naive modeling approaches lead to misleading or very wrong results, which can cause significant financial losses <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. This practical demonstration helps convince non-technical audiences without delving into the intricacies of [[causal_inference_and_machine_learning | causal inference]] <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.

The Bayesian framework is particularly well-suited for this purpose because it forces explicit stating of assumptions about the data generation process <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. This transparency allows for understanding variability and incorporating domain knowledge <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. Dr. Orus's background in physics helps in simplifying problems and iterating, focusing on the essence of the problem before adding complexity <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

For model evaluation, alongside statistical techniques, Dr. Orus relies on robustness checks, such as shuffling data, removing data, or adding edges to a DAG that should not affect the estimate if the causal structure is correctly specified <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>. Cross-validations and parallel geo-tests can further validate estimations <a class="yt-timestamp" data-t="00:36:26">[00:36:26]</a>.

## Useful Causal Tools and Concepts

Dr. Orus finds Directed Acyclic Graphs (DAGs) to be the most conceptually helpful tool <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. DAGs allow for explicitly stating assumptions, which is crucial for identifying proper models and understanding potential limitations, even if not directly used for the final model specification <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>.

In terms of Python libraries, he recommends starting with foundational concepts before diving into specific packages. However, for more complex models, popular libraries like `DoWhy` and `EconML` are very useful <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>.

He sees the graphical tradition (Pearl) and potential outcomes framework (Rubin), as well as econometric methods like synthetic control, as complementary <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>. The graphical model helps in choosing the right set of regressors for estimation within the potential outcomes framework <a class="yt-timestamp" data-t="00:22:17">[00:22:17]</a>.

## Starting with Causality in Python

For newcomers to [[causality_in_marketing_and_product_insight | causality]], Dr. Orus advises:
1.  **Focus on Concepts**: Begin by understanding the core conceptual ideas, rather than getting distracted by estimation methods or specific libraries <a class="yt-timestamp" data-t="00:25:25">[00:25:25]</a>.
2.  **Recommended Resources**: "Causal Inference: The Brave and The True" by Matheus is a good starting point as it builds concepts using `statsmodels` for estimation <a class="yt-timestamp" data-t="00:25:03">[00:25:03]</a>. Pearl's books are also valuable for theory, but should be combined with coding practice <a class="yt-timestamp" data-t="00:45:29">[00:45:29]</a>.
3.  **Start Simple**: Don't over-complicate things initially. Writing a linear regression from scratch to understand the fundamentals is a great start <a class="yt-timestamp" data-t="00:25:45">[00:25:45]</a>.
4.  **Fundamentals**: A strong grasp of linear algebra and probability theory is key, as they form the backbone for most data science problems <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>.
5.  **Hands-on Problem Solving**: Engage with concrete problems that genuinely interest you, even if they seem basic. This helps in understanding the core challenges and building practical skills <a class="yt-timestamp" data-t="00:48:05">[00:48:05]</a>.

## Causality as a Fundamental Concept

Dr. Orus firmly believes that [[causality_in_marketing_and_product_insight | causality]] is fundamental for humanity because it's about decision-making <a class="yt-timestamp" data-t="00:43:52">[00:43:52]</a>. He hopes it's not just a trend and emphasizes the need for more causal education in the industry <a class="yt-timestamp" data-t="00:44:24">[00:44:24]</a>.

Causal thinking is valuable for anyone making decisions based on data, not just modelers <a class="yt-timestamp" data-t="00:37:15">[00:37:15]</a>. Intuition can often be misleading, as demonstrated by the example of a child associating putting on gloves with feeling cold, rather than gloves preventing cold <a class="yt-timestamp" data-t="00:38:53">[00:38:53]</a>. Understanding fundamental causal concepts helps decision-makers avoid contradictory results when filtering data or interpreting dashboards <a class="yt-timestamp" data-t="00:37:35">[00:37:35]</a>.

## Applying Symmetry in Modeling

Drawing from his physics background, Dr. Orus highlights the concept of symmetry in modeling. Inspired by Noether's theorem, which states that symmetry implies a conserved quantity <a class="yt-timestamp" data-t="00:27:54">[00:27:54]</a>, he explains that recognizing patterns or symmetries can lead to more efficient computations <a class="yt-timestamp" data-t="00:28:12">[00:28:12]</a>. For example, clustering two concentric circles is complicated in Cartesian coordinates but becomes a simple linear separation in polar coordinates by leveraging rotational symmetry <a class="yt-timestamp" data-t="00:28:47">[00:28:47]</a>. In [[causality_in_marketing_and_product_insight | causality]], fulfilling certain assumptions (symmetries in the causal structure) can simplify complex problems, allowing for easier interventions or counterfactual computations <a class="yt-timestamp" data-t="00:29:15">[00:29:15]</a>.

## Geolift Models in Marketing and Causality

Geolift models are a practical application of [[causality_in_marketing_and_product_insight | causal inference in finance]] <a class="yt-timestamp" data-t="00:31:14">[00:31:14]</a>. They aim to estimate counterfactuals, such as the uplift from a campaign in a specific city (e.g., Berlin) where a true control group is not feasible <a class="yt-timestamp" data-t="00:31:49">[00:31:49]</a>.

The process involves:
1.  **Defining the Counterfactual**: What would conversions have been without the campaign? <a class="yt-timestamp" data-t="00:32:27">[00:32:27]</a>
2.  **Proxying Control**: Using a city with similar historical conversion development (e.g., Hamburg) as a proxy for the control group <a class="yt-timestamp" data-t="00:32:44">[00:32:44]</a>.
3.  **Assumptions and DAGs**: Explicitly stating assumptions about comparability between cities is vital. The DAG can help identify if a chosen proxy is truly suitable <a class="yt-timestamp" data-t="00:32:52">[00:32:52]</a>.
4.  **Methods**: Time-based regression or synthetic control methods can be used, possibly combining data from multiple cities to create a better counterfactual estimate <a class="yt-timestamp" data-t="00:33:14">[00:33:14]</a>.

While not a "silver bullet," geolift methods can work surprisingly well under mild assumptions <a class="yt-timestamp" data-t="00:34:12">[00:34:12]</a>. They are often preferable to purely time-series models, which place all the weight on forecasting the future and thus carry higher uncertainty <a class="yt-timestamp" data-t="00:34:40">[00:34:40]</a>. Geolifts allow for simpler models to achieve better estimations, providing valuable insights for campaigns <a class="yt-timestamp" data-t="00:34:59">[00:34:59]</a>.

## Conclusion

Dr. Juan Orus's insights highlight the transformative potential of [[causality_in_marketing_and_product_insight | causality]] in data science and business. By emphasizing fundamental concepts, explicit assumption-stating through DAGs, and practical communication tools like simulations, he advocates for a more rigorous and effective approach to decision-making beyond traditional [[machine_learning_versus_causal_models_in_business | machine learning]] models. His message underscores the importance of a "childlike curiosity" and continuous learning to navigate the complexities of causal inference and unlock its full value in the industry <a class="yt-timestamp" data-t="00:47:10">[00:47:10]</a>.