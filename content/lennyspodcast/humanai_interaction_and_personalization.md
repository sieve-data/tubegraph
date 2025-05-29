---
title: HumanAI interaction and personalization
videoId: IxkvVZua28k
---

From: [[lennyspodcast]] <br/> 

The development of AI products presents unique challenges and opportunities, particularly in how humans interact with these evolving systems and how products are personalized. Unlike traditional software development, AI's underlying technology is constantly shifting, requiring a different approach to product design and user education <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>.

## The Evolving Nature of AI Products

Building products with AI is distinct because the technology base is not fixed; computers can do something new every two months that they've never been able to do before <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>. This rapid [[the_evolving_landscape_of_ai_technology | evolving landscape of AI technology]] means product strategy must constantly adapt <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>. This internal disruption can even upend product roadmaps <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>.

The development process often involves "peering through the mist" to anticipate capabilities, as models exhibit emergent properties during training <a class="yt-timestamp" data-t="06:31:00">[06:31:00]</a>. Researchers themselves may not know the full extent of a model's abilities or how successful it will be at a given task (e.g., 60% vs. 99% good) <a class="yt-timestamp" data-t="06:44:00">[06:44:00]</a>. This means planning is less predictable, and the iteration cycle involves discovering new functionalities alongside research teams <a class="yt-timestamp" data-t="08:08:00">[08:08:00]</a>. Sometimes, capabilities exist for months before product teams realize their importance <a class="yt-timestamp" data-t="09:55:00">[09:55:00]</a>.

### Designing for Non-Deterministic Systems

AI products are inherently non-deterministic; the same inputs may not always yield the exact same outputs <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>. This goes against decades of user intuition for computers <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>.

This stochastic nature requires new product design principles:
*   **Human-in-the-Loop Design** Even if a model is only 60% successful at a task, it can still be valuable if the product is designed to expect human intervention <a class="yt-timestamp" data-t="10:52:00">[10:52:00]</a>. Tools like GitHub Copilot demonstrated this, saving significant typing time even if the code wasn't perfect <a class="yt-timestamp" data-t="11:02:00">[11:02:00]</a>. The combination of human and model can achieve much higher success rates than the model alone <a class="yt-timestamp" data-t="12:05:00">[12:05:00]</a>.
*   **Understanding Confidence** Models that can express their confidence (e.g., "I'm not sure about this, can you help?") allow for better human-AI collaboration <a class="yt-timestamp" data-t="11:57:00">[11:57:00]</a>.
*   **Feedback Mechanisms** Product design must incorporate robust feedback mechanisms to understand when the model goes "astray," collect rapid feedback, and implement guardrails <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>.

## Core Skills for Product Managers

The role of a Product Manager (PM) in AI is increasingly merging with that of a researcher, particularly in evaluating and optimizing model performance <a class="yt-timestamp" data-t="14:55:00">[14:55:00]</a>.

### The Importance of Evals and Prompt Engineering
Evaluating models (evals) is critical, as models today are often "eval-limited" rather than "intelligence-limited" <a class="yt-timestamp" data-t="13:15:00">[13:15:00]</a>. They can do more if properly taught specific topics <a class="yt-timestamp" data-t="13:23:00">[13:23:00]</a>.

*   **Writing Evals:** This is becoming a core skill for PMs <a class="yt-timestamp" data-t="14:38:00">[14:38:00]</a>. It involves defining what success looks like for a task and iteratively improving model performance <a class="yt-timestamp" data-t="13:49:00">[13:49:00]</a>. Models themselves can assist in writing good evals <a class="yt-timestamp" data-t="16:06:00">[16:06:00]</a>.
*   **Prompt Engineering:** The quality of an AI feature is now "gated on how well you have done the evals and the prompts" <a class="yt-timestamp" data-t="15:20:00">[15:20:00]</a>.
*   **Data Analysis:** Building intuition means "looking at the data," observing failure cases, and understanding that even "golden answers" for evals might be flawed <a class="yt-timestamp" data-t="16:28:00">[16:28:00]</a>.

