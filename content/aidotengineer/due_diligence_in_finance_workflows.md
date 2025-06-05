---
title: Due diligence in finance workflows
videoId: MWTJIAwAAnk
---

From: [[aidotengineer]] <br/> 

Due diligence in finance workflows is a complex and demanding process, particularly in competitive deal environments where speed and accuracy are paramount <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. This often involves digesting vast amounts of content, identifying critical risk factors, and building conviction quickly <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Challenges in Manual Due Diligence
The nature of financial due diligence tasks makes them "non-trivial" for human analysts <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. Challenges include:
*   **Large Data Volumes** Thousands of pages of content need to be reviewed in data rooms <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   **Tight Deadlines** Junior analysts are often tasked with impossible goals under severe time constraints <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   **Cognitive Demands** Understanding market dynamics at both sector and individual ticker levels, or sifting through hundreds of vendor contracts to spot early termination clauses, is cognitively demanding and time-intensive <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>, <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>, <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Human Cost** The manual nature of this work can put professionals "in a meat grinder" due to the high stakes and human cost involved <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>, <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

### Examples of Due Diligence Scenarios
*   **Competitive Deal Process** Assessing thousands of pages in a data room pre-term sheet to gain conviction quickly and spot risk factors that could diminish asset performance <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   **Mutual Fund Analysis** During earnings season, analyzing calls, transcripts, and filings for a universal coverage of 80 to 120 names <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **Confirmatory Diligence** Reviewing hundreds of vendor contracts to identify early termination clauses or understand thematic negotiation strategies across a portfolio <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## The Role of AI in Financial Due Diligence
AI, particularly [[knowledge_agents_in_financial_research | knowledge agents]], are transforming financial due diligence by allowing professionals to bring greater sophistication to analysis <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. Companies like BrightWave build research agents specifically designed to digest very large corpuses of financial content <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

This shift mirrors the impact of spreadsheets on accounting, where the computational tools allowed for more effective and efficient thinking, elevating the job beyond mere "running numbers" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

### Benefits of AI Agents
AI systems can:
*   **Digest Volumes of Content** Rapidly process vast amounts of data that would be impossible for humans <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   **Accelerate Efficiency** Perform meaningful work that accelerates efficiency and time to value by orders of magnitude <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### [[design_considerations_for_financial_ai_tools | Design Considerations]] for AI in Due Diligence
A key [[design_considerations_for_financial_ai_tools | design consideration]] for these systems is how to reveal the AI's thought process to a human user in a useful and legible way, especially when the AI has considered thousands of pages of content <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **Transparency** The final form factor for presenting AI findings is still evolving, as simple chat interfaces are likely insufficient <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. Products need to scaffold workflows and shape system behavior to specify user intent, removing the burden of complex prompting <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   **Mimicking Human Decision-Making** Autonomous agents should mimic the human decision-making process, decomposing tasks like finding public market comparables, assessing relevant document sets, distilling findings, and enriching/error-correcting them <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   **Intermediate Notes** Capturing intermediary notes—what the model believes based on its findings—is extremely useful for transparency and auditability <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.
*   **Self-Correction** Models can self-correct for factual accuracy or entity recognition by asking "is this factually entailed by this document?" or "is this actually an organization?" <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
*   **Synthesis** AI can weave together disparate fact patterns across many documents into a coherent narrative <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. However, current models have limitations in producing very long, coherent, and novel outputs, making it beneficial to decompose research instructions into multiple sub-themes to achieve higher-fidelity, more information-dense results <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>, <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.
*   **Granularity** Being more granular and specific in instructions leads to higher quality outputs <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.
*   **Limitations** State-of-the-art models still face limitations in managing complex real-world situations, such as temporality (e.g., changes after a merger and acquisition or contract addendums) and combining disparate fact patterns across many documents <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>, <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>.
*   **Human Oversight and "Taste-Making"** Human oversight remains crucial. Analysts can nudge the model with directives, pull interesting threads, and leverage their access to non-digitized information (e.g., conversations with management, portfolio manager opinions) to guide the AI <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>, <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>. This "taste-making" is where powerful products will lean <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
*   **User Interface** Interfaces should offer a continuous surface where users can click on citations for context, interact with structured outputs, highlight any passage to ask for implications, and "drill in" for details on demand <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>. This provides an audit trail for the system's findings <a class="yt-timestamp" data-t="00:18:59">[00:18:59]</a>.

## The Latency Trap and User Experience
The "latency trap" highlights a challenge with agentic systems: if the feedback loop for user interaction is too long (e.g., 8-20 minutes), users cannot develop proficiency with the system quickly, leading to low faculty with the product <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>. The product experience should allow users to refine their mental model of how their prompts elicit behaviors from the models <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.