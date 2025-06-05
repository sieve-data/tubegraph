---
title: Finetuning AI models for specific use cases
videoId: zM9RYqCcioM
---

From: [[aidotengineer]] <br/> 

Finetuning AI models is a powerful technique for adapting pre-trained models to specific tasks, overcoming the limitations of general models and achieving better performance, lower costs, and reduced latency. It's considered a "power tool" in AI development, requiring more engineering investment than simple prompt engineering, but offering significant advantages when off-the-shelf models don't meet production requirements <a class="yt-timestamp" data-t="13:48:00">[13:48:00]</a>.

## Challenges with General Purpose Models

Method, a company that collects and centralizes liability data, faced a challenge in providing specific liability data points like payoff amounts on auto loans or escrow balances for mortgages <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>. There was no central API available to retrieve this information <a class="yt-timestamp" data-t="02:07:07">[02:07:07]</a>.

Initially, companies would hire offshore teams to manually call banks, authenticate, gather information, and proof-check it before integration into financial platforms <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>. This manual process was:
*   **Inefficient and not scalable** <a class="yt-timestamp" data-t="03:23:00">[03:23:00]</a>
*   **Expensive** due to the need for more personnel to scale <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>
*   **Slow** due to its synchronous nature <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>
*   **Prone to human error**, requiring additional teams for fact-checking and proof-checking <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>

The core problem was making sense of unstructured data <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>. With the rise of advanced Large Language Models (LLMs) like GPT-4, which excel at parsing unstructured data for tasks like summarization or classification <a class="yt-timestamp" data-t="05:02:00">[05:02:00]</a>, Method developed an agentic workflow using GPT-4 <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>.

However, using off-the-shelf, larger models like GPT-4, even when effective, presented new [[customization_and_scalability_in_ai_models | challenges]]:

*   **Cost:** The first month in production with GPT-4 incurred a cost of $70,000 <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>. This high cost made scaling difficult <a class="yt-timestamp" data-t="07:15:00">[07:15:00]</a>.
*   **Prompt Engineering Limitations:** Prompt engineering only goes so far <a class="yt-timestamp" data-t="06:25:00">[06:25:00]</a>. GPT models, while smart, are not financial experts, requiring extremely detailed and specific instructions with examples <a class="yt-timestamp" data-t="06:31:00">[06:31:00]</a>. Prompts became long, convoluted, hard to generalize, and unstable (fixing one scenario broke another) <a class="yt-timestamp" data-t="06:42:00">[06:42:00]</a>.
*   **Latency:** Baseline latency was too slow for concurrent scaling <a class="yt-timestamp" data-t="07:24:00">[07:24:00]</a>.
*   **Caching Issues:** Variability in responses and frequent prompt tweaks made it difficult to optimize for caching <a class="yt-timestamp" data-t="07:18:00">[07:18:00]</a>.
*   **AI Errors (Hallucinations):** Like human errors, AI models produced errors (hallucinations) that were hard to catch <a class="yt-timestamp" data-t="07:36:00">[07:36:00]</a>.

Despite these issues, GPT-4 remained in production for specific use cases due to its effectiveness <a class="yt-timestamp" data-t="07:44:00">[07:44:00]</a>. The problem then shifted from solving data parsing to scaling this AI system robustly to handle high volumes, with targets like 16 million requests per day, 100K concurrent load, and sub-200 millisecond latency <a class="yt-timestamp" data-t="07:57:00">[07:57:00]</a>.

## Benchmarking and Goals

To address these issues, OpenPipe worked with Method on [[evaluations_and_finetuning_in_ai_development | benchmarking]] different models against specific criteria:

*   **Error Rates (Quality):**
    *   GPT-4: ~11% error rate <a class="yt-timestamp" data-t="09:24:00">[09:24:00]</a>
    *   03 Mini: ~4% error rate <a class="yt-timestamp" data-t="09:26:00">[09:26:00]</a>
    *   Method measured this by having a human determine the correct numbers for bank balances and comparing them to the agent's final outputs <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>. Their target was around 9% error rate, due to additional plausibility checks <a class="yt-timestamp" data-t="11:50:00">[11:50:00]</a>.
*   **Latency:**
    *   GPT-4: ~1 second <a class="yt-timestamp" data-t="10:08:00">[10:08:00]</a>
    *   03 Mini: ~5 seconds <a class="yt-timestamp" data-t="10:12:00">[10:12:00]</a>
    *   Measurements were conducted under real production conditions with diverse tasks and reasonable concurrency <a class="yt-timestamp" data-t="10:21:00">[10:21:00]</a>. Method's real-time agent system required a hard latency cut-off for quick responses <a class="yt-timestamp" data-t="12:06:00">[12:06:00]</a>.
