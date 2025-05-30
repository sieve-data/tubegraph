---
title: Challenges and opportunities in AI model finetuning
videoId: gwgDDkLFvd0
---

From: [[redpointai]] <br/> 

Finetuning AI models involves adapting a pre-trained model to a specific task or dataset. This process can significantly improve model performance and efficiency for particular use cases <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>.

## When to Finetune vs. Use Base Models

For developers and enterprises, deciding whether to use a base model (like GPT-3.5 or GPT-4) or to finetune is a key consideration <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.

*   **GPT-3.5 Turbo vs. GPT-4:** GPT-3.5 Turbo is highly capable for many use cases, but it may require more effort to craft a precise prompt <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>. GPT-4 generally performs better when prompts involve more than three or four instructions <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>. Following DevDay price drops, GPT-4 has become more affordable, leading many to use it directly to avoid the extra effort of prompt engineering <a class="yt-timestamp" data-t="05:33:00">[05:33:00]</a>.
*   **Performance:** Some early customers using finetuned GPT-3.5, combined with prompt engineering, have achieved GPT-4 level performance <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>.

## Benefits of Finetuning

Finetuning offers several advantages for specific applications:

*   **Improved Performance:** Finetuning can help models achieve better performance for particular tasks <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>.
*   **Token Savings:** For example, by finetuning GPT-3.5 for function calling, developers can train the model to "hallucinate" functions, eliminating the need to pay for function tokens with every call <a class="yt-timestamp" data-t="06:50:00">[06:50:00]</a>. This can lead to significant cost savings <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>.

## Challenges of Finetuning

While beneficial, finetuning presents [[Challenges and strategies in AI model development | challenges]]:

*   **Data Requirements:** Finetuning requires substantial, high-quality data <a class="yt-timestamp" data-t="07:42:00">[07:42:00]</a>. For custom models, billions of tokens might be needed <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>.
*   **Expertise:** Effective finetuning demands a level of machine learning understanding, and poor data quality can lead to suboptimal results <a class="yt-timestamp" data-t="10:44:00">[10:44:00]</a>.
*   **Cost:** Creating custom models can be very expensive, potentially costing millions of dollars <a class="yt-timestamp" data-t="08:17:00">[08:17:00]</a>.
*   **Dependency Concerns:** Some enterprises are wary of taking on dependencies with venture-backed open-source companies, preferring to rebuild infrastructure themselves <a class="yt-timestamp" data-t="20:07:00">[20:07:07]</a>.

## Custom Models: An Advanced Approach

Custom models represent a deeper form of finetuning, often involving OpenAI's research teams directly assisting companies.

*   **Requirements:** These models are typically suited for domains where base models lack sufficient training data, such as legal or medical fields, and where companies possess extensive proprietary data <a class="yt-timestamp" data-t="07:44:00">[07:44:00]</a>.
*   **Cost and Accessibility:** Custom models are currently very expensive, limiting their accessibility to companies with significant capital expenditure <a class="yt-timestamp" data-t="08:23:00">[08:23:00]</a>.
*   **Expert Support:** OpenAI's research teams provide hands-on assistance to companies training these custom models, addressing the need for world-class machine learning expertise <a class="yt-timestamp" data-t="11:15:00">[11:15:15]</a>.
*   **Comparison to Open Source:** While open-source models (like Llama) offer more granular customization and ownership of model weights <a class="yt-timestamp" data-t="15:52:00">[15:52:00]</a>, large proprietary models are expected to remain superior in performance due to their scale and engineering investment <a class="yt-timestamp" data-t="15:03:00">[15:03:00]</a>. Open-source models also allow for more extensive [[Pretraining and finetuning AI models | finetuning approaches and considerations in AI]], including reinforcement learning from human feedback (RLHF), which is not yet a standard offering from OpenAI <a class="yt-timestamp" data-t="16:16:00">[16:16:00]</a>.

## Future of Finetuning and Custom Models

The future of [[Finetuning approaches and considerations in AI | finetuning AI models for enterprise data]] and custom models is expected to evolve:

*   **Accessibility:** OpenAI aims to make custom models more accessible and affordable through API offerings <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>.
*   **Advanced Techniques:** The company anticipates supporting more diverse finetuning and training techniques, such as RLHF <a class="yt-timestamp" data-t="16:07:00">[16:07:00]</a>.
*   **Base Model Improvements:** Continued improvements in base models will make them more steerable, which could reduce the need for custom models in some cases, though a need will likely always remain for specialized domains <a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a>.
*   **Efficiency:** Custom models may become more compute-efficient by removing unnecessary data from training sets, allowing for more focused data input <a class="yt-timestamp" data-t="10:02:00">[10:02:00]</a>.

As the AI ecosystem progresses, the goal is to provide a comprehensive platform where developers can find all necessary tools for building, including [[The role of reinforcement and finetuning in AI | finetuning]], [[Challenges and optimizations in AI model training and inference | inference]], and various model development steps <a class="yt-timestamp" data-t="00:59:22">[00:59:22]</a>.