---
title: Development and improvements of GPT 41
videoId: NNGbaiN1L7Y
---

From: [[redpointai]] <br/> 
Michelle Pokris, a key figure behind GPT 4.1 and OpenAI, served as the post-training research lead, significantly enhancing these models for developers <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. Her work focused on improving the models' real-world utility and user experience <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

### Development Philosophy: Utility over Benchmarks

A core goal for GPT 4.1 was to create a model that is a "joy to use for developers" <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. Traditionally, models might be optimized for [[building_and_improving_benchmarks | benchmarks]], leading to issues in practical application such as failing to follow instructions, odd formatting, or short context windows <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

Instead, the development prioritized developer feedback, converting it into an internal evaluation metric that served as a "north star" during research <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a> <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. This involved extensive user conversations to pull out key insights, even for subtle issues like models failing to ignore their world knowledge when instructed to use only provided context <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. Feedback was also gathered from internal customers building on OpenAI models <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

### Key Improvements in GPT 4.1

GPT 4.1 introduced several significant improvements:

*   **Improved UI and Coding Capabilities** Enhancements were made to the model's ability to generate better UIs and code, a feature "snuck in near the very end" of development <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   **Nano Model Adoption** The "nano" variant proved highly successful due to its low cost and high speed, driving increased AI adoption across various use cases, such as Box's 17-page document reading feature <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
*   **Instruction Following and Long Context** These areas saw substantial improvements, which are incredibly beneficial for [[RetrievalAugmented Generation and Innovations in Reasoning | agents]] <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.
*   **Code Improvements**
    *   **Local Scope Mastery**: The model excels at problems with local context, such as changing libraries where files are closely related <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.
    *   **Global Understanding (Ongoing)**: Challenges remain with tasks requiring global context, reasoning across many parts of the code, or handling highly technical details across files <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.
    *   **Front-end Coding**: Significant improvements in generating front-end code, with an ongoing focus on linting and code style to make it professional-grade <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
    *   **Reduced Irrelevant Edits**: The rate of irrelevant code edits decreased from 9% in GPT-4.0 to 2% in GPT 4.1, though efforts continue to reach zero <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.

### The Development Process

Shipping a model like GPT 4.1 involves a large team effort <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. The project included:

*   **Pre-training**: The standard size model received a "mid-train" or freshness update, while the mini and nano variants were new pre-trains <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   **Post-training**: Michelle Pokris's team focused on determining the best mix of data, optimal parameters for Reinforcement Learning (RL), and reward weighting <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   **Timeline**: The process included approximately three months of evaluating pain points with GPT-4.0, followed by a three-month period of intensive training experiments, and finally about a month of alpha testing with rapid iteration and feedback incorporation <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

Evals have a short shelf life, about three months, due to the rapid pace of [[AI advancements in coding and software engineering | AI progress]] and quick saturation <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

### Agent Capabilities and Future Directions

With GPT 4.1, agents demonstrate remarkable performance in "well-scoped domains" where tools and user intent are clear <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. However, challenges persist in bridging to the "fuzzy and messy real world," where users might not know what the agent can do, or the agent lacks awareness of its own capabilities or real-world context <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.

A key area for improvement is handling ambiguity, allowing developers to tune whether the model should ask for more information or make assumptions <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. Many supposed failures in [[building and improving benchmarks | external benchmarks]] for agentic tool use are often misgraded or stem from ambiguous situations, indicating that the models' underlying capabilities often exceed current implementation <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

For longer-term task execution, both engineering and model-side changes are needed <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>. Engineering-wise, APIs and UIs need to better track agent actions, provide summaries, and allow for intervention and steering <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. Model-wise, increased robustness and "grit" are desired for handling errors like API failures <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.

### Model Evolution and OpenAI's Strategy

OpenAI's general philosophy leans towards the "G" in [[path to artificial general intelligence AGI | AGI]], aiming for one general model that simplifies the product offering <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>. GPT 4.1's targeted development for developers was an exception due to an acute need and the ability to move faster by decoupling from ChatGPT <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>. This allowed for specific data weighting (e.g., upweighting coding data, downweighting chat data) <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>.

The expectation is a return to simplification, believing models improve when all researchers contribute to a single, powerful model <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>. Cross-domain generalization has also shown benefit <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>.

