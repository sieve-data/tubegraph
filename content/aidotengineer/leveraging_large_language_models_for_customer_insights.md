---
title: Leveraging large language models for customer insights
videoId: dvft0Gp9sEE
---

From: [[aidotengineer]] <br/> 

Analyzing vast amounts of customer data, such as sales calls, support tickets, product reviews, user feedback, and social media interactions, has historically been a daunting and time-consuming task for businesses. This unstructured data often goes untouched, despite being a valuable source of insight <a class="yt-timestamp" data-t="09:11:00">[09:11:00]</a>. However, modern [[challenges_and_solutions_in_using_large_language_models | large language models]] (LLMs) are transforming this challenge into an opportunity, enabling single engineers to perform analyses that previously required dedicated teams <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>.

## The Challenge of Manual Analysis

Manually analyzing a large database of customer interactions, such as 10,000 sales call transcripts, is practically impossible for humans. Even with extreme dedication, it would take nearly two years (625 days) of continuous work to read, take notes, identify insights, and compile reports <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>. The human brain is simply not equipped to process such a massive volume of information <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>.

Traditional approaches before LLMs typically fell into two categories <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>:
*   **Manual analysis:** High quality but completely unscalable <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.
*   **Keyword analysis:** Fast and cheap, but often missed context and nuance <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.

This gap created a need for a solution that could handle both scale and depth.

## LLMs: The Sweet Spot for Unstructured Data

The intersection of unstructured data and pattern recognition is a "sweet spot" for [[challenges_and_solutions_in_using_large_language_models | AI projects]] <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>. [[challenges_and_solutions_in_using_large_language_models | Large language models]] excel at this, making it feasible to analyze vast datasets of customer interactions <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>. For example, a project aimed at analyzing 10,000 sales calls to refine an ideal customer profile (ICP) was accomplished by a single AI engineer in about a fortnight, a task that would have been impossible two years prior <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>.

### Choosing the Right Model

Selecting the appropriate LLM is crucial. While smaller, cheaper models might be tempting, they often produce an alarming number of false positives and high [[large_language_model_interpretability | hallucination rates]] <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>. For a project where data trustworthiness is paramount, investing in more intelligent models like GPT-4o or Claude 3.5 Sonnet, despite their higher cost and slower speed, is essential to ensure acceptable accuracy <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>. Claude 3.5 Sonnet was ultimately chosen for its prompt caching capabilities and accuracy <a class="yt-timestamp" data-t="07:34:00">[07:34:00]</a>.

### Minimizing Hallucinations and Ensuring Reliability

Achieving reliable results with LLMs requires a multi-layered approach beyond simply feeding in transcripts <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>:
*   **Data Enrichment:** Raw transcript data is enriched via retrieval augmented generation (RAG) from both third-party and internal sources <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>.
*   **[[meta_prompting_with_language_models | Prompt Engineering]]:** Techniques like chain of thought prompting are employed to elicit more reliable outputs <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a>.
*   **Structured Outputs with Citations:** Generating structured JSON outputs and ensuring a verifiable trail back to the original transcripts allows for confidence in the final results and extraction of accurate company details and meaningful insights <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.

### Cost Optimization

Maintaining low error rates and high accuracy can drive up costs significantly due to token limits and multiple requests per analysis <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>. Experimental features can dramatically lower these costs:
*   **Prompt Caching:** Reusing the same transcript content for repeated analysis (e.g., metadata and insight extraction) can reduce costs by up to 90% and latency by up to 85% <a class="yt-timestamp" data-t="05:33:00">[05:33:00]</a>.
*   **Extended Outputs:** Accessing experimental features that double the original output context allows for complete summaries in single passes, avoiding multiple rounds of credit usage <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>.
These optimizations can turn a $5,000 analysis into a $500 one, yielding results in days instead of weeks <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>.

## Wider Organizational Impact and Key Takeaways

What begins as a project for an executive team can have a wide-ranging impact across an organization <a class="yt-timestamp" data-t="06:30:00">[06:30:00]</a>. For example:
*   **Marketing teams** can easily pull customer data for branding and positioning exercises <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>.
*   **Sales teams** can automate transcript downloads, saving dozens of hours weekly <a class="yt-timestamp" data-t="06:54:00">[06:54:00]</a>.
*   The ability to easily perform analysis encourages teams to ask questions that were previously too daunting to consider <a class="yt-timestamp" data-t="07:03:00">[07:03:00]</a>.

This transformation turns mountains of unstructured data from a liability into an asset <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>.

### Key Learnings:
1.  **Models Matter:** Despite the push for open-source and cheaper models, more powerful LLMs like Claude 3.5 and GPT-4o are often necessary for complex tasks that smaller models simply cannot handle <a class="yt-timestamp" data-t="07:22:00">[07:22:00]</a>. The right tool is the one that best fits specific needs <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>.
2.  **Good Engineering Still Matters:** Significant gains come from fundamental software engineering principles, such as leveraging JSON structured output, good database schemas, and proper system architecture <a class="yt-timestamp" data-t="07:48:00">[07:48:00]</a>. [[integration_of_large_language_models_in_development | AI engineering]] involves building effective systems *around* LLMs, ensuring they are thoughtfully [[integration_of_large_language_models_in_development | integrated]] into existing systems rather than being an afterthought <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>.
3.  **Consider Additional Use Cases:** Don't stop at a single report. Building a user experience (UX) around AI analysis, with features like search filters and exports, can transform a one-off project into a company-wide resource <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>.

Ultimately, LLMs can transform seemingly impossible tasks into routine operations <a class="yt-timestamp" data-t="08:42:00">[08:42:00]</a>. It's not about replacing human analysis, but augmenting it and removing human bottlenecks, thereby unlocking entirely new possibilities <a class="yt-timestamp" data-t="08:50:00">[08:50:00]</a>. The tools and techniques are available today to turn customer data into gold <a class="yt-timestamp" data-t="09:29:00">[09:29:00]</a>.