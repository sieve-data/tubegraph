---
title: Scaling paradigms in AI research
videoId: 1XvN5EBDnDw
---

From: [[aidotengineer]] <br/> 

AI research has witnessed significant advancements in scaling paradigms over the past two to four years, unlocking new frontiers in product research <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## First Scaling Paradigm: Next Token Prediction (Pre-training)

The first major scaling paradigm is **Next Token Prediction**, often referred to as **pre-training** <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Core Concept
Next token prediction functions as a "world-building machine" <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. The model learns to comprehend the world by predicting the subsequent word or token in a sequence <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. This process leverages the inherent irreversibility of sequences caused by initial actions, allowing the model to learn fundamental "physics of the world" <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. Tokens can be diverse, including strings, words, or pixels <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### Multitask Learning
Pre-training embodies massive multitask learning <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. During this stage, some tasks are easily learned, such as translation (e.g., "boarding" in French) and factual knowledge (e.g., "the capital of France is Paris") due to their prevalence in internet data <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

However, a class of tasks is exceptionally difficult to learn, necessitating significant computational resources for scaling during the pre-training phase <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. These include:
*   **Physics, Problem Solving, Generation, and Logical Expressions**: Models learn complex aspects of these areas <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   **Spatial Reasoning**: While not perfect, models learn some spatial reasoning <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Mathematics**: Computing numbers during next token prediction for math tasks is computationally intensive, often requiring [[Evolution of AI models and their application | Chain of Thought]] reasoning for better performance <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
*   **Creative Writing**: This is a particularly challenging area because while models can predict writing style, creative writing involves world-building, storytelling, and plot coherence <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. Mistakes in next token prediction can quickly deteriorate plot coherence <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. Evaluating "good" creative writing is an open research problem, with the goal of models inventing new forms of writing and maintaining coherent stories over long periods <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. This highlights a significant [[Challenges in AI Development | challenge in AI development]] <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

### Era of Pre-training (2020-2021)
The period from 2020 to 2021 was characterized by extensive scaling of pre-training at organizations like Anthropic and OpenAI <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. A notable product from this era was GitHub Copilot, an autocomplete tool <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. The model's deep understanding of code from billions of code tokens enabled this capability <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. Reinforcement Learning from Human Feedback (RLHF) and Reinforcement Learning from AI Feedback (RLAF) were applied in a "post-training" stage to enhance its usefulness <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. This post-training phase focuses on teaching models to complete function bodies, understand docstrings, generate multi-line completions, and predict/apply diffs <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

## Second Scaling Paradigm: Scaling Reinforcement Learning on Chain of Thought

The second paradigm, emerging more recently (last year, published by OpenAI with the 01 model), involves **scaling reinforcement learning on [[Evolution of AI models and their application | Chain of Thought]]** <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. This enables highly complex reasoning <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

### How it Works
This approach involves significantly more test-time compute during training to scale reinforcement learning <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. The model learns *how to think* during training and improves from feedback via strong RL signals <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. For increasingly difficult tasks, such as solving medical problems, models need to dedicate substantial time to thinking through the problem <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. This often involves creating more complex environments with [[Tool Usage and Development in AI Frameworks – Link name: tool_usage_and_development_in_ai_frameworks | tools]] to verify outputs during the [[Evolution of AI models and their application | Chain of Thought]] process <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.

### Challenges in Chain of Thought
Despite its power, [[Evolution of AI models and their application | Chain of Thought]] presents [[Challenges in AI Development | challenges]] <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>:
*   **Faithfulness**: Measuring the faithfulness of the Chain of Thought is a key research area <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
*   **Backtracking**: Enabling models to backtrack if they pursue a wrong direction is crucial <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

### New Interaction Paradigms
This paradigm necessitates new human-AI interaction models. One solution to prevent long wait times for complex problems (15 seconds to 30 minutes) is to stream the model's thoughts to the user, communicating summaries of its reasoning <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. This introduces new [[Challenges in AI Development | design challenges]] as model capabilities and interaction paradigms evolve <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.

## Future of AI: From Collaborators to Co-Innovators

The current year (2024) is seen as the "year of agents" <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. These agents exhibit highly complex reasoning, trained on RL and [[Evolution of AI models and their application | Chain of Thought]], and utilize real-world [[Tool Usage and Development in AI Frameworks – Link name: tool_usage_and_development_in_ai_frameworks | tools]] like browsing, search, and computer use over long horizons <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

The next stage envisions **co-innovators** <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. These agents build upon current reasoning, [[Tool Usage and Development in AI Frameworks – Link name: tool_usage_and_development_in_ai_frameworks | tool use]], and long context capabilities, adding **creativity** enabled by human-AI collaboration <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. The aim is to create new affordances for humans to collaborate effectively with AI, fostering co-creation of the future <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.

## Impact on Product Research and Development

