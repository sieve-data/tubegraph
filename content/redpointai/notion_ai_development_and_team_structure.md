---
title: Notion AI development and team structure
videoId: og57f_tv3zY
---

From: [[redpointai]] <br/> 

Notion has quickly integrated advanced AI features into its product, leveraging large language models (LLMs) and generative AI to enhance user experience <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>. The company's approach involves a blend of user-centric problem-solving and proactive exploration of new AI capabilities <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

## Origin and Product Evolution

Notion's journey into AI began around late 2022. During a company offsite, CEO Ivan Zhao and co-founder Simon Last took a few days to experiment with GPT-3, recognizing its potential as a writing tool <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. This hackathon-style effort led to the first version of Notion AI <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

Key Notion AI features include:
*   **Notion AI Writer** Launched in beta in November 2022 and released in February 2023, this feature helps users write, summarize pages, extract key ideas or action items, fix spelling and grammar, and improve writing style. It supports iterative refinement, allowing users to conversationally adjust generated content (e.g., "make it shorter" or "more punchy") <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **AI Autofill** Released in May 2023, this feature integrates AI into Notion databases, often used for project management. It can automatically fill entire columns or properties, such as extracting key topics from meeting notes or core user needs from interview transcripts <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
*   **Notion Q&A** A newer feature, Notion Q&A understands the entire workspace, allowing users to ask questions and receive answers based on information across multiple pages <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. This addresses the common problem of finding information in increasingly complex Notion workspaces <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

## AI Development Process

Notion's AI team operates on an "expand out and then contract" cycle <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
1.  **Exploration**: They start with broad problem statements, such as helping users find information or organize content. Motivated by these, they prototype quickly using promising technologies like retrieval-augmented generation (RAG) <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
2.  **Dogfooding**: Notion heavily "dogfoods" its products internally. Prototypes are used by the entire company, providing immediate feedback and forcing rapid iteration on output quality. This continuous exposure helps validate usefulness and adds pressure to improve <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
3.  **Refinement**: Based on internal usage and external early testers (Notion ambassadors, partners), they identify promising approaches and recalibrate, leading to a more defined solution <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
4.  **Productization**: Once a clear direction is established, the process becomes more like traditional product building, involving user research and designers to ensure a confident user experience and model quality <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.

> [!NOTE] User-driven adaptation
> Initial features are often extended by users in unanticipated ways. For instance, Autofill was heavily used for translation outside the US, leading Notion to build translation as a native, pre-built prompt <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>. This iterative process of discovering common use cases via custom prompts and then baking them into templates is a core Notion pattern <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>.

## AI Team Structure

The Notion AI team consists of about a dozen people <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. It's roughly split into two halves:
*   **Data Model & Quality**: Focuses on the correctness and coherence of model outputs <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.
*   **Product Concerns**: Works on the user interface and [[integration_and_features_of_notion_ai | integration into Notion]] <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>.
*   **Design Resources**: The team also collaborates closely with a couple of designers who help present model outputs in user-friendly ways <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.

The ownership of AI features is evolving. Currently, the core AI team owns features with a specific AI surface (like AI Writer and Q&A). However, features deeply integrated with other Notion products, like Autofill with databases, are owned by those respective product teams, though close collaboration with the AI team continues for complex AI problems <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. This fluid structure reflects the ongoing process of determining the [[ai_integration_and_product_development_strategies | foundational pieces of Notion AI]] and how they intersect with existing product areas <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. It's an open question whether AI engineers will eventually be embedded in every team, or if a centralized infrastructure team will remain essential for quality, monitoring, and data management <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.

## Challenges in AI Development

Developing AI features like Q&A presents unique challenges, particularly regarding evaluation <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.
*   **Correctness and Quality**: For features like Q&A, precise answers are critical, making evaluation much more black and white compared to creative writing tasks where there's more "wiggle room" <a class="yt-timestamp" data-t="00:23:48">[00:23:48]</a>.
*   **Anticipating User Questions**: It's challenging to anticipate the full range of user questions, especially "meta" questions about Notion itself (e.g., "How can I share this page with Jack?") or time-sensitive queries (e.g., "What is the marketing team working on this week?") that require sophisticated understanding beyond a simple document lookup <a class="yt-timestamp" data-t="00:24:19">[00:24:19]</a>.
*   **Operational Concerns**: Addressing customer needs around privacy and security, as well as managing the necessary scale for AI features, required starting from first principles due to a lack of clear industry answers <a class="yt-timestamp" data-t="00:25:33">[00:25:33]</a>.

## Tooling and Evaluation

