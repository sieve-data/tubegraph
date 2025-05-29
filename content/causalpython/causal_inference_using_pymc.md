---
title: Causal Inference using PyMC
videoId: QAzAFess1AA
---

From: [[causalpython]] <br/> 

Dr. Thomas Wiecki, known for developing PyMC, a prominent Python probabilistic programming framework, explores the powerful synergy between PyMC and [[causal_inference_and_machine_learning | causal inference]]. He emphasizes how Bayesian modeling provides unique capabilities for understanding and impacting real-world problems, moving beyond mere prediction to enable better decision-making. <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>

> "It's great to be wrong and that's how we learn." <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>

## Dr. Thomas Wiecki's Path to Bayesian Modeling

Thomas Wiecki's journey into programming began in childhood by modifying code examples from a book. <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a> He pursued studies in neuroscience and bioinformatics before discovering a fascination with Bayesian modeling. <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a> This fascination led him to develop PyMC, recognizing the utility of Bayesian tools not only in academic research but also in industry, such as in a fintech startup focused on crowdsourced hedge funds. <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a> <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a> He realized that these tools could solve a wide range of data science problems requiring deep understanding and the incorporation of prior knowledge. <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>

A significant aspect of his enjoyment comes from the community surrounding open-source projects like PyMC, where talented individuals collaborate to push the boundaries of what's possible and solve advanced problems. <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a> The ability to enable humanity to solve potentially massive problems, such as [[application_of_causal_inference_to_large_scale_climate_data | climate change]], is a core motivation. <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a> <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>

## Integrating Causal Inference into PyMC

While not a causal expert himself, Wiecki approaches [[causal_inference_and_machine_learning | causal inference]] from a Bayesian perspective, finding it to be a helpful lens. <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a> He notes that the two fields have largely developed independently, but many interesting cross-connections exist. <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>

### The `do` Operator
A recent significant addition to PyMC is the [[causal_inference_and_discovery_in_python | causal do operator]]. <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a> This operator, primarily driven by Ben Vincent with implementation by Ricardo Viri, maps causal theory into a language understandable by Bayesian practitioners. <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a> The `do` operator integrates well into PyMC's framework, despite requiring some graph manipulation. <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a> Its inclusion provides a critical missing piece, allowing PyMC to function as a framework for answering structural causal problems and building corresponding models. <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>

### Structural Thinking and Generative Processes
Wiecki recalls initially being puzzled by the similarities between structural causal models and Bayesian data generative processes. <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a> After repeatedly asking about the difference in various talks, he concluded that these two approaches are essentially the same, just viewed through different lenses. <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>

Causal inference, often expressed in a frequentist framework, emphasizes causality and estimating treatment effects. <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a> However, there is significant value in expressing these ideas within a Bayesian framework. <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a> Conversely, Bayesian modeling can benefit from adopting the language and framework of causality to better communicate its value. <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>

## Benefits of Bayesian Causal Inference

### Communication and Actionability
Wiecki highlights that communicating the value of Bayesian modeling to business stakeholders can be challenging when discussing priors and uncertainty. <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a> However, framing the discussion around causality resonates deeply, as it directly addresses the purpose of data science: to make better actions and decisions. <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a> <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>

> "The purpose of data science is to make better actions... We really need to understand how actions affect outcomes, and that is at the core a causal question." <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a> <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>

He distinguishes between prediction and [[causal_inference_and_decision_theory | decision-making]], noting that while prediction forecasts what will happen, it doesn't necessarily enable action. <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a> A classic example is a marketing campaign that consistently results in losses despite using predictive [[machine_learning_and_causal_inference_methodologies | machine learning]] models. <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a> This demonstrates that blackbox machine learning algorithms, while good for forecasting, are often not the right fit for problems requiring an understanding of cause and effect. <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>

### Overcoming Fear of Being Wrong
Many people starting with structural thinking fear being wrong about defining the data generating process or structural causal model. <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a> Wiecki advises that "it's great to be wrong," as it is how learning occurs. <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a> Models should start simple and be iteratively refined using tools like posterior predictive checks and simulations to identify discrepancies with data. <a class="yt-timestamp" data-t="00:20:03">[00:20:03]</a> This iterative process fosters learning about the data and problem, enabling effective communication with domain experts who can provide crucial insights for model improvement. <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a> <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>

The alternative—blindly training classifiers—might produce predictions but offers no understanding or interpretability, which is problematic for trust and effective decision-making, especially when domain experts have decades of experience. <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>

### Variable Selection and Model Assumptions
In traditional frequentist [[causal_inference_in_practical_applications | causal models]], selecting which variables to include is critical to avoid biases (e.g., from including a collider or not including confounders). <a class="yt-timestamp" data-t="00:33:13">[00:33:13]</a> In contrast, the Bayesian framework of PyMC allows for the direct estimation of the complete structural model. <a class="yt-timestamp" data-t="00:34:45">[00:34:45]</a> Users can include all relevant structure, and the inference process inherently incorporates causal relationships without needing separate variable selection logic. <a class="yt-timestamp" data-t="00:35:01">[00:35:01]</a>

Furthermore, using point estimates in complex structural models often leads to biased or noisy results. <a class="yt-timestamp" data-t="00:35:34">[00:35:34]</a> Bayesian methods, particularly with Markov Chain Monte Carlo (MCMC), provide a more robust and flexible way to estimate models by focusing on the mean of distributions rather than just the mode, which is crucial for handling complex structures like hierarchical models. <a class="yt-timestamp" data-t="00:36:40">[00:36:40]</a>

