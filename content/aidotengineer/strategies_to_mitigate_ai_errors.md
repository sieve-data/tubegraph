---
title: Strategies to Mitigate AI Errors
videoId: HS5a8VIKsvA
---

From: [[aidotengineer]] <br/> 

While 2025 is considered the "AI agent moment," with reasoning models outperforming human ability and increasing computational efficiency, AI agents are not yet fully operational in practical applications <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>. Despite significant advancements, autonomous AI systems encounter various challenges that prevent consistent and reliable performance <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.

## Defining AI Agents
For the purpose of addressing these challenges, an AI agent is defined as a fully autonomous system where large language models (LLMs) direct their own actions <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>.

## The Problem of Cumulative Errors
Often, discussions about AI errors focus on "hallucinations" or "fabrications" <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>. However, a more pervasive issue is the accumulation of "tiny cumulative errors" that compound over multi-step tasks <a class="yt-timestamp" data-t="06:54:00">[06:54:00]</a>.

Consider a seemingly simple task, like booking a flight from New York to San Francisco with specific constraints (e.g., after 3 PM, avoid rush hour, specific airlines, under $500, aisle seat not near bathroom, before midnight) <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>. An AI agent might struggle with this complex request, as demonstrated by attempts using an OpenAI operator that failed to meet the criteria <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>.

These errors, even when minor, can lead to significant disparities in performance over multiple steps <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>. For example, an agent with 99% accuracy might drop to 60% accuracy after 50 consecutive steps, while a 95% accurate agent performs even worse <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>.

### Types of Cumulative Errors
*   **Decision Error:** The AI chooses the wrong fact, such as booking a flight to "San Francisco, Peru" instead of "San Francisco, California" <a class="yt-timestamp" data-t="07:10:00">[07:10:00]</a>.
*   **Implementation Error:** The AI encounters wrong access or integration issues, like a CAPTCHA interrupting a flow or getting locked out of a database <a class="yt-timestamp" data-t="07:23:00">[07:23:00]</a>.
*   **Heuristic Error:** The AI applies the wrong criteria, such as not accounting for New York City rush hour traffic when booking a 5:30 PM flight from JFK, or not asking the user's starting borough <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>.
*   **Taste Error:** The AI fails to account for personal preferences not explicitly stated in the prompt, such as booking a flight on a specific aircraft type the user dislikes <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>.
*   **Perfection Paradox:** Human expectations are set too high for AI's magical capabilities, leading to frustration when agents are slow or inconsistent, even if they ultimately get the task right <a class="yt-timestamp" data-t="08:22:00">[08:22:00]</a>.

## Strategies for Mitigating AI Errors

To optimize complex AI agents and ensure consistent, reliable decision-making, several [[challenges_and_strategies_in_ai_production | strategies for AI production]] can be employed <a class="yt-timestamp" data-t="09:30:00">[09:30:00]</a>. These [[strategies_for_effective_ai_implementation | strategies for effective AI implementation]] aim to mitigate cumulative errors and improve overall agent performance.

### 1. Data Curation
Data is paramount, and its quality and organization directly impact an AI agent's effectiveness <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.
*   **Comprehensive Data:** Data is messy, unstructured, siloed, and includes various modalities beyond text and web, such as design, image, video, audio, sensor, and manufacturing data <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>.
*   **Proprietary Data:** Focus on curating proprietary data, including data the AI agent generates itself, and data used for quality control within the model workflow <a class="yt-timestamp" data-t="10:32:00">[10:32:00]</a>.
*   **Agent Data Flywheel:** Design an agent data flywheel from day one, allowing the product to automatically improve in real-time and at scale every time a user interacts with it <a class="yt-timestamp" data-t="10:49:00">[10:49:00]</a>. For example, collecting a curated dataset of a user's travel preferences, including specific airline and aircraft dislikes, and recycling this content to adapt to preferences over time <a class="yt-timestamp" data-t="11:01:00">[11:01:00]</a>.

### 2. Evals (Evaluations)
Rigorous evaluations are crucial for collecting and measuring a model's responses and choosing the correct answer <a class="yt-timestamp" data-t="11:19:00">[11:19:00]</a>. This aligns with [[strategies_for_ai_evaluation_and_troubleshooting | strategies for AI evaluation and troubleshooting]].
*   **Verifiable Domains:** Evals are straightforward in verifiable domains with clear yes/no answers, like math and science benchmarks <a class="yt-timestamp" data-t="11:33:00">[11:33:00]</a>.
*   **Non-Verifiable Systems:** The challenge lies in setting up evaluations for non-verifiable systems where answers are subjective (e.g., "Did Grace like this plane seat?") <a class="yt-timestamp" data-t="11:50:00">[11:50:00]</a>.
*   **Human Preferences:** It's essential to collect human preferences and build evaluations that are truly personal <a class="yt-timestamp" data-t="12:27:00">[12:27:00]</a>. Sometimes, the best evaluation is simply trying out the agent yourself, relying on "Vibes" based on personal needs rather than numbers or leaderboards <a class="yt-timestamp" data-t="12:33:00">[12:33:00]</a>.

