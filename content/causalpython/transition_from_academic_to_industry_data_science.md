---
title: Transition from academic to industry data science
videoId: bTTSg91pFUk
---

From: [[causalpython]] <br/> 
Dr. Juan Orus, originally from Bogotá, Colombia, made a significant [[transition_from_physics_to_finance|transition from pure mathematics]] to applied data science and has become a prominent advocate for using [[causal_machine_learning_applications_in_various_industries|causality in marketing]] <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. His journey highlights the challenges and advantages of moving from an academic environment to the industry <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## Academic Background and Shift
Juan Orus earned his PhD in geometric analysis <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. Despite attending prestigious conferences in his field, he realized that pure math did not make him happy <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This realization came to a breaking point during his time at the Fields Institute in Canada, where he found himself unhappy despite being at a prestigious conference <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. He describes his career path as non-linear, having started with physics before moving to pure math <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

He decided to explore other fields, picking up a book called "Data Science for Dummies" in September 2016 <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. Through networking in Berlin, he met people in data science, which felt like the most interesting field for him to apply his knowledge, even though it wasn't hyped at the time <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

## Challenges and Benefits of the Transition
The transition from academia to industry was "pretty tough" <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. A key challenge was learning to understand data problems from a business perspective rather than an academic one <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

However, his pure mathematics background proved to be incredibly helpful <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>:
*   **Problem-Solving**: Math teaches how to learn and solve problems by breaking them down into smaller, manageable steps <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. This approach makes tackling hard, ill-defined industry problems less daunting <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Strong Toolbox**: Fundamental concepts like linear algebra are crucial, as many industry problems can be reduced to linear algebra problems <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
*   **Mindset**: His physics background also instilled the principle of simplifying phenomena to their essence before adding complexity, which is vital for building models iteratively <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.

## Integrating Causality and Bayesian Methods
Orus recognized the need for [[causality_in_science_and_industry|causality]] early in his career, especially when dealing with marketing analytics problems where traditional statistical models like linear regression often led to biased estimations <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. He found that simply "torturing the data to get a story" was not ideal <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

His journey into causality was heavily influenced by [[applications_of_bayesian_modeling_in_industry|Bayesian modeling]], particularly after reading Richard McElreath's "Statistical Rethinking," which introduces causality within a Bayesian framework <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. He found that the Bayesian framework forces explicit assumptions about the data generation process, which is very helpful for simulations <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. These simulations are key for communicating complex causal concepts to stakeholders, as they allow demonstrating misleading results from naive approaches <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

### Key Tools and Concepts
*   **Directed Acyclic Graphs (DAGs)**: Orus finds the concept of a model as a DAG to be very natural and transparent, forcing one to state assumptions explicitly <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>. While challenging initially, this framework helps systematically define the model structure needed for proper estimation <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.
*   **Iterative Process**: He advocates for starting with simpler models and iterating, especially in industry, where speed and timely results are critical <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. This allows for immediate value delivery before adding complexity or [[integration_of_uncertainty_estimation_in_data_science|uncertainty quantification]] <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.
*   **Quasi-Experimental Methods**: He uses methods like GeoLift to estimate counterfactuals when A/B tests are not feasible, such as measuring the impact of a city-wide campaign <a class="yt-timestamp" data-t="00:31:30">[00:31:30]</a>. These methods, while not silver bullets, are convenient approximations that work surprisingly well under mild assumptions <a class="yt-timestamp" data-t="00:34:12">[00:34:12]</a>.
*   **Model Evaluation**: For [[challenges_in_deploying_causal_models_in_industry|causal models]], evaluation involves both statistical techniques and robustness checks, such as shuffling data or adding/removing edges in a DAG to see how stable the estimate remains <a class="yt-timestamp" data-t="00:35:34">[00:35:34]</a>.

## Broader Implications and Advice
Orus believes [[causality_in_science_and_industry|causal thinking]] is fundamental for humanity, not just a trend, as it provides a framework for better decision-making <a class="yt-timestamp" data-t="00:43:52">[00:43:52]</a>. He emphasizes the need for more [[collaboration_between_academia_and_industry|causal education]] in the industry <a class="yt-timestamp" data-t="00:44:24">[00:44:24]</a>.

His advice for those entering fields like machine learning, Bayesian modeling, or causality:
*   **Focus on Fundamentals**: Prioritize understanding core concepts like linear algebra and probability theory over chasing "hot" libraries or technologies <a class="yt-timestamp" data-t="00:41:39">[00:41:39]</a>.
*   **Solve Concrete Problems**: Gain practical experience by tackling real problems that genuinely interest you, even if they are simple at first <a class="yt-timestamp" data-t="00:48:02">[00:48:02]</a>. This hands-on approach helps overcome anxiety and builds confidence <a class="yt-timestamp" data-t="00:49:50">[00:49:50]</a>.
*   **Embrace Curiosity and Iteration**: Maintain a childlike curiosity <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>, don't blindly trust everything you read <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>, and be open to learning new things <a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a>. Running simulations and testing when assumptions break is crucial for building intuition <a class="yt-timestamp" data-t="00:46:26">[00:46:26]</a>.