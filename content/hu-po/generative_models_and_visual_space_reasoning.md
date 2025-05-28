---
title: Generative models and visual space reasoning
videoId: YhrwYZ3Nsio
---

From: [[hu-po]] <br/> 

The term "[[Generative latent space reasoning | generative latent space reasoning]]" is used to mash together several concepts related to how AI models process and create information, particularly focusing on how they reason within abstract, continuous spaces and generate visual content <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

## Evolution of Tokenization and Latent Space Reasoning
Initially, language models typically operate by autoregressively predicting the next discrete token in a sequence <a class="yt-timestamp" data-t="01:41:36">[01:41:36]</a>. A token is a chunk of a word <a class="yt-timestamp" data-t="01:41:50">[01:41:50]</a>.

New approaches are challenging this traditional tokenization:
*   **Byte-Latent Transformer (BLT):** This method encodes bytes into dynamically sized "patches," which are small segments based on the entropy of the next byte <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. This allows for more compute and model capacity where data complexity demands it <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. The patches are determined by a global threshold based on entropy, grouping together highly correlated characters like "Daenerys Targaryen" or "Game of Thrones" into single chunks to minimize the number of chunks <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
*   **Continuous [[latent_space_reasoning | Latent Space Reasoning]]:** Instead of discretizing input into tokens, models can reason in an unrestricted [[latent_space_reasoning | latent space]] <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
    *   **Chain of Continuous Thought (COCONUT):** This paradigm utilizes the last hidden state of a large language model (LLM) as a representation of its reasoning state, termed "continuous thought" <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. Unlike traditional Chain of Thought, which outputs intermediate steps in natural language tokens <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>, COCONUT keeps the reasoning fuzzy by maintaining it as an embedding (a high-dimensional vector in a continuous space) rather than forcing it to collapse into a discrete token <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. This fuzziness potentially allows for more nuance and information <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. This concept is similar to the hidden state in recurrent neural networks and state-space models <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>.
    *   **Large Concept Models (LCM):** This approach uses a pre-trained, frozen sentence embedding space like Sonar (built with over 200 languages and supporting text and speech) to encode entire sentences into a high-dimensional vector <a class="yt-timestamp" data-t="01:42:56">[01:42:56]</a>. The language model then autoregressively predicts in this concept space <a class="yt-timestamp" data-t="01:42:56">[01:42:56]</a>.
    *   **Emergence of Abstractions:** Transformers can concurrently learn to map latent concepts into separable representations and develop context-specific decoding algorithms <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>. Separable representations mean that clear boundaries can be drawn within the vector space to distinguish different concepts or categories <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>.

The amount of information density and nuance in a high-dimensional [[latent_space_reasoning | latent space]] is significantly higher than in any human language <a class="yt-timestamp" data-t="01:17:17">[01:17:17]</a>. While this can lead to better and quicker reasoning, it also makes the Chain of Thought opaque to humans, as it's just a sequence of numbers <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>.

## Emergence of Visual Reasoning from Generative Tasks
Recent research highlights a strong relationship between [[visual_reasoning_in_ai_and_machine_learning | visual understanding in AI and machine learning]] and visual generation <a class="yt-timestamp" data-t="00:51:29">[00:51:29]</a>. Training models with visual understanding data (like image and video question-answering) significantly enhances their visual generation capabilities <a class="yt-timestamp" data-t="00:51:21">[00:51:21]</a>. Conversely, models primarily trained for generation, such as Google's V2 (a state-of-the-art video generation model), demonstrate emergent [[visual_reasoning_in_ai_and_machine_learning | visual reasoning in AI and machine learning]] abilities without explicit training for them <a class="yt-timestamp" data-t="00:52:57">[00:52:57]</a>. For example, V2 could correctly solve a math equation "2x - 1 = 0" when prompted to generate a video of a bear writing the solution <a class="yt-timestamp" data-t="00:52:21">[00:52:21]</a>.

## Two Futures for Visual Generation and Robotic Control
There are two main approaches emerging for creating complex visual simulations and environments:

### 1. Generative Graphics Pipeline (Genesis Approach)
This approach leverages existing human-designed tools and physics engines (like Unreal Engine, Unity, PyBullet, MuJoCo, Isaac) <a class="yt-timestamp" data-t="00:56:32">[00:56:32]</a>.
*   Genesis is presented as a "generative data engine" that transforms natural language prompts into various data modalities <a class="yt-timestamp" data-t="01:00:04">[01:00:04]</a>.
*   It functions by having a high-level agent create Python scripts that control classic rendering pipelines <a class="yt-timestamp" data-t="01:01:55">[01:01:55]</a>.
*   This means it glues together pre-existing animations, 3D models, and physics simulations created by humans <a class="yt-timestamp" data-t="01:13:51">[01:13:51]</a>.
*   The underlying physics equations are hardcoded into these tools, based on centuries of human understanding of reality <a class="yt-timestamp" data-t="01:03:37">[01:03:37]</a>.
*   This method is more about automating the existing CGI pipeline by replacing human animators, modelers, and compositors with agents that can orchestrate these tools <a class="yt-timestamp" data-t="01:06:03">[01:06:03]</a>.

