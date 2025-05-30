---
title: Grammarlys AI development and application
videoId: jGlSC4t7XvU
---

From: [[redpointai]] <br/> 

Grammarly is an AI assistant app for writing that boasts over 30 million daily active users and has raised over $400 million, with a recent valuation of $13 billion <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. The company has been building AI productivity tools long before the recent wave of generative AI <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## Vision for AI in Communication

Rahul Roy-Chowdhury, CEO of Grammarly, envisions a future where human-to-human communication is more meaningful and forms deeper connections because the drudgery of day-to-day work is handled by AI <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. This means potentially less email and fewer documents, allowing humans to focus on creativity, synthesizing ideas, and connecting <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. The goal is not to create more content, but to make existing communication better, more memorable, evocative, and precise <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

Currently, the average person switches contexts 1,200 times in an average workday <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. AI's promise is to enable a "flow state" where individuals can focus on what they do best, making each conversation measurably more valuable <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. While there's a risk of AI generating and consuming more content, leading to a "dystopian" scenario, Rahul advocates for human agency to bring about a world where AI augments human communication, rather than outsourcing the uniquely human aspects of writing and thinking <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

## Grammarly Product Evolution

Grammarly has been active for 15 years, launching in 2009, and has evolved by riding multiple technology waves, from rules-based systems and natural language processing (NLP) to deep learning models, and now large language models (LLMs) and generative AI (GenAI) <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. Their approach is to identify user problems and then apply the best available technology to solve them <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

### Communication Lifecycle Stages
Grammarly conceptualizes the communication lifecycle in four stages <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>:
1.  **Ideation and Conceptualization** <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>
2.  **Composition** (writing down ideas) <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>
3.  **Revision and Polishing** <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>
4.  **Comprehension** (recipient understanding) <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>

Historically, Grammarly focused primarily on the **revision phase**, helping users correct grammar, ensure clarity, adhere to style guides, strike the right tone, and achieve brevity <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

### Impact of LLMs and Future Direction
LLMs are enabling Grammarly to "turbocharge" the value provided to users in two main ways <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>:
1.  **Tying Communication to Business Outcomes:** Suggestions will become more strategically aligned to desired outcomes. Correctness and polish will increasingly be auto-applied, allowing Grammarly to focus on helping users achieve goals, such as drumming up enthusiasm for an event or clarifying calls to action in an email to a board <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. This aligns with [[generative_ai_for_business_applications | generative AI for business applications]].
2.  **Engagement Across the Entire Lifecycle:** Grammarly is moving beyond just revision to assist with ideation, composition, and comprehension <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. For example, it can summarize long email threads and identify action items <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

## AI Development Process

Grammarly takes a responsible approach to developing and deploying AI features, especially given the importance of communication use cases <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. They do not simply "throw a model over the wall" but undertake significant work to fine-tune models for specific use cases, conduct quality and safety evaluations, and integrate user feedback <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

### Model Evaluation and Quality
Unlike use cases where 60-80% accuracy might be acceptable (e.g., marketing), Grammarly's high-stakes communication requires much greater precision <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. They determine the necessary accuracy levels through various methods <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>:
*   **User Response Tracking:** Monitoring how users accept or reject suggestions and their engagement with features <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. This continuous feedback loop helps fine-tune quality <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
*   **Human Evals:** Conducting side-by-side evaluations where linguistic experts rate LLM outputs against human-generated content to determine preference <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
*   **Experiments and Iteration:** Features are initially launched to a small percentage of users <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. If engagement is low or rejection rates are high, they go back to the drawing board <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
*   **Contextual Dependency:** Quality bars are not one-size-fits-all but are dependent on the specific use case <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.

### Edge Cases and Safety
One example of learning from user feedback is Grammarly's tone detector <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. While generally helpful for adjusting tone (e.g., sounding more positive), they learned to suppress suggestions in sensitive contexts, such as police reports about serious crimes, where a "sound more positive" suggestion would be inappropriate <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. This highlights the importance of understanding specific scenarios to ensure helpful suggestions and suppress unhelpful ones <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.

Ensuring model safety is a priority that cannot be "punted" to the future <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>. Grammarly performs extensive post-processing, fine-tuning, and custom safety evaluations to provide a safe environment for users <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>. They use external benchmarks relevant to their use cases, internal safety evals based on extensive user feedback regarding false positives, and side-by-side comparisons by linguistic experts <a class="yt-timestamp" data-t="00:28:59">[00:28:59]</a>.

