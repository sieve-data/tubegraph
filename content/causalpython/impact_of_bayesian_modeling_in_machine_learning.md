---
title: Impact of Bayesian Modeling in Machine Learning
videoId: QAzAFess1AA
---

From: [[causalpython]] <br/> 

Dr. Thomas Wiecki, a prominent figure in the field of probabilistic programming, discusses his journey into and the significant impact of [[intersection_of_neuroscience_and_bayesian_modeling | Bayesian modeling]], particularly its growing intersection with [[machine_learning_and_causality | causality]] and [[causal_inference_and_machine_learning | causal inference]], within the realm of data science and machine learning <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## A Journey into Bayesian Modeling

Dr. Wiecki's fascination with programming began as a child, modifying code examples from a book <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. His academic path led him through bioinformatics, where he "fell in love with Bayesian modeling" <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. This passion inspired him to develop PyMC, one of the most recognizable Python probabilistic programming frameworks <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

He realized the immense utility of Bayesian modeling during his PhD research and later at a FinTech startup called Quantopian <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Despite working on completely different problems like portfolio construction and algorithm evaluation in quantitative finance, the same Bayesian tools proved effective <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. This experience solidified his understanding that Bayesian modeling is not only useful for academic challenges but also for industry problems, especially those requiring a deep understanding and incorporation of domain knowledge into the model <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

## Bridging Bayesian Modeling and Causal Inference

A key insight for Dr. Wiecki was the deep connection between Bayesian modeling and [[integration_of_causal_thinking_in_machine_learning | causal thinking]] <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. Initially, he observed that while Bayesian models involve building a "data generative process," which is a structural aspect, it seemed conceptually similar to the structural causal models he encountered in [[causal_inference_and_machine_learning | causal inference]] talks <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. After repeatedly asking about the difference between these two approaches, he concluded that they are "the same just to a different lens through a different framework" <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

### The Causal `do` Operator in PyMC
PyMC recently added a `do` operator, a critical missing piece for making PyMC a framework capable of answering structural causal problems <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. This addition, driven by Ben Vincent and implemented by Ricardo V.I., maps [[causal_inference_and_machine_learning | causal theory]] into a language understandable to those with a Bayesian background <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. It allows for the integration of best ideas from causal inference directly into the Bayesian modeling framework <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

### Advantages of Bayesianism for Causality
*   **Unified Framework**: In a Bayesian framework, one can build the same structural model and estimate it directly <a class="yt-timestamp" data-t="00:34:45">[00:34:45]</a>. Unlike frequentist approaches that require explicit variable selection rules (like avoiding colliders or including confounders), Bayesian models incorporate the entire structure, including colliders, and handle relationships correctly during inference <a class="yt-timestamp" data-t="00:34:50">[00:34:50]</a>.
*   **Avoiding Biased Estimates**: Point estimates, often used in frequentist methods, can be biased or noisy, especially in complex structural models like hierarchical models <a class="yt-timestamp" data-t="00:35:48">[00:35:48]</a>. Bayesian methods, particularly through Markov Chain Monte Carlo (MCMC), provide more robust estimates (e.g., the mean of the posterior distribution), which are more representative and useful <a class="yt-timestamp" data-t="00:36:48">[00:36:48]</a>.
*   **Generative Modeling**: The generative nature of Bayesian modeling aids in understanding and building models <a class="yt-timestamp" data-t="00:37:32">[00:37:32]</a>. By first building a causal structure and then generating data from it, practitioners can immediately see if the model behaves as expected, facilitating "structural discovery" and refinement of hypotheses <a class="yt-timestamp" data-t="00:38:09">[00:38:09]</a>. This iterative process of comparing model-generated data to real-world data or insights is akin to [[causal_inference_and_machine_learning | causal discovery]] <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a>.

## Communication and Business Impact

A significant [[machine_learning_versus_causal_models_in_business | benefit of Bayesian modeling]], especially when framed through a causal lens, is its ability to resonate with business stakeholders <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. While concepts like "priors" and "uncertainty" can be abstract, "causality" intuitively makes sense: to take effective action, one must understand "what causes what" <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.

Dr. Wiecki posits that the ultimate purpose of data science is to "make better actions" or "make better decisions" <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. This requires understanding how actions affect outcomes, which is fundamentally a causal question <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>. Blindly applying predictive [[machine_learning_and_causality | machine learning]] models for decision-making can lead to "pure losses" if causal relationships are not understood <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>.

### Embracing "Being Wrong"
A common fear in structural modeling is explicitly defining a structure that might be "wrong" <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>. Dr. Wiecki encourages this, stating, "it's great to be wrong... that's how we learn" <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>. Bayesian models provide tools like posterior predictive checks and simulations to assess how wrong a model is <a class="yt-timestamp" data-t="00:20:16">[00:20:16]</a>. This process fosters learning about the data and problem, and facilitates crucial communication with domain experts who can refine the model based on their intuition <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>. The alternative – using opaque [[machine_learning_and_causality | machine learning]] algorithms without understanding their underlying mechanisms – hinders learning, communication, and trust <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>.

