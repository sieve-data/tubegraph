---
title: Comparisons and partnerships with AI model providers
videoId: og57f_tv3zY
---

From: [[redpointai]] <br/> 

Notion, a company known for quickly shipping AI features into its product, has extensively leveraged partnerships with leading AI model providers like OpenAI and Anthropic. This approach is central to how Notion develops and integrates artificial intelligence into its platform <a class="yt-timestamp" data-t="00:24:01">[00:24:01]</a>.

## Strategy for AI Model Development

Notion's strategy for AI model development is primarily focused on understanding and defining the specific tasks their models need to perform, and then partnering with external providers for the foundational model infrastructure <a class="yt-timestamp" data-t="00:31:42">[00:31:42]</a>.

### Core Focus: Task Understanding and Data Generation
Notion's team concentrates on:
*   **Understanding tasks:** Defining what makes a "good summary" can vary significantly between a meeting note, a long technical document, or a bug report <a class="yt-timestamp" data-t="00:32:45">[00:32:45]</a>.
*   **Data collection and generation:** This involves generating synthetic data for models and building data sets for evaluating specific tasks, particularly given the commitment not to train on customer data <a class="yt-timestamp" data-t="00:31:46">[00:31:46]</a>. This approach helps them understand how Notion workspaces are organized and what kinds of documents are prototypical for AI service <a class="yt-timestamp" data-t="00:32:23">[00:32:23]</a>.

### Partnering for Infrastructure
Notion recognizes the difficulty of [[competing_with_tech_giants_in_the_ai_market | competing]] at the infrastructure level with companies like OpenAI, Anthropic, or Google <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>.
*   **Division of Labor:** Partners are responsible for building effective models that follow instructions and hosting them scalably and reliably <a class="yt-timestamp" data-t="00:31:31">[00:31:31]</a>.
*   **Beneficial for Ecosystem:** The continuous reduction in model costs by large foundation model companies like OpenAI is seen as beneficial for the startup ecosystem, allowing companies like Notion to build on top of their services without significant [[challenges_and_opportunities_in_ai_model_development_and_infrastructure | infrastructure investment]] <a class="yt-timestamp" data-t="00:56:06">[00:56:06]</a>.

## Proprietary vs. Third-Party AI Models

Notion's approach involves a clear preference for leveraging external, state-of-the-art models from their partners rather than building their own foundation models from scratch <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>.

### Benefits of Partnerships
*   **Access to State-of-the-Art:** Notion has strong partnerships with Anthropic and OpenAI, benefiting from their expertise in infrastructure and initial model building <a class="yt-timestamp" data-t="00:31:08">[00:31:08]</a>.
*   **Scalability and Reliability:** Partners manage the complex task of hosting models in a reliable and scalable manner <a class="yt-timestamp" data-t="00:31:35">[00:31:35]</a>.
*   **Focus on Application Layer:** This allows Notion to focus on understanding specific tasks, [[evaluation_methodologies_and_user_feedback_for_ai_models | evaluating model performance]], and designing user experiences <a class="yt-timestamp" data-t="00:33:04">[00:33:04]</a>.

### Considerations for Model Selection
The best model for a particular feature depends on several factors:
*   **Performance:** The model must meet performance expectations <a class="yt-timestamp" data-t="00:33:53">[00:33:53]</a>.
*   **Throughput:** Some features, like AI autofill which runs in the background when a page changes, require models that support higher throughput <a class="yt-timestamp" data-t="00:33:59">[00:33:59]</a>.
*   **Cost:** Notion evaluates the cost of different models to find the most suitable option <a class="yt-timestamp" data-t="00:34:18">[00:34:18]</a>. This often means using different model scales or even different providers for different features <a class="yt-timestamp" data-t="00:34:25">[00:34:25]</a>.

### [[open_source_models_versus_proprietary_ai_models | Open Source Models Versus Proprietary AI Models]]
While Notion is exploring open-source models, especially for embedding tasks, they have not yet shipped any production features using them <a class="yt-timestamp" data-t="00:33:10">[00:33:10]</a>. Their current approach primarily relies on proprietary models from their partners.

## Managing Model Interactions and Outputs

Notion employs extensive pre-processing and in-house tools to manage how their products interact with and evaluate the outputs from third-party AI models.

### Prompt Engineering and Pre-processing
*   User prompts are often wrapped in Notion's own processing, which may include prompt templates that incorporate dialogue history or context from the page <a class="yt-timestamp" data-t="00:34:54">[00:34:54]</a>.
*   For features like Q&A, a query rewrite phase might occur where the model rephrases the query based on conversation context before searching <a class="yt-timestamp" data-t="00:35:37">[00:35:37]</a>.
*   [[challenges_and_progress_in_ai_model_alignment_research | Prompt engineering]] involves understanding specific task criteria (e.g., what makes a good summary) and then instructing the model to meet those criteria, including format requirements and what to avoid <a class="yt-timestamp" data-t="00:37:27">[00:37:27]</a>. These core instructions tend to carry over between different models <a class="yt-timestamp" data-t="00:38:29">[00:38:29]</a>.

### Evaluation Methodologies
Notion has built most of its evaluation tools in-house <a class="yt-timestamp" data-t="00:26:28">[00:26:28]</a>. This is due to the lack of suitable off-the-shelf tools when they started and the complexity of Notion's rich, structured documents <a class="yt-timestamp" data-t="00:26:31">[00:26:31]</a>.
*   **Spectrum of Evaluation:**
    *   **Programmatic/Deterministic:** Automated checks of model outputs <a class="yt-timestamp" data-t="00:27:58">[00:27:58]</a>.
    *   **Human Annotators:** A team of human annotators helps to speed up processes <a class="yt-timestamp" data-t="00:28:38">[00:28:38]</a>.
    *   **ML Engineer Review:** ML engineers manually review model outputs to understand why failures occur (e.g., model misunderstanding instructions, difficulty with relative dates) <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>. This deep dive into errors is crucial for identifying where to intervene in the pipeline (e.g., embedding problem vs. answering problem) <a class="yt-timestamp" data-t="00:30:37">[00:30:37]</a>.

### Multilingual Performance
Large models generally transfer well across languages, though performance might excel in English and fall off in other languages <a class="yt-timestamp" data-t="00:38:36">[00:38:36]</a>. Notion prototypes with English and then uses specific evaluation datasets for multilingual performance, sometimes adding few-shot examples or training to bolster performance <a class="yt-timestamp" data-t="00:39:06">[00:39:06]</a>.
*   **Example:** Notion Q&A can read documents in Japanese and translate the answer back to the user without an intermediate translation layer <a class="yt-timestamp" data-t="00:39:21">[00:39:21]</a>.

## Conclusion
Notion's approach to AI development highlights the significance of strategic [[role_of_opensource_models_and_partnerships_in_ai_advancement | partnerships]] with foundational model providers. By outsourcing the complex, resource-intensive task of model building and hosting, Notion can focus its internal efforts on understanding specific user needs, refining interaction patterns, and building robust evaluation frameworks. This allows them to iterate quickly and adapt to the evolving landscape of AI capabilities, delivering tailored and high-quality AI features to their users.