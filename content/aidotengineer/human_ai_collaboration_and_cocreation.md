---
title: Human AI collaboration and cocreation
videoId: 1XvN5EBDnDw
---

From: [[aidotengineer]] <br/> 

AI research has undergone significant [[AI scaling paradigms|scaling paradigms]] in recent years, unlocking new frontiers in product development and fostering new forms of [[collaboration_between_human_engineers_and_ai|human-AI collaboration]] <a class="yt-timestamp" data-t="00:41:00">[00:41:00]</a>. The progression of AI agents from mere collaborators to co-innovators represents a transformative shift in how humans interact with and leverage artificial intelligence <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>.

## Evolution of AI Capabilities
The foundation of modern AI capabilities lies in two primary [[AI scaling paradigms|scaling paradigms]] <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>:

1.  **Next Token Prediction (Pre-training)**: This paradigm involves models learning about the world by predicting the next word, string, pixel, or any token in a sequence <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>. It functions as a "world-building machine," enabling the model to understand the physics of the world and perform massive multitask learning <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>. While some tasks like translation are easy, complex tasks such as math, problem-solving, and especially creative writing require significant compute due to the high risk of coherence deterioration <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>. The era of 2020-2021 saw extensive scaling in pre-training <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>.
2.  **Reinforcement Learning (Post-training)**: This phase, often leveraging [[user_feedback_and_ai_development|Reinforcement Learning from Human Feedback (RLHF)]] or Reinforcement Learning from AI Feedback (RLAF), refines the model's usefulness <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>. Products like GitHub Copilot exemplify this, teaching models to complete function bodies, generate multi-line completions, and predict diffs <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>.
3.  **Scaling Reinforcement Learning on Chain of Thought**: A more recent paradigm involves scaling RL on Chain of Thought, where models learn to "think" during training and receive good feedback signals in RL <a class="yt-timestamp" data-t="07:05:00">[07:05:00]</a>. This allows models to reason through complex problems by creating detailed internal thought processes, enabling them to tackle harder tasks like medical problems or complex codebases <a class="yt-timestamp" data-t="07:45:00">[07:45:00]</a>.

## From Collaborators to Co-innovators
The current stage of AI, particularly models trained with Chain of Thought and real-world tools (browsing, search, computer use) over long horizons, marks the era of "agents" <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>. The next evolutionary stage envisions AI as "co-innovators" <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>.

> [!info] Co-innovators
> Co-innovators are agents built upon advanced reasoning, tool use, and long context, **plus creativity enabled through human-AI collaboration** <a class="yt-timestamp" data-t="10:33:00">[10:33:00]</a>. This is expected to create new affordances for humans to collaborate better with AI, enabling them to co-create the future <a class="yt-timestamp" data-t="10:52:00">[10:52:00]</a>.

## New Interaction Paradigms and Design Challenges
The increased capabilities of AI agents introduce new interaction paradigms and design challenges <a class="yt-timestamp" data-t="09:02:00">[09:02:00]</a>:

*   **Streaming Model Thoughts**: To avoid long waiting times, one simple approach is to stream the model's thoughts to the user, providing summaries of its reasoning <a class="yt-timestamp" data-t="09:31:00">[09:31:00]</a>.
*   **Familiar Form Factors for Unfamiliar Capabilities**: Presenting powerful new capabilities, like 100K context windows, through familiar interfaces such as file uploads, makes them more accessible <a class="yt-timestamp" data-t="13:39:00">[13:39:00]</a>.
*   **Modular Compositions**: Product features should enable modular compositions that can scale with future, higher-capability models <a class="yt-timestamp" data-t="15:21:00">[15:21:00]</a>.
*   **Bridging Real-time and Asynchronous Tasks**: A significant challenge is bridging real-time AI interaction with asynchronous task completion (e.g., models researching for hours) <a class="yt-timestamp" data-t="15:42:00">[15:42:00]</a>. The key bottleneck is trust, which can be addressed by giving humans [[collaboration_between_human_engineers_and_ai|new collaborative affordances]] to verify and edit model outputs, and provide real-time [[user_feedback_and_ai_development|feedback for self-improvement]] <a class="yt-timestamp" data-t="16:00:00">[16:00:00]</a>.

