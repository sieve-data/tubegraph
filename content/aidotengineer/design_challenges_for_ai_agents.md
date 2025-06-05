---
title: Design challenges for AI agents
videoId: 1XvN5EBDnDw
---

From: [[aidotengineer]] <br/> 

Karina, an AI researcher at OpenAI, discussed the scaling paradigms in AI research over the past two to four years and the new frontiers they have unlocked in product research. She also shared insights into the [[challenges_in_developing_ai_agents | design challenges]] encountered during the development of products like Claude and ChatGPT, and her vision for the future of AI agents as co-innovators <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Scaling Paradigms and Emerging Challenges

Two primary scaling paradigms have dominated AI research recently:

### Next Token Prediction (Pre-training)
This paradigm, often referred to as pre-training, enables models to build a "world understanding" by predicting the next word or token in a sequence <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This process allows models to learn about the physics of the world and perform massive multitask learning <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. While some tasks, like translation, are easy to learn, others present significant [[challenges_in_developing_ai_agents | challenges]]:
*   **Hard-to-Learn Tasks** Scaling compute in the pre-training stage is crucial for tasks that are "really, really hard to learn" <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. These include:
    *   **Math and Computational Tasks** Requires complex reasoning, often necessitating techniques like Chain of Thought to enable the model to compute numbers and reason through problems <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
    *   **Creative Writing** This remains an open-ended research problem and "one of the hardest AI research problems today" <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. The difficulty arises because it's hard to measure what constitutes good creative writing <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>, and models struggle with maintaining plot coherence over long narratives, leading to rapid deterioration <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. The goal is for models to invent new forms of writing and generate extremely creative content <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

### Post-training (RLHF/RLAF)
Following pre-training, models undergo post-training using Reinforcement Learning from Human Feedback (RLHF) and Reinforcement Learning from AI Feedback (RLAF) <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. This stage teaches models to complete specific functions like understanding docstrings, generating multi-line completions, and predicting/applying diffs <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

### Scaling Reinforcement Learning on Chain of Thought
The latest paradigm, introduced with OpenAI's GPT-4, involves scaling reinforcement learning on Chain of Thought <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. This allows models to learn how to "think" during training by receiving good feedback signals, leading to highly complex reasoning <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.

A key [[challenges_in_developing_ai_agents | challenge]] in this area is:
*   **Faithfulness in Chain of Thought** Significant scientific work is needed to measure the faithfulness of a model's Chain of Thought <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. This includes understanding what happens if a model pursues a wrong direction and if it can backtrack itself to correct errors <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

## Specific Design Challenges for AI Agents

As model capabilities and interaction paradigms evolve, new [[challenges_in_developing_ai_agents | design challenges]] emerge <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>:

### Human-AI Interaction Paradigms
*   **Managing Wait Times** A significant [[challenges_in_developing_ai_agents | design challenge]] is creating new interaction paradigms where humans don't have to wait extended periods (e.g., 15 seconds or 30 minutes) for a model's response <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. One simple approach implemented is streaming model thoughts to the user <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Familiar Form Factors for New Capabilities** Bringing unfamiliar AI capabilities into familiar user interfaces is a [[challenges_in_developing_ai_agents | design challenge]] <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. For instance, the success of Claude's 100K context was partly due to integrating it via familiar file uploads, rather than less intuitive infinite chats <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>. Product features should enable modular compositions that scale well with future model capabilities <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.

### Bridging Real-time and Asynchronous Tasks
*   **Building Trust** A major [[challenges_in_building_reliable_ai_agents | challenge]] is bridging real-time interaction with asynchronous task completion, where a model might research or write code for hours before returning a solution <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>. The core bottleneck here is **trust** <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>. This can be addressed by providing humans with new collaborative affordances to verify and edit model outputs, and by enabling real-time feedback for model self-improvement <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.

### Multi-agentic and Multiplayer Collaboration
*   **Navigating Complex Interactions** A new [[challenges_in_developing_ai_agents | design challenge]] involves scaling interfaces to support multi-agentic and multiplayer collaboration, where multiple people can join a document or multiple AI agents (e.g., a model critic or editor) can interact simultaneously <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>.

### Creative Co-Innovation and Co-direction
The future vision involves AI agents becoming "co-innovators," blending reasoning, tool use, and long context with creativity, enabled through human-AI collaboration <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. This requires creating new affordances for humans to collaborate more effectively with AI <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. Ultimately, the goal is for co-innovation to occur through "co-direction" with models, leading to new novels, films, games, science, and knowledge creation <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>.

The ability to use highly reasoning models to distill knowledge into smaller, faster models, and to synthetically generate new data for post-training and reinforcement learning environments, creates a rapid iteration cycle for product development <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>. This also enables the creation of new classes of tasks, such as simulating different users for multiplayer collaboration <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.