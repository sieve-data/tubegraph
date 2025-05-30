---
title: Impact of AI on customer support
videoId: fi4-kSuaw40
---

From: [[redpointai]] <br/> 

Intercom, a company providing customer support platforms, rapidly integrated AI into its products following the public launch of ChatGPT <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This swift adoption was driven by the understanding that customer support is highly susceptible to the influence of AI and large language models (LLMs) <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. LLMs are conversational, can look up facts, read, understand, and summarize information, performing a significant portion of a customer service representative's job out of the box <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

## Intercom's Rapid AI Integration

The release of ChatGPT on a Tuesday evening in Dublin prompted an immediate internal reaction at Intercom <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Within hours, the AI and ML team was playing with the new technology <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. By the following Sunday, conversations with the CEO led to the decision to "rip up the entire AI ML road map" and go all-in on this new technology <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

Intercom shipped an initial AI product before Christmas, had a reasonable release in January, and broadly launched their AI product, Finn, in March and July <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. This rapid development positioned Intercom as a leader in AI adoption within the customer support industry <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### Initial AI Features: Inbox AI

The first step was to integrate "zero downside" AI features into their inbox product <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. These included:
*   Summarizing conversations <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>
*   Translating messages for multilingual support <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>
*   Expanding or collapsing text <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>

These features addressed actual needs in customer support, such as summarizing issues for ticket creation <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. This "crawl, walk, run" approach provided immediate value with minimal risk <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>, as users could simply not use the feature if it wasn't helpful <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

### Introduction of Finn

The next major release was Finn, a user-facing chatbot, enabled by access to the GPT-4 beta <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. GPT-4 significantly improved the ability to "contain the bot" and reduce hallucinations compared to GPT-3.5 <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. Finn could answer questions based on a high confidence threshold <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

Key aspects addressed for Finn's adoption included ensuring it was:
*   Trustworthy <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>
*   Reliable <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>
*   On-topic (e.g., not giving political opinions or recommending competitors) <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>

Later, Inbox AI was expanded to include features like matching a standard tone of voice <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. There are plans for significant new capabilities for Finn within the inbox <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. Finn has already handled over two million answers and is used by thousands of people, with high-quality responses to complex queries <a class="yt-timestamp" data-t="00:28:50">[00:28:50]</a>.

### Managing Costs and Latency

Intercom processes approximately 500 million conversations per month <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. Automatically summarizing all of them would be prohibitively expensive, leading to the decision to initially offer summarization as an optional button in the UI <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

The company remains in a "deep exploration mode" rather than primarily in cost optimization <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. While there are opportunities to use less expensive models (e.g., moving from GPT-4 to GPT-3.5 or open-source models like Llama), the focus is on expanding AI capabilities across the product <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>. This includes using AI for reporting, augmenting human agents, and powering messages sent by Intercom <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.

Latency is a significant concern; current AI tools can feel slow, akin to "modem internet days" <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>. The expectation is that AI will become instant, especially with the potential for LLMs to run on devices like phones <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

## Building and Scaling AI Products

### Guardrails and Hallucination Prevention

A core component of building reliable AI for customer support is a robust "torture test" that covers all potential scenarios of misbehavior and desired behaviors <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. This testing helps to understand the trade-offs between constraining the model (reducing creativity and errors) and potentially missing correct answers <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.

