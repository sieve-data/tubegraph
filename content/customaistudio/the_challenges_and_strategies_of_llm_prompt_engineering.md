---
title: The challenges and strategies of LLM prompt engineering
videoId: iMzEzLZ9gXw
---

From: [[customaistudio]] <br/> 

Prompt engineering for Large Language Models (LLMs) has evolved significantly, shifting from rigid, step-by-step instructions to more flexible decision-making frameworks. This evolution brings both challenges and new strategies for building effective AI systems <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Evolution of Prompting: From Step-by-Step to Decision Frameworks

Initially, prompt engineering for AI agents was similar to chatbot prompting, where developers attempted to fit every possible decision and action, including intricate decision trees and step-by-step conditionals, directly into a single prompt <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. This approach involved spelling out each decision and trying to capture all possible edge cases in one massive prompt <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. Even tool calls were thoroughly explained within the prompt, detailing parameters and input data <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

The old prompt template often included objective, context, and detailed action parameters, such as every parameter required for creating a calendar event <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. However, this verbose method led to significant issues <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

### Challenges of the Old Approach
*   **Constant Hallucinations:** Over-specifying led to frequent inaccuracies and irrelevant outputs <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   **Continuous Tweaking:** Prompts required constant adjustment to try and improve performance <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   **Excessive Conditionals:** Prompts became overly conditional (e.g., "if X, run tool A, respond with template B") <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   **Large Prompt Size:** Fitting all logic into a single prompt resulted in massive, difficult-to-manage instructions <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

## Key Challenges in Prompt Engineering

*   **Causality is Slippery:** It is exceptionally difficult to pinpoint why a prompt did or did not work, unlike traditional code where specific errors are highlighted <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. This requires extensive testing and "reps" to gain familiarity with how LLMs respond to communication <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Over-specifying Underperforms:** Providing too many explicit details or rules can lead to poorer outcomes, as LLMs are often better at making "plays" or decisions within defined boundaries <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
*   **Prompts as Hypotheses, Not Code:** Prompts are more like hypotheses that need to be run and measured at scale to assess performance, unlike code which can be meticulously reviewed before execution <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Negative Instructions are Difficult:** LLMs struggle more with negative instructions (e.g., "don't do this") compared to positive ones (e.g., "do this") <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>.
*   **Habit Change is Challenging:** Even highly effective AI agents might not be widely adopted if they require significant changes in user habits or break even once <a class="yt-timestamp" data-t="01:19:36">[01:19:36]</a>.

## Effective Strategies for Agentic Prompting

The new approach to prompt engineering for agentic systems focuses on designing decision-making frameworks rather than providing exhaustive step-by-step instructions <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

*   **Hardcode Deterministic Logic:** For predictable automations, hardcode logic using "if" nodes, switches, or filters, and only integrate the LLM where flexibility is truly needed <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Structure Input Data and Pull Context:** Focus on how input data is structured before it reaches the LLM and how necessary context (e.g., customer records, order history) is pulled and packaged <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   **Give the LLM "Thinking Space":** Instead of detailed steps, define the overarching objective, KPIs, and boundaries (guardrails) within which the LLM can operate and make decisions <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. This allows the LLM to "make plays" and uncover new solutions, much like AlphaGo did in Go <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.
*   **Use Emotion in Prompts:** Adding emotional cues (e.g., "all caps," "exclamation points," "do not do this") can heighten the LLM's attention and focus on critical instructions <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
*   **KPIs as Scoreboards:** Monitor Key Performance Indicators (KPIs) to evaluate agent performance, treating them like individual contributors whose performance can improve or degrade <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.
*   **Live KPI Monitoring and A/B Prompt Testing:** Implement systems for real-time KPI monitoring and automated triggering of A/B tests for different prompt versions to continuously optimize performance <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>.

## The Role of Model Selection

The choice of LLM model is crucial and can determine if a system is production-ready or merely a proof of concept <a class="yt-timestamp" data-t="00:22:14">[00:22:14]</a>.

*   **Model-Specific Prompting:** Different models (e.g., Anthropic, DeepMind, Gemini, Grok, OpenAI) have their own nuances in how they respond to prompts, requiring specific prompting techniques to get the most out of them <a class="yt-timestamp" data-t="00:23:49">[00:23:49]</a>.
*   **Context Window and Tool Calling:** Models vary in their context window size and compatibility with tool calling (e.g., Claude excels at calling MCP servers, while Gemini struggles but offers long context windows and live web search) <a class="yt-timestamp" data-t="00:24:15">[00:24:15]</a>.
*   **Architecting Agents:** A common and effective architecture involves a planner, executor, and verifier chain. Models can be selected for specific roles (e.g., Claude 3 Sonnet for high-level reasoning in the planner stage, GPT-4 for human-sounding external communication) <a class="yt-timestamp" data-t="00:25:38">[00:25:38]</a>.
*   **Optimal Model-Prompt Combo:** Bad outputs do not always indicate a bad prompt or a bad model; often, it's about finding the "Goldilocks zone" for the model-to-prompt combination <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>. A 20% difference in output quality can be observed by simply switching models with the same prompt <a class="yt-timestamp" data-t="00:28:04">[00:28:04]</a>.
*   **Fine-tuning for Specific Scenarios:** Fine-tuning models on specific industry jargon, language, cadence, standards, and norms (e.g., for legal firms) can significantly improve results and reduce the need for excessive guardrails in prompts <a class="yt-timestamp" data-t="00:31:55">[00:31:55]</a>.
*   **Standardize Prompting Techniques:** While models frequently update, establishing standardized prompting techniques based on the scenario and the chosen model is crucial <a class="yt-timestamp" data-t="00:32:34">[00:32:34]</a>.