### 3. Scaffolding Systems
[[best_practices_for_building_resilient_ai_workflows | Building resilient AI workflows]] requires scaffolding systems to prevent a single error from causing a cascading effect throughout the organization or agentic system <a class="yt-timestamp" data-t="12:44:00">[12:44:00]</a>.
*   **Infrastructure Logic:** Implement infrastructure logic to ensure that a failure in a new applied AI feature does not impact the broader production infrastructure <a class="yt-timestamp" data-t="12:56:00">[12:56:00]</a>.
*   **Compound Systems & Human in the Loop:** Mitigate scaffolding by building complex compound systems where different components work together, and sometimes, bringing a human back into the loop for reasoning <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>.
*   **Self-Healing Agents:** For stronger agents, adapt the scaffold to allow them to self-heal and grow, realizing when they are wrong and correcting their own path, or breaking execution when unsure to get back on track <a class="yt-timestamp" data-t="13:18:00">[13:18:00]</a>. Checkpoints can be added, for instance, to verify traffic conditions for a flight booking <a class="yt-timestamp" data-t="13:33:00">[13:33:00]</a>.

### 4. User Experience (UX)
UX is critical because AI apps often use the same underlying foundation models, which are quickly depreciating assets <a class="yt-timestamp" data-t="13:43:00">[13:43:00]</a>. The quality of the product experience and the user workflow distinguishes successful AI applications.
*   **Human-Machine Collaboration:** Reimagine product experiences to deeply understand user workflows and promote elegant human-machine collaboration <a class="yt-timestamp" data-t="14:02:00">[14:02:00]</a>.
*   **Concrete Examples:**
    *   Asking clarifying questions to fully understand the user's intent, like with Deep Research <a class="yt-timestamp" data-t="14:13:00">[14:13:00]</a>.
    *   Understanding the user's psyche to predict their next step, as seen with Wier from Codium for developers <a class="yt-timestamp" data-t="14:20:00">[14:20:00]</a>.
    *   Seamlessly integrating with legacy systems to create real ROI for users, such as Harvey in the legal world <a class="yt-timestamp" data-t="14:27:00">[14:27:00]</a>.
*   **Proprietary Data & Workflow Knowledge:** Companies with proprietary data sources and deep understanding of specific user workflows (e.g., robotics, hardware, defense, manufacturing, life sciences) are well-positioned to create magical experiences for end-users <a class="yt-timestamp" data-t="14:55:00">[14:55:00]</a>.

### 5. Multimodality
Moving beyond traditional interfaces like chatbots, [[strategies_for_adapting_ai_models_and_prompts | multimodality]] allows for reimagining and creating 10x more personalized user experiences <a class="yt-timestamp" data-t="15:22:00">[15:22:00]</a>.
*   **Human-like Senses:** Make AI more human by incorporating senses such as eyes, ears, nose, voice, and touch <a class="yt-timestamp" data-t="15:43:00">[15:43:00]</a>. Voice improvements have been significant, and digitizing the sense of smell is also being explored <a class="yt-timestamp" data-t="15:50:00">[15:50:00]</a>.
*   **Embodiment & Memory:** Instill a more human feeling and sense of embodiment through robotics <a class="yt-timestamp" data-t="16:01:00">[16:01:00]</a>. Furthermore, enable AI to have "memories" to know users on a deeper, truly personal level <a class="yt-timestamp" data-t="16:07:00">[16:07:00]</a>.
*   **Visionary Product Experience:** Even if an agent is inconsistent or unreliable, a visionary product that exceeds expectations through novel multimodal experiences can reframe what "perfection" means to a human <a class="yt-timestamp" data-t="16:18:00">[16:18:00]</a>. An example is Tlop, which reimagines the visual canvas by implementing AI through brush strokes and combining various AI models seamlessly in the background <a class="yt-timestamp" data-t="16:28:00">[16:28:00]</a>.

By focusing on these strategies, organizations can work towards building more robust, reliable, and user-friendly AI agents despite the inherent [[challenges_in_ai_development | challenges in AI development]] <a class="yt-timestamp" data-t="16:51:00">[16:51:00]</a>.