These two scaling paradigms have significantly transformed product research <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.
*   **Rapid Evaluation Cycle**: A rapid evaluation cycle for product development is now possible <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.
*   **Model Distillation**: Highly reasoning models can distill their knowledge back into smaller, faster-iterating models <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Synthetic Data Generation**: Complex reasoning models can synthetically generate new data, enabling the creation of new post-training datasets and reinforcement learning environments <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
*   **New Classes of Tasks**: This allows for creating entirely new classes of tasks, such as simulating different users for multiplayer human-AI collaboration <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
*   **Complex RL Environments**: The shift is towards more complex reinforcement learning environments where models can use search, browsing, or collaborative [[Tool Usage and Development in AI Frameworks – Link name: tool_usage_and_development_in_ai_frameworks | tools]] like canvas to enhance their collaboration skills <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.
*   **In-context Learning**: Models are highly proficient at in-context learning, allowing developers to create new tools with just a few shot examples, accelerating development cycles <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
*   **New Model Behaviors**: Models can invent new behaviors and interactions by leveraging user feedback <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.

### Lessons Learned and Design Challenges

Experience from Anthropic and OpenAI products like Claude and ChatGPT illustrates key lessons and [[Challenges in AI Development | design challenges]] <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>:

*   **Familiar Form Factors for Unfamiliar Capabilities**: Presenting new AI capabilities within familiar interfaces (e.g., 100K context with file uploads rather than infinite chats) helps user adoption <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>. This is a crucial [[Challenges in AI Development | design challenge]] in this new era <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.
*   **Modular Compositions**: Product features should enable modular compositions that scale with evolving model capabilities. ChatGPT tasks, for instance, can schedule reminders, continue stories, or perform daily searches, demonstrating how familiar tasks can scale with new AI capabilities <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.
*   **Real-time vs. Asynchronous Interaction**: Bridging real-time model interaction with asynchronous task completion (e.g., a model researching for hours and then returning with a solution) is a [[Challenges in AI Development | challenge]] <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>. The bottleneck is **trust** <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>. This can be addressed by giving humans collaborative affordances to verify and edit model outputs, and by providing real-time feedback for self-improvement <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.
*   **Virtual Teammates**: Early projects like Claude in Slack demonstrated the concept of a virtual teammate, leveraging Slack's [[Tool Usage and Development in AI Frameworks – Link name: tool_usage_and_development_in_ai_frameworks | tool]] integrations, image uploads, and multiplayer collaboration <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>. Claude could summarize channels weekly for organizational insights <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>.
*   **Canvas as a Co-creator**: OpenAI's Canvas project highlighted how human-AI collaborative affordances can scale and foster creative capabilities <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>. Canvas provides a flexible interface for:
    *   Fine-grain editing <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>.
    *   Model-driven search for report generation <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>.
    *   Verification of outputs <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.
    *   Multiplayer collaboration (others joining documents) and multi-agent systems (e.g., model as a critic or editor) <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>.
*   **Personalized Tutors**: AI models are becoming highly [[Multimodal AI Systems | multimodal]] and flexible, capable of adapting to individual learning styles (e.g., visual vs. auditory learners) <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>.
*   **Generative Entertainment**: The ability for AI to create interactive games or entertainment on the fly <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>.
*   **Invisible Software Creation for All**: A future where non-coders can create and deploy their own [[Tool Usage and Development in AI Frameworks – Link name: tool_usage_and_development_in_ai_frameworks | tools]] and web apps, potentially enabling new businesses <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>. Pair programming and code creators will be instrumental <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>. Canvas, for example, functions as a pair programmer, capable of writing and coding, searching API documentation, and acting as a data scientist by analyzing CSV data in real-time <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.
*   **AI for Research and Knowledge Creation**: AI can assist in research by reproducing papers or open-source GitHub repositories <a class="yt-timestamp" data-t="00:20:12">[00:20:12]</a>. The interactive paradigm allows humans and AI to co-create documents, generate new research hypotheses, verify directions, and delegate tasks <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>.

## Future of AI Interaction and Co-Innovation

The interaction with AI and access to the internet will fundamentally change <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>. Users will click less on links, accessing information via AI model lenses for a cleaner, more personalized experience <a class="yt-timestamp" data-t="00:21:56">[00:21:56]</a>. This includes highly personalized [[Multimodal AI Systems | multimodal]] outputs, such as interactive 3D visualizations instead of text for topics like the solar system <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>.

The interface to AI is envisioned as a "blank canvas" that self-morphs based on user intent <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>. For a coder, it becomes an IDE; for a writer, it generates [[Tool Usage and Development in AI Frameworks – Link name: tool_usage_and_development_in_ai_frameworks | tools]] on the fly for brainstorming, editing, or visualizing plot structures <a class="yt-timestamp" data-t="00:22:52">[00:22:52]</a>.

Ultimately, **co-innovation** will occur through co-direction with models <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>. Collaboration with highly reasoning, agentic systems capable of superhuman tasks will lead to the creation of new novels, films, games, science, and knowledge <a class="yt-timestamp" data-t="00:23:39">[00:23:39]</a>. This represents the exciting [[Future directions in AI model training and scaling | future direction in AI model training and scaling]] <a class="yt-timestamp" data-t="00:23:49">[00:23:49]</a>.