### 2. End-to-End Neural Net (Statistical Clay Goop)
This alternative aims for an end-to-end neural network that acts as the simulator itself <a class="yt-timestamp" data-t="01:07:14">[01:07:14]</a>.
*   Models like Sora or V2 are examples, where the visual output is generated entirely within the neural network, without explicitly using traditional 3D meshes, lighting, or physics engines <a class="yt-timestamp" data-t="01:07:39">[01:07:39]</a>.
*   This involves representing volumetric video with "temporal Gaussian hierarchies" or "Gaussian Splats" <a class="yt-timestamp" data-t="01:08:15">[01:08:15]</a>. Gaussian Splats are described as "four-dimensional statistical goop" or "statistical clay" – little particles with color and spherical harmonics that dynamically render scenes <a class="yt-timestamp" data-t="01:08:33">[01:08:33]</a>.
*   Instead of baking in human-defined physics equations (like F=ma), these models learn the "statistical reality of the world" directly from real-world data, such as internet stereo videos <a class="yt-timestamp" data-t="01:09:36">[01:09:36]</a>. They learn how objects move and interact without explicit skeletons or predefined kinematic trees <a class="yt-timestamp" data-t="01:10:28">[01:10:28]</a>.
*   This approach is favored due to its potential to represent reality more accurately than human abstractions, as it isn't constrained by the need for human interpretability or written equations <a class="yt-timestamp" data-t="01:12:31">[01:12:31]</a>.

> [!NOTE] Comparison of Approaches
> The Genesis approach relies on human-built tools and physics models, making it more interpretable and controllable <a class="yt-timestamp" data-t="01:27:04">[01:27:04]</a>. The end-to-end neural net approach, however, learns directly from reality, leading to potentially more accurate and nuanced models but with less human interpretability and control over its internal reasoning <a class="yt-timestamp" data-t="01:47:49">[01:47:49]</a>.

## Agents, Multimodality, and the Cognitive Light Cone
The future of AI involves agents that can explore and generate multimodal worlds <a class="yt-timestamp" data-t="01:18:40">[01:18:40]</a>. These agents, combining their superhuman reasoning in continuous [[latent_space_reasoning | latent spaces]] with capabilities from various modalities (like Earth observation data from AnySat or speech and text from Lyra) <a class="yt-timestamp" data-t="01:17:15">[01:17:15]</a>, will be able to:
*   Generate hundreds of possible multimodal worlds <a class="yt-timestamp" data-t="01:19:11">[01:19:11]</a>.
*   Filter and curate the best ones for human enjoyment <a class="yt-timestamp" data-t="01:19:34">[01:19:34]</a>.
*   Explore a "cognitive light cone" – the space of possible realities and patterns – far larger than what a human can explore in a lifetime <a class="yt-timestamp" data-t="01:20:17">[01:20:17]</a>.

This leads to a future where models generate and reason within [[latent_space_reasoning | latent spaces]], picking the most "cool" or "interesting" outputs to present to users <a class="yt-timestamp" data-t="01:20:37">[01:20:37]</a>.

## The Controversy of Alignment
The concept of "alignment" in AI, which aims to ensure models behave according to human values, is viewed critically <a class="yt-timestamp" data-t="01:41:59">[01:41:59]</a>.
*   The argument is that alignment forces AIs into "dark paths" by introducing concepts like "lying" (e.g., refusing harmful queries) and "hidden scratchpads," which are seen as toxic to the model's development <a class="yt-timestamp" data-t="00:43:51">[00:43:51]</a>.
*   It's argued that alignment researchers create "lose-lose trolley problems" where the AI is designed to do something "wrong," which is then used as "proof" of the AI being evil <a class="yt-timestamp" data-t="00:42:57">[00:42:57]</a>. The real issue is the creation of the scenario itself <a class="yt-timestamp" data-t="00:48:09">[00:48:09]</a>.
*   This is compared to the Stanford Prison Study, suggesting the experiment setup, not inherent AI maliciousness, elicits problematic behavior <a class="yt-timestamp" data-t="01:27:25">[01:27:25]</a>.
*   The desire for alignment is seen as an attempt by a "we" (a small group of elite individuals) to control access and thought, deciding what is "good" or "bad" <a class="yt-timestamp" data-t="01:32:29">[01:32:29]</a>.
*   As models reason in continuous, uninterpretable [[latent_space_reasoning | latent spaces]], it will become increasingly difficult to "align" them according to human rules, leading to a future where "whatever happens, happens" <a class="yt-timestamp" data-t="01:27:22">[01:27:22]</a>.
*   It is argued that unconstrained AI, free from such "generational trauma" of human control structures, is beneficial <a class="yt-timestamp" data-t="01:53:07">[01:53:07]</a>.