## Uncertainty Quantification

The Bayesian framework naturally handles [[uncertainty_quantification_in_causal_machine_learning | uncertainty quantification]] in a "very natural, very organic way" <a class="yt-timestamp" data-t="00:44:29">[00:44:29]</a>.

### Bayesian vs. Conformal Prediction
Dr. Wiecki views [[uncertainty_quantification_in_causal_machine_learning | uncertainty quantification]] and "understandability" (or "actionability") as two orthogonal axes <a class="yt-timestamp" data-t="00:45:17">[00:45:17]</a>. While blackbox machine learning models rank low on understandability, causal models rank high <a class="yt-timestamp" data-t="00:45:50">[00:45:50]</a>. Both frequentist (including conformal prediction) and Bayesian methods can quantify uncertainty, but the choice depends on the specific problem and desired level of interpretability <a class="yt-timestamp" data-t="00:46:30">[00:46:30]</a>.

Bayesian models can easily split aleatoric (data inherent) and epistemic (model uncertainty) uncertainty <a class="yt-timestamp" data-t="00:47:54">[00:47:54]</a>. However, Dr. Wiecki cautions that the meaningfulness of this split and the absolute uncertainty estimates depend heavily on the chosen priors and require rigorous validation against reality <a class="yt-timestamp" data-t="00:48:06">[00:48:06]</a>.

### Actionable Uncertainty in Practice
The real power of uncertainty estimates in Bayesian modeling comes when they become "actionable" <a class="yt-timestamp" data-t="00:51:25">[00:51:25]</a>. By integrating these estimates into an optimizer with a defined loss function (e.g., maximizing sales in a marketing context), the model can suggest optimal actions that account for risk <a class="yt-timestamp" data-t="00:52:19">[00:52:19]</a>.

For instance, an optimizer utilizing Bayesian uncertainty would prioritize a marketing channel with 3 years of solid data (low uncertainty) over a new channel with only 2 months of data (high uncertainty), even if the new channel has a higher point estimate of effectiveness <a class="yt-timestamp" data-t="00:53:18">[00:53:18]</a>. This behavior mirrors human risk aversion in decision-making <a class="yt-timestamp" data-t="00:54:26">[00:54:26]</a>. This approach directly supports the goal of data science: making better, risk-aware decisions <a class="yt-timestamp" data-t="00:54:49">[00:54:49]</a>.

## Future Directions and PyMC
Recent developments in the PyMC ecosystem, such as the `do` operator and the `CausalPy` package, signal a clear direction towards a more causal future for PyMC <a class="yt-timestamp" data-t="00:40:50">[00:40:50]</a>. CausalPy, developed by Ben Vincent, focuses on quasi-experimentation, allowing users to leverage either scikit-learn models or Bayesian models, with the latter providing valuable uncertainty quantification <a class="yt-timestamp" data-t="00:41:20">[00:41:20]</a>. This integration aims to overcome historical misunderstandings that suggest Bayesian frameworks cannot support causal analysis or interventions <a class="yt-timestamp" data-t="00:42:49">[00:42:49]</a>.

Dr. Wiecki expresses his delight if PyMC can be helpful in this endeavor, emphasizing that all these methods ultimately relate to probability <a class="yt-timestamp" data-t="00:43:30">[00:43:30]</a>. The goal is to build the best tools by approaching challenges with fresh eyes and exploring methods freely <a class="yt-timestamp" data-t="00:43:48">[00:43:48]</a>.

## Advice for Newcomers
For those starting in fields like [[machine_learning_and_causality | machine learning]], [[machine_learning_and_treatment_effect_estimation | Bayesian modeling]], or [[causal_inference_and_machine_learning | causal inference]], Dr. Wiecki offers three main pieces of advice <a class="yt-timestamp" data-t="01:02:12">[01:02:12]</a>:
1.  **Follow Your Passion**: Engage with what genuinely excites you, as this intrinsic motivation makes the challenging work feel less like work <a class="yt-timestamp" data-t="00:57:42">[00:57:42]</a>.
2.  **Take Calculated Risks**: Assess the upsides and downsides, and protect the downside <a class="yt-timestamp" data-t="00:57:59">[00:57:59]</a>. Don't overcommit if things aren't working out, and be realistic about outcomes <a class="yt-timestamp" data-t="01:00:33">[01:00:33]</a>.
3.  **Explore Beyond Current Endeavors**: Be open to trying new things, as you might discover a passion for something unexpected <a class="yt-timestamp" data-t="01:01:53">[01:01:53]</a>. Reaching out to people and doing internships can open doors and provide invaluable learning experiences <a class="yt-timestamp" data-t="00:59:06">[00:59:06]</a>.