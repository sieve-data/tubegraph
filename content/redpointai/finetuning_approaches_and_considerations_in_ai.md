---
title: Finetuning approaches and considerations in AI
videoId: YCKVxXrcZ-0
---

From: [[redpointai]] <br/> 

The development of AI models for enterprise applications involves strategic decisions regarding how models are adapted and utilized. Chris Roman, co-founder and CEO of Fireflies.ai, shared insights on their approach to leveraging large language models (LLMs), particularly their perspective on [[the_role_of_reinforcement_and_finetuning_in_ai | finetuning]].

## The Debate: To Finetune or Not to Finetune?

Fireflies.ai generally avoids finetuning models on customer data, prioritizing privacy by not training on it by default <a class="yt-timestamp" data-t="00:27:27">[00:27:27]</a> <a class="yt-timestamp" data-t="00:30:22">[00:30:22]</a>. Chris Roman expressed a lack of belief in finetuning, citing several reasons:
*   **Cost and Diminishing Returns** Finetuning is expensive, and its returns diminish over time as the base models themselves improve significantly <a class="yt-timestamp" data-t="00:44:12">[00:44:12]</a> <a class="yt-timestamp" data-t="00:46:04">[00:46:04]</a>. The rapid evolution of models, such as the jump from GPT-3 to GPT-4, makes earlier finetuning efforts less relevant <a class="yt-timestamp" data-t="00:44:20">[00:44:20]</a> <a class="yt-timestamp" data-t="00:45:06">[00:45:06]</a>. A non-finetuned GPT-5 might outperform a finetuned GPT-4 <a class="yt-timestamp" data-t="01:04:09">[01:04:09]</a>.
*   **Market Volatility** The AI market changes weekly, requiring constant adaptation of assumptions and strategies <a class="yt-timestamp" data-t="00:44:50">[00:44:50]</a> <a class="yt-timestamp" data-t="00:45:01">[00:45:01]</a>. Finetuning slows down development and flexibility <a class="yt-timestamp" data-t="00:45:13">[00:45:13]</a>.
*   **Viability of Building Own LLMs** Companies attempting to build their own LLMs from scratch for end applications often struggle due to immense costs, lack of traction, and the need for expensive AI engineers and data <a class="yt-timestamp" data-t="00:48:42">[00:48:42]</a> <a class="yt-timestamp" data-t="00:48:48">[00:48:48]</a>. The focus should be on riding the technology wave provided by general-purpose LLMs <a class="yt-timestamp" data-t="00:48:52">[00:48:52]</a>.

### Alternatives to Finetuning

Instead of finetuning, Fireflies.ai emphasizes:
*   **Prompt Engineering**: Using precise and constrained prompt engineering to guide the AI's output, ensuring it stays within the given information and doesn't "get too creative" <a class="yt-timestamp" data-t="00:45:55">[00:45:55]</a> <a class="yt-timestamp" data-t="00:46:02">[00:46:02]</a>.
*   **Contextualization**: Leveraging context from meetings to improve AI performance <a class="yt-timestamp" data-t="00:45:55">[00:45:55]</a>.
*   **Dynamic Model Selection**: Utilizing different LLM vendors and models for specific tasks where they excel (e.g., one model for summary overviews, another for shorthand notes, another for action items) <a class="yt-timestamp" data-t="00:46:47">[00:46:47]</a> <a class="yt-timestamp" data-t="00:47:09">[00:47:09]</a>. This requires flexibility <a class="yt-timestamp" data-t="00:47:10">[00:47:10]</a>.
*   **Continuous Experimentation**: Building an in-house A/B experimentation platform to roll out different models, measure performance, and gather customer ratings for responses. This allows for continuous optimization based on user feedback <a class="yt-timestamp" data-t="00:46:11">[00:46:11]</a> <a class="yt-timestamp" data-t="00:46:16">[00:46:16]</a> <a class="yt-timestamp" data-t="00:46:25">[00:46:25]</a>.

## [[challenges_and_opportunities_in_ai_model_finetuning | Challenges in AI Model Development and Evaluation]]

AI models, despite their advancements, present challenges in consistency and reliability.
*   **Consistency**: Newer models may produce different answers for the same input, posing a challenge in controlling for variance <a class="yt-timestamp" data-t="00:42:20">[00:42:20]</a> <a class="yt-timestamp" data-t="00:42:36">[00:42:36]</a>.
*   **Evaluation**: While internal "eyeball tests" can give an initial sense, the ultimate judge of model quality should be the customer <a class="yt-timestamp" data-t="00:46:30">[00:46:30]</a> <a class="yt-timestamp" data-t="00:46:35">[00:46:35]</a>. A large user base allows for quick, strong signals on model performance <a class="yt-timestamp" data-t="00:46:37">[00:46:37]</a>.

## [[pretraining_and_finetuning_ai_models | Strategic Considerations for AI Application Developers]]

