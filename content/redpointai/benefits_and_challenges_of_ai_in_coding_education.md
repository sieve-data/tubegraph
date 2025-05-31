---
title: Benefits and challenges of AI in coding education
videoId: n6PazYmo_Qo
---

From: [[redpointai]] <br/> 

The landscape of coding education is undergoing a significant transformation due to the integration of Artificial Intelligence (AI). Omj, founder of Replit, a company focused on enabling the next billion developers, discusses how AI is reshaping how individuals learn to code, the future of software engineering roles, and the inherent [[challenges_and_opportunities_in_ai_development | challenges and opportunities]] in this evolving space <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Reimagining Coding Education with AI

Omj believes that the most effective way to learn coding is by "making things" <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. This contrasts with the traditional academic approach of studying basics in a university setting, which he feels does not suit most learners <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Instead, people typically learn by working towards a specific goal and acquiring knowledge along the way <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

Despite the prevalence of computers and the power of coding, less than 0.5% of the global population has exposure to it <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. Large Language Models (LLMs) significantly enhance the "learning by doing" philosophy by allowing users to get something running in minutes, often through prompting an AI-powered editor <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. This immediate feedback, or "dopamine hit," encourages further experimentation and project development <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

## Replit's Approach to AI Integration

Replit, an AI-native company, has deeply embedded AI into its product, moving away from an "add-on" model where AI features were separate <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. Initially, Replit's AI product was called Ghostwriter, but it has since been integrated directly into the core Replit experience <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

This integration means that:
*   Every interaction with the product is AI-powered <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   AI suggestions appear from the very first line of code a user types, even on the free plan <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
*   Users can generate entire files by prompting the AI <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   An "AI debug" button in the console provides pre-prompted AI chat with error context to help solve issues <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

The decision to build their own model, costing around $100,000, was driven by the need for low latency and cost-effectiveness to offer AI features as part of the free experience <a class="yt-timestamp" data-t="00:28:05">[00:28:05]</a>. Replit found that smaller models (like their 3-billion parameter model) are capable and affordable to train and deploy, making it feasible to embed AI throughout the product <a class="yt-timestamp" data-t="00:29:18">[00:29:18]</a>.

## [[impact_of_ai_on_software_engineering | Impact of AI on Software Engineering]] and Learning

AI is causing a bifurcation in software engineering roles <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
1.  **Product Engineer/Creator:** This role focuses on making products and acquiring users, often involving prompting AI, iterating on prompts, and some debugging <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. This path might not require a traditional computer science degree <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
2.  **Traditional Software Engineer:** This role involves building cloud infrastructure, data pipelines, and backend systems, which is not expected to change as dramatically <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. A computer science degree remains relevant for this path <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.

AI disproportionately benefits beginners. The return on investment for new coders has significantly increased, with individuals going from learning through Replit's "100 days of code" course to making substantial income from applications in months <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>. This aligns with studies showing AI benefits beginners more than advanced users <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.

However, Omj notes that advanced users, once trained in sophisticated prompting techniques like Chain of Thought, could see even greater benefits, as they possess both coding skills and the ability to leverage AI effectively <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>.

### [[ai_in_education | AI in Education]]: The "Calculator Moment"

When Replit rolled out AI features for free, younger users adapted easily, often not even "blinking" <a class="yt-timestamp" data-t="00:22:31">[00:22:31]</a>. More established users, including some teachers, found it jarring <a class="yt-timestamp" data-t="00:22:40">[00:22:40]</a>. Omj compares this to the "calculator moment" in mathematics education; while some teachers initially banned calculators, AI is a tool that will see widespread usage <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>. Some teachers, after initial hesitation, found their students learned better and were more adept at utilizing AI models <a class="yt-timestamp" data-t="00:23:19">[00:23:19]</a>. This phenomenon is attributed to the brain's plasticity, allowing younger generations to adapt quickly to new innovations <a class="yt-timestamp" data-t="00:23:34">[00:23:34]</a>.

## [[challenges_and_opportunities_in_ai_development | Challenges and Opportunities in AI Development]] for Coding

### The Nature of AI Models and Data

Omj views LLMs reductively as a function of data, or a compression of data <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. Their power lies in interpolating different data distributions, like writing a rap song in the style of Shakespeare <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>. Understanding model capabilities requires understanding the data they are fed and post-training mechanisms <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.

### Data Quality and Scarcity for Coding Models

