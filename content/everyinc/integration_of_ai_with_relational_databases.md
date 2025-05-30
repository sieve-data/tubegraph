---
title: Integration of AI with relational databases
videoId: E5EgUuzzH5I
---

From: [[everyinc]] <br/> 

The integration of artificial intelligence (AI) with relational databases is a transformative approach to managing and interacting with information. This concept envisions a future where AI handles much of the data management, reducing direct human interaction with databases and automating cumbersome tasks <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Core Principles of AI Integration

When considering how to rebuild a system like Notion with AI, a key principle is minimizing human interaction with the database <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Ideally, AI should manage the database, automating updates to fields based on contextual information, such as emails <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This shifts the database from being a primary user interface to more of an "implementation detail," with users interacting more directly with processed outputs and insights rather than raw data <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.

### New Primitives for AI Interaction

The emergence of AI introduces new "primitives" for thinking and interacting with data:
*   **Foundation Models (Thinking Boxes):** These models act as "thinking boxes" that can take context and a task, then perform reasoning and formatting to achieve a specific outcome <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. They enable the automation of knowledge work tasks that were previously too cumbersome or expensive for humans to perform <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.
*   **Embeddings:** These provide "really good semantic search," allowing for the capture of many dimensions of information, which is particularly useful for storing data without a predefined future use <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

While these new primitives are crucial, traditional primitives like relational databases remain fundamental for tracking structured information <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. The goal is to plug these "thinking boxes" on top of existing database structures to automate tasks and fluidly transform information <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

### Designing Schemas with AI

For relational databases, designing a schema is most effective when the data's intended use is known <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. AI can assist in schema design, though it's more successful when focused on minimal schemas required for current tasks, ensuring each property serves a clear purpose <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

## Database Management and Interaction

### Combining Deterministic and Stochastic Approaches
Integrating AI means having both deterministic querying (like SQL) and embeddings as tools <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>. The choice between them depends on the specific question:
*   **Deterministic Queries:** Ideal for precise, factual questions (e.g., "how many sales did we do last quarter?"), where accuracy is paramount <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.
*   **Embeddings:** More flexible for semantic searches (e.g., "do we have any customers in the entertainment space?"), where exact matching isn't the primary goal <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

The challenge lies in defining a routing layer that determines the best tool for a given job and combines them to present the user with the most relevant result <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>. While long contexts for models and improved attention are desired, currently, limiting context and removing irrelevant information still yields better results in RAG (Retrieval Augmented Generation) scenarios <a class="yt-timestamp" data-t="00:34:39">[00:34:39]</a>.

### Automating Data Entry and Documentation
A significant benefit of AI integration is the potential to automate data entry and keep information up-to-date <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>. In companies, a vast amount of information often remains unwritten or quickly becomes outdated <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>. AI can capture this information, ensuring it's recorded and legible for others, thereby improving organizational knowledge and efficiency <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>. This also allows for the treatment of a knowledge base like a database, where operations can make semantic sense <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.

## [[challenges_and_benefits_of_integrating_ai_into_product_development | Challenges and Benefits of Integrating AI into Product Development]]

Integrating AI introduces a shift from deterministic to stochastic software, which can be challenging at scale <a class="yt-timestamp" data-t="00:28:33">[00:28:33]</a>. It's difficult to predict all cases where AI might fail, and new classes of errors can emerge even after extensive evaluation <a class="yt-timestamp" data-t="00:29:14">[00:29:14]</a>.

### Evaluation Strategies
Effective evaluation of AI models involves:
*   **Deterministic Evals:** If possible, creating deterministic evaluations is ideal because they are easy to measure and score, especially for classifier elements within workflows <a class="yt-timestamp" data-t="00:29:47">[00:29:47]</a>.
*   **Non-Deterministic Evals (Model-Graded Evals):** These involve using an AI to evaluate another AI's output, assessing "the vibe" or overall correctness <a class="yt-timestamp" data-t="00:30:19">[00:30:19]</a>. This requires careful design to ensure the grading model is highly competent and the evaluation task is targeted and clearly described <a class="yt-timestamp" data-t="00:30:50">[00:30:50]</a>.
*   **Continuous Improvement Loop:** A robust loop for logging, collecting, and labeling issues, and optimizing prompts is essential to prevent regressions <a class="yt-timestamp" data-t="00:31:26">[00:31:26]</a>. This process benefits from good data sets that capture error distributions and standardized evaluation methods <a class="yt-timestamp" data-t="00:31:53">[00:31:53]</a>.

### Designing Good LLM Interfaces
Key properties of a good AI interface include:
*   **Alignment with Training Data:** Interfaces should align with what models have been trained on (e.g., models prefer Markdown over complex XML structures) <a class="yt-timestamp" data-t="00:23:53">[00:23:53]</a>. This helps the model focus its attention on reasoning rather than complex formatting instructions <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>.
*   **Simplicity of Output Structure:** The output structure should be as simple as possible while still accomplishing the task <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>. Simplifying complex internal data representations can make it easier for models to produce correct outputs <a class="yt-timestamp" data-t="00:26:10">[00:26:10]</a>.
*   **Preventing Errors:** Developers should prioritize designing systems where classes of errors are impossible or have validation around them, before trying to improve prompts <a class="yt-timestamp" data-t="00:26:39">[00:26:39]</a>.
*   **Structured Chains of Thought:** Encouraging models to output intermediate steps or estimates (e.g., estimating the number of records needed) can align their thinking and improve adherence to constraints <a class="yt-timestamp" data-t="00:27:27">[00:27:27]</a>.

## The Future of AI and Human Interaction

The shift to AI-driven systems means that the role of humans will evolve. Instead of direct data entry or detailed management, humans will increasingly focus on defining high-level goals and overseeing AI operations <a class="yt-timestamp" data-t="00:49:50">[00:49:50]</a>. This involves observing AI outputs, ensuring they align with desired outcomes, and controlling what the AI does <a class="yt-timestamp" data-t="00:50:02">[00:50:02]</a>.

The ability to [[impact_of_ai_on_team_efficiency_and_business_operations | scale AI operations]] by adding more compute, rather than relying solely on human labor, is expected to lead to significant economic value creation and a complete transformation of job roles <a class="yt-timestamp" data-t="00:53:00">[00:53:00]</a>. Tasks like generating weekly updates from scattered data, which consume significant human time, can be automated by AI <a class="yt-timestamp" data-t="00:46:51">[00:46:51]</a>.

This era presents a unique opportunity for individuals to [[integrating_ai_with_creative_processes | build AI-powered tools]] for personal and professional needs, as the field is still new, with "low-hanging fruit" yet to be picked <a class="yt-timestamp" data-t="00:47:32">[00:47:32]</a>. The technology's power makes it common for random technical ideas to work, fostering creativity and exploration <a class="yt-timestamp" data-t="00:48:20">[00:48:20]</a>.