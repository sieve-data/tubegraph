---
title: Applications of generative modeling in causality
videoId: ubSFglvhBd0
---

From: [[causalpython]] <br/> 

The intersection of [[causality_in_ai | causality]] and [[generative_ai_and_causal_reasoning | generative modeling]] is a significant area of focus in modern [[machine_learning_and_causality | machine learning]], particularly for addressing limitations in current artificial intelligence systems and developing more robust and intelligent agents <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Connecting Generative Models and Causality

Current [[generative_ai_and_causal_reasoning | generative AI]] and [[machine_learning_and_causality | machine learning]] models primarily rely on statistical representations, focusing on correlations and large-scale pattern recognition <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. While impressive, this approach lacks the ability to understand interventions and actions <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.

Thinking, as described by ethologist Konrad Lorenz, is "acting in an imagined space" <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. To achieve this in AI, representations must be interventional, allowing for actions within the imagined space <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. This necessitates a move towards [[causality_in_ai | causality]], where representations include notions of intervention and action <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.

Many problems in [[generative_ai_and_causal_reasoning | generative modeling]], especially "controllable generation," are inherently linked to [[causality_in_ai | causality]], even if practitioners are not always aware of this connection <a class="yt-timestamp" data-t="00:32:36">[00:32:36]</a>.

## Causal Representation Learning

Modern [[machine_learning_and_causality | machine learning]] heavily focuses on representation learning, particularly with high-dimensional [[generative_ai_and_causal_reasoning | generative models]] <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. In settings where data is independently and identically distributed (IID), statistical dependencies and correlations are sufficient <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. However, in real-world scenarios where conditions or measured variables change, [[causality_in_ai | causality]] becomes crucial <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

[[causality_in_agentbased_systems | Causal representation learning]] addresses scenarios where the entities to be causally modeled in high-dimensional data are not explicitly given <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. For example, in an image, determining which pixels form an object is not pre-defined <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. By observing changes in data—such as lighting variations, camera movement, or object manipulation—the IID assumption is violated, providing hints on how to represent the data and identify the underlying "objects" or low-dimensional causal representations <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. This contrasts with classical AI, which often assumes symbols are already provided <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

## Biological Inspiration and Finite Data

Biological systems, as compelling examples of intelligence, operate with finite training data and computational resources, unlike [[large_language_models_and_causality | large language models]] that leverage vast amounts of collected cultural knowledge <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. This resource constraint forces biological systems to learn more efficiently, often in a modular fashion <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.

This modular learning suggests that the modules learned by biological systems might structurally correspond to modules in the physical world <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>. For instance, the human retina's gain control mechanisms allow for color consistency despite varying light conditions throughout the day, enabling recognition of objects like apples regardless of ambient light <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>. This module, once learned, can be reused across different recognition tasks <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.

The physicist Hermann von Helmholtz proposed a principle of consistency: if an object is represented in the brain, its imagined evolution (e.g., moving it in thought) should yield the same result as physically moving the object and then observing it again <a class="yt-timestamp" data-t="00:16:53">[00:16:53]</a>. This "commutative diagram" highlights the importance of interventional representations that accurately simulate real-world actions <a class="yt-timestamp" data-t="00:17:38">[00:17:38]</a>.

## Internal World Models for Learning

While correlational learning is valuable for rapid responses and many tasks, internal world models, which are enhanced by [[causality_in_ai | causality]], offer significant benefits, particularly in situations where trial-and-error is too risky <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.

For example, learning to prepare food safely or attributing the cause of sickness requires more than mere correlation; it benefits from a model that allows for simulating interventions and understanding consequences without direct experience <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>. This contrasts with automatic actions, like brushing teeth, where explicit world models are not needed after extensive practice <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>. However, even for such tasks, the ability to imagine modifications (e.g., avoiding a sore tooth) showcases the utility of an underlying world model <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>.

## Future Directions in AI

To advance the field, particularly in the context of [[the_future_of_ai_integrating_generative_ai_and_causal_ai | integration of language models and causality]], the community should focus on:

*   **Compelling [[practical_applications_of_causal_methods | Applications]]**: Demonstrating the tangible benefits of [[causality_in_ai | causal models]] through practical applications is essential to convince the broader AI community <a class="yt-timestamp" data-t="00:31:58">[00:31:58]</a>.
*   **Interface between Causality and [[generative_ai_and_causal_reasoning | Generative Modeling]]**: Researchers should actively work at this intersection, understanding that many challenges in [[generative_ai_and_causal_reasoning | generative modeling]], especially controllable generation, are deeply connected to [[causality_in_ai | causality]] <a class="yt-timestamp" data-t="00:32:23">[00:32:23]</a>. This involves engaging with high-performance [[generative_ai_and_causal_reasoning | generative models]] and neural networks, integrating causal principles into their design <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>.