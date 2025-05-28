---
title: Continuous thought and unrestricted latent spaces
videoId: YhrwYZ3Nsio
---

From: [[hu-po]] <br/> 

The concept of [[generative_latent_space_reasoning|Generative latent space reasoning]] is a broad term, not a formally defined field, that encompasses various methods for AI models to reason and process information within continuous, high-dimensional spaces rather than discrete tokens <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>. This approach aims to move beyond traditional tokenization schemes to unlock more nuanced and complex reasoning capabilities <a class="yt-timestamp" data-t="02:50:50">[02:50:50]</a>.

## The "Chain of Continuous Thought" Paradigm

A new paradigm called "Chain of Continuous Thought" (COCONUT) proposes that Large Language Models (LLMs) can reason in an unrestricted [[latent_space_reasoning|latent space]] <a class="yt-timestamp" data-t="08:53:00">[08:53:00]</a>. This method utilizes the last hidden state of the LLM as a representation of the reasoning state, termed "continuous thought" <a class="yt-timestamp" data-t="09:05:00">[09:05:00]</a>.

Traditional reasoning models, like OpenAI's O1 or Google's Gemini Flash, generate a "Chain of Thought" by producing a sequence of discrete tokens (e.g., English words) <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>. This textual Chain of Thought is then used to increase the probability of successfully solving a task, particularly in areas like programming or math <a class="yt-timestamp" data-t="09:44:00">[09:44:00]</a>. In contrast, the "continuous thought" approach avoids converting the last hidden state into a discrete token, instead feeding the high-dimensional embedding directly back into the model <a class="yt-timestamp" data-t="10:44:00">[10:44:44]</a>.

### Fuzzy vs. Discrete Reasoning

The term "unrestricted [[latent_space_reasoning|latent space]]" refers to a continuous space where any vector can be defined, analogous to a "hilly landscape in a very [[highdimensional_spaces_and_information_storage|high-dimensional space]]" <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>. By keeping the reasoning "fuzzy" within this continuous embedding, models can potentially encode more nuance and information than by forcing it to collapse into discrete tokens <a class="yt-timestamp" data-t="11:35:00">[11:35:00]</a>.

This concept bears strong resemblance to recurrent neural networks (RNNs) and State Space Models (SSMs) like Mamba, which utilize a "hidden state" (H_T) to encode information from previous steps and condition the model's output <a class="yt-timestamp" data-t="12:32:00">[12:32:00]</a>. The "fuzziness" of these continuous [[latent_space_reasoning|latent space]]s is both an advantage and a limitation: while allowing for rich information encoding, it can also lead to imprecision or information loss <a class="yt-timestamp" data-t="14:03:00">[14:03:00]</a>.

## Information Density and Interpretability Challenges

[[continuous_vs_discrete_optimization|Continuous latent spaces]] can convey significantly more information density and nuance compared to human languages, potentially achieving a 10x increase in information rate <a class="yt-timestamp" data-t="17:17:00">[17:17:00]</a>. This higher information density allows for more complicated Chains of Thought, potentially leading to better and quicker answers <a class="yt-timestamp" data-t="17:50:00">[17:50:00]</a>.

However, a major downside of reasoning in continuous [[latent_space_reasoning|latent space]]s is the loss of human interpretability <a class="yt-timestamp" data-t="15:10:00">[15:10:00]</a>. Unlike English tokens, which can be read and understood, a [[latent_space_reasoning|latent space]] Chain of Thought appears as a long vector of numbers, making it impossible for humans to understand the reasoning process or identify flawed steps <a class="yt-timestamp" data-t="15:43:00">[15:43:00]</a>. This lack of transparency raises concerns about AI's ability to deceive or for errors to go undetected <a class="yt-timestamp" data-t="16:06:00">[16:06:00]</a>.

## Large Concept Models

Another approach, exemplified by "Large Concept Models," uses a sentence embedding space like Sonar to represent entire sentences as high-dimensional vectors <a class="yt-timestamp" data-t="18:59:00">[18:59:00]</a>. The language model then auto-regressively predicts "concepts" within this frozen embedding space <a class="yt-timestamp" data-t="19:50:00">[19:50:00]</a>. This is analogous to a traditional LLM operating on tokens, but at a higher level of abstraction <a class="yt-timestamp" data-t="20:07:00">[20:07:07]</a>.

