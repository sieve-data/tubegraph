---
title: Advancements and implications of AI models like o1
videoId: ZEi4OTuFa3I
---

From: [[redpointai]] <br/> 

Percy Liang, a leading AI researcher and co-founder of Together AI, discusses the [[openais_o1_model_and_systemlevel_innovation | OpenAI's o1 model]], its implications for the future of AI, and the broader landscape of [[developing_and_utilizing_ai_models_in_the_tech_industry | AI model development]] and evaluation <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Initial Impressions of OpenAI's o1 <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>
From a product standpoint, o1 was initially perceived as slow and difficult to use <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. However, from a research perspective, its release signals a significant shift towards "test-time compute" <a class="yt-timestamp" data-t="01:01:15">[01:01:15]</a>. This approach allows AI to tackle more ambitious tasks that might take days, weeks, or even months for humans to complete, such as new research or drug discovery <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.

Historically, [[ai_models_and_their_impact_on_productivity | language models]] were seen as prompt-in, response-out systems measured by tokens per second <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>. o1 represents a small but directional step toward [[advancements_and_implications_of_ai_agents | AI agents]] that can reason, plan, and execute tasks over extended periods <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>. This marks a return to concepts from reinforcement learning, where agents take actions and receive feedback to improve over time <a class="yt-timestamp" data-t="03:00:00">[03:03:00]</a>.

## Capabilities and Evaluation Challenges <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>
o1 has shown impressive capabilities in specific domains like math and coding, where multi-step reasoning chains are beneficial <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a>. New benchmarks, such as "Sidebench" for Capture the Flag cyber security exercises, are emerging to test these advanced reasoning abilities <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>. Some of these challenges are so complex that even a team of human competitors might take over 24 hours to solve them <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>.

However, evaluating models like o1 presents [[challenges_and_advancements_in_ai_model_development | challenges]] <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>:
*   **Compatibility Issues**: When integrated into existing systems, o1 might ignore predefined templates for agent behavior (e.g., reflection and planning), leading to less-than-expected overall performance despite improvements in sub-tasks <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>. This highlights that raw benchmark scores don't always tell the full story <a class="yt-timestamp" data-t="05:34:00">[05:34:00]</a>.
*   **Monotonic Progress vs. System Fit**: Simply dropping in a new model doesn't guarantee improvements if it doesn't fit the existing system <a class="yt-timestamp" data-t="05:42:00">[05:42:00]</a>. Compatibility is a crucial, often overlooked factor <a class="yt-timestamp" data-t="06:05:00">[06:05:00]</a>.
*   **Train-Test Overlap**: A persistent problem in evaluation is the unknown content of proprietary training data, making it hard to trust benchmark results <a class="yt-timestamp" data-t="00:30:26">[00:30:26]</a>.
*   **Moving Target**: As [[challenges_and_advancements_in_ai_technology | AI models]] improve, new benchmarks are constantly needed to capture their evolving capabilities <a class="yt-timestamp" data-t="00:31:10">[00:31:10]</a>. Language models themselves are increasingly used to generate new, diverse evaluation inputs <a class="yt-timestamp" data-t="00:32:13">[00:32:13]</a>.
*   **Lack of Transparency**: Compared to earlier models, newer ones often don't provide visibility into their internal reasoning processes, making debugging and customization difficult <a class="yt-timestamp" data-t="07:02:00">[07:02:00]</a>. This "black box" nature can hinder development, especially for novel applications where data coverage might be limited <a class="yt-timestamp" data-t="07:49:00">[07:49:00]</a>.

## Paradigm Shift: Internalized Reasoning and its Implications <a class="yt-timestamp" data-t="06:45:00">[06:45:00]</a>
The o1 model signifies a shift where reasoning scaffolding, previously managed by developers through prompt chaining, is internalized within the model and not exposed to the user <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>. While this aims for greater ease of use, it complicates debugging when things go wrong, as there's no "stack trace" of the model's internal steps <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>. This tension exists between Open AI's desire for the model to "just take care of it" and a developer's need for transparency and customization <a class="yt-timestamp" data-t="07:20:00">[07:20:00]</a>.

This trend also impacts [[the_role_and_potential_of_open_source_models_in_ai | open-source models]] and the competitive landscape. With closed models internalizing their logic, the transparency previously offered by explicit prompt chains is diminishing, leading to more opaque systems <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>.

## [[impact_of_ai_advancements_on_business_models | Impact on the Inference Market]] <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>
The rise of models like o1 with their focus on "test-time compute" has significant implications for the inference market:
*   **Fundamental Building Block**: Inference remains a core, low-level primitive required for every aspect of AI, from training to agentic workflows and synthetic data generation <a class="yt-timestamp" data-t="00:44:10">[00:44:10]</a>. It needs to be robust and cost-effective <a class="yt-timestamp" data-t="00:44:20">[00:44:20]</a>.
*   **Abstraction Shift**: The market is moving beyond merely serving specific models like Llama 3 <a class="yt-timestamp" data-t="00:45:10">[00:45:10]</a>. The focus is on serving models that perform well for specific use cases, and customization becomes key for achieving better and faster performance <a class="yt-timestamp" data-t="00:45:40">[00:45:40]</a>.
*   **Optimization for Agentic Workflows**: The new agentic workflows create opportunities for further optimization, especially in high-throughput settings where many possibilities need to be generated <a class="yt-timestamp" data-t="00:45:58">[00:45:58]</a>.

## Evolution of AI Architectures <a class="yt-timestamp" data-t="00:40:08">[00:40:08]</a>
Historically, model architectures like LSTMs, CNNs, and Transformers were often developed through intuition and experimentation, considering gradients and how they should work <a class="yt-timestamp" data-t="00:40:47">[00:40:47]</a>. However, newer architectures like Mamba (state-space models) emerged from mathematical breakthroughs, solving fundamental problems that then found application within neural networks <a class="yt-timestamp" data-t="00:41:03">[00:41:03]</a>.

It's likely that Transformers will not be the ultimate architecture <a class="yt-timestamp" data-t="00:42:04">[00:42:04]</a>. Future innovations in model architectures are more probable in new domains like video or complex agentic settings, where existing architectures might break down <a class="yt-timestamp" data-t="00:42:19">[00:42:19]</a>. Structural changes are needed for genuinely novel architectures to emerge, often driven by tackling fundamentally different problems, much like machine translation spurred Transformer development <a class="yt-timestamp" data-t="00:43:11">[00:43:11]</a>.

## The Future of AI: Beyond Mimicry <a class="yt-timestamp" data-t="00:48:16">[00:48:16]</a>
AI is moving beyond merely mimicking human capabilities. The next significant milestones involve AI extending human knowledge, such as solving open math problems or discovering new research insights that haven't been solved by humans <a class="yt-timestamp" data-t="00:48:22">[00:48:22]</a>. Finding "zero-days" in cybersecurity is another example of a potential game-changer <a class="yt-timestamp" data-t="00:49:12">[00:49:12]</a>.

Progress in AI is not slowing down; rather, it continues to move quickly, with qualitative changes like o1's approach representing different ways to think about using these systems <a class="yt-timestamp" data-t="00:49:26">[00:49:26]</a>. Advances in chip power and cost reduction will further drive this progress <a class="yt-timestamp" data-t="00:50:03">[00:50:03]</a>.

### Underexplored Application Areas <a class="yt-timestamp" data-t="00:59:01">[00:59:01]</a>
While commercial applications like RAG (Retrieval Augmented Generation) and summarization are well-explored, more fundamental areas remain underexplored <a class="yt-timestamp" data-t="00:59:06">[00:59:06]</a>. These include:
*   Fundamental science and scientific discovery <a class="yt-timestamp" data-t="00:59:21">[00:59:21]</a>
*   Improving researcher productivity <a class="yt-timestamp" data-t="00:59:26">[00:59:26]</a>
Such areas are crucial as they feed back into and enhance the entire AI ecosystem <a class="yt-timestamp" data-t="00:59:34">[00:59:34]</a>.