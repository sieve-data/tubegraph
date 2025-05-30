---
title: Integration and features of Notion AI
videoId: og57f_tv3zY
---

From: [[redpointai]] <br/> 

Notion has quickly integrated [[integration_and_orchestration_of_ai_applications | AI features]] into its product, leveraging large language models (LLMs) and generative AI [00:02:11]. Linus Lee, who helps head Notion's AI initiatives, joined the company's AI team in January 2023 [00:00:05, 00:02:32, 00:02:36].

## History and Development

Notion's journey into AI began around late 2022 [00:02:38]. During a company offsite, CEO Ivan and co-founder Simon dedicated a few days to experiment with GPT-3, which had recently been released [00:03:00, 00:03:02, 00:03:05]. This hackathon-style exploration in a hotel room led to the first version of Notion AI, internally dubbed "Notion AI Writer" [00:03:17, 00:03:32, 00:03:33, 00:03:35].

## Key Notion AI Products

### Notion AI Writer
Notion AI Writer, the first feature to emerge, went into beta in November (likely 2022) and launched in February (likely 2023) [00:03:38, 00:03:41, 00:04:11, 00:04:12]. It integrates AI directly into documents, allowing users to:
*   Summarize pages in specific formats [00:03:48, 00:04:36].
*   Extract key ideas, action items, or topics [00:03:51, 00:05:06].
*   Fix spelling and grammar mistakes [00:03:56, 00:03:57, 00:19:38].
*   Improve writing style and voice [00:04:00, 00:04:01, 00:19:38].
*   Generate basic marketing copy [00:04:09, 00:04:10].
*   Iterate conversationally on generated content, such as making it shorter or more "punchy" [00:04:19, 00:04:30, 00:04:36, 00:35:10].

A core theme identified during its development was the collaborative nature of AI and human interaction to achieve better outcomes [00:04:15, 00:04:18, 00:04:21].

### Notion AI Autofill
Launched in May (likely 2023) as part of Notion's project management suite, [[ai_and_user_interface_customization_in_notion | AI Autofill]] brings AI to Notion databases [00:04:39, 00:04:41, 00:04:44, 00:05:19, 00:05:20]. It allows for automatic filling of entire columns or properties. Examples include:
*   Extracting key topics from meeting notes [00:05:04, 00:05:06].
*   Pulling core needs or company roles from customer or user interview transcripts [00:05:07, 00:05:11, 00:05:13, 00:05:15].
*   Unexpectedly, a popular use case, especially outside the US, was translation [00:18:27, 00:18:32]. This led Notion to build translation into its pre-built prompts [00:18:41].

### Notion Q&A
Notion Q&A is a recent feature designed to understand an entire Notion workspace and answer questions spanning multiple pages [00:00:28, 00:05:23, 00:05:27, 00:05:31, 00:05:35, 00:05:37, 00:05:43]. It emerged from the need to address information-finding problems in increasingly complex Notion workspaces and organizations, coupled with the rise of Retrieval-Augmented Generation (RAG) in the broader [[capabilities_and_limitations_of_ai | AI community]] [00:06:01, 00:06:04, 00:06:08, 00:06:10, 00:06:19, 00:06:28, 00:06:30, 00:06:36, 00:06:37].

Q&A supports multi-turn conversations, allowing users to ask follow-up questions where the AI retains context [00:35:22, 00:35:24, 00:35:30]. It also leverages multilingual capabilities, enabling users to ask questions in one language and receive answers translated from documents in another [00:39:21, 00:39:23, 00:39:27, 00:39:29, 00:39:30].

