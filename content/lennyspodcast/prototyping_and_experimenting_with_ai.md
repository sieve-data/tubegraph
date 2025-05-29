---
title: Prototyping and experimenting with AI
videoId: IxkvVZua28k
---

From: [[lennyspodcast]] <br/> 

Developing products with Artificial Intelligence (AI) introduces unique challenges compared to traditional software development, primarily due to the rapidly evolving and often unpredictable nature of AI models <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. Unlike building on a fixed technology base, AI capabilities are constantly advancing, requiring a fundamental shift in how products are designed and iterated upon <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

## The Evolving Landscape of AI Product Development

The early stages of [[the_role_and_evolution_of_ai_models_in_product_development | AI product development]] are characterized by uncertainty <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. New capabilities emerge from model training, and it's often unclear how effective these capabilities will be (e.g., 60% good versus 99% good) <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. The optimal product design differs significantly based on the model's reliability <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. This requires continuous **experimentation** and discovery, where the product development team is essentially "discovering things together" with the research team <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

This dynamic environment means that organizations must adapt to internal disruptions caused by their own AI advancements <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

## Iteration and Discovery Cycles

The iteration cycle for AI products differs significantly from traditional methods. Instead of a predictable process, it involves:
*   **Observing intelligence trends** While not fully predictable, the general advancement direction of AI intelligence can be observed <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Co-design and Fine-tuning** Product teams actively collaborate with research teams to invest in specific capabilities and fine-tune models <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. Examples include features like "artifacts" or "canvas" <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   **Responding to Emergent Capabilities** Sometimes, new model capabilities are discovered unexpectedly by researchers, requiring product teams to quickly assess their potential and integrate them <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

A key aspect of this cycle is to embed designers and product managers early in the process <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. The primary output of early experiments should be *learning* and *informative demos* that spark product ideas, rather than expecting a perfectly shippable product <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

## Designing for Imperfection: The "60% Good" Model

A significant challenge is developing products with models that are not yet "perfect." Many AI tasks are closer to 60% success rate than 99% <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. However, even at 60% accuracy, AI can be valuable if the product is designed to accommodate human involvement <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.

*   **Human-in-the-loop design** This involves expecting a human to be more involved in the process, such as with GitHub Copilot, where the AI provides a significant head start but requires human editing and validation <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
*   **Graceful failure** Designing for scenarios where the AI may not be fully confident or accurate, allowing the model to prompt the user for assistance <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
*   **Lumpy performance** AI models often perform exceptionally well on some tasks and poorly on others, which can be leveraged by focusing on areas of strength in pilot programs <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.

## The Importance of Evaluations (Evals)

A critical component of [[building_and_scaling_aienabled_tools | building AI-enabled tools]] is the development and use of robust evaluations (evals) <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>. Models are often "eval-limited" rather than "intelligence-limited," meaning they can do more if properly taught and evaluated <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.

*   **Defining Success** The first step in effective evals is clearly defining what success looks like for a given problem <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.
*   **Automated and Human Evaluation** AI models can even assist in writing and grading evaluations, streamlining the iterative improvement process <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
*   **Evals as a Core PM Skill** The ability to write effective evals and prompts is becoming an increasingly central skill for product managers (PMs) building [[creating_aipowered_product_teams | AI-powered product teams]] <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. This means PMs are becoming more involved in model capabilities and development <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.
*   **Intuition through Data** To build intuition for good evals, it's crucial to analyze the actual outputs of the models, especially where they fail, rather than relying solely on aggregate metrics <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.
*   **Evolving Evals for Complex Tasks** As models handle longer, more ambiguous tasks (e.g., booking a hotel), evaluations will become more nuanced and less about "right or wrong," similar to performance reviews for human employees <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.

## Skills for Product People in the Age of AI

Product professionals need to develop new skills to effectively [[prototyping_with_ai_in_product_development | prototype with AI in product development]]:

*   **[[using_ai_tools_for_product_management and_development | AI-powered Prototyping]]** Using AI models to quickly generate and compare UI concepts, accelerating the design and evaluation process <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>.
*   **Deeper Technical Understanding** PMs will increasingly need to understand the underlying technology stack of AI models, even if not at a researcher level, to effectively build products <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>.
*   **Designing for Non-Deterministic Systems** Product design for AI involves dealing with stochastic, non-deterministic outputs. This requires new approaches to feedback mechanisms, guardrails, and understanding aggregate model behavior <a class="yt-timestamp" data-t="00:20:22">[00:20:22]</a>.
*   **Adapting to Non-Intuitive User Interfaces** AI models can produce different outputs for the same inputs, challenging decades of user intuition about computer interactions <a class="yt-timestamp" data-t="00:21:29">[00:21:29]</a>. Product teams must put themselves in users' shoes to design for this new reality, leveraging its advantages <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>.

## Educating Users and Managing Expectations

The rapid adoption of AI products like ChatGPT (less than two years old) demonstrates how quickly users adapt to new technologies, even those that seem magical <a class="yt-timestamp" data-t="00:23:13">[00:23:13]</a>. However, educating end-users, especially in Enterprise contexts, requires thoughtful strategies <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a>.

*   **Product as Educator** Integrating educational elements directly into the product, such as enabling the AI to explain its own features and provide documentation links <a class="yt-timestamp" data-t="00:24:53">[00:24:53]</a>.
*   **Leveraging Power Users** In Enterprise settings, power users can act as evangelists, creating customized AI tools (like custom GPTs) that simplify AI use for less technical colleagues <a class="yt-timestamp" data-t="00:26:50">[00:26:50]</a>.
*   **Embracing Non-Technical Users** Exposure of non-technical users to AI is crucial, and structured educational sessions can help onboard entire organizations <a class="yt-timestamp" data-t="00:26:19">[00:26:19]</a>.

## Future of Prototyping and AI Experiences

The future of AI-powered products will likely feature:

*   **Proactivity** Models will become more proactive, monitoring user data (with authorization) to offer timely insights, pre-empt research, draft content, and anticipate meeting needs <a class="yt-timestamp" data-t="00:33:50">[00:33:50]</a>.
*   **Asynchronous Interactions** AI interactions will become more asynchronous, allowing users to initiate complex tasks and return later for completed work, rather than expecting immediate responses <a class="yt-timestamp" data-t="00:34:21">[00:34:21]</a>. This frees up users to focus on creative tasks while AI handles "drudgery" <a class="yt-timestamp" data-t="00:28:57">[00:28:57]</a>.
*   **Multimodal Interaction** Models will interact in all the same ways humans do: typing, speaking, and seeing <a class="yt-timestamp" data-t="00:35:40">[00:35:40]</a>. Advanced voice modes will enable universal translation, removing language barriers for travel and business <a class="yt-timestamp" data-t="00:36:04">[00:36:04]</a>.
*   **Model Personality and Relationships** The personality of the AI model will become a key product feature, with users developing nuanced relationships and even a sense of empathy towards them <a class="yt-timestamp" data-t="00:38:41">[00:38:41]</a>. This raises questions about customization and how different AI personalities will appeal to users <a class="yt-timestamp" data-t="00:39:50">[00:39:50]</a>.