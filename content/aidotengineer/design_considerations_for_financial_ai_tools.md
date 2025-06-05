---
title: Design considerations for financial AI tools
videoId: MWTJIAwAAnk
---

From: [[aidotengineer]] <br/> 

Brightwave, founded by Mike Con, develops a research agent designed to digest vast corpuses of content within the financial domain <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This technology addresses the significant data processing challenges faced by finance professionals <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Addressing Financial Data Processing Challenges

Financial tasks, such as due diligence in competitive deal processes, require quickly getting to conviction ahead of other teams and spotting critical risk factors from thousands of pages of content <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Mutual fund analysts during earnings season face a universal coverage of 80-120 names, involving calls, transcripts, and filings, making it a non-trivial problem to understand market dynamics at both sector and individual ticker levels <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. Similarly, in confirmatory diligence, reviewing hundreds of vendor contracts to spot early termination clauses or understand thematic negotiation patterns is "frankly not a human level intelligence task" <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. Junior analysts are often put in a "meat grinder" tasked to do the impossible on extremely tight deadlines <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. This highlights the [[challenges_in_data_processing_for_finance_professionals | challenges in data processing for finance professionals]].

The transition from manual financial work to computational tools can be paralleled with the advent of spreadsheets in 1978 <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. Initially, running numbers was cognitively demanding and time-intensive <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Now, tools allow for a substantially increased sophistication of thought, enabling greater [[efficiency_improvements_with_ai_in_financial_analysis | efficiency improvements with AI in financial analysis]] <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. AI systems, including [[knowledge_agents_in_financial_research | knowledge agents]], can digest volumes of content and accelerate meaningful work by orders of magnitude, improving efficiency and time-to-value <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

## Core Design Challenges for Financial AI Agents

A primary [[design_challenges_for_ai_agents | design challenge for AI agents]] in finance is revealing the thought process of a system that has considered thousands of pages of content in a useful and legible way <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. This is a new product architecture problem that did not exist previously <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

### Limitations of Current Models and Approaches

*   **Beyond Chat:** While chat interfaces are a common focus, they are likely "not enough" for complex financial analysis <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **Non-Reasoning Models:** Current non-reasoning models perform "greedy local search," leading to fidelity issues <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. A 5-10% error rate in extracting information, when chained, can exponentially increase the likelihood of errors <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. The ideal winning systems will perform end-to-end Reinforcement Learning (RL) over tool use calls, allowing for locally suboptimal decisions to achieve globally optimal outputs <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. However, intelligently availing oneself of tools to achieve globally optimal outputs remains an open research problem <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   **User Skill vs. Product Scaffolding:** Users are unlikely to become prompting experts, a skill that can take over a thousand hours to develop <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. Therefore, the "scaffolding that products put in place" to orchestrate workflows and shape system behavior is crucial. Verticalized product workflows, which specify intent and offload the burden from the user, are likely to be enduring <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

### Archetypal Design Patterns for Autonomous Agents

To ensure [[effective_design_of_ai_in_products | effective design of AI in products]], autonomous agents should mimic the human decision-making process <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>:
1.  **Assess Content:** Identify relevant document sets from SEC filings, earnings call transcripts, knowledge graphs, or news <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
2.  **Distill Findings:** Extract findings that substantiate hypotheses or investment theses from these documents <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
3.  **Enrich and Error Correct:** This step is extremely powerful. Models can self-correct by being asked if a finding is factually entailed by a document or if an entity is indeed an organization <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. It's more effective to do this as a secondary call rather than within the same Chain of Thought <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
4.  **Synthesis:** Weave together fact patterns from many documents into a coherent narrative <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
5.  **Human Oversight:** A "control loop" with human oversight is critical for [[guidelines_for_developing_proactive_ai_systems | proactive AI systems]] <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. The ability to "nudge" the model with directives or to select an interesting thread to pull is vital because human analysts have access to non-digitized information, such as conversations with management or portfolio manager insights <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. This "taste making" is where the most powerful products will lean <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

### System Architecture and Tool Selection

*   **Avoid Anthropomorphism:** Overly anthropomorphizing systems (e.g., "portfolio manager agent," "fact checker") constrains flexibility if the design needs of the compute graph change <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   **Unix Philosophy:** Adopt the Unix philosophy of simple tools that do one thing well and work together, with text as a universal interface <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
*   **Price-Performance Frontier:** The efficiency frontier for compute and performance/price trade-off will continue to move <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. This necessitates careful selection of which tool, system, or model to use for each node in the compute graph <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.

## The Latency Trap and User Experience

A significant consideration for [[Best Practices for Building AI Systems | building AI systems]] is the "latency trap" <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. For agentic systems, it's easy to assume high quality outputs in a short time, but often, the quality is uncertain <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>. The impulse response for the user—how quickly they receive feedback and refine their mental model of the system—is crucial <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. If the feedback loop is 8-20 minutes, users won't interact enough to develop fluency with the system, leading to low user faculty <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.

## Challenges and Solutions in Synthesis

Synthesis is where much of the "magic happens" in these systems <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.

*   **Output Length Limitations:** Models struggle to produce very long, coherent, novel outputs (e.g., 50,000 tokens) because instruction tuning demonstrations have a characteristic short output length <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>. Current state-of-the-art models like A1 still typically produce only 2,000-3,000 tokens <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.
*   **Decomposition of Instructions:** With large input context windows, information is compressed into a set of tokens <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>. To get higher quality, more information-dense outputs, research instructions should be decomposed into multiple sub-themes <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>. This allows for more focused and specific responses.
*   **Recombinative Reasoning:** The presence of recombinative reasoning demonstrations in training corpuses is low <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>. While models can internalize a single document and create new content from it, it's challenging to get high-quality, intelligent analysis from weaving together disparate fact patterns from *multiple* documents <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.
*   **Complex Real-World Situations:** Models have practical limitations in managing complex real-world situations, such as temporality (e.g., understanding changes from mergers and acquisitions) <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>. It is crucial to propagate evidentiary passages with metadata that contextualizes findings <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.

## Brightwave's Approach to Revealing Thought Processes

Brightwave aims to present AI-generated insights as an "interactive surface" rather than just a static report <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>.

*   **Details on Demand:** The ability to give users details on demand is extremely important <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.
*   **Interactive Citations:** Users can click on a citation to get additional context, including not just the source document but also "what the model was thinking" <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.
*   **Structured Interactive Outputs:** These allow users to "pull the thread" and inquire further about specific findings, like rising capital expenditure <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>.
*   **Highlighting and Interrogation:** Any passage of text can be highlighted, and users can ask for implications or additional details <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.
*   **High-Dimensional Data Structure:** The model's discoveries from reading documents are treated as a high-dimensional data structure, with the report being one view <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>.
*   **Audit Trail:** Especially in finance, being able to see "the receipts" or the audit trail for the system's analysis is crucial <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>. This includes laying out all findings (e.g., fundraising timeline, ongoing litigation) <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>.
*   **Magnifying Glass for Text:** The ability to drill in and get additional details on demand, like a "magnifying glass for text," is extremely important <a class="yt-timestamp" data-t="00:19:39">[00:19:39]</a>.

The final form factor for this class of products has not yet been determined, presenting an "extremely interesting design problem" <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.