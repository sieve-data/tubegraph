---
title: Enterprise AI model management
videoId: 7-3IxVvWoxc
---

From: [[redpointai]] <br/> 

Jonathan Frankle, Chief AI Scientist at Databricks, focuses on helping enterprises navigate their AI journeys. This involves determining when to train their own models, [[finetuning_ai_models_for_enterprise_data | finetune existing models]], or simply use prompt engineering [00:00:08]. Databricks leverages lessons learned from working with its 12,000 customers on AI, and internally, the company uses its own suite of products, including Spark for data ingestion, Delta tables for storage, Unity Catalog for tracking, MLflow for experiment tracking, and Mosaic inference service [00:14:30].

## The Enterprise AI Journey

The first step in any AI journey for an enterprise is to keep options open, as the end goal (prompting versus pre-training from scratch) is not immediately obvious [00:07:56]. Databricks aims to provide a platform that accommodates the entire spectrum of possibilities without compromise [00:08:00].

### Initial Exploration and Experimentation
Starting small is crucial. Enterprises can begin by prompting an existing model (e.g., OpenAI or Llama on Databricks) for a minimal cost, like 20 cents, to perform a "litmus test" and determine if AI is suitable for a specific use case [00:08:21]. This involves running experiments and building initial benchmarks, even if they are imperfect [00:08:43]. The focus should be on incremental progress justified by rigorous ROI [00:09:04].

### Leveraging Data
For most enterprise applications, a generic model will not inherently understand internal company data [00:09:31]. Therefore, bringing the company's data to bear is essential, often through techniques like Retrieval Augmented Generation (RAG) [00:09:27]. This process is referred to as "data intelligence" at Databricks [00:09:41].

### Model Optimization and Customization
As value is realized, the journey can progress to more advanced stages:
*   **[[finetuning_ai_models_for_enterprise_data | Finetuning]]**: This bakes knowledge into the model, offering better quality in a smaller package and potentially reducing inference costs, despite a slightly higher upfront investment [00:09:50].
*   **Continued Pre-training**: This step requires more extensive use cases to justify the investment [00:10:03].
*   **Full Pre-training**: This is a significant undertaking, expensive and demanding, but for those who need it, it provides unique capabilities not widely available elsewhere [00:08:08].

These steps represent a [[cost_optimization_and_economic_considerations_for_ai_model_deployment | cost-quality trade-off]]: moving up the chain involves more upfront investment but yields better quality or lower inference costs for the same quality [00:18:08]. The justification for advancing to more complex methods should come from increasing usage and a clear ROI [01:00:07].

### Agile Development and Evaluation
A common mistake is waiting for "perfect" data or evaluation metrics before starting AI development [00:10:14]. Instead, an agile approach is recommended:
*   Perform minimal data preparation to allow interaction with the model [00:10:46].
*   Build the simplest possible model [00:10:50].
*   Create a quick, basic evaluation [00:10:51].
*   Test and iterate to identify whether issues lie with the model, data, or unrealistic expectations of AI [00:10:55].

For evaluation, starting with just five examples can help calibrate an LLM judge to rate responses [00:13:01]. Direct human testing, even with a single friend, is more valuable than any synthetic benchmark [00:11:30]. Databricks is releasing an "agent eval" product to help users create meaningful evaluation sets quickly, aiming to enable an afternoon's work to build a robust eval set [00:13:31].

## When Company-Specific Models Make Sense
Custom or domain-specific models are beneficial in several scenarios:
1.  **Language/Cultural Nuances**: Models may not be well-tuned for non-English languages (e.g., Japanese, Korean) due to less available data [00:16:18].
2.  **Unique Domains**: For tasks entirely different from typical language modeling, such as protein modeling, custom models are necessary [00:17:13].
3.  **Speed and Specificity**: When an extremely fast and specific model is required, for instance, for code completion in free-tier services where cost is a major constraint [00:17:27].
4.  **Cost Optimization**: Beyond a certain usage threshold, the upfront cost of pre-training or [[finetuning_ai_models_for_enterprise_data | finetuning]] can be offset by significantly reduced inference costs or improved quality [00:17:58].

Once a product achieves market fit, the focus shifts to optimizing for both quality and cost, which justifies moving further up the model development chain [01:00:07].

