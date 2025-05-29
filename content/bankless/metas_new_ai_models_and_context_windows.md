---
title: Metas new AI models and context windows
videoId: lrfplnEW090
---

From: [[bankless]] <br/> 

Meta has recently released a new AI model, referred to as Llama 4, which has generated significant discussion within the AI industry <a class="yt-timestamp" data-t="02:48:47">[02:48:47]</a>. While the model appears impressive on paper, its performance claims have led to controversy, raising questions about how [[AI Agents and Model Developments | AI models]] are evaluated and used <a class="yt-timestamp" data-t="02:54:82">[02:54:82]</a>.

## Key Features of Meta's New Models
Meta's latest release includes three models, with one being a "gigantic" two trillion-parameter beast <a class="yt-timestamp" data-t="08:20:79">[08:20:79]</a>. Two standout features of these [[AI Agents and Model Developments | models]] are:

*   **10 Million Token Context Window** <a class="yt-timestamp" data-t="05:42:26">[05:42:26]</a>: This represents a significant leap, as Google's Gemini model previously held the flagship with a 1 million token context window <a class="yt-timestamp" data-t="05:44:91">[05:44:91]</a>. A context window can be thought of as the "quick access memory" for a large language model <a class="yt-timestamp" data-t="05:57:43">[05:57:43]</a>, allowing the model to process a larger amount of data in a single query <a class="yt-timestamp" data-t="06:00:10">[06:00:10]</a>. A 10 million token window is equivalent to 75 novels or 1 million lines of code, enabling better recall and accuracy <a class="yt-timestamp" data-t="07:55:00">[07:55:00]</a>.
*   **Mixture of Experts (MoE) Design** <a class="yt-timestamp" data-t="08:30:26">[08:30:26]</a>: This design makes the models hyper-efficient. When querying the model, only a portion of its parameters (around 14 to 17 billion for the basic models, up to 250 billion for the larger one) are accessed <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>. This approach is more computationally efficient compared to models like OpenAI's, which query the entire trillion-parameter model <a class="yt-timestamp" data-t="08:55:38">[08:55:38]</a>.

Parameters, also known as weights, are units of information within an AI model <a class="yt-timestamp" data-t="09:13:95">[09:13:95]</a>. More parameters generally mean a "higher resolution camera pointed at the internet," leading to a more knowledgeable model <a class="yt-timestamp" data-t="09:27:00">[09:27:00]</a>. The continuous feeding of data during training alters these parameters, improving the model over time <a class="yt-timestamp" data-t="10:29:40">[10:29:40]</a>.

## Controversy and Benchmarking Issues
Meta has historically lagged as an [[AI Agents and Model Developments | AI lab]], with users typically preferring [[Frontier AI models and advancements by OpenAI | OpenAI's ChatGPT-4]] or Claude <a class="yt-timestamp" data-t="11:24:90">[11:24:90]</a>. The new Llama 4 models aimed to position Meta as a top contender <a class="yt-timestamp" data-t="11:41:00">[11:41:00]</a>. However, their release was met with significant backlash regarding its benchmark claims <a class="yt-timestamp" data-t="12:59:00">[12:59:00]</a>.

### Allegations and Meta's Response
Critics claimed that Meta had blended test results across different [[AI Agents and Model Developments | models]] to achieve skewed benchmarks, making their models appear comparable or superior to DeepSeek V3/R1 and [[Frontier AI models and advancements by OpenAI | OpenAI's]] 03 reasoning model <a class="yt-timestamp" data-t="13:12:00">[13:12:00]</a>. Many users, upon testing the model themselves, found its performance to be inferior to the reported benchmarks <a class="yt-timestamp" data-t="13:37:88">[13:37:88]</a>.

Meta's Head of Generative AI, Armored, denied claims of training on test sets, stating this was "simply not true" <a class="yt-timestamp" data-t="14:13:79">[14:13:79]</a>. He attributed the variable quality users were experiencing to an "implementation issue" that needed stabilization, implying challenges with inferencing or model overheating <a class="yt-timestamp" data-t="14:19:90">[14:19:90]</a>.

### Broader Implications for AI Benchmarking
The controversy highlights a growing concern within the industry: the effectiveness of benchmarks themselves <a class="yt-timestamp" data-t="14:51:71">[14:51:71]</a>.

> "Benchmarks as a whole very much feel like they're broken because they can be gamified." <a class="yt-timestamp" data-t="14:51:71">[14:51:71]</a>

Early benchmarks were effective for measuring new [[AI Agents and Model Developments | AI models]], but as models have become more advanced, standardizing these problems has made them "cheatable" <a class="yt-timestamp" data-t="15:02:40">[15:02:40]</a>. This phenomenon aligns with **Goodhart's Law**: "when a measure becomes a target, it ceases to become a good measure" <a class="yt-timestamp" data-t="15:52:19">[15:52:19]</a>. [[AI Agents and Model Developments | AI labs]] are incentivized to optimize models for specific tests rather than overall utility <a class="yt-timestamp" data-t="16:06:00">[16:06:00]</a>.

The drive for high benchmark numbers is also linked to talent acquisition, as top [[AI Agents and Model Developments | AI talent]] is scarce and prefers to work on leading [[AI Agents and Model Developments | models]] <a class="yt-timestamp" data-t="17:03:00">[17:03:00]</a>. This creates "warped outcomes and warped incentives" around benchmarking <a class="yt-timestamp" data-t="17:41:00">[17:41:00]</a>.

A suggested alternative to theoretical benchmarks is practical testing, similar to how GPUs are benchmarked using real, high-intensity games <a class="yt-timestamp" data-t="19:03:00">[19:03:00]</a>. The idea is to assess a model's capability based on its "material impact" on users' lives and how it helps solve real-world problems <a class="yt-timestamp" data-t="18:11:00">[18:11:00]</a>.