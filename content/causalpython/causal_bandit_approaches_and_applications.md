---
title: Causal Bandit Approaches and Applications
videoId: Y4wMksHyMFg
---

From: [[causalpython]] <br/> 

This article summarizes discussions from the Triple AI 2024 conference, specifically focusing on various aspects of causality, including transportable representations, counterfactual explanations, continuous treatment effect distribution, and the intersection of causality with robustness and fairness in AI models <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Transportable Representations for Domain Generalization

Kevin Sha from the Causal AI Lab at Columbia University discussed "Transportable Representations for Domain Generalization" <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

### The Challenge of Domain Shift
When solving statistical tasks like classification, a common issue arises when the source domain (where data is collected) differs from the target domain (where the model is applied) <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. Blindly using all features (X) might lead to incorrect predictions in the target domain <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. The aim is to create a classifier that can generalize across different environments <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

### Concept of Transportability
A key concept is "transportability," meaning that a representation or classifier is invariant across domains <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. While causal features might be invariant, a more informative and still invariant representation can often be found <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. The paper explores methods to find such a representation (R) from features (X), ensuring that predictions of Y given R remain transportable across domains <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Addressing Causal Knowledge
The research covers how to achieve this generalization both with and without explicit knowledge of causal mechanisms. Even without a causal diagram, guarantees can be provided for obtaining a domain-invariant representation by making statistical assumptions <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

### Real-World [[Practical applications of causal methods | Applications]]
This work is crucial for real-world scenarios where data collection in the target domain is impractical, such as applying models trained in a lab setting to human healthcare <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Ignoring domain differences hinders accurate results <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. Leveraging causal understanding is vital for maintaining strong predictive performance across different domains <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

### [[advances in causal machine learning research | Large Language Models]] and Causal Inference
Recent studies, including one that produced the "Causer" dataset, indicate that large language models (LLMs) currently perform poorly on [[Causal discovery algorithms and realworld applications | causal inference]] tasks <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. However, such datasets are valuable for [[Benchmarking in causal machine learning | benchmarking]] and advancing future research into how LLMs understand the world <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

## Counterfactual Explanations and Faithfulness

Research is being conducted on counterfactual explanations, which aim to clarify the behavior of black-box models without directly accessing their internal workings <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. These explanations focus on identifying minimal input changes required for a model to produce a different output <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

### Faithfulness vs. Plausibility
While much prior work has emphasized the "plausibility" of explanations (making them intuitive and consistent with the true data-generating process), the current focus is on "faithfulness" <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. Plausibility ensures that the generated counterfactual appears realistic within the data distribution <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. However, focusing solely on plausibility can lead to explanations that do not accurately reflect the model's actual behavior <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

For example, when attempting to change a digit classification from '9' to '7', different counterfactual generation approaches yield various results. Some might produce valid outputs that appear as adversarial attacks rather than human-plausible digits, while others (like the "revise" approach using a variational autoencoder) generate visually plausible changes <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. The concern is that presenting only plausible explanations might "whitewash" a black-box model, showing what pleases us rather than what the model actually does <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. The goal is to prioritize faithfulness first and plausibility second <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

### Incorporating Causal Knowledge
Some existing approaches leverage causal knowledge to generate causally valid and more efficient counterfactuals <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. The new work, however, aims to rely directly on the model's properties rather than external surrogate tools to derive better explanations <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. This is achieved by borrowing ideas from energy-based modeling and conformal prediction to characterize the classifier's generative capacity and predictive uncertainty <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. These approaches are model-agnostic and can be applied to any differentiable classifier <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

## Continuous Treatment Effect Distribution

Research from IIT Bombay addresses the estimation of continuous treatment effect distribution using an augmenting interpolation and kernel smoothing approach <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

### Method Overview
The method involves augmenting new treatments in the dataset and estimating pseudo-outcomes for them <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. While pseudo-outcomes for treatments close to observed ones are easily obtained via first-order Taylor expansion, treatments far from observed data require uncertainty measures to scale down unreliable contributions <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>. This data augmentation helps break confounding in observational datasets, leading to improved performance <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. The technique has significantly boosted the performance of VCNet, a state-of-the-art neural network for treatment distribution <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.

### Main Contribution
The core contribution is the ability to provide uncertainty estimates for treatments distant from the observed data, which is crucial for downscaling the impact of less reliable pseudo-outcomes <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

