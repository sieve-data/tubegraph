---
title: Structural causal models and machine learning
videoId: QAzAFess1AA
---

From: [[causalpython]] <br/> 

The Causal Bandits podcast, known for its focus on [[causality_and_machine_learning | causality and machine learning]], hosted Dr. Thomas Wiecki, an expert in Bayesian modeling and the developer of a recognizable Python probabilistic programming framework, PyMC (PMC) <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This article explores his insights into the intersection of [[causal_ai_and_machine_learning | causal AI and machine learning]], particularly through the lens of Bayesian approaches and their practical applications.

## Dr. Thomas Wiecki's Journey to Bayesian Modeling

Dr. Thomas Wiecki began learning programming as a child by modifying code examples from a book <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. He was fascinated by the idea of creating something from nothing and controlling systems <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. His academic journey led him through neuroscience and bioinformatics, where he "fell in love with Bayesian modeling" <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

A pivotal moment occurred when he realized the broad applicability of Bayesian modeling beyond his PhD research <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Working at Quantopian, a fintech startup focused on crowdsourced hedge funds, he found the same tools could solve "completely orthogonal problems" like portfolio construction <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. This showed him that the tool was useful not just academically but also for industry and many data science problems requiring deep understanding and incorporation of knowledge into the model <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

Wiecki's motivation stems from the creativity involved in programming and model building, but primarily from the community aspect of open-source development <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. He finds it immensely rewarding to work with talented people at PyMC Labs, pushing the boundaries of what's possible and enabling humanity to solve "potentially massive problems" like climate change <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

## Integrating Causality into PyMC

A significant recent development in PyMC is the addition of a [[causal_reasoning_and_structural_causal_models | causal do operator]] <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. While Wiecki doesn't consider himself a "causal expert," his Bayesian background provides a helpful lens for learning about causality <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. He notes that the two fields—Bayesian statistics and causal inference—have largely developed independently but have interesting cross-connections <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

The main driving force behind the `do` operator integration was Ben Vincent, who mapped causal theory into a language accessible to Bayesian modelers <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. Ricardo V. Marques implemented the operator, which fit well into the PyMC framework despite requiring graph manipulation <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. This addition is considered a "critical missing piece" to make PyMC a framework for answering [[causality_and_causal_models | structural causal problems]] <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

## Connecting Bayesian Modeling and Causality

Wiecki's first encounter with [[causal_reasoning_and_structural_causal_models | causal inference]] was at a conference where he observed structural causal models being used to answer data science questions <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. He immediately recognized the similarity to Bayesian modeling, which often involves building "data generative processes" <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. Initially, no one could articulate the difference, but now Wiecki believes "those two things are the same just to a different lens through a different framework" <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.

### Benefits of Bayesian Framework for Causal Inference

1.  **Transparency and Communication**: While terms like "priors" and "uncertainty" can be hard for non-experts to grasp, "talking about causality... really resonates with a lot of people" <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. It intuitively makes sense that to act effectively, one must understand what causes what <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.
2.  **Focus on Actionability**: The ultimate purpose of data science is to "make better actions" or "make better decisions" <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. This requires understanding how actions affect outcomes, which is fundamentally a [[causal_reasoning_and_structural_causal_models | causal question]] <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. Relying solely on prediction can lead to errors in decision-making, as illustrated by a marketing example where predictive models led to "pure losses" for three years <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.
3.  **Beyond Black-Box ML**: While black-box [[machine_learning_and_causality | machine learning algorithms]] might be suitable for pure forecasting, Wiecki argues that many problems where they are applied would benefit more from a [[causal_reasoning_and_structural_causal_models | causal approach]] <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>. A more careful understanding of the problem and building a model that maps the [[causality_and_causal_models | causal structure]] is crucial for solving real business problems and ensuring the relevance of data science <a class="yt-timestamp" data-t="00:18:37">[00:18:37]</a>.

## Challenges and Solutions in Structural Thinking

Many people are "afraid that if they need to explicitly define this structure... they are just afraid that it will be wrong" <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>. Wiecki's advice is to embrace being wrong: "it's great to be wrong... that's how we learn" <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>.

Key points on this approach:
*   **Iterative Model Building**: Start with a simple model and use tools like posterior predictive checks and simulations to identify when and how it's wrong <a class="yt-timestamp" data-t="00:20:16">[00:20:16]</a>. This iterative process leads to learning about the data and the problem <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>.
*   **Collaboration with Domain Experts**: Building [[causality_and_causal_models | structural models]] facilitates communication with domain experts <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>. Their insights can help improve the model, leading to solutions that combine expertise with data-driven approaches, fostering trust <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>.
*   **Subjectivity in Modeling**: All modeling, including [[machine_learning_and_causality | machine learning]], involves subjective choices in data processing, outlier removal, normalization, and algorithm selection <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>. Bayesian modeling encourages being "conscious about them and transparent" <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a>.