*   **Cost:**
    *   03 Mini was found to be more expensive than GPT-4 for Method's specific use case, despite its lower per-token cost, because it generated more reasoning tokens and longer outputs <a class="yt-timestamp" data-t="10:42:00">[10:42:00]</a>.
    *   Given Method's high volume, cost was a critical factor <a class="yt-timestamp" data-t="12:40:00">[12:40:00]</a>.

Neither GPT-4 nor 03 Mini met all three requirements for production deployment <a class="yt-timestamp" data-t="13:03:00">[13:03:00]</a>. GPT-4 fell short on error rate and cost, while 03 Mini failed on cost and, critically, latency <a class="yt-timestamp" data-t="13:16:00">[13:16:00]</a>. This situation indicated that simple prompting wouldn't suffice, necessitating [[finetuning_of_language_models_using_quen_models | finetuning]].

## The Power of Finetuning

[[ai_models_and_training_methods | Finetuning]] involves building [[customization_and_scalability_in_ai_models | custom models]] for specific use cases. It allows for significant improvements in the price-performance curve <a class="yt-timestamp" data-t="14:17:00">[14:17:00]</a>:

*   **Improved Quality (Lower Error Rates):**
    *   Finetuning enabled Method to achieve significantly better accuracy than GPT-4, falling below their required error rate threshold <a class="yt-timestamp" data-t="14:28:00">[14:28:00]</a>.
    *   Modern models like 03 Mini facilitate this by allowing the use of production data to generate outputs, which then serve as training data for a smaller, finetuned model (a "teacher model" approach) <a class="yt-timestamp" data-t="14:40:00">[14:40:00]</a>. While not always matching the teacher model's performance, the finetuned model can get "quite close" and often outperform larger, less optimized models <a class="yt-timestamp" data-t="15:00:00">[15:00:00]</a>.
    *   For Method, an 8-billion parameter LLM model was sufficient <a class="yt-timestamp" data-t="15:14:00">[15:14:00]</a>.
*   **Reduced Latency:**
    *   Moving to a much smaller, finetuned model (e.g., 8 billion parameters) significantly reduces latency because there are fewer calculations <a class="yt-timestamp" data-t="15:34:00">[15:34:00]</a>.
    *   It also enables deploying the model within one's own infrastructure, co-locating it with application code to eliminate network latency entirely <a class="yt-timestamp" data-t="15:51:00">[15:51:00]</a>.
*   **Lower Cost:**
    *   Smaller finetuned models result in a much lower cost of operation <a class="yt-timestamp" data-t="16:04:00">[16:04:00]</a>.
    *   For Method, the finetuned model far exceeded their cost thresholds, making the solution viable from a unit economics perspective and removing cost as a primary concern <a class="yt-timestamp" data-t="16:20:00">[16:20:00]</a>.

## Implementing Finetuning

[[techniques_for_improving_ai_model_efficiency | Finetuning]] allows companies to achieve high reliability numbers that might be unattainable with prompt engineering alone <a class="yt-timestamp" data-t="16:50:00">[16:50:00]</a>. Method successfully implemented finetuning by:
*   Identifying a specific use case <a class="yt-timestamp" data-t="17:25:00">[17:25:00]</a>.
*   Using the cheapest available model <a class="yt-timestamp" data-t="17:28:00">[17:28:00]</a>.
*   Leveraging existing data from GPT in production for training <a class="yt-timestamp" data-t="17:32:00">[17:32:00]</a>.
*   Selecting a model that offered the fastest performance <a class="yt-timestamp" data-t="17:39:00">[17:39:00]</a>.
*   Avoiding the need to purchase their own GPUs <a class="yt-timestamp" data-t="17:42:00">[17:42:00]</a>.

[[leveraging_ai_tools_for_efficiency_and_scalability | Productionizing AI agents]] requires openness and patience from engineering and leadership teams because, unlike traditional code, AI agents take time to become production-ready and provide desired responses consistently <a class="yt-timestamp" data-t="17:47:00">[17:47:00]</a>. This approach of finetuning smaller models allows businesses like Method to scale to very large production volumes <a class="yt-timestamp" data-t="17:04:00">[17:04:00]</a>.