---
title: Causality and Machine Learning
videoId: gazCIKYEv44
---

From: [[causalpython]] <br/> 

The Causal Bandits podcast focuses on [[causality_in_artificial_intelligence | causality]] and [[causal_ai_and_machine_learning | machine learning]] <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. This episode features Dr. Robert Ness, a senior researcher at Microsoft Research <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Dr. Robert Ness's Journey to Causality

Dr. Robert Ness began his educational journey in economics, later transitioning to computation and [[causality_in_artificial_intelligence | causal inference]] <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. A unifying aspect across these choices was his desire to engage in quantitative work that connected to real-world applied problems <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. Statistics came naturally to him, a "superpower" that made formal mathematical topics seem effortless <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. What he found most attractive was the process of modeling data, doing data science, and building models <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

### Influence of Systems Biology

His experience in systems biology during his PhD greatly influenced his thinking about [[causality_in_artificial_intelligence | causality]] <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. He chose to work in systems biology over financial engineering because he felt financial markets lacked an "anchor in reality" <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. In natural sciences, a "ground truth" exists to model, even if the model is an approximation <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. He was drawn to complex and dynamic systems, building models to simulate processes like the workings of a cell <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

Through computational and systems biology, he was introduced to the task of using structure learning or causal discovery algorithms to reconstruct biological pathways, specifically signal transduction pathways, from single-cell data <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

### Challenges in Applied Causal Discovery

The main challenge in applying structural algorithms to biological data was building something useful in practice <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. [[causality_in_artificial_intelligence | Causal discovery]] involves taking data (observational or experimental) and learning the causal properties of a system, typically the structure of a causal Directed Acyclic Graph (DAG) <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. While explosion in molecular biology measurement technology provided rich datasets, simply generating a graph from an algorithm was not enough for biologists <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. They needed to use the graph to solve specific problems, such as discovering new biomarkers or informing drug discovery <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

To address this, Dr. Ness began steering [[causality_in_artificial_intelligence | causal discovery]] methods towards experimental design, particularly Bayesian experimental design <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. This approach focuses on an outcome where the DAG is an intermediate artifact, dealing with uncertainty and experimental design questions like "what should I measure?" <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

Evaluating the correctness of a learned structure was done by measuring the distance between the learned graph and a known ground truth graph using metrics like precision-recall or structural Hamming distance <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. However, this is only useful when the ground truth is known <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. Dr. Ness turned to Bayesian reasoning to deal with uncertainty and incorporate prior knowledge about the system (e.g., protein interactions) <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. This allowed for a rigorous way to incorporate all knowledge and uncertainty, providing guarantees that even without knowing the exact ground truth, the approach would move towards the correct answer given more data <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.

## Causal Decision Making and Reinforcement Learning

The broader field of [[causal_ai_and_machine_learning | causal decision making]] or causal decision theory has an interesting history, often contrasted with "empirical decision theory" <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. Traditional views of decision-making focus on maximizing expected utility conditional on interaction, whereas causal decision theory emphasizes attending to the consequences of actions <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

With a more mature understanding of [[structural_causal_models_and_machine_learning | causal models]], [[causal_ai_and_machine_learning | causal decision making]] is emerging in automated decision theory, as seen in "causal bandits" <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. Another area gaining traction is [[causal_ai_and_machine_learning | causal reinforcement learning]] <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>.

### Advantages of Causal Reinforcement Learning

[[causal_ai_and_machine_learning | Causal reinforcement learning]] typically aims to:
*   **Increase sample efficiency**: By leveraging causal assumptions about the data generating process, it's possible to make inferences not possible with traditional statistical pattern modeling <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>. This is crucial in high-dimensional settings, making intractable problems tractable <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
*   **Improve credit assignment**: When understanding why a policy led to a certain outcome, it can be posed as a causal question, using attribution or root cause analysis methods from [[causality_in_artificial_intelligence | causal inference]] theory <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.

Traditional deep reinforcement learning often folds everything into a "state variable," ignoring causal nuances <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>. While this is often sufficient for maximizing reward, it can lead to suboptimal decisions when actions change the environment in ways not captured by traditional methods <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>. [[causality_in_artificial_intelligence | Causality]] helps understand when and how these differences occur <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>.

### When Causal Models are Necessary

It's not always necessary to use [[structural_causal_models_and_machine_learning | causal models]], as traditional methods might work well in many practical scenarios <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>. The core challenge in [[causal_machine_learning_in_medicine_and_industry | causal machine learning]] is identifying practical scenarios where a causal model is *definitely* required <a class="yt-timestamp" data-t="00:21:30">[00:21:30]</a>.