## Human Cognition, Models, and Practical Applications

Wiecki notes an interesting research direction in cognitive neuroscience: the hypothesis that the human brain operates using Bayesian updating <a class="yt-timestamp" data-t="00:24:55">[00:24:55]</a>. This parallels how we start with beliefs, apply them, learn, and update those beliefs <a class="yt-timestamp" data-t="00:25:21">[00:25:21]</a>. Humans also build internal [[causality_and_causal_models | causal models]] of the world, providing helpful intuitions for how computers should learn <a class="yt-timestamp" data-t="00:25:38">[00:25:38]</a>.

### Local vs. Global Causal Models
In practice, Wiecki's team often builds "localized specialized models" as a starting point, avoiding overly ambitious models that tend to "crumble" <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a>. However, there's a "huge appeal to these global models" due to the complex interactions between different factors <a class="yt-timestamp" data-t="00:27:40">[00:27:40]</a>.

Using marketing as an example, a global model could integrate:
*   Different types of marketing (brand vs. performance) <a class="yt-timestamp" data-t="00:28:11">[00:28:11]</a>.
*   Competitors' marketing efforts <a class="yt-timestamp" data-t="00:28:45">[00:28:45]</a>.
*   Price elasticity and competitor pricing <a class="yt-timestamp" data-t="00:29:03">[00:29:03]</a>.
*   Linking different datasets, such as marketing spend, purchasing behavior, and lift tests <a class="yt-timestamp" data-t="00:29:28">[00:29:28]</a>.

Regarding exogenous variables (noise), the decision to include or simplify them "depends on... the specific problem and data set" <a class="yt-timestamp" data-t="00:31:15">[00:31:15]</a>. The approach is to test if simplifying noise terms works; if not, more structure is added <a class="yt-timestamp" data-t="00:31:31">[00:31:31]</a>. In practice, they tend to err on the side of including more, as they often feel "underutilized in terms of what the data can provide" <a class="yt-timestamp" data-t="00:31:54">[00:31:54]</a>.

### Variable Selection in Bayesian vs. Frequentist Causal Models
In [[causality_and_causal_models | causal models]] using a frequentist approach, variable selection is critical to avoid biases (e.g., from including a collider or not including confounders) <a class="yt-timestamp" data-t="00:33:13">[00:33:13]</a>. However, in the Bayesian framework, one can "just include it all" in the structural model, and the inference process will incorporate the structure correctly <a class="yt-timestamp" data-t="00:34:50">[00:34:50]</a>.

A key advantage of the Bayesian approach is its ability to provide robust parameter estimates. Frequentist point estimates can often be "biased or noisy," especially in complex models like hierarchical models, leading to misleading results <a class="yt-timestamp" data-t="00:35:43">[00:35:43]</a>. Bayesian methods, often utilizing Markov Chain Monte Carlo (MCMC), provide the full posterior distribution, allowing for more representative mean estimates <a class="yt-timestamp" data-t="00:36:51">[00:36:51]</a>.

### Generative Nature of Bayesian Models
The generative nature of Bayesian models is a powerful tool. In the Bayesian workflow, before fitting a model to data, one can build the hypothesized [[causal_reasoning_and_structural_causal_models | causal structure]] and then "generate data" from it <a class="yt-timestamp" data-t="00:37:53">[00:37:53]</a>. This allows immediate visual verification of whether the model behaves as expected, enabling "structural discovery" by testing different hypotheses and observing the implications <a class="yt-timestamp" data-t="00:38:49">[00:38:49]</a>. This process is iterative and often constrained enough by domain knowledge that comprehensive search is not necessary <a class="yt-timestamp" data-t="00:40:39">[00:40:39]</a>.

## Future of PyMC and Causality

Recent developments in the PyMC ecosystem include the `do` operator and a new package called `causal_py`, focusing on quasi-experimentation <a class="yt-timestamp" data-t="00:40:50">[00:40:50]</a>. This indicates a strong future direction for PyMC in [[causal_ai_and_machine_learning | causal AI and machine learning]] <a class="yt-timestamp" data-t="00:41:07">[00:41:07]</a>.

