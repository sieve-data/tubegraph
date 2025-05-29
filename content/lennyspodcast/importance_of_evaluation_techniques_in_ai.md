---
title: Importance of evaluation techniques in AI
videoId: IxkvVZua28k
---

From: [[lennyspodcast]] <br/> 

The landscape of AI product development presents unique challenges due to the rapidly evolving nature of AI models and their capabilities <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>. Unlike traditional software development, where the underlying technology base is fixed <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>, AI models are constantly advancing, with new capabilities emerging every couple of months <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>. This dynamic environment necessitates a strong emphasis on [[evals_and_their_importance_in_ai_product_management | evaluation techniques]] to guide product development and ensure successful deployment.

## The Challenge of Unpredictable Capabilities

A significant challenge in [[challenges_in_building_ai_products | building AI products]] is the inherent uncertainty regarding model capabilities. Product teams may have a sense of potential capabilities during model training, but the exact performance (e.g., 60% good, 90% good, or 99% good) often remains unknown until late in the development cycle <a class="yt-timestamp" data-t="06:58:00">[06:58:00]</a>. The type of product built would differ drastically based on these performance levels <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>.

Furthermore, research teams, being focused on fundamental advancements, might discover capabilities they don't immediately recognize as important for product development <a class="yt-timestamp" data-t="09:52:00">[09:52:00]</a>. This can lead to "magic happening sometimes" where capabilities exist but are not yet leveraged <a class="yt-timestamp" data-t="10:10:00">[10:10:00]</a>.

### Designing for Imperfection: The "60% Good" Model

A crucial aspect of [[evals_and_their_importance_in_ai_product_management | AI product evaluation]] is understanding how to build products even when a model is only 60% successful at a task <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>.

[!NOTE|Human in the Loop]
This often requires designing for a "human in the loop," where the user is expected to intervene and refine the model's output <a class="yt-timestamp" data-t="10:56:00">[10:56:00]</a>. A prime example is GitHub Co-pilot, which launched with models that were "multiple generations ago" and not perfect, yet still provided significant value by drafting code that users could then edit <a class="yt-timestamp" data-t="11:02:00">[11:02:00]</a>. The value lies in saving initial time and effort, even if the model's output isn't flawless <a class="yt-timestamp" data-t="11:54:00">[11:54:00]</a>.

Models that can convey their confidence levels and ask for human assistance can significantly enhance the combined human-model performance <a class="yt-timestamp" data-t="11:57:00">[11:57:00]</a>.

Model performance can also be "lumpy," meaning a model might excel at certain tasks while performing poorly on others <a class="yt-timestamp" data-t="12:19:00">[12:19:00]</a>. This necessitates detailed feedback from pilot programs and real-world deployment to understand specific strengths and weaknesses across different use cases <a class="yt-timestamp" data-t="12:27:00">[12:27:00]</a>.

## The Critical Role of Evals

A key insight is that models today are often "eval limited" rather than "intelligence limited" <a class="yt-timestamp" data-t="13:13:00">[13:13:00]</a>. This means models have latent capabilities that can be unlocked and improved through proper evaluation and teaching <a class="yt-timestamp" data-t="13:23:00">[13:23:25]</a>. Many older AI deployments lacked robust evaluation frameworks, making it difficult to assess progress with newer, potentially better models <a class="yt-timestamp" data-t="13:40:00">[13:40:00]</a>.

### Defining Success and Iterative Improvement

The first step in effective evaluation is clearly defining what success looks like for a given problem <a class="yt-timestamp" data-t="13:49:00">[13:49:00]</a>. With well-defined evaluations, it's possible to iteratively improve models. AI tools themselves, like Claude, can assist in writing and even grading evaluations, automating a significant part of the process <a class="yt-timestamp" data-t="14:01:00">[14:01:00]</a>.

### Evals as a Core Skill for Product Managers

The role of a Product Manager (PM) in AI development is increasingly merging with that of a "research PM" <a class="yt-timestamp" data-t="14:47:00">[14:47:00]</a>. The quality of an AI-powered feature is directly "gated on how well you have done the evals and the prompts" <a class="yt-timestamp" data-t="15:20:00">[15:20:00]</a>. Therefore, [[evals_and_their_importance_in_ai_product_management | writing evaluations]] is becoming a core skill for PMs <a class="yt-timestamp" data-t="14:38:00">[14:38:00]</a>. Companies are even running bootcamps to train PMs on the differences between good and bad evaluations <a class="yt-timestamp" data-t="15:31:00">[15:31:00]</a>.

