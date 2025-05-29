---
title: Causal inference and decision theory
videoId: gazCIKYEv44
---

From: [[causalpython]] <br/> 

## Dr. Robert Ness's Journey to Causal Inference

Dr. Robert Ness, a Senior Researcher at Microsoft Research, began his academic journey in economics before transitioning to statistics, computation, and eventually [[causal_analysis_and_decision_making | causal inference]] <a class="yt-timestamp" data-t="01:16:11">[01:16:11]</a>. His unifying interest across these fields was in quantitative work that connected to real-world applications and solving applied problems <a class="yt-timestamp" data-t="01:44:47">[01:44:47]</a>. Statistics naturally resonated with him, feeling like a "superpower" due to its ease of understanding, unlike other mathematical topics <a class="yt-timestamp" data-t="01:57:58">[01:57:58]</a>. What attracted him to statistics was the process of modeling data, data science, and building models <a class="yt-timestamp" data-t="02:55:01">[02:55:01]</a>.

During his PhD, Dr. Ness moved into systems biology, preferring it over financial engineering because natural sciences offer a "ground truth in reality" to model, unlike financial markets which he felt "lacked a certain type of anchor in reality" <a class="yt-timestamp" data-t="03:50:04">[03:50:04]</a>. This shift introduced him to the task of using [[causal_discovery_and_inference_in_AI | causal discovery]] algorithms, or structure learning, to reconstruct biological pathways from single-cell data <a class="yt-timestamp" data-t="05:04:06">[05:04:06]</a>.

### Challenges in Practical Causal Discovery

A main challenge in applying structural algorithms to biological data was building something practically useful <a class="yt-timestamp" data-t="05:41:09">[05:41:09]</a>. While causal discovery involves learning causal properties of a system (often a directed acyclic graph or DAG) from data, simply producing a graph was not the end goal for laboratory analysts <a class="yt-timestamp" data-t="05:46:27">[05:46:27]</a>. They sought to use these analyses for specific purposes like discovering new biomarkers or informing drug discovery <a class="yt-timestamp" data-t="07:07:07">[07:07:07]</a>. This need led Dr. Ness to focus on experimental design, specifically Bayesian experimental design, to create a workflow for guiding measurements and dealing with uncertainty, where the DAG was an intermediate step towards a final outcome <a class="yt-timestamp" data-t="07:43:08">[07:43:08]</a>.

### Evaluating Causal Structures

Initially, learned graphs were evaluated by comparing them to a known "ground truth" graph using metrics like precision-recall or structural Hamming distance <a class="yt-timestamp" data-t="08:48:50">[08:48:50]</a>. However, this is only possible when ground truth is available <a class="yt-timestamp" data-t="09:08:08">[09:08:08]</a>. Dr. Ness turned to Bayesian reasoning to handle uncertainty and incorporate prior knowledge about the system (e.g., protein interactions) <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>. This approach aimed to provide guarantees that the model would move towards the correct answer even if the true ground truth was unknown <a class="yt-timestamp" data-t="10:22:00">[10:22:00]</a>.

## [[causal_analysis_and_decision_making | Causal Decision Making]] and Decision Theory

[[causal_analysis_and_decision_making | Causal decision theory]] has an interesting history, often contrasted with empirical decision theory <a class="yt-timestamp" data-t="10:55:00">[10:55:00]</a>. Empirical decision theory suggests decision-making agents should only consider the consequences of their actions, deviating from the traditional view of maximizing expected utility conditional on action <a class="yt-timestamp" data-t="11:12:00">[11:12:00]</a>. Examples like Newcomb's Problem illustrate where causal ideas might lead to suboptimal results <a class="yt-timestamp" data-t="11:39:00">[11:39:00]</a>.

However, with a more mature understanding of causal models, their application is emerging in automated decision theory <a class="yt-timestamp" data-t="11:47:00">[11:47:00]</a>. One example is [[causal_discovery_and_inference_in_AI | Causal Bandits]], where causal knowledge is applied to optimize systems with unknown or partially identified causal factors, such as using causal Thompson sampling <a class="yt-timestamp" data-t="12:04:00">[12:04:00]</a>. Another area is [[causal_decision_making_and_reinforcement_learning | Causal Reinforcement Learning]] (CRL), which leverages causal assumptions to:
*   Improve sample efficiency in high-dimensional settings, making intractable problems tractable <a class="yt-timestamp" data-t="13:02:00">[13:02:00]</a>.
*   Aid in credit assignment, posing questions about why a policy led to a certain outcome as causal questions, using attribution or root cause analysis <a class="yt-timestamp" data-t="13:24:00">[13:24:00]</a>.

