---
title: Agent Development Life Cycle at Sierra
videoId: 0vBKv9yAQi4
---

From: [[aidotengineer]] <br/> 

At [[sierras_conversational_ai_platform | Sierra]], the Agent Development Life Cycle (ADLC) is the core process used to build and continuously improve AI agents for businesses <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. The company views "every agent as a product," necessitating a fully featured developer and customer experience operations platform for their creation and refinement <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. This approach mirrors the dedication applied to developing mobile apps or websites <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

## Evolution of AI Development

The journey towards the ADLC is informed by the history of AI. Early AI efforts, like the speaker's work on Google Lens in 2016, focused on fundamental tasks such as distinguishing between images (e.g., Chihuahuas and blueberry muffins) <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This period, described as the "AI caves," highlighted the non-deterministic nature of AI models, where consistent results were not guaranteed, feeling like a "slot machine" <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. The iterative improvement over a decade, similar to the continuous [[building_ai_agents_in_the_enterprise_sdlc | software development life cycle]] (SDLC), transformed Google Lens into a highly capable tool for shopping, translation, and more <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

## Why a New Development Cycle for AI Agents?

While traditional software development is deterministic, fast, cheap, rigid, and governed by strict logic, large language models (LLMs) are often non-deterministic, slow, expensive, and flexible <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. LLMs are creative and can reason through problems, but building on them is compared to building on a "foundation of jello" <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>. The ADLC was conceived to leverage the strengths of LLMs while integrating traditional software where beneficial <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.

## The Agent Development Life Cycle (ADLC) in Practice

The ADLC is a systematic process designed to build and improve AI agents, emphasizing iterative refinement with customers in production environments <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.

### Key Aspects of the ADLC:

*   **Quality Assurance (QA):** Customers have access to [[sierras_conversational_ai_platform | Sierra]]'s Experience Manager, allowing them to review every conversation and monitor agent performance in real-time <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.
*   **Feedback and Issue Resolution:** Users can report issues directly, which leads to the filing of an issue, creation of a test, and subsequent release of improvements <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>. Over time, agents accumulate hundreds to thousands of tests as they improve <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>.
*   **Continuous Improvement:** The goal is for an agent to continuously get better every day, even if not perfect at launch <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
*   **Leveraging AI for Development:** Recognizing the rapid advancements in AI, [[sierras_conversational_ai_platform | Sierra]] integrates AI into each stage of the ADLC to accelerate improvements <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. Reasoning models, for example, act as a "force multiplier" for development, testing, and QA <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.

### Case Study: Chubbies' Duncan Smothers

[[sierras_conversational_ai_platform | Sierra]] partnered with Chubbies to create an AI agent named Duncan Smothers <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. Duncan is designed to be capable and engaging, handling various customer inquiries on the Chubbies website <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. Examples of Duncan's capabilities include:
*   Empathetically assisting with sizing and fit questions, offering product recommendations <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   Providing inventory tracking information <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
*   Managing package tracking and issuing refunds <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. This highlights [[agent_networks_and_execution_loops | autonomous agents]] taking action beyond just answering questions <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

The results for Chubbies include helping more customers more quickly and with higher satisfaction <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. Chubbies even allocates a budget for its agents to "delight customers," allowing for proactive solutions like door-dashing shorts from a retail location if unavailable online <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.

## Scalability and Multimodality

The ADLC becomes more effective as customer scale increases, particularly for clients handling tens of millions of requests, where velocity and change management are crucial <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>. The process also adapts to external changes in the AI space, such as model upgrades, new reasoning paradigms, and multimodality <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.

[[sierras_conversational_ai_platform | Sierra]] has also applied the ADLC to voice agents, launching voice capabilities in October <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. Customers like Sirius XM benefit from [[sierras_conversational_ai_platform | Sierra]]'s voice capabilities to answer calls immediately <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>. The approach to voice is similar to responsive web design, where the underlying platform and agent code remain the same but adapt to different channels and modalities <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

## Design Philosophy

Building with AI means working with models that are unpredictable, slow, and not always proficient at math, but also capable of creativity and reasoning <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>. This non-deterministic nature allows for empathetic design, putting oneself in the "shoes of the robot" or the "primordial soup of the jello" to build good experiences <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>. [[sierras_conversational_ai_platform | Sierra]]'s approach aims for robustness by providing LLMs with the same inputs and experiences that humans have <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.