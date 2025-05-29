---
title: Probabilistic modeling and Bayesian frameworks
videoId: QAzAFess1AA
---

From: [[causalpython]] <br/> 

The Causal Bandits podcast frequently discusses the intersection of causality and machine learning. In this episode, host Alex Molak interviews Dr. Thomas Wiecki, an expert in Bayesian modeling and the developer of one of the most recognizable Python probabilistic programming frameworks <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Dr. Thomas Wiecki's Journey

Dr. Wiecki began learning programming as a child by modifying code examples from a book <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. His early fascinations included the idea of creating something from nothing and controlling systems <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. He studied bioinformatics and neuroscience, eventually falling in love with [[applications_of_bayesian_modeling_in_industry | Bayesian modeling]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

He realized the broad applicability of Bayesian modeling tools beyond academic research <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. For instance, at Quantopian, a fintech startup focused on building a crowdsourced hedge fund, the same Bayesian modeling tools he used for his PhD research were effective for problems related to portfolio construction and evaluating algorithms <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. This experience solidified his belief that Bayesian modeling is useful for industry problems and many data science challenges that require deep understanding <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

### The Appeal of Probabilistic Programming

For Dr. Wiecki, the appeal of programming and model building lies in its creativity <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. More recently, he finds immense enjoyment in the community aspect, particularly within the open-source arena <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. He values working with driven and talented individuals at PyMC Labs to solve advanced problems and push the boundaries of what's possible <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This involves making previously impossible things possible and opening up new avenues for discovery <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. He sees himself as a "modern explorer" <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>, enabling humanity to solve potentially massive problems like climate change through these tools <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. The PyMC project, for example, has over 2,000 citations in various fields, including astrophysics <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

## Integrating Bayesian Modeling and Causal Inference

### The `do-operator` in PyMC

PyMC recently added a "causal do-operator," a significant development for causal inference <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. Dr. Wiecki, approaching causality from a Bayesian perspective, notes that these two fields have mostly developed independently <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. Ben Vincent was the main driving force behind mapping causal theory into a language understandable to Bayesian practitioners <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>, while Ricardo Viegas implemented the do-operator and its underlying graph manipulation <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. This addition is considered a critical missing piece to make PyMC a framework for answering structural causal problems <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

### Structural Thinking in Both Worlds

Dr. Wiecki first encountered [[causal_inference_models_and_ai_workshops | causal inference]] at a talk in London, where structural causal models were used to answer data science questions like price elasticity <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. He immediately recognized the similarity to Bayesian modeling, which also involves defining a "data generative process" <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. He observed that while causal inference often operates within a frequentist framework <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>, there is great value in expressing these causal ideas within a Bayesian framework <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

The benefit of Bayesian modeling lies in its ability to incorporate and make sense of complex relationships <a class="yt-timestamp" data-t="00:34:45">[00:34:45]</a>. Unlike frequentist approaches that require careful variable selection to avoid biases (e.g., confounders or colliders), a Bayesian framework allows for direct estimation of the complete structural model, incorporating all variables and their defined structures naturally <a class="yt-timestamp" data-t="00:34:45">[00:34:45]</a>.

### Communicating Value: Causality and Decision Making

A major challenge for Bayesian modeling advocates is explaining its value <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>. Concepts like "priors" and "uncertainty" often don't resonate with general audiences <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>. However, framing the discussion around [[role_of_causality_and_bayesian_methods_in_decision_making | causality]] is far more compelling because it intuitively aligns with the purpose of data science: to make better actions and decisions <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. To take effective action, one must understand what causes what <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.

A common "myth" in data science is that prediction and decision-making are the same <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>. However, as an example from a friend's marketing efforts showed, good predictions don't necessarily lead to good business outcomes if the underlying causal mechanisms are misunderstood <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>. Models focused purely on prediction, often "black-box" algorithms, might perform well predictively but fail to address the underlying business problem, sometimes leading to years of losses <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.

## Overcoming Fears of Structural Modeling

Many data scientists are afraid of explicitly defining a structural causal model because they fear being wrong <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>. Dr. Wiecki's advice is: "it's great to be wrong" <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>. Model building is an iterative process where one starts simply, identifies errors using tools like posterior predictive checks and simulations, and then learns from those errors to improve the model <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>. This process also fosters communication with domain experts, whose insights are crucial for refining the model's structure <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>.

Ignoring structural modeling means training classifiers that might be nonsensical, offering no learning, and hindering communication and trust <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>. For example, entrusting marketing budgets to a black-box algorithm that contradicts human intuition is risky <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>. The ideal approach combines domain expertise with data-driven insights <a class="yt-timestamp" data-t="00:22:31">[00:22:31]</a>. All modeling involves subjective choices, from feature selection to data processing and algorithm choice, and these choices significantly impact the outcome <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>. Being conscious and transparent about these choices is key <a class="yt-timestamp" data-t="00:24:20">[00:24:20]</a>.

## Generative Models and Discovery

The generative nature of Bayesian models in probabilistic programming is a powerful tool. The workflow encourages building the causal structure first, even before fitting data <a class="yt-timestamp" data-t="00:37:45">[00:37:45]</a>. By simulating data from this hypothesized structure, one can immediately see if the model behaves as expected, intuitively identifying incorrect assumptions or relationships <a class="yt-timestamp" data-t="00:38:09">[00:38:09]</a>. This process facilitates "structural discovery" by allowing exploration of different hypotheses and their implications <a class="yt-timestamp" data-t="00:38:49">[00:38:49]</a>. This iterative approach, which often incorporates expert knowledge as a form of "prior," is similar to causal discovery in real-world settings <a class="yt-timestamp" data-t="00:39:06">[00:39:06]</a>.

## Uncertainty Quantification

The Bayesian framework naturally provides [[Uncertainty Quantification in Machine Learning | uncertainty quantification]] <a class="yt-timestamp" data-t="00:44:01">[00:44:01]</a>. Unlike frequentist methods that often provide only point estimates, Bayesian models can directly estimate the full posterior distribution, providing a more complete picture of uncertainty <a class="yt-timestamp" data-t="00:35:34">[00:35:34]</a>.

Dr. Wiecki sees [[bayesian_inference_and_conformal_prediction | conformal prediction]] as an interesting, orthogonal direction in uncertainty quantification <a class="yt-timestamp" data-t="00:45:05">[00:45:05]</a>. He conceptualizes different modeling approaches along two axes: uncertainty quantification and "actionability" or "understandability" <a class="yt-timestamp" data-t="00:45:36">[00:45:36]</a>. Black-box machine learning models rank low on understandability, while correlational models offer more insight, and causal models provide the highest level of understanding for action <a class="yt-timestamp" data-t="00:45:50">[00:45:50]</a>. Different tools, including Bayesian models and conformal prediction, can be placed on this 2D map <a class="yt-timestamp" data-t="00:46:30">[00:46:30]</a>.

While Bayesian methods can theoretically separate aleatoric (data) and epistemic (model) uncertainty, the trustworthiness of this split often depends on the chosen prior and requires validation against reality <a class="yt-timestamp" data-t="00:47:54">[00:47:54]</a>.

### Actionable Uncertainty in Practice

In practice, uncertainty becomes most interesting when it's actionable <a class="yt-timestamp" data-t="00:51:25">[00:51:25]</a>. Instead of just providing posterior estimates with uncertainty bounds, these estimates can be fed into an optimizer to define a loss function (e.g., maximizing sales) and find the best actions <a class="yt-timestamp" data-t="00:52:16">[00:52:16]</a>. For example, in marketing budget allocation, an optimizer incorporating uncertainty would favor a well-established marketing channel with low uncertainty over a newer, seemingly effective one with limited data and high uncertainty <a class="yt-timestamp" data-t="00:53:14">[00:53:14]</a>. This mirrors human risk aversion in decision-making <a class="yt-timestamp" data-t="00:54:24">[00:54:24]</a>. Providing actionable recommendations like optimal budget allocations is more impactful than just presenting raw estimates with error bars <a class="yt-timestamp" data-t="00:54:51">[00:54:51]</a>.

## Advice for New Learners

Dr. Wiecki offers three main lessons for those starting new endeavors in machine learning, Bayesian modeling, or causal inference:
1.  **Explore outside your current comfort zone** <a class="yt-timestamp" data-t="01:02:18">[01:02:18]</a>. New areas might offer unexpected passions.
2.  **Take calculated risks** <a class="yt-timestamp" data-t="00:57:51">[00:57:51]</a>. Think carefully about upsides and downsides, protecting the downside. He applied this himself by pursuing a PhD while also building industry-relevant programming skills <a class="yt-timestamp" data-t="00:58:33">[00:58:33]</a>. Starting PyMC Labs, for instance, was bootstrapped without loans, limiting the worst-case scenario <a class="yt-timestamp" data-t="01:00:10">[01:00:10]</a>.
3.  **Follow your passion** <a class="yt-timestamp" data-t="00:57:25">[00:57:25]</a>. Doing what you enjoy makes the effort feel less like work <a class="yt-timestamp" data-t="00:57:42">[00:57:42]</a>.

He emphasizes that being "wrong" is how we learn <a class="yt-timestamp" data-t="00:59:57">[00:59:57]</a>. He also encourages reaching out to people, noting that many are open and helpful <a class="yt-timestamp" data-t="00:59:30">[00:59:30]</a>. It's important to be realistic and know when to try something new rather than doubling down on a path that isn't working <a class="yt-timestamp" data-t="01:00:48">[01:00:48]</a>.

## The PyMC Ecosystem

The PyMC ecosystem has seen many new causal developments recently <a class="yt-timestamp" data-t="00:50:50">[00:50:50]</a>. Besides the do-operator, a new package called CausalPy was introduced last year <a class="yt-timestamp" data-t="00:41:02">[00:41:02]</a>. Developed by Ben Vincent, CausalPy focuses on quasi-experimentation <a class="yt-timestamp" data-t="00:41:20">[00:41:20]</a>, allowing users to either use scikit-learn models or Bayesian models, with the latter providing uncertainty <a class="yt-timestamp" data-t="00:42:18">[00:42:18]</a>. Dr. Wiecki believes that while there was a historical misunderstanding that causal analysis couldn't be done in a Bayesian framework, this is not true <a class="yt-timestamp" data-t="00:42:49">[00:42:49]</a>. By adding tools like the do-operator and approaching problems with fresh eyes, the field can advance <a class="yt-timestamp" data-t="00:43:13">[00:43:13]</a>.

## Resources

To learn more about PyMC, the open ecosystem, and Bayesian modeling:
*   **PyMC Website**: [pymc.io](https://www.pymc.io) for a gallery of examples <a class="yt-timestamp" data-t="01:04:25">[01:04:25]</a>.
*   **PyMC Labs Blog**: [pymc-labs.io/blog](https://www.pymc-labs.io/blog) for current thinking and ideas, including the post on the do-operator <a class="yt-timestamp" data-t="01:04:45">[01:04:45]</a>.
*   **Social Media**: LinkedIn for updates <a class="yt-timestamp" data-t="01:05:12">[01:05:12]</a>.
*   **Thomas Wiecki's Twitter**: T Wei <a class="yt-timestamp" data-t="01:07:38">[01:07:38]</a>.