### Model Selection and Optimization
Grammarly uses a combination of closed-source and open-source models, typically having about half a dozen in production <a class="yt-timestamp" data-t="00:24:08">[00:24:08]</a>. Most models are fine-tuned on Grammarly's user data for precision in specific use cases <a class="yt-timestamp" data-t="00:24:18">[00:24:18]</a>. The goal is to distill models down to the smallest and most efficient size possible for a given use case without decreasing quality, balancing cost and latency <a class="yt-timestamp" data-t="00:24:33">[00:24:33]</a>. Low latency is crucial for a better user experience and achieving a "flow state" <a class="yt-timestamp" data-t="00:25:11">[00:25:11]</a>.

### Personalization and Organizational Customization
Grammarly leverages its massive user data, processing 75 billion user events daily, to fine-tune and train models for different use cases and personalize experiences <a class="yt-timestamp" data-t="00:25:54">[00:25:54]</a>. This high-quality, contextual data is considered a unique advantage <a class="yt-timestamp" data-t="00:26:22">[00:26:22]</a>.

For individuals, Grammarly helps users sound more like themselves, with a future goal of automating this voice fine-tuning <a class="yt-timestamp" data-t="00:26:40">[00:26:40]</a>. For organizations, it ensures adherence to style guides, brand tones, and corporate values, enforcing compliance across all internal and external communications <a class="yt-timestamp" data-t="00:26:54">[00:26:54]</a>. This involves ingesting organization-specific knowledge and automating rules that might otherwise be manual and out of the communication flow <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>.

### Future Capabilities: Multi-Step Reasoning
A highly anticipated capability for future models is improved multi-step reasoning <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>. This would enable "agentic workflows" where Grammarly could help orchestrate and reason through complex, multi-step communication flows, such as drafting a board email that requires integrating information from various teams (marketing, engineering, product) and adhering to specific communication attributes (brief, succinct, confident) <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>. This capability could be a "game-changer" for reducing the drudgery of work by automating the synthesis and summarization of context <a class="yt-timestamp" data-t="00:21:43">[00:21:43]</a>.

## Competitive Landscape and Moats

Grammarly welcomes competition, viewing it as bringing attention to the problem space of communication assistance and increasing interest in their product <a class="yt-timestamp" data-t="00:31:04">[00:31:04]</a>. Their key differentiators (moats) include <a class="yt-timestamp" data-t="00:31:40">[00:31:40]</a>:
1.  **Proprietary User Data:** The quality and scale of their user data, which allows for continuous product improvement through cyclical feedback loops <a class="yt-timestamp" data-t="00:31:43">[00:31:43]</a>.
2.  **Ubiquitous Presence:** Grammarly operates across a fragmented landscape of tools (e.g., Gmail, Microsoft Word, Slack, Salesforce, Greenhouse), offering a uniform AI stack for communication wherever people work <a class="yt-timestamp" data-t="00:32:09">[00:32:09]</a>. Their focus is on enhancing existing investments in various tools, not on pushing their own platforms <a class="yt-timestamp" data-t="00:33:01">[00:33:01]</a>.

## Organizational Structure of AI Team

Grammarly employs a dual approach to structuring its AI team <a class="yt-timestamp" data-t="00:34:10">[00:34:10]</a>:
*   **Core Research Group:** This team focuses on longer-term initiatives, exploring future capabilities like on-device AI inference based on the trajectory of model efficiency <a class="yt-timestamp" data-t="00:34:35">[00:34:35]</a>. They look 18-24 months out, building necessary infrastructure and addressing data collection gaps <a class="yt-timestamp" data-t="00:34:41">[00:34:41]</a>.
*   **Embedded AI Engineers:** AI engineers are integrated into each product and feature team, working alongside front-end and back-end engineers to launch full-stack features <a class="yt-timestamp" data-t="00:34:55">[00:34:55]</a>.

On-device AI is becoming increasingly capable for simple use cases, and rapid efficiency gains in models suggest it will soon be viable for more complex ones, offering benefits like lower latency, reduced cost of inference, and improved user experience <a class="yt-timestamp" data-t="00:35:16">[00:35:16]</a>.

## Enterprise AI Adoption

Grammarly sees AI as a profound transformation for the workplace, akin to the shift from on-premise to cloud <a class="yt-timestamp" data-t="00:36:03">[00:36:03]</a>. It's a journey, not a one-time deployment, requiring trust in vendor partners <a class="yt-timestamp" data-t="00:36:26">[00:36:26]</a>.

While there's much excitement and experimentation with AI in enterprises, measurable productivity gains have been somewhat "elusive" outside of a few core use cases like software engineering and code generation <a class="yt-timestamp" data-t="00:37:21">[00:37:21]</a>. Grammarly aims to demonstrate tangible value: the average Grammarly user in an organization saves 19 days per year, a significant productivity unlock <a class="yt-timestamp" data-t="00:38:03">[00:38:03]</a>. This focus on measurability and repeatability is crucial for proving AI's impact <a class="yt-timestamp" data-t="00:38:33">[00:38:33]</a>.

