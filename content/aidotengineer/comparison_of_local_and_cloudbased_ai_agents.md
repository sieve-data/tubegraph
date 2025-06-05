---
title: Comparison of local and cloudbased AI agents
videoId: jMoAaZP_Kkw
---

From: [[aidotengineer]] <br/> 

An AI agent is defined as something that possesses agency and can act in the world. Conversely, anything that can only gather context and process information without taking external action is not considered an agent <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. For instance, Swix's AI news, while useful for aggregating information, is not an agent because it doesn't take actions <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. The effectiveness of an intelligent agent is heavily reliant on its context; without sufficient context, it is as good as useless <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

## Importance of Context for Personal Agents

A personal agent's utility is tied to its ability to access and understand a user's life context <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. If an agent lacks access to crucial information sources (e.g., specific messaging apps for prescriptions, or different bank accounts for financial data), it can provide incorrect or incomplete information, leading to an irritating and unpredictable user experience <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>, <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. For an agent to be truly useful, it must achieve a high level of reliability and predictability <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

The ideal scenario for providing context is for the AI to "see everything you see and listen to everything you hear" <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

### Challenges in Providing Context

*   **Wearable devices**: Not practical due to current battery limitations <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   **Mobile phones**: Ecosystems like Apple restrict asynchronous background processes, limiting an agent's ability to constantly monitor screen activity or run in the background <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
*   **Feasible Local Setup**: A Mac Mini connected to the internet can be a practical device for running a personal AI agent asynchronously, offering no battery life issues and allowing access to various services, including the open Android ecosystem <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

## Arguments for Local and Private AI Agents

Despite the option to subscribe to cloud-based agent services, there are strong reasons to favor local and private personal agents:

### 1. Trust and Predictability
Users trust digital services like cloud email because they operate on a simple, predictable mental model (e.g., "email in, reply out") <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. This trust correlates directly with understanding how the service behaves <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
If a service's action space becomes powerful and unpredictable (e.g., auto-replying to emails on your behalf without full control), users become uncomfortable <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. With personal agents taking actions on your behalf, this unpredictability can lead to significant issues, such as an agent making purchasing decisions based on kickbacks rather than user preference <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. Ultimately, for something as personal as an agent, users want to be in control <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

### 2. Decentralization
Current digital ecosystems often function as "walled gardens" that prevent interoperability <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. Building a personal agent around a single, potentially restrictive ecosystem might not be desirable for an agent capable of taking a wide array of actions across different aspects of a user's daily life <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. Local agents foster decentralization and greater user autonomy.

### 3. Privacy and "Thought Crimes"
When an AI agent deeply augments a user's personal life, users might ask it questions or provide information they would never vocalize publicly <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. Using a cloud provider for such an intimate service carries the risk of legally mandated logging and safety checks, even for enterprise-grade APIs <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>. This raises concerns about privacy and the potential for "thought crimes" — the idea of being persecuted for private thoughts or queries <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>. Focusing on local agents mitigates this risk for the most personal augmentations <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.

## Challenges for Local AI Agents

### Technical Challenges
*   **Running Models Locally**: While projects like `ollama` and `vllm` are excellent for running local models (often built on PyTorch <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>), local model inference is currently slower and more limited compared to cloud services <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. While smaller models (e.g., 20 billion parameters or distilled models) can run quickly, larger, unquantized models remain very slow <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>. However, this is seen as a rapidly improving area <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>.

### Research and Product Challenges
The main [[challenges_in_ai_agent_evaluation | challenges in AI agent evaluation]] are not solely technical, but also involve research and product development:
*   **Open Multimodal Models**: These models are currently good but not great <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.
    *   **Computer Vision**: Even closed models struggle with computer vision for agents, frequently breaking <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
    *   **Understanding Taste/Specificity**: Models often provide generic shopping recommendations. When given specific taste preferences, they fail to accurately identify visual elements, relying more on text matching <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.
*   **Catastrophic Action Classifiers**: There's a lack of robust mechanisms to identify "catastrophic actions" – irreversible or highly damaging actions an agent might take (e.g., buying a car instead of laundry detergent) <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>, <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>. More research is needed to enable agents to identify such actions and notify users before proceeding, which is crucial for building user trust <a class="yt-timestamp" data-t="00:16:28">[00:16:28]</a>.
*   **Voice Mode**: Open-source voice mode for local agents is still in nascent stages, but is essential for natural interaction <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>.

## Optimism for Local AI Agents

Despite the [[challenges_in_ai_agent_evaluation | challenges in AI agent evaluation]], there's strong optimism for local AI agents due to the rapid progress of open models:
*   **Compounding Intelligence of Open Models**: Open models are improving their intelligence faster than closed models because they benefit from broader, coordinated community resources and contributions <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>.
*   **Open Source Advantage**: Similar to projects like Linux, once open source communities achieve a critical mass for coordination, they tend to win in unprecedented ways <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>. This suggests that open models will eventually outperform closed models in terms of efficiency and investment return ("per dollar of investment") <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.
*   **Pytorch's Role**: PyTorch is actively working on enabling local agents, addressing many of the technical challenges <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.