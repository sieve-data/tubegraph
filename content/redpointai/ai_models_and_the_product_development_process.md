---
title: AI models and the product development process
videoId: A2uBXF8iPKY
---

From: [[redpointai]] <br/> 

Perplexity AI, a next-generation search product, has gained significant traction, raising a $500 million valuation in recent months <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. The company's CEO, Arvin Seros, shares insights into their product development philosophy, the role of [[developers_approach_to_ai_models_and_agents | AI models]], and strategies for navigating the competitive AI landscape.

## Core Product Development Philosophy

Perplexity AI's development is guided by five key dimensions to ensure a top-tier product:
*   **Accuracy** <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>
*   **Reliability** <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>
*   **Latency** <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>
*   **Delightful User Experience (UX)** <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>
*   **Iterative Improvement:** Constantly improving for everyone or through personalization <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>

Achieving excellence across all five dimensions simultaneously is crucial for creating a multi-billion dollar company <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.

## Complexity Behind the Seams

Despite the simplicity of its user interface, Perplexity AI involves significant underlying complexity <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>. When a user asks a query, the system undertakes a series of actions:
*   **Query Understanding and Reformulation:** The system tries to comprehend and rephrase the query <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.
*   **Source Selection:** Identifying which web pages are best to use for the query <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>.
*   **Content Extraction:** Determining which parts of the selected pages are relevant for answering <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>.
*   **Answer Rendering:** Deciding how the answer should be presented (e.g., summary, bullets) <a class="yt-timestamp" data-t="02:33:00">[02:33:00]</a>.
*   **Citation and Error Minimization:** Ensuring each sentence has supporting citations and minimizing hallucinations <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>.
*   **Multimedia Integration:** Incorporating images or videos when text alone is insufficient <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>.
*   **Shareability:** Making answers easily shareable via permalinks, an innovation later adopted by competitors <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>.
*   **Follow-up Questions:** Suggesting further questions to help users articulate their curiosity, as people are often not good at asking precise questions <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>. This led to the "co-pilot" feature, which assists users in prompt engineering <a class="yt-timestamp" data-t="04:25:00">[04:25:00]</a>.

## [[ai_model_pretraining_and_finetuning_decisions | AI Model Pretraining and Fine-tuning Decisions]] and [[ai_model_selection_and_evaluation_for_businesses | AI Model Selection]]

