---
title: Challenges and solutions in using AI for unstructured data
videoId: zM9RYqCcioM
---

From: [[aidotengineer]] <br/> 

Method, a company that centralizes liability data from hundreds of sources for fintechs, banks, and lenders, faced significant challenges in extracting specific, liability-specific data points like payoff amounts or escrow balances for customers [01:48:09]. This information was crucial for debt management services such as refinancing, loan consolidation, and personal finance management [00:58:12].

## Initial Challenges and the Status Quo

Initially, Method found no central API to access these specific data points [02:07:10]. Working directly with banks was impractical for an early-stage company, as it would take years to establish [02:17:00].

The existing industry solution involved companies hiring offshore teams of contractors to manually call banks, authenticate, gather information, proof-check it, and integrate it into financial platforms [02:53:00].

This manual process presented several [[challenges_with_current_ai_implementation | challenges]]:
*   **Inefficiency and Lack of Scalability:** It was a highly inefficient and manual process, making scaling difficult [03:23:00].
*   **High Cost:** Each contractor could only handle one task at a time, necessitating more hires for scale [03:33:00].
*   **Slowness:** The synchronous nature of the process made it inherently slow [03:41:00].
*   **Human Error:** Significant human error was involved, requiring additional teams for fact-checking and proof-checking. Surfacing inaccurate financial information was a major risk [03:48:00].

Conceptually, this problem was akin to an API with request, authentication, and response validation components, boiling down to making sense of unstructured data [04:04:00].

## The Rise of AI and Initial Adoption

The announcement of GPT-4 and the subsequent "Cambrian explosion" of AI/LLM-enabled applications offered a potential solution [04:31:00]. Advanced LLMs, particularly post-GPT-4 models, excel at parsing unstructured data for tasks like summarization or classification [04:56:00].

Method developed an agentic workflow using GPT-4, which initially performed well [05:16:00]. They expanded use cases, finding GPT-4 effective even with high API costs [05:21:00].

## [[challenges_and_opportunities_in_ai_adoption | Challenges with Early AI Models and Implementations]]

Despite initial success, scaling the GPT-4 solution led to significant [[challenges_with_early_ai_models_and_improvements | challenges with early AI models and improvements]]:
*   **Prohibitive Cost:** The first month in production with GPT-4 incurred a cost of $70,000 [05:50:00]. While leadership recognized the immense value, this cost was a major concern [06:01:00].
*   **Prompt Engineering Limitations:** As use cases scaled, prompt engineering reached its limits [06:23:00]. GPT-4, though smart, was not a financial expert, requiring detailed instructions and examples [06:29:00]. Prompts became long, convoluted, and hard to generalize, leading to a "cat and mouse" chase where fixes for one scenario broke others [06:41:00]. There was also a lack of prompt versioning [06:52:00].
*   **Scaling Impediments:**
    *   **Expense:** Optimization for caching was difficult due to variability in responses and constant prompt tweaks [07:17:00].
    *   **Latency:** The baseline latency was too slow, preventing concurrent scaling [07:24:00].
    *   **AI Errors:** "Hallucinations" were hard to catch, similar to human errors but of a different nature [07:33:00].

Despite these scaling [[challenges_and_opportunities_in_ai_adoption | challenges and opportunities in AI adoption]], the system remained in production for specific valuable use cases [07:43:00].

## Shifting Focus: Scaling the Agentic Workflow

The problem evolved from parsing unstructured data (which GPT-4 had solved) to building a robust, scalable agentic workflow [07:50:00]. Method aimed for ambitious targets:
*   At least 16 million requests per day [08:10:00].
*   At least 100,000 concurrent load [08:12:00].
*   Minimal latency (sub-200 milliseconds) for real-time operations [08:16:00].

## OpenPipe's Solution: Benchmarking and Fine-Tuning

OpenPipe collaborated with Method to address these common issues of quality, cost, and latency [08:35:00].

### Benchmarking Existing Models
OpenPipe performed detailed benchmarking under real production conditions, considering diverse tasks and concurrency levels [10:21:00].

| Metric      | GPT-4 (0)     | O3 Mini (0)     |
| :---------- | :------------ | :-------------- |
| **Error Rate** | 11% [09:24:00] | 4% [09:28:00]   |
| **Latency** | ~1 second [10:08:00] | ~5 seconds [10:12:00] |
| **Cost**    | Lower [10:50:00] | Higher for this use case (more reasoning tokens) [10:50:00] |

Method measured error rates by having a human go through the agentic workflow and compare the agent's extracted information (e.g., bank balances) to the real numbers [09:39:00].

### Defining Performance Targets
Method established specific targets based on their operational needs:
*   **Error Rate:** Around 9% was acceptable, as additional plausible checks were performed after the model output [11:50:00].
*   **Latency:** A hard latency cutoff was necessary due to the real-time nature of their agent [12:06:00].
*   **Cost:** Critical due to the very high volume of transactions [12:40:00].

### The Need for Fine-Tuning
Neither GPT-4 nor O3 mini met all three requirements simultaneously [13:05:00]. GPT-4 struggled with error rate and cost, while O3 mini failed on cost and especially latency [13:16:00].

This indicated the need for fine-tuning, which is a powerful tool requiring more engineering investment than prompt engineering, but necessary when off-the-shelf models don't meet production reliability numbers [13:48:00].

### Fine-Tuning Results with OpenPipe
OpenPipe fine-tuned an 8 billion parameter LL 3.1 model, which often suffices for the majority of their customers [15:12:00].

| Metric      | Fine-Tuned Model |
| :---------- | :--------------- |
| **Error Rate** | Significantly better than GPT-4, below 9% threshold [14:28:00] |
| **Latency** | Much lower due to smaller model, can be further reduced by colocation [15:34:00] |
| **Cost**    | Much lower, exceeding cost thresholds for viability [16:02:00] |

Fine-tuning enabled Method to bend the price-performance curve significantly [14:18:00]. The process was made easier by using existing production data from GPT-4 to generate training data [14:45:00].

## Key Takeaways for [[Challenges and innovations in AI engineering | Productionizing AI Agents]]

*   **Simplicity and Cost-Effectiveness:** It's possible to identify a specific use case, fine-tune the cheapest available model, and achieve fast performance without needing to buy own GPUs [17:23:00].
*   **Data Availability:** Leveraging data already generated by earlier AI models (like GPT in production) can provide valuable training data for fine-tuning [17:30:00].
*   **Patience and Openness:** Productionizing AI agents requires a level of openness and patience from both engineering and leadership teams [17:47:00]. Unlike traditional code that is expected to "just work" once deployed, AI agents take time to become production-ready and continuously improve [17:57:00]. This marks a shift from traditional software engineering [18:14:00].