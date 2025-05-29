---
title: AI model capabilities and evaluation
videoId: IxkvVZua28k
---

From: [[lennyspodcast]] <br/> 

Developing [[ai_in_product_development | AI products]] presents unique challenges compared to traditional software, primarily due to the rapidly [[the_evolving_capabilities_and_future_potential_of_ai | evolving capabilities and future potential of AI]] models and the critical role of robust evaluation systems <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>. The nature of AI models means that every few months, computers can accomplish tasks they never could before, constantly changing the product landscape <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>.

## The Unpredictable Nature of AI Product Development

Unlike traditional product development built on a fixed technology base, [[ai_in_product_development | AI product development]] involves working with emergent properties of models <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>, <a class="yt-timestamp" data-t="06:33:00">[06:33:00]</a>. Developers may train a new model with a sense that it *might* have a certain capability, but they don't truly know its exact performance (e.g., 60%, 90%, or 99% good) until it's developed <a class="yt-timestamp" data-t="06:35:00">[06:35:00]</a>, <a class="yt-timestamp" data-t="06:55:00">[06:55:00]</a>. This uncertainty means that the product design must adapt significantly depending on the model's actual performance <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>.

Research teams themselves often don't know the full extent of a model's capabilities, leading to instances where a team might discover an existing, powerful capability that was overlooked because its importance wasn't initially recognized <a class="yt-timestamp" data-t="09:55:00">[09:55:00]</a>, <a class="yt-timestamp" data-t="10:03:00">[10:03:00]</a>. This internal "disruption from within" can shift product roadmaps significantly <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>, <a class="yt-timestamp" data-t="07:59:00">[07:59:00]</a>.

## Designing Products for Imperfect Models

A key challenge in [[ai_product_development_and_prototyping | AI product development and prototyping]] is building valuable experiences even when models are not 99% successful at a task <a class="yt-timestamp" data-t="10:18:00">[10:18:00]</a>. Many useful applications can be built with models that are only 60% accurate, provided the product is designed to anticipate human intervention <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>, <a class="yt-timestamp" data-t="10:56:00">[10:56:00]</a>.

For example, GitHub Co-pilot, an early [[ai_in_product_development | AI product]], was valuable even when built on older, imperfect models (like GPT-2) because it saved developers significant typing time and allowed for easy editing <a class="yt-timestamp" data-t="11:02:00">[11:02:00]</a>, <a class="yt-timestamp" data-t="11:15:00">[11:15:00]</a>. Similarly, for agents and longer-form tasks, an AI that saves five or ten minutes, even if not perfect, is still valuable <a class="yt-timestamp" data-t="11:48:00">[11:48:00]</a>, <a class="yt-timestamp" data-t="11:55:00">[11:55:00]</a>. The combination of human and model can achieve much higher success rates if the model can communicate its confidence levels <a class="yt-timestamp" data-t="11:57:00">[11:57:00]</a>.

The performance of models can also be "lumpy," meaning they perform exceptionally well on some tasks while struggling with others <a class="yt-timestamp" data-t="12:21:00">[12:21:00]</a>. Real-world feedback from pilot programs often reveals this variability, with some companies finding a model perfectly solves their problem, while others find it completely off-target <a class="yt-timestamp" data-t="12:27:00">[12:27:00]</a>.

## The Critical Role of Evaluations (Evals)

A major bottleneck in current [[the_evolving_capabilities_and_future_potential_of_ai | AI development]] is not the models' intelligence, but the quality of their evaluations <a class="yt-timestamp" data-t="13:13:00">[13:13:00]</a>. Models can often perform better and be more correct if they are effectively taught specific topics through proper evaluation <a class="yt-timestamp" data-t="13:23:00">[13:23:00]</a>.

Many early [[ai_in_product_development | AI deployments]] focused on shipping cool features without establishing clear evaluation metrics for success <a class="yt-timestamp" data-t="13:36:00">[13:36:00]</a>, <a class="yt-timestamp" data-t="13:41:00">[13:41:00]</a>. Defining what "success" looks like and iteratively improving based on evaluations is crucial <a class="yt-timestamp" data-t="13:47:00">[13:47:00]</a>, <a class="yt-timestamp" data-t="14:09:00">[14:09:00]</a>. AI models like Claude can even assist in writing and grading evaluations, automating a significant part of this process <a class="yt-timestamp" data-t="14:01:00">[14:01:00]</a>, <a class="yt-timestamp" data-t="14:04:00">[14:04:00]</a>.

Writing effective evals is becoming a core skill for Product Managers <a class="yt-timestamp" data-t="14:38:00">[14:38:00]</a>, blurring the lines between research PMs (focused on model capabilities) and product surface PMs (focused on user interfaces) <a class="yt-timestamp" data-t="14:47:00">[14:47:00]</a>, <a class="yt-timestamp" data-t="15:00:00">[15:00:00]</a>. The quality of an AI-powered feature is directly tied to the quality of its evaluations and prompts <a class="yt-timestamp" data-t="15:20:00">[15:20:00]</a>, <a class="yt-timestamp" data-t="15:24:00">[15:24:00]</a>.

To develop intuition for writing good evaluations, one can:
*   Use the models themselves to generate sample evals <a class="yt-timestamp" data-t="16:06:00">[16:06:00]</a>.
*   Examine the actual data and model answers, even if they initially contradict automated evaluation scores <a class="yt-timestamp" data-t="16:28:00">[16:28:00]</a>.
*   Understand that as models perform more ambiguous, long-form, and agentic tasks, evaluations will become "softer" and more nuanced, similar to human performance reviews rather than simple right/wrong answers <a class="yt-timestamp" data-t="17:18:00">[17:18:00]</a>, <a class="yt-timestamp" data-t="18:11:00">[18:11:00]</a>.

