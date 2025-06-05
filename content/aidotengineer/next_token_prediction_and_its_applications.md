---
title: Next token prediction and its applications
videoId: 1XvN5EBDnDw
---

From: [[aidotengineer]] <br/> 

Next token prediction is a foundational scaling paradigm in [[AI industry trends and challenges | AI research]] that has profoundly influenced the development of new frontiers in product research <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Core Concept: The World-Building Machine

The first major scaling paradigm in AI research over the past few years is next token prediction, often referred to as pre-training <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   **Fundamental Mechanism**: It functions as a "world-building machine" where the model learns to comprehend the world by anticipating the subsequent word or token in a sequence <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. This is based on the principle that certain sequences are caused by initial actions and are irreversible <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   **Token Flexibility**: Tokens can represent various data types, including strings, words, or pixels <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. To predict what comes next, the model must develop an understanding of how the world operates <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

## Next Token Prediction as Multitask Learning

Next token prediction can be viewed as massive multitask learning <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
*   **Easy Tasks**: Some tasks, like translation, are relatively easy for the model to learn during pre-training <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. Models also readily acquire world knowledge, such as geographical capitals, due to the prevalence of such information online <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Hard Tasks and Compute Importance**: A crucial reason for scaling compute in the pre-training stage is the existence of tasks that are inherently difficult for models to learn <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. These include:
    *   **Physics Understanding and Problem Solving**: Learning physics, problem-solving, generation, and logical expressions <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
    *   **Mathematical Computation**: Complex mathematical computations during next token prediction are very demanding, often necessitating [[advancements_in_ai_model_technology_and_performance | Chain of Thought]] reasoning to assist the model <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
    *   **Creative Writing**: This is exceptionally challenging because while style can be predicted, the coherence of world-building, storytelling, and plot is difficult to maintain without errors <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. Measuring "good" creative writing is also an open-ended research problem, with the goal for models to invent new forms of writing and maintain long-term coherent stories <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

## Eras of AI Scaling and Product Development

### Era of Scaling Pre-training (2020-2021)
This period saw significant scaling of pre-training at organizations like Anthropic and OpenAI <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **GitHub Copilot**: One of the first products to emerge from this era was GitHub Copilot <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. Its autocomplete functionality leveraged the model's extensive learning about code and next token prediction from billions of code tokens <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.

### Post-Training and Reinforcement Learning
To make products like GitHub Copilot more useful, researchers constrained the pre-trained models using reinforcement learning from human feedback (RLHF) and reinforcement learning from AI feedback (RLAIF) <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   **Applications**: Post-training teaches models to complete function bodies, understand docstrings, generate multi-line completions, and predict/apply code diffs <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. This area still holds significant potential for advancing models' ability to reason through complex codebases <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### Scaling Reinforcement Learning on Chain of Thought
The next major paradigm shift, marked by OpenAI's '01' model, involves scaling reinforcement learning on Chain of Thought for highly complex reasoning <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   **Mechanism**: This approach invests more compute in training to scale reinforcement learning, allowing the model to learn "how to think" during training and improve from feedback signals in RL <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **Complex Problem Solving**: For harder tasks, like solving medical problems, models need to spend significant time thinking through the problem, creating complex environments with tools to verify their outputs during the Chain of Thought process <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.
*   **Research Challenges**: Key research areas include ensuring the faithfulness of the Chain of Thought and enabling models to backtrack from wrong directions <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   **Interaction Paradigm**: The interaction paradigm changes, with models thinking extensively to solve hard problems <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. Design challenges arise in creating new human-AI interaction methods, such as streaming model thoughts to users, to avoid long waiting times <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

## The Future of Agents: From Collaborators to Co-Innovators

OpenAI views the current era as the "year of agents," defined by highly complex reasoning and the use of real-world tools (browsing, search, computer use) over long horizons <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   **Co-Innovators**: The next stage envisions agents as co-innovators, built upon reasoning, tool use, and long context, but critically adding creativity enabled by human-AI collaboration <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. The goal is to create new affordances for humans to collaborate better with AI, co-creating the future <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.