### Human-like Decision Making and [[causal_reasoning_in_AI | Causal Reasoning in AI]]

A key interest for Dr. Ness is automatizing how humans make decisions and reason about causes <a class="yt-timestamp" data-t="13:53:00">[13:53:00]</a>. Humans often imagine hypothetical scenarios and condition on potential outcomes, which is very sample-efficient, as one doesn't need to experience something directly to learn from it <a class="yt-timestamp" data-t="14:35:00">[14:35:00]</a>. Causal models provide the language for building algorithms that emulate this [[causal_reasoning_in_artificial_intelligence | causal reasoning]] <a class="yt-timestamp" data-t="15:06:00">[15:06:00]</a>.

Reinforcement learning (RL) aims to find optimal, automated policies for sequential decision-making <a class="yt-timestamp" data-t="16:09:00">[16:09:00]</a>. Traditional RL, especially model-free approaches, often treats everything as a Markov Decision Process, folding causal nuances into a single "state" variable without explicitly modeling causal relationships <a class="yt-timestamp" data-t="17:37:00">[17:37:37]</a>. While this is often sufficient for maximizing reward, issues arise when:
*   Actions that maximize expected reward differ from actions that maximize expected reward when accounting for how actions change the environment <a class="yt-timestamp" data-t="18:36:00">[18:36:00]</a>.
*   The state variable lacks information required for [[causal_inference_and_machine_learning | causal identifiability]], potentially leading to biases (e.g., collider bias) or purely associative decisions <a class="yt-timestamp" data-t="19:54:00">[19:54:00]</a>.
*   Models need to select actions that maximize outcomes under circumstances not seen in training data <a class="yt-timestamp" data-t="19:05:00">[19:05:00]</a>.

While traditional RL can work well in many practical scenarios, [[causal_inference_in_practical_applications | causal inference]] is crucial for specific high-value scenarios where a causal model is necessary to avoid problems <a class="yt-timestamp" data-t="21:12:00">[21:12:00]</a>. The challenge is to identify these practical scenarios beyond mere "toy problems" <a class="yt-timestamp" data-t="22:01:00">[22:01:00]</a>.

### When Causal Models are Necessary

It's easy to construct examples where the expectation of Y given a "do" action (causal intervention) is different from the expectation of Y given an observed action <a class="yt-timestamp" data-t="24:12:00">[24:12:00]</a>. However, the value of X that maximizes both queries (interventional vs. observational) is often the same <a class="yt-timestamp" data-t="25:10:00">[25:10:00]</a>. This means that while an observational model might approximate the causal effect, it often leads to the same optimal decision <a class="yt-timestamp" data-t="25:22:00">[25:22:00]</a>.

The motivation for explicitly modeling the "do" action comes in instances where the argument that maximizes the observational query and the interventional query are different, and this difference is significant in a practical scenario <a class="yt-timestamp" data-t="25:39:00">[25:39:00]</a>. [[causal_analysis_and_decision_making | Causal analysis]] provides a clear guideline, explaining when an approximation might be error-prone, or when the optimization target differs from what's actually being optimized, leading to different outcomes <a class="yt-timestamp" data-t="26:19:00">[26:19:00]</a>.

## [[causal_reasoning_in_AI | Causal Reasoning in AI]] and AGI

From a causal perspective, an Artificial General Intelligence (AGI) model would need to be able to reason about cause and effect <a class="yt-timestamp" data-t="29:45:00">[29:45:00]</a>. This involves modeling human reasoning capabilities computationally, comparing algorithmic outputs to human responses in vignettes, and understanding how humans reason about processes <a class="yt-timestamp" data-t="30:21:00">[30:21:00]</a>. [[causal_inference_and_machine_learning | Causal inference theory]] provides the framework to specify assumptions and inductive biases needed to draw conclusions beyond observed data <a class="yt-timestamp" data-t="31:18:00">[31:18:00]</a>.

Traditional causal inference research focuses on answering objective questions about cause-effect relationships that exist externally (e.g., "Does this drug treat this illness?") <a class="yt-timestamp" data-t="32:23:00">[32:23:00]</a>. However, emulating human reasoning might involve capturing cognitive biases or inefficient heuristics in a model, not just objective correctness <a class="yt-timestamp" data-t="33:50:00">[33:50:00]</a>. This distinction between objective truth and alignment with human reasoning is an interesting path towards AGI <a class="yt-timestamp" data-t="34:32:00">[34:32:00]</a>.

