---
title: Enterprise adoption of AI technologies
videoId: IxkvVZua28k
---

From: [[lennyspodcast]] <br/> 

The integration of AI into enterprise environments presents a unique set of [[Challenges and opportunities in implementing AI solutions | challenges and opportunities]] distinct from consumer product development. Both Kevin and Mike highlight their experiences and observations regarding the [[Cultural and operational shifts in companies with AI integration | cultural and operational shifts]] within companies as they adopt AI.

## The Nuance of Enterprise Product Development
Unlike consumer products where the user is often the direct recipient, enterprise AI solutions must consider the "buyer" and their specific goals, which may not always align directly with the end-user's experience. This adds a layer of complexity to product development and deployment.

> "The interesting thing about Enterprise is it's not necessarily about the product, right? There's a buyer and they have goals and you could build the best product in the world that all the people at the company might be happy to use and it still doesn't necessarily matter." <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>

Enterprise timelines are also significantly longer than consumer ones, requiring patience and a different rhythm for product managers. A product that might ship in weeks in a consumer context could take months or even six months to reach deployment in an enterprise setting, before knowing if it's the right solution <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. However, once deployed, enterprise feedback can be more direct and financially incentivized, providing valuable insights on where the product excels or falls short <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

## Working with Imperfect Models: The 60% Solution
A significant challenge in enterprise AI is working with models that are not 99% accurate but might be 60% successful at a task <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. This requires a different product design philosophy that anticipates human involvement. For example, GitHub Copilot was useful even when its underlying model was generations older and not perfect, as it still significantly reduced the typing burden for developers, allowing them to edit the generated code <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. This approach of "human in the loop" is crucial.

Model performance can also be "lumpy," meaning it performs very well on some tasks and poorly on others. This leads to varied feedback from different companies even with the same model, as their custom datasets and internal use cases highlight different strengths and weaknesses <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

## The Critical Role of Evals and Prompt Engineering
For AI models, particularly in enterprise contexts, the ability to define success and iteratively improve is paramount. Many early AI deployments lacked robust "evals" (evaluations), meaning companies shipped "cool AI features" without clear metrics for success <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.

> "Models today are not intelligence limited, they're eval limited." <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>

This means models often have greater capabilities than currently utilized; the challenge lies in effectively teaching them and evaluating their performance <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>. Product managers in AI companies are finding their role increasingly merging with that of a research PM, requiring skills in writing evaluations and prompt engineering <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>. Organizations are now running bootcamps to train product managers in writing effective evals <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.

To develop intuition for good evals:
*   **Utilize the models themselves:** Ask models what makes a good eval or for sample evals <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.
*   **Look at the data:** Don't just rely on aggregate numbers; examine cases where the model fails to understand *why* and whether the grader itself is accurate <a class="yt-timestamp" data-t="00:16:28">[00:16:28]</a>.
*   **Anticipate ambiguity:** As models handle more long-form, ambiguous tasks (e.g., "get me a hotel in New York City"), evaluations will become less about right/wrong and more about nuanced performance reviews, like evaluating a competent human's work <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.

## Educating End-Users and Organizations
The rapid pace of AI development means users quickly adapt to new "magical" capabilities, even things that were mind-blowing just two years ago <a class="yt-timestamp" data-t="00:23:13">[00:23:13]</a>. However, enterprise adoption requires deliberate education and change management due to existing organizational processes and non-technical users <a class="yt-timestamp" data-t="00:25:53">[00:25:53]</a>.

Companies are focusing on:
*   **Product as educator:** Integrating instructions directly into the AI product to help users understand how to use new features <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>.
*   **In-person sessions:** Running dedicated educational sessions for enterprise users, especially non-technical ones, to expose them to AI <a class="yt-timestamp" data-t="00:26:29">[00:26:29]</a>.
*   **Leveraging power users:** Identifying internal power users who can become evangelists and create tools, like custom GPTs, to make AI more accessible and immediately valuable for others <a class="yt-timestamp" data-t="00:26:43">[00:26:43]</a>.

## [[Role of AI in enhancing productivity tools | Enhancing Productivity Tools]] with AI
The "computer use" feature, enabling AI to interact with software interfaces, offers significant [[Leveraging AI in product development | opportunities for leveraging AI in product development]] within enterprises. Early use cases include:
*   **UI testing:** Automating UI tests that are typically brittle and hard to write manually <a class="yt-timestamp" data-t="00:28:14">[00:28:14]</a>.
*   **Automating "drudgery":** Handling repetitive, data-manipulation tasks for teams like support and finance, allowing humans to focus on creative work <a class="yt-timestamp" data-t="00:28:50">[00:28:50]</a>.

## Orchestration of Models: The Future of Enterprise AI
Sophisticated enterprise customers are moving beyond using a single AI model for a task. Instead, they are building workflows and orchestrating multiple models, leveraging each for its specific strengths <a class="yt-timestamp" data-t="00:29:31">[00:29:31]</a>.

For example, a reasoning model (like O1, which pauses to "think" before answering) might be combined with other models that are faster or more precise for different parts of a complex task <a class="yt-timestamp" data-t="00:30:40">[00:30:40]</a>. This approach, akin to different people with different skill sets collaborating on a task, enables AI to tackle complex problems like cybersecurity, even where hallucination could be problematic <a class="yt-timestamp" data-t="00:31:50">[00:31:50]</a>. Models can even be fine-tuned to check the outputs of other models, realizing when something doesn't make sense and asking for a retry <a class="yt-timestamp" data-t="00:32:39">[00:32:39]</a>.

## [[The evolving landscape of AI technology | The Evolving Landscape]] and [[Future of startups with AI tools | Future of Enterprise AI]]
The models are expected to get smarter at an accelerating rate <a class="yt-timestamp" data-t="00:35:31">[00:35:31]</a>. Key trends for the near future (6-12 months) include:
*   **Proactivity:** Models becoming more proactive, monitoring user data (with authorization) to spot trends, provide recaps, or even draft presentations for upcoming meetings <a class="yt-timestamp" data-t="00:34:02">[00:34:02]</a>.
*   **Asynchronous interaction:** AI tasks evolving to allow for longer "thinking" times, freeing users to do other things while the model works, and then notifying them upon completion <a class="yt-timestamp" data-t="00:34:33">[00:34:33]</a>. This allows for more complex, mini-project-level tasks rather than simple screen changes or bug fixes <a class="yt-timestamp" data-t="00:35:05">[00:35:05]</a>.
*   **Multimodal interaction:** AI systems interacting in all human ways – beyond typing, to speaking (as seen in advanced voice modes for translation <a class="yt-timestamp" data-t="00:35:54">[00:35:54]</a>) and eventually seeing <a class="yt-timestamp" data-t="00:35:51">[00:35:51]</a>. This promises to dissolve language barriers and enable new forms of interaction <a class="yt-timestamp" data-t="00:36:35">[00:36:35]</a>.

The "personality" or "behavior" of the model is becoming a crucial product consideration, with users developing an almost "befriending" relationship and two-way empathy with the AI <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a>. This raises questions about how much an AI should customize its personality versus maintaining a distinct brand identity <a class="yt-timestamp" data-t="00:39:50">[00:39:50]</a>. This human-like interaction and personalization are becoming increasingly important for user adoption and engagement.