### [[Application of causal methods in industry | Applications]] in Recourse
A primary application for this research is in learning "recourse," where the goal is to find an optimal treatment for a given patient <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. Efficiently estimating treatment effects is an intermediate step in achieving this, and this work aims to address challenges in these problems <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.

## Responsible AI: Causality, Robustness, and Fairness

Research by Golnoosh from McGill University focuses on integrating causality, robustness, and fairness in training responsible AI models <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. Traditionally, these aspects are studied independently <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.

### Interconnected Concepts
*   **Adversarial Robustness:** Ensuring a model is resilient to perturbations that change a data point's label <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
*   **Individual Fairness:** Requiring similar individuals to receive similar model decisions <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.

These two notions are highly connected. Robustness can be viewed in terms of fairness by considering perturbations on sensitive attributes, aiming for similar individuals to receive similar decisions even with such changes <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>. Conversely, perturbations can define similarity between data points <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.

### Incorporating Causal Structure
The work defines a new metric that accounts for perturbations, sensitive attribute perturbations, and the underlying causal structure where sensitive and non-sensitive features are related <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>. Unlike uniform perturbations in traditional adversarial robustness, causal awareness acknowledges that perturbing one feature affects others <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. The paper proposes creating perturbations using ideas from causal literature (counterfactuals) to achieve a model that is robust, fair, and causally aware <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.

### Impact and Feasibility
The research demonstrates that it is possible to train models that are robust, fair, and causally aware, and these properties should not be defined independently as they are highly interconnected <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>. Crucially, the performance of the model does not significantly degrade, nor does the computational cost increase substantially, when accounting for these combined dimensions <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>. This means deploying such responsible AI models is feasible without a high price <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.

## Identifying Parameters in Causal Models

Marcus Bläser from Saarland University presented work on identifying parameters in structural causal models (SCMs) where the graph is given, and variables are linear combinations with normally distributed errors <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>. The challenge is to identify these parameters from observed covariances of random variables <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>.

### Existing Approaches and Limitations
*   **Gröbner basis approaches:** Solvable in principle, complete (always identify if possible), but have prohibitive double exponential running time <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>.
*   **Instrumental variable algorithms:** More efficient but incomplete (may fail to identify parameters that are identifiable in principle) <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.

### New Contribution
The new work focuses on SCMs where the underlying graph of directed edges forms a tree <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>. For these "tree-shift structure causal models," an algorithm has been developed that is both randomized polynomial time and complete <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>. This represents a significant step towards understanding the complexity of this problem <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.

## Continual Causality and Community Challenges

Devendra Singhai, Assistant Professor at the Eindhoven University of Technology, discussed "continual causality" – the intersection of continual learning and causality – from the Triple AI 2024 conference <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.

### Bridging Continual Learning and Causality
The conference included a bridge program on continual causality, featuring talks from emerging researchers aiming to connect the two fields <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>. A key insight from the bridge program and discussions is that both continual learning and causality currently lack sufficient real-world applications <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>. To scale both to real-world applications, a combination of the two fields is necessary <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.

### Main Challenges for the Community
1.  **[[Benchmarking in causal machine learning | Benchmarking]]:** There is a significant lack of specific causal benchmarks to test models <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>. Many papers present strong theoretical results and algorithms but rely on synthetic data or a limited set of standard datasets (e.g., Asia dataset) for empirical validation <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>. The community needs to move beyond these limitations <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.
2.  **Scaling Causality:** A long-term goal for the field is to scale causality to larger, more complex models and real-world problems <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>.

### Future Research Directions
*   **Causality and [[Machine learning and causal inference methodologies | Large Language Models]]:** This will be a major focus for the next few years <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>. While recent papers discuss LLMs and causality, many identify open problems without offering solutions <a class="yt-timestamp" data-t="00:20:11">[00:20:11]</a>. The next step is to actively work on solving these identified problems <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>. There is a debate regarding whether LLMs can learn causality; some research suggests they can under certain assumptions, despite initial findings to the contrary <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>.
*   **Probabilistic Circuits:** As a long-term goal for scaling causality, probabilistic circuits (generative models with linear inference time) are promising <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a>. Existing work has bridged causality with probabilistic circuits, and the next step is to apply these to real-world problems and develop new combinations to ensure mutual benefit <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.

### Message to the Causal AI Community
The community is doing excellent work, but it's time to scale models and focus on developing better benchmarks <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>. When developing libraries, the ultimate goal of scaling these models to large, complex systems should be kept in mind <a class="yt-timestamp" data-t="00:22:31">[00:22:31]</a>.