For application-layer companies, the focus should shift away from foundational model development:
*   **Solving End-to-End Problems**: The most defensible moat against large incumbents and basic LLM capabilities is solving an end-to-end customer problem deeply within their workflow <a class="yt-timestamp" data-t="00:49:17">[00:49:17]</a> <a class="yt-timestamp" data-t="00:49:52">[00:49:52]</a>. This includes integrating with downstream systems like Salesforce, Asana, and Slack <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a> <a class="yt-timestamp" data-t="00:42:40">[00:42:40]</a>.
*   **Leveraging Cost Reduction**: The decreasing cost of transcription, increased adoption of video conferencing, and the falling cost of AI intelligence are transformative factors <a class="yt-timestamp" data-t="00:49:29">[00:49:29]</a> <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>.
*   **Pricing Strategy**: A hybrid pricing model, combining seat-based pricing for core value with utility-based pricing for complex, high-compute tasks, can be effective <a class="yt-timestamp" data-t="00:52:05">[00:52:05]</a> <a class="yt-timestamp" data-t="00:53:05">[00:53:05]</a>.
*   **Commoditization**: Companies should be willing to be the first to commoditize features as base model capabilities improve, passing the benefits to users <a class="yt-timestamp" data-t="00:54:39">[00:54:39]</a> <a class="yt-timestamp" data-t="00:54:47">[00:54:47]</a>.
*   **Focus on Value**: It is crucial for founders to genuinely solve deep customer problems rather than chasing hype or valuations based solely on being an "AI company" <a class="yt-timestamp" data-t="00:55:51">[00:55:51]</a> <a class="yt-timestamp" data-t="00:56:19">[00:56:19]</a>.

## [[personalization_and_steerability_of_ai_models | Personalization and Steerability of AI Models]]

AI applications can be personalized without direct finetuning:
*   **User Profiles**: Users can inform the AI about their role (e.g., "I am a person in Pharma") to receive tailored insights and recommendations from the same general model <a class="yt-timestamp" data-t="01:03:39">[01:03:39]</a> <a class="yt-timestamp" data-t="01:03:52">[01:03:52]</a>.
*   **AI for Recommendations**: AI is becoming incredibly adept at recommending relevant information and actions, even from smaller datasets, similar to how large companies use recommendation algorithms <a class="yt-timestamp" data-t="01:04:47">[01:04:47]</a> <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>.

## Future Outlook: Multimodal AI and Agentic Collaboration

The future of AI involves more intelligent and integrated systems:
*   **Increased Intelligence**: Future models (e.g., GPT-5) are expected to reach intelligence levels comparable to a PhD, enabling more sophisticated actions and recommendations <a class="yt-timestamp" data-t="00:47:02">[00:47:02]</a> <a class="yt-timestamp" data-t="00:47:08">[00:47:08]</a>.
*   **Multimodality**: Models will process and act upon various types of data, including voice, screen recognition, and external data sources, leading to capabilities like real-time background checks or research during conversations <a class="yt-timestamp" data-t="00:47:42">[00:47:42]</a> <a class="yt-timestamp" data-t="00:48:10">[00:48:10]</a>.
*   **Agentic Future**: An "agentic future" envisions multiple specialized AI agents collaborating (e.g., a meeting agent talking to a legal agent or a search agent to fact-check information) <a class="yt-timestamp" data-t="00:49:06">[00:49:06]</a> <a class="yt-timestamp" data-t="00:51:10">[00:51:10]</a>.
*   **Horizontal AI with Customization**: Instead of highly specialized vertical SaaS, the trend might shift towards general horizontal products that can be customized by users or through an ecosystem of AI apps (like app stores) <a class="yt-timestamp" data-t="01:00:58">[01:00:58]</a> <a class="yt-timestamp" data-t="01:01:40">[01:01:40]</a>.

## [[challenges_and_strategies_in_ai_model_development | Overcoming Incumbent Competition]]

Competing with large incumbents like Microsoft, Google, and Zoom requires distinct strategies:
*   **Deep Execution**: Startups must execute better and go deeper into specific workflows, especially for features that are merely "checklist items" for larger companies <a class="yt-timestamp" data-t="00:53:22">[00:53:22]</a> <a class="yt-timestamp" data-t="00:53:33">[00:53:33]</a>.
*   **AI-First Mindset**: Being an "AI-first" company allows startups to build products with a new perspective, free from legacy baggage and corporate bureaucracy <a class="yt-timestamp" data-t="00:53:50">[00:53:50]</a> <a class="yt-timestamp" data-t="00:54:02">[00:54:02]</a>.
*   **Velocity**: Startups can adapt and innovate faster due to their lean structure, crucial in a rapidly changing AI landscape <a class="yt-timestamp" data-t="01:06:44">[01:06:44]</a>.

## [[challenges_and_strategies_in_ai_model_evaluation | Operationalizing AI at Scale]]

Beyond the AI models themselves, managing the underlying infrastructure is a significant challenge:
*   **Speed and Latency**: Reducing processing time for meetings and notes directly correlates with increased user engagement and utility <a class="yt-timestamp" data-t="00:59:16">[00:59:16]</a> <a class="yt-timestamp" data-t="00:59:30">[00:59:30]</a>.
*   **Infrastructure Management**: Handling millions of meetings, adhering to strict rate limits (e.g., tokens per minute), and managing email sending volumes are massive infrastructural challenges <a class="yt-timestamp" data-t="00:59:52">[00:59:52]</a> <a class="yt-timestamp" data-t="01:00:48">[01:00:48]</a>. This involves breaking down monolithic codebases and optimizing each component <a class="yt-timestamp" data-t="01:00:07">[01:00:07]</a> <a class="yt-timestamp" data-t="01:00:26">[01:00:26]</a>.
*   **Security and Trust**: Handling sensitive conversational data at scale requires robust security measures <a class="yt-timestamp" data-t="01:00:29">[01:00:29]</a>. Gaining customer trust is paramount, especially for startups competing with established incumbents <a class="yt-timestamp" data-t="00:38:41">[00:38:41]</a>.

Overall, the approach to AI development is shifting from deep technical customization of models (like finetuning) to strategic application development that leverages powerful, rapidly evolving base models, focusing on deep workflow integration, user experience, and efficient operations.