To develop intuition for writing good evals:
*   **Utilize AI models themselves**: Ask models to explain what makes a good eval or to generate sample evals <a class="yt-timestamp" data-t="16:06:00">[16:06:00]</a>.
*   **Examine raw data**: Look at actual model outputs and failure cases, rather than relying solely on aggregate metrics <a class="yt-timestamp" data-t="16:28:00">[16:28:00]</a>. Sometimes, human-written "golden answers" for evaluations might even be flawed <a class="yt-timestamp" data-t="16:51:00">[16:51:00]</a>.

## Evolving Evals for Agentic AI

As models progress towards longer-form, more agentic tasks (e.g., "go get me a hotel in New York City" <a class="yt-timestamp" data-t="17:38:00">[17:38:00]</a>), the nature of evaluation will need to evolve <a class="yt-timestamp" data-t="17:18:00">[17:18:00]</a>. For complex, ambiguous tasks, grading becomes "much softer" <a class="yt-timestamp" data-t="17:52:00">[17:52:00]</a>. Evaluations might begin to resemble performance reviews, assessing whether a model "met your expectation of what a competent human would have done" <a class="yt-timestamp" data-t="18:16:00">[18:16:00]</a> or even "exceeded it" <a class="yt-timestamp" data-t="18:24:00">[18:24:00]</a>.

[!INFO|Model surpasses human performance]
A unique challenge arises when models can outperform humans at certain tasks or provide answers that users prefer over human answers <a class="yt-timestamp" data-t="18:38:00">[18:38:00]</a>. This fundamentally shifts how evaluations are designed and interpreted.

## Skills for the AI Product Manager

Beyond [[evals_and_their_importance_in_ai_product_management | evaluation]], other crucial skills for PMs in the AI era include:
*   **[[prototyping_and_experimenting_with_ai | Prototyping]] with models**: Using AI tools to rapidly create and test UI variations <a class="yt-timestamp" data-t="19:05:00">[19:05:00]</a>. This allows for faster experimentation and evaluation at scale <a class="yt-timestamp" data-t="19:28:00">[19:28:00]</a>.
*   **Deeper technical understanding**: PMs need to go deeper into the tech stack to appreciate how AI models work and understand their language <a class="yt-timestamp" data-t="19:49:00">[19:49:00]</a>.
*   **Designing for non-deterministic systems**: AI introduces stochastic, non-deterministic behavior <a class="yt-timestamp" data-t="20:24:00">[20:24:00]</a>, which is counter-intuitive to decades of computer use <a class="yt-timestamp" data-t="21:24:00">[21:24:00]</a>. PMs must design feedback mechanisms, guardrails, and aggregate monitoring to manage this unpredictability <a class="yt-timestamp" data-t="20:35:00">[20:35:00]</a>.

## Educating Users on AI

Despite the rapid adoption of AI, adapting to non-deterministic user interfaces is a significant hurdle for most users <a class="yt-timestamp" data-t="21:09:00">[21:09:00]</a>. What was once "absolute magic" quickly becomes commonplace <a class="yt-timestamp" data-t="23:54:00">[23:54:00]</a>. Product teams are learning to make the product itself educational, by having the AI directly explain its features and provide links to documentation <a class="yt-timestamp" data-t="24:53:00">[24:53:00]</a>.

In Enterprise settings, where non-technical users are introduced to AI, structured educational sessions and materials can be deployed <a class="yt-timestamp" data-t="26:30:00">[26:30:00]</a>. Power users within organizations often act as "evangelists," creating custom AI tools (like custom GPTs) to make AI more accessible and valuable for their less technical colleagues <a class="yt-timestamp" data-t="26:50:00">[26:50:00]</a>.

## The Future of AI and Evaluation

The future of AI will involve models interacting in more human-like ways, beyond just typing, to include speech and vision <a class="yt-timestamp" data-t="35:38:00">[35:38:00]</a>. Experiences like universal translators <a class="yt-timestamp" data-t="36:24:00">[36:24:00]</a> will become commonplace.

Model behavior and personality are becoming crucial aspects of product design <a class="yt-timestamp" data-t="39:43:00">[39:43:00]</a>. Users are developing "two-way empathy" and even "befriending" the AI, noting nuanced changes in its intelligence and demeanor <a class="yt-timestamp" data-t="38:57:00">[38:57:00]</a>. This highlights that PMs are not just shipping a product, but shipping "intelligence" that fosters interpersonal relationships <a class="yt-timestamp" data-t="39:16:00">[39:16:00]</a>. The ability to monitor and shape this "model behavior" will be integral to the continued [[the_role_and_evolution_of_ai_models_in_product_development | evolution of AI products]].