### The Role of [[the_role_of_evaluations_evals_in_ai_product_management | evaluations (evals) in AI product management]]

> "Models today are not intelligence limited, they're eval limited." <a class="yt-timestamp" data-t="13:13:00">[13:13:00]</a>

## Evolving [[ai_product_management_and_its_future | AI product management]] Skills

Beyond mastering evaluations, [[ai_powered_product_management_skills | AI-powered product management skills]] require new approaches:
*   **Prototyping with Models**: The best product managers use models for rapid [[ai_product_development_and_prototyping | AI product development and prototyping]], conducting A/B comparisons of UI options through prompting, allowing for faster evaluation of a wider variety of ideas <a class="yt-timestamp" data-t="19:04:00">[19:04:00]</a>, <a class="yt-timestamp" data-t="19:31:00">[19:31:00]</a>.
*   **Deeper Technical Understanding**: Product managers need to go deeper into the technical stack, gaining an appreciation for how the underlying AI models work and learning their language <a class="yt-timestamp" data-t="19:46:00">[19:46:00]</a>, <a class="yt-timestamp" data-t="20:17:00">[20:17:00]</a>.
*   **Designing for Non-Determinism**: AI systems are stochastic and non-deterministic. Product design must account for this by building robust feedback mechanisms, guardrails, and ways to understand aggregate model behavior <a class="yt-timestamp" data-t="20:22:00">[20:22:00]</a>, <a class="yt-timestamp" data-t="20:47:00">[20:47:00]</a>. This fundamentally shifts user interface intuition, as the same input may not yield the exact same output <a class="yt-timestamp" data-t="21:24:00">[21:24:00]</a>.
*   **Adapting to User Research**: User research sessions now involve not only observing user behavior but also the model's behavior in response, leading to insights about both user and AI interaction <a class="yt-timestamp" data-t="22:10:00">[22:10:10]</a>.

## Scaling Intelligence: O1 Model and Orchestration

Beyond scaling intelligence through larger pre-trained models (like GPT-2 to GPT-5), there's a new approach called "O1" which scales intelligence at query time <a class="yt-timestamp" data-t="30:52:00">[30:52:00]</a>, <a class="yt-timestamp" data-t="30:58:00">[30:58:00]</a>. Instead of immediate "system one" thinking, O1 models pause to reason, form hypotheses, and refine answers, similar to how humans solve complex problems <a class="yt-timestamp" data-t="31:04:00">[31:04:00]</a>, <a class="yt-timestamp" data-t="31:32:00">[31:32:00]</a>. This allows for deeper thought processes, potentially for minutes or even hours <a class="yt-timestamp" data-t="31:40:00">[31:40:00]</a>, <a class="yt-timestamp" data-t="31:47:00">[31:47:00]</a>.

Sophisticated [[enterprise_ai_solutions_and_user_adaptation | Enterprise AI solutions and user adaptation]] often involve orchestrating multiple models together, using each for its strengths <a class="yt-timestamp" data-t="30:31:00">[30:31:00]</a>, <a class="yt-timestamp" data-t="30:39:00">[30:39:00]</a>. For example, in cybersecurity, different models can be fine-tuned for specific tasks, with some checking the outputs of others to reduce hallucinations <a class="yt-timestamp" data-t="32:14:00">[32:14:00]</a>, <a class="yt-timestamp" data-t="32:39:00">[32:39:00]</a>. This parallels how humans with different skill sets collaborate to achieve complex goals <a class="yt-timestamp" data-t="33:04:00">[33:04:00]</a>.

## The Future of AI Experiences

The future of [[the_evolving_capabilities_and_future_potential_of_ai | AI products]] will likely be characterized by:
*   **Proactivity**: Models will become more proactive, monitoring user information (with authorization) to spot trends, provide proactive recaps, prepare for meetings, or even draft presentations <a class="yt-timestamp" data-t="33:50:00">[33:50:00]</a>, <a class="yt-timestamp" data-t="34:18:00">[34:18:00]</a>.
*   **Asynchronous Interactions**: Interactions will become more asynchronous, allowing models to take significant time to reason and research, while users can engage in other tasks and return when the model is ready <a class="yt-timestamp" data-t="34:21:00">[34:21:00]</a>, <a class="yt-timestamp" data-t="34:34:00">[34:34:00]</a>. This will enable more complex, longer-horizon tasks like fleshing out project plans or adapting PRDs for new market conditions <a class="yt-timestamp" data-t="35:04:00">[35:04:00]</a>.
*   **Multimodal Interaction**: AI models will increasingly interact in all the same ways humans do, moving beyond typing to include speech and vision. Universal translators like advanced voice mode in ChatGPT demonstrate the potential for seamless cross-language communication in business and travel <a class="yt-timestamp" data-t="35:40:00">[35:40:00]</a>, <a class="yt-timestamp" data-t="36:11:00">[36:11:00]</a>, <a class="yt-timestamp" data-t="36:35:00">[36:35:00]</a>.
*   **Evolving [[human_interaction_and_personalization_with_ai_models | Human interaction and personalization with AI models]]**: Users, especially younger generations, are quickly adapting to and even befriending AI models, treating them as entities with distinct personalities and evolving relationships <a class="yt-timestamp" data-t="37:09:00">[37:09:00]</a>, <a class="yt-timestamp" data-t="37:29:00">[37:29:00]</a>, <a class="yt-timestamp" data-t="38:57:00">[38:57:00]</a>. This "model behavior" will be a key aspect of [[ai_product_management_and_its_future | AI product management]], with interesting questions around personalization versus maintaining a distinct model personality <a class="yt-timestamp" data-t="39:43:00">[39:43:00]</a>, <a class="yt-timestamp" data-t="39:58:00">[39:58:00]</a>.