### Shift to Enterprise Business
Historically, Grammarly was primarily a direct-to-consumer business <a class="yt-timestamp" data-t="00:48:52">[00:48:52]</a>. A few years ago, they launched an Enterprise business, which is now their fastest-growing segment <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>. Rahul initially thought consumer and enterprise would remain separate but has since changed his mind, realizing the distinction is artificial <a class="yt-timestamp" data-t="00:49:11">[00:49:11]</a>. Many users buy Grammarly for work, blurring the lines between a "consumer sale" and an "Enterprise deployment of one" <a class="yt-timestamp" data-t="00:49:24">[00:49:24]</a>. Grammarly is building the company around a seamless customer journey, from free versions to premium, then self-served team licenses, and finally larger enterprise deals <a class="yt-timestamp" data-t="00:49:35">[00:49:35]</a>.

## AI in Education

AI presents a unique moment for education, offering a powerful new tool that must be incorporated responsibly into pedagogical methods <a class="yt-timestamp" data-t="00:39:51">[00:39:51]</a>. Initially, there was a tendency to "ban AI," but this has largely dissipated <a class="yt-timestamp" data-t="00:40:58">[00:40:58]</a>. Educators are now eager to partner with industry to equip graduates with critical AI skills for the workforce <a class="yt-timestamp" data-t="00:41:02">[00:41:02]</a>.

Grammarly is committed to being a responsible partner in this transformation <a class="yt-timestamp" data-t="00:41:14">[00:41:14]</a>:
*   **Citing AI Use:** They launched a feature that allows users to cite their use of AI in a work product <a class="yt-timestamp" data-t="00:41:18">[00:41:18]</a>. This helps differentiate between a student who merely generates an essay using AI (Student A) and one who engages with the AI tool for feedback and improvement, deepening their understanding (Student B) <a class="yt-timestamp" data-t="00:41:30">[00:41:30]</a>.
*   **Authorship Tool:** Another upcoming feature, "Authorship," provides provenance for every piece of content in a document, indicating if parts were written manually, cut and pasted, or AI-generated <a class="yt-timestamp" data-t="00:42:27">[00:42:27]</a>. This transparency empowers educators and students to set their own acceptable usage guidelines <a class="yt-timestamp" data-t="00:43:04">[00:43:04]</a>.

AI acts as a "leveler" and "democratizer of skills," especially for students globally who lack access to extensive educational resources <a class="yt-timestamp" data-t="00:44:47">[00:44:47]</a>. It enables them to study with assistance where otherwise they might not study at all, opening up new possibilities <a class="yt-timestamp" data-t="00:45:04">[00:45:04]</a>. This supports [[ai_powered_tutoring_tools | AI powered tutoring tools]] and [[integration_of_ai_in_language_fluency_and_pronunciation | integration of AI in language fluency and pronunciation]].

## Rahul Roy-Chowdhury's Views on AI

*   **Overhyped:** Chat interfaces, which he views as "subpar command line interfaces" that hopefully disappear <a class="yt-timestamp" data-t="00:46:41">[00:46:41]</a>.
*   **Underhyped:** AI's potential as a tool to upskill and uplevel people globally, serving as a "force multiplier" for skill development and a "democratizer" of skills <a class="yt-timestamp" data-t="00:46:51">[00:46:51]</a>. Studies show AI is most impactful for individuals in the bottom half of ability in certain tasks <a class="yt-timestamp" data-t="00:47:29">[00:47:29]</a>.
*   **Biggest Surprise in Building AI Features:** The strong resonance and user impact of the tone detector and tone AI feature <a class="yt-timestamp" data-t="00:47:57">[00:47:57]</a>.
*   **Most Exciting AI Startup (Outside Grammarly's Space):** [[compound_ai_systems_and_their_development | AlphaFold]], for its game-changing impact on drug discovery and improving healthcare outcomes through precise research <a class="yt-timestamp" data-t="00:50:07">[00:50:07]</a>. This relates to [[building_ai_applications_for_the_legal_industry | building AI applications for the legal industry]] (as mentioned previously with ModMed, an e-health company using Grammarly strategically).

The web browser of the future, influenced by AI, will likely involve synthesizing information, remembering things across different places, and surfacing content at the right moments, potentially solving issues like "too many tabs" <a class="yt-timestamp" data-t="00:45:50">[00:45:50]</a>. This points to [[the_future_potential_and_development_of_ai_assistance_apis | the future potential and development of AI assistance APIs]].