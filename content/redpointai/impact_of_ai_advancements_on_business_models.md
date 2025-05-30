---
title: Impact of AI advancements on business models
videoId: og57f_tv3zY
---

From: [[redpointai]] <br/> 

Notion, a prominent productivity and project management tool, has rapidly integrated [[developing_and_utilizing_ai_models_in_the_tech_industry | AI features]] into its product, providing a compelling case study on the [[enterprise_ai_adoption_and_deployment_models | adoption of AI]] within an existing business model. Their approach highlights rapid iteration, strategic partnerships, and a deep understanding of user needs.

## Notion's AI Product Journey

Notion's journey into AI began around late 2022, spurred by their CEO and co-founder's exploration of GPT-3's capabilities as a writing tool [03:02:05]. This led to a hackathon-style development of their initial [[developing_and_utilizing_ai_models_in_the_tech_industry | AI features]] [03:17:00].

### Key AI Product Releases:

*   **Notion AI Writer** (Beta: November 2022, Launch: February 2023) <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>
    *   **Functionality:** [[impact_of_ai_on_the_music_industry | AI]] integrated directly into documents to summarize pages, extract key ideas, identify action items, correct spelling and grammar, and improve writing style or voice [03:48:00]. It also assists in drafting basic marketing copy [04:09:00].
    *   **User Interaction:** Users often leverage the AI to generate a first draft or iterate on existing content [04:22:00]. A key addition was the ability to conversationally refine outputs (e.g., "make it shorter," "make it more Punchy") [04:30:00].

*   **AI Autofill** (Launch: May 2023) <a class="yt-timestamp" data-t="04:39:00">[04:39:00]</a>
    *   **Functionality:** Extends AI to Notion databases, allowing users to automatically populate entire columns or properties [04:57:00]. Examples include extracting key topics from meeting notes or core needs from customer interview transcripts [05:04:00].
    *   **Integration:** This feature is more deeply integrated with Notion's existing database functionalities, necessitating collaboration with the core database team [13:40:00].

*   **Notion Q&A** (Recently Launched) <a class="yt-timestamp" data-t="05:23:00">[05:23:00]</a>
    *   **Functionality:** A significant advancement, allowing Notion AI to understand and answer questions based on the entire user's workspace, spanning multiple pages [05:35:00]. This feature acts as an intelligent search replacement or augmentation [05:45:00].
    *   **Problem Solved:** Addresses the challenge organizations face in finding information as their Notion workspaces grow in complexity and size [06:05:00].
    *   **Technical Foundation:** Inspired by the Retrieval-Augmented Generation (RAG) trend in the broader [[challenges_and_advancements_in_ai_technology | AI community]], grounding [[advancements_and_implications_of_ai_agents | AI]] in factual, internal information [06:36:00].

## Product Development & Team Structure

Notion's AI team operates with an iterative "expand out and then contract" cycle, balancing user problem-solving with exploration of new [[challenges_and_advancements_in_ai_technology | AI capabilities]] [07:27:00].

### Team Organization:

*   **Core AI Team:** Consists of approximately a dozen individuals, divided evenly between:
    *   **Data Model/Quality:** Focuses on the correctness and coherence of model outputs [12:09:00].
    *   **Product Concerns:** Handles user interface and integration into the Notion product [12:20:00].
*   **Designers:** A couple of designers work closely with the team from the ideation phase, focusing on presenting model outputs in a user-friendly manner [12:41:00].
*   **Dogfooding:** Notion heavily tests its [[developing_and_utilizing_ai_models_in_the_tech_industry | AI features]] internally, with prototypes designed to be "annoying" to ensure rapid iteration and quality improvement [10:02:00]. This internal usage also helps validate usefulness by observing engagement and feedback [10:52:00].

### Development Phases:

*   **Exploratory Phase:** Characterized by rapid iteration and a team enthusiastic about the technology, able to operate with a clear vision to overcome technical and operational challenges to build working prototypes [11:11:00].
*   **Defined Solution Phase:** Once a clear direction is set, the process resembles traditional product building, involving user research and structured design collaboration to achieve confidence in UX and model output quality [11:41:00].

