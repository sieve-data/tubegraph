---
title: Improving GPT 41 for developers
videoId: NNGbaiN1L7Y
---

From: [[redpointai]] <br/> 

Michelle Pokris, as OpenAI's Post-Training Research Lead, played a pivotal role in refining GPT-4.1, making it significantly more effective for developers <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The focus for this model shifted from optimizing solely for benchmarks to prioritizing real-world usage and utility <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Development Philosophy and Process

The primary goal for GPT-4.1 was to create a model that is a "joy to use for developers" <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. This involved addressing common developer pain points, such as models not following instructions, strange formatting, or limited context windows <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

To achieve this, the development process included:
*   **User Feedback Integration**: Extensive conversations with users to identify issues and transform their feedback into actionable evaluations (evals) <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. An internal instruction following eval, based on real API usage, served as a "north star" during development <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Identifying Key Problems**: Rather than users providing specific evals, developers often describe general "weirdness" in use cases, which then requires deeper investigation to uncover the underlying issues <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. For example, one insight revealed that models needed to improve at ignoring pre-existing world knowledge and exclusively using in-context information <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. Recurring themes from customer feedback and internal model usage guide which evals to prioritize <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Rapid Iteration**: The process involved about three months of eval development, followed by three months of intense training and experimentation, and finally a month of alpha testing to rapidly incorporate feedback <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   **Eval Shelf Life**: The rapid progress in AI means that the shelf life of an eval is often only about three months, as models quickly saturate existing benchmarks <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

### Shipping the Model
Shipping GPT-4.1 involved a large team and three models: standard, mini, and nano <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. The larger model received a "mid-train" or freshness update, while the mini and nano versions were entirely new pre-trains <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. Michelle Pokris's team focused heavily on post-training, determining the optimal mix of data, RL training parameters, and reward weightings <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.

A key decision for GPT-4.1 was to decouple its development from [[ChatGPT and its applications in coding | ChatGPT]] <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>. This allowed for faster training and feedback cycles, and enabled specific model training choices, such as removing [[ChatGPT and its applications in coding | ChatGPT]] specific datasets and significantly increasing the weighting of coding data <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>.

## Key Improvements and Capabilities

### Agents and Tool Use
GPT-4.1 brought significant improvements to [[openai_agent_development_tools | agent development tools]] through enhanced instruction following and long context capabilities <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

*   **Current State**: Agents excel in "well-scoped domains" where all necessary tools are provided and user intent is clear <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Challenges**: The main challenge is bridging the gap to "fuzzy and messy real-world" scenarios <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. This includes the agent's awareness of its own capabilities, connection to real-world information, and handling ambiguity (e.g., knowing when to ask for more information versus making assumptions) <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Future Progress**: Progress requires both engineering and model changes <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>. On the engineering side, better APIs and UIs are needed for monitoring, summarizing, and steering agent actions <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. On the modeling side, improved robustness and "grit" are needed to handle errors (e.g., API 500s) <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>. Most current agent benchmarks are nearing saturation or have ambiguous failure cases <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.

### Code Capabilities
GPT-4.1 demonstrated "remarkably good" performance in coding, especially for locally scoped problems where files are closely related <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.

*   **Areas for Improvement**:
    *   **Global Understanding**: The model still needs improvement in understanding global context and reasoning across many disparate parts of a codebase <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.
    *   **Front-End Coding**: While improved, the goal is to produce front-end code that a human engineer would be proud of, focusing on linting and code style <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.
    *   **Irrelevant Edits**: Reducing changes beyond what was requested (from 9% in 4.0 to 2% in 4.1, but aiming for zero) <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   **Benchmarks**: While some code benchmarks like SWEBench are still useful, many are becoming saturated, necessitating the creation of new ones <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.
*   **Personal Use**: Michelle uses Codeex (main model: 04 Mini for speed) and still dabbles with GitHub Copilot, Windsurf, and Cursor for her personal coding <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.

## Model Strategy and Evolution

### Generalization vs. Specialization
OpenAI's general philosophy leans into the "G" in AGI, aiming for one general model <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>. The long-term goal is to simplify the product offering, having one model for both [[ChatGPT and its applications in coding | ChatGPT]] and API use cases <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>. However, GPT-4.1's separate development was due to a "particularly acute need" for developers, allowing faster progress by decoupling from [[ChatGPT and its applications in coding | ChatGPT]] <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>. While a targeted approach was successful, the belief is that combining the "creative energies of all researchers" on one model yields better overall results <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.

