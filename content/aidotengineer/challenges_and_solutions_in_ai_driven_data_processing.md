---
title: Challenges and solutions in AI driven data processing
videoId: dvft0Gp9sEE
---

From: [[aidotengineer]] <br/> 

This article explores the [[Challenges in AI Development | challenges]] and solutions encountered when using AI, specifically Large Language Models (LLMs), to process and analyze vast amounts of unstructured data, such as sales call transcripts, to derive actionable insights.

## The Challenge of Manual Data Analysis

Analyzing large datasets manually presents significant obstacles. For instance, a single individual working an eight-hour day with no breaks could listen to and take notes on approximately 16 sales calls, each 30 minutes long <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Even with "zero work-life balance," this number only extends to about 32 calls daily <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. To analyze 10,000 sales calls, a task that one CEO set with a two-week deadline, would require 625 days of continuous manual work—nearly two years <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

Manual analysis of a sales call database would involve:
*   Downloading each transcript <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   Reading conversations <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   Deciding if conversations match target personas <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   Scanning hundreds or thousands of lines for key insights <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   Remembering information while writing reports, compiling notes, and citing for future reference <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   Repeating this process 10,000 times <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

The human brain is not equipped to process such vast amounts of information <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Prior to LLMs, analysis methods were either high-quality but unscalable manual approaches or fast but context-lacking keyword analyses <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

## The AI Solution: Analyzing Sales Calls

The intersection of unstructured data and pattern recognition is a "sweet spot" for [[Role of AI in research and data analytics | AI projects]] <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. What might seem like a simple task—using AI to analyze sales calls—actually required solving several interconnected technical [[Challenges and Solutions in Building AI Agents | challenges]] <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

### Key Technical [[Challenges and strategies in AI production | Challenges]] and Solutions

#### Model Selection
*   **Challenge:** Choosing the right model involved balancing intelligence, cost, and speed <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. While GPT-4o and Claude 3.5 Sonnet were the most intelligent options available, they were also the most expensive and slowest <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. Smaller and cheaper models produced an "alarming number of false positives," misclassifying companies or prospect roles without supporting evidence <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. A bad analysis would render the entire project pointless <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   **Solution:** The choice was made to use more expensive models, specifically Claude 3.5 Sonnet, due to their acceptable hallucination rate and accuracy <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

#### Reducing Hallucinations and Ensuring Accuracy
*   **Challenge:** Simply feeding transcripts to the model and asking for answers was not sufficient <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **Solution:** A multi-layered approach was developed <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>:
    *   **Data Enrichment:** Raw transcript data was enriched via Retrieval Augmented Generation (RAG) using both third-party and internal sources <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
    *   **Prompt Engineering:** Techniques like chain of thought prompting were employed to achieve more reliable results <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
    *   **Structured Outputs:** Structured JSON outputs were generated to facilitate citations and create a verifiable trail back to the original transcripts, ensuring confidence in the final results <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. This system reliably extracted accurate company details and meaningful insights <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

#### Cost Management
*   **Challenge:** Maintaining low error rates and performing complex analysis drove up costs significantly, often hitting the 4,000-token output limit for Claude 3.5 Sonnet, requiring multiple requests per transcript analysis <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   **Solution:** Two experimental features were leveraged to dramatically lower costs <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>:
    *   **Prompt Caching:** By caching transcript content, which was reused repeatedly for metadata and insights extraction, costs were reduced by up to 90% and latency by up to 85% <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
    *   **Extended Outputs:** An experimental feature flag in Claude provided access to double the original output context. This allowed for complete summaries to be generated in single passes, avoiding multiple turns and reducing credit consumption <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

These solutions transformed a potential $5,000 analysis into a $500 one, with results delivered in days instead of weeks <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

## Broader Impact and Key Learnings

The AI-driven analysis, initially intended for executive insights, yielded wide-ranging benefits across the organization <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
*   **Marketing:** Used insights to pull customers for branding and positioning exercises <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   **Sales:** Automated transcript downloads, saving dozens of hours weekly <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
*   **Cross-functional:** Teams began asking questions previously unconsidered due to the daunting nature of manual analysis <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

Ultimately, mountains of unstructured data were transformed from a liability into a valuable asset <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

### Key Takeaways:
1.  **Models Matter:** Despite the push for open-source and smaller models, advanced LLMs like Claude 3.5 and GPT-4o could handle tasks other models couldn't <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. The right tool is the one that best fits specific needs <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
2.  **Good Engineering Still Matters:** Significant gains came from traditional software engineering practices, including leveraging JSON structured output, robust database schemas, and proper system architecture <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. [[Challenges in building AI applications | AI engineering]] involves building effective systems around LLMs, requiring thoughtful integration rather than just bolting on AI as an afterthought <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
3.  **Consider Additional Use Cases:** The project extended beyond a single report, evolving into a company-wide resource with a dedicated user experience including search filters and exports <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

This project demonstrated how AI can transform "seemingly impossible tasks into routine operations" <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. The promise of LLMs is not merely faster execution, but unlocking entirely new possibilities by augmenting human analysis and removing bottlenecks <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. Valuable customer data, such as sales calls, support tickets, product reviews, user feedback, and social media interactions, often goes untouched but is now accessible via LLMs <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. The tools and techniques exist to turn this data into valuable insights <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.