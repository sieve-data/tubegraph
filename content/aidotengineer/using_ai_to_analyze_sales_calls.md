---
title: Using AI to analyze sales calls
videoId: dvft0Gp9sEE
---

From: [[aidotengineer]] <br/> 

Analyzing large volumes of sales call data manually is an almost impossible task for humans, often taking years and requiring extensive resources <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. For example, analyzing 10,000 sales calls would take approximately 625 days of continuous work, equivalent to nearly two years <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. The human brain is not equipped to process such vast amounts of information <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

Traditional approaches to analyzing sales calls included manual, high-quality but unscalable methods, or fast, cheap keyword analyses that lacked context and nuance <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. However, modern large language models (LLMs) offer a solution for analyzing unstructured data and recognizing patterns <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. What once required a dedicated team working for weeks, or was considered impossible, can now be accomplished by a single AI engineer in about two weeks <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## The Challenge

A specific goal was set to analyze 10,000 sales calls within two weeks to perform a comprehensive analysis of the ideal customer profile (ICP) for Pulley, a company whose ICP was previously defined broadly as venture-backed startups <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. To refine this, the aim was to identify specific personas, such as "CTO of an early-stage venture-backed crypto startup" <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

The challenge lay in the sheer volume of data, consisting of thousands of hours of sales representatives speaking directly with customers <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. A [[challenges_of_manual_sales_call_analysis | manual analysis]] would involve:
*   Downloading and reading each transcript <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   Determining if the conversation matched the target persona <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   Scanning hundreds or thousands of lines for key insights <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   Remembering information while compiling notes, reports, and citations <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   Repeating this process 10,000 times <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## Technical Implementation

While seemingly simple ("just use AI to analyze sales calls"), this project required addressing several interconnected technical challenges <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

### Model Selection
The first critical decision was choosing the right LLM <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. GPT-4o and Claude 3.5 Sonnet were identified as the most intelligent options available, despite being the most expensive and slowest <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. Experiments with smaller, cheaper models quickly revealed their limitations, as they produced an alarming number of false positives <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. For instance, they might incorrectly classify a transcript as crypto-related due to a brief mention of blockchain features, or misidentify a prospect as a founder without supporting evidence <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. Ultimately, Claude 3.5 Sonnet was chosen because its hallucination rate was acceptable, ensuring data reliability <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

### Reducing Hallucinations
A multi-layered approach was developed to reduce hallucinations and ensure reliable results <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>:
1.  **Data Enrichment**: Raw transcript data was enriched using Retrieval Augmented Generation (RAG) from both third-party and internal sources <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
2.  **Prompt Engineering**: Techniques like chain-of-thought prompting were employed to guide the model towards more reliable outputs <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
3.  **Structured Outputs**: Generating structured JSON outputs where possible allowed for the creation of verifiable citations <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

This combined approach created a system that could reliably extract accurate company details and meaningful insights, with a verifiable trail back to the original transcripts, ensuring confidence in the final results <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

### Cost Optimization
While effective, the extensive analysis and low error rate significantly drove up costs, often hitting the 4,000-token output limit of Claude 3.5 Sonnet, requiring multiple requests per transcript <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. Two experimental features were leveraged to dramatically reduce expenses:
1.  **Prompt Caching**: By caching transcript content, which was often reused for extracting metadata and insights, costs were reduced by up to 90% and latency by up to 85% <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
2.  **Extended Outputs**: An experimental feature flag in Claude allowed access to double the original output context. This enabled the generation of complete summaries in single passes, avoiding multiple turns and reducing credit consumption <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

These optimizations transformed a $5,000 analysis into a $500 one, delivering results in days instead of weeks <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

## Impact and Key Takeaways

The project's most surprising aspect was its wide-ranging impact across the organization <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. What began as an executive-level project to generate insights became useful across multiple departments:
*   The marketing team could easily identify customers for branding and positioning exercises <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   The sales team automated transcript downloads, saving dozens of hours weekly <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
*   Teams began asking questions that were previously considered too daunting for [[challenges_of_manual_sales_call_analysis | manual analysis]] <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

Ultimately, mountains of unstructured data were transformed from a liability into a valuable asset <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

### Key Takeaways:
1.  **Models Matter**: Despite the push for open-source and cheaper models, powerful LLMs like Claude 3.5 and GPT-4o demonstrated superior capabilities for complex tasks <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. The right tool is the one that best fits specific needs, not always the most powerful <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
2.  **Good Engineering Still Matters**: Significant gains were achieved through solid software engineering practices, including leveraging JSON structured output, good database schemas, and proper system architecture <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. [[integrating_ai_into_business_operations | AI engineering]] involves building effective systems around LLMs, ensuring AI is thoughtfully integrated, not merely bolted on <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
3.  **Consider Additional Use Cases**: The project evolved beyond a single report by building an entire user experience around the AI analysis, including search filters and exports <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. This transformed a one-off project into a company-wide resource <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.

This project demonstrates how AI can transform seemingly impossible tasks into routine operations <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. It's not about replacing human analysis but augmenting it and removing bottlenecks, thereby unlocking entirely new possibilities <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. Valuable customer data such as sales calls, support tickets, product reviews, user feedback, and social media interactions, often overlooked, are now highly accessible via large language models, offering significant insights <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.