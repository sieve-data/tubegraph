---
title: Generative models and the future of AI
videoId: Vz5n5SamDAc
---

From: [[causalpython]] <br/> 

The integration of generative models, particularly large language models (LLMs), with causal reasoning is a significant area of focus in the advancement of artificial intelligence <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>. While the capacity for LLMs to reason causally is still developing, their embedded knowledge can augment the causal analysis process <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

## Large Language Models and Causal Analysis

LLMs are viewed as a "common-sense database about how the world works" <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. This capability can provide technological support for setting up causal assumptions <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. Specifically, LLMs can:
*   Suggest plausible causal mechanisms when given an open question and a dataset <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   Critique existing assumptions, highlighting potential errors or missing information <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. This alleviates the burden on domain experts, who no longer have to start from scratch <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

### Practical Applications
In industry, LLMs have proven useful in constructing knowledge graphs with domain experts. They not only accelerate the process but also motivate experts to share their knowledge by providing an initial draft for critique <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

## Generative Models and World Modeling

Current [[advancements_in_causal_modeling_and_AI | advancements in causal modeling and AI]] indicate a trend towards generative models, such as GPT and Sora, attempting to model the world <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>. [[causality_in_ai | Causality]] is considered a necessary element for constructing a sound world model <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>.

While it is plausible that these models could learn world or causal world models, current LLMs primarily model language, not the world itself <a class="yt-timestamp" data-t="00:22:49">[00:22:49]</a>. Moving Foundation models to operate over direct observations of the world, rather than just language, will provide clearer insights into what these models are actually capturing <a class="yt-timestamp" data-t="00:23:20">[00:23:20]</a>.

### Limitations in Physical Simulation
Models like Sora, while impressive, are described as approximate or local physics simulators rather than true physics simulators <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>. They may learn shortcuts to produce plausible-looking outputs rather than a fundamentally correct function of how the world works <a class="yt-timestamp" data-t="00:24:51">[00:24:51]</a>.

For creative tasks, such as generating a video of pirate ships battling in a coffee cup, violating physics can be acceptable and even necessary to achieve the desired creative outcome <a class="yt-timestamp" data-t="00:25:51">[00:25:51]</a>. However, for applications requiring accurate physical modeling, ensuring the right controls to achieve precise behavior will be critical <a class="yt-timestamp" data-t="00:26:43">[00:26:43]</a>.

### Learning World Models
The debate exists whether models should learn directly from raw data like pixels or focus on latent representations. While pixels are the immediate view of the world, learning a latent representation of the world and then modeling physics over that representation makes more sense <a class="yt-timestamp" data-t="00:43:20">[00:43:20]</a>.

## The Future of the Generative Revolution

The current state of [[the_future_of_ai_integrating_generative_ai_and_causal_ai | the future of AI integrating generative AI and causal AI]] is compared to the early commercial internet in the mid-1990s <a class="yt-timestamp" data-t="00:28:01">[00:28:01]</a>. While the potential is evident, significant infrastructure and engineering work are still required to fully realize it <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>. The pace of change is expected to be faster than with the internet revolution <a class="yt-timestamp" data-t="00:29:05">[00:29:05]</a>.

Analogous to the emergence of applications like Uber and Lyft that were only possible with the combination of smartphones and the internet, future complementary technologies will likely make AI even more impactful than currently imagined <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>.

## Direction for Causal AI Development

Future efforts in [[causal_ai_and_machine_learning_intersection | causal AI and machine learning intersection]] include:
*   **Integrating LLMs for practical causal analysis:** This involves using LLMs to suggest causal graphs, identify potential missing data and confounders, and critique analysis processes <a class="yt-timestamp" data-t="00:40:35">[00:40:35]</a>.
*   **Modeling complex physical systems:** Exploring how Foundation models can help model more complex physics-style systems, which could open up a broad set of exciting applications <a class="yt-timestamp" data-t="00:41:07">[00:41:07]</a>.

The field of causal Python community is seen as healthy, with various libraries (e.g., PyWhy, CausalPy) contributing to the ecosystem <a class="yt-timestamp" data-t="00:35:35">[00:35:35]</a>. A key message for advancing the community is to remain focused on the end goal: solving real-world problems with causal methods, whether through algorithmic improvements, software engineering, or better documentation <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>.

A significant challenge in applied causal inference is making concepts like partial identification, sensitivity analysis, and proximal learning more accessible and easier to implement for practitioners <a class="yt-timestamp" data-t="00:37:45">[00:37:45]</a>. While some methods exist (like the one by Carlos Cinelli used in DoWhy), broader accessibility and tool development are needed <a class="yt-timestamp" data-t="00:39:15">[00:39:15]</a>.