For example, while the expectation of Y given a "do action" (interventional) and the expectation of Y given an observed action (observational) are often different, the *action* that maximizes both might be the same <a class="yt-timestamp" data-t="00:24:10">[00:24:10]</a>. To motivate using a causal model, one must zero in on instances where the maximizing action for interventional and observational queries are different and frequently different in a practical scenario <a class="yt-timestamp" data-t="00:25:30">[00:25:30]</a>. This requires significant domain knowledge <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>.

## Causality and Artificial General Intelligence (AGI)

From a [[causality_in_artificial_intelligence | causal perspective]], an AGI model would need to be able to reason about cause and effect <a class="yt-timestamp" data-t="00:29:56">[00:29:56]</a>. This aligns with computational psychology research, which observes and computationally models human reasoning abilities <a class="yt-timestamp" data-t="00:30:10">[00:30:10]</a>. [[causality_in_artificial_intelligence | Causal models]] and [[causality_in_artificial_intelligence | causal inference]] theory specify assumptions and inductive biases that allow conclusions beyond what can be made from observed data alone <a class="yt-timestamp" data-t="00:31:16">[00:31:16]</a>.

A key distinction arises between answering objective questions about cause-effect relationships in the world (e.g., "does this drug treat this illness?") and emulating human reasoning, which might involve cognitive biases or inaccurate heuristics <a class="yt-timestamp" data-t="00:33:11">[00:33:11]</a>. While these goals often overlap, an AGI model might need to capture human-like reasoning even if it's not objectively perfect <a class="yt-timestamp" data-t="00:34:16">[00:34:16]</a>.

Humans engage in counterfactual simulation, imagining hypothetical scenarios, but are less likely to simulate counterfactually in the absence of actions or events <a class="yt-timestamp" data-t="00:35:55">[00:35:55]</a>. This is an economical heuristic because it's easier to enumerate actions that happened than those that did not <a class="yt-timestamp" data-t="00:36:31">[00:36:31]</a>. Developing algorithms that can address this gap (e.g., by scoping out negative events) can improve upon human heuristics <a class="yt-timestamp" data-t="00:37:15">[00:37:15]</a>.

## Integration of Causal Reasoning in Machine Learning

Dr. Ness highlights a paper he co-authored that demonstrates how [[integration_of_causal_reasoning_in_machine_learning | causal identification results]] can be integrated with probabilistic machine learning frameworks <a class="yt-timestamp" data-t="00:38:29">[00:38:29]</a>. The paper showed that if an intervention distribution is identified using rules like the "do-calculus," then sampling from a latent variable model (like those in PyMC, Stan, or Pyro) is a valid procedure <a class="yt-timestamp" data-t="00:39:19">[00:39:19]</a>. As training data increases, the distribution sampled from converges to the ground truth interventional distribution <a class="yt-timestamp" data-t="00:40:46">[00:40:46]</a>.

This means that latent variable models, which can be represented as graphs, can be used for causal inference if identification can be proven using graphical identification frameworks <a class="yt-timestamp" data-t="00:41:07">[00:41:07]</a>. Tools like Python's "Ynot" library can determine if a query of interest is identifiable given a DAG and observed variables <a class="yt-timestamp" data-t="00:41:50">[00:41:50]</a>. This opens the world of causal reasoning to people familiar with model-based probabilistic programming workflows <a class="yt-timestamp" data-t="00:42:07">[00:42:07]</a>.

### Cairo and Abstraction of Causal Operations

The new "Cairo" library builds on Pyro, abstracting certain causal operations on graphical models <a class="yt-timestamp" data-t="00:46:01">[00:46:01]</a>. It addresses the difficulty of conditioning on evidence in models with deterministically set variables (like structural causal models), which often leads to intractable likelihoods <a class="yt-timestamp" data-t="00:47:11">[00:47:11]</a>. Cairo aims to abstract away the "inference engineering" aspect, allowing users to focus on causal reasoning <a class="yt-timestamp" data-t="00:47:54">[00:47:54]</a>. Its philosophy draws parallels between causal uncertainty and Bayesian uncertainty, connecting probabilistic machine learning with [[causality_in_artificial_intelligence | causality]] <a class="yt-timestamp" data-t="00:48:03">[00:48:03]</a>.

## The Future of Causality in AI

A significant area for future development is **causal representation learning** <a class="yt-timestamp" data-t="00:49:48">[00:49:48]</a>. This involves learning latent representations that correspond to actual causes in the data generating process <a class="yt-timestamp" data-t="00:50:07">[00:50:07]</a>. The knowledge of [[causality_in_artificial_intelligence | causality]] can be used to identify desiderata for how these causes should behave, for example, by being modular and invariant under intervention <a class="yt-timestamp" data-t="00:50:20">[00:50:20]</a>.

### Generative AI and Causal Representations

