---
title: Evaluation methodologies and user feedback for AI models
videoId: NNGbaiN1L7Y
---

From: [[redpointai]] <br/> 

The development of AI models, particularly at OpenAI, has shifted focus from traditional benchmarks to real-world utility and user satisfaction, emphasizing continuous [[customer_feedback_and_ai_model_refinement | customer feedback and AI model refinement]] to drive improvements <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. Michelle Pokris, a post-training research lead at OpenAI, highlights that the goal is to create models that are a "joy to use for developers" <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## Shifting Focus from Benchmarks to Utility

Historically, AI models were often optimized for benchmarks, which, while looking "really great," could lead to models stumbling over basic real-world issues like instruction following or formatting <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. For GPT-4.1, the focus was explicitly on what developers had been requesting, turning that [[customer_feedback_and_ai_model_refinement | feedback]] into actionable evaluations that could be used during research <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. OpenAI developed an internal instruction following eval based on real API usage and user input, serving as a "north star" during development <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### The Feedback Gathering Process
Gathering [[customer_feedback_and_ai_model_refinement | customer feedback]] is often about understanding subtle issues rather than explicit requests for specific evaluations <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. Users might describe an issue as "kind of weird in this one use case," requiring OpenAI to actively pull out key insights by generating prompts and investigating <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. For example, a recent insight revealed that models could improve in situations where they need to "ignore everything you know about the world and only use the information in context" <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. This type of nuanced feedback would not typically be captured by standard benchmarks <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

The determination of what evaluations matter most comes from:
*   Repeated themes in [[customer_feedback_and_ai_model_refinement | customer feedback]] <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   Internal usage of the models <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   Insights from internal customers building on OpenAI's models <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

OpenAI actively seeks more [[customer_feedback_and_ai_model_refinement | feedback]], particularly for long-context real-world evaluations and instruction following <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. The company offers an "eval product" where users can opt-in to receive free inference on their evaluations in exchange for their data <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

## The Model Development and Evaluation Cycle

The process of shipping a model like GPT-4.1 involves significant effort from large teams <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. This includes:
*   **Pre-training:** Developing new "mid-trains" or fresh pre-trains for different model sizes (standard, mini, nano) <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   **Post-training:** Michelle's team focuses on post-training, which involves determining the best mix of data, parameters for reinforcement learning (RL) training, and weighting of different rewards <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   **Iterative Evaluation:** A lead-up of three months was spent on developing and refining evaluations to understand the biggest model problems <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. This was followed by a three-month period of intensive training, running numerous experiments to tweak datasets and parameters <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
*   **Alpha Testing:** A final month of alpha testing involved rapid training cycles, gathering [[customer_feedback_and_ai_model_refinement | feedback]], and incorporating it as much as possible <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

A significant challenge is the rapid saturation of [[ai_model_evaluation_and_benchmarking | benchmarks]]; the "shelf life of an eval is like three months" due to fast progress <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. This necessitates a continuous hunt for new and relevant evaluations <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

### Unexpected Discoveries and User Adoption
Upon release, GPT-4.1 showed unexpected capabilities, particularly in improved UI and coding <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. The "nano" model, being small, cheap, and fast, spurred significant AI adoption, demonstrating a demand for models across various cost-latency curves <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

## Evaluating AI System and Managing Human-AI Collaboration [[evaluating_ai_systems_and_managing_humanai_collaboration | Evaluating AI Systems and Managing HumanAI Collaboration]]

### Current State of Agents
Agents work "remarkably well" in well-scoped domains where the model has the right tools and clear user intent <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. The challenge now lies in bridging the gap to the "fuzzy and messy real world," where user requests are ambiguous, or the agent lacks awareness of its own capabilities <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. Michelle believes many capabilities are already present, but the difficulty is getting sufficient context into the model <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. Future improvements include enabling developers to tune for ambiguity (e.g., asking for more information vs. proceeding with assumptions) <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

In [[ai_model_evaluation_and_benchmarking | AI model evaluation and benchmarking]] of agentic tool use, many "incorrect" grades are found to be misgraded, ambiguous, or due to user models not following instructions <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. This suggests that existing benchmarks for function calling and agentic tool use are becoming saturated <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

### Long-Term Task Execution
To make progress on longer, multi-step, and ambiguous tasks, both engineering and model-side changes are needed <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Engineering:** Develop APIs and UIs that allow users to follow an agent's actions, see summaries, and "jump in and change the trajectory" <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.
*   **Modeling:** Enhance robustness and "grit" so models don't get stuck when external systems (like APIs) fail <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.

## Model Evaluation in Code Generation
GPT-4.1 and other models excel at locally scoped coding problems, where files are close together <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. However, challenges remain in tasks requiring "global context" or reasoning about many disparate parts of the code <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>. While front-end coding has seen significant improvement, the goal is for models to produce code that a front-end engineer would be "proud of," focusing on linting and code style <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. Another ongoing focus is reducing "irrelevant edits," where the model changes more than requested, down from 9% in GPT-4.0 to 2% in GPT-4.1 <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>.

While [[ai_model_evaluation_and_benchmarking | benchmarks]] like SWEBench remain useful for differentiating significant performance gaps (e.g., 55% vs. 35% pass rates), many others are "fully saturated and not useful" <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. The strategy is to "use the most out of an eval during its lifespan and then move on and create another one" <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.

## Best Practices for Businesses in a Rapidly Evolving AI Landscape [[ai_model_selection_and_evaluation_for_businesses | AI model selection and evaluation for businesses]]