### Vignettes from Product Development

*   **GitHub Copilot**: An early product demonstrating the power of pre-trained models for code completion, refined with RLHF/RLAF for usability <a class="yt-timestamp" data-t="05:38:00">[05:38:00]</a>. This highlights [[integration_of_ai_into_development_environments_and_editors|integrating AI into natural workflows]] for developers.
*   **Anthropic's Claude in Slack**: An early attempt at a virtual teammate in an organization, leveraging Slack's tools and [[multiplayer collaboration|multiplayer collaboration]] features <a class="yt-timestamp" data-t="16:21:00">[16:21:00]</a>. This concept informed later products like ChatGPT tasks <a class="yt-timestamp" data-t="16:53:00">[16:53:00]</a>.
*   **ChatGPT Tasks**: Extends familiar concepts like reminders and to-do lists with new AI capabilities, allowing models to continue stories, perform daily searches, or help learn languages with [[multimodal_ai_and_the_future_of_human_interaction|multimodal and interactive visualizations]] <a class="yt-timestamp" data-t="14:41:00">[14:41:00]</a>.
*   **OpenAI's Canvas**: An extremely flexible interface designed to scale [[collaboration_between_human_engineers_and_ai|human collaborative affordances]] and foster new creative capabilities <a class="yt-timestamp" data-t="17:14:00">[17:14:00]</a>. Canvas can act as a co-creator, co-editor, and even a pair programmer <a class="yt-timestamp" data-t="17:40:00">[17:40:00]</a>. It supports fine-grain editing, search for report generation, and multi-agent [[multiagent_orchestration_for_ai_copilot_development|collaboration (e.g., a model critic or editor)]] <a class="yt-timestamp" data-t="18:03:00">[18:03:00]</a>.

## The Future of [[Multimodal AI and the Future of Human Interaction|Human Interaction]] with AI
The integration of highly reasoning models allows for a rapid evaluation cycle in product development <a class="yt-timestamp" data-t="11:22:00">[11:22:00]</a>. These models can distill knowledge to smaller models, synthetically generate new data for post-training, and create new reinforcement learning environments <a class="yt-timestamp" data-t="11:33:00">[11:33:00]</a>.

Key areas for the future of [[future_of_ai_in_improving_user_experience_and_integrations|AI in improving user experience and integrations]] include:

*   **Creating New Task Classes**: Simulating different users or generating synthetic datasets to create new [[building_user_experiences_with_ai|product experiences]] <a class="yt-timestamp" data-t="11:57:00">[11:57:00]</a>.
*   **Complex RL Environments**: Allowing models to use collaborative tools like canvas, search, or browsing within RL environments to learn better collaboration <a class="yt-timestamp" data-t="12:39:00">[12:39:00]</a>.
*   **In-context Learning**: Models are extremely good at learning new tools from few-shot examples, accelerating development cycles <a class="yt-timestamp" data-t="13:00:00">[13:00:00]</a>.
*   **Personalized Tutors**: Models can adapt to individual learning styles (e.g., visual or auditory) <a class="yt-timestamp" data-t="18:16:00">[18:16:00]</a>.
*   **Generative Entertainment**: Enabling non-technical individuals to create games or tools on the fly <a class="yt-timestamp" data-t="18:47:00">[18:47:00]</a>.
*   **Invisible Software Creation**: The future suggests an invisible layer of software creation where people can create their own tools directly from mobile devices without coding <a class="yt-timestamp" data-t="21:32:00">[21:32:00]</a>.
*   **AI as Research Partner**: Models can assist in research by reproducing papers, leveraging internal knowledge to form new hypotheses, and delegating tasks to AI assistants <a class="yt-timestamp" data-t="20:12:00">[20:12:00]</a>.
*   **Dynamic Interface**: The AI interface will be a "blank canvas" that self-morphs based on user intent, becoming an IDE for coders or a writing assistant with tools for brainstorming and visualization for writers <a class="yt-timestamp" data-t="22:42:00">[22:42:00]</a>.

Ultimately, co-innovation will occur through creative co-direction with highly reasoning agentic systems, leading to the creation of new novels, films, games, science, and knowledge <a class="yt-timestamp" data-t="23:31:00">[23:31:00]</a>.