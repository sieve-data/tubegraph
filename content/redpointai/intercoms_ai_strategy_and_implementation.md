---
title: Intercoms AI Strategy and Implementation
videoId: fi4-kSuaw40
---

From: [[redpointai]] <br/> 

Intercom, a customer messaging platform, rapidly integrated AI capabilities into its product suite following the public release of ChatGPT in late 2022 <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. The company, co-founded by Des Traynor, saw customer support as being "in the kill zone of AI" due to large language models' inherent conversational abilities and their capacity to look up, understand, and summarize facts <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. This realization led to an "all hands on deck" moment, shifting Intercom's entire AI/ML roadmap to go "all in" on the new technology <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## Rapid AI Adoption at Intercom

Intercom's AI team, based in Dublin, Ireland, quickly recognized the potential of large language models after ChatGPT's launch <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Des Traynor recalls playing with ChatGPT on his phone, initially testing its ability to answer factual questions, then being genuinely impressed when it could perform more creative tasks, like writing a song in the style of Rage Against the Machine about installing a Windows driver <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

The company moved swiftly:
*   **Before Christmas 2022:** Shipped an initial AI product <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **January 2023:** Had a "reasonable release" <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   **March 2023:** Launched Finn, their user-facing chatbot, initially <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   **July 2023:** Broadly launched Finn <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

This rapid pace was driven by the understanding that if Intercom didn't lead in AI adoption for customer support, another company would <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

## Intercom's AI Product Suite

Intercom's initial strategy for adopting AI was to build "zero downside" features, where users could opt-in, and if they didn't like the AI's output, they could simply not use it <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

### Inbox AI Features
The first AI-powered features were integrated into the Intercom inbox, primarily using GPT-3.5 Turbo <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. These included:
*   Summarizing conversations <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
*   Translating messages for multilingual support <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   Expanding or collapsing text <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   Summarizing issues to create tickets <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

These features provided immediate value, leading customers to ask for automatic summarization <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. However, automatically summarizing 500 million conversations per month was cost-prohibitive with initial model pricing <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

### Finn Chatbot
The next major release was Finn, a user-facing chatbot, launched after Intercom gained access to the GPT-4 beta <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. GPT-4 significantly reduced hallucinations, allowing for a more contained and trustworthy bot <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. Key developments for Finn included ensuring it was:
*   Trustworthy and reliable <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   Capable of staying on topic (e.g., not giving political opinions or recommending competitors) <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   Able to match a standard or customer's specific tone of voice <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

Finn has already provided over two million answers and is used by thousands of people, with answers being high-quality and capable of handling complex, multi-part questions <a class="yt-timestamp" data-t="00:28:50">[00:28:50]</a>.

## Key Challenges and Solutions

Intercom faced several [[enterprise_ai_adoption_challenges_and_solutions | challenges]] in its AI implementation journey.

### Managing Hallucinations and Guardrails
A core ingredient to managing hallucinations and ensuring appropriate behavior is a robust "torture test" <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. This involves:
*   A long set of scenarios, questions, and contexts to observe the AI's behavior <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   Internal weighting to determine acceptable trade-offs between answer quality and occasional misbehavior (e.g., political opinions) <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   Prioritizing given context over the LLM's general knowledge (e.g., local laws for sunbeds) <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
*   Using sophisticated prompting techniques to resolve conflicts between different data sources <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

Intercom continuously evaluates models like GPT-3.5, GPT-4, Anthropic's Claude, and open-source models like Llama against these scenarios, considering factors like trust, cost, reliability, stability, uptime, malleability (control), and speed <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

### Cost Optimization vs. Exploration
Initially, the cost of automatically summarizing 500 million conversations monthly would have been prohibitive, leading to the decision to make it a user-triggered feature <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. However, Intercom remains in "deep exploration mode" for AI applications rather than prioritizing cost optimization <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
*   The primary focus is on building the best possible customer support platform enriched with AI <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.
*   The belief is that technology generally gets cheaper and faster, so even if left untouched, models will improve <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>.
*   Cost optimization will become more critical when models plateau in their capabilities, indicating a shift from acceleration to a more mature phase of the S-curve <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.