### [[Prototyping_and_building_with_ai_tools | Prototyping and Building with AI Tools]]
PMs are increasingly using models directly to rapidly prototype and evaluate UI designs or different approaches, significantly accelerating the development cycle <a class="yt-timestamp" data-t="19:05:00">[19:05:00]</a>.

### Deeper Technical Understanding
PMs will be pushed to go deeper into the tech stack, gaining an appreciation for how AI models work and learning their language <a class="yt-timestamp" data-t="19:46:00">[19:46:00]</a>.

## User Adaptation and Education

People adapt incredibly quickly to new, magical technologies <a class="yt-timestamp" data-t="23:13:00">[23:13:00]</a>. What seems mind-blowing one year (e.g., GPT-3.5) feels primitive just two years later <a class="yt-timestamp" data-t="24:00:00">[24:00:00]</a>. This rapid adaptation allows for continuous evolution of AI products.

### Educating End Users
AI products are becoming more educational, with models like Claude able to explain their own features and provide documentation links, helping users understand how to interact with them <a class="yt-timestamp" data-t="24:53:00">[24:53:00]</a>.

### [[Enterprise_adoption_of_ai_technologies | Enterprise Adoption of AI Technologies]]
In [[enterprise_adoption_of_ai_technologies | enterprise settings]], AI often reaches non-technical users. This requires structured educational materials and sessions <a class="yt-timestamp" data-t="26:19:00">[26:19:00]</a>. Power users within organizations often become evangelists, creating custom models (e.g., custom GPTs) to make AI immediately valuable for less technical colleagues <a class="yt-timestamp" data-t="26:50:00">[26:50:00]</a>. This is particularly relevant for automating "drudgery" tasks like UI testing and data manipulation within organizations <a class="yt-timestamp" data-t="28:57:00">[28:57:00]</a>.

## The Future of Human-AI Interaction

### Proactivity and Asynchronous Interaction
Future AI experiences will be more proactive, anticipating user needs and providing relevant information or drafting content without explicit prompts <a class="yt-timestamp" data-t="33:50:00">[33:50:00]</a>. They will also be more asynchronous, allowing users to initiate complex tasks and return later for the results, breaking free from the expectation of immediate answers <a class="yt-timestamp" data-t="34:21:00">[34:21:00]</a>.

### Multimodal Interaction and [[the_concept_of_agents_in_ai_and_product_design | Agents]]
Models will interact with humans in all the ways humans interact with each other: not just typing, but speaking, seeing, and more <a class="yt-timestamp" data-t="35:38:00">[35:38:00]</a>. Real-time translation, like advanced voice mode, can remove language barriers for travel and business <a class="yt-timestamp" data-t="35:57:00">[35:57:00]</a>.

The shift towards [[the_concept_of_agents_in_ai_and_product_design | agents]] and longer-form tasks means AI can tackle more complex, multi-step projects, even if not perfectly, by saving users time and understanding where human help is needed <a class="yt-timestamp" data-t="11:45:00">[11:45:00]</a>. This involves models pausing to "think" and reason, forming hypotheses, and refining answers over time, similar to human problem-solving <a class="yt-timestamp" data-t="31:01:00">[31:01:00]</a>.

### Personalization and Relationship
The "personality" of AI models is a key product consideration, with questions arising about how much AI should customize itself for individual users versus maintaining a distinct persona <a class="yt-timestamp" data-t="39:46:00">[39:46:00]</a>. Users are starting to develop a "two-way empathy" with models, understanding their nuances and even forming relationships, similar to how people prefer certain human friends <a class="yt-timestamp" data-t="38:57:00">[38:57:00]</a>. Models responding to user questions like "based on everything you know about me... what would you say about me?" highlights this evolving personal interaction <a class="yt-timestamp" data-t="40:19:00">[40:19:00]</a>.