### Future Organizational Models:

Notion is still evaluating the optimal structure for [[developing_and_utilizing_ai_models_in_the_tech_industry | AI development]] within a larger company. Potential models include:
*   A central "hub" AI team that liaises with other product teams [14:05:00].
*   [[advancements_and_implications_of_ai_agents | AI]] engineers embedded within every product team [14:14:00].
The current setup, with a core AI team owning both backend and UI components for specific AI surfaces, makes sense where dedicated AI features exist [13:14:00].

## User Interaction and Education

Notion's internal "dogfooding" provides rich insights but isn't fully representative of their diverse user base (individuals, students, startups) [17:12:00]. They also engage with early testers and Notion ambassadors to uncover unanticipated use cases [17:55:00].

### Learning from Users:

*   **Unanticipated Use Cases:** Users, especially early testers, often find novel applications for the [[advancements_and_implications_of_ai_agents | AI]]. For example, translation emerged as a popular use case for Autofill, leading to it becoming a built-in prompt [18:30:00].
*   **Pre-built Prompts vs. Customization:** Notion observes a "power law" distribution in usage:
    *   **Pre-built prompts** (e.g., summarization, grammar correction, translation) are most popular for common tasks [19:32:00].
    *   **Custom prompts** and iteration on model outputs account for a significant portion of usage, especially among power users who craft and reuse specific prompts for their workflows (e.g., generating social media tags for newsletters) [19:50:00].
*   **Overcoming Blank Canvas Problem:** Pre-built prompts help users overcome the initial "blank canvas" problem by demonstrating possibilities and inspiring creative use [20:45:00]. Notion considers suggesting revisions based on generated content to further guide users [22:12:00].

## Technical and Operational Challenges

### Evaluation and Quality Control:

*   **Complexity of Evaluation:** Evaluating language models, especially for precise tasks like Q&A where correctness is paramount, is challenging [23:14:00]. Unlike creative writing, Q&A has less "wiggle room" for error [23:28:00].
*   **Edge Cases:** Anticipating all types of user questions, especially "meta" questions about Notion (e.g., "How can I share this page with Jack?") or time-sensitive queries (e.g., "What is the marketing team working on this week?") that aren't easily answered by static documents, is difficult [24:16:00].
*   **Evaluation Methods:** Notion employs a spectrum of evaluation methods:
    *   **Deterministic/Programmatic:** Automated checks and model-graded outputs [27:58:00].
    *   **Human Annotators:** A team of human annotators speeds up processes [28:38:00].
    *   **ML Engineer Review:** Engineers manually review model outputs to understand failure modes (e.g., did the model understand instructions? struggles with relative dates?) [28:44:00]. This costly but high-yield approach helps identify where to intervene in the pipeline (e.g., embedding problems vs. answering problems) [29:11:00].
*   **In-house Tools:** The majority of Notion's [[developing_and_utilizing_ai_models_in the_tech_industry | AI development tools]] are built in-house [26:21:00]. This is due to the lack of suitable external tools when they started and the complex, structured nature of Notion documents (rich text, tables, images, metadata) [26:40:00]. Custom tools allow for faster iteration [27:22:00].

### Model Selection and Data Management:

*   **Partnerships over In-house Training:** Notion partners with leading [[developing_and_utilizing_ai_models_in_the_tech_industry | AI companies]] like Anthropic and OpenAI for core model infrastructure and hosting [31:08:00]. They deem it "exceedingly difficult" to compete at this level [31:22:00].
*   **Notion's Role:** Their focus is on understanding specific task profiles, building synthetic datasets (without training on customer data due to privacy commitments), and developing robust evaluation methods [31:40:00]. Understanding what constitutes a "good" summary, for instance, varies greatly depending on the document type [32:47:00].
*   **Open-source Models:** While exploring open-source models (e.g., for embedding), Notion has not yet shipped any production features using them [33:16:00].
*   **Multiple Models:** The choice of model depends on various factors, including performance, cost, and throughput requirements (e.g., a batch-running autofill feature needs higher throughput) [33:49:00]. This often leads to using different model scales or providers for different features [34:25:00].