Notion has primarily built its own internal tools for working with language models <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>. This decision was driven by the early stage of the industry when few suitable tools existed, and by the unique complexity of Notion documents (rich text, tables, images, metadata) which don't map well to simpler formats like PDFs or Wikipedia pages <a class="yt-timestamp" data-t="00:26:40">[00:26:40]</a>. In-house tools also allow for faster iteration and customization (e.g., comparing more than two models side-by-side) <a class="yt-timestamp" data-t="00:27:24">[00:27:24]</a>.

Evaluation occurs across a spectrum:
*   **Deterministic Programmatic Evaluations**: Automated checks of model outputs <a class="yt-timestamp" data-t="00:27:58">[00:27:58]</a>.
*   **Human Annotators**: A team reviews outputs to speed up certain processes <a class="yt-timestamp" data-t="00:28:38">[00:28:38]</a>.
*   **ML Engineers' Qualitative Review**: ML engineers deeply examine model outputs to understand *why* a model is failing (e.g., misinterpreting instructions, struggling with relative dates vs. absolute dates). This costly but high-payoff approach helps identify where in the pipeline to intervene (e.g., embeddings, ranking, or the answering component) <a class="yt-timestamp" data-t="00:28:44">[00:28:44]</a>.

## Model Strategy

Notion has strong partnerships with Anthropic and OpenAI, relying on them for foundational model building and scalable hosting <a class="yt-timestamp" data-t="00:31:08">[00:31:08]</a>. Notion's role in this partnership is to:
*   **Understand Tasks**: Deeply understand the specific tasks its models need to perform <a class="yt-timestamp" data-t="00:31:40">[00:31:40]</a>.
*   **Data Set Curation**: Collect or generate synthetic data for those models. Notion has committed to not training on customer data <a class="yt-timestamp" data-t="00:31:46">[00:31:46]</a>. This limitation has pushed them to systematically understand Notion workspace archetypes and document structures to create high-quality synthetic data <a class="yt-timestamp" data-t="00:32:06">[00:32:06]</a>.
*   **Evaluation**: Define clear criteria for evaluating task performance (e.g., what makes a good summary for a meeting note versus a technical document) <a class="yt-timestamp" data-t="00:32:40">[00:32:40]</a>.

Notion iterates on the full stack, experimenting with different pipeline stages (e.g., rephrasing retrieved passages) <a class="yt-timestamp" data-t="00:29:30">[00:29:30]</a>. They decide which model to use based on capabilities, cost, and throughput requirements, potentially using different models or providers for different features <a class="yt-timestamp" data-t="00:33:49">[00:33:49]</a>. While open-source models are explored for areas like embeddings, Notion hasn't shipped production features with them yet <a class="yt-timestamp" data-t="00:33:16">[00:33:16]</a>.

## User Interaction and Interface Design

Notion emphasizes providing users with the right "building blocks" and abstractions for [[ai_and_user_interface_customization_in_notion | AI and user interface customization]]. For every AI feature, users can access a direct prompting interface <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>. However, Notion also provides pre-built prompts to guide users and overcome the "blank canvas problem" <a class="yt-timestamp" data-t="00:40:08">[00:40:08]</a>. The most popular use cases are often driven by these pre-built options (e.g., summarization, grammar fixes), but users frequently iterate on the outputs to fit specific needs <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>. Power users often hand-write and reuse custom prompts <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.

Notion is exploring whether AI can output interactive UI elements (generative interfaces) or perform actions, which would require defining new "blocks" or a domain-specific language for AI outputs <a class="yt-timestamp" data-t="00:41:18">[00:41:18]</a>.

## AI Team Philosophy and Learnings

*   **Betting on Generality**: Notion has been surprised by how well general approaches work, suggesting that investing in a single model that can perform multiple tasks (even by combining data sets for different tasks) may yield better long-term outcomes and a deeper understanding of the product's domain <a class="yt-timestamp" data-t="00:46:14">[00:46:14]</a>.
*   **Iterate Quickly**: In the early phases of development, rapid iteration is key, especially when dealing with AI outputs where quality and usefulness need constant refinement <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
*   **"Garden Approach" to Innovation**: Similar to places like Midjourney or GitHub Next, Notion's environment allows individuals to champion specific ideas and push prototypes forward rapidly. This "garden" of different people trying different things can yield productive outcomes <a class="yt-timestamp" data-t="00:48:29">[00:48:29]</a>.

The development of [[compound_ai_systems_and_their_development | compound AI systems]] is a key focus, as getting foundational components like retrieval right can augment many capabilities beyond just question answering <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>. While long context windows are currently "overhyped," robust retrieval and effective data filtering will always be essential <a class="yt-timestamp" data-t="00:42:24">[00:42:24]</a>. The exploration of alternative architectures to Transformers is "underhyped," as more efficient and effective sequence modeling approaches may emerge <a class="yt-timestamp" data-t="00:44:36">[00:44:36]</a>.