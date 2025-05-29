---
title: Causal tools and methodologies in business applications
videoId: bTTSg91pFUk
---

From: [[causalpython]] <br/> 

Causality is considered fundamental for humanity, offering a framework to enhance the [[causal_analysis_and_decision_making | decision-making]] process, with curiosity being a key component <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. Dr. Juan Orus, a leading advocate for using causality in marketing, emphasizes its importance in industry applications <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Dr. Juan Orus's Journey into Data Science

Dr. Orus, originally from Bogotá, Colombia, pursued a PhD in geometric analysis in Berlin <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Despite attending prestigious conferences, he realized pure mathematics did not make him happy <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This led him to transition into data science, a field he found interesting and a good fit for applying his learned skills, even though it wasn't "hype" at the time <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. His background in pure mathematics, particularly in areas like linear algebra, taught him how to learn and approach complex problems by breaking them down, which has been immensely helpful in his applied work <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

## The Necessity of Causal Thinking in Industry

Orus realized the need for causality early in his career, especially when dealing with marketing analytics and optimization problems <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. Traditional methods, such as linear regression, often led to "torturing the data to get a story" and produced misleading results, particularly when trying to estimate media efficiency or optimize budgets <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. He discovered the language of causality through Richard McElreath's "Statistical Rethinking," a book that focuses on Bayesian statistics with a strong emphasis on causality <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

### Limitations of Traditional Approaches in Marketing

In the context of marketing, traditional approaches often involve throwing all available data and channels into a model, assuming they will compete in a regression framework <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. However, the marketing funnel is complex, with channels like TV creating awareness, and others like search acting as mediators before a final conversion <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. Simply including all variables can lead to biased estimations <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. A causal approach necessitates identifying specific channels and explicitly stating assumptions, often requiring multiple models and sometimes even leaving out certain channels to avoid masking effects <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

## Tools and Communication Strategies

To communicate complex causal concepts to non-technical stakeholders, Dr. Orus found that pure theory or fundamental arguments are not very successful <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>. Instead, he advocates for using simulations <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. By controlling the "truth" in a simulation, he can demonstrate how naive modeling approaches lead to "very wrong" and potentially costly decisions, thereby convincing stakeholders without delving into the intricate details of causal inference <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

The [[machine_learning_and_causal_inference_methodologies | Bayesian framework]] is particularly well-suited for this, as it forces explicit assumptions about the data generation process, which is crucial for running effective simulations and understanding variability <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. His background in physics also influenced his approach, promoting the idea of modeling phenomena by starting simple, identifying the essence of the problem, and then iteratively adding complexity <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

## Key Causal Concepts and Tools

Conceptually, [[causal_discovery_algorithms_and_realworld_applications | Directed Acyclic Graphs (DAGs)]] are most helpful <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>. DAGs allow one to explicitly state assumptions about the model as a graph, making the process systematic and transparent <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>. For software, popular Python libraries like `do-sampler` and `econ-ml` are useful, though a strong conceptual understanding precedes the choice of tooling <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>.

### Combining Causal Traditions

Dr. Orus believes that different causal traditions, such as Pearl's graphical models and Rubin's potential outcomes framework, complement each other <a class="yt-timestamp" data-t="00:22:02">[00:22:02]</a>. While Rubin's approach may be easier to initially understand, DAGs and do-calculus become invaluable for automating the selection of regressors to ensure proper estimation <a class="yt-timestamp" data-t="00:22:10">[00:22:10]</a>. DAGs are particularly advantageous for quasi-experimental methods (e.g., synthetic control) because they force the explicit stating of assumptions, revealing potential limitations or infeasibility of estimation from observational data <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>.

### Geo-Lift Models in Marketing

Geo-lift models are a specific application in marketing used to estimate counterfactuals when a traditional control group is unavailable <a class="yt-timestamp" data-t="00:31:38">[00:31:38]</a>. For example, to measure the impact of a TV campaign in Berlin, where splitting the city into treatment and control groups is impossible, one can use a "synthetic control" from other cities (e.g., Hamburg, Munich) with similar historical conversion developments <a class="yt-timestamp" data-t="00:32:40">[00:32:40]</a>. This allows for the estimation of what conversions would have been without the campaign, revealing the actual uplift <a class="yt-timestamp" data-t="00:32:50">[00:32:50]</a>. These methods can work "surprisingly well" under mild assumptions, providing good estimations, especially when uncertainty is properly controlled <a class="yt-timestamp" data-t="00:34:12">[00:34:12]</a>.

### [[evaluating_and_explaining_causal_models_in_industry | Evaluating Causal Models]]

[[evaluating_and_explaining_causal_models_in_industry | Model evaluation]] involves assessing both the causal structure and the estimation process <a class="yt-timestamp" data-t="00:35:34">[00:35:34]</a>. For the causal component, techniques include testing estimate stability by shuffling data, removing data, or adding/removing edges on the DAG to see their effect <a class="yt-timestamp" data-t="00:35:58">[00:35:58]</a>. In marketing, estimations from causal models (like media mix models) can be cross-referenced with Geo-tests or uplift tests to see their agreement, which helps identify areas for deeper investigation <a class="yt-timestamp" data-t="00:36:26">[00:36:26]</a>.

## Broader Impact and Learning Advice

Causal thinking extends beyond modelers; it's crucial for anyone making decisions from data, such as business analysts or marketing managers <a class="yt-timestamp" data-t="00:37:05">[00:37:05]</a>. Without fundamental causal understanding, even simple actions like filtering dashboards by variables that are colliders can lead to contradictory results and incorrect decisions <a class="yt-timestamp" data-t="00:37:33">[00:37:33]</a>.

For those starting with causality, Dr. Orus advises focusing on the fundamentals, such as linear algebra and probability theory, rather than getting distracted by specific estimation techniques or "hot" libraries <a class="yt-timestamp" data-t="00:41:41">[00:41:41]</a>. Key resources recommended include:
*   "Statistical Rethinking" by Richard McElreath <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
*   Pearl's books for theoretical understanding <a class="yt-timestamp" data-t="00:45:28">[00:45:28]</a>.
*   "Causal Inference: The Brave and The True" by Matheus, which focuses on concepts and uses `statsmodels` for estimation <a class="yt-timestamp" data-t="00:25:03">[00:25:03]</a>.

The advice is to always combine reading with coding, running simulations, and experimenting with assumptions to build intuition <a class="yt-timestamp" data-t="00:45:38">[00:45:38]</a>. Furthermore, solving concrete problems, even small ones, can be a great learning experience, helping individuals overcome anxiety and build confidence in their abilities <a class="yt-timestamp" data-t="00:48:02">[00:48:02]</a>.

## Causality: A Fundamental for Humanity

Dr. Orus firmly believes that causality is not merely a trend but "fundamental for Humanity" as it offers a framework for improved [[causal_analysis_and_decision_making | decision-making]] <a class="yt-timestamp" data-t="00:43:52">[00:43:52]</a>. He emphasizes the need for greater [[application_of_causal_methods_in_industry | causal education]] and thinking in industry to prevent it from being viewed as a temporary hype or too complex for investment <a class="yt-timestamp" data-t="00:44:24">[00:44:24]</a>. It should be recognized as a core concept for better decisions <a class="yt-timestamp" data-t="00:44:42">[00:44:42]</a>.