---
title: Challenges and Opportunities in Structural Causal Models
videoId: QAzAFess1AA
---

From: [[causalpython]] <br/> 

Dr. Thomas Wiecki, creator of one of the most recognizable Python probabilistic programming frameworks, discusses the journey into Bayesian modeling and its profound connection with causal inference. He emphasizes how these fields, though historically separate, offer significant opportunities when integrated, particularly in addressing real-world business problems and enabling better decision-making <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

## From Programming to Bayesian Modeling
Dr. Wiecki's early fascination with programming stemmed from the idea of "creating something out of nothing" and controlling systems <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. His academic journey through neuroscience and bioinformatics eventually led him to fall in love with Bayesian modeling <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. He realized its broad applicability when he could use the same tools from his PhD research in a completely different domain: Quant Finance at a FinTech startup <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This experience cemented his belief that Bayesian modeling is valuable not only for academic research but also for industry problems, especially those requiring deep understanding and incorporation of domain knowledge <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

Beyond the technical aspects, Dr. Wiecki highlights the "community aspect" as the most enjoyable part of his work today <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. The collaborative nature of open-source development, where talented individuals from around the world contribute, leads to forming friendships and pushing the boundaries of what's possible <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. This element of discovery—making possible what was previously impossible—is a constant motivation <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

## Bridging Bayesian and Causal Inference

The introduction of the `do-operator` in PyMC, implemented by Ricardo V. <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>, is a significant step towards enabling [[structural_causal_models_and_causal_discovery | structural causal problems]] within the Bayesian framework <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. This development, spearheaded by Ben Vincent, facilitates mapping causal theory into a language understandable to those with a Bayesian background <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

Dr. Wiecki notes that Bayesian modeling and causal inference have largely developed independently <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. He recalls repeatedly asking about the difference between models built in a Bayesian framework (which he calls "data generative processes") and [[structural_causal_models_and_causal_discovery | structural causal models]] (SCMs), only to find that few people seemed to know the answer <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. The conclusion is that "those two things are the same just through a different lens, through a different framework" <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

### Opportunities for Integration
*   **Bayesian Perspective on Causal Inference**: While much of causal inference is expressed in a frequentist framework, there is significant value in articulating these ideas within a Bayesian context <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. Bayesian models naturally incorporate priors and uncertainty <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.
*   **Causal Insight for Bayesian Modeling**: The causal framework provides a powerful way to motivate and explain the benefits of building [[structural_causal_models_and_graph_theory | structural models]] to non-experts <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.

## Communicating Value: Causality in Practice

One of the key [[communication_challenges_in_causal_inference | communication challenges in causal inference]] for data scientists is explaining the value of complex methods like Bayesian modeling to business stakeholders <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>. Dr. Wiecki posits that the ultimate purpose of data science is "to make better actions" and "make better decisions" <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. This requires understanding "how actions affect outcomes," which is fundamentally a causal question <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.

### The Prediction vs. Decision-Making Myth
A common misconception in data science is that prediction and decision-making are the same <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>. However, predictive models, while useful for forecasting, may fail for decision-making if they don't capture causal relationships <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>. An example is a marketing campaign that yields "pure losses" despite using predictive machine learning models for three years, because the models couldn't identify the causal drivers of success <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>. Causal models, like using a topographic map for climbing versus a default navigation map, are the right tool for understanding how to intervene and achieve desired outcomes <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.

While black-box ML algorithms suffice for legitimate forecasting problems, Dr. Wiecki's experience suggests that fewer problems than commonly assumed truly fit this category <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>. A careful causal approach can solve more business problems effectively, even if it requires learning new tools <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>.

## [[Challenges in Implementing Causal Analysis in Practice | Challenges in Implementing Causal Analysis]]

### The Fear of Being Wrong
A significant [[challenges_in_implementing_causal_analysis_in_practice | challenge in implementing causal analysis]] is the fear of explicitly defining the [[structural_causal_models_and_causal_discovery | structural causal model]] and being wrong <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>. Dr. Wiecki encourages embracing mistakes:
> "It's great to be wrong... We're wrong all the time, and that's how we learn" <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>.

### The Iterative Approach
Bayesian modeling promotes an [[iterative_approach_in_building_causal_models | iterative approach in building causal models]]:
1.  **Start Simple**: Begin with a very simple model <a class="yt-timestamp" data-t="00:20:03">[00:20:03]</a>.
2.  **Evaluate and Learn**: Use tools like posterior predictive checks and simulations to determine if the model is wrong and how <a class="yt-timestamp" data-t="00:20:16">[00:20:16]</a>. This process fosters learning about the data itself <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>.
3.  **Collaborate with Domain Experts**: Present models to domain experts, who can identify discrepancies and provide insights, leading to model improvements <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>. This blend of domain expertise and data-driven insights creates the "best of both worlds" <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>.

The alternative – solely relying on black-box algorithms – offers no learning, limited communication, and erodes trust <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>.

### Subjectivity in Modeling
All modeling inherently involves subjective choices, not just in Bayesian priors, but also in machine learning frameworks through data processing (e.g., outlier removal, normalization) and algorithm selection <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>. The key is to be "conscious about them and transparent" <a class="yt-timestamp" data-t="00:24:20">[00:24:20]</a>.

## Advantages of Bayesian Structural Causal Models