Perplexity AI's journey reflects a strategic evolution in [[developers_approach_to_ai_models_and_agents | AI model development]]:
*   **Starting with Off-the-Shelf Models:** Initially, the company leveraged models from OpenAI <a class="yt-timestamp" data-t="07:27:00">[07:27:00]</a>. The advice for product-focused companies is to begin with existing models to quickly launch a product, gain users, and secure funding and talent <a class="yt-timestamp" data-t="07:59:00">[07:59:00]</a>.
*   **Transition to Fine-tuning and Open Source:** Perplexity later fine-tuned smaller, faster models and increasingly utilized open-source models like LLaMA and Mistral <a class="yt-timestamp" data-t="07:34:00">[07:34:00]</a>. This shift was driven by a desire to reduce dependency on third parties, especially competitors, and to control costs <a class="yt-timestamp" data-t="10:30:00">[10:30:00]</a>. The company waited for the "open-source wave" to arrive, like LLaMA 2, to position themselves effectively <a class="yt-timestamp" data-t="10:49:00">[10:49:00]</a>.
*   **Building Internal Capabilities:** Over time, Perplexity has built its own inference engine and models fine-tuned on open-source foundations, aiming to rival models like GPT-3.5 Turbo <a class="yt-timestamp" data-t="24:21:00">[24:21:00]</a>. This move is to address user concerns about being a "rapper" (a company merely wrapping another's API) and to earn trust by demonstrating internal infrastructure capabilities <a class="yt-timestamp" data-t="24:40:00">[24:40:00]</a>.
*   **Model Agnosticism:** Despite building their own models, Perplexity aims to remain model agnostic, prioritizing giving users the best answer, regardless of the underlying model <a class="yt-timestamp" data-t="13:44:00">[13:44:00]</a>. Users care about the best answer, not the technology stack <a class="yt-timestamp" data-t="14:06:00">[14:06:00]</a>.

## [[product_development_and_prioritization_in_ai_startups | Product Development and Prioritization]]

### Organizational Structure
The company emphasizes vertical integration, ensuring designers, product engineers, and backend teams collaborate closely <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>. Regular meetings foster appreciation for all aspects of product development, aligning company values (quality, truth, velocity) with product goals <a class="yt-timestamp" data-t="07:05:00">[07:05:00]</a>.

### Balancing User Types
A key challenge is balancing the needs of power users with those of new users <a class="yt-timestamp" data-t="35:05:00">[35:05:00]</a>. While power users provide valuable feedback, focusing solely on their requests can make the product unintuitive for new users and hinder growth <a class="yt-timestamp" data-t="35:45:00">[35:45:00]</a>. The goal is to find a sweet spot that caters to a broad audience <a class="yt-timestamp" data-t="36:24:00">[36:24:00]</a>.

### Overcoming Hallucinations with RAG
Perplexity has been effective at using Retrieval Augmented Generation (RAG) to solve hallucinations in web search <a class="yt-timestamp" data-t="27:45:00">[27:45:00]</a>. However, the CEO warns against universal solutions, noting that solving RAG for internal enterprise search is vastly different from web search due to unique indexing, embeddings, and ranking requirements <a class="yt-timestamp" data-t="28:18:00">[28:18:00]</a>. The quality of retrieval is critical, as simply dumping information into a large language model can increase hallucinations <a class="yt-timestamp" data-t="30:07:00">[30:07:00]</a>.

## Evolution of the Product and Go-to-Market Strategy

Perplexity AI's success stemmed from iterating on different ideas before finding product-market fit:
*   **Initial Ideas:** Early concepts included a vision-based search (glasses with microphone/airpods) and search over databases (text-to-SQL for enterprise spreadsheets) <a class="yt-timestamp" data-t="38:58:00">[38:58:00]</a>. The text-to-SQL idea faced challenges as most SQL is recurring, and new queries are often generated visually rather than typed <a class="yt-timestamp" data-t="40:46:00">[40:46:00]</a>.
*   **Twitter Search:** The team built a graph search over Twitter data, allowing users to find connections or specific tweets <a class="yt-timestamp" data-t="42:46:00">[42:46:00]</a>. This led to a viral moment when Jack Dorsey tweeted about it, bringing tens of thousands of users to the site and causing a crash <a class="yt-timestamp" data-t="46:51:00">[46:51:00]</a>. The system's ability to summarize social media activity across platforms for a given handle "spooked people out," leading to viral screenshots and further adoption <a class="yt-timestamp" data-t="48:01:00">[48:01:00]</a>.
*   **Consumer-Facing Search:** The summarization-based search, initially a Slack bot for internal use, was chosen for public launch because it resonated with early users who found it "better than Google" for quick, cited answers to complex questions <a class="yt-timestamp" data-t="44:56:00">[44:56:00]</a>. The viral usage during the winter vacation period confirmed the product's real demand <a class="yt-timestamp" data-t="48:48:00">[48:48:00]</a>.

> [!NOTE] The "User is Never Wrong" Philosophy
> Larry Page's early Google demos showed him insisting that the user was never wrong for not typing a query "the right way" <a class="yt-timestamp" data-t="05:20:00">[05:20:00]</a>. This philosophy guides Perplexity AI's development, leading to features like Co-pilot that assist users in formulating queries <a class="yt-timestamp" data-t="04:25:00">[04:25:00]</a>.

## The Future of Search and AI

The future of search, according to Perplexity AI's CEO, will be primarily about "answers" delivered by [[developers_approach_to_ai_models_and_agents | agents]] that perform tasks <a class="yt-timestamp" data-t="22:23:00">[22:23:00]</a>. It will resemble natural conversation with friends, concise enough to be useful without rambling <a class="yt-timestamp" data-t="23:31:00">[23:31:00]</a>.

The company's focus is on maximizing "knowledge velocity" – accelerating the transfer of knowledge <a class="yt-timestamp" data-t="15:36:00">[15:36:00]</a>. Unlike static Wikipedia articles or slow Quora answers, Perplexity aims to provide fast, personalized, sourced answers, essentially automating the research process that would take humans hours <a class="yt-timestamp" data-t="16:51:00">[16:51:00]</a>.

## [[challenges_in_ai_product_development | Challenges in AI Product Development]]

### Competition and Differentiation
Competing with incumbents like Google requires a different approach than replicating their technology <a class="yt-timestamp" data-t="20:17:00">[20:17:00]</a>. Previous Google challengers focused too much on technology and not enough on market positioning or unique go-to-market strategies (e.g., privacy for DuckDuckGo, crypto for Brave) <a class="yt-timestamp" data-t="21:17:00">[21:17:00]</a>. The emergence of powerful, accessible LLMs was a rare "failure" for Google, creating an opportunity for companies like Perplexity to leverage the technology <a class="yt-timestamp" data-t="22:46:00">[22:46:00]</a>.

### Talent Acquisition
Recruiting skilled engineers and [[ai_production_and_evaluation_techniques | AI researchers]] is more challenging than raising capital in the current generative AI landscape, as top talent is scarce and crucial for destiny-changing impact <a class="yt-timestamp" data-t="09:14:00">[09:14:00]</a>.

### Regulation
Regulation of AI is currently premature, as the widespread economic benefits are not yet fully realized <a class="yt-timestamp" data-t="33:30:00">[33:30:00]</a>. Over-regulation could stifle innovation and centralize AI development among a few well-funded entities <a class="yt-timestamp" data-t="54:47:00">[54:47:00]</a>. Transparency and broad participation are preferred to ensure safety and prevent control by a select few <a class="yt-timestamp" data-t="55:03:00">[55:05:00]</a>.

## Personal Vision for AI's Future

The CEO expresses a personal desire to use [[ai_models_and_educational_engagement | AI models]] to preserve memories of loved ones, such as recording parents extensively to create AI voices or personas for future interaction <a class="yt-timestamp" data-t="56:03:00">[56:03:00]</a>. This reflects a broader belief in AI's potential to democratize creative processes, like movie-making, by significantly reducing creation costs <a class="yt-timestamp" data-t="56:55:00">[56:55:00]</a>.