### Future of Model Families (GPT-5)
The challenge for future models like GPT-5 will be combining diverse capabilities <a class="yt-timestamp" data-t="00:37:27">[00:37:27]</a>. For example, balancing the conversational delight of the 4.0 series with the strong reasoning abilities of 03, ensuring the model knows when to engage in casual chat versus deep thought <a class="yt-timestamp" data-t="00:38:03">[00:38:03]</a>. Decisions about upweighting or downweighting specific data types (like chat vs. coding) create "zero-sum decisions" that must be carefully balanced <a class="yt-timestamp" data-t="00:38:21">[00:38:21]</a>.

## Advice for Developers and Companies

### Navigating Rapid Progress
Companies must have strong evals tailored to their specific use cases to quickly assess new models <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>. They should also be able to adapt their prompts and scaffolding to new models <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.

### Building for the Future
*   **"Just Out of Reach"**: Focus on use cases that are "maybe just out of reach of the current models," or that work only occasionally but have high potential <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>. If a problem can be fine-tuned from 10% to 50% pass rate, it's likely "on the cusp" and a future model will "crush it" <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.
*   **Scaffolding**: Building scaffolding (e.g., RAG, repeating instructions) is worthwhile for immediate value and short-term arbitrage <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>. However, companies must be prepared to change their approach as model capabilities (context windows, reasoning, instruction following) continuously improve <a class="yt-timestamp" data-t="00:20:16">[00:20:16]</a>.
*   **Multimodal Capabilities**: Acknowledge the significant improvements in multimodal understanding, especially with new pre-trains <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>. Connecting models to diverse information sources (even if results are currently mediocre) is a good strategy as capabilities will improve <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.

### [[Finetuning approaches and considerations in AI | Finetuning Approaches and Considerations in AI]]

Fine-tuning has seen a "renaissance" in usefulness <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>. It can be categorized into two camps:
1.  **Fine-tuning for Speed and Latency (SFT)**: This remains the workhorse, allowing models like 4.1 to be run at a fraction of the latency <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>.
2.  **Fine-tuning for Frontier Capabilities (RFT)**: This approach allows pushing the frontier in specific domains, even with small datasets (e.g., hundreds of samples) <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>. [[Finetuning AI models for enterprise data | RFT]] is expected to be generally available soon and is particularly useful for:
    *   Teaching agents complex workflows <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>.
    *   Deep tech applications where organizations have unique, verifiable data (e.g., chip design, biology, drug discovery) <a class="yt-timestamp" data-t="00:22:48">[00:22:48]</a>.
    *   RFT is based on the same reinforcement learning process OpenAI uses internally, making it robust and effective <a class="yt-timestamp" data-t="00:23:32">[00:23:32]</a>.

*   **When to Use Which Fine-tuning**:
    *   **Preference Fine-tuning**: For stylistic adjustments <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>.
    *   **SFT**: For simple tasks like classification where the model gets a small percentage of cases wrong <a class="yt-timestamp" data-t="00:24:13">[00:24:13]</a>.
    *   **RFT**: For problems where no current model in the market meets the specific needs <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a>.

### Choosing the Right Model and Prompting
For general [[ChatGPT and its applications in coding | ChatGPT]] use, 4.0 is recommended, with 4.5 for creative tasks and 03 for the hardest math or critical problems like tax filing <a class="yt-timestamp" data-t="00:26:36">[00:26:36]</a>.

For enterprise users:
*   Start with 4.1 to see if it meets the use case <a class="yt-timestamp" data-t="00:27:35">[00:27:35]</a>.
*   If faster speeds are needed, look into mini and nano, and fine-tuning them <a class="yt-timestamp" data-t="00:27:39">[00:27:39]</a>.
*   If 4.1's capabilities are insufficient, try O4 Mini for reasoning, then O3, and finally [[Finetuning AI models for enterprise data | RFT]] with O4 Mini <a class="yt-timestamp" data-t="00:27:48">[00:27:48]</a>.

Effective prompting techniques for 4.1 include:
*   **Structuring prompts with XML**: This helps organize instructions effectively <a class="yt-timestamp" data-t="00:28:23">[00:28:23]</a>.
*   **"Keep Going"**: Explicitly telling the model to continue until the problem is solved can significantly improve performance <a class="yt-timestamp" data-t="00:28:30">[00:28:30]</a>.

