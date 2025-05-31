---
title: Future of AI and pretraining challenges
videoId: a0bEU83P8g8
---

From: [[redpointai]] <br/> 

Bob McGrew, former Chief Research Officer at OpenAI, shared insights into the [[challenges_and_opportunities_in_ai_development | future of AI]] and the progress of models, drawing from his six and a half years at the forefront of AI research <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Pre-training Progress: Beyond the Wall

While external observers might perceive a slowdown in AI model capabilities, particularly after GPT-4, the internal view from major labs like OpenAI is quite different <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. The impression of a "wall" in model capabilities is misleading <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

### The Role of Compute and Algorithmic Improvements
To achieve significant progress in pre-training, an immense increase in compute is required. For instance, moving from GPT-2 to GPT-3, or GPT-3 to GPT-4, necessitated a 100x increase in effective compute <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. This increment is achieved through:
*   **Adding more hardware**: Investing in more chips and building larger data centers <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   **Algorithmic improvements**: While these can yield significant gains (50%, 2x, 3x), they are not sufficient on their own for generational leaps <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

Building new data centers is a slow, multi-year process, which explains the perceived gaps between major model releases <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

### O1: A New Generation through Reinforcement Learning
OpenAI's O1 model represents a significant leap, effectively a 100x compute increase over GPT-4, primarily achieved through advanced reinforcement learning (RL) techniques <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. This approach allows the model to create longer, more coherent "Chains of Thought," packing more compute into its answers <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. What's crucial about this method is that it doesn't immediately require new data centers, opening significant room for algorithmic improvements <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. The same techniques could theoretically extend thought processes from minutes to hours or even days <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

## Progress in 2025 and Beyond

Future [[future_trends_in_ai_hardware_and_software | AI progress]] will be different. As new generations of models are developed, new, unforeseen problems emerge, requiring time to work through even after new data centers are available <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. The focus for 2025 is expected to be on "test-time compute" <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

## New Form Factors and the Rise of AI Agents

Current chatbot interactions are well-handled by models like GPT-4 <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. However, to unlock the full capabilities of advanced models like O1, new "form factors" are needed <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. These models excel at structured, long-duration tasks like programming or writing complex documents, which require sustained, coherent reasoning <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

