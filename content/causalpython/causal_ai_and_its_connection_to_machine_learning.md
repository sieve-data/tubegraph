---
title: Causal AI and its connection to machine learning
videoId: ubSFglvhBd0
---

From: [[causalpython]] <br/> 

The "Causal Bandits" podcast hosted Bernhard Schölkopf, a professor and director at the Max Planck Institute for Intelligent Systems, to discuss the intersection of causality and [[machine_learning_and_causality | machine learning]] <a class="yt-timestamp" data-t="01:05:07">[01:05:07]</a>. Schölkopf, a recipient of the ACM Alan Newell Award, emphasizes that many interesting open problems in [[machine_learning_and_causality | machine learning]] are connected to causality <a class="yt-timestamp" data-t="03:44:03">[03:44:03]</a>.

## Journey into Causality

Bernhard Schölkopf's journey into causality was a gradual process <a class="yt-timestamp" data-t="01:47:05">[01:47:05]</a>. Around 20 to 25 years ago, he was introduced to the theory of causal inference by Judea Pearl at a conference <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>. While fascinated by the mathematical study of causality, he initially continued his work on kernel methods <a class="yt-timestamp" data-t="02:40:02">[02:40:02]</a>.

Some years later, a persistent student of his friend Dominique Janzing, who was working on quantum information theory, wanted to focus on causality, leading Schölkopf and Janzing to advise the student together <a class="yt-timestamp" data-t="02:48:05">[02:48:05]</a>. This collaboration drew him deeper into the field, eventually making [[causal_ai_and_machine_learning | causal AI]] his primary research focus <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>. He realized that causality was not separate from [[machine_learning_and_causality | machine learning]], but rather a path to progress on fundamental problems in [[machine_learning_and_causality | machine learning]] and inference <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.

## *Elements of Causal Inference*

Schölkopf co-authored *Elements of Causal Inference* with Dominik Janzing and Jonas Peters <a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a>. Their aim was to provide a modern and reasonably compact treatment of the main ideas of causality <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>. He advises authors to aim for a short book and finish it within two years to avoid it becoming "too painful" <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>. They are currently working on a new book focusing on [[causal_ai_and_machine_learning | causal representation]] building <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>.

### Causal Representation Learning

Modern [[machine_learning_and_causality | machine learning]] heavily relies on representation learning, especially for high-dimensional generative models <a class="yt-timestamp" data-t="06:02:00">[06:02:00]</a>. In an IID (independent and identically distributed) data setting, correlation statistics are often sufficient <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>. However, when conditions change—such as distribution shifts or changes in measured variables—causality becomes essential <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>.

[[causal_ai_and_machine_learning | Causal representation]] learning addresses scenarios where causal entities in high-dimensional data are not explicitly given <a class="yt-timestamp" data-t="06:46:00">[06:46:00]</a>. For instance, in an image, an [[causal_ai_and_machine_learning | AI]] must learn which pixels form an object <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>. Violating the IID assumption (e.g., by changing lighting, camera position, or moving objects) can provide clues on how to represent data and identify the underlying "objects" or "symbols" <a class="yt-timestamp" data-t="07:21:00">[07:21:00]</a>.

A major advancement of [[machine_learning_and_causality | machine learning]] over classical [[The Evolution of AI Technologies Deep Learning vs Causal AI | AI]] is its ability to learn symbols rather than assuming they are given <a class="yt-timestamp" data-t="07:58:00">[07:58:00]</a>. For example, instead of being given chess piece positions, an [[causal_ai_and_machine_learning | AI]] observing chess play must identify the pieces and their states <a class="yt-timestamp" data-t="08:22:00">[08:22:00]</a>.

## [[Causality and Machine Learning | Causality and Machine Learning]] in Intelligence

Schölkopf views intelligence, both artificial and natural, through the lens of animal behavior <a class="yt-timestamp" data-t="09:05:00">[09:05:00]</a>. He cites Konrad Lorenz, a father of ethology, who stated that "thinking is nothing but acting in an imagined space" <a class="yt-timestamp" data-t="09:32:00">[09:32:00]</a>. Current [[machine_learning_and_causality | machine learning]], including generative [[The Evolution of AI Technologies Deep Learning vs Causal AI | AI]], primarily relies on statistical representations for large-scale pattern recognition <a class="yt-timestamp" data-t="09:52:00">[09:52:00]</a>.

To move towards "thinking in an imagined space," representations must become "interventional" <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>. This requires incorporating a notion of intervention and action, which points towards [[causal_ai_and_machine_learning | causality]] <a class="yt-timestamp" data-t="10:37:00">[10:37:00]</a>. Biological systems offer a model for this: they integrate external signals with "efference copies" of actions (copies of brain commands for movement) to form an internal world model <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>. This internal model allows for simulating the world and actions within it, reducing the need to "risk your life every time you learn" <a class="yt-timestamp" data-t="20:56:00">[20:56:00]</a>.

