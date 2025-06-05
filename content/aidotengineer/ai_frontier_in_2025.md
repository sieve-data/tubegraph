---
title: AI Frontier in 2025
videoId: HS5a8VIKsvA
---

From: [[aidotengineer]] <br/> 

The year 2025 is described as being "off to an even Wilder start" for AI, following exponential progress in the two and a half years prior, particularly in the last 18 months <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a> <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>. Progress is becoming more aggressive, impressive, and widespread beyond just OpenAI and Anthropic, including models from xAI, Mistral, and DeepSeek <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>. Models are increasingly performant and compute-efficient <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>.

Notable developments in 2025 include:
*   The announcement of the $500 billion Stargate project involving the US government, OpenAI, SoftBank, and Oracle <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.
*   OpenAI's O3 model exceeding human performance in the ARC AGI challenge <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>.
*   DeepSeek's R1 model launch, impacting Nvidia shares and reaching number one in the app store <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>.
*   The France AI Summit, where Macron launched a new AI initiative <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>.

## The AI Agent Moment
2025 is considered the "AI agent moment" and a "perfect storm for AI agents" <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a> <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>. This environment is fostered by several factors:
*   **Reasoning Models** Advanced models like OpenAI's O1 and O3, DeepSeek's R1, and Grok's latest reasoning model are outperforming human ability and demonstrating new capabilities <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>.
*   **Test-Time Compute** Increased compute applied at inference rather than training is boosting model performance <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>.
*   **Engineering and Hardware Optimizations** Significant engineering feats and hardware efficiency are evident, exemplified by the DeepSeek model <a class="yt-timestamp" data-t="04:12:00">[04:12:00]</a>.
*   **Cost Reductions** Inference and hardware are becoming cheaper <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>.
*   **Closing Gap** The performance gap between open-source and closed-source models (e.g., DeepSeek and Llama) is narrowing <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>.
*   **Infrastructure Investment** Billions are being invested in data centers and compute, including the US Stargate project, France's initiative, and Japan's investments with Sopig and Nvidia <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>.

This groundwork sets the stage for the autonomous "agents at work" vision <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.

## Current State of AI Agents
Despite the excitement, [[future_of_ai_agent_ecosystems | AI agents]] are not yet fully operational <a class="yt-timestamp" data-t="04:59:00">[04:59:00]</a>. An [[future_of_ai_agent_ecosystems | AI agent]] is defined as a "fully autonomous system where LLMs direct their own actions" <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>. An example of booking a flight illustrates the current limitations, where an OpenAI operator struggled with complex user preferences and contextual information <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>.

### Cumulative Errors
Unlike hallucinations, which are widely discussed, the problem lies in "tiny cumulative errors that add up" <a class="yt-timestamp" data-t="06:54:00">[06:54:00]</a>. These errors compound in complex multi-agent systems and multi-step tasks <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>.
Types of errors include:
*   **Decision Error** Choosing the wrong fact, such as booking a flight to "San Francisco, Peru" instead of "San Francisco, California" <a class="yt-timestamp" data-t="07:10:00">[07:10:00]</a>.
*   **Implementation Error** Wrong access or integration, like encountering a CAPTCHA or being locked out of a critical database <a class="yt-timestamp" data-t="07:23:00">[07:23:00]</a>.
*   **Heuristic Error** Using the wrong criteria, such as not accounting for New York City traffic conditions or the user's starting location when booking a flight <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>.
*   **Taste Error** Failing to account for personal preferences, like booking a flight on a specific airplane model a user dislikes, even if not explicitly stated <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>.
*   **Perfection Paradox** User frustration arises when AI, despite its magical capabilities, is inconsistent or unreliable, leading to underwhelming human expectations <a class="yt-timestamp" data-t="08:22:00">[08:22:00]</a>. Even highly accurate agents (e.g., 99%) can see their effective accuracy drop significantly over many sequential steps (e.g., to 60% over 50 steps) <a class="yt-timestamp" data-t="08:53:00">[08:53:00]</a>.

## Strategies for Building Better AI Agents
To address these challenges and consistently and reliably make the right decisions, several best practices and strategies are emerging for building [[future_of_ai_agent_ecosystems | AI agents]]:

### 1. Data Curation
Data is paramount for [[future_of_ai_agent_ecosystems | AI agents]] <a class="yt-timestamp" data-t="10:04:00">[10:04:00]</a>. Data is messy, unstructured, and siloed, encompassing web/text, design, image, video, audio, sensor, and even agent-produced data <a class="yt-timestamp" data-t="10:11:00">[10:11:00]</a>. Key aspects include:
*   **Proprietary Data** Curating proprietary data is crucial for quality control in the model workflow <a class="yt-timestamp" data-t="10:32:00">[10:32:00]</a>.
*   **Agent Data Flywheel** Designing systems where every user interaction automatically improves the product in real-time and at scale <a class="yt-timestamp" data-t="10:49:00">[10:49:00]</a>. This includes curating user preferences and recycling past content to adapt to them <a class="yt-timestamp" data-t="11:01:00">[11:01:00]</a>.

