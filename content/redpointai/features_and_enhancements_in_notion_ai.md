---
title: Features and enhancements in Notion AI
videoId: og57f_tv3zY
---

From: [[redpointai]] <br/> 

Notion AI is a suite of artificial intelligence features integrated into the Notion workspace, designed to augment user productivity across various tasks. Linus Lee, who helps lead Notion's AI efforts, discusses the development and evolution of these features, highlighting their rapid deployment and user-centric approach <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Origin of Notion AI
The idea for Notion AI originated from a company offsite in late 2022. Notion's CEO, Ivan, and co-founder, Simon, took a few days to experiment with GPT-3, which had just been released <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. This hackathon-style exploration led to the first version of Notion AI, initially known as "Notion AI Writer" <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

## Key Features

### Notion AI Writer
Launched in beta in November 2022 and generally available in February 2023, Notion AI Writer is designed to assist users directly within their documents <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. Its capabilities include:
*   **Summarization**: Condensing pages into various formats or extracting key ideas, action items, and topics <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Editing and Revision**: Fixing spelling and grammar mistakes, and improving writing style and voice <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Drafting**: Helping users generate initial drafts or marketing copy <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **Iterative Refinement**: Users can conversationally follow up on generated content, asking for adjustments like making it shorter or more "punchy" <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

### AI Autofill
Released in May 2023, AI Autofill integrates AI into Notion databases, which are often used for project management <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a> <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. It can automatically populate entire columns or "properties" within a database <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. Examples include:
*   Extracting key topics from meeting notes <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   Pulling out core needs or company roles from user interview transcripts <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
*   Translation: Initially an unanticipated [[user_interaction_with_notion_ai | use case]] identified from user behavior, translation is now a built-in prompt <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a> <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.

### Notion Q&A
Notion Q&A is a newer feature that allows AI to understand the entire workspace and answer questions, potentially spanning multiple pages <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a> <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. It addresses the common problem of finding information in increasingly complex organizational workspaces <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a> <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   **Information Retrieval**: Solves the "information finding problem" by grounding AI in factual information from the user's workspace, leveraging retrieval-augmented generation (RAG) <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a> <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   **Contextual Understanding**: Supports multi-turn conversations, allowing users to ask follow-up questions where the AI retains context from previous interactions <a class="yt-timestamp" data-t="00:35:24">[00:35:24]</a>.
*   **Multilingual Capability**: Can read documents in one language (e.g., Japanese) and translate the answer back to the user's query language <a class="yt-timestamp" data-t="00:39:21">[00:39:21]</a>.

## [[notion_ai_team_structure_and_development_process | Notion AI Team Structure and Development Process]]
Notion's AI team operates with an "expand out and then contract" cycle, balancing user problem-solving with exploration of new AI capabilities <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a> <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **Prototyping**: The team quickly prototypes ideas, often using "dogfooding" (internal testing) to determine which approaches are most promising <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a> <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. An "annoying prototype" for Q&A, for instance, forced rapid iteration and quality improvement due to constant internal exposure <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.
*   **Team Composition**: The core AI team consists of about a dozen people, split between data/model quality and product concerns like interface and integration <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. They also collaborate closely with designers <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.
*   **Organizational Structure**: The AI team owns both backend and UI components for specific AI "surfaces" (like AI Writer and Q&A chatbox) <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. Features like Autofill are more deeply integrated with existing product teams (e.g., databases team), requiring tight collaboration <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>. There's an ongoing discussion about centralizing foundational AI technologies versus embedding AI engineers in every product team <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a> <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.

## [[user_interaction_with_notion_ai | User Interaction and Interface Design]]
Notion prioritizes understanding how users interact with AI products to inform design and education <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.
*   **Internal Dogfooding**: Internal usage provides the richest source of information on useful ways to use AI, though Notion employees may not be fully representative of all user segments (e.g., individuals, students) <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>.
*   **Early Testers and Ambassadors**: External partners often discover unanticipated [[user_interaction_with_notion_ai | use cases]], which can inspire new features or built-in prompts, like the translation feature for Autofill <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.
*   **Pre-built vs. Custom Prompts**: Notion provides pre-baked "formulas" or templates for common tasks (e.g., summarization, improving writing, fixing grammar) <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a> <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>. While these are the most popular, advanced users often start with them and then iterate using custom prompts to fit specific needs <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>. This approach helps users overcome the "blank canvas problem" <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>.