While correlational learning is powerful and likely accounts for much of human and animal cognition, biological systems operate with finite training data and computational resources <a class="yt-timestamp" data-t="13:43:00">[13:43:00]</a>. This forces them to be more modular and reuse learned modules <a class="yt-timestamp" data-t="15:10:00">[15:10:00]</a>. For instance, the human visual system maintains color consistency despite varying light conditions, applying this ability across various recognition tasks <a class="yt-timestamp" data-t="14:55:00">[14:55:00]</a>.

Schölkopf highlights a fascinating idea from physicist Heinrich Hertz: if an object is represented in the brain, and then its evolution is thought about, the result should match performing the evolution in the real world and then representing the evolved object <a class="yt-timestamp" data-t="16:53:00">[16:53:00]</a>. This implies a "commutative diagram" that captures consistency between mental simulation and real-world intervention <a class="yt-timestamp" data-t="17:38:00">[17:38:00]</a>.

## Physics and Causality

Schölkopf, with his background in physics and mathematics, views [[causality_and_machine_learning | causal systems]] from a multi-level perspective <a class="yt-timestamp" data-t="22:42:00">[22:42:00]</a>. While [[machine_learning_and_causality | machine learning]] often operates at the level of statistical dependencies or correlations, physics' "gold standard" involves differential equations that allow for simulation and reasoning about interventions <a class="yt-timestamp" data-t="23:30:00">[23:30:00]</a>. Structural causal models (SCMs) sit between these extremes, aiming to preserve the simplicity of [[machine_learning_and_causality | machine learning]] methods while enabling understanding and reasoning about interventions without a full mechanistic understanding <a class="yt-timestamp" data-t="24:05:00">[24:05:00]</a>.

A key concept is that of "mechanisms" – physical processes that give rise to statistical dependencies <a class="yt-timestamp" data-t="25:19:00">[25:19:00]</a>. A lot of Schölkopf's work, particularly on independent mechanisms, focuses on additional assumptions that capture how [[Causality and Machine Learning | causal systems]] are physically realized in the world <a class="yt-timestamp" data-t="25:57:00">[25:57:00]</a>. His work with Lars Kaiser on using stochastic differential equations for causality is motivated by the prevalence of time-series data in practice and the challenge of handling loops in causal graphs <a class="yt-timestamp" data-t="26:42:00">[26:42:00]</a>.

## Future Directions for [[causal_ai_and_machine_learning | Causal AI]]

Schölkopf believes the [[causal_ai_and_machine_learning | causal AI]] community needs to:
*   Develop compelling applications to convince the broader [[machine_learning_and_causality | machine learning]] community of its value <a class="yt-timestamp" data-t="32:00:00">[32:00:00]</a>.
*   Work at the interface of [[Causality and Machine Learning | causality]] and generative modeling <a class="yt-timestamp" data-t="32:23:00">[32:23:00]</a>. Many people working on controllable generation in [[generative_ai | generative AI]] don't realize its connection to [[causality_and_machine_learning | causality]] <a class="yt-timestamp" data-t="32:36:00">[32:36:00]</a>. He encourages researchers, especially young students, to embrace neural networks and connect them to [[causality_and_machine_learning | causality]] in interesting ways <a class="yt-timestamp" data-t="32:57:00">[32:57:00]</a>.

## Advice for Researchers

Schölkopf offers two key pieces of advice for those entering complex fields like [[Causality and Machine Learning | causality]] or advanced physics:
1.  **Pick a good problem**: Choose a problem that hasn't been "beaten to death" to maximize the chance of making a novel contribution <a class="yt-timestamp" data-t="33:49:00">[33:49:00]</a>.
2.  **Go into depth**: Once a problem is chosen, don't be afraid to dig deep. Even if the initial goal isn't met, staying with a problem long enough will likely uncover something intriguing <a class="yt-timestamp" data-t="34:31:00">[34:31:00]</a>.

### Influential Books

He cites several books that influenced him:
*   **Borges's writings**: Especially the short story "Borges and I," which explores the difference between the individual and the author <a class="yt-timestamp" data-t="28:03:00">[28:03:00]</a>.
*   **Hans Primas's *Chemistry, Quantum Physics, and Reductionism*** <a class="yt-timestamp" data-t="29:24:00">[29:24:00]</a>.
*   **Vladimir Vapnik's *Estimation of Dependencies from Empirical Data* / *Statistical Data***: This book, focusing on perceiving non-random structure and identifying dependencies mathematically, profoundly influenced him <a class="yt-timestamp" data-t="30:20:00">[30:20:00]</a>.
*   **Vladimir Vapnik's *The Nature of Statistical Learning Theory***: As Vapnik's PhD advisor, Schölkopf proofread and discussed many parts of this more philosophical book, which further shaped his thinking <a class="yt-timestamp" data-t="31:09:00">[31:09:00]</a>.