The most exciting development is enabling long-term actions, essentially powerful [[the_future_and_current_state_of_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. These [[the_future_and_current_state_of_ai_agents | agents]] could book flights, shop, or solve problems by interacting with the real world <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

### Challenges for AI Agents and Enterprise Adoption
The primary challenge for [[the_future_and_current_state_of_ai_agents | AI agents]] is **reliability** <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. If an agent makes mistakes while performing actions (e.g., buying something or sending an email), it can lead to wasted time, embarrassment, or financial loss <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. Achieving higher reliability (e.g., from 90% to 99% or 99% to 99.9%) demands another order of magnitude increase in compute, which takes years of work <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

For enterprise adoption, the key is providing context to the AI, which is currently a hand-holding process <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. This context (co-workers, projects, codebases, preferences) is scattered across various enterprise systems (Slack, documents, Figma) <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>. Solutions include:
*   Building libraries of "connectors" to integrate data sources <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.
*   Developing "computer use" models, like Anthropic's, which can control a mouse and keyboard as a general "hammer" <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>. However, this increases token count significantly (10x-100x), again emphasizing the need for models with long, coherent Chains of Thought <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.

The future will likely see a mix of these approaches <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>. Widespread computer use agents are still a few years away, moving from compelling demos to limited use cases in a year, and surprisingly effective but not perfectly reliable in two years <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>. [[challenges_in_ai_adoption_and_deployment | Adoption]] hinges on the tolerable level of mistakes <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.

## Multimodal AI and Video Models

Multimodal AI, incorporating vision and audio alongside text, is another exciting area <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>. While models like DALL-E (image generation) and Whisper (audio) started as separate entities, they are gradually being integrated into core models <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.

Video has been the most challenging modality to integrate <a class="yt-timestamp" data-t="00:18:54">[00:18:54]</a>. OpenAI's Sora is a pioneering example <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>. Two key differences for video models are:
*   **Extended sequences**: Video is not a single prompt but an unfolding story, requiring new user interfaces for creation <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>.
*   **High cost**: Training and running video models are very expensive <a class="yt-timestamp" data-t="00:20:18">[00:20:18]</a>.

The progress of video models is expected to mirror LLMs: quality will improve, especially for extended coherent generations (e.g., from seconds to hours of video), and costs will drop dramatically, making high-quality, realistic videos practically free <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a>. A full-length, AI-generated movie that audiences genuinely want to watch is predicted within two years, driven by human creative vision leveraging the AI tool <a class="yt-timestamp" data-t="00:23:08">[00:23:08]</a>.

## Robotics: A Resurgent Field

Robotics, a personal passion for McGrew, is expected to see widespread, though somewhat limited, adoption within five years <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>. Foundation models are a breakthrough due to their ability to:
*   Translate vision into plans of action <a class="yt-timestamp" data-t="00:25:32">[00:25:32]</a>.
*   Enable natural language interaction with robots, simplifying control (e.g., talking to a robot instead of typing commands) <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>.

A major unresolved question in robotics is whether to learn primarily in simulation or the real world <a class="yt-timestamp" data-t="00:26:29">[00:26:29]</a>. While simulators are useful for rigid bodies, they struggle with "floppy" materials (cloth, cardboard), making real-world demonstrations necessary for general-purpose robots <a class="yt-timestamp" data-t="00:27:11">[00:27:11]</a>.

Mass consumer adoption of home robots is still distant due to safety concerns (robot arms can be dangerous) and the unconstrained nature of home environments <a class="yt-timestamp" data-t="00:28:10">[00:28:10]</a>. However, widespread deployment in constrained work environments like warehouses and retail is expected within five years <a class="yt-timestamp" data-t="00:28:36">[00:28:36]</a>.

## Specialization vs. General Models

Frontier labs will continue to develop large, general-purpose models that perform well across various modalities and tasks <a class="yt-timestamp" data-t="00:29:41">[00:29:41]</a>. However, specialization offers significant price-performance advantages <a class="yt-timestamp" data-t="00:29:55">[00:29:55]</a>. A common strategy for companies is to:
1.  Define the desired AI task.
2.  Run it against a best-in-class frontier model to generate a large dataset.
3.  Fine-tune a much smaller, cheaper model on this dataset for specific use cases (e.g., customer service chatbots) <a class="yt-timestamp" data-t="00:30:21">[00:30:21]</a>.

While these specialized models may not be as robust as frontier models when going "off-script," the cost savings justify the trade-off <a class="yt-timestamp" data-t="00:31:02">[00:31:02]</a>.

## The Slow Burn of AI Productivity

Despite rapid advancements in AI capabilities, the impact on overall productivity statistics (e.g., GDP growth) has been surprisingly slow <a class="yt-timestamp" data-t="00:31:42">[00:31:42]</a>. This phenomenon, reminiscent of the internet in the 1990s, is attributed to several factors:
*   **Underestimation of job complexity**: What humans do in a "job" is composed of many tasks, and often a core task remains difficult to automate <a class="yt-timestamp" data-t="00:33:05">[00:33:05]</a>.
*   **Boilerplate vs. Core Reasoning**: AI initially automates the "boilerplate" parts of a job (e.g., code generation), leaving the more challenging "giving direction" or "figuring out what to do" aspects to humans <a class="yt-timestamp" data-t="00:33:37">[00:33:37]</a>.

McGrew is particularly excited about applying AI to "boring" problems in areas like procurement, where infinite patience is more valuable than infinite intelligence <a class="yt-timestamp" data-t="00:34:11">[00:34:11]</a>. AI can save significant money by meticulously comparison shopping, a task human experts find tedious <a class="yt-timestamp" data-t="00:34:47">[00:34:47]</a>. Studies showing productivity gains from AI, particularly among lower-performing individuals, are seen as hopeful; AI helps those who know *what* to do but struggle with *how* to do it <a class="yt-timestamp" data-t="00:35:55">[00:35:55]</a>.

## OpenAI's Culture and Pivots

OpenAI's culture is characterized by its numerous "refoundings" or pivots, which were often controversial but necessary <a class="yt-timestamp" data-t="00:53:53">[00:53:53]</a>:
*   **Nonprofit to For-profit**: Transitioning from a research-focused nonprofit to a for-profit entity to secure funding <a class="yt-timestamp" data-t="00:41:01">[00:41:01]</a>.
*   **Microsoft Partnership**: Partnering with Microsoft, initially controversial, provided crucial compute resources <a class="yt-timestamp" data-t="00:41:41">[00:41:41]</a>.
*   **Building Products**: The decision to build their own products (like the API) alongside research, demonstrating model value <a class="yt-timestamp" data-t="00:42:04">[00:42:04]</a>.
*   **ChatGPT Release**: A famously "accidental" release of ChatGPT, which was not initially thought to have met the bar for daily use by the team, but exploded in popularity <a class="yt-timestamp" data-t="00:44:05">[00:44:05]</a>. The team initially worried it would be a fad, like DALL-E 2 <a class="yt-timestamp" data-t="00:45:25">[00:45:25]</a>.
*   **Focus on Language Modeling**: The decision to double down on language modeling (including multimodal work) was a painful but critical choice, leading to the shutdown of exploratory projects like robotics and games teams <a class="yt-timestamp" data-t="00:59:34">[00:59:34]</a>. This came from the conviction, learned from projects like Dota 2, that problems could be solved by increasing scale <a class="yt-timestamp" data-t="01:00:37">[01:00:37]</a>.

These shifts, occurring every 18-24 months, fundamentally changed the company's purpose and the identity of its people, moving from paper writing to building a single model for global use <a class="yt-timestamp" data-t="00:42:20">[00:42:20]</a>.

## The Future of Artificial General Intelligence (AGI)

McGrew expresses a deep critique of the concept of AGI as a single "moment," believing that progress will be continuous and "fractal" <a class="yt-timestamp" data-t="00:47:11">[00:47:11]</a>. He anticipates an AGI future that feels "banal" – where self-driving cars take people to offices where they boss around AI armies, and it still feels like "office space" <a class="yt-timestamp" data-t="00:47:25">[00:47:25]</a>.

He contends that solving reasoning was the *last fundamental challenge* needed to scale to human-level intelligence <a class="yt-timestamp" data-t="00:47:59">[00:47:59]</a>. Now, the remaining challenge is **scaling**, which encompasses systems, hardware, optimization, and data problems <a class="yt-timestamp" data-t="00:48:17">[00:48:17]</a>. In this sense, the path to AGI is "predestined," though the scaling work itself is immensely difficult <a class="yt-timestamp" data-t="00:48:50">[00:48:50]</a>.

## Societal Impact and the Scarcity of Agency

McGrew believes that society is moving from a world where intelligence is a critical scarcity to one where it will be ubiquitous and free <a class="yt-timestamp" data-t="00:49:16">[00:49:16]</a>. The new scarce factor of production will likely be **agency**: the ability to ask the right questions and pursue the right projects <a class="yt-timestamp" data-t="00:49:34">[00:49:34]</a>. AI will struggle to solve these core human problems <a class="yt-timestamp" data-t="00:49:47">[00:49:47]</a>. This shift will feel continuous, like an exponential curve <a class="yt-timestamp" data-t="00:50:11">[00:50:11]</a>. While AI can create a video from a vague prompt, a human's agency is needed to craft the *desired* video through detailed choices <a class="yt-timestamp" data-t="00:50:58">[00:50:58]</a>.

## AI Research and Future Outlook

McGrew emphasizes the importance of **grit** in top AI researchers <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a>. He recounts Adria Ramos's 18-month perseverance to generate a "pink panda skating on ice" image with DALL-E, proving neural network creativity, despite initial results being just a blur <a class="yt-timestamp" data-t="00:38:12">[00:38:12]</a>.

He views engineers and researchers as "artists" who must be allowed freedom to pursue their vision, especially in research, where stifling artistry can prevent foundational breakthroughs <a class="yt-timestamp" data-t="00:39:05">[00:39:05]</a>.

In terms of future research, McGrew finds programming a consistently useful metric for evaluating models because it scales from simple line completion to entire website creation, and it's far from a solved problem <a class="yt-timestamp" data-t="00:53:56">[00:53:56]</a>. He also sees immense potential for AI in social sciences, particularly in simulating human interaction for product management and AB testing <a class="yt-timestamp" data-t="00:55:25">[00:55:25]</a>.

McGrew left OpenAI after accomplishing his core research program goals (pre-training, multimodal, reasoning) and felt it was time to pass the torch to the next generation <a class="yt-timestamp" data-t="01:03:51">[01:03:51]</a>. He plans to explore new ideas, learn, and meet people, much like his two-year period between Palantir and OpenAI, without rushing into his next venture <a class="yt-timestamp" data-t="01:04:36">[01:04:36]</a>.

He concludes that [[challenges_and_opportunities_in_ai_model_development_and_infrastructure | progress in AI]] will continue to be exciting and will not slow down, but it *will* change <a class="yt-timestamp" data-t="01:06:55">[01:06:55]</a>.

### Overhyped vs. Underhyped
*   **Overhyped**: New architectures that tend to fall apart at scale <a class="yt-timestamp" data-t="01:03:08">[01:03:08]</a>. [[limitations_of_current_ai_models_and_future_architecture | Limitations of current AI models and future architecture]] are often overlooked.
*   **Underhyped**: O1 <a class="yt-timestamp" data-t="01:03:24">[01:03:24]</a>.