---
title: Notion AI team structure and development process
videoId: og57f_tv3zY
---

From: [[redpointai]] <br/> 

Notion's AI team, headed by Linus Lee, operates with a dynamic and iterative development process, emphasizing rapid prototyping and internal "dogfooding" to integrate AI features deeply into the product [00:07:22].

## Team Structure
Linus Lee joined Notion's AI team in January 2023 [00:03:36]. The core AI team comprises about a dozen individuals [00:12:05]. This team is roughly evenly split between:
*   **Data and Model Quality**: Focusing on the correctness, coherence, and overall quality of model outputs [00:12:09].
*   **Product Concerns**: Handling the user interface (UI) and integration of AI features into the broader Notion product [00:12:20].

The AI team also collaborates closely with designers [00:12:41]. For features that are deeply integrated into existing Notion products, such as [[features_and_enhancements_in_notion_ai | AI autofill]] with Notion databases, the ownership of the feature resides with the relevant product team (e.g., the databases team) [00:13:40]. However, there is still tight collaboration with the core AI team, especially for complex [[challenges_in_ai_product_development | AI problems]] [00:13:54].

The company is still exploring how to best organize its AI capabilities in the long term, considering options like a central "hub" AI team that liaises with other product teams or embedding AI engineers directly within every product team [00:14:10]. The development of foundational [[ai_models_and_the_product_development_process | AI technologies]] like retrieval is seen as crucial, as it can augment many capabilities beyond just question answering [00:14:40].

## Product Development Process
Notion's [[product_development_and_prioritization_in_ai_startups | product development]] for AI features follows an "expand out and then contract" cycle [00:07:30].

### Ideation and Exploratory Phase
The initial spark for Notion AI came around a company offsite almost exactly a year ago, where co-founders Ivan and Simon began experimenting with GPT-3 [00:02:40]. They "hacked" on it in a hotel room, leading to the first version, Notion AI writer [00:03:17].

This phase starts with broad problem statements, such as helping users organize or find information [00:07:37]. Different ideas and [[ai_models_and_the_product_development_process | technologies]] like Retrieval Augmented Generation (RAG) are explored [00:07:48]. A few team members rapidly prototype solutions [00:07:55]. A key aspect of this phase is extensive internal "dogfooding," where Notion employees use the nascent features heavily [00:08:05]. This internal usage quickly highlights which approaches are most promising [00:08:12].

For the [[features_and_enhancements_in_notion_ai | Notion Q&A]] feature, an "annoying" internal prototype was intentionally deployed [00:10:02]. This forced the team to iterate quickly to improve output quality because everyone was constantly exposed to its results [00:10:32]. It also provided immediate feedback on whether the feature was useful or not, based on internal adoption and direct feedback [00:10:57]. This phase requires individuals who are enthusiastic about the technology, knowledgeable about current techniques, and capable of overcoming technical and operational hurdles to build a functional prototype [00:11:14].

### Solution Definition and Shipping Phase
Once a clear direction emerges from the exploratory phase, the process shifts to a more traditional [[product_development_and_prioritization_in_ai_startups | product building]] approach, involving user research, design, and iterative refinement of both the user experience (UX) and model output quality [00:11:41].

### Resource Allocation
The resources allocated to shipping an AI product vary [00:09:54]. In the exploratory phase, the focus is on rapid iteration, meaning a small, agile group of engineers enthusiastic about the technology can be highly effective [00:11:11]. As a solution becomes more defined, it requires a cross-functional team, including user researchers and designers, similar to typical software feature development [00:11:45].

## Evaluation and Model Strategy
Evaluation of language model outputs, especially for features requiring high correctness like Notion Q&A, is one of the most challenging aspects [00:23:07]. Unlike creative writing where there's "wiggle room," Q&A demands specific and accurate answers, making errors more critical [00:23:50].

Notion uses a spectrum of evaluation methods:
*   **Deterministic Programmatic Evaluations**: Automated checks of model outputs [00:28:01].
*   **Model-Graded Outputs**: Using other models to assess output quality [00:28:03].
*   **Human Annotators**: A team of human evaluators speeds up some assessment processes [00:28:38].
*   **ML Engineers Manual Review**: Engineers personally examine model outputs to diagnose *why* models fail, identifying patterns like misinterpreting instructions, struggling with relative dates, or failing to retrieve the correct information [00:28:46]. This costly but valuable approach helps pinpoint where to intervene in the pipeline [00:29:11].

Notion iterates on the full stack of its AI pipeline, from data representation to model prompting and post-processing [00:29:31]. This includes experimenting with adding intermediate stages, such as rephrasing retrieved passages before generating a final answer [00:29:51].

Notion maintains strong partnerships with major AI model providers like Anthropic and OpenAI [00:31:08]. They primarily focus on understanding the specific tasks their models need to perform, collecting or generating synthetic data, and building evaluations around those tasks [00:31:40]. They are committed to not training their models on customer data, which drives a systematic understanding of how Notion workspaces are structured and what kinds of documents are prototypical [00:31:57]. While they have explored open-source models, they have not yet shipped anything to production using them [00:33:16].

The choice of which model to use (from different providers or of different scales) depends on various factors:
*   **Performance**: The model must meet expectations [00:33:53].
*   **Throughput**: Some features, like [[features_and_enhancements_in_notion_ai | AI autofill]] which runs in the background, require models that support higher throughput [00:33:59].
*   **Cost**: Balancing capabilities with the cost of inference [00:34:18].