### Latency Concerns
[[Latency and System Integration Challenges in AIbased Voice Systems | Speed]] is a significant factor in AI system performance <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. Current AI interactions can feel slow, akin to "modem internet days" <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>. The expectation is that advancements, potentially like Apple integrating an LLM directly into phones or Google's Gemini builds, will lead to "instant AI" <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>. For Intercom, latency is currently a more pressing forcing function than cost for exploring smaller or more localized models <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.

### Regional Compliance (EU)
Operating AI solutions globally presents [[challenges_and_strategies_in_expanding_ai_applications_globally | challenges]], particularly with regional compliance like the EU. Getting Finn to work in the EU was complex due to server locations and data regulations, leading to unexpected partnerships, such as with Microsoft Azure <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.

## Organizational Approach to AI

### Centralized AI/ML Team
Intercom employs a centralized AI/ML team, comprising 17-20 people (initially around 9) with deep domain expertise in building, running, training, and using models <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>. This team enables product engineers (around 150) to build customer-facing features by providing API endpoints for tasks like answering questions or suggesting next steps in a conversation <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.

> "There's about like our our team today in total is about 17 maybe 20 people uh um in that and but when we started on this journey it was probably like nine or something like that to be clear uh I think um you know there's a few threads I'd pull on like it's not you know people often forget this but small teams can do an awful lot" <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>

This centralized model is critical for companies that are "AI first" or "AI as in they're literally working on the bleeding edge of AI" <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>, requiring data scientists and experienced AI engineers <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>. Companies merely "sprinkling" AI onto their products might get by with product engineers dabbling in Open AI specs <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>.

### AI Project Management: Portfolio of Bets
Developing AI-powered software differs from traditional software development due to a second wave of uncertainty: whether the AI functionality is even possible <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>. Unlike traditional projects where risks are often mitigated at the design stage, AI projects can lead to prolonged efforts without a clear "no" on feasibility <a class="yt-timestamp" data-t="00:23:10">[00:23:10]</a>.

> "The worst part about the is any of this [__] even possible is that you don't even know if you'll ever know the answer to that question like you know all you know is it's it hasn't started working yet and you'll never actually have a clean no it's firmly not possible" <a class="yt-timestamp" data-t="00:23:08">[00:23:08]</a>

Therefore, AI development should be viewed as a "portfolio of bets" <a class="yt-timestamp" data-t="00:23:39">[00:23:39]</a>:
*   **High Probability Bets:** Features like expanding or rephrasing text have a 99% probability of success <a class="yt-timestamp" data-t="00:23:42">[00:23:42]</a>.
*   **Low Probability Bets:** More ambitious features, such as generating editable vector graphics, might only have a 20-40% probability <a class="yt-timestamp" data-t="00:24:08">[00:24:08]</a>. The challenge is that one may never definitively know if they are impossible <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>.

An example of a tricky problem is AI-powered sentence completion in customer support, which faces challenges in distinguishing personal answers, handling PII, and abstracting irrelevance from context <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>.

## Strategic Insights and Future Outlook

### AI Adoption Curve in Customer Support
Customers are moving from "AI curious to all in on AI" <a class="yt-timestamp" data-t="00:26:57">[00:26:57]</a>. Intercom facilitates this transition by offering low-risk ways to adopt AI, such as:
*   Piloting AI for free users <a class="yt-timestamp" data-t="00:27:22">[00:27:22]</a>.
*   Limiting AI usage to weekends or specific query types <a class="yt-timestamp" data-t="00:27:43">[00:27:43]</a>.

This "dip your toe" approach helps customers realize the value, often leading to them wanting to expand AI use after seeing superior support for pilot groups <a class="yt-timestamp" data-t="00:27:52">[00:27:52]</a>. A key enabler for widespread adoption will be major tech companies like Apple and Google fully integrating LLMs into their consumer products (e.g., Siri, Bard), which will normalize "talking to software" <a class="yt-timestamp" data-t="00:29:26">[00:29:26]</a>.