### 2. Evaluations (Evals)
Measuring a model's response and choosing the correct answer is critical <a class="yt-timestamp" data-t="11:19:00">[11:19:00]</a>. While straightforward in verifiable domains (e.g., math, science), it's challenging for non-verifiable systems <a class="yt-timestamp" data-t="11:33:00">[11:33:00]</a>.
*   **Collecting Human Preferences** Evals need to collect signals and build evaluations that capture human preferences and personal needs <a class="yt-timestamp" data-t="12:25:00">[12:25:00]</a>. Sometimes, the best evaluation is personal "Vibes" based on individual needs, rather than numbers or leaderboards <a class="yt-timestamp" data-t="12:33:00">[12:33:00]</a>.

### 3. Scaffolding Systems
These systems prevent a single error from causing a cascading effect throughout the organization or agentic system <a class="yt-timestamp" data-t="12:45:00">[12:45:00]</a>.
*   **Mitigation through Compound Systems** Building complex compound systems mitigates cascading errors <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>.
*   **Human-in-the-Loop** Sometimes, bringing a human back into the loop is necessary <a class="yt-timestamp" data-t="13:12:00">[13:12:00]</a>.
*   **Self-Healing Agents** Stronger agents can adapt scaffolding, realizing their own errors, trying to correct their path, or pausing execution when unsure <a class="yt-timestamp" data-t="13:16:00">[13:16:00]</a>. Checkpoints can be added for verification, such as for traffic conditions <a class="yt-timestamp" data-t="13:33:00">[13:33:00]</a>.

### 4. User Experience (UX)
UX is crucial for making [[future_of_ai_agent_ecosystems | AI agents]] better co-pilots <a class="yt-timestamp" data-t="13:44:00">[13:44:00]</a>. Foundation models are rapidly depreciating assets <a class="yt-timestamp" data-t="13:53:00">[13:53:00]</a>, meaning UX truly differentiates [[the_future_of_aidriven_user_applications | AI apps]] <a class="yt-timestamp" data-t="13:59:00">[13:59:00]</a>. Companies that reimagine product experiences, deeply understand user workflows, and promote "beautiful elegant human machine collaboration" will succeed <a class="yt-timestamp" data-t="14:02:00">[14:02:00]</a>.
*   **Contextual Understanding** Asking clarifying questions to fully understand user intent <a class="yt-timestamp" data-t="14:13:00">[14:13:00]</a>.
*   **Predictive UX** Understanding the user's psyche to predict their next step <a class="yt-timestamp" data-t="14:20:00">[14:20:00]</a>.
*   **Seamless Integration** Integrating seamlessly with legacy systems to create real ROI <a class="yt-timestamp" data-t="14:27:00">[14:27:00]</a>.

Lux Capital is particularly interested in new [[ai_native_companies | AI Frontier companies]] with proprietary data sources and deep understanding of specific user workflows, such as those in robotics, hardware, defense, manufacturing, and life sciences <a class="yt-timestamp" data-t="14:51:00">[14:51:00]</a>.

### 5. Multimodality
Moving beyond the chatbot interface, building multimodally can create a 10x more personalized user experience <a class="yt-timestamp" data-t="15:22:00">[15:22:00]</a>. This involves making AI more human by adding "eyes and ears nose a [[future_directions_for_voicefirst_ai | voice]]" <a class="yt-timestamp" data-t="15:43:00">[15:43:00]</a>.
*   **Sensory Integration** Significant improvements are seen in [[future_directions_for_voicefirst_ai | voice]], and efforts are underway in smell (e.g., Osmo) and touch to instill a more human feeling and embodiment with robotics <a class="yt-timestamp" data-t="15:49:00">[15:49:00]</a>.
*   **Memories** The ability to make AI truly personal and know a user on a deeper level <a class="yt-timestamp" data-t="16:07:00">[16:07:00]</a>.
*   **Visionary Products** Reframing the definition of "perfection" to humans means creating products so new and visionary that they exceed expectations, even if inconsistent <a class="yt-timestamp" data-t="16:18:00">[16:18:00]</a>. An example is Tlop, which reimagines the visual canvas by implementing AI through brush strokes and combining multiple AI models seamlessly <a class="yt-timestamp" data-t="16:28:00">[16:28:00]</a>.

In summary, while 2025 presents a perfect storm for [[future_of_ai_agent_ecosystems | AI agents]], they are not yet fully realized due to cumulative errors leading to wrong answers, preferences, criteria, and human expectations <a class="yt-timestamp" data-t="16:51:00">[16:51:00]</a>. Overcoming these [[challenges_of_shipping_ai_products_at_the_frontier | challenges]] requires data curation, effective evaluations, scaffolding systems, and a strong focus on user experience and multimodality to create innovative product experiences <a class="yt-timestamp" data-t="17:09:00">[17:09:00]</a>.