## [[challenges_in_deploying_ai_in_notion | Challenges in Deploying AI]]
Notion faced several [[challenges_in_deploying_ai_in_notion | challenges in deploying AI]] features:
*   **Evaluation and Quality Control**: Ensuring correctness and quality is particularly hard for Q&A, where answers are expected to be specific. Unlike creative writing, there's less "wiggle room" for errors <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.
    *   **Edge Cases**: Anticipating and handling various types of questions, such as "meta" questions about Notion itself (e.g., "how can I share this page with Jack?") or questions involving time ranges (e.g., "what is the marketing team working on this week?") <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a> <a class="yt-timestamp" data-t="00:24:36">[00:24:36]</a>.
    *   **Evaluation Tools**: Notion built most of its evaluation tools in-house due to the complexity and structured nature of Notion documents (rich text, tables, images, metadata) <a class="yt-timestamp" data-t="00:26:28">[00:26:28]</a>. These tools allow for faster iteration and comparison of model outputs <a class="yt-timestamp" data-t="00:27:24">[00:27:24]</a>. Evaluation involves a spectrum from deterministic programmatic checks to human annotators and in-depth analysis by ML engineers to understand *why* models fail <a class="yt-timestamp" data-t="00:28:38">[00:28:38]</a>.
*   **Operational Concerns**: Addressing customer needs around privacy and security, and ensuring the system can handle scale for language model-augmented features <a class="yt-timestamp" data-t="00:25:33">[00:25:33]</a>.
*   **Model Selection and Integration**: Notion partners with Anthropic and OpenAI for their foundational models, acknowledging the difficulty of competing at the infrastructure level <a class="yt-timestamp" data-t="00:31:08">[00:31:08]</a> <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>.
    *   **Data Privacy**: A key commitment is not training models on customer data <a class="yt-timestamp" data-t="00:31:57">[00:31:57]</a>. This encourages systematic thinking about generating synthetic data that accurately represents Notion workspace archetypes <a class="yt-timestamp" data-t="00:32:11">[00:32:11]</a>.
    *   **Task Understanding**: Notion's role is to understand the specific tasks its models need to perform and build appropriate datasets and evaluations around them, recognizing that criteria for a "good summary" differ significantly between document types (e.g., meeting notes vs. technical documents vs. bug reports) <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a> <a class="yt-timestamp" data-t="00:33:04">[00:33:04]</a>.
    *   **Prompt Engineering**: Prompts are often heavily wrapped in Notion's own processing, including context about the page or workspace <a class="yt-timestamp" data-t="00:34:58">[00:34:58]</a>. While general instructions carry over between models, fine-tuning for specific model quirks is sometimes necessary <a class="yt-timestamp" data-t="00:38:11">[00:38:11]</a>.

## Future Outlook and Philosophy
Linus Lee believes that while context length in models is "overhyped" for most useful tasks <a class="yt-timestamp" data-t="00:42:24">[00:42:24]</a>, [[advancements_in_ai_developer_tools | alternatives to Transformers]] are "underhyped" and could offer more efficient sequence modeling <a class="yt-timestamp" data-t="00:44:36">[00:44:36]</a> <a class="yt-timestamp" data-t="00:44:50">[00:44:50]</a>.
*   **Generality over Specificity**: He suggests that investing in general approaches that can solve multiple tasks (e.g., a single model trained on diverse datasets for various functions) yields longer-term payoffs by enabling the model to better understand the product's domain <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>.
*   **Generative Interfaces**: Notion is exploring models that can output interactive UI elements instead of just text <a class="yt-timestamp" data-t="00:47:24">[00:47:24]</a>. This requires defining the "building blocks" or "component library" for AI-generated interfaces, akin to how Notion provides rich blocks for user customization <a class="yt-timestamp" data-t="00:40:48">[00:40:48]</a>. Giving AI more control over UI generation is a harder ML problem but could lead to more interesting outcomes <a class="yt-timestamp" data-t="00:47:48">[00:47:48]</a>.