---
title: Role of representation learning in modern AI
videoId: ubSFglvhBd0
---

From: [[causalpython]] <br/> 

Representation learning is a core aspect of modern [[causal_ai_and_machine_learning | machine learning]], particularly within the context of high-dimensional [[future_directions_for_causal_ai_and_generative_models | generative models]] <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. This field is seen as a way to make progress on fundamental problems in [[causal_ai_and_machine_learning | machine learning]] and inference, going beyond traditional statistical dependencies <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a> <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

## From Statistical to Interventional Representations

Current [[The Evolution of AI Technologies Deep Learning vs Causal AI | AI]] and [[causal_ai_and_machine_learning | machine learning]], especially [[future_directions_for_causal_ai_and_generative_models | generative AI]], largely rely on statistical representations. These models identify and transform statistical dependencies in data to find useful patterns, often in lower-dimensional spaces, for tasks like large-scale pattern recognition <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a> <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

However, to enable "thinking as acting in an imagined space"—a metaphor for intelligence <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a> <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>—representations need to become interventional. This means they must incorporate the notion of intervention and action, allowing the system to simulate actions and their effects within its internal model <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a> <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

## Addressing Challenges in Data and Environment

In scenarios where data is not independent and identically distributed (IID), or when conditions and measured variables change, simple correlations are insufficient <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Such dynamic real-world settings necessitate [[causal_ai_and_its_connection_to_machine_learning | causal]] approaches <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

[[causal_ai_and_its_connection_to_machine_learning | Causal]] representation learning aims to discover the underlying entities or "symbols" in high-dimensional data that should be modeled [[causal_ai_and_its_connection_to_machine_learning | causally]], even when these entities are not explicitly provided <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a> <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. This involves learning how to represent data by observing how things change in the environment, such as changes in lighting, camera position, or object manipulation, which helps violate the IID assumption and reveals underlying causal structures <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a> <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

## Contrast with Classical AI

Classical [[The Evolution of AI Technologies Deep Learning vs Causal AI | AI]] often assumes that symbols (e.g., chess pieces on a board) are already given, and then focuses on algorithms to process these symbols <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. Modern [[causal_ai_and_machine_learning | machine learning]], through representation learning, tackles the harder problem of identifying these symbols and finding suitable data representations in the first place, especially when direct observation of play is the only input <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

## Inspiration from Biological Systems

Biological systems offer a compelling blueprint for intelligence, particularly in how they manage finite training and computational resources <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a> <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>. Instead of building separate systems for every changing condition (like light spectrum for recognizing an apple from morning to evening), biological systems develop modular solutions (e.g., color constancy) that can be reused across different tasks <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a> <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.

This modular learning approach suggests that the learned modules in the brain might reflect structural similarities with the modular composition of the world itself <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>. Furthermore, an internal model allows for "acting in an imagined space," simulating actions without risking real-world consequences, enabling more efficient learning and credit attribution <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a> <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>.

A key concept is the commutative diagram, where imagining an intervention on a mental representation of an object yields the same result as performing the intervention in the real world and then perceiving the evolved object <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. This highlights the consistency required for interventional representations.

## Future Directions

Research should focus on bridging [[causality_and_ai_challenges_and_opportunities | causality]] and [[future_directions_for_causal_ai_and_generative_models | generative modeling]], especially for controllable generation, as many working in this area may not recognize its connection to [[causal_ai_and_its_connection_to_machine_learning | causality]] <a class="yt-timestamp" data-t="00:32:36">[00:32:36]</a>. This involves integrating [[causality_robustness_and_fairness_in_ai_models | causal]] principles into the training of high-performance [[The Evolution of AI Technologies Deep Learning vs Causal AI | generative models]] and [[Symbolic reasoning and logical deduction in AI | neural networks]] <a class="yt-timestamp" data-t="00:33:04">[00:33:04]</a>.