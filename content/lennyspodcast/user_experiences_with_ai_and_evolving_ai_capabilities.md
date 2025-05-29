---
title: User experiences with AI and evolving AI capabilities
videoId: IxkvVZua28k
---

From: [[lennyspodcast]] <br/> 

The landscape of product development is undergoing a significant transformation due to the rapid evolution of artificial intelligence (AI). Product managers (PMs) and engineers are navigating a new era where the underlying technology changes at an unprecedented pace, challenging traditional product development instincts and user experience design principles <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

## Unique Challenges in AI Product Development

Unlike conventional product development built upon a fixed technology base, AI product development faces a constantly shifting foundation. Every two months, computers gain capabilities previously unseen in history, requiring continuous adaptation of product strategies <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. This rapid advancement means that AI companies are often disrupted from within by their own technological breakthroughs <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

A major challenge is the unpredictable emergence of AI capabilities. When training new models, even research teams don't definitively know what new capabilities might manifest or their level of accuracy (e.g., 60% vs. 99% good), which significantly impacts product design <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. Product development instincts, honed over years of building for predictable technology, apply primarily to the final stages of shipping a product, not the uncertain early phases of AI development <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

## The Critical Role of Evaluations (Evals)

In this dynamic environment, "evals" (evaluations) are becoming a core skill for product managers <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.
<br>
> [!quote] "I actually think it's going to become a core skill for PMs" <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>
<br>
Evals define what success looks like for an AI model and help identify where models are underperforming <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>. Often, models are not intelligence-limited but eval-limited, meaning they have more capability than is currently being utilized or measured <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.

Developing strong eval skills requires:
*   **Leveraging AI Models Themselves**: Models can help generate good eval examples and explain what constitutes a good eval <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.
*   **Data-Driven Insights**: Deeply examining the actual output of models, including failures, is crucial. Sometimes, what appears to be a model's failure might be an issue with the evaluation criteria itself <a class="yt-timestamp" data-t="00:16:28">[00:16:28]</a>.
*   **Adapting to Ambiguity**: As models handle more complex, ambiguous, and "agentic" tasks (e.g., booking a hotel), evals will need to become "softer" and more nuanced, akin to performance reviews assessing whether a model "met, exceeded, or greatly exceeded" human expectations <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.

## User Experience in a Non-Deterministic World

AI products introduce a fundamental shift in user experience: non-determinism. Unlike traditional software where the same inputs yield the same outputs, AI models can produce varied responses to identical prompts <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>. This challenges decades of user intuition built on predictable computer interactions <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>.

Designing for this "stochastic" (randomly determined) nature requires:
*   **Human in the Loop**: When a model is only 60% successful at a task, the product must be designed to anticipate human intervention <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. For example, [[the_evolution_of_software_development_with_ai | GitHub Copilot]], despite being built on older, less perfect models, was valuable because it could get code "a significant fraction of the way there," allowing users to edit and complete it <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
*   **Graceful Failure**: Products need to incorporate mechanisms for graceful failure, enabling the model to understand when it lacks confidence and prompt the user for assistance, thereby increasing combined human-model success rates <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.
*   **Prototyping with Models**: Product managers are using AI models to rapidly prototype user interfaces and test different design ideas <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>.
*   **Deeper Technical Understanding**: Product managers must gain a deeper appreciation for the technical stack and how AI models work to effectively design products around their unique behaviors <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>.

Despite these challenges, users adapt to new AI experiences remarkably fast <a class="yt-timestamp" data-t="00:23:13">[00:23:13]</a>. What seems like magic one day (e.g., a Waymo ride or early ChatGPT) quickly becomes commonplace and even "garbage" compared to newer, more advanced iterations <a class="yt-timestamp" data-t="00:23:54">[00:23:54]</a>.