In generative AI, like Midjourney or Stable Diffusion, users often want to make precise, localized changes (e.g., changing glasses color without affecting the entire image) <a class="yt-timestamp" data-t="00:51:10">[00:51:10]</a>. This is a counterfactual question: "What would this image look like if X were different, but nothing else changed except what is causally downstream of X?" <a class="yt-timestamp" data-t="00:51:43">[00:51:43]</a>. Current models often produce artifacts or unwanted changes, highlighting a need for semantic, causal control over generated content <a class="yt-timestamp" data-t="00:52:21">[00:52:21]</a>. Operating semantically on learned causal representations would make such adjustments much easier <a class="yt-timestamp" data-t="00:52:40">[00:52:40]</a>. This could transform generative AI by providing "knobs" for precise creative control, similar to how text can be edited in large language models <a class="yt-timestamp" data-t="00:53:19">[00:53:19]</a>.

### Causal Large Language Models (LLMs)

The concept of large language models (LLMs) learning a "world model" essentially refers to them learning a [[structural_causal_models_and_machine_learning | causal model]] <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>. The "causal hierarchy theorem" (also known as Pearl's Causal Ladder) outlines three levels of reasoning: associational (level 1), interventional (level 2), and counterfactual (level 3) <a class="yt-timestamp" data-t="00:55:50">[00:55:50]</a>. To answer questions at a given level, assumptions at that same level are required <a class="yt-timestamp" data-t="00:56:31">[00:56:31]</a>. For example, answering a counterfactual question requires level three assumptions, often in the form of a [[structural_causal_models_and_machine_learning | structural causal model]] <a class="yt-timestamp" data-t="00:56:42">[00:56:42]</a>.

While LLMs can empirically answer causal questions (e.g., "does smoking cause cancer?") and even perform causal analysis in code, they are prone to "hallucinations," saying things as if true when they are not <a class="yt-timestamp" data-t="00:57:05">[00:57:05]</a>. The challenge is to ensure reliable causal answers and reduce hallucination <a class="yt-timestamp" data-t="00:57:50">[00:57:50]</a>. This requires that the necessary causal assumptions exist somewhere, whether in the training data, model architecture, or prompt <a class="yt-timestamp" data-t="00:58:43">[00:58:43]</a>.

One research direction involves incorporating [[causality_in_artificial_intelligence | causal information]] into the Transformer architecture itself to provide theoretical guarantees for answering causal queries <a class="yt-timestamp" data-t="01:00:08">[01:00:08]</a>. This contrasts with the current emphasis on simply scaling models with ever-larger datasets <a class="yt-timestamp" data-t="01:02:51">[01:02:51]</a>. Leveraging innate structure in data, such as the history of a code repository or the act structure of film scripts, can lead to more efficient and powerful models even with smaller datasets <a class="yt-timestamp" data-t="01:04:18">[01:04:18]</a>.

## Personal Insights and Advice

### Influential Books
*   **"Computational Systems Biology" by Darren Wilkinson**: This book provided a broad introduction to computational Bayes and how to build computational models of dynamic systems, heavily influencing Dr. Ness's research <a class="yt-timestamp" data-t="01:05:45">[01:05:45]</a>.
*   **A book by Hadley Wickham on the R language**: This introduced Dr. Ness to functional programming paradigms, shaping his approach as a modeler <a class="yt-timestamp" data-t="01:07:32">[01:07:32]</a>.

### Precious Life Lesson
The power of routine and habits <a class="yt-timestamp" data-t="01:10:37">[01:10:37]</a>. Motivation and excitement are unreliable, but consistent habits provide reliable fuel to keep progressing, especially during unmotivated times <a class="yt-timestamp" data-t="01:10:55">[01:10:55]</a>.

### Advice for Aspiring Causality Researchers
1.  **Work through a good book**: Understand the "shape of the territory" to identify the research frontier and push against it <a class="yt-timestamp" data-t="01:13:29">[01:13:29]</a>.
2.  **Identify impactful people**: Find researchers making a difference in the field by attending workshops, listening to podcasts, and examining their papers and citations <a class="yt-timestamp" data-t="01:13:56">[01:13:56]</a>.
3.  **Connect with the community**: During training (e.g., PhD), be in proximity to the network of people doing the work you care about <a class="yt-timestamp" data-t="01:14:26">[01:14:26]</a>. Focus on connecting with individuals rather than solely pursuing prestigious institutions <a class="yt-timestamp" data-t="01:15:14">[01:15:14]</a>.

The future of [[causality_in_artificial_intelligence | causality]] is assured, as these fundamental questions are not likely to be made obsolete by new [[machine_learning_and_causality | deep learning]] architectures <a class="yt-timestamp" data-t="01:16:11">[01:16:11]</a>.