Key strategies include:
*   **Contextual Understanding**: Ensuring the AI prioritizes specific contextual information over its general knowledge to avoid irrelevant or inappropriate responses (e.g., providing local legal information for sunbeds vs. general legality) <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
*   **Conflict Resolution**: Defining how the AI should resolve conflicts when consuming multiple documents <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   **Model Evaluation**: Continuously testing various models (GPT-3.5, GPT-4, Anthropic's Claude, Llama) against the same scenarios to assess trust, cost, reliability, stability, uptime, malleability, and speed <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

The possibility of offering customers a choice of AI models in the future based on their preferences is also being considered <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

### Organizational Structure

Intercom utilizes a centralized AI/ML team, comprising 17-20 people (initially 9-ish) with deep expertise in building, running, training, and using models <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>. This central team enables about 150 "regular product engineers" who then build customer-facing features on top of the AI team's enabled endpoints <a class="yt-timestamp" data-t="00:20:18">[00:20:18]</a>.

This centralized model is deemed necessary for "AI-first" companies whose existence depends on cutting-edge AI or those building new product categories <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>. For companies merely "applying AI" as a minor enhancement, product engineers with some AI familiarity might suffice <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>.

### Challenges in AI Product Development

Developing AI-powered products differs significantly from traditional software development <a class="yt-timestamp" data-t="00:22:32">[00:22:32]</a>. In traditional software, uncertainty is primarily in the design stage; with AI, a second wave of uncertainty arises around feasibility ("is any of this even possible?") <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>. This uncertainty can linger, making it hard to definitively know if a project will succeed <a class="yt-timestamp" data-t="00:23:10">[00:23:10]</a>.

This necessitates a "portfolio of bets" approach to AI projects, with some having high probabilities of success (e.g., text expansion or rephrasing) and others being lower-probability, higher-reward endeavors (e.g., generating vector-based graphics from text) <a class="yt-timestamp" data-t="00:23:39">[00:23:39]</a>.

An example of a challenging problem is sentence completion for support agents, where distinguishing personal answers from public information and handling Personally Identifiable Information (PII) proves difficult <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>.

### Missing Tools in the AI Ecosystem

There is a perceived need for better tooling in the AI space <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.
*   **Prompt Management**: Tools for subtle changes to prompts, rerunning tests, versioning prompts across different models, and A/B testing are needed <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.
*   **Robust Infrastructure**: More robust solutions for deploying AI, especially concerning regional data residency (e.g., in the EU), authentication, monitoring, and data logging <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.

While some tools like Pinecone exist for vector search, established companies like Intercom may have already built their own capabilities <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>. The concern also exists that major AI providers like OpenAI, acting as the "AWS of AI," might eventually build their own tooling, "sherlocking" smaller startups <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.

## Customer Adoption and the Future of AI in Support

Customers typically start with AI adoption in "pilot mode," using it for low-risk scenarios like weekend support or simple tasks such as password resets <a class="yt-timestamp" data-t="00:26:33">[00:26:33]</a>. Intercom actively facilitates this "dip your toe" approach by enabling AI for specific user segments (e.g., free users, or users who have been with the product for over a year) <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>.

Over time, customers often realize that AI-powered support (e.g., instant answers) provides better service, leading them to go "all in" on AI <a class="yt-timestamp" data-t="00:28:08">[00:28:08]</a>.

### Broad Rollouts and Normalization of AI
A significant catalyst for broad AI adoption will be when major consumer technology companies like Apple and Google fully integrate LLMs into their products (e.g., Siri, Google Bard) <a class="yt-timestamp" data-t="00:29:28">[00:29:28]</a>. This will normalize the idea of conversational interaction with software, similar to how the iPhone normalized good software design in B2B applications <a class="yt-timestamp" data-t="00:30:10">[00:30:10]</a>. The quality of [[the_future_of_ai_in_human_communication | AI-enriched software]] is expected to become a competitive battlefield in the next few years <a class="yt-timestamp" data-t="00:30:47">[00:30:47]</a>.

### AI Model Training and Voice
Currently, Intercom uses Retrieval-Augmented Generation (RAG) for Finn, not fine-tuning per customer <a class="yt-timestamp" data-t="00:31:30">[00:31:30]</a>. Tone of voice is handled through prompting <a class="yt-timestamp" data-t="00:31:37">[00:31:37]</a>. Finn can naturally pick up the tone of voice by analyzing existing documentation and customer support conversations <a class="yt-timestamp" data-t="00:32:50">[00:32:50]</a>.

Intercom also has an AI lab where 30-40% of the AI team explores advanced possibilities, such as building their own models or training models on proprietary customer support data <a class="yt-timestamp" data-t="00:32:11">[00:32:11]</a>.

### Future Automation Levels
The percentage of requests handled by AI will vary significantly by industry and product complexity <a class="yt-timestamp" data-t="00:33:17">[00:33:17]</a>:
*   **High Automation**: E-commerce stores with a limited number of common queries (e.g., "where is the thing," "in stock," returns) could see 100% AI automation <a class="yt-timestamp" data-t="00:33:31">[00:33:31]</a>. Simple note-taking apps with few features could also achieve 100% automation <a class="yt-timestamp" data-t="00:34:38">[00:34:38]</a>.
*   **Partial Automation**: More complex products like Google Docs with thousands of diverse questions might reach 80-90% automation <a class="yt-timestamp" data-t="00:34:02">[00:34:02]</a>.
*   **[[Advancements and implications of AI agents | AI agents]] and Actions**: A growing area is AI taking actions, not just providing text answers <a class="yt-timestamp" data-t="00:35:06">[00:35:06]</a>. This includes tasks like logging into Stripe to issue a refund or cancelling an order <a class="yt-timestamp" data-t="00:35:09">[00:35:09]</a>. This requires significant software development for authentication, monitoring, and data logging <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>. Some customers may prefer full automation, while others may want human oversight for sensitive actions, acting as "line managers" for the AI <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>.

## Impact of AI on Business Models and Product Development

AI is expected to transform product landscapes, in some cases rendering entire existing product stacks obsolete <a class="yt-timestamp" data-t="00:38:58">[00:38:58]</a>. An example is advertising optimization platforms, where AI could automate ad generation, performance measurement, and winner selection without human login <a class="yt-timestamp" data-t="00:39:34">[00:39:34]</a>.

However, for businesses like email marketing platforms (e.g., Mailchimp, Klaviyo), while AI can simplify email design and writing, the core challenge remains sending hundreds of millions of emails, which involves complex technical and reputational hurdles (e.g., deliverability, spam compliance) <a class="yt-timestamp" data-t="00:40:33">[00:40:33]</a>. In such cases, incumbents with established infrastructure have a significant advantage <a class="yt-timestamp" data-t="00:41:23">[00:41:23]</a>.

### Advice for Startups and Incumbents

For **startups**:
*   Focus on areas where the existing "incumbent tech stack is pretty much irrelevant" <a class="yt-timestamp" data-t="00:41:36">[00:41:36]</a>. These are areas where if the product were built today, it would be entirely different, with no UI or features surviving from the old model <a class="yt-timestamp" data-t="00:41:46">[00:41:46]</a>.

For **incumbents (larger companies)**:
1.  **Find asymmetric upside**: Identify simple AI applications that can be implemented quickly to understand costs and latency <a class="yt-timestamp" data-t="00:42:19">[00:42:19]</a>.
2.  **Workflow analysis**: Break down the entire product into workflows (e.g., creating a project, assigning tasks) <a class="yt-timestamp" data-t="00:42:39">[00:42:39]</a>.
3.  **Automate/Delete**: If AI can reliably and accurately perform a workflow, make AI do it and delete the old manual processes <a class="yt-timestamp" data-t="00:42:55">[00:42:55]</a>.
4.  **Augment/Simplify**: If AI cannot remove a workflow, use it to augment or reduce it to a simpler decision set, significantly increasing efficiency <a class="yt-timestamp" data-t="00:43:32">[00:43:32]</a>.
5.  **Sprinkle AI**: Add minor AI enhancements for completeness, even if not critically impactful <a class="yt-timestamp" data-t="00:43:51">[00:43:51]</a>.
6.  **Educate Customers**: Actively sell the value of AI integration to customers to help them understand the benefits <a class="yt-timestamp" data-t="00:44:12">[00:44:12]</a>.

## Overhyped vs. Underhyped AI

<p class="callout-block success">
<p class="callout-block-title">Overhyped</p>
<p>Productivity tools that write emails, sales pitches, or other content <a class="yt-timestamp" data-t="00:44:35">[00:44:35]</a>. It's predicted that people will learn to detect AI-generated content, and filters will emerge to identify it <a class="yt-timestamp" data-t="00:44:42">[00:44:42]</a>.</p>
</p>

<p class="callout-block success">
<p class="callout-block-title">Underhyped</p>
<p>Changes coming to [[impact_of_ai_on_the_music_industry | creativity]] through AI <a class="yt-timestamp" data-t="00:44:59">[00:44:59]</a>. Tools like Kaiber (for video), Refusion (for sound), and Synthesia (for video) are enabling new forms of creativity, similar to how Instagram filters enabled everyone to feel like photographers <a class="yt-timestamp" data-t="00:45:21">[00:45:21]</a>.</p>
</p>

## Incumbents and AI Adoption

<p class="callout-block info">
<p class="callout-block-title">Most Impressed By</p>
<p>
*   **Adobe**: Praised for quickly releasing interesting AI features <a class="yt-timestamp" data-t="00:46:11">[00:46:11]</a>.
*   **Figma & Miro**: Noted for finding valuable, sensible AI use cases rather than just applying AI for marketing <a class="yt-timestamp" data-t="00:46:20">[00:46:20]</a>.
*   **Shopify & Costco**: Mentioned as having done some nice work <a class="yt-timestamp" data-t="00:46:41">[00:46:41]</a>.
</p>
</p>

<p class="callout-block danger">
<p class="callout-block-title">Most Disappointed By</p>
<p>
*   **Apple**: Criticized for the slow pace of AI adoption, especially considering the primitive nature of Siri compared to advanced LLMs like ChatGPT <a class="yt-timestamp" data-t="00:46:50">[00:46:50]</a>.
*   **Amazon**: Similar to Apple, their voice assistants like Alexa are seen as lagging behind <a class="yt-timestamp" data-t="00:47:20">[00:47:20]</a>.
</p>
</p>

The expectation is for a "leveling out" in AI capabilities across different platforms in 2024, leading to a broader societal acceptance of AI <a class="yt-timestamp" data-t="00:47:43">[00:47:43]</a>.

## Key Takeaways from Intercom's Experience

*   **Speed of Adoption**: Intercom's rapid "all-in" approach immediately after ChatGPT's launch provided a first-mover advantage in the customer support space <a class="yt-timestamp" data-t="00:49:53">[00:49:53]</a>.
*   **Low-Risk Entry**: Starting with "zero downside" AI features allowed customers to incrementally adopt AI without disrupting their existing experience <a class="yt-timestamp" data-t="00:49:27">[00:49:27]</a>.
*   **Strategic Investment**: Companies like Intercom and Meta (with its massive compute investment for Llama 3) are demonstrating that going "all-in" and embracing AI's core capabilities is crucial <a class="yt-timestamp" data-t="00:55:16">[00:55:16]</a>.
*   **Exploration Over Optimization**: Many companies are still focused on exploring the full capabilities of new AI models rather than optimizing for cost, indicating a broad frontier of untapped potential <a class="yt-timestamp" data-t="00:53:22">[00:53:22]</a>.
*   **Iterative Rollout**: A thoughtful, iterative deployment to subsets of users (e.g., less critical segments or those unlikely to churn) allows companies to control risk, manage costs, and experiment with AI functionality <a class="yt-timestamp" data-t="00:54:19">[00:54:19]</a>.