### Generative Modeling and Structural Discovery
The generative nature of Bayesian models in PyMC is a powerful tool for understanding the problem. <a class="yt-timestamp" data-t="00:37:32">[00:37:32]</a> By building a causal structure and generating synthetic data from it *before* fitting to real data, users can immediately see the implications of their assumptions and intuitively identify potential issues. <a class="yt-timestamp" data-t="00:37:51">[00:37:51]</a> This process allows for structural discovery, enabling exploration of different hypotheses and their data implications, a process that is very similar to how [[causal_inference_and_discovery_in_python | causal discovery]] is done in real-world settings. <a class="yt-timestamp" data-t="00:38:49">[00:38:49]</a> <a class="yt-timestamp" data-t="00:39:06">[00:39:06]</a>

## Uncertainty Quantification

The Bayesian framework naturally provides uncertainty estimates. <a class="yt-timestamp" data-t="00:42:26">[00:42:26]</a> While methods like conformal prediction also offer uncertainty, Bayesian models can often provide a more organic split between aleatoric (data inherent) and epistemic (model uncertainty) uncertainty. <a class="yt-timestamp" data-t="00:47:54">[00:47:54]</a> However, Wiecki cautions that the meaningfulness of this split depends heavily on the model and prior choices and requires validation. <a class="yt-timestamp" data-t="00:48:02">[00:48:02]</a>

### Actionable Uncertainty in Decision Making
Uncertainty estimates become most valuable when they are actionable. <a class="yt-timestamp" data-t="00:51:21">[00:51:21]</a> Instead of just providing posterior distributions or error bars, these estimates can be fed into an optimizer to make better decisions. <a class="yt-timestamp" data-t="00:52:19">[00:52:19]</a>

For example, in [[causal_inference_in_finance | marketing mix modeling]], an optimizer can use uncertainty to allocate budget most effectively. <a class="yt-timestamp" data-t="00:52:33">[00:52:33]</a> A marketing channel with only two months of data might show high effectiveness but also high uncertainty. A channel with three years of solid data might show lower point effectiveness but very low uncertainty. An optimizer that incorporates uncertainty would prioritize the safer, well-supported channel, mimicking human risk-averse behavior. <a class="yt-timestamp" data-t="00:53:16">[00:53:16]</a> <a class="yt-timestamp" data-t="00:54:24">[00:54:24]</a>

This integration of uncertainty with an optimizer makes the output directly actionable, leading to solutions that account for risk, aligning with human decision-making processes. <a class="yt-timestamp" data-t="00:54:38">[00:54:38]</a>

## Future of PyMC and Causal Inference

The PyMC ecosystem has seen new causal developments, including the `do` operator and the `CausalPy` package. <a class="yt-timestamp" data-t="00:40:50">[00:40:50]</a> `CausalPy`, developed by Ben Vincent, focuses on quasi-experimentation, allowing users to fit data in an in-sample period and predict out-of-sample, comparing against actual outcomes. <a class="yt-timestamp" data-t="00:41:20">[00:41:20]</a> It supports both scikit-learn models and Bayesian models, providing uncertainty estimates with the latter. <a class="yt-timestamp" data-t="00:42:18">[00:42:18]</a>

Wiecki believes there has been a historical misconception that causal analysis is not possible within a Bayesian framework. <a class="yt-timestamp" data-t="00:42:49">[00:42:49]</a> However, by adding functionalities like the `do` operator, PyMC demonstrates that these perceived limitations can be overcome. <a class="yt-timestamp" data-t="00:43:02">[00:43:02]</a> Since everything ultimately relies on probability, integrating these methods with fresh eyes can lead to powerful new tools for understanding the world and solving data science problems. <a class="yt-timestamp" data-t="00:43:27">[00:43:27]</a>

## Advice for Aspiring Practitioners

Thomas Wiecki offers three key pieces of advice for those starting in new fields like machine learning, Bayesian modeling, or [[causal_inference_and_discovery_in_python | causal inference]]:

1.  **Give yourself a chance to explore:** There might be something outside your current focus that you enjoy even more. <a class="yt-timestamp" data-t="01:01:54">[01:01:54]</a> Many who transitioned from academia to industry found their new work equally or more exciting. <a class="yt-timestamp" data-t="01:01:04">[01:01:04]</a>
2.  **Take calculated risks:** Evaluate the upsides and downsides, and protect the downside. <a class="yt-timestamp" data-t="00:57:51">[00:57:51]</a> For example, his decision to pursue a PhD was a calculated risk that provided valuable skills for an industry career, even if academia didn't work out. <a class="yt-timestamp" data-t="00:58:15">[00:58:15]</a> Similarly, starting PyMC Labs without VC funding limited the downside risk. <a class="yt-timestamp" data-t="01:00:10">[01:00:10]</a>
3.  **Follow your passion:** He attributes his persistence to finding joy in the work, which made it feel less like a chore. <a class="yt-timestamp" data-t="00:57:22">[00:57:22]</a> Reaching out to people, even with random emails, can lead to opportunities like internships and ultimately, job offers, as people are often open to helping. <a class="yt-timestamp" data-t="00:59:30">[00:59:30]</a>

## Resources

*   **PyMC Website**: `pymc.io` offers a comprehensive examples gallery for self-guided exploration. <a class="yt-timestamp" data-t="01:04:25">[01:04:25]</a>
*   **PyMC Labs Blog**: `pylabs.io/blogs` features articles, including the post on the `do` operator, detailing current thinking and future directions. <a class="yt-timestamp" data-t="01:04:45">[01:04:45]</a>
*   **Social Media**: LinkedIn is the primary platform for updates. <a class="yt-timestamp" data-t="01:05:12">[01:05:12]</a>
*   **Connect with Thomas Wiecki**: Find him on LinkedIn or Twitter (`T_Wei`). <a class="yt-timestamp" data-t="01:07:34">[01:07:34]</a>