## OpenAI's Internal Focus and Future Research

### Power Users and Evals
OpenAI's "power users research team" focuses on understanding and improving models for discerning users, including developers, who often use advanced features and know the models' capabilities best <a class="yt-timestamp" data-t="00:41:44">[00:41:44]</a>. Insights from power users predict what median users will be doing in the future <a class="yt-timestamp" data-t="00:42:27">[00:42:27]</a>.

Sophisticated companies excel at creating modular systems with granular evals, breaking down problems into subcomponents to understand precisely what is working or failing <a class="yt-timestamp" data-t="00:30:16">[00:30:16]</a>. This modularity allows for faster development in the long run <a class="yt-timestamp" data-t="00:30:47">[00:30:47]</a>.

### Future Research Areas
*   **Models Improving Models**: Using AI models to make other models better, particularly in reinforcement learning, by generating signals to determine if a model is on the right track <a class="yt-timestamp" data-t="00:32:04">[00:32:04]</a>. This includes leveraging synthetic data, which is an "incredibly powerful trend" <a class="yt-timestamp" data-t="00:33:18">[00:33:18]</a>.
*   **Speed of Iteration**: Improving the speed of experimentation, reducing GPU usage per experiment, and ensuring sufficient scale to derive clear signals <a class="yt-timestamp" data-t="00:32:26">[00:32:26]</a>.
*   **Generalization in Agents**: The trend suggests that learning to use one set of tools improves the model's ability to use other tools, leading to broadly capable agents rather than highly specialized, single-tool trained ones <a class="yt-timestamp" data-t="00:34:14">[00:34:14]</a>. Coding agents are expected soon due to current performance levels <a class="yt-timestamp" data-t="00:35:22">[00:35:22]</a>.
*   **Personality and Steerability**: Enhancing model personality through "enhanced memory" (making it more useful as it learns about the user) and increased steerability via custom instructions <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a>.

## Personal Journey at OpenAI
Michelle Pokris joined OpenAI two and a half years ago on the API engineering team, with a background in back-end distributed systems <a class="yt-timestamp" data-t="00:40:36">[00:40:36]</a>. After about 1.5 years, she shifted to focusing on models specifically for the API, identifying a need to improve models for developers (e.g., structured outputs) <a class="yt-timestamp" data-t="00:41:14">[00:41:14]</a>. She then formed and now leads the Power Users Research team, which focuses on developers and other discerning users across OpenAI's products <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a>. The pace of shipping remains consistently fast despite the company's growth <a class="yt-timestamp" data-t="00:42:51">[00:42:51]</a>.

## Quick Fire Round

*   **Overhyped**: Benchmarks, especially saturated agentic ones or those showing unrealistic best numbers <a class="yt-timestamp" data-t="00:43:38">[00:43:38]</a>.
*   **Underhyped**: Companies' own evals derived from real usage data <a class="yt-timestamp" data-t="00:43:55">[00:43:55]</a>.
*   **Mind Change**: Michelle was initially a "fine-tuning bear" but was convinced by [[Finetuning AI models for enterprise data | RFT]]'s ability to push the frontier in specific domains <a class="yt-timestamp" data-t="00:44:10">[00:44:10]</a>. The shift occurred because [[Finetuning AI models for enterprise data | RFT]] offers a similar algorithm to OpenAI's internal reinforcement learning process, making it a "big shift" in eliciting capabilities <a class="yt-timestamp" data-t="00:44:47">[00:44:47]</a>.
*   **Model Progress**: Expect model progress to be about the same this year, with continued speed and many new models <a class="yt-timestamp" data-t="00:45:01">[00:45:01]</a>. There is still "tens of trillions of dollars of value" to be extracted from current models, representing at least 10 years of building <a class="yt-timestamp" data-t="00:36:31">[00:36:31]</a>.
*   **Exciting Consumer Products (outside OpenAI)**: Products that take AI out of the digital world, such as Levels and Whoop (for health insights) <a class="yt-timestamp" data-t="00:45:46">[00:45:46]</a>.

For more information, readers can refer to the GPT-4.1 blog post or reach out to Michelle Pokris on Twitter for feedback <a class="yt-timestamp" data-t="00:46:05">[00:46:05]</a>.