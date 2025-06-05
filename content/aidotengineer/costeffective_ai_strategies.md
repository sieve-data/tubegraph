---
title: Costeffective AI strategies
videoId: dvft0Gp9sEE
---

From: [[aidotengineer]] <br/> 

Analyzing a large volume of customer data, such as sales calls, can be an insurmountable task for human teams. A single person, working an 8-hour day with no breaks, could listen to 16 sales calls. Even with extreme work-life balance issues, this number only reaches 32 calls daily <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. Analyzing 10,000 sales calls manually would take nearly two years of continuous work <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>. This daunting task, once requiring a dedicated team for several weeks, can now be accomplished by a single AI engineer in about two weeks <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>.

## The Challenge of Unstructured Data Analysis

The goal was to analyze 10,000 sales calls to define an ideal customer profile (ICP) more specifically than "venture-backed startups" <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>. The challenge lay in the sheer volume of unstructured data <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>. A manual analysis would involve:
*   Downloading and reading each transcript <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>
*   Deciding if it matches the target persona <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>
*   Scanning for insights <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>
*   Compiling notes and citations <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>

Before Large Language Models (LLMs), traditional approaches were either high-quality but unscalable (manual analysis) or fast but prone to missing context (keyword analysis) <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>. The intersection of unstructured data and pattern recognition is a "sweet spot" for AI projects <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.

## Selecting the Right AI Model and Reducing Hallucinations

Solving the problem required addressing several interconnected technical challenges <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>. A critical decision involved choosing the right model, balancing intelligence, speed, and cost. While smaller, cheaper models were tempting, experiments showed their limitations, such as an alarming number of false positives or "hallucinations" <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>. For example, they might classify a transcript as crypto-related simply because "blockchain features" were mentioned, or incorrectly identify a prospect as a founder <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>.

To ensure data trustworthiness, the choice was made to invest in more expensive models like GPT-4o and Claude 3.5 Sonnet, which offered acceptable hallucination rates <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>. Claude 3.5 Sonnet was ultimately selected <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>. This decision highlights a common pitfall in [[common_pitfalls_in_ai_strategy]]: prioritizing low cost over accuracy, which can render the entire project pointless if the output isn't reliable <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>.

A multi-layered approach was developed to reduce hallucinations:
*   **Data Enrichment**: Raw transcript data was enriched using retrieval-augmented generation (RAG) from third-party and internal sources <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>.
*   **Prompt Engineering**: Techniques like Chain of Thought prompting were used to elicit more reliable results <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a>.
*   **Structured Outputs**: Generating structured JSON outputs allowed for citations and a verifiable trail back to the original transcripts, ensuring confidence in the final results <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>. These techniques align with [[best_practices_for_building_ai_systems]].

## [[Cost and efficiency in deploying AI systems|Cost Optimization for AI Agent Deployment]]

Initially, ensuring low error rates significantly drove up costs, with the model often hitting its 4,000-token output limit, requiring multiple requests per transcript analysis <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>. To address these [[cost_considerations_in_ai_agent_deployment]], two experimental features were leveraged, dramatically reducing costs:
1.  **Prompt Caching**: By caching transcript content, which was reused for metadata and insight extraction, costs were reduced by up to 90% and latency by up to 85% <a class="yt-timestamp" data-t="05:33:00">[05:33:00]</a>. This is a key [[best_practices_for_ai_deployment_and_optimization]] for [[factors_affecting_ai_agent_pricing]].
2.  **Extended Outputs**: An experimental feature flag provided double the original output context, enabling complete summaries in single passes instead of multiple turns and credit burns <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>.

As a result, a $5,000 analysis was transformed into a $500 one, with results delivered in days instead of weeks <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>.

## Wider Impact and Key Takeaways

The project's impact extended beyond the initial executive team's request, becoming useful across the organization <a class="yt-timestamp" data-t="06:34:00">[06:34:00]</a>. The marketing team used it for branding and positioning, and the sales team automated transcript downloads, saving dozens of hours weekly <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>. This demonstrates how a well-implemented AI solution can contribute to [[scaling_ai_solutions_in_production]] and expand its utility.

Key takeaways from this project for [[strategies_for_ai_model_deployment]]:
*   **Models Matter**: Despite the push for open-source and smaller models, robust models like Claude 3.5 and GPT-4o were essential for handling complex tasks, emphasizing that "the right tool isn't always the most powerful one. It's the one that best fits your specific needs" <a class="yt-timestamp" data-t="07:22:00">[07:22:00]</a>.
*   **Good Engineering Still Matters**: Significant gains came from software engineering best practices, including JSON structured output, good database schemas, and proper system architecture. AI engineering involves building effective systems *around* LLMs, ensuring thoughtful integration rather than just bolting on AI as an afterthought <a class="yt-timestamp" data-t="07:48:00">[07:48:00]</a>. This also relates to [[hiring_and_building_effective_ai_teams]] in that skilled engineers are crucial for integrating AI effectively.
*   **Consider Additional Use Cases**: The project evolved from a single report to a company-wide resource with a dedicated UX, search filters, and export features. Building a flexible tool turned a one-off project into a continuous asset <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>.

This project showcases AI's ability to transform seemingly impossible tasks into routine operations, augmenting human analysis and removing bottlenecks rather than replacing human roles <a class="yt-timestamp" data-t="08:45:00">[08:45:00]</a>. It unlocks entirely new possibilities by making previously untouched customer data (sales calls, support tickets, product reviews, user feedback) accessible and actionable via large language models <a class="yt-timestamp" data-t="09:11:00">[09:11:00]</a>.