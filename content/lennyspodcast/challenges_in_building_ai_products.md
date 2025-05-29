---
title: Challenges in building AI products
videoId: IxkvVZua28k
---

From: [[lennyspodcast]] <br/> 

Building AI-powered products presents unique challenges that differentiate it from traditional product development, requiring a shift in mindset and skillsets for product managers and development teams <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. The rapid evolution of AI capabilities means that "every two months computers can do something computers have never been able to do before" <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>, constantly reshaping product possibilities <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

## Unpredictable Capabilities and Planning Difficulties
One of the primary challenges is the inherent unpredictability of AI model capabilities <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. When training a new model, even the research team may not fully know its emergent properties or the exact percentage of success it will achieve on a given task <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>. This uncertainty makes traditional product planning difficult, as a product designed for 60% accuracy would be "super different" <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a> from one designed for 90% or 99% accuracy <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

Sometimes, new capabilities are discovered unexpectedly within the research phase, leading to situations where a product team might wish for a feature, only to find out a researcher has had the capability for months <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. This internal disruption can fundamentally alter existing product roadmaps <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

> "It's like that but your own company is the one kind of disrupting you from within which is like a very like it's very cool but also like oh this might totally in my product road map now" <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>

Despite the unpredictability, [[the_role_and_evolution_of_ai_models_in_product_development | intelligence in AI models]] generally advances in a discernible direction, allowing for some strategic planning <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. Teams can also strategically invest in specific capabilities from the product side and then work closely with research teams for fine-tuning <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.

## Adapting to Non-Deterministic Systems
Unlike traditional software, AI systems are stochastic and non-deterministic <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>. The same inputs may not always yield the exact same outputs <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>, challenging decades of user intuition about how computers work <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>.

This requires product designers to consider:
*   **Feedback mechanisms**: How to quickly identify when the model has gone astray and collect user feedback <a class="yt-timestamp" data-t="00:20:35">[00:20:35]</a>.
*   **Graceful failures**: Designing products to accommodate instances where the model is not 100% accurate, such as with [[humanai_collaboration_in_product_development | human-in-the-loop systems]] <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>, or by allowing the model to indicate its confidence level <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.

Even with lower accuracy (e.g., 60%), an AI tool can be valuable if it significantly reduces human effort and allows for editing or refinement, as seen with [[using_ai_tools_for_product_management_and_development | GitHub Copilot]] <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.

## The Importance of Evaluation (Evals)
A critical challenge and emerging skill in AI product development is the creation and application of "evals" (evaluations) <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>. Many AI models today are "eval-limited," meaning they have greater intelligence than is currently leveraged due to insufficient evaluation <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

*   **Defining Success**: The first hurdle is clearly defining what success looks like for a particular problem an AI is trying to solve <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.
*   **Automating Evals**: AI models themselves, such as Claude, can assist in writing and grading evaluations <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>, but human oversight and intuition are still crucial <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.
*   **Nuance in Evaluation**: As models tackle more ambiguous, long-form, or agentic tasks, evaluations become less about simple right/wrong answers and more about nuanced performance reviews, akin to human performance evaluations <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>. The model's "personality" or "behavior" also becomes a key product consideration <a class="yt-timestamp" data-t="00:39:43">[00:39:43]</a>.

## Enterprise vs. Consumer Product Development
[[integration_of_ai_in_business_and_product_development | Building AI products for enterprise customers]] introduces distinct challenges compared to consumer products:
*   **Buyer vs. User**: In enterprise, there's often a "buyer" with specific organizational goals that might not align directly with the end-users' immediate product satisfaction <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
*   **Longer Feedback Cycles**: The sales and deployment process can take months, delaying crucial feedback on whether the product is truly effective <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Change Management**: Educating entire organizations, especially non-technical users, about new AI-powered workflows requires significant change management <a class="yt-timestamp" data-t="00:25:53">[00:25:53]</a>. This involves providing educational materials and leveraging internal power users as evangelists <a class="yt-timestamp" data-t="00:26:33">[00:26:33]</a>.

## [[Impact of AI on Product Management | Evolving Product Management Roles]]
The unique nature of AI products means that the role of a product manager is rapidly evolving:
*   **Deeper Technical Understanding**: Product managers need to go "deeper into the tech stack" <a class="yt-timestamp" data-t="00:19:49">[00:19:49]</a>, appreciating the language and gaining intuition for how the underlying models work <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>.
*   **Eval and Prompt Engineering**: The ability to write effective evaluations and craft precise prompts is becoming a core skill, blurring the lines between "research PMs" and "product surface PMs" <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.
*   **Prototyping with AI Tools**: Product managers can leverage AI models for rapid UI prototyping and A/B comparisons of different user interface approaches <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>.
*   **Adapting to User Behavior**: Product teams must anticipate and adapt to how users interact with non-deterministic AI. Younger, "AI native" users are already demonstrating new ways of interacting with AI, such as speaking directly to models for long periods or expecting real-time content generation <a class="yt-timestamp" data-t="00:37:09">[00:37:09]</a>.

Despite these challenges, the rapid pace of AI development means that what feels like "magic" today will quickly become commonplace and even outdated in just 12 months <a class="yt-timestamp" data-t="00:24:24">[00:24:24]</a>. The industry and users alike are adapting quickly to these new paradigms <a class="yt-timestamp" data-t="00:23:35">[00:23:35]</a>.