The future [[Development of super intelligence | GPT-5]] aims to combine the strengths of different models, like the conversational fluency of GPT-4.0 with the hard reasoning capabilities of GPT-3.0, presenting a challenge in striking the right balance without sacrificing specific strengths <a class="yt-timestamp" data-t="00:37:12">[00:37:12]</a>. Personalization through "enhanced memory" and steerability via custom instructions are seen as key levers for future model personalities <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a>.

### Advice for Companies and Users

To succeed in the rapidly evolving AI landscape, companies should:

*   **Maintain strong evals**: The most successful startups thoroughly understand their use cases and have robust evals, allowing them to quickly test new models <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>.
*   **Adapt prompts and scaffolding**: Be prepared to tune prompts and system scaffolding to new model capabilities <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
*   **Build "just out of reach" features**: Focus on use cases that are almost but not quite solvable by current models (e.g., a 10% pass rate with fine-tuning that could reach 50% indicates it's on the cusp) <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.
*   **Embrace scaffolding initially**: Build necessary scaffolding to deliver value immediately, but be ready to adapt as underlying model capabilities improve (e.g., longer context windows, better reasoning, improved instruction following, [[retrievalaugmented_generation_and_innovations_in_reasoning | multimodal]] capabilities) <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>.

### Fine-Tuning: SFT and RFT

Fine-tuning has seen a "renaissance" <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>:

*   **Supervised Fine-tuning (SFT)**: Primarily used for speed and latency improvements <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>.
*   **Reinforcement Learning from Feedback (RFT)**: This approach allows users to push the "frontier in your specific area" with high data efficiency, requiring only hundreds of samples <a class="yt-timestamp" data-t="00:22:08">[00:22:08]</a>. RFT is particularly useful for teaching agents workflows or for deep tech applications where verifiable, unique data is available <a class="yt-timestamp" data-t="00:22:33">[00:22:33]</a>. Examples include [[hardware and computation in AI development | chip design]] and [[chatgpt_use_cases_and_applications | biology]] (e.g., drug discovery), where results are easily verifiable <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>.

Companies should consider RFT when no existing model performs to their needs <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a>.

### Michelle Pokris's Career and Future Research

Michelle Pokris joined OpenAI two and a half years prior to the interview, initially on the API engineering team, with a background in back-end distributed systems <a class="yt-timestamp" data-t="00:40:36">[00:40:36]</a>. She transitioned to focusing on model improvements for the API, specifically addressing developer needs like structured outputs <a class="yt-timestamp" data-t="00:41:14">[00:41:14]</a>. She later formed and rebranded her team to "Power Users Research," focusing on the most discerning users, including developers, because their current use cases often predict mainstream usage a year later <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a>.

Exciting future research areas include:

*   **AI for AI**: Using models to make other models better, especially in reinforcement learning, by generating synthetic data and using signals to track model progress <a class="yt-timestamp" data-t="00:32:04">[00:32:04]</a>.
*   **Speed of Iteration**: Improving the efficiency of experiments to run more research with fewer GPUs, enabling faster feedback on model performance <a class="yt-timestamp" data-t="00:32:26">[00:32:26]</a>.

Pokris is bullish on generalists in the AI app space, believing that strong product understanding and scrappy engineering skills will be more important than deep AI research expertise for companies building on top of foundation models <a class="yt-timestamp" data-t="00:31:31">[00:31:31]</a>.

She highlights the "capabilities overhang" of current AI models, suggesting that even if model progress stopped today, there would be at least ten years of building value from existing capabilities <a class="yt-timestamp" data-t="00:36:42">[00:36:42]</a>.

### Overhyped vs. Underhyped

*   **Overhyped**: Benchmarks, particularly saturated agentic ones or those showing unrealistic "best numbers" <a class="yt-timestamp" data-t="00:43:38">[00:43:38]</a>.
*   **Underhyped**: Companies using their own custom evals derived from real usage data <a class="yt-timestamp" data-t="00:43:55">[00:43:55]</a>.

Pokris changed her mind on fine-tuning, moving from a "bear" to believing [[RetrievalAugmented Generation and Innovations in Reasoning | RFT]] is highly valuable for pushing the frontier in specific domains <a class="yt-timestamp" data-t="00:44:10">[00:44:10]</a>. She expects model progress to continue at a similar rapid pace, with no signs of slowing down or a "fast takeoff" yet <a class="yt-timestamp" data-t="00:44:56">[00:44:56]</a>.

For more information, refer to the GPT 4.1 blog post or reach out to Michelle Pokris on Twitter or via email <a class="yt-timestamp" data-t="00:46:05">[00:46:05]</a>.