Wiecki challenges the historical misconception that [[integration_of_causal_reasoning_in_machine_learning | causal analysis cannot be done in a Bayesian framework]] <a class="yt-timestamp" data-t="00:42:52">[00:42:52]</a>. He clarifies that while traditional Bayesian networks might not directly cover interventions (the `do` operator), there's "nothing stopping us from adding the `do` operator" <a class="yt-timestamp" data-t="00:43:15">[00:43:15]</a>. These are all just tools to build the best solutions, rooted in probability <a class="yt-timestamp" data-t="00:43:23">[00:43:23]</a>. The future of PyMC aims to be helpful in this endeavor by "adding these tools and also in communication" <a class="yt-timestamp" data-t="00:43:58">[00:43:58]</a>.

### Uncertainty Quantification: Bayesian vs. Conformal Prediction

Wiecki views uncertainty quantification and model actionability/understandability as two orthogonal axes <a class="yt-timestamp" data-t="00:45:17">[00:45:17]</a>. Black-box machine learning models rank low in understandability, while correlational models provide more insight, and [[causal_ai_and_its_connection_to_machine_learning | causal models]] offer the highest level of understanding for action <a class="yt-timestamp" data-t="00:45:50">[00:45:50]</a>. Estimating these models (e.g., frequentist, Bayesian, conformal prediction) is a separate dimension <a class="yt-timestamp" data-t="00:46:30">[00:46:30]</a>. Different tools are appropriate for different problems across this 2D space <a class="yt-timestamp" data-t="00:47:04">[00:47:04]</a>.

While Bayesian frameworks can naturally separate aleatoric and epistemic uncertainty, Wiecki emphasizes the need to validate these estimates against reality <a class="yt-timestamp" data-t="00:48:02">[00:48:02]</a>. For example, some Bayesian deep learning approaches might produce "weird properties" where uncertainty decreases far from the hyperplane, even without data, leading to a false sense of certainty <a class="yt-timestamp" data-t="00:49:17">[00:49:17]</a>.

In practice, uncertainty estimates in PyMC become most interesting when "actionable" <a class="yt-timestamp" data-t="00:51:25">[00:51:25]</a>. Instead of just providing posterior estimates with error bars, these can be fed into an optimizer with a loss function (e.g., maximizing sales from marketing spend) <a class="yt-timestamp" data-t="00:52:19">[00:52:19]</a>. This allows the optimizer to make decisions that account for risk, similar to human behavior <a class="yt-timestamp" data-t="00:54:24">[00:54:24]</a>. For instance, it can prioritize a marketing channel with more data and lower uncertainty over a newer, seemingly effective one with limited data <a class="yt-timestamp" data-t="00:53:52">[00:53:52]</a>. This directly provides actionable solutions to business problems <a class="yt-timestamp" data-t="00:54:51">[00:54:51]</a>.

## Advice for Newcomers

For those starting in [[machine_learning_and_causality | machine learning]], Bayesian modeling, or [[causality_and_causal_models | causal inference]], Wiecki offers three main lessons:
1.  **Follow Your Passion**: Focus on what you find fun and engaging, as this will sustain motivation <a class="yt-timestamp" data-t="00:57:42">[00:57:42]</a>.
2.  **Take Calculated Risks**: Assess the up- and downsides of opportunities, protecting the downside <a class="yt-timestamp" data-t="00:57:59">[00:57:59]</a>. Don't overcommit to something that might not work out <a class="yt-timestamp" data-t="01:00:33">[01:00:33]</a>.
3.  **Explore and Be Open**: Give yourself a chance to explore new fields and connect with others <a class="yt-timestamp" data-t="01:02:20">[01:02:20]</a>. People are often "extremely open and helpful" if approached genuinely <a class="yt-timestamp" data-t="00:59:48">[00:59:48]</a>. The "only thing that will be amazing for them" might not be, as people often fall in love with whatever they are doing <a class="yt-timestamp" data-t="01:01:53">[01:01:53]</a>.

## Resources

To learn more about PyMC, Bayesian modeling, and causality:
*   **PyMC Website**: `pymc.io` for a great examples gallery <a class="yt-timestamp" data-t="01:04:25">[01:04:25]</a>.
*   **PyMC Labs Blog**: `pymc-labs.io/blogs` for current thinking and ideas, including posts on the `do` operator <a class="yt-timestamp" data-t="01:04:45">[01:04:45]</a>.
*   **Social Media**: LinkedIn for updates <a class="yt-timestamp" data-t="01:05:12">[01:05:12]</a>.
*   **Connect with Thomas Wiecki**: LinkedIn or Twitter (`T_Wiecki`) <a class="yt-timestamp" data-t="01:07:34">[01:07:34]</a>.