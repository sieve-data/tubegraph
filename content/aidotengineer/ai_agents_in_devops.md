---
title: AI agents in DevOps
videoId: VZzUhELgYk4
---

From: [[aidotengineer]] <br/> 

Diamond, an AI veteran with 15 years in the field, shares insights on [[building_ai_agents_in_the_enterprise_sdlc | building AI agents]] at DataDog, specifically focusing on the development of a "DevOps engineer who never sleeps" <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. His background includes work at Microsoft Cortana, Amazon Alexa, Meta (PyTorch), and an AI startup focused on a DevOps assistant <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. DataDog's current endeavor is "Bits AI," an AI assistant designed to help with DevOps challenges <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## DataDog and AI: A Historical Perspective

DataDog functions as an observability and security platform for cloud applications, primarily focused on helping users observe system happenings and take action, making systems safer and more DevOps-friendly <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. DataDog has been shipping AI since approximately 2015, integrated into features like proactive alerting, root cause analysis, impact analysis, and change tracking, though not always overtly presented as "AI products" <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

## The Current Era Shift in AI

A significant "era shift" is underway in AI, comparable to the advent of the microprocessor or the shift to SaaS <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This shift is characterized by:
*   Bigger, smarter models <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>
*   Reasoning capabilities <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>
*   Multimodal AI <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>
*   "Foundation model wars" <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>
*   Intelligence becoming "too cheap to meter" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>

This shift leads to rapid growth in AI products like Cursor and increased user expectations <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. DataDog aims to leverage these advancements by moving up the stack, providing [[agent_frameworks_and_orchestration_layers_in_ai_engineering | AI agents]] that use the DataDog platform on behalf of customers <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. This requires work in agent development, evaluation, and new types of observability <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

## DataDog's AI Agents in Beta

DataDog is currently developing several [[building_ai_agents_in_the_enterprise_sdlc | AI agents]] in private beta:

### AI Software Engineer
This agent proactively observes and acts on errors, analyzes them, identifies causes, and proposes solutions <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   **Capabilities:** Generates code fixes, reduces on-call incidents, and can even create recursion tests to prevent future issues <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
*   **Integration:** Offers options to create Pull Requests in GitHub or open diffs in VS Code for editing <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. This significantly reduces manual coding, testing, and overall human time spent <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.

### AI On-Call Engineer
Designed to handle 2 AM alerts and reduce the frequency of engineer pages <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Workflow:**
    1.  Kicks off proactively when an alert occurs <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
    2.  Situationally orients itself by reading runbooks and grabbing alert context <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
    3.  Investigates by looking through logs, metrics, and traces, acting in a loop to understand the situation <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
    4.  Automatically runs investigations and provides summaries/information before a human even gets to their computer <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   **Human-AI Collaboration:** A new page allows for human-AI collaboration, enabling users to verify agent actions, learn from them, and build trust <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. Users can see the reasoning behind hypotheses, what the agent found, and the steps taken from runbooks <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Reasoning and Remediation:** The agent develops hypotheses, reasons over them, tests ideas using tools (e.g., running queries against logs/metrics), and validates or invalidates each hypothesis <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. If a root cause is found, it can suggest remediations like paging another team or scaling infrastructure <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. It can also integrate with existing DataDog workflows <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
*   **Post-Mortem Generation:** After an incident is remediated, the agent can write a post-mortem, summarizing what occurred and the actions taken by both the agent and humans <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.

## Lessons Learned Building AI Agents

DataDog has identified several key learnings from developing these [[building_ai_agents_in_the_enterprise_sdlc | AI agents]]:

### 1. Scoping Tasks for Evaluation
Building quick demos is easy, but robust evaluation is harder <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   **Define "Jobs to Be Done":** Clearly understand the step-by-step human workflow and how a human would evaluate it <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   **Vertical, Task-Specific Agents:** Focus on specific tasks rather than generalized agents <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
*   **Measurable and Verifiable:** Ensure each step is measurable and verifiable, as this is a common pain point <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   **Domain Experts as Design Partners:** Use domain experts for evaluation and verification, not for writing code or rules, due to the stochastic nature of AI models <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   **Eval, Eval, Eval:** Deeply consider evaluation from the start. This includes offline, online, and "living" evaluation sets with end-to-end measurements <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. Instrumenting product usage is crucial for feedback <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

### 2. Building the Right Team
*   **Optimistic Generalists:** While one or two ML experts are helpful, the core team should consist of optimistic generalists who can write code effectively and adapt quickly to ambiguity <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
*   **UX/Frontend Importance:** User experience and frontend development are crucial for effective collaboration with agents <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
*   **AI-Augmented Teammates:** Team members should be excited about being AI-augmented, exploring new capabilities, and adapting to a rapidly changing field <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.

### 3. The Changing User Experience (UX)
The traditional UX patterns are evolving, and developers must be comfortable with this <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. DataDog favors agents that function more like human teammates rather than requiring numerous new pages or buttons <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.

### 4. Observability Matters
Even with agents, observability is paramount and should not be an afterthought <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.
*   **Debugging Complex Workflows:** AI agent workflows are complex, requiring situational awareness for debugging <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
*   **LM Observability:** DataDog's "LM Observability" view helps monitor LLMs, providing a single pane of glass for diverse interactions, hosted models, and API usage <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.
*   **Agent Graph:** For multi-step, complex agent calls (potentially hundreds of calls or decisions), a specialized "agent graph" provides a human-readable view to quickly identify errors <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

## The "Bitter Lesson" and Agents as Users

A key insight, referred to as the "agent or application layer bitter lesson," suggests that general methods leveraging new, off-the-shelf models are ultimately the most effective <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>. Fine-tuning specific models can be quickly surpassed by general advancements in foundation models <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>. The ability to easily swap and try out new models is crucial <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.

Diamond also emphasizes the future where AI agents will become users of platforms like DataDog <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>. It's estimated that agents could surpass humans as users within the next five years <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. Therefore, product development should consider not just human users, but also how third-party [[integration_of_ai_coding_agents_with_thirdparty_tools | agents]] like Claude might directly use the platform, requiring clear API documentation and context <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.

## Future Outlook for AI in DevOps

The future of AI in DevOps is expected to be "weird and fun," with accelerating AI advancements <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.
*   **DevSecOps Agents For Hire:** DataDog aims to offer teams of DevSecOps [[building_ai_agents_in_the_enterprise_sdlc | agents for hire]] that can directly use their platform and handle tasks like on-call duties <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.
*   **Agents as Customers:** Companies building SRE, coding, and other types of [[scaling_ai_agents_in_production | agents]] will increasingly use platforms like DataDog as customers <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.
*   **Accelerated Innovation:** Small companies will be able to leverage automated developers (like Cursor or Devin) to bring ideas to life, and agents for operations and security, enabling an order of magnitude more ideas to reach the real world <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.