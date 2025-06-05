---
title: Reinforcement learning and Chain of Thought
videoId: 1XvN5EBDnDw
---

From: [[aidotengineer]] <br/> 

Karina, an AI researcher at OpenAI, discusses the scaling paradigms that have shaped AI research over the past few years, particularly focusing on how these paradigms have unlocked new frontiers in product development <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Two Major AI Scaling Paradigms

Over the past few years, two primary scaling paradigms have emerged in AI research <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>:

1.  **Next Token Prediction (Pre-training)** <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>
2.  **Scaling Reinforcement Learning on Chain of Thought** <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>

### 1. Next Token Prediction (Pre-training)

This paradigm is described as a "world-building machine" where the model learns to understand the world by predicting the next token <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. This works because certain sequences are caused by initial actions and are irreversible, leading the model to learn some "physics of the world" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. Tokens can be anything, including strings, words, or pixels <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

Next token prediction functions as massive multi-task learning <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. While some tasks, like translation, are easy to learn, others are significantly harder <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. The model learns problem-solving, generation, logical expressions, and spatial reasoning <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

For complex computational tasks such as math, where the model needs to compute numbers during next token prediction, the difficulty is very high <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This is where [[chain_of_thought_reasoning_in_ai | Chain of Thought]] becomes crucial, allowing the model to reason through these computationally intensive tasks <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. Creative writing is another example of a difficult task, as maintaining plot coherence is challenging and measuring "good" creative writing is an open research problem <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

The period of 2020-2021 was an era of scaling pre-training significantly <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. An early product from this era was GitHub Copilot, which used next token prediction on billions of code tokens <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

#### Post-Training with Reinforcement Learning

The capabilities of pre-trained models were further refined in the "post-training" era using [[reinforcement_learning_in_large_language_models | reinforcement learning]] from Human Feedback (RLHF) and [[reinforcement_learning_in_large_language_models | reinforcement learning]] from AI Feedback (RLAIF) <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. This process made models like GitHub Copilot more useful for tasks such as completing function bodies, understanding docstrings, generating multi-line completions, and predicting/applying diffs <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. This era continues to be explored for pushing models to reason through complex codebases <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### 2. Scaling Reinforcement Learning on Chain of Thought

This paradigm, which emerged more recently (last year with OpenAI's O1 model), focuses on scaling [[reinforcement_learning_in_large_language_models | reinforcement learning]] on [[chain_of_thought_reasoning_in_ai | Chain of Thought]] for highly complex reasoning <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. The effectiveness of this approach stems from the model learning *how to think* during training, leveraging strong signals from [[reinforcement_learning_in_large_language_models | RL]] feedback <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.

To tackle increasingly difficult tasks, such as solving medical problems, models need to dedicate significant time to thinking through the problem <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. This paradigm involves creating more complex environments where models can use tools to think through and verify their outputs during the [[chain_of_thought_reasoning_in_ai | Chain of Thought]] process <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.

Research challenges related to [[chain_of_thought_reasoning_in_ai | Chain of Thought]] include measuring its faithfulness and enabling models to backtrack if they follow a wrong direction <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.

#### New Interaction Paradigms

This shift necessitates new interaction paradigms with humans <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. To avoid long waiting times (e.g., 15 seconds to 30 minutes for a model response), one approach is to stream the model's thoughts to the user, requiring clear summaries of these thoughts <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

### The Future of Agents and Co-Innovation

The current year (in context of the talk) is considered the "year of agents" for OpenAI, focusing on highly complex reasoning, such as models trained on [[layered_chain_of_thought_for_robust_ai | Layered Chain of Thought for robust AI]] utilizing real-world tools like browsing, search, and computer use over long horizons <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

The next stage envisions agents as "co-innovators" <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. This builds upon existing reasoning and tool use capabilities, adding creativity enabled by human-AI collaboration <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. The goal is to create new affordances for humans to collaborate with AI, co-creating the future <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.

### Product Development and Design Challenges

These scaling paradigms have accelerated product research and development <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.
A rapid evaluation cycle is possible by:
*   Using highly reasoning models to distill knowledge into smaller, faster-iterating models <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   Employing complex reasoning models to synthetically generate new data for post-training and [[reinforcement_learning_in_large_language_models | reinforcement learning]] environments <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.

This enables the creation of new classes of tasks, such as simulating different users for multiplayer human-AI collaboration <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.

#### Design Challenges and Product Learnings:

*   **Familiarity for new capabilities**: Bringing unfamiliar capabilities into familiar form factors (e.g., 100K context via file uploads instead of infinite chats) <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.
*   **Modular Compositions**: Designing product features that enable modular compositions that scale with increasing model capabilities, exemplified by "Chach tasks" that can go beyond reminders to continuous story generation or daily searches <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.
*   **Bridging Real-time and Asynchronous Tasks**: Addressing the challenge of models performing long-duration tasks (e.g., 10 hours of research) while maintaining human trust <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>. This can be solved by giving humans new collaborative affordances to verify, edit, and provide real-time feedback for model [[selfimprovement_and_reasoning_in_ai_agents | self-improvement]] <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.
*   **Virtual Teammates**: Early products like "Clau and Slack" explored virtual teammates, offering insights into multiplayer collaboration with tools and image uploads <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.
*   **Flexible Interfaces (Canvas)**: Products like Canvas demonstrate how human collaborative affordances can scale and foster creative capabilities <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>. Canvas operates as a co-creator and co-editor, capable of fine-grain editing, performing search to generate reports, and allowing human verification of outputs <a class="yt-timestamp" data-t="00:17:38">[00:17:38]</a>. This interface scales to multiplayer and multi-agent scenarios, where models can act as critics or editors <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>.

#### Future Applications

*   **Personalized Tutors**: Models are becoming highly multimodal and flexible, adapting to individual learning styles (e.g., visual vs. auditory learners) <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>.
*   **Generative Entertainment**: Models can create games and tools on the fly, enabling non-coders to develop and deploy their own applications or even start businesses, moving towards [[decision_intelligence_and_pair_programming_with_ai | pair programming]] and code creation <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>. Canvas, for example, functions as a pair programmer, capable of writing and coding, searching API documentation, and performing real-time data analysis with CSV uploads <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.
*   **AI for Research and Knowledge Creation**: Models can assist in research by reproducing papers or open-source GitHub repositories <a class="yt-timestamp" data-t="00:20:12">[00:20:12]</a>. Humans and AI can collaborate to form new research hypotheses, verify directions, and delegate tasks to AI assistants <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>.
*   **Invisible Software Creation**: The future may involve seamless software creation for all, especially on mobile devices <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>.
*   **Changing Internet Access**: Predictions suggest less clicking on internet links, with models acting as a cleaner, more personalized lens to access information, generating multimodal outputs like interactive 3D visualizations for learning <a class="yt-timestamp" data-t="00:21:56">[00:21:56]</a>.
*   **Dynamic AI Interfaces**: The AI interface could be a blank canvas that morphs based on user intent (e.g., becoming an IDE for coding or generating tools for writers) <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>.
*   **Co-direction and Superhuman Tasks**: Co-innovation will involve co-direction with models through collaboration with highly reasoning agentic systems, capable of superhuman tasks to create new novels, films, games, and scientific knowledge <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>.