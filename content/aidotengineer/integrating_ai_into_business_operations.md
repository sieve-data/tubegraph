---
title: Integrating AI into business operations
videoId: dvft0Gp9sEE
---

From: [[aidotengineer]] <br/> 

Traditionally, analyzing vast amounts of unstructured data like sales calls has been an impossible or resource-intensive task for businesses <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This limitation often meant valuable insights from customer interactions remained untapped <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. However, modern large language models (LLMs) now offer a solution to [[transformative_role_of_ai_in_business_operations | transform]] these seemingly impossible tasks into routine operations, augmenting human analysis and removing bottlenecks <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.

## The Challenge of Data Analysis

Consider the task of analyzing 10,000 sales calls to understand an ideal customer profile (ICP) <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
A single person, working an 8-hour day with no breaks, could listen to 16 calls <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Even with extreme work-life imbalance, this number only reaches 32 calls daily <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. To manually analyze 10,000 sales calls would require approximately 625 days of continuous work, or nearly two years, making it an unfeasible endeavor for a human <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

Manual analysis of sales call data typically involves:
*   Downloading and reading each transcript <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   Deciding if a conversation matches a target persona <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   Scanning hundreds or thousands of lines for insights <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   Compiling notes, reports, and citations <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   Repeating this process 10,000 times <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

Before LLMs, approaches to this type of analysis fell into two categories <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>:
1.  **Manual Analysis:** High quality but completely unscalable <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
2.  **Keyword Analysis:** Fast and cheap but often missed context and nuance <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

This problem highlights a "sweet spot for AI projects": the intersection of unstructured data and pattern recognition <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## AI as a Solution: A Case Study

At Pulley, the goal was to analyze 10,000 sales calls within two weeks to refine their ideal customer profile beyond "venture-backed startups" to more specific segments like "CTO of an early-stage venture-backed crypto startup" <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. This task, previously impossible or requiring a dedicated team for weeks, was accomplished by a single AI engineer in about a fortnight <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

### Technical Implementation

Solving this seemingly simple task required addressing several interconnected technical challenges <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

#### 1. Choosing the Right Model
The initial decision involved selecting an appropriate large language model <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
*   **Options considered:** GPT-4o and Claude 3.5 Sonnet <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
*   **Challenge with smaller models:** While cheaper and faster, smaller models produced an "alarming number of false positives," misclassifying transcripts or incorrectly identifying prospect roles <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   **Decision:** The more expensive models (Claude 3.5 Sonnet was chosen) were necessary due to their acceptable hallucination rates, ensuring the analysis could be trusted <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

#### 2. Reducing Hallucinations
A multi-layered approach was developed to reduce hallucinations and ensure reliable results <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>:
*   **Data Enrichment:** Raw transcript data was enriched via Retrieval Augmented Generation (RAG) using both third-party and internal sources <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Prompt Engineering:** Techniques like "chain of thought prompting" were employed to elicit more reliable outputs from the model <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
*   **Structured Outputs:** Generating structured JSON outputs with citations allowed for a verifiable trail back to the original transcripts, increasing confidence in the results <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

This system reliably extracted accurate company details and meaningful insights, crucial for [[customer_success_with_ai_solutions | customer success]] <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

#### 3. Cost Optimization
High accuracy and low error rates significantly drove up costs, often hitting the 4,000 token output limit for Claude 3.5 Sonnet, requiring multiple requests per transcript <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. Two experimental features were leveraged to dramatically reduce costs:
*   **Prompt Caching:** Reusing the same transcript content repeatedly for metadata extraction and insights allowed for cost reductions of up to 90% and latency reductions of up to 85% <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
*   **Extended Outputs:** An experimental feature flag on Claude provided double the original output context, enabling complete summaries in single passes and saving multiple rounds of credits <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

These optimizations transformed a potential $5,000 analysis into a $500 one, delivering results in days instead of weeks <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

## Organizational Impact and Learnings

The [[introduction_and_application_of_ai_in_business_platforms | impact of this AI analysis]] extended far beyond its initial goal for the executive team <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
*   **Marketing Team:** Utilized the insights to pull customers for branding and positioning exercises <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   **Sales Team:** Automated transcript downloads, saving dozens of hours weekly <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
*   **Broader Impact:** Teams began asking questions previously unconsidered due to the daunting nature of manual analysis <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

This project transformed mountains of unstructured data from a liability into a valuable asset <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

### Key Takeaways for [[implementing_ai_in_enterprises | Implementing AI in Enterprises]]

1.  **Models Matter:** Despite the appeal of open-source and smaller models, more powerful models like Claude 3.5 and GPT-4o were essential for handling complex tasks <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. The right tool is not always the most powerful, but the one that best fits specific needs <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
2.  **Good Engineering Still Matters:** Significant gains came from traditional software engineering practices, such as leveraging JSON structured output, robust database schemas, and proper system architecture <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. AI engineering involves building effective systems around LLMs, meaning AI must be [[integrating_ai_into_natural_workflows | thoughtfully integrated into existing systems]] and architectures, not merely an afterthought <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. This highlights the importance of [[using_existing_enterprise_systems_for_ai_integration | integrating AI agents into existing infrastructure]].
3.  **Consider Additional Use Cases:** The project evolved beyond a single report into a company-wide resource with a dedicated user experience, including search filters and exports <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. Building a simple yet flexible tool can transform a one-off project into a continuous asset <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. This demonstrates the value of considering [[enterprise_leadership_and_organizational_alignment_for_ai_initiatives | organizational alignment for AI initiatives]].

## Conclusion

The successful implementation of AI for sales call analysis demonstrates how AI can transform seemingly impossible tasks into routine operations <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. The true promise of LLMs like Claude, ChatGPT, and Gemini lies not just in doing things faster, but in unlocking entirely new possibilities for understanding and leveraging customer data <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

Valuable sources of insight, such as sales calls, support tickets, product reviews, user feedback, and social media interactions, often go untouched <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. However, with current tools and techniques, these are now readily accessible via large language models, allowing companies to turn their data into a golden asset <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.