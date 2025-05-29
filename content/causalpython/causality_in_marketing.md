---
title: Causality in marketing
videoId: bTTSg91pFUk
---

From: [[causalpython]] <br/> 

[[causality_in_marketing_and_decisionmaking | Causality]] is described as a fundamental concept for humanity, providing a framework for improved decision-making processes <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. Curiosity is identified as a key component in this field <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This article explores the role of [[causality_in_marketing_and_decisionmaking | causality]], particularly in marketing, through the insights of Dr. Juan Orús.

## Dr. Juan Orús: A Journey from Pure Math to [[causality_in_marketing_and_decisionmaking | Causal Data Science]]

Dr. Juan Orús, born and raised in Bogotá, Colombia, pursued his PhD in geometric analysis, a field related to geometric deep learning <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Despite attending prestigious conferences, he realized that pure mathematics did not bring him happiness <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This led him to transition into data science, where he became a leading advocate for using [[causality_in_marketing_and_decisionmaking | causality in marketing]] <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

Orús's career path is diverse, having started in physics, specifically particle physics, before shifting to mathematics due to an interest in geometry <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. His academic background in mathematics provided him with a strong problem-solving approach, enabling him to break down complex industry problems into manageable pieces <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. He emphasizes that math teaches how to learn to solve problems and provides a robust toolbox, particularly linear algebra, which he sees as fundamental <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

The transition from academia to industry was challenging, as it required understanding data problems from a business, not academic, perspective <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. He found his passion for data science in 2016, drawn to it not because it was "hot" but because it felt like a good field to apply his knowledge <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

## The Imperative of [[causality_in_marketing_and_decisionmaking | Causality in Marketing]]

Dr. Orús recognized the need for [[causality_in_marketing_and_decisionmaking | causality]] early in his career, especially when dealing with marketing analytics problems like estimating media efficiency and optimizing budgets <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. Traditional methods, such as linear regression, often involved "throwing everything into the model" and hoping for the best, leading to "tortured data" and unnatural outcomes <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

### Traditional vs. [[causality_in_marketing_and_decisionmaking | Causal Approach]]

In traditional marketing modeling, especially for media mix models, marketeers often believe that including all data and channels will allow them to compete in a regression framework to derive ROI <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. However, this approach can lead to biased estimations due to the complex nature of the marketing funnel <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

For instance, channels like TV or out-of-home advertising create awareness, while search channels act as mediators between initial touchpoints and final conversions <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. Simply including all channels in a model can mask effects or lead to misleading results, as a mediator effect will cause bias <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>. The [[causal approach]] requires explicitly identifying channels and effects, often necessitating multiple models and strategically leaving out certain channels to avoid masking effects <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

### Communicating [[causality_in_marketing_and_decisionmaking | Causal Concepts]]

Communicating the need for [[causality]] to stakeholders who may not be technical is challenging because it requires structuring complex concepts <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. Pure theory or fundamental arguments are often unsuccessful <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

> "You need to show them something, like prove something, and this is where I see simulations as a great tool because you control the truth." <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>

Simulations allow demonstrating how naive modeling approaches can lead to very wrong and costly decisions <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. By showing the true effects versus biased estimations, stakeholders become more convinced without needing to delve into the intricate details of [[causal inference]] <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

### Iterative Process

An iterative approach, starting with simpler models and gradually adding complexity, is crucial in industry settings where speed and quick results are important <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. Delivering initial, understandable results helps stakeholders get a feel for the end product and its utility for decision-making, allowing for further iterations with additional features or uncertainty quantification <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>.

> "If you're going to have a perfect model in a year, that's pretty much useless, right? Because we need to make decisions now." <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>

## Tools and Methods in [[applications_of_causal_models_in_business_and_marketing | Causal Marketing]]

### Bayesian Framework and DAGs

The [[causality_and_causal_models | Bayesian framework]] is well-suited for [[causal modeling]] because it forces explicit statement of assumptions about the data generation process <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. This clarity helps in setting up simulations, understanding variability, and incorporating domain knowledge <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.

Directed Acyclic Graphs (DAGs) are a highly useful conceptual tool for understanding [[causality_and_causal_models | causal models]] <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. DAGs allow for explicitly stating assumptions as a graph of nodes and connections, which can then be processed by software or calculus to systematically derive the necessary model structure for estimation <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.

> "Definitely thinking about DAG makes everything much transparent." <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>

### Combining Causal Traditions

Dr. Orús views different [[causality_and_causal_models | causal traditions]], such as Pearl's graphical models and Rubin's potential outcomes framework, as complementary rather than separate <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>. While the potential outcomes approach might be easier to grasp initially, graphical models and the do-calculus become invaluable for automating the selection of regressors to achieve proper estimation <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>.

DAGs are crucial because they force one to state assumptions, which is hard but essential <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>. This transparency reveals potential limitations or infeasibility of estimations from observational data, even if the DAG itself isn't directly used to specify the model <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>.

### Quasi-experimental Methods (Geo-lift)

