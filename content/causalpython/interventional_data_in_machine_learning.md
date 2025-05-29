---
title: Interventional data in machine learning
videoId: relI7Q9A03g
---

From: [[causalpython]] <br/> 

Interventional data plays a crucial role in the development and generalization capabilities of machine learning models, particularly large language models (LLMs). While traditional machine learning discussions often use terms like 'interventional', 'observational', or 'counterfactual' from Pearl's causal hierarchy, understanding the nature of data, whether actively collected or passively observed, is key <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

## Nature of Language Data

Although large language models are trained passively by processing language data from the internet, this data is not necessarily purely observational <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. For example, a scientific paper, even when merely absorbed by the model, contains interventional data from experiments conducted by others <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. Similarly, Stack Overflow posts involve debugging efforts with trials and errors, and conversations involve each statement acting as an intervention <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. Thus, language models learn passively from data that is inherently interventional, which is an important distinction <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

## Generalization Capabilities

The presence of interventional data in training can provide LLMs with causal strategies and understanding that generalize beyond the specific data they were trained on <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. By learning from others' interventions, models can discover generalizable strategies for intervening in new situations to uncover novel causal structures and achieve downstream goals <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. It is empirically shown that a generalizable strategy for intervening to determine causal structures can be discovered through passive observation of someone else's interventions <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

### Experimental Evidence

To explore this, researchers train simpler models on controlled data distributions, allowing for a better understanding of generalization. In one study, a model was trained on data showing interventions on causal Directed Acyclic Graphs (DAGs) <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. The model passively observed series of interventions aiming to maximize a variable on a set of DAGs that deliberately held out certain causal structures <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

The key insight was to test if the model, trained passively, could generalize to actively intervene and discover new causal structures at test time <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. Similar to how a language model becomes active when deployed with a user, the system, trained passively, was tested interactively <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. Results showed the system could apply passively observed causal strategies to actively intervene, discover new causal structures, and exploit them <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. This performance closely approximated correct causal reasoning, outperforming simpler heuristic or associational strategies <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

### Contrasting with "Causal Parrots" Hypothesis

While the "Causal Parrots" paper suggested that LLMs learn a "Meta Structural Causal Model" based on correlations of causal facts in training data, leading to the conclusion that models "talk causality but do not reason causally," the results from Dr. Lampinen's paper offer a contrasting view <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. Their findings suggest that models are capable of discovering a [[causal_inference_and_machine_learning | causal reasoning]] algorithm applicable in a new, generalizable setting, given a suitable training regime <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.

Although natural data contains more correlations and only occasional interventional data, influencing what models learn, experiments show that if LLMs are given explanations in prompts, they can learn to experiment and discover new causal structures effectively <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>. This suggests sufficient interventional data exists in training distributions for models to discover these strategies <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

## Optimizing Training Paradigms

The current training paradigm for large models is largely driven by scalability and what works <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. However, incorporating auxiliary tasks, such as providing natural language explanations of rewards in reinforcement learning, can significantly improve learning and generalization <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. This can even shape out-of-distribution generalization in confounded data <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.

Conditioning models on quality signals (e.g., reward estimates) during training is another emerging approach <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. This helps disentangle training and allows the system to generate high-quality responses at test time, even if it learned from lower-quality data <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. This is similar to offline reinforcement learning paradigms like Decision Transformer, where conditioning on a 'goodness' signal allows learning from suboptimal data without replicating it at test time <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

## Interventions in Agents and Auto-regressive Models

The term "agents" is broad, encompassing systems that take inputs and produce output actions in sequential decision-making problems, including language models <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. A key distinction is whether these agents interact with the environment during training or only at testing <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. Often, agents are trained partly on passive data (e.g., observing expert behavior) before fine-tuning with reinforcement learning, where they interact and receive rewards <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>. This multi-stage training, starting with passive language data and progressing to reinforcement learning with human preference rewards, is common for LLMs <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.

Regarding auto-regressive models and error accumulation in long-form content, state-of-the-art LLMs have some error correction abilities, as seen in Chain-of-Thought reasoning where they can identify and correct mistakes <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>. The architecture and context length influence this <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.

Passive learning is generally less efficient and can lead to poorer out-of-distribution generalization, as models may break down when they move off their training data distribution in active scenarios <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>. Techniques from offline reinforcement learning, such as DAgger, use a small amount of interventional data to guide the system back to the data distribution if it deviates <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>. The reinforcement learning step in LLM training, or supervised tuning on real generations from user interactions, can be considered a form of interventional data <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. The precise amount of interventional data needed for robust models remains an open and complex question <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

## Causal Data Fusion and Prior Knowledge

There is a parallel between these ideas and [[causal_inference_and_machine_learning | causal inference]] literature on "causal data fusion," which involves mixing observational and interventional data <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. This fusion aims to recover causal structures and maximize inference efficiency <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>. Similarly, systems can be cued with "prior knowledge" from observational sources (e.g., literature) to identify relevant variables, enabling more efficient determination of causal structure by intervening only on those variables <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>. Combining observational data in the learning process can efficiently pinpoint promising areas for intervention <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>.

## Implications for System Design

Overly constraining reasoning processes in a system, based on assumptions about how it "should" work (e.g., being a formal logical reasoner), can make the system more fragile <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>. If these assumptions don't match reality, the system can completely break down <a class="yt-timestamp" data-t="00:44:30">[00:44:30]</a>. Instead, approaches that encourage systems to represent important information without excessively constraining internal computations, such as explanation prediction objectives, can be more effective <a class="yt-timestamp" data-t="00:44:40">[00:44:40]</a>.

While strong inductive biases can improve performance for specific, well-defined problems, this approach can lead to brittleness at scale, as described by Rich Sutton's "The Bitter Lesson" <a class="yt-timestamp" data-t="00:45:03">[00:45:03]</a>. Softer solutions, like providing explanations or modifying the data distribution (e.g., by incorporating more interventional data), are often more effective and scalable for complex, real-world problems like building large language models or agents for rich virtual environments <a class="yt-timestamp" data-t="00:46:01">[00:46:01]</a>.

Working with real-world data and tasks, even with their ill-defined nature and unknown distributions, serves as a "forcing function" to prevent overfitting and ensure that models truly solve real problems, not just toy ones designed for specific algorithms <a class="yt-timestamp" data-t="00:46:48">[00:46:48]</a>. This practical application tests the robustness of ideas and solutions <a class="yt-timestamp" data-t="00:47:53">[00:47:53]</a>.