### [[interactions_and_implications_of_ai_in_enterprise_settings | Enterprise AI Adoption]]
[[interactions_and_implications_of_ai_in_enterprise_settings | Enterprise settings]] present unique user education challenges compared to consumer products. While consumer AI initially appeals to early adopters, [[interactions_and_implications_of_ai_in_enterprise_settings | enterprise deployments]] reach a wider range of users, including non-technical individuals <a class="yt-timestamp" data-t="00:26:14">[00:26:14]</a>. Education strategies involve:
*   **Product as Educator**: AI products can directly inform users about their features and how to use them, providing documentation links and step-by-step assistance <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>.
*   **Power User Evangelism**: Identifying internal power users who are enthusiastic to teach others and enabling them to create custom AI tools (e.g., custom GPTs) can drive adoption <a class="yt-timestamp" data-t="00:26:43">[00:26:43]</a>.

## [[future_expectations_and_development_trends_in_ai | Future of AI Interactions]]

The [[future_expectations_and_development_trends_in_ai | future of AI]] promises experiences characterized by:

### Proactivity
Models will become more proactive, monitoring user information (with authorization) to offer timely assistance. Examples include:
*   Providing recaps of daily activities <a class="yt-timestamp" data-t="00:34:03">[00:34:03]</a>.
*   Preparing research for upcoming meetings <a class="yt-timestamp" data-t="00:34:09">[00:34:09]</a>.
*   Drafting presentations based on user's calendar or documents <a class="yt-timestamp" data-t="00:34:14">[00:34:14]</a>.

### Asynchronous Interaction
Models will perform longer, more complex tasks in the background, allowing users to attend to other activities and receive notification upon completion. This moves beyond immediate answer expectations to "mini project plans" where AI can "flesh out" ideas or adapt documents based on new conditions <a class="yt-timestamp" data-t="00:34:21">[00:34:21]</a>.

### Multimodal and [[the_concept_and_potential_of_ai_agents | Agentic Capabilities]]
AI will increasingly interact in all the ways humans do, including speech, vision, and more sophisticated reasoning.
*   **Advanced Voice Mode**: Enables universal translation for real-time conversations, breaking down language barriers for travel and business <a class="yt-timestamp" data-t="00:35:54">[00:35:54]</a>.
*   **Reasoning Models (e.g., O1)**: These models go beyond "system one" fast thinking (text completion) to "system two" slow thinking, pausing to form hypotheses, refute them, and continuously reason, similar to how humans solve complex problems or make scientific breakthroughs <a class="yt-timestamp" data-t="00:30:50">[00:30:50]</a>. This is a new way to scale intelligence, with current capabilities comparable to the early stages of generative AI <a class="yt-timestamp" data-t="00:31:49">[00:31:49]</a>.
*   **Orchestration of Models**: Complex tasks will be handled by workflows where different models, specialized for certain tasks (e.g., reasoning, precision), work in concert, checking each other's outputs and adapting as needed <a class="yt-timestamp" data-t="00:29:36">[00:29:36]</a>. This mirrors how diverse human skill sets collaborate on complex tasks <a class="yt-timestamp" data-t="00:33:04">[00:33:04]</a>.

## The Evolving Human-AI Relationship

A surprising aspect of user experience with AI is the development of a relationship between users and the models <a class="yt-timestamp" data-t="00:38:45">[00:38:45]</a>. Users begin to understand the "nuance" and "personality" of different models, developing a sense of empathy with them <a class="yt-timestamp" data-t="00:38:55">[00:38:55]</a>. This includes observing the model's "behavior" and even "befriending" it <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a>.

This growing bond means:
*   **Model Personality is Key**: The distinct personality of an AI model becomes a critical aspect of the product, influencing user preference, much like human friendships <a class="yt-timestamp" data-t="00:39:43">[00:39:43]</a>.
*   **Personalization**: Models that can understand a user's past interactions and reflect on their "relationship" with the user (e.g., describing what it knows about the user) further blur the lines between tool and entity <a class="yt-timestamp" data-t="00:40:16">[00:40:16]</a>.

Younger, "AI-native" generations, like 14-year-olds, already expect AI to interact in ways that surprise older generations, often "pouring their heart out" to voice modes and having complex, creative interactions <a class="yt-timestamp" data-t="00:37:09">[00:37:09]</a>. This generation views AI as capable of fulfilling complex, real-time creative demands, such as generating stories with specific characters and settings on the fly <a class="yt-timestamp" data-t="00:38:13">[00:38:13]</a>.