### Evolution of AI in Workflows
The percentage of requests handled by AI will vary significantly by vertical <a class="yt-timestamp" data-t="00:33:17">[00:33:17]</a>:
*   **High Automation (e.g., e-commerce):** Simple, repetitive queries (e.g., "where is my order?") mean nearly 100% automation is possible <a class="yt-timestamp" data-t="00:33:31">[00:33:31]</a>.
*   **Mixed Automation (e.g., complex software):** Products like Google Docs generate diverse questions, making 100% automation unlikely, but 80-90% is achievable <a class="yt-timestamp" data-t="00:34:02">[00:34:02]</a>.

[[AI agent capabilities and limitations | AI agent capabilities and limitations]] are expanding beyond just text-based answers to include performing actions (e.g., issuing refunds on Stripe, canceling orders) <a class="yt-timestamp" data-t="00:35:06">[00:35:06]</a>. This involves writing significant code for authentication, monitoring, and data logging <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>. The future might see AI suggesting complex actions for human approval, turning support reps into "line managers" who oversee AI operations <a class="yt-timestamp" data-t="00:36:23">[00:36:23]</a>.

### Overhyped and Underhyped AI Trends
*   **Overhyped:** Productivity tools focused on generating content like emails or sales pitches <a class="yt-timestamp" data-t="00:44:33">[00:44:33]</a>. Traynor believes people will learn to detect AI-generated content, and filters will emerge, leading to a renewed appreciation for human writing <a class="yt-timestamp" data-t="00:44:42">[00:44:42]</a>.
*   **Underhyped:** The transformative impact of AI on creativity <a class="yt-timestamp" data-t="00:44:56">[00:44:56]</a>. Similar to how Instagram filters made everyone feel like photographers, tools like Midjourney, Refusion (for sound), and Synthesia (for video) are enabling new forms of creativity that are yet to be fully understood <a class="yt-timestamp" data-t="00:45:20">[00:45:20]</a>.

### Industry Impressions
*   **Most Impressed By:** Adobe (for quick AI integration), Figma, and Miro (for finding useful, sensible AI use cases) <a class="yt-timestamp" data-t="00:46:08">[00:46:08]</a>. Shopify and Cot also received positive mentions <a class="yt-timestamp" data-t="00:46:41">[00:46:41]</a>.
*   **Most Disappointed By:** Apple and Amazon <a class="yt-timestamp" data-t="00:46:48">[00:46:48]</a>. Current voice assistants like Siri and Alexa seem primitive compared to advanced LLMs like ChatGPT, which can generate complex, long-form stories <a class="yt-timestamp" data-t="00:47:01">[00:47:01]</a>. The hope is for a "leveling out" in 2024 with more widespread consumer adoption of advanced AI <a class="yt-timestamp" data-t="00:47:41">[00:47:41]</a>.

For startups, the advice is to target areas where incumbent "tech stack is pretty much irrelevant" <a class="yt-timestamp" data-t="00:41:39">[00:41:39]</a>, meaning if they started over, they would build it entirely differently with AI at the core, rendering existing UI and features obsolete <a class="yt-timestamp" data-t="00:41:48">[00:41:48]</a>. For incumbents, the recommended algorithm is:
1.  **Remove what AI can remove:** Delete features or workflows that AI can automate entirely <a class="yt-timestamp" data-t="00:43:04">[00:43:04]</a>.
2.  **Optimize what remains:** If AI can't remove it, let it augment or simplify the workflow into a clear decision set <a class="yt-timestamp" data-t="00:43:32">[00:43:32]</a>.
3.  **Sprinkle AI where possible:** Add AI touches for completeness, even if not core to efficiency <a class="yt-timestamp" data-t="00:43:51">[00:43:51]</a>.
4.  **Learn to sell the value:** Effectively communicate the benefits of AI to customers <a class="yt-timestamp" data-t="00:44:12">[00:44:12]</a>.

This outlines [[strategic_uses_of_ai_in_enterprises | strategic uses of AI in enterprises]] and [[challenges_and_strategies_in_enterprise_ai_deployment | challenges and strategies in enterprise AI deployment]].

---
*For more information, visit intercom.com or intercom.com/blog. Des Traynor can be found as @destraynor on social media.* <a class="yt-timestamp" data-t="00:48:02">[00:48:02]</a>