## Product Market Fit in AI Applications
Two patterns indicate product market fit for AI:
1.  **High Tolerance for Error**: Applications where brainstorming, creativity, or information surfacing don't require perfect accuracy, as there are many "right" answers [00:19:47]. Examples include creative applications, marketing, media, or tools like Glean for surfacing information [00:20:00].
2.  **Human Checkable Outputs**: Scenarios where the AI's proposed answer is costly for a human to produce but relatively quick for a human to check [00:20:14]. This aligns with "P versus NP" problems where solutions are hard to find but easy to verify [00:20:41]. Coding copilots are a prime example, as reviewing code is easier than writing it from scratch [00:21:02]. Customer support and certain semantic search problems (where missing one link is acceptable) also fit this category [00:21:28].

AI's inherent "fuzziness" is both a superpower and a challenge [00:22:37]. While chaining multiple models can push quality higher, achieving "perfection" (e.g., five nines of reliability) is hard with current technology [00:24:07]. Organizations need to understand and accept this fuzziness, just as they learned to manage the complexities and vulnerabilities of traditional software engineering over decades [00:24:40].

## The Role of Platforms and Future Directions
Databricks' strategy is to provide a comprehensive, end-to-end platform where all tools work seamlessly together, minimizing concerns about data transit or cobbling disparate tools [00:30:09]. The goal is to make the journey from zero to one in AI as straightforward as possible for customers [00:29:58].

Key unanswered questions in the AI offerings space include:
*   How to help customers effectively measure their models [00:31:00].
*   Navigating the choices between RAG, prompting, and [[finetuning_ai_models_for_enterprise_data | finetuning]] for different use cases [00:31:15]. The solution might involve providing a wide array of options (e.g., 200 diverse models from one or two fine-tuning runs) and tools to help choose the best fit [00:31:48].
*   Helping customers get models into production and ensuring their comfortable operation [00:32:29].

The AI infrastructure landscape, including standalone evaluation companies, data ingestion companies, and inference providers, will likely evolve like other software spaces: end-to-end platforms coexist with specialized point solutions [00:33:15]. Databricks partners with many startups and sometimes acquires them (like Lilac for data exploration/eval creation) when their tools prove invaluable [00:34:44].

Regarding the future of large language models like Llama, Frankle believes the open-source model world is "exceedingly well covered" due to massive investments by companies like Meta and the valuable contributions of organizations like the Allen Institute for AI [00:37:00]. Databricks' focus is on addressing other gaps in the AI ecosystem to ensure customer success, such as:
*   Eval creation [00:37:15].
*   Navigating the space of [[finetuning_ai_models_for_enterprise_data | finetuning]] and RAG without overwhelming choice [00:37:25].
*   Assisting customers with varied and imperfect data inputs (e.g., lots of inputs but few outputs, or only documents/code) [00:37:40].
*   Developing compound AI systems and agents to connect different components [00:38:05].

Frankle emphasizes that the "last mile" of turning raw AI technology into useful systems for customers is where the biggest challenges and opportunities lie [00:38:15].

## Societal and Policy Considerations
Jonathan Frankle stresses the importance of AI practitioners participating in policy conversations, not solely for self-interest, but as a service to society [00:53:00]. Building trust with policymakers is crucial, and transparency about biases and limitations is key [00:55:00].

Key policy issues to discuss include:
*   **Contextual Application**: Determining when AI systems should or should not be allowed in specific contexts based on their reliability [00:55:21].
*   **Standards for AI vs. Humans**: Thoughtfully setting standards for AI systems and, by extension, re-evaluating standards for human performance in similar tasks [00:56:07].
*   **Extraordinary Caution**: Exercising extreme caution in high-stakes areas where mistakes can have severe consequences (e.g., law enforcement, medicine, autonomous vehicles) [00:57:02]. It's acceptable to be "technologically backwards" in certain areas if it allows for careful and thoughtful deployment [00:56:37].
*   **Honesty and Trust**: The AI industry owes society scientific honesty about what the technology can and cannot do, avoiding over-promising superintelligence or specific timelines [00:57:46]. This honesty is vital for building and maintaining trust [00:57:56].

## Underexplored Applications and Future Technologies
While most AI application areas are being explored, Frankle expresses excitement about **robotics** and embodied systems [00:58:53]. The potential to automate physical tasks, similar to how information processing has been transformed, is immense, though it carries significant risks [00:59:01].

Regarding massive compute investments (e.g., $50 billion+) for future models, Frankle states it's hard to predict if they will yield superintelligence or merely incremental improvements [01:00:07]. He views these as experiments he's curious to observe [01:00:29].