## Product Development and Team Structure
[[notion_ai_development_and_team_structure | Notion's AI development and team structure]] follows an "expand out and then contract" cycle [00:07:22, 00:07:30].

### Ideation and Prototyping
The process often starts with broad problem statements (e.g., helping people organize or find information) [00:07:37, 00:07:40, 00:07:42]. Motivated by these, a few team members quickly prototype solutions, often leveraging new technologies like RAG [00:07:46, 00:07:50, 00:07:55]. Notion heavily "dogfoods" its own products, meaning employees use them extensively internally [00:08:05, 00:17:00, 00:17:14]. This internal testing helps quickly identify promising and less promising approaches [00:08:10, 00:08:12].

For the Q&A feature, an "annoying prototype" that automatically tried to answer every question asked within the company forced rapid iteration and quality improvement due to constant internal feedback [00:10:02, 00:10:04, 00:10:10, 00:10:19, 00:10:21, 00:10:22, 00:10:32, 00:10:34]. This also helped validate usefulness, as usage and feedback were direct indicators [00:10:57, 00:10:58, 00:11:00].

### Team Composition
The AI team has about a dozen people, split between those focusing on data model quality (correctness, coherence of model outputs) and product concerns (interface, integration into Notion) [00:12:05, 00:12:09, 00:12:11, 00:12:14, 00:12:20, 00:12:22, 00:12:23]. They also work with a couple of designers who help present model outputs effectively [00:12:41, 00:12:42, 00:12:47, 00:12:54].

### Organizational Structure
Currently, Notion maintains a core AI team that owns the backend components and UI for specific AI surfaces (e.g., AI Writer's bar, Q&A's chatbox) [00:13:14, 00:13:16, 00:13:20, 00:13:22, 00:13:24, 00:13:27, 00:13:30, 00:13:33, 00:13:34, 00:13:37]. For features like Autofill, which are deeply integrated with other product areas (e.g., databases), ownership may lie with the relevant product team, but with tight collaboration with the core AI team on hard AI problems [00:13:40, 00:13:42, 00:13:43, 00:13:46, 00:13:48, 00:13:49, 00:13:51, 00:13:54, 00:13:55, 00:13:57].

Notion is still exploring the optimal organizational structure as [[notion_ai_development_and_team_structure | AI capabilities]] evolve. Options include a central "hub" team that liaises with other teams, or potentially embedding "AI engineers" within every product team [00:14:01, 00:14:05, 00:14:13, 00:14:15, 00:14:17]. Linus believes that even with broader AI proficiency across engineers, a centralized team will still be crucial for foundational tasks like monitoring, quality assurance, data set management, and training workflows [00:16:16, 00:16:18, 00:16:33, 00:16:35, 00:16:37, 00:16:41, 00:16:43, 00:16:44, 00:16:47, 00:16:48].

## Challenges in AI Integration
[[challenges_and_opportunities_in_ai_integration | Challenges and opportunities in AI integration]] include:

### Evaluation and Correctness
Evaluating model outputs, particularly for features requiring high correctness like Q&A, is a significant challenge [00:23:07, 00:23:14, 00:23:20, 00:23:24]. Unlike creative writing tasks where there's "wiggle room" for different acceptable outputs, Q&A demands specific, accurate answers, leaving less room for error [00:23:27, 00:23:30, 00:23:33, 00:23:37, 00:23:45, 00:23:46, 00:23:48, 00:23:50].

### Anticipating User Questions
A major difficulty has been anticipating the wide variety of questions users might ask, especially those that "poke at the edges" of the model's capabilities [00:24:36, 00:24:38, 00:25:07, 00:25:09]. This includes:
*   **Meta questions**: Questions about Notion itself (e.g., "how can I share this page?") rather than content within the workspace [00:24:19, 00:24:21, 00:24:23, 00:24:24, 00:24:25, 00:24:26, 00:24:32].
*   **Time-based queries**: Questions involving temporal context (e.g., "what is the marketing team working on this week?") that require the model to interpret dynamic information rather than static documents [00:24:40, 00:24:42, 00:24:47, 00:24:48, 00:24:50, 00:24:51, 00:24:52, 00:24:55, 00:24:57, 00:25:01, 00:25:03].

Creating high-quality evaluation sets for these edge cases and defining grading criteria are crucial steps [00:25:14, 00:25:15, 00:25:17].

### Operational Concerns
Questions around customer privacy, security, and the necessary scale of the infrastructure were also significant, often requiring "first principles" thinking due to the novelty of large language model augmented question answering [00:25:33, 00:25:36, 00:25:38, 00:25:43, 00:25:45, 00:25:47, 00:25:50, 00:25:51, 00:25:55, 00:25:56, 00:25:58, 00:26:00, 00:26:01, 00:26:03].

## Model Strategy

### Custom Tools and Evaluation
Notion has largely built its own internal tools for working with language model-powered features [00:26:21, 00:26:24, 00:26:26, 00:26:28]. This was partly due to a lack of suitable off-the-shelf tools when they started [00:26:31, 00:26:33, 00:26:36, 00:26:38] and the complex, structured nature of Notion documents (rich text, tables, images, metadata) [00:26:40, 00:26:42, 00:26:45, 00:26:48, 00:26:50, 00:26:54, 00:26:55, 00:26:57, 00:27:00, 00:27:02, 00:27:04, 00:27:06, 00:27:07, 00:27:09, 00:27:10]. Having proprietary tools also allows for faster iteration [00:27:22, 00:27:24, 00:27:26].

Notion uses a spectrum of evaluation methods:
*   **Deterministic, programmatic evaluations**: Automated checks of model outputs [00:27:58, 00:28:01].
*   **Human annotators**: A team reviews outputs, speeding up processes [00:28:38, 00:28:40, 00:28:42].
*   **ML Engineers' manual inspection**: Engineers directly analyze model outputs and data sets to understand *why* models fail, not just *that* they fail, identifying specific issues like misinterpreting instructions or struggling with relative dates [00:28:44, 00:28:46, 00:28:49, 00:28:52, 00:28:53, 00:28:54, 00:28:56, 00:28:57, 00:28:58, 00:29:01, 00:29:02, 00:29:05, 00:29:06, 00:29:07, 00:29:09, 00:29:10, 00:29:11, 00:29:12, 00:29:14].

Notion iterates on the "full stack," from data representation to the final output, intervening at different stages of the RAG pipeline depending on the cause of model errors (e.g., embedding/ranking issues vs. answering problems) [00:29:29, 00:29:31, 00:29:33, 00:29:35, 00:29:38, 00:29:40, 00:30:07, 00:30:10, 00:30:12, 00:30:16, 00:30:17, 00:30:19, 00:30:20, 00:30:22, 00:30:23, 00:30:25, 00:30:26, 00:30:28, 00:30:29, 00:30:30, 00:30:33, 00:30:35, 00:30:37, 00:30:38, 00:30:39, 00:30:41, 00:30:42].

### Partnership with LLM Providers
Notion has strong partnerships with Anthropic and OpenAI, relying on them for core model building and infrastructure [00:31:08, 00:31:09, 00:31:12, 00:31:17, 00:31:19, 00:31:22, 00:31:24]. Notion's role is to deeply understand specific tasks, collect or generate synthetic data, and evaluate models for those tasks [00:31:40, 00:31:42, 00:31:44, 00:31:46, 00:31:49, 00:31:51, 00:32:32, 00:32:35, 00:32:38, 00:32:40, 00:32:42, 00:33:04, 00:33:05, 00:33:07]. For example, the criteria for a "good summary" vary significantly depending on the document type (meeting note vs. technical document vs. bug report) [00:32:45, 00:32:47, 00:32:48, 00:32:49, 00:32:51, 00:32:53, 00:32:55, 00:32:56, 00:32:58, 00:32:59, 00:33:01].

A key commitment is not training models on customer data, which pushes the team to systematically understand Notion workspace archetypes for synthetic data generation [00:31:57, 00:32:00, 00:32:06, 00:32:07, 00:32:11, 00:32:13, 00:32:15, 00:32:18, 00:32:19, 00:32:21, 00:32:23, 00:32:24].

Notion evaluates different models based on their performance, capabilities, cost, and throughput needs (e.g., a batch process like Autofill requires higher throughput) [00:33:33, 00:33:49, 00:33:51, 00:33:53, 00:33:54, 00:33:57, 00:33:59, 00:34:00, 00:34:02, 00:34:04, 00:34:06, 00:34:08, 00:34:09, 00:34:10, 00:34:12, 00:34:15, 00:34:18, 00:34:20, 00:34:22, 00:34:25, 00:34:26, 00:34:27]. While they have explored open-source models, they have not yet shipped any to production [00:33:16, 00:33:20, 00:33:22, 00:33:25, 00:33:29].

### Prompt Engineering
User prompts are often wrapped in Notion's own processing and prompt templates, including dialogue history and context from the user's page or workspace [00:34:54, 00:34:56, 00:34:59, 00:35:01, 00:35:04, 00:35:06, 00:35:08, 00:35:10, 00:35:12, 00:35:13, 00:35:15, 00:35:16, 00:35:19, 00:35:22, 00:35:37, 00:35:38, 00:35:39, 00:35:42, 00:35:44, 00:35:46, 00:35:47, 00:35:51].

When designing prompts, the focus is on clear evaluation criteria and a thorough understanding of the task and desired output format [00:37:02, 00:37:04, 00:37:05, 00:37:07, 00:37:09, 00:37:15, 00:37:16, 00:37:18, 00:37:21, 00:37:25, 00:37:27, 00:37:28, 00:37:31, 00:37:32, 00:37:33, 00:37:35, 00:37:37]. While minor "per-model" tweaks may be needed (e.g., to prevent specific phrases), the core instructions tend to be transferable across models as they improve at following directions [00:37:40, 00:37:43, 00:37:45, 00:37:46, 00:37:47, 00:37:50, 00:37:52, 00:37:54, 00:37:57, 00:37:59, 00:38:01, 00:38:03, 00:38:05, 00:38:07, 00:38:09, 00:38:11, 00:38:13, 00:38:15, 00:38:16, 00:38:18, 00:38:19, 00:38:21, 00:38:23, 00:38:25, 00:38:26, 00:38:27, 00:38:29, 00:38:30].

## User Interaction and Interface

### Learning from Users
Internal usage provides the richest source of information on useful ways to use new features, but Notion's internal usage isn't fully representative of all customers (e.g., individuals, students vs. large organizations) [00:17:12, 00:17:14, 00:17:17, 00:17:18, 00:17:20, 00:17:22, 00:17:24, 00:17:26, 00:17:27, 00:17:29, 00:17:31, 00:17:33, 00:17:35, 00:17:36, 00:17:38, 00:17:39, 00:17:42, 00:17:44, 00:17:46, 00:17:47, 00:17:50].

Early testers and Notion ambassadors often use initial features for "totally unanticipated use cases," sometimes inspiring new features or built-in prompts [00:17:55, 00:17:57, 00:18:00, 00:18:02, 00:18:04, 00:18:07, 00:18:08, 00:18:09, 00:18:10, 00:18:14, 00:18:15, 00:18:16, 00:18:18, 00:18:20, 00:18:22, 00:18:24].

### Pre-built vs. Custom Prompts
Notion follows a pattern of offering both "sanctioned" templates and fully customizable options [00:18:45, 00:18:46, 00:18:48, 00:18:50, 00:18:55, 00:18:57, 00:18:59, 00:19:01, 00:19:02, 00:19:03]. Popular use cases are integrated into pre-built prompts (e.g., summarization, writing improvement, grammar correction, translation) [00:19:11, 00:19:12, 00:19:13, 00:19:15, 00:19:17, 00:19:26, 00:19:29, 00:19:32, 00:19:34, 00:19:36, 00:19:38, 00:19:40, 00:19:41, 00:19:42, 00:19:44].

While pre-built prompts are widely used, a significant portion of usage comes from users iterating on model outputs or creating their own custom prompts [00:19:45, 00:19:48, 00:19:50, 00:19:52, 00:19:55, 00:19:57, 00:19:59, 00:20:01, 00:20:03]. Power users often start with pre-built options for inspiration, then hand-write and reuse specific prompts for their unique workflows (e.g., a newsletter writer using a template to generate social media tags) [00:20:07, 00:20:09, 00:20:12, 00:20:13, 00:20:16, 00:20:18, 00:20:19, 00:20:20, 00:20:22, 00:20:24, 00:20:26, 00:20:27, 00:20:29, 00:20:30, 00:20:33, 00:20:36, 00:20:38, 00:20:40].

### Guiding User Interaction
Notion aims to help users overcome the "blank canvas problem" [00:20:45, 00:20:47, 00:20:49, 00:20:55]. Presenting options or suggesting next steps (e.g., revisions after AI generation) can significantly reduce the "mental work" of interacting with AI [00:22:02, 00:22:04, 00:22:07, 00:22:10, 00:22:12, 00:22:15, 00:22:18, 00:22:19, 00:22:20, 00:22:23, 00:22:25, 00:22:26, 00:22:29, 00:22:30, 00:22:32].

For [[ai_and_user_interface_customization_in_notion | AI and user interface customization]], the goal is to provide the "right building blocks" and abstractions [00:40:02, 00:40:04, 00:40:06, 00:40:08, 00:40:11, 00:40:13, 00:40:15, 00:40:17, 00:40:19, 00:40:21, 00:40:22, 00:40:24, 00:40:26, 00:40:28, 00:40:30, 00:40:33, 00:40:35, 00:40:38, 00:40:40, 00:40:41, 00:40:43, 00:40:45, 00:40:47, 00:40:49, 00:40:51, 00:40:53, 00:40:56, 00:40:57, 00:41:00, 00:41:02]. This includes exploring "generative interfaces" where models output UI components or can perform actions, requiring a structured language or component library for coherence [00:41:18, 00:41:19, 00:41:22, 00:41:24, 00:41:26, 00:41:28, 00:41:30, 00:41:32, 00:41:34, 00:41:35, 00:41:39, 00:41:40, 00:41:42, 00:41:44, 00:41:45, 00:41:47, 00:41:49, 00:41:51, 00:41:53, 00:41:55, 00:41:56].

## Overhyped vs. Underhyped in AI
Linus Lee shares his views on current trends in AI:
*   **Overhyped: Context Length**
    He struggles to imagine truly useful tasks requiring extremely long context windows (e.g., 50,000 words or 100,000 tokens), noting that noise in the data still hinders performance [00:42:22, 00:42:24, 00:42:28, 00:42:30, 00:42:34, 00:42:38, 00:42:41, 00:42:44, 00:42:45, 00:42:46]. He believes that RAG (retrieving good information into context) is always the necessary starting point [00:42:52, 00:42:53, 00:42:55, 00:42:59, 00:43:01, 00:43:02]. He suggests that most useful tasks may only require 16k to 32k tokens [00:44:16, 00:44:18, 00:44:20, 00:44:22, 00:44:25, 00:44:26, 00:44:27, 00:44:30].
*   **Underhyped: Alternatives to Transformers**
    While Transformers are excellent at modeling long sequences efficiently, there's nothing architecturally "most optimal" about them [00:44:36, 00:44:39, 00:44:40, 00:44:41, 00:44:42, 00:44:45, 00:44:46, 00:44:48, 00:44:51, 00:44:53, 00:44:56]. He predicts that new architectures that are also efficient at sequence modeling will emerge in the coming years [00:44:58, 00:44:59, 00:45:00, 00:45:02, 00:45:05, 00:45:06, 00:45:09, 00:45:11, 00:45:13, 00:45:14, 00:45:16, 00:45:19, 00:45:20, 00:45:22, 00:45:23, 00:45:25, 00:45:27, 00:45:29, 00:45:31, 00:45:33, 00:45:34, 00:45:36, 00:45:37, 00:45:39, 00:45:40, 00:45:44, 00:45:45, 00:45:47, 00:45:48]. He is particularly interested in state-space models [00:45:50, 00:45:53].

## Biggest Surprises / Learnings
A significant surprise has been how effective "really general approaches" can be [00:46:14, 00:46:18, 00:46:20]. Instead of building separate, specialized models for distinct tasks, training a single model on various data sets for different use cases can lead to a model that "overall understands the domain of your product better" [00:46:51, 00:46:53, 00:46:55, 00:46:56, 00:46:57, 00:47:00, 00:47:03, 00:47:04, 00:47:06, 00:47:08, 00:47:11, 00:47:12, 00:47:14, 00:47:16, 00:47:18, 00:47:19].

Notion is also exploring giving AI more control over what appears on screen in "generative UI" scenarios, which is a harder ML problem but promises more interesting long-term possibilities [00:47:22, 00:47:24, 00:47:28, 00:47:32, 00:47:33, 00:47:36, 00:47:38, 00:47:40, 00:47:42, 00:47:43, 00:47:46, 00:47:48, 00:47:50, 00:47:53, 00:47:55, 00:47:56]. Given the rapid [[advancements_in_ai_for_creative_tools | advancements in AI]], betting on generality is seen as a worthwhile strategy [00:47:59, 00:48:00, 00:48:03, 00:48:05].