*   **Size and Compute:** Larger, more diverse, and fresher data tokens lead to better models <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.
*   **Quality:** Training on minified JavaScript, for example, can negatively impact models <a class="yt-timestamp" data-timestamp="00:16:48">[00:16:48]</a>. Models should be trained on data generated by the best programmers, as LLMs essentially "behavior clone" humans <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>.
*   **Application Code Gap:** GitHub is rich in high-quality infrastructure code but lacks high-quality application code, which Replit's user base helps to fill <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>.
*   **Novel Data Sources:** Non-coding data, such as scientific or even legal text, has been shown to improve code generation capabilities, hinting at "coding-adjacent reasoning" <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.
*   **"Open Source" Limitations:** Omj argues that many "open source" models are not truly open source because their training data and compilation processes are not reproducible <a class="yt-timestamp" data-t="00:31:50">[00:31:50]</a>. This creates a dependency on the goodwill of companies that release them <a class="yt-timestamp" data-t="00:32:30">[00:32:30]</a>.
*   **Security Risks:** Without clarity on the training process and data, there's a significant security risk, as models could have hidden "back doors" that evade inspection <a class="yt-timestamp" data-t="00:36:51">[00:36:51]</a>.

### [[challenges_in_ai_product_development | Challenges in AI Product Development]]: Latency and Cost

Latency is a critical factor; a two-to-three-second response time completely changes the user experience compared to 300 milliseconds <a class="yt-timestamp" data-t="00:58:27">[00:58:27]</a>. This is why Replit chose to train its own model for core features, as commercial models often don't meet their latency requirements <a class="yt-timestamp" data-t="00:28:07">[00:28:07]</a>.

Advanced AI features, particularly "agentic workflows" (where models recursively call themselves or perform background tasks), are currently expensive <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>. A task like "refactor this and run the tests" can quickly become cost-prohibitive for most consumers <a class="yt-timestamp" data-t="00:40:26">[00:40:26]</a>. The hope is that agent capabilities will improve and become more affordable in the future <a class="yt-timestamp" data-t="00:40:55">[00:40:55]</a>.

### Pricing Models in the AI Era

As AI becomes "table stakes" for software products, pricing will shift from a "cost-plus" model to a "value-based" approach <a class="yt-timestamp" data-t="00:42:41">[00:42:41]</a>. Companies must project forward the decreasing costs of models and inference <a class="yt-timestamp" data-t="00:43:01">[00:43:01]</a>. Omj predicts that "usage-based pricing" will become more prevalent, as some power users could incur significantly higher costs due to heavy model usage <a class="yt-timestamp" data-t="00:44:29">[00:44:29]</a>.

## The [[future_of_coding_and_ai_integration | Future of Coding and AI Integration]]

Omj is bullish on the future of agents, seeing it as the next major development beyond multimodal AI <a class="yt-timestamp" data-t="00:46:56">[00:46:56]</a>. He anticipates background agents performing tasks on behalf of users becoming more common this year <a class="yt-timestamp" data-t="00:48:01">[00:48:01]</a>. A key milestone for agents would be their ability to reliably follow a bulleted list of actions without "going off the rails" or "talking to themselves" <a class="yt-timestamp" data-t="00:49:38">[00:49:38]</a>.

The overall [[ai_advancements_in_coding_and_software_engineering | AI advancements in coding and software engineering]] market presents a complex competitive landscape. While Microsoft, with its large install base and sales team, is a default frontrunner <a class="yt-timestamp" data-t="00:51:26">[00:51:26]</a>, there's also room for specialized companies. These could focus on specific aspects of coding workflows, such as generating tests <a class="yt-timestamp" data-t="00:52:59">[00:52:59]</a>.

Omj predicts that in five years, companies could achieve the same output with one-tenth of the engineers <a class="yt-timestamp" data-t="01:01:46">[01:01:46]</a>. In ten years, there could be a "1000x" improvement, leading to a significant reduction in company size <a class="yt-timestamp" data-t="01:02:01">[01:02:01]</a>. He believes the number of "software creators" will continue to grow, though the definition and title of this role may evolve <a class="yt-timestamp" data-t="01:02:45">[01:02:45]</a>.

## Overhyped vs. Underhyped AI Aspects

*   **Overhyped:** Chatbots, especially where they are an inappropriate solution <a class="yt-timestamp" data-t="00:57:51">[00:57:51]</a>.
*   **Underhyped:** Integrating LLMs as part of everyday systems and backend software call chains <a class="yt-timestamp" data-t="00:58:05">[00:58:05]</a>.

For more information, Replit's technical blog can be found at blog.replit.com <a class="yt-timestamp" data-t="01:03:09">[01:03:09]</a>. Omj also shares insights on his blog (amjad.me) and Twitter (@amjadm) <a class="yt-timestamp" data-t="01:03:21">[01:03:21]</a>. The best way to understand Replit's AI work is to use the product at replit.com <a class="yt-timestamp" data-t="01:03:37">[01:03:37]</a>.