> [!TIP] Stop overtuning prompts on the wrong model. First, identify the model that makes the most sense for the given scenario, then dial in that prompt for that specific model <a class="yt-timestamp" data-t="00:31:04">[00:31:04]</a>.

## The Importance of Custom Tooling and Data Management

Reliance on off-the-shelf tools can be limiting; building custom tools and ensuring robust [[data_management_and_prompt_engineering_for_ai_agents | data management]] are vital for effective prompt engineering <a class="yt-timestamp" data-t="00:32:56">[00:32:56]</a>.

*   **Custom Tool Development:** Custom tools for data processing, labeling, cleaning, API function calling, and data retrieval offer full control and more relevant solutions than generic SaaS platforms <a class="yt-timestamp" data-t="00:33:52">[00:33:52]</a>.
*   **Avoid Architecture Bending:** Off-the-shelf tools often force systems to bend their architecture to the tool's limits, leading to cohesive issues when integrating multiple solutions <a class="yt-timestamp" data-t="00:37:18">[00:37:18]</a>.
*   **Master Contextual Database (Agentic Database):** A central, real-time, continually updated database for an organization's knowledge and event data is crucial for feeding accurate and relevant context to agents <a class="yt-timestamp" data-t="00:55:03">[00:55:03]</a>. This becomes the "single source of truth" <a class="yt-timestamp" data-t="00:57:46">[00:57:46]</a>.
*   **Event Data Processing:** Developing workflows to process real-time event data (emails, Slack messages, meeting transcripts) allows for understanding operational patterns and identifying AI opportunities <a class="yt-timestamp" data-t="00:42:22">[00:42:22]</a>.

## Impact of UI/UX on Agent Adoption

For widespread adoption of [[building_efficient_ai_agents_with_prompts | agentic systems]], an intuitive and differentiated User Interface (UI) and User Experience (UX) are paramount <a class="yt-timestamp" data-t="01:15:27">[01:15:27]</a>.

*   **Dedicated Workspace and KPIs:** Agents should have their own workspace within a UI that tracks activity and showcases performance against real KPIs, fostering a sense of human-agent collaboration <a class="yt-timestamp" data-t="01:16:33">[01:16:33]</a>.
*   **Collaborative Approach:** The interaction between humans and agents needs to shift from a "master and tool" dynamic to a truly collaborative one, where agents own entire processes and outcomes <a class="yt-timestamp" data-t="01:19:07">[01:19:07]</a>.
*   **Frictionless Interaction:** Similar to how ChatGPT made LLMs accessible, a "UI/UX chip moment" is needed for agentic systems to make them frictionless and easy for everyday use, overcoming the challenge of habit change <a class="yt-timestamp" data-t="01:20:18">[01:20:18]</a>.

## Shifting Mindsets: From Automation to Agentic Systems

Businesses must recognize that [[introduction_to_prompt_engineering | AI automation]] is an improvement of traditional automation, while [[building_efficient_ai_agents_with_prompts | Agentic AI]] represents a fundamental paradigm shift <a class="yt-timestamp" data-t="00:47:01">[00:47:01]</a>.

*   **Focus on Agentic Systems:** Instead of building simple automations, focus on developing agentic operating systems (Agentic OS) that act as the underlying framework for business operations, capable of orchestrating and even building automations themselves <a class="yt-timestamp" data-t="00:47:42">[00:47:42]</a>.
*   **Performance-Based Systems:** LLMs enable basing software performance on business KPIs (e.g., conversion rates, refund rates) rather than just system health <a class="yt-timestamp" data-t="00:47:51">[00:47:51]</a>.
*   **Redefining Business Margins:** [[ai_in_legal_firms_and_cost_efficiency | Agentic systems]] can significantly reduce operational expenses and improve performance, leading to a "flywheel effect" of increased margins and reinvestment into growth <a class="yt-timestamp" data-t="01:30:40">[01:30:40]</a>. This redefines industry standards and margins <a class="yt-timestamp" data-t="01:37:49">[01:37:49]</a>.
*   **Knowledge Base and Business Logic:** A primary focus should be on defining and digitizing the organization's knowledge base and business logic, which is often "trapped in people's heads," to make it accessible to agents <a class="yt-timestamp" data-t="00:58:15">[00:58:15]</a>. This helps overcome [[challenges_of_implementing_ai_agents | challenges of implementing AI agents]] at scale.
*   **New Approach to Consulting:** AI consulting should focus on guiding clients through the implementation of holistic agentic operating systems, not just simple automation solutions <a class="yt-timestamp" data-t="01:40:03">[01:40:03]</a>. This includes deep discovery processes to understand existing tech stacks, data flows, and where the agentic layer and dynamic tools can be most effectively applied <a class="yt-timestamp" data-t="01:03:08">[01:03:08]</a>.

> [!WARNING] Many businesses missed the wave of traditional automation. However, instead of catching up, they should skip directly to Agentic AI, as traditional automation is now considered "yesterday's news" given the capabilities of LLMs <a class="yt-timestamp" data-t="00:47:19">[00:47:19]</a>. This also highlights [[challenges_in_automating_enterprise_processes | challenges in automating enterprise processes]].

> [!NOTE] [[the_role_of_language_in_ai_prompt_engineering | Agentic AI]] is not simply an improvement of traditional automation; it is a whole new paradigm that redefines efficiency and operational capabilities <a class="yt-timestamp" data-t="00:51:59">[00:51:59]</a>.