---
title: Challenges in data processing for finance professionals
videoId: MWTJIAwAAnk
---

From: [[aidotengineer]] <br/> 

Finance professionals face significant challenges in processing and analyzing vast amounts of unstructured data, leading to demanding workloads and potential for errors when handled manually <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. Brightwave, a company specializing in AI-powered research agents, aims to address these issues by digesting large corpuses of financial content and performing meaningful analytical work <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a><a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

## The Human Cost of Manual Data Processing

The sheer volume and complexity of financial data often overwhelm human analysts. Mike Kahn, founder and CEO of Brightwave, notes that these tasks are "not a human level intelligence task" <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Junior analysts, in particular, are often tasked with impossible assignments under extremely tight deadlines, leading to a "deep sense of empathy for the stakes and the human cost of doing this work manually" <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a><a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

### Specific Workflow Challenges

*   **[[Due diligence in finance workflows | Due Diligence]]**: In a competitive deal process, professionals may encounter data rooms with thousands of pages of content. The challenge is to quickly gain conviction and identify critical risk factors that could diminish asset performance before other teams <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a><a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   **Earnings Season**: Mutual fund analysts covering 80-120 names face an overwhelming amount of calls, transcripts, and filings. Understanding market dynamics at both sector and individual ticker levels is a non-trivial problem <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a><a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   **Contract Review**: In confirmatory diligence, dealing with 80-800 vendor contracts requires spotting early termination clauses and understanding thematic negotiation patterns across an entire portfolio <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a><a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

### Historical Parallel

The current situation for finance professionals is likened to the pre-spreadsheet era for accountants in 1978 <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. Accountants would manually "run the numbers" on physical spreadsheets, a cognitively demanding, important, and time-intensive task <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Just as computational spreadsheets revolutionized accounting by allowing more sophisticated thought and efficiency, AI tools are expected to do the same for financial analysis <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a><a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

## Technical Challenges in AI for Financial Data Processing

While AI offers immense potential for [[efficiency_improvements_with_ai_in_financial_analysis | efficiency improvements]], building effective AI tools for finance involves several technical hurdles:

### Non-Reasoning Models and Error Propagation
Many current models perform "greedy local search," leading to fidelity issues. For example, a 5-10% error rate in extracting organizations from a Reuters article can lead to exponential errors when chaining multiple such calls <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a><a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. Winning systems will need to perform end-to-end Reinforcement Learning (RL) over tool use calls, allowing for locally suboptimal decisions to achieve globally optimal outputs <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. However, intelligently availing oneself of knowledge graphs and other tools for globally optimal outputs remains an open research problem <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a><a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

### The Latency Trap
A significant challenge for agentic systems is the "latency trap" <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. If the feedback loop for a user is too long (e.g., 8-20 minutes for a report), users cannot perform many iterations in a day, which limits their ability to develop proficiency and trust with the system <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a><a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>. The product needs to provide quick "impulse response" to the user's input to facilitate learning and refinement of their mental model <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a><a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.

### Limitations in Synthesis
*   **Output Length**: Models often struggle to produce very long, coherent, and novel outputs (e.g., 50,000 words), as the instruction tuning datasets typically have characteristic output lengths <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a><a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>. This means a very large input context window gets compressed into shorter, less information-dense outputs <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a><a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.
*   **Recombinative Reasoning**: The ability to synthesize disparate fact patterns from multiple documents (e.g., across biomedical literature or financial reports) is limited <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a><a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>. This is because demonstrations of such complex recombinative reasoning are low in post-training corpuses <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a><a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.
*   **Complex Real-World Situations**: State-of-the-art models still have limitations in managing complex real-world situations, such as temporality (e.g., distinguishing financial statements before and after a merger) and propagating metadata that contextualizes findings <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a><a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a><a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.

## [[Design considerations for financial AI tools | Product Design and User Interaction]]

Designing effective AI tools for finance is not just a UI/UX or product architecture problem; it involves revealing the thought process of a system that has considered thousands of pages of content in a useful and legible way <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a><a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

### Mimicking Human Decision-Making
An ideal autonomous agent should mimic the human decision-making process by decomposing tasks <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. This involves:
1.  Looking for public market comparables (e.g., SEC filings, earnings call transcripts) <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
2.  Assessing relevant content from knowledge graphs or news <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
3.  Distilling findings that substantiate hypotheses <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
4.  Enriching and error-correcting those findings <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

### User Interaction and Oversight
*   **Intermediate Notes**: Allowing the model to "think out loud" with intermediary notes about what it believes based on findings is extremely useful <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.
*   **Self-Correction**: Models can self-correct by being asked to verify accuracy (e.g., "is this factually entailed by this document?") as a secondary call <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a><a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
*   **Human Oversight**: Human oversight is crucial, allowing analysts to "nudge the model" with directives or by selecting interesting threads to explore <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a><a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. This is because human analysts possess external information (e.g., conversations with management, portfolio manager opinions) not available to the AI <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

### The "Surface" Interface
Instead of a simple chat interface, the final form factor for these products is still evolving <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a><a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. It's envisioned as a "surface" that reveals the model's thought process <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>. Key features include:
*   **Details on Demand**: The ability to click on citations for additional context, including what the model was "thinking" <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a><a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.
*   **Interactive Outputs**: Structured outputs that allow users to "pull the thread" and ask for more details on specific points <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a><a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>.
*   **Interrogating Findings**: The ability to highlight any passage of text and ask for implications or further information <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a><a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>.
*   **Audit Trail**: Providing visibility into all findings as a high-dimensional data structure, allowing users to "turn over that cube" and see the "receipts" or audit trail of the system's analysis <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a><a class="yt-timestamp" data-t="00:18:59">[00:18:59]</a>. This allows investor/analyst "taste" to come into play, enabling them to zoom in on what catches their eye, like patent litigation or a factory fire <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a><a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.

These [[design_considerations_for_financial_ai_tools | design patterns]] aim to allow AI systems to handle the complex, unstructured data challenges in finance, while maintaining human oversight and facilitating user interaction, ultimately driving greater efficiency and deeper insights.