[[applications_of_causal_models_in_business_and_marketing | Geo-lift]] is a common quasi-experimental method in marketing used to estimate counterfactuals <a class="yt-timestamp" data-t="00:31:36">[00:31:36]</a>. For example, to assess the impact of a TV campaign in Berlin where a control group isn't feasible, Geo-lift uses a "synthetic control" from a similar city like Hamburg (or a combination of cities) that had a comparable conversion development <a class="yt-timestamp" data-t="00:31:49">[00:31:49]</a>. This synthetic control estimates what Berlin's conversions would have been without the campaign, allowing for the calculation of the uplift <a class="yt-timestamp" data-t="00:32:15">[00:32:15]</a>.

While planning Geo-lift can be complex due to city selection and boundary considerations, the method itself is not inherently hard and can work "surprisingly well" under mild assumptions <a class="yt-timestamp" data-t="00:33:02">[00:33:02]</a>. It's often preferred over solely relying on time series models (like [[causal impact]]), which place too much weight on prediction and can have large uncertainty bands <a class="yt-timestamp" data-t="00:34:30">[00:34:30]</a>.

## [[causality_and_machine_learning | Causality and Machine Learning]]

While acknowledging the potential of large language models (LLMs) in areas like creativity and communication optimization, Dr. Orús notes that their application in marketing is still in early stages due to the need for careful message control and brand safety <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>. He primarily uses LLMs to boost personal productivity (e.g., GitHub Copilot, text summarization) <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>.

### Useful Causal Tools in Python

For practical application, once the causal problem is properly specified with a DAG, various Python libraries can be used <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a>. Dr. Orús mentions DoWhy and EconML as particularly useful <a class="yt-timestamp" data-t="00:21:15">[00:21:15]</a>.

## Challenges and Future Outlook

### Model Evaluation

Model evaluation in [[causal modeling]] involves two main components: the causal structure (DAG) and the estimation process <a class="yt-timestamp" data-t="00:35:34">[00:35:34]</a>. For the causal component, techniques like testing the stability of estimates when shuffling data, removing data, or adding/removing edges in the graph are crucial <a class="yt-timestamp" data-t="00:35:58">[00:35:58]</a>. In marketing, parallelizing with Geo-tests or uplift tests can help cross-validate causal estimates, acknowledging that discrepancies might hint at areas for deeper investigation rather than indicating a wrong model <a class="yt-timestamp" data-t="00:36:26">[00:36:26]</a>.

### Broader Adoption of [[causality_in_artificial_intelligence | Causal Thinking]]

Dr. Orús believes that [[causal thinking]] is valuable not only for modelers but for anyone making decisions <a class="yt-timestamp" data-t="00:36:55">[00:36:55]</a>. Without fundamental causal understanding, even seemingly simple actions like filtering dashboard data can lead to contradictory or biased results if variables like colliders are conditioned upon <a class="yt-timestamp" data-t="00:37:31">[00:37:31]</a>.

> "Having certain fundamental [[causality]] without going into the very kind of core formalism is definitely something that decision makers should over all have because we can all be and I've been fooled by my intuition." <a class="yt-timestamp" data-t="00:37:46">[00:37:46]</a>

He hopes that [[causality]] is not just a trend but a fundamental concept for humanity, especially for decision-making <a class="yt-timestamp" data-t="00:43:52">[00:43:52]</a>. More [[causal education]] and thinking are needed in industry, ensuring it's seen as a fundamental concept rather than a fleeting hype or tool <a class="yt-timestamp" data-t="00:44:24">[00:44:24]</a>.

## Learning Resources and Advice

For those starting with [[causality_in_science_and_industry | causality]], Dr. Orús recommends focusing on fundamental concepts rather than being distracted by estimation methods or specific libraries <a class="yt-timestamp" data-t="00:25:25">[00:25:25]</a>.

*   **Books**:
    *   *Statistical Rethinking* by Richard McElreath (introduces [[causality]] within a [[causality_and_causal_models | Bayesian framework]]) <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>
    *   *Causal Inference: The Brave and The True* by Matheus Facure (builds concepts using `statsmodels` for estimation) <a class="yt-timestamp" data-t="00:25:03">[00:25:03]</a>
    *   Pearl's books (for theory lovers) <a class="yt-timestamp" data-t="00:45:28">[00:45:28]</a>
*   **Practice**:
    *   Combine reading with hands-on coding and simulations to make abstract concepts tangible <a class="yt-timestamp" data-t="00:45:40">[00:45:40]</a>.
    *   Experiment by distorting data or assumptions to understand when methods break and how sensible they are <a class="yt-timestamp" data-t="00:46:31">[00:46:31]</a>.
    *   Embrace curiosity and challenge what you read <a class="yt-timestamp" data-t="00:47:10">[00:47:10]</a>.
    *   Focus on solving concrete problems that genuinely interest you, even if they are basic, to gain practical experience <a class="yt-timestamp" data-t="00:48:05">[00:48:05]</a>.

> "Going through the pain of solving a very concrete problem which interested you, it's a great way." <a class="yt-timestamp" data-t="00:49:34">[00:49:34]</a>

He advises focusing on fundamental fields like linear algebra and probability theory, which provide a "backbone" and "intuition" applicable across many industry problems, unlike fleeting hot technologies <a class="yt-timestamp" data-t="00:41:39">[00:41:39]</a>.