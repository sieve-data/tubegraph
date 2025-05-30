---
title: Challenges in building and deploying AI features
videoId: og57f_tv3zY
---

From: [[redpointai]] <br/> 

Building and deploying AI features, especially with large language models (LLMs), presents unique challenges, as experienced by Notion's AI team led by Linus Lee. These challenges span product development, technical implementation, resource allocation, and organizational structure.

## Product Development Challenges
When developing AI features, Notion's team balances traditional product management — understanding core user problems — with exploring new AI capabilities [00:07:08]. The approach often involves a "expand out and then contract" cycle, where initial hunches about broad problems (e.g., organizing or finding information) lead to rapid prototyping with promising technologies like Retrieval-Augmented Generation (RAG) [00:07:30].

A key aspect of Notion's development process is "dogfooding," where the AI features are extensively tested internally [00:08:05]. This internal usage, even if initially "annoying" (as with the early Q&A prototype), forces rapid iteration and immediate feedback on output quality [00:10:02]. It also helps validate usefulness, as lack of internal adoption indicates a feature is not helpful [00:11:03].

## Technical and Operational Challenges
### Evaluation and Quality Control
A significant [[challenges_in_ai_model_training_and_deployment | challenge in AI model training and deployment]] for Notion, especially for features like Q&A where correctness matters, is evaluation [00:23:14]. Unlike writing tools that allow for "wiggle room" in output, Q&A requires specific and accurate answers, making evaluation more "black and white" [00:23:48]. The model can fail in numerous ways, such as saying the wrong thing or ignoring the correct document [00:23:54].

Linus Lee notes that anticipating all types of user questions and constructing high-quality evaluation sets is difficult [00:25:07]. Users often ask "meta" questions about Notion itself (e.g., "How can I share this page with Jack?") or questions involving dynamic time ranges (e.g., "What is the marketing team working on this week?") which push the boundaries of a traditional RAG pipeline [00:24:19].

To address these [[challenges_and_advancements_in_ai_model_development | challenges]], Notion builds most of its evaluation tools in-house [00:26:24]. This is due to the complex, structured nature of Notion documents (rich text, tables, images, metadata) which aren't easily handled by off-the-shelf tools [00:26:40]. In-house tools also allow for faster iteration and customization [00:27:24]. Evaluation methods range from deterministic, programmatic checks to human annotation and direct observation by ML engineers to understand *why* a model fails [00:27:58].

### Resource Allocation and Staffing
Determining how to staff AI projects is another [[challenges_in_enterprise_ai_deployment | enterprise AI adoption challenge]] [00:09:22]. In the exploratory phase, the focus is on quick iteration [00:11:11]. This phase requires individuals who are enthusiastic, knowledgeable about current AI techniques, and capable of operating with a clear problem-solving vision, breaking through technical and operational hurdles to build a working prototype [00:11:17]. Once a solution is more defined, it transitions to a more traditional product building process with user research and designers [00:11:41].

Notion's AI team consists of about a dozen people, split between focusing on data model quality (correctness and coherence of outputs) and product concerns (interface, integration) [00:12:05]. They also collaborate with designers [00:12:41].

### Organizational Structure
The organizational structure for AI teams is still evolving [00:13:10]. Notion currently operates with a core AI team that owns the backend and UI components for dedicated AI surfaces like AI Writer and Q&A [00:13:14]. However, for features like autofill, which are deeply integrated with existing products (like databases), ownership might reside with the respective product teams, necessitating tight collaboration with the core AI team [00:14:01].

The long-term vision is debated: whether to maintain a "hub" AI team that liaises with other teams, or to embed AI engineers within every product team [00:14:03]. Linus Lee believes that while engineers across teams will be empowered to use LLMs, a central team will still be beneficial for foundational tasks like monitoring, quality assurance, data set management, and training workflows [00:16:33].

## User Interaction and Adoption Challenges
Educating users and encouraging adoption of new AI features is crucial [00:17:03]. While internal dogfooding provides rich insights, Notion's internal usage isn't always representative of its diverse customer base (individuals, students, companies) [00:17:24].

Early testers and Notion ambassadors play a vital role, often discovering unanticipated use cases for features [00:17:57]. For example, the autofill feature, initially not designed for it, saw significant usage for translation, leading Notion to build translation as a pre-built prompt [00:18:25].

This pattern of "built-in" or "engineer-optimized" prompts alongside a customizable "custom prompt" field is a core Notion strategy [00:18:48]. Popular use cases like summarization, improving writing, and fixing grammar are offered as pre-baked options [00:19:32]. Users often start with these templates for inspiration and then iterate to fit their specific needs, with power users handwriting and reusing their own prompts [00:20:06]. This addresses the "blank canvas problem," guiding users and sparking creative application [00:20:45].

## Strategic Considerations
### Model Selection and Data Training
Notion partners with LLM providers like Anthropic and OpenAI, acknowledging the difficulty of competing at the infrastructure and initial model building level [00:31:17]. Notion's role is to understand its specific tasks, collect or generate synthetic data (without training on customer data due to privacy concerns), and build evaluations around those tasks [00:31:40]. They believe this approach helps them deeply understand how Notion workspaces are organized and what prototypical documents to serve AI for [00:32:23].

For different features, Notion may use different models based on capabilities, cost, and throughput needs [00:33:49]. For instance, a background batch process like autofill would prioritize a model with higher throughput [00:34:00].

### Pre-processing and Prompt Engineering
User prompts and queries are extensively pre-processed before being sent to the LLMs [00:34:50]. This can involve wrapping simple requests in complex prompt templates that include dialogue history or context [00:35:06]. For Q&A, a query rewrite phase rephrases user questions based on conversational context to improve search [00:35:37].

Linus Lee emphasizes that prompt engineering is downstream from clear evaluation criteria and a deep understanding of the task [00:37:02]. While specific model behaviors may require minor "per-model tweaks" (e.g., preventing a model from saying "in this document"), the core understanding of the problem and desired output format translates well across different models [00:37:27]. Large models generally transfer well across languages, though performance may fall off in non-English languages, requiring specific evaluation datasets and fine-tuning [00:38:37].

### Interface Design and Generalizability
Designing interfaces for AI features involves picking the right "building blocks" [00:40:04]. While direct prompting is always an option for power users, the team explores more structured abstractions [00:40:15]. This could mean models outputting entire UI components in the future, requiring a component library or UI language [00:41:19].

Notion's team bets on generalizability in AI approaches [00:47:59]. Instead of building specific models for each of Notion's five distinct AI tasks, they aim for a single, more general model trained on diverse datasets for all these tasks [00:47:00]. This approach is expected to lead to a model that better understands the overall product domain and allows for more interesting future capabilities, such as generative UIs [00:47:16].

### Overhyped vs. Underhyped AI Concepts
Linus Lee considers **context length** in LLMs to be overhyped [00:42:24]. He struggles to imagine truly useful tasks requiring extremely long contexts (e.g., 50,000 words), arguing that good information retrieval (RAG) is always the starting point [00:42:59]. He also highlights the [[challenges_in_ai_model_training_and_deployment | challenges in AI model training and deployment]] of generating sufficiently complex training data to utilize such long contexts [00:43:28].

Conversely, **alternatives to Transformers** are underhyped [00:44:36]. While Transformers are effective, nothing about their architecture is definitively "optimal," suggesting that more efficient sequence-modeling architectures could emerge in the future [00:44:51]. Linus notes that current models' power comes primarily from vast training data and their ability to absorb it, and new architectures could improve on this [00:45:22]. He mentions **state-space models** as a promising alternative [00:45:50].