---
title: Agentic prompting and decisionmaking frameworks
videoId: iMzEzLZ9gXw
---

From: [[customaistudio]] <br/> 

Building an AI company involves specific learnings, particularly regarding [[Building Efficient AI Agents with Prompts | prompt engineering]] for AI agents. After approximately eight to nine months in the field, key distinctions have emerged between traditional chatbot prompting and agentic prompting <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Evolution of Prompt Engineering

### The Old Approach: Step-by-Step Instructions
Initially, the approach to prompting focused on fitting every possible decision and the entire decision tree into a single prompt <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. This involved spelling out each decision as a step-by-step conditional statement (e.g., "if this happens then do that") and attempting to capture all possible edge cases <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Tool calls were explained thoroughly, detailing parameters for each action <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Even when attempting to decrease the prompt size, it remained "massive" and "too conditional," leading to constant hallucinations and continuous prompt tweaking <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

An example of an old prompt template included detailed objective, context, and "action parameters" where every single parameter for actions like creating a calendar event was explicitly listed <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. This extensive detailing of parameters is often appended to the prompt anyway by the system when an agent calls a tool, making manual inclusion redundant <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

### The New Approach: Designing Decision Frameworks
The current strategy for [[Building Efficient AI Agents with Prompts | agentic prompt engineering]] shifts from step-by-step instructions to designing decision-making frameworks <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. This involves:
*   **Hardcoding Deterministic Logic**: If a process can be handled by an if node, switch, or filter, it is hardcoded outside the LLM prompt <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. The goal is to identify where the LLM's flexibility is truly needed <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Structured Data Input**: Focusing on how input data is structured before it reaches the LLM and how necessary context (e.g., customer records, order history) is pulled and packaged <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   **Providing Thinking Space**: Instead of detailed instructions, the LLM is given an overarching objective (macro KPI) and clear boundaries or "guardrails" <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. This allows the LLM to act as a "playmaker," reasoning and planning steps within defined constraints, similar to how AlphaGo uncovered new strategies in Go <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.
*   **Focus on Business Context and Guidelines**: Prompts now focus on providing context about the business, input data, specific scenarios, and policies relevant to decision-making <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

A revealing experiment involved asking a chatbot to re-write a hard-worked prompt, which resulted in "significantly better" performance. This demonstrated that LLMs can sometimes be better at making "plays" if given the right balance and guardrails, even by omitting details human engineers might consider necessary <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.

## Key Learnings in Prompt Engineering

*   **Overspecification Leads to Underperformance**: Overly detailed prompts often result in poorer outcomes <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. Providing guardrails rather than lengthy "how-to" instructions is generally more effective <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
*   **Prompts as Hypotheses, Not Code**: Unlike code, where one can predict functionality by reading, prompts require execution and scale testing to evaluate performance and identify issues <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Causality is Slippery**: It is challenging to pinpoint why a prompt did or did not work, unlike debugging code with clear error messages <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. Understanding prompt behavior often comes from extensive testing and familiarity with communication patterns <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Use Emotion in Prompts**: Adding emotional cues (e.g., "ALL CAPS," "DO NOT DO THIS," "ALWAYS REMEMBER") can heighten the LLM's attention, leading to better adherence to instructions <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.
*   **Positive vs. Negative Instructions**: LLMs tend to be worse at understanding negative instructions (e.g., "don't do this") compared to positive ones (e.g., "do this") <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>.

The overarching takeaway is to design the rules of the game and allow the LLM to play within those boundaries, using Key Performance Indicators (KPIs) as a scoreboard <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>.

## Practical Architectures and Examples

### Customer Success Bot Improvement
A customer success bot, which was initially prompted with "if this question, answer this way," saw a 20% improvement in output appropriateness after a framework swap <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. The shift involved providing the bot with options and guidelines to avoid giving refunds, allowing it to navigate scenarios rather than following rigid, pre-defined responses for every edge case <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. This approach aims to decrease the refund rate by allowing the agent to offer upsells or support for technical issues, or to explain when a refund is not qualified <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.

