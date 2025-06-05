---
title: Customer success with AI solutions
videoId: VhPfM_aGBVc
---

From: [[aidotengineer]] <br/> 

Anthropic is an AI safety and research company focused on building highly capable and safe large language models (LLMs) <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Their mission involves not only releasing advanced models like Sonnet 3.5 <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>, but also leading in safety techniques, research, and policy <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. Sonnet is particularly noted for its leadership in the code space, topping leaderboards for agentic coding evaluations like Sbench <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## Anthropic's Approach to Customer Success

Anthropic's applied AI team works closely with customers on technical implementation and brings insights back to product and model research <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. They support the technical aspects of use cases, helping to design architectures, evaluations, and tweak prompts to get the best out of their models <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. This approach is based on hundreds of customer interactions, aiming to provide actionable insights for [[implementing_ai_in_enterprises | implementing AI]] and best practices <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Solving Core Business Problems with AI

Anthropic encourages customers to use AI to solve the fundamental problems their products address, moving beyond basic applications like chatbots and summarization <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. While these can be helpful, the focus should be on placing bigger bets <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

For example, an onboarding and upskilling platform aims to help users ramp up quickly and advance their careers <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. Instead of just summarizing course content or offering a Q&A chatbot, AI could be used to:
*   Hyper-personalize course content based on each individual employee's context <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
*   Dynamically adapt course content to make it more challenging for fast learners <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   Dynamically update course material based on learning styles (e.g., creating visual content for visual learners) <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

AI is making an impact across various industries, including taxes, legal, and project management, by drastically enhancing the [[building_user_experiences_with_ai | customer experience]] <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. This means making products easier to use and more trustworthy, leading to high-quality outputs where hallucination is unacceptable, such as in tax preparation <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

### Case Study: Intercom's Finn AI Agent

Intercom, an AI customer service platform, developed an AI agent called Finn <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>. Anthropic collaborated with Intercom's data science team on a two-week sprint, comparing Intercom's most difficult prompt for Finn against a prompt refined with Claude <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.

This initial success led to a two-month optimization sprint, fine-tuning all of Intercom's prompts for Claude's best performance <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. The results showed Anthropic's LLM outperforming Intercom's existing model <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. Intercom's resolution-based pricing model further incentivized the model to be helpful in solving customer problems <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.

Upon launching Finn 2, Intercom achieved impressive metrics:
*   Can solve up to 86% of customer support volume, with 51% resolution out of the box <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.
*   Improved human-like interaction, allowing adjustment of tone and answer length <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
*   Enhanced policy awareness, such as for refund policies, unlocking new capabilities <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

## Best Practices for AI Implementation and Success

When [[implementing_ai_in_enterprises | implementing AI]], several best practices and common pitfalls should be considered:

### 1. Testing and Evaluation

A common mistake is building a robust workflow and then only later considering evaluations <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. Evaluations should direct the path towards a perfect outcome and ideally be built from the outset or very shortly after <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.

It's crucial to design representative test cases, including "silly examples" that a user might ask but are unrelated to the product, to ensure the model responds appropriately or reroutes the question <a class="yt-timestamp" data-t="00:15:59">[00:15:59]</a>. Customers should invest in telemetry to back-test their architecture and understand the "latent space" of their use cases <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>. Evaluations are considered intellectual property, key to competitive advantage in navigating and optimizing AI solutions <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.

### 2. Identifying Metrics and Trade-offs

Organizations often face an "intelligence-cost-latency triangle" when optimizing AI solutions <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. While it's difficult to meet all three, the balance should be defined in advance for the specific use case <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.

For example:
*   **Customer Support**: Latency is critical; a response needed within 10 seconds to prevent customer abandonment <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>. [[building_user_experiences_with_ai | User experience]] strategies, like "thinking boxes" or redirecting customers to other pages, can manage perceived latency <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.
*   **Financial Research**: High intelligence and accuracy are paramount, even if it means a longer response time (e.g., 10 minutes) because the stakes (capital allocation) are very high <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>.

The stakes and time sensitivity of the decision should drive optimization choices <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.

### 3. Fine-tuning Considerations

Fine-tuning is not a "silver bullet" <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>. It's akin to "brain surgery on the model," which can limit its reasoning in areas outside of what it's fine-tuned for <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>. It's recommended to try other approaches first, ensuring clear success criteria are established beforehand <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>. The cost and effort of fine-tuning must be justified by a clear difference in performance for the specific intelligence domain <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.

> "Don't let fine tuning slow you down... no no pursue it and then realize that you need to do fine tuning and then you can just sub in the fine tuned model and then explore other methods first." <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>

### 4. Other Optimization Methods

Beyond basic prompt engineering, several other features and architectures can drastically change the success of a use case <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>:
*   **Prompt Caching**: Can lead to significant cost reductions (e.g., 90%) and speed increases (e.g., 50%) without sacrificing model intelligence <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.
*   **Contextual Retrieval**: Improves the performance of retrieval mechanisms, feeding information more effectively to the model and reducing processing time <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>.
*   **Citations**: An out-of-the-box feature that enhances reliability <a class="yt-timestamp" data-t="00:20:09">[00:20:09]</a>.
*   **Agentic Architectures**: Architectural decisions that can significantly impact performance <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>.

## Getting Started with Anthropic's AI

Anthropic offers several avenues for businesses to access their models:
*   **API**: For businesses looking to embed AI into their products and services <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Claude for Work**: Empowers entire organizations to leverage AI in their day-to-day operations <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   **Cloud Partnerships**: Access to Frontier models via AWS Bedrock or Google Cloud's Vertex AI, allowing deployment in existing environments without managing new infrastructure, thereby reducing barriers to entry <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. Support is consistent regardless of the access method <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.