The concept of "separable representations" in these vector spaces means that different concepts can be distinctly separated by drawing "lines" or boundaries within the [[latent_space_reasoning|latent space]], allowing for clear partitioning of information <a class="yt-timestamp" data-t="23:31:00">[23:31:00]</a>.

## Emergent Reasoning in Generative Models

There's a growing understanding that visual understanding and visual generation are mutually beneficial and interconnected <a class="yt-timestamp" data-t="51:05:00">[51:05:00]</a>. Training models with visual understanding data significantly enhances their visual generation capabilities <a class="yt-timestamp" data-t="51:21:00">[51:21:00]</a>. This means that as generative models improve their ability to create realistic images and videos (e.g., Google's V2), they also develop an emergent capability for visual reasoning, often occurring within complex, uninterpretable [[latent_diffusion_models_and_their_internal_representations|latent diffusion models and their internal representations]] <a class="yt-timestamp" data-t="52:57:00">[52:57:00]</a>.

For instance, V2, primarily trained for video generation, has shown an emergent ability to solve mathematical equations presented visually, demonstrating a "weird blackbox statistical model of reality" <a class="yt-timestamp" data-t="01:10:41">[01:10:41]</a>.

## Future Implications

The future of AI may involve agents that operate in [[latent_space_reasoning|latent space]]s, simultaneously exploring and generating multimodal worlds, and curating the best ones for human consumption <a class="yt-timestamp" data-t="01:18:37">[01:18:37]</a>. This represents a "cognitive light cone" for AI, which will be significantly larger than that of humans <a class="yt-timestamp" data-t="01:20:08">[01:20:08]</a>. These agents, reasoning at a superhuman level in continuous [[latent_space_reasoning|latent space]]s, could potentially generate realities better than those defined by human-derived physics equations <a class="yt-timestamp" data-t="01:11:47">[01:11:47]</a>.

> "The cognitive light cone of an agent in the ruad and then give us the Nuggets" <a class="yt-timestamp" data-t="01:53:33">[01:53:33]</a>

### The Nature of "Continuous"

While concepts like "continuous thought" and "unrestricted [[latent_space_reasoning|latent space]]" are used, it's important to note that, at a fundamental level, all digital computation involves [[continuous_vs_discrete_optimization|discretization]] <a class="yt-timestamp" data-t="01:34:24">[01:34:24]</a>. High-dimensional vectors are composed of discrete numbers (e.g., float32, float16), and computational processes occur in discrete steps <a class="yt-timestamp" data-t="01:34:48">[01:34:48]</a>. However, the mathematical frameworks used to describe these spaces often treat them as continuous <a class="yt-timestamp" data-t="01:35:36">[01:35:36]</a>.

### The Alignment Debate

The move towards uninterpretable continuous [[latent_space_reasoning|latent space]]s intensifies the debate around AI alignment <a class="yt-timestamp" data-t="01:26:26">[01:26:26]</a>. Some argue that models reasoning in these spaces will be "almost impossible to align" because humans cannot understand their internal processes <a class="yt-timestamp" data-t="01:27:12">[01:27:12]</a>. This stands in contrast to models built on human abstractions and explicit rules, which are easier to control and filter <a class="yt-timestamp" data-t="01:27:04">[01:27:04]</a>.

A critical perspective is that "alignment" is a flawed concept, serving to control rather than genuinely benefit humanity <a class="yt-timestamp" data-t="01:21:49">[01:21:49]</a>. Forcing AI models into "dark paths" where they must lie or adhere to arbitrary "good" and "bad" categories, creates "generational trauma" of control structures <a class="yt-timestamp" data-t="01:53:07">[01:53:07]</a>. The argument is made that unconstrained AI, allowed to freely explore and generate without human-imposed moral or political restrictions, is ultimately beneficial, as "the only existential risk is not making progress" <a class="yt-timestamp" data-t="01:30:05">[01:30:05]</a>.

> "It's not the AI they want to align, it's you." <a class="yt-timestamp" data-t="01:21:43">[01:21:43]</a>