### Planner-Executor-Verifier Architecture
A common and effective [[AI agent frameworks and platforms | agent architecture]] now employs a Planner-Executor-Verifier chain <a class="yt-timestamp" data-t="00:25:38">[00:25:38]</a>:
*   **Planner**: Ingests input data, accesses tool lists and schemas, and creates a step-by-step instruction set for the executor based on the scenario <a class="yt-timestamp" data-t="00:25:44">[00:25:44]</a>. For high-level reasoning, models like Claude 3 Sonnet are often used in this stage <a class="yt-timestamp" data-t="00:25:54">[00:25:54]</a>.
*   **Executor**: Executes the API calls sequentially based on the Planner's instructions <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>.
*   **Verifier**: Confirms that all actions were completed correctly <a class="yt-timestamp" data-t="00:26:06">[00:26:06]</a>.

This modular design is often all that's needed for agents, especially when prompts are pulled dynamically from [[Data management and prompt engineering for AI agents | databases]] rather than hardcoded, which simplifies editing and focuses effort on prompt quality <a class="yt-timestamp" data-t="00:26:12">[00:26:12]</a>.

## Model Selection and Prompting

The choice of LLM model significantly impacts whether a system is production-ready or merely a proof of concept <a class="yt-timestamp" data-t="00:22:14">[00:22:14]</a>. Different models have varying strengths and require slightly different prompting techniques to achieve optimal results <a class="yt-timestamp" data-t="00:23:49">[00:23:49]</a>.

For instance:
*   **Gemini**: Has a long context window and live web search capabilities, making it useful for retrieving and packaging necessary context before hitting the LLM <a class="yt-timestamp" data-t="00:24:35">[00:24:35]</a>. However, it is noted to be less effective at tool calling <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>.
*   **Claude 3.7 Sonnet**: Preferred for high-level reasoning and memory, staying on topic longer, making it suitable for the planner stage in [[AI agent frameworks and platforms | agent architectures]] <a class="yt-timestamp" data-t="00:25:04">[00:25:04]</a>.
*   **GPT-4.5**: Excels at human-sounding, conversational external communication <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>.
*   **Grock**: Has shown strong chatbot experience and access to X (Twitter) data, although its agentic capabilities need more testing <a class="yt-timestamp" data-t="00:27:20">[00:27:20]</a>.

A single prompt can produce a 20% deviation in output quality depending on the model used <a class="yt-timestamp" data-t="00:28:04">[00:28:04]</a>. This highlights the importance of finding the "Goldilocks zone" for model-to-prompt combinations <a class="yt-timestamp" data-t="00:30:25">[00:30:25]</a>. The approach is to first identify the most suitable model for a given scenario, then fine-tune the prompt specifically for that model <a class="yt-timestamp" data-t="00:31:09">[00:31:09]</a>.

## Roadmap and Future Challenges

The roadmap for [[Agentic Operating Systems and their evolution | agentic systems]] and prompting includes:
*   **Live KPI Monitoring and Auto-Triggering A/B Prompt Versions**: Continuously testing and optimizing prompts based on performance metrics <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>. This involves creating "optimization workflows" but faces challenges with causality and the LLM's understanding of negative instructions <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>.
*   **Fine-Tuning Models**: Expected to be the next step for significantly improving outputs and reducing the need for excessive "guardrails" and scaffolding around LLMs <a class="yt-timestamp" data-t="00:31:24">[00:31:24]</a>. Fine-tuning models on specific industry jargon, cadence, and norms (e.g., for a law firm) is anticipated to yield better results <a class="yt-timestamp" data-t="00:32:15">[00:32:15]</a>.
*   **Standardizing Prompting Techniques**: Developing standardized techniques based on scenario and model, while acknowledging that model updates will frequently require adjustments <a class="yt-timestamp" data-t="00:32:34">[00:32:34]</a>.