## [[User interaction with Notion AI | User Interaction]] and Interface Design
Internal usage by Notion employees is the richest source of information for determining the most useful ways to apply AI [00:17:14]. However, Notion's internal usage patterns are not entirely representative of all customers, who range from individuals and students to large organizations using the product in diverse ways [00:17:24].

Notion also works with early testers and ambassadors who often discover unanticipated use cases for features, sometimes inspiring new ones (e.g., translation becoming a built-in option for [[features_and_enhancements_in_notion_ai | autofill]]) [00:18:00]. This iterative process allows Notion to observe how users customize features, then formalize common patterns into "pre-baked" templates or prompts [00:19:10].

Key observations about [[user_interaction_with_notion_ai | user behavior]]:
*   **Pre-built prompts are popular**: Most users prefer pre-built prompts for common tasks like summarization, improving writing, fixing grammar, and translation [00:19:32].
*   **Iteration is common**: A significant portion of usage involves users iterating on initial model outputs, often by following up with conversational refinements [00:19:50].
*   **Power users create custom prompts**: Experienced users often hand-write and reuse specific prompts tailored to their unique workflows [00:20:18].
*   **Addressing the "blank canvas" problem**: Pre-built prompts and suggested actions help users overcome the initial difficulty of knowing what to ask the AI [00:20:45].

For every Notion AI feature, user prompts are wrapped in a layer of internal processing [00:34:54]. This might involve prompt templating that includes conversation history and user revisions, or, for [[features_and_enhancements_in_notion_ai | Q&A]], a query rewrite phase that leverages conversational context to improve search queries [00:35:10]. For example, if a user asks "what's David working on this week" and then "tell me more about that automation project," the AI understands the context and searches for "David automation project" [00:35:26].

Linus Lee emphasizes designing the right "building blocks" for AI, similar to Notion's existing block abstraction for content [00:40:02]. While users can always prompt the AI directly, the goal is to provide abstractions that align with the intended AI output. For writing, custom prompts work well, but for generative interfaces that output UI elements or models that perform actions, a structured "component library" or "domain-specific language" is necessary [00:41:19].

## [[Challenges in deploying AI in Notion | Challenges and Learnings]]
*   **Evaluation Difficulty**: Ensuring correctness and quality for specific answers, like in Q&A, is extremely challenging, as models can fail in many ways (e.g., hallucinating, not looking at the right document) [00:23:20].
*   **Anticipating Edge Cases**: It's difficult to predict all types of user questions, especially "meta" questions about Notion itself (e.g., "how can I share this page with Jack?") or questions involving temporal information (e.g., "what is the marketing team working on this week?"), which diverge from traditional RAG pipelines [00:24:16].
*   **Operational Concerns**: Addressing customer needs around privacy, security, and scalability for a new, rapidly evolving technology like large language model augmented question answering without clear industry answers [00:25:33].
*   **Building Internal Tools**: Due to the complexity of Notion documents (rich text, tables, metadata) and the nascent state of external tools, Notion built most of its language model-powered tools in-house, enabling faster iteration [00:26:21].
*   **Prompt Portability**: While task understanding and evaluation criteria carry over between different models, specific "tweaks" or fine-tuning of prompts to address a particular model's quirks (e.g., a model overusing "in this document") may be necessary when switching providers [00:37:02].
*   **Multilingual Performance**: Large models generally transfer well across languages, though English performance tends to be superior [00:38:37]. Notion prototypes in English, then uses specific evaluation datasets for multilingual performance, sometimes adding few-shot examples or training to bolster other languages [00:39:08]. A cool feature for [[features_and_enhancements_in_notion_ai | Q&A]] is its ability to read documents in one language (e.g., Japanese) and translate the answer back to the user's query language [00:39:21].
*   **Generality of Approach**: Notion has been surprised by how well general AI approaches work [00:46:14]. Betting on generality — building a single model that can handle multiple tasks (e.g., question answering, writing, onboarding) — can lead to a model that better understands the product's domain [00:47:00]. This includes exploring generative UI, where AI directly outputs interactive elements, giving the AI more control over the interface [00:47:24].
*   **Context Length**: Linus Lee believes context length is "overhyped" [00:42:24]. He struggles to imagine truly useful tasks requiring extremely long contexts (e.g., 50,000 words), suggesting that much of it resembles retrieval [00:42:28]. He believes that good information retrieval into a smaller context window is more crucial than ever-expanding context [00:43:01].
*   **Alternative Architectures**: Alternatives to Transformers are "underhyped" [00:44:36]. While Transformers are excellent for long sequences and efficiency, they are not architecturally optimal [00:44:51]. Linus Lee expects new architectures that are also good at modeling sequences and efficient to emerge in the coming years, citing state-space models as an interesting area [00:44:58].

## Industry Comparison
Notion's approach to AI development is distinct. While they leverage powerful large language models from partners, they focus on the specific tasks within their domain and building tools to evaluate and improve performance [00:31:31]. This contrasts with companies that build foundational models themselves. Notion AI is seen as a leading example of an [[advancements_in_ai_developer_tools | enterprise AI]] use case, similar to [[ai_in_software_development_with_github_copilot | GitHub Copilot]] [00:56:30].

The rapid reduction in model costs (e.g., OpenAI slashing prices) is a significant factor, making previously cost-prohibitive features viable [00:58:09]. This constant evolution of the underlying models means companies like Notion can rely on providers for the base model, while focusing on application-specific innovation [00:56:06].