Companies using AI APIs need strategies to stay current with rapid model progress:
1.  **Develop Strong Evals:** The most successful startups have deep knowledge of their use case and "really good evals" that allow them to quickly test new models when they drop <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>.
2.  **Adapt Prompts and Scaffoldings:** Be able to switch and tune prompts and scaffoldings to specific models <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.
3.  **Build for "Just Out of Reach" Capabilities:** Focus development on problems that current models struggle with (e.g., works 1/10 times, but ideally 9/10). These are likely to be "crushed" by future models <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>. A heuristic for "just out of reach" is if fine-tuning can improve a 10% pass rate to 50% <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.

Building scaffolding for current model limitations is "super worth it" for startups to deliver immediate value and achieve a few months of "arbitrage" <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>. However, it's crucial to be prepared to adapt, keeping future trends in mind, such as improving context windows, reasoning capabilities, and instruction following <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>. Multimodal capabilities are also rapidly improving, making it worthwhile to connect models to as much task information as possible, even if results are "meh" today <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>.

## The Role of Fine-Tuning: SFT vs. RFT

Fine-tuning has seen a "renaissance" <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a> and is generally categorized into two camps:
1.  **Fine-tuning for Speed and Latency (SFT):** This is the "workhorse" for making models like GPT-4.1 faster at a fraction of the latency <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>. This is suitable for simpler classification tasks where a model might be 10% wrong, and SFT can close that gap <a class="yt-timestamp" data-t="00:24:13">[00:24:13]</a>.
2.  **Fine-tuning for Frontier Capabilities (RFT):** Reinforced Fine-Tuning (RFT), based on the same RL process OpenAI uses internally, allows pushing the frontier in specific areas <a class="yt-timestamp" data-t="00:22:08">[00:22:08]</a>. RFT is "extremely data efficient," often requiring only hundreds of samples <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>. It is less fragile than SFT <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>. RFT is particularly useful for:
    *   Teaching an agent to pick workflows or reason through decision processes <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>.
    *   Deep tech applications where an organization has unique, verifiable data, such as chip design or drug discovery <a class="yt-timestamp" data-t="00:22:48">[00:22:48]</a>. RFT is recommended when "no model in the market does what you need" <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a>.

## Model Selection for Businesses [[ai_model_selection_and_evaluation_for_businesses | AI model selection and evaluation for businesses]]

For developers, the recommendation is to "start with 4.1" and see if it works well <a class="yt-timestamp" data-t="00:27:33">[00:27:33]</a>. If speed is a priority, then explore Mini and Nano, and fine-tuning them <a class="yt-timestamp" data-t="00:27:39">[00:27:39]</a>. If 4.1 struggles with certain tasks, move to O4 Mini for its reasoning capabilities, then O3, and finally RFT with O4 Mini if needed <a class="yt-timestamp" data-t="00:27:48">[00:27:48]</a>.

## Future of AI Models and Research

### Combining Model Capabilities
OpenAI aims to simplify its product offering, moving towards "one model that's general" to lean into the "G in AGI" <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>. While GPT-4.1 temporarily decoupled from ChatGPT to move faster and optimize for developers (e.g., removing chat-specific data, upweighting coding data), the general philosophy is that models improve when "creative energies of all researchers at OpenAI are working on them" <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.

The challenge for future models like GPT-5 is combining diverse capabilities: being a "delightful chitchat partner" while also knowing "when to reason" without unnecessary delays <a class="yt-timestamp" data-t="00:37:57">[00:37:57]</a>. This involves striking the right balance in training data, as some decisions (e.g., upweighting coding data) can be zero-sum <a class="yt-timestamp" data-t="00:38:21">[00:38:21]</a>.

### Research Directions
Key research areas include:
*   **Models Improving Models:** Using existing models to generate signals and synthetic data for improving future models, a "remarkably powerful trend" <a class="yt-timestamp" data-t="00:32:04">[00:32:04]</a>.
*   **Speed of Iteration:** Accelerating the research cycle by running more experiments with fewer GPUs, allowing researchers to quickly determine if an approach is working <a class="yt-timestamp" data-t="00:32:26">[00:32:26]</a>. This requires ensuring sufficient scale for signals during training <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>.
*   **Generalization of Tool Use:** While products like Deep Research focused on deep training on specific tools, the trend with O3 models shows that learning one set of tools improves the model's ability to use other tools more broadly <a class="yt-timestamp" data-t="00:34:04">[00:34:04]</a>. This suggests less need for "one tool specific training" going forward <a class="yt-timestamp" data-t="00:34:27">[00:34:27]</a>.

Future capabilities expected sooner rather than later include coding agents, given current benchmark performance, and long workflows like customer support, where models can build on previous tool calls and outputs <a class="yt-timestamp" data-t="00:35:07">[00:35:07]</a>.

## Industry Perspectives on AI Development

*   **Overhyped:** Benchmarks, especially agentic ones that are saturated, or claims based on "absolute best numbers" rather than realistic performance <a class="yt-timestamp" data-t="00:43:38">[00:43:38]</a>.
*   **Underhyped:** Internal evaluations using real usage data to understand what works well <a class="yt-timestamp" data-t="00:43:55">[00:43:55]</a>.
*   **Model Progress:** Expected to continue at a fast pace, similar to the last year, without necessarily being a "fast takeoff" <a class="yt-timestamp" data-t="00:44:56">[00:44:56]</a>.

Michelle Pokris leads the "power users research team" at OpenAI, focusing on users who push the models' limits (e.g., developers, discerning Chat GPT users). This focus is strategic because "the things that the power users are doing today are going to be the things that the median users are doing a year from now," providing valuable insights for future model improvements <a class="yt-timestamp" data-t="00:41:42">[00:41:42]</a>.