An example of human causal reasoning involves counterfactual simulation. Humans tend to engage in less counterfactual simulation regarding the absence of actions or events, as it's harder to enumerate things that didn't happen compared to things that did <a class="yt-timestamp" data-t="35:55:00">[35:55:00]</a>. Algorithms could potentially remedy this by scoping out negative events in a way that makes counterfactual reasoning about them easier <a class="yt-timestamp" data-t="37:15:00">[37:15:00]</a>.

## Probabilistic Programming and Causal Inference

A paper by Dr. Ness and colleagues (including S. Mohammad Taheri and Karen Sachs) showed that a latent variable modeling approach, common in probabilistic machine learning (e.g., PyMC, Stan, Pyro), can be used for [[causal_inference_and_machine_learning | causal inference]] <a class="yt-timestamp" data-t="38:29:00">[38:29:00]</a>. The key finding was that if a model has a DAG and the intervention distribution being sampled from is identified (e.g., by the rules of do-calculus), then the sampling procedure is valid <a class="yt-timestamp" data-t="39:19:00">[39:19:00]</a>. This allows researchers familiar with latent variable models to enter the world of [[causal_reasoning_in_AI | causal reasoning]], as long as they can prove the validity of their approach using graphical identification frameworks <a class="yt-timestamp" data-t="41:07:00">[41:07:00]</a>. Libraries like `y0` in Python can automate the process of checking if a query is identifiable <a class="yt-timestamp" data-t="41:21:00">[41:21:00]</a>.

This means that if a quantity is identifiable using do-calculus, a probabilistic programming framework can produce an unbiased estimate of the causal effect <a class="yt-timestamp" data-t="42:03:00">[42:03:00]</a>. For those accustomed to model-based machine learning, this demonstrates how their existing frameworks can be adapted to answer causal queries, especially given the ability of modern probabilistic programming languages to handle high-dimensional settings and diverse data types like images and sound <a class="yt-timestamp" data-t="43:49:00">[43:49:00]</a>.

The recently released `Cairo` library, built on `Pyro`, abstracts away complex causal inference challenges that don't mesh well with existing deep probabilistic machine learning frameworks <a class="yt-timestamp" data-t="47:30:00">[47:30:00]</a>. It simplifies the inference side of the problem and aligns with the philosophy that causal uncertainty and system uncertainty can be addressed by making causal assumptions <a class="yt-timestamp" data-t="48:03:00">[48:03:00]</a>.

## The Next Big Thing in Causality: Causal Representation Learning

Dr. Ness believes that a significant breakthrough in causality would be **causal representation learning** <a class="yt-timestamp" data-t="49:48:00">[49:48:00]</a>. This is related to probabilistic machine learning concepts like disentanglement, aiming to learn latent representations that correspond to actual causes in the data generating process <a class="yt-timestamp" data-t="49:50:00">[49:50:00]</a>. Causality can provide criteria for how a learned cause should behave (e.g., modularity, invariance under intervention), guiding the application of practical assumptions to learning problems to guarantee the discovery of these abstractions <a class="yt-timestamp" data-t="50:04:00">[50:04:00]</a>.

### Application in Generative AI

A concrete example is generative AI (e.g., Midjourney, Stable Diffusion) <a class="yt-timestamp" data-t="51:02:00">[51:02:00]</a>. Current generative models make it difficult to perform precise, semantically meaningful edits (e.g., changing glasses color without affecting other elements) <a class="yt-timestamp" data-t="51:10:00">[51:10:00]</a>. This is essentially a counterfactual question: "What would this image look like if the glasses were red instead of blue, with nothing else changing?" <a class="yt-timestamp" data-t="51:43:00">[51:43:00]</a>. If models could operate semantically on learned [[machine_learning_and_causal_inference_methodologies | causal abstractions]] or representations behind an image, it would allow users to have "knobs" to make precise adjustments, akin to editing text in natural language models <a class="yt-timestamp" data-t="52:40:00">[52:40:00]</a>. This would be a powerful improvement, particularly for creative applications of generative AI, where models augment human creative processes <a class="yt-timestamp" data-t="53:03:00">[53:03:00]</a>.

### Causal Large Language Models