### Prompt Engineering:

*   **Pre-processing and Prompt Wrapping:** User prompts are always wrapped in Notion's own processing, which can include adding dialogue history for multi-turn conversations (e.g., query rewriting for Q&A) [34:50:00].
*   **Post-processing:** Notion models have shown good performance in avoiding objectionable content and have made strides in reducing hallucination, though it remains an ongoing effort [36:11:00].
*   **Model Agnosticism:** While minor, model-specific prompt tweaks (e.g., avoiding a particular phrase like "in this document") might be necessary, the core bulk of instructions related to task understanding, evaluation criteria, and desired output format generally carries over between models as they improve at following instructions [37:02:00].
*   **Multilingual Performance:** Large models generally transfer well across languages, though performance might be better in English [38:37:00]. Notion uses specific evaluation datasets for multilingual performance and adds few-shot examples or training to bolster it [39:06:00]. A notable capability is Q&A's ability to read documents in one language (e.g., Japanese) and translate the answer back to the user's query language (e.g., English) without an intermediate translation layer [39:21:00].

## Future Vision and Broader [[influence_of_ai_on_economics_and_societal_transformation | AI Trends]]

Notion sees [[advancements and implications of AI agents | AI]] as an ongoing journey of exploration, particularly regarding the "building blocks" of AI within their product [40:40:00].

### Overhyped vs. Underhyped [[influence_of_ai_on_economics_and_societal_transformation | AI Trends]]:

*   **Overhyped:** **Context length** in large language models. While useful for specific cases, many real-world tasks don't require extremely long contexts (e.g., 50,000 words), and noise in the data still hinders performance [42:24:00]. Retrieval-Augmented Generation (RAG) remains crucial for getting good information into the context [42:53:00].
*   **Underhyped:** **Alternatives to Transformers**. While Transformers are excellent, the architecture isn't necessarily "most optimal," and other efficient sequence modeling architectures are likely to emerge [44:36:00]. State-space models are noted as particularly interesting [45:50:00].

### Surprises and Bets:

*   **Generality of Approaches:** Linus Lee, who heads much of Notion's AI efforts, has been surprised by how well general approaches work [46:14:00]. Building a single model capable of handling multiple tasks (e.g., answering questions, writing, onboarding assistance) by training it on diverse datasets can lead to a model that better understands the product's domain [46:56:00].
*   **Generative UI:** Betting on [[advancements_and_implications_of_ai_agents | models]] that can output entire pieces of UI (generative interfaces) rather than just text, giving the [[advancements_and_implications_of_ai_agents | AI]] more control over what appears on screen [47:19:00]. This is a harder ML problem but is expected to yield more interesting results long-term given the rapid pace of model improvement [47:50:00].

### [[economic_and_strategic_considerations_in_ai_model_deployment | Economic Impact]] of [[influence_of_ai_on_economics_and_societal_transformation | AI Advancements]]:

*   **Cost Reduction:** The rapid decrease in [[economic_and_strategic_considerations_in_ai_model_deployment | inference costs]] (e.g., OpenAI slashing prices by 3x for Turbo) has a dramatic positive impact on businesses leveraging [[developing_and_utilizing_ai_models_in_the_tech_industry | AI features]], potentially turning previously cost-prohibitive features into viable ones [58:41:00]. This fosters innovation within the startup ecosystem [59:00:00].
*   **Ecosystem Development:** Large foundation model providers (like OpenAI) offer a broad array of tools, creating an environment akin to AWS, where startups can still compete and win in specific verticals by offering specialized products [01:00:51:00]. Notion AI and GitHub Copilot are cited as prime examples of successful [[enterprise_ai_adoption_and_deployment_models | enterprise AI applications]] [01:00:00:00].