The Bayesian framework offers significant [[benefits_and_challenges_of_causal_machine_learning | benefits and challenges of causal machine learning]]:
*   **Variable Selection**: Unlike frequentist approaches that require careful variable selection (e.g., avoiding colliders, including confounders) for subsequent estimation <a class="yt-timestamp" data-t="00:33:57">[00:33:57]</a>, Bayesian models can directly estimate the complete [[structural_causal_models_and_graph_theory | structural model]]. The inherent structure (like a collider) is naturally incorporated into the inference <a class="yt-timestamp" data-t="00:34:45">[00:34:45]</a>.
*   **Robust Estimation**: Point estimates (e.g., maximum likelihood) in complex [[structural_causal_models_and_graph_theory | structural causal models]] can be "biased or noisy" and often collapse to a single point <a class="yt-timestamp" data-t="00:35:34">[00:35:34]</a>. Bayesian methods, particularly using Markov Chain Monte Carlo (MCMC) for integration, yield more representative "mean" estimates that are more useful in complex parameter spaces <a class="yt-timestamp" data-t="00:36:40">[00:36:40]</a>.
*   **Generative Models and [[structural_causal_models_and_causal_discovery | Structural Discovery]]**: Bayesian models are generative, meaning they can express a causal graph and then simulate data from it <a class="yt-timestamp" data-t="00:37:34">[00:37:34]</a>. This allows practitioners to immediately see the implications of their hypothesized causal structure and iteratively refine it based on expected data patterns <a class="yt-timestamp" data-t="00:38:24">[00:38:24]</a>. This workflow facilitates [[structural_causal_models_and_causal_discovery | structural discovery]] by testing different hypotheses <a class="yt-timestamp" data-t="00:38:49">[00:38:49]</a>.

### Uncertainty Quantification: Bayesian vs. Conformal Prediction
[[Evaluation and Systematic Testing of Causal Models | Uncertainty quantification]] is a key strength of the Bayesian framework <a class="yt-timestamp" data-t="00:42:26">[00:42:26]</a>. Dr. Wiecki views different approaches to uncertainty (Bayesian, frequentist, conformal prediction) as orthogonal to the "actionability or understandability" axis of a model (e.g., black-box ML vs. correlational vs. causal) <a class="yt-timestamp" data-t="00:45:17">[00:45:17]</a>. While Bayesian models can distinguish between aleatoric (data) and epistemic (model) uncertainty, he advises caution, emphasizing the need for validation, as the split often depends on prior choices and can behave unexpectedly in certain models (e.g., Bayesian deep learning) <a class="yt-timestamp" data-t="00:48:02">[00:48:02]</a>.

## Actionable Uncertainty and Optimization

The true power of uncertainty estimates lies in their actionability <a class="yt-timestamp" data-t="00:51:21">[00:51:21]</a>. Rather than merely providing posterior estimates with error bars, uncertainty can be integrated into optimizers to inform decision-making <a class="yt-timestamp" data-t="00:52:19">[00:52:19]</a>. For example, in marketing mix modeling, an optimizer can use uncertainty to allocate budget effectively, favoring channels with more data and less uncertainty, thus reflecting human risk aversion <a class="yt-timestamp" data-t="00:53:52">[00:53:52]</a>. This translates directly into "better decisions" by providing actionable budget allocations instead of just statistical estimates <a class="yt-timestamp" data-t="00:54:51">[00:54:51]</a>.

## [[challenges and future directions in causal inference | Challenges and Future Directions in Causal Inference]]
The PyMC ecosystem continues to evolve with a focus on causal tools, such as the `do-operator` and CausalPy, a package for quasi-experimentation <a class="yt-timestamp" data-t="00:41:07">[00:41:07]</a>. These developments address historical misunderstandings about Bayesian methods in causal analysis, demonstrating that features like interventions (the `do-operator`) can be naturally incorporated <a class="yt-timestamp" data-t="00:42:49">[00:42:49]</a>. Dr. Wiecki believes that by approaching these fields with "fresh eyes," new and improved tools can be developed <a class="yt-timestamp" data-t="00:43:37">[00:43:37]</a>.

### Personal Advice for Navigating New Fields
Dr. Wiecki offers three key lessons for those starting in new fields like machine learning or causal inference:
1.  **Follow Your Passion**: Pursue what you find fun and exciting, as this intrinsic motivation will sustain you <a class="yt-timestamp" data-t="00:57:42">[00:57:42]</a>.
2.  **Take Calculated Risks**: Assess the upsides and downsides, and protect the downside <a class="yt-timestamp" data-t="00:57:59">[00:57:59]</a>. He exemplified this by pursuing a PhD that offered valuable skills for industry, even if an academic career didn't materialize <a class="yt-timestamp" data-t="00:58:35">[00:58:35]</a>.
3.  **Explore and Connect**: Be open to exploring different paths and reaching out to people, as most are "extremely open and helpful and eager to work with you" <a class="yt-timestamp" data-t="00:59:48">[00:59:48]</a>. Give yourself a chance to try things and be realistic about when to pivot if something isn't working <a class="yt-timestamp" data-t="01:00:27">[01:00:27]</a>.

## Resources
*   **PyMC Website**: pc.io <a class="yt-timestamp" data-t="01:04:25">[01:04:25]</a> (features an examples gallery with various notebooks) <a class="yt-timestamp" data-t="01:04:29">[01:04:29]</a>.
*   **PyMC Labs Blog**: pyml.io/blogs <a class="yt-timestamp" data-t="01:04:45">[01:04:45]</a> (contains current thinking and posts like the one on the `do-operator`).
*   **Social Media**: LinkedIn is the primary platform for updates <a class="yt-timestamp" data-t="01:05:12">[01:05:12]</a>.
*   **Connect with Dr. Thomas Wiecki**: LinkedIn and Twitter (`TWei`) <a class="yt-timestamp" data-t="01:07:34">[01:07:34]</a>.