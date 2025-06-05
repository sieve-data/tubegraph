---
title: Scaling paradigms in AI research
videoId: 1XvN5EBDnDw
---

From: [[aidotengineer]] <br/> 

Karina, an AI researcher at OpenAI (previously at Anthropic), highlights significant [[scaling_ai_models_and_their_impact_on_development_tools | scaling paradigms]] in AI research over the past two to four years and their impact on product development, sharing lessons learned from products like Claude and ChatGPT <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. She also discusses the future of AI agents evolving from collaborators to co-innovators <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## Two Core Scaling Paradigms

### 1. Next Token Prediction (Pre-training)

This paradigm, prominent from 2020 to 2021, views the model as a "World building machine" <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. The model learns to understand the world by predicting the next word or token <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. To predict what comes next, the model must understand how the world operates <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. Tokens can be strings, words, or pixels <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

Pre-training involves massive multitask learning, where some tasks are easier to learn, such as translation or factual knowledge like "the capital of France is Paris" <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. However, other tasks are significantly harder and require substantial compute scaling during the training stage <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. These include:
*   Physics and problem-solving <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>
*   Logical expressions and spatial reasoning <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>
*   Complex math, which often necessitates Chain of Thought to aid in computation <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>
*   Creative writing, particularly World building, storytelling, and maintaining plot coherence, where mistakes can easily deteriorate the narrative <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. Measuring "good" creative writing is also a significant open-ended research problem <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

### 2. Scaling Reinforcement Learning on Chain of Thought

Introduced by OpenAI with the model "01" last year, this paradigm focuses on highly complex reasoning <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. It involves spending more test time compute on training reinforcement learning <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. The model learns to think during training and improves through feedback by having strong signals in reinforcement learning <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

To tackle increasingly difficult tasks, such as solving medical problems, models need to spend significant time reasoning through the problem <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. This requires creating more complex environments and utilizing tools to think through and verify outputs during the Chain of Thought process <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. Challenges remain in measuring the faithfulness of the Chain of Thought and enabling models to backtrack from wrong directions <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

### Product Development and Design Challenges

These [[scaling_ai_models_and_their_impact_on_development_tools | scaling paradigms]] have unlocked new avenues for product research <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. High-reasoning models enable a rapid evaluation cycle for product development by:
*   Distilling knowledge back to smaller, faster-iterating models <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.
*   Synthetically generating new data for post-training and reinforcement learning environments <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.

This allows for the creation of entirely new classes of tasks, such as simulating different users for multiplayer collaboration <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>. [[building_scalable_ai_systems | Building scalable AI systems]] also means moving towards more complex reinforcement learning environments where models can use tools like search, browsing, or collaborative canvases to improve their collaborative abilities <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.

Models are becoming extremely good at in-context learning, capable of learning new tools from a few-shot examples, which greatly accelerates the development cycle <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

[[design_challenges_for_ai_agents | Design challenges for AI agents]] include:
*   Bringing unfamiliar capabilities into familiar form factors, such as making 100K context successful through file uploads <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.
*   Enabling modular compositions in product features to scale with future model capabilities, as seen with ChatGPT Tasks which extends beyond reminders to continuous story generation or personalized daily searches <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.
*   Bridging real-time interaction with asynchronous task completion, where models might research or write code for extended periods <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>. Building trust in these asynchronous tasks can be achieved by giving humans new collaborative affordances to verify and edit model outputs, and provide real-time feedback for self-improvement <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>.

## Case Studies and Future Vision

### GitHub Copilot
This product demonstrated the power of pre-training in understanding code and predicting the next token <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. It was made more useful through post-training using Reinforcement Learning from Human Feedback (RLHF) and Reinforcement Learning from AI Feedback (RLAF) <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

### Claude (Anthropic)
Claude on Slack was an early attempt at a virtual teammate, leveraging Slack's tools and multiplayer collaboration features <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>. It could summarize channels across an organization, a concept that inspired future projects like ChatGPT Tasks <a class="yt-timestamp" data-t="00:16:53">[00:16:53]</a>.

### Canvas (OpenAI)
Karina's first project at OpenAI, Canvas, focused on human-AI collaboration and creative capabilities <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>. It offers a flexible interface for:
*   Co-creation and fine-grain editing <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.
*   Model search to generate reports and verify outputs <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>.
*   [[Multiagentic systems in AI | Multi-agentic]] and multiplayer collaboration, allowing critics or editors to join <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>.
*   Becoming a pair programmer and data scientist, capable of analyzing CSV documents in real-time <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.
*   Co-creating new knowledge and research artifacts, enabling human-AI teams to verify research directions or reproduce open-source repositories <a class="yt-timestamp" data-t="00:20:09">[00:20:09]</a>.

## Future of AI Agents: From Collaborators to Co-Innovators

OpenAI considers the current year (2024) the "year of agents," characterized by highly complex reasoning models using real-world tools like browsing, search, and computer use over long contexts <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

The next stage envisions agents as "co-innovators" <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. This combines current reasoning and tool-use capabilities with creativity, enabled through human-AI collaboration <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>. The goal is to create new affordances for humans and AI to co-create the future <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.

Future predictions include:
*   **Invisible software creation for all:** Enabling non-coders to create and deploy their own tools directly from mobile devices <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>. This could facilitate starting businesses from scratch <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>.
*   **Changed internet access:** Users will click less on links and access the internet through model lenses, providing cleaner, more personalized, and multimodal outputs <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>. For instance, learning about the solar system could generate an interactive 3D visualization instead of text <a class="yt-timestamp" data-t="00:22:13">[00:22:13]</a>.
*   **Blank canvas interface:** The AI interface will dynamically adapt to the user's intent. If a user wants to write code, the canvas transforms into an IDE; if they want to write a novel, it provides tools for brainstorming, editing, and visualizing plot structures <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>.
*   **Co-direction and new knowledge creation:** Co-innovation will occur through creative co-direction with models, leveraging highly reasoning [[multiagentic_systems_in_ai | multiagentic systems]] to create new novels, films, games, and fundamentally, new science and knowledge <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>.