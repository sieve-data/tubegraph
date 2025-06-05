---
title: Large language models for data analysis
videoId: dvft0Gp9sEE
---

From: [[aidotengineer]] <br/> 

Analyzing vast amounts of unstructured data, such as thousands of sales calls, can be an impossible task for human teams due to the sheer volume and time constraints <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. This challenge highlights a significant bottleneck in gleaning insights from critical business interactions <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. Historically, approaches were either high-quality but unscalable manual analysis, or fast but context-lacking keyword analysis <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. However, the advent of [[large_language_models_in_ai_agents | modern large language models]] (LLMs) has transformed this landscape, making complex data analysis achievable for a single AI engineer in a matter of weeks <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

## The Challenge of Unstructured Data
At Pulley, a key objective was to analyze 10,000 sales calls within two weeks to refine their ideal customer profile (ICP), moving beyond a broad "venture-backed startups" to more specific segments like "CTO of an early-stage venture-backed crypto startup" <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a> <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Manual analysis of such a dataset would involve:
*   Downloading and reading each transcript <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   Classifying conversations based on target personas <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   Scanning for key insights and compiling notes with citations <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

To analyze 10,000 30-minute calls manually, it would take approximately 625 days of continuous work, equivalent to nearly two years <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a> <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. This highlights the human brain's inability to process such vast amounts of information efficiently <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

## Leveraging Large Language Models
The intersection of unstructured data and pattern recognition is a "sweet spot" for AI projects <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. While seemingly simple, using AI for sales call analysis required addressing several technical challenges <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

### Model Selection and Performance
For this project, [[experiments_with_large_language_models_and_ai_assisted_work | experiments with Large Language Models and AI Assisted Work]] revealed that model choice was crucial <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. Although smaller, cheaper models were tempting, they quickly showed limitations, producing an alarming number of false positives <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. For example, they might mistakenly classify a company as crypto-related due to a fleeting mention of blockchain features or incorrectly identify a prospect as a founder without supporting evidence <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

The project prioritized accuracy, recognizing that a bad analysis would render the entire effort pointless <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. Therefore, the decision was made to use more expensive yet intelligent options like GPT-4o and Claude 3.5 Sonnet, which offered an acceptable hallucination rate <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a> <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. Claude 3.5 Sonnet was ultimately chosen <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

### Reducing Hallucinations and Ensuring Reliability
To combat hallucinations and enhance reliability, a multi-layered approach was developed <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>:
1.  **Data Enrichment:** Raw transcript data was enriched using Retrieval Augmented Generation (RAG) from both third-party and internal sources <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
2.  **Prompt Engineering:** Techniques like chain-of-thought prompting were employed to guide the model towards more reliable results <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
3.  **Structured Outputs:** Generating structured JSON outputs allowed for automatic citation generation, creating a verifiable trail back to the original transcripts <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

This robust system reliably extracted accurate company details and meaningful insights with high confidence in the final results <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

### Cost Optimization
Initial high costs due to extensive analysis and low error rate requirements, often hitting the 4,000 token output limit for Claude 3.5 Sonnet, necessitated multiple requests per transcript <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. Two experimental features significantly reduced these costs:
1.  **Prompt Caching:** Reusing the same transcript content for repeated analysis (metadata and insights extraction) reduced costs by up to 90% and latency by up to 85% <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
2.  **Extended Outputs:** An experimental feature flag provided double the original output context, allowing for complete summaries in single passes instead of multiple turns <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

These optimizations transformed a $5,000 analysis into a $500 one, delivering results in days instead of weeks <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

## Impact and Future Possibilities
What began as a project for the executive team yielded wider organizational benefits <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>:
*   **Marketing Team:** Able to quickly identify customers for branding and positioning exercises <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   **Sales Team:** Automated transcript downloads, saving dozens of hours weekly <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
*   **New Questions:** Teams began asking questions previously considered too daunting for manual analysis <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

The project transformed unstructured data from a liability into an asset <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

### Key Takeaways
> [!info] Models Matter <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>
> Despite the push for open-source and cheaper models, high-performing models like Claude 3.5 and GPT-4o could handle tasks others could not <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. The right tool is the one that best fits specific needs <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

> [!info] Good Engineering Still Matters <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>
> Significant wins came from traditional software engineering principles: leveraging JSON structured output, good database schemas, and proper system architecture <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. [[AI Engineering and Large Language Models at Jane Street | AI engineering]] involves building effective systems around LLMs, ensuring they are thoughtfully integrated, not merely bolted on <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

> [!info] Consider Additional Use Cases <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>
> Building a flexible tool with features like search filters and exports transformed a one-off report into a company-wide resource <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

This project demonstrated how AI can transform seemingly impossible tasks into routine operations <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. LLMs augment human analysis and remove bottlenecks, not just doing things faster, but unlocking entirely new possibilities <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

Valuable sources of insight such as sales calls, support tickets, product reviews, user feedback, and social media interactions often go untouched <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. However, [[large_language_models_in_ai_agents | large language models]] now make these data accessible, enabling companies to turn them into valuable assets <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.