### Product Research Unlocked by Scaling Paradigms
These two scaling paradigms in [[advancements_in_ai_and_future_implications | AI research]] have unlocked new kinds of product research <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.
*   **Rapid Iteration Cycle**: A rapid evaluation cycle in product development is possible because highly reasoning models can distill knowledge back to smaller models for faster iteration <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.
*   **Synthetic Data Generation**: Complex reasoning models can synthetically generate new data for post-training and new reinforcement learning environments <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
*   **New Task Classes**: This enables the creation of entirely new classes of tasks, such as simulating different users for multiplayer human-AI collaboration <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
*   **Complex RL Environments**: Moving towards more complex reinforcement learning environments allows models to use tools like search, browsing, or collaborative canvases, improving their collaboration skills <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.
*   **In-Context Learning**: Models excel at in-context learning, allowing developers to create new tools with just a few examples for a rapid evaluation cycle <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
*   **New Model Behavior**: It's possible to invent new model behaviors and interactions by utilizing user feedback <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.

## Vignettes and Lessons Learned

### Familiar Form Factor for Unfamiliar Capability
The success of 100K context models (like Claude) was attributed to presenting an unfamiliar capability (massive context) in a familiar form factor, such as file uploads, rather than an infinite chat <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>. This highlights the design challenge of finding the simplest interaction method for new AI capabilities <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.

### Modular Compositions and Scaling Capabilities
*   **ChatGPT Tasks**: This product takes familiar tasks like reminders and scheduling and scales them with new AI capabilities <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. It allows for continuous story generation, daily information searches, or interactive, multimodal language learning <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. The lesson here is that product features should enable modular compositions that scale with advancing model capabilities <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.

### Bridging Real-time Interaction and Asynchronous Task Completion
A design challenge is bridging real-time model interaction with asynchronous task completion, allowing models to work on research or code for extended periods <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.
*   **Trust**: The bottleneck is trust, which can be addressed by giving humans collaborative affordances to verify and edit model outputs, providing real-time feedback for self-improvement <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>.
*   **Claude in Slack**: An early example of a virtual teammate, Claude in Slack, leveraged slack's existing tools and collaborative features for functions like channel summaries <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.

### Human Collaborative Affordances and Creativity
*   **Canvas**: This project aimed to scale human collaboration and create new creative capabilities through a flexible interface <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>.
    *   **Features**: Canvas can act as a co-creator and co-editor with fine-grain editing, perform searches for reports, and allow users to verify outputs <a class="yt-timestamp" data-t="00:17:38">[00:17:38]</a>.
    *   **Multiplayer/Multi-Agent**: The interface scales to multiplayer collaboration, and even multi-agent collaboration with model critics or editors <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>.
    *   **Flexible Roles**: Canvas can serve as a pair programmer, trained for both collaborative writing and coding <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>. With tools like search for API documentation and the ability to upload CSV documents, it can also function as a data scientist for real-time analysis <a class="yt-timestamp" data-t="00:19:49">[00:19:49]</a>.

## Future Outlook

### [[applications_and_future_of_ai_technology | Applications and Future of AI Technology]]
*   **Personalized Tutors**: Models are becoming multimodal and flexible enough to adapt to individual learning styles (e.g., visual vs. auditory learners) <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>.
*   **Generative Entertainment**: The ability to generate experiences on the fly, such as creating a game in Canvas, points to a future of generative entertainment where people can create and share new games <a class="yt-timestamp" data-t="00:18:44">[00:18:44]</a>.
*   **Invisible Software Creation for All**: A future where non-coders can create and deploy their own tools or start businesses from scratch, leveraging AI for pair programming and code creation <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.
*   **Changing Internet Interaction**: Interaction with AI will fundamentally change how users access the internet, leading to less clicking on links and more access via a cleaner, more personalized "model's lens" <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>. This includes highly personalized multimodal outputs, like an interactive 3D visualization of the solar system instead of just text <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>.

### The Blank Canvas Interface
The interface to AI is envisioned as a "blank canvas" that self-morphs into the user's intent <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>.
*   **Adaptive Environment**: If the user intends to write code, the canvas transforms into an IDE; if they want to write a novel, it creates tools on the fly for brainstorming, editing, character plotting, and plot visualization <a class="yt-timestamp" data-t="00:22:52">[00:22:52]</a>.

### Co-Innovation and Knowledge Creation
The ultimate goal is co-innovation through creative co-direction with models <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>.
*   **Superhuman Tasks**: Collaboration with highly reasoning agentic systems, capable of superhuman tasks, will lead to the creation of new novels, films, games, and fundamentally, new science and knowledge <a class="yt-timestamp" data-t="00:23:39">[00:23:39]</a>.
*   **Research Reproduction and Hypothesis Generation**: Models can reproduce papers and open-source GitHub repositories <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>. Through interaction and leveraging their internal knowledge, humans and AI can jointly develop new research hypotheses and verify research directions <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>. Tasks can also be delegated to an AI assistant <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a>.