The concept of large language models (LLMs) learning a "world model" often refers to them learning a [[causal_reasoning_in_AI | causal model]] <a class="yt-timestamp" data-t="55:00:00">[55:00:00]</a>. The Causal Hierarchy Theorem (also known as Pearl's hierarchy or ladder) states that different levels of causal questions (associational, interventional, counterfactual) require assumptions of the corresponding level <a class="yt-timestamp" data-t="55:52:00">[55:52:00]</a>. For counterfactual questions, Level 3 assumptions (e.g., in the form of a structural causal model) are needed <a class="yt-timestamp" data-t="56:44:00">[56:44:00]</a>.

While LLMs can empirically answer causal questions (e.g., "Does smoking cause cancer?", generating causal analysis code, or simulating counterfactuals) <a class="yt-timestamp" data-t="57:05:00">[57:05:00]</a>, they are prone to "hallucinations" <a class="yt-timestamp" data-t="57:44:00">[57:44:00]</a>. The challenge is ensuring reliable causal answers <a class="yt-timestamp" data-t="58:17:00">[58:17:00]</a>. According to the Causal Hierarchy Theorem, for LLMs to reliably answer counterfactual questions, the necessary Level 3 assumptions must exist somewhere – whether implicitly in the training data, model architecture, parameterization, or explicitly in the prompt <a class="yt-timestamp" data-t="58:43:00">[58:43:00]</a>.

Dr. Ness is exploring ways to incorporate causal information directly into the Transformer architecture of LLMs, similar to how his paper showed theoretical guarantees for latent variable models <a class="yt-timestamp" data-t="01:00:08">[01:00:08]</a>. This approach aims to provide theoretical guarantees for causal behavior based on the model's structure <a class="yt-timestamp" data-t="01:00:27">[01:00:27]</a>. An example is a toy model demonstrating how structural knowledge (e.g., Act One causes Act Two, which causes Act Three in a script) can allow models to simulate outcomes for unobserved scenarios in natural language <a class="yt-timestamp" data-t="01:00:51">[01:00:51]</a>.

The goal is not just to guarantee causal correctness but to provide users with "knobs" that align models with human thinking about abstractions, enhancing creative processes <a class="yt-timestamp" data-t="01:01:53">[01:01:53]</a>. This research area emphasizes leveraging depth (structural information) over just scaling up data, training models more efficiently with smaller datasets, and incorporating innate data structure (e.g., GitHub repo history for code generation) <a class="yt-timestamp" data-t="01:03:18">[01:03:18]</a>.

## Recommended Books

Two books that significantly influenced Dr. Robert Ness's career are:
*   **"Computational Systems Biology" by Darren Wilkinson**: This book provides a broad introduction to computational Bayes, including random variable simulation and inference algorithms (e.g., importance sampling, MCMC), alongside methods for building computational models of dynamic systems, with a focus on biology <a class="yt-timestamp" data-t="01:05:45">[01:05:45]</a>. Its principles are broadly applicable beyond biology <a class="yt-timestamp" data-t="01:06:30">[01:06:30]</a>.
*   **A book by Hadley Wickham on the R language**: Heavily influenced by functional programming paradigms (e.g., "Structure and Interpretation of Computer Programs"), this book introduced Dr. Ness to the design and implementation of programming languages, profoundly impacting his approach as a modeler <a class="yt-timestamp" data-t="01:07:32">[01:07:32]</a>.

## Advice for Aspiring Causal Inference Researchers

For those looking to become researchers in [[causal_analysis_and_decision_making | causal inference]]:
1.  **Work through a good book**: Understand the "shape of the territory" to identify the research frontier and push against it <a class="yt-timestamp" data-t="01:13:29">[01:13:29]</a>.
2.  **Identify impactful people**: Find researchers making a significant impact in the field through workshops, conferences, and podcasts <a class="yt-timestamp" data-t="01:13:56">[01:13:56]</a>.
3.  **Study their work and citations**: Examine their papers to understand the cutting edge of research <a class="yt-timestamp" data-t="01:14:14">[01:14:14]</a>.
4.  **Connect with the community**: During training (e.g., PhD), be in proximity to the network of people doing the work <a class="yt-timestamp" data-t="01:14:26">[01:14:26]</a>. Focus on developing personal connections rather than solely on institutional prestige <a class="yt-timestamp" data-t="01:15:14">[01:15:14]</a>.

Dr. Ness believes that questions related to causality are not going away and will not be made obsolete by new deep learning architectures <a class="yt-timestamp" data-t="01:16:11">[01:16:11]</a>.

---
**Find more about Dr. Robert Ness's work**:
*   Microsoft Researchers website <a class="yt-timestamp" data-t="01:51:52">[01:51:52]</a>
*   altdeep.ai <a class="yt-timestamp" data-t="01:51:59">[01:51:59]</a> (includes links to a GitHub repo: alt-deep/causal-ml with free tutorials and Jupyter notebooks) <a class="yt-timestamp" data-t="01:12:08">[01:12:08]</a>
*   LinkedIn <a class="yt-timestamp" data-t="01:12:23">[01:12:23]</a>