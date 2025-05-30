---
title: AIs impact on software development
videoId: n6PazYmo_Qo
---

From: [[redpointai]] <br/> 

Omay (`omjmad`), founder of Replit, discusses the transformative [[ais_impact_on_software_development_and_programming_jobs | impact of AI on software development]] and the evolving [[role_and_expectations_of_software_developers_in_the_context_of_ai_advancements | role and expectations of software developers]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Replit is at the forefront of using AI in innovative ways for coding, having raised over $100 million at a valuation exceeding $1 billion <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## Learning to Code in the AI Era

The traditional academic approach to learning to code, such as going to university to study basics, is not how most people learn <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Instead, people learn by creating things to achieve a goal <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Omaj believes that Large Language Models (LLMs) take this "learn by doing" concept to its extreme <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. With LLM-powered editors like Replit, users can get something running in as little as five minutes, avoiding the "drudgery" of installation and setup <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. This provides immediate "dopamine hits" from seeing results, encouraging further experimentation and larger projects <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

## The Evolving Role of Software Engineers

Omaj predicts a bifurcation in software engineering roles, a trend that was already present with frontend and backend engineers, but which AI will significantly widen <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

The two main paths are:
*   **Product Engineer/Creator**: This role involves using AI to create products for customers and users, often through prompting and iterating on prompts <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. While debugging code is still part of it for now, it may eventually be automated <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. This path does not necessarily require a computer science degree <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
*   **Traditional Software Engineering**: This path focuses on building [[ai_infrastructure_and_developer_tools | cloud infrastructure]], data pipelines, or backend systems <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. This role, which involves thinking about components and systems, is expected to change less dramatically with AI <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. A computer science degree remains relevant for this path <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

AI disproportionately benefits beginners more than advanced users initially <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>. Beginners can achieve significant results with minimal coding knowledge, even starting companies and generating substantial revenue within months <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>. However, Omaj suggests that advanced users who are skilled at leveraging AI tools (e.g., prompting techniques, Chain of Thought, using multiple LLMs) will ultimately see greater benefits <a class="yt-timestamp" data-t="00:20:12">[00:20:12]</a>. Younger generations, in particular, are much better at adapting to and building mental models for what LLMs can do <a class="yt-timestamp" data-t="00:22:10">[00:22:10]</a>.

## Replit's AI Integration

Replit's strategy involves deeply embedding AI into its product, moving beyond the "co-pilot" add-on model <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

*   **From Ghostwriter to Core Product**: Initially, Replit's AI product was called Ghostwriter, functioning as an add-on <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. Recognizing that AI would become "table stakes," Replit embedded AI into every interaction, making it part of the free plan <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
*   **AI-Powered Workflows**:
    *   **Co-suggestions**: Replit provides AI code suggestions while users type, similar to GitHub Copilot <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. This is a "push model" where AI passively assists <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.
    *   **Code Generation**: Users can prompt the AI to generate entire files based on context <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. This is a "pull model" where the user actively requests AI assistance <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
    *   **AI Debugging**: An "AI debug button" appears when an error occurs in the console, opening an AI chat pre-prompted with the error and relevant context <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
    *   **Contextual Actions**: The product can derive information from the cursor's position, enabling highly contextual AI actions within the IDE <a class="yt-timestamp" data-t="00:59:36">[00:59:36]</a>.

Replit chose to build its own 3-billion parameter model for Ghostwriter, spending approximately $100,000, due to the need for low latency and cost-effectiveness <a class="yt-timestamp" data-t="00:28:05">[00:28:05]</a>. This decision was crucial because commercial models at the time did not meet their latency requirements <a class="yt-timestamp" data-t="00:28:07">[00:28:07]</a>. Small models were found to be capable and affordable to train and deploy <a class="yt-timestamp" data-t="00:29:18">[00:29:18]</a>. Despite training their own models, Replit also utilizes commercial models for other use cases like general-purpose chat features <a class="yt-timestamp" data-t="00:30:10">[00:30:10]</a>.

## Understanding AI Models for Coding

Omaj views LLMs reductively as a "function of data" or a "compression of the data" <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. Their power lies in interpolating different distributions of data (e.g., writing a rap song in Shakespeare's style) <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.

Key factors for model capabilities are:
*   **Data Sources**: Understanding the data fed into the models is crucial <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.
*   **Fine-tuning/Post-training**: Mechanisms like instruction fine-tuning, RLHF (Reinforcement Learning from Human Feedback), and DPO (Direct Preference Optimization) are used to improve models for specific downstream tasks <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.

For code generation models, the quality of data is paramount:
*   **Size and Compute**: More tokens and more compute spent on training lead to better models <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.
*   **Diversity and Freshness**: A wider variety and newer data are beneficial <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>.
*   **Human-generated Data**: Training on code generated by the "best programmers" is important because LLMs emulate human thinking <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>.
*   **Application Code**: While GitHub is rich in high-quality [[ai_infrastructure_and_developer_tools | infrastructure code]], there's a "poverty" of high-quality application code <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>. Replit, with its user base writing applications, has an advantage in gathering this type of data <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>.
*   **Adjacent Data**: Surprisingly, scientific data and even [[ais_impact_on_the_legal_sector | legal text]] have been shown to improve code generation abilities <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.

Omaj expresses concern that "open source" models today are not truly open source because they cannot be fully reproduced or compiled without proprietary compilers or data, making users dependent on the "goodwill" of the companies releasing them <a class="yt-timestamp" data-t="00:31:48">[00:31:48]</a>. Not knowing the underlying training data also poses a significant security risk, as "backdoors" can be hidden in the models, activated only under specific conditions <a class="yt-timestamp" data-t="00:36:20">[00:36:20]</a>.

## The Future of AI in Software Development

*   **Agents**: Omaj believes agentic workflows and background agents are the next major advancement <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>. These allow models to recursively call themselves to perform larger tasks, such as refactoring code and running tests <a class="yt-timestamp" data-t="00:40:05">[00:40:05]</a>. The current limitation is cost with large models like GPT-4 <a class="yt-timestamp" data-t="00:40:30">[00:40:30]</a> and reliability (e.g., models going "off the rails") <a class="yt-timestamp" data-t="00:49:52">[00:49:52]</a>.
*   **Pricing**: As AI becomes table stakes, pricing models for software will shift from "Cost Plus" (based on AI inference costs) to "Value Based" <a class="yt-timestamp" data-t="00:42:51">[00:42:51]</a>. Usage-based pricing is also becoming more prevalent to account for "power users" who incur high costs <a class="yt-timestamp" data-t="00:44:33">[00:44:33]</a>.
*   **Competitive Landscape**: Microsoft, with its vast install base, sales team, and commercial mindset, is seen as the default winner in the AI coding market <a class="yt-timestamp" data-t="00:51:26">[00:51:26]</a>. However, there is room for specialized companies (e.g., those focused on generating tests) and platforms that offer a holistic approach to cloud development environments, integrating AI across the entire stack <a class="yt-timestamp" data-t="00:52:03">[00:52:03]</a>.

Omaj notes that the overall [[ais_influence_on_industry_landscapes | speed of AI adoption]] in everyday technology is surprisingly slow, attributing it to corporate inertia and forces working against faster progress <a class="yt-timestamp" data-t="00:24:41">[00:24:41]</a>. Despite this, he believes AI will "kickstart another S-curve of growth" <a class="yt-timestamp" data-t="00:26:08">[00:26:08]</a>. The future of software development will see fewer engineers required to achieve current output levels (e.g., 1/10th the engineers in 5 years, possibly 1/1000th in 10 years), but the number of "software creators" will continue to grow, even if they are called something else <a class="yt-timestamp" data-t="01:01:49">[01:01:49]</a>.

## Key Insights

*   **Latency Matters**: For [[ai_infrastructure_and_developer_tools | AI infrastructure and developer tools]], low latency is crucial; even a few seconds delay can drastically change the user experience <a class="yt-timestamp" data-t="00:58:27">[00:58:27]</a>.
*   **"Vibes" of Models**: While benchmarks are important, the practical "vibes" (how a model feels to use) are also key <a class="yt-timestamp" data-t="00:55:14">[00:55:14]</a>.
*   **Hyperreality**: The rapid advancement of generative AI is leading to a "hyperreality" where it's increasingly difficult to distinguish between fiction and reality, raising concerns about lack of technology to counteract it <a class="yt-timestamp" data-t="00:37:49">[00:37:49]</a>.
*   **[[openais_approach_to_product_development_and_platform_strategy | OpenAI's ambition]]**: [[openais_approach_to_product_development_and_platform_strategy | OpenAI]] is admired for its ambition and diverse partnerships across various sectors, from education to robotics <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.
*   **Perplexity**: Perplexity is highlighted for its strong engineering and ability to deliver value, despite intense competition <a class="yt-timestamp" data-t="01:01:04">[01:01:04]</a>.