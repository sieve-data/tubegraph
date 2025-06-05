---
title: Best Practices for Building AI Systems
videoId: HS5a8VIKsvA
---

From: [[aidotengineer]] <br/> 

The year 2025 marks a "perfect storm" for AI agents, driven by advancements in reasoning models like OpenAI's O1 and O3, DeepSeek's R1, and Grok's latest models, which are outperforming human ability and showcasing new capabilities <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>. This progress is further fueled by increased test-time compute, enhanced engineering and hardware optimizations, cheaper inference and hardware, a closing gap between open-source and closed-source models, and billions in infrastructure investment <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>. Despite this momentum, AI agents are not yet consistently working as intended <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.

An AI agent, for the purpose of this discussion, is defined as a fully autonomous system where large language models (LLMs) direct their own actions <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>.

## Challenges in AI Agent Development

While much focus is often placed on hallucinations and fabrications in AI models, a significant challenge arises from tiny, cumulative errors that add up <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>. These errors can compound rapidly, leading to substantial disparities in performance over multiple steps <a class="yt-timestamp" data-t="08:51:00">[08:51:00]</a>. For example, an agent with 99% accuracy can drop to 60% accuracy after 50 consecutive steps due to compounded errors <a class="yt-timestamp" data-t="09:07:00">[09:07:00]</a>.

Key types of cumulative errors include:
*   **Decision Error**: Choosing the wrong fact or overthinking/exaggerating <a class="yt-timestamp" data-t="07:10:00">[07:10:00]</a>. An example is booking a flight to San Francisco, Peru instead of San Francisco, California <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>.
*   **Implementation Error**: Incorrect access or integration, such as being locked out of a critical database or encountering a CAPTCHA <a class="yt-timestamp" data-t="07:26:00">[07:26:00]</a>.
*   **Heuristic Error**: Applying the wrong criteria or failing to acknowledge best practices, like not accounting for rush hour traffic when booking a flight <a class="yt-timestamp" data-t="07:44:00">[07:44:00]</a>.
*   **Taste Error**: Misinterpreting personal preferences, such as booking a flight on an airline or aircraft type the user dislikes <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>.

Additionally, there's a "Perfection Paradox" where users become frustrated when AI performs at human speed or has minor inconsistencies, despite its otherwise magical capabilities <a class="yt-timestamp" data-t="08:22:00">[08:22:00]</a>. Even if an agent initially gets it right, inconsistency and unreliability can lead to underwhelming human expectations <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>.

## [[best_practices_and_lessons_learned_in_ai_agent_development | Best Practices for Building AI Agents]]

To address these challenges and consistently and reliably make the right decisions, several strategies constitute [[best_practices_for_ai_deployment_and_optimization | best practices for AI deployment and optimization]]:

### Data Curation
Ensuring an AI agent has the necessary, high-quality information is crucial <a class="yt-timestamp" data-t="10:04:00">[10:04:00]</a>. Data is often messy, unstructured, and siloed, encompassing not just web and text but also design, image, video, audio, sensor, and even real-time agent-generated data <a class="yt-timestamp" data-t="10:11:00">[10:11:00]</a>. [[best_practices_for_ai_deployment_and_optimization | Key practices]] include:
*   **Curating proprietary data**: Utilizing unique datasets <a class="yt-timestamp" data-t="10:32:00">[10:32:00]</a>.
*   **Managing agent-generated data**: Data produced by the AI agent itself <a class="yt-timestamp" data-t="10:35:00">[10:35:00]</a>.
*   **Quality control**: Using data in the model workflow for quality assurance <a class="yt-timestamp" data-t="10:37:00">[10:37:00]</a>.
*   **Designing an agent data flywheel**: Building systems where every user interaction improves the product automatically, in real-time, and at scale <a class="yt-timestamp" data-t="10:49:00">[10:49:00]</a>. This allows for continuous adaptation to user preferences <a class="yt-timestamp" data-t="11:10:00">[11:10:00]</a>.

### [[best_practices_for_ai_evaluation | The Importance of Evals]]
[[best_practices_for_ai_evaluation | Evaluating]] how a model responds and choosing the correct answer is fundamental <a class="yt-timestamp" data-t="11:22:00">[11:22:00]</a>. While simple in verifiable domains like math and science, evaluating non-verifiable systems, where clear yes/no answers are absent, is complex <a class="yt-timestamp" data-t="11:33:00">[11:33:00]</a>.
*   **Collecting human preferences**: Actively gathering signals on what users prefer <a class="yt-timestamp" data-t="12:27:00">[12:27:00]</a>.
*   **Personalized evaluations**: Building evals that are truly personal, sometimes relying on "vibes" and direct user experience rather than just numbers or leaderboards <a class="yt-timestamp" data-t="12:29:00">[12:29:00]</a>.

### Scaffolding Systems
To prevent one error from cascading throughout an agentic system and across production infrastructure, scaffolding is essential <a class="yt-timestamp" data-t="12:45:00">[12:45:00]</a>.
*   **Mitigating cascading effects**: Building a complex compound system that ensures errors don't spread <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>.
*   **Human-in-the-loop**: Incorporating human intervention for reasoning models, allowing for checkpoints to verify decisions or steer the agent back on track <a class="yt-timestamp" data-t="13:12:00">[13:12:00]</a>.
*   **Self-healing agents**: Designing agents that can realize they are wrong and attempt to correct their own path, or pause execution when unsure <a class="yt-timestamp" data-t="13:18:00">[13:18:00]</a>.

### User Experience (UX)
UX is paramount, as many AI applications often use the same underlying foundation models <a class="yt-timestamp" data-t="13:51:00">[13:51:00]</a>. [[efficiency_and_smart_execution_in_ai_systems | UX]] is the key differentiator for companies that reimagine product experiences and deeply understand user workflows, fostering elegant human-machine collaboration <a class="yt-timestamp" data-t="13:59:00">[13:59:00]</a>.
*   **Asking clarifying questions**: Ensuring the AI fully understands the user's intent <a class="yt-timestamp" data-t="14:13:00">[14:13:00]</a>.
*   **Predicting user next steps**: Understanding user psychology to anticipate needs <a class="yt-timestamp" data-t="14:20:00">[14:20:00]</a>.
*   **Seamless integration**: Creating real return on investment (ROI) by integrating with legacy systems <a class="yt-timestamp" data-t="14:29:00">[14:29:00]</a>.
Companies with proprietary data sources and deep knowledge of specific user workflows, such as in robotics, hardware, defense, manufacturing, and life sciences, are well-positioned to create magical user experiences <a class="yt-timestamp" data-t="14:55:00">[14:55:00]</a>.

### Building Multimodally
Moving beyond simple chatbot interfaces, multimodality allows for reimagined, 10x personalized user experiences <a class="yt-timestamp" data-t="15:22:00">[15:22:00]</a>. The goal is to make AI more human by adding "eyes and ears, nose, a voice" <a class="yt-timestamp" data-t="15:40:00">[15:40:00]</a>.
*   **Incorporating diverse senses**: Significant improvements have been seen in voice, and there is exploration into digitizing the sense of smell and instilling a sense of touch and embodiment through robotics <a class="yt-timestamp" data-t="15:50:00">[15:50:00]</a>.
*   **Personalized memories**: Developing AI that truly knows the user on a deeper, more personal level <a class="yt-timestamp" data-t="16:07:00">[16:07:00]</a>.
This approach redefines "perfection" for a human, where the visionary nature of the product can exceed expectations even if the agent is occasionally inconsistent or unreliable <a class="yt-timestamp" data-t="16:18:00">[16:18:00]</a>. Examples include reimagining visual canvases and combining multiple AI models seamlessly in the background <a class="yt-timestamp" data-t="16:28:00">[16:28:00]</a>.

In summary, while AI agents are poised for significant impact, achieving widespread reliability requires addressing cumulative errors through meticulous data curation, robust evaluations, resilient scaffolding systems, and a strong focus on innovative, multimodal user experiences <a class="yt-timestamp" data-t="16:51:00">[16:51:00]</a>.