---
title: Comparisons with proprietary models like ChatGPT and Bard
videoId: 1ZwXkw9_Xq8
---

From: [[hu-po]] <br/> 

Llama 2 is Meta's large language model (LLM), serving as an open-source alternative to proprietary models such as [[using_gpt_api_for_dialogue_generation | ChatGPT]], Claude, and Bard <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. Unlike its predecessor, Llama 1, which was leaked, Llama 2 is the first "big competitive LLM" made widely available for public use <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Open-Source vs. Closed-Source Philosophy

Meta explicitly positions Llama 2 as a contrast to closed-source models from OpenAI and Google, which are described as very secretive <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. While proprietary LLMs like [[using_gpt_api_for_dialogue_generation | ChatGPT]], Bard, and Claude are heavily fine-tuned to align with human and company preferences for usability and safety, this process is often not transparent or easily reproducible, limiting progress <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>. Meta advocates for an open approach, believing it fosters responsible AI innovation, collaboration, and accelerates progress by allowing diverse stakeholders and small businesses to leverage and build upon foundational models <a class="yt-timestamp" data-t="02:34:25">[02:34:25]</a>.

## Performance Benchmarks

Llama 2 models, ranging from 7 billion to 70 billion parameters, include fine-tuned versions called Llama 2 Chat, optimized for dialogue use cases <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. They are noted to outperform other open-source chat models on most tested benchmarks <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

### Human Evaluations
Human evaluators compared Llama 2 models against other models on approximately 4,000 prompts, covering both single and multi-turn interactions.
*   **Against Open-Source Models:** Llama 2 consistently wins against Falcon 40B <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
*   **Against Proprietary Models:**
    *   Llama 2 70B performs roughly on par with Palm Bison, Google's language model <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>. Palm Bison is speculated to be around 80 billion parameters <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
    *   Llama 2 70B is "pretty much on par" with [[using_gpt_api_for_dialogue_generation | ChatGPT]] 3 (specifically Chat GPT 03/01) <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>. More ties are observed between Llama 2 and [[using_gpt_api_for_dialogue_generation | ChatGPT]] 3 than wins for either <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
    *   Overall, Llama 2 performs somewhere between [[using_gpt_api_for_dialogue_generation | ChatGPT]] 3 and Google's Palm Bison <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
    *   Human evaluators' agreement on helpfulness scores is not consistently high, with inter-rater reliability (IRR) varying between 0.37 and 0.5 <a class="yt-timestamp" data-t="01:57:31">[01:57:31]</a>.

### GPT-4 Based Evaluations
Llama 2's performance was also evaluated using [[capabilities_of_gpt4 | GPT-4]] as a judge, comparing it to [[using_gpt_api_for_dialogue_generation | GPT3]], Palm Bison, and Falcon 40B.
*   Llama 2 is found to be better in "pretty much every case" in terms of helpfulness and safety when judged by [[capabilities_of_gpt4 | GPT-4]] <a class="yt-timestamp" data-t="01:12:22">[01:12:22]</a>.
*   Using [[capabilities_of_gpt4 | GPT-4]] for evaluation is noted as potentially misleading due to unknown biases [[capabilities_of_gpt4 | Capabilities of GPT4]] <a class="yt-timestamp" data-t="01:13:19">[01:13:19]</a>.

### Academic Benchmarks
[[comparison_of_language_models_in_coding_tasks | Academic benchmarks]] results are self-reported for closed models:
*   On the MMLU (Massive Multitask Language Understanding) benchmark, [[capabilities_of_gpt4 | GPT-4]] "blows everything else out of the water" <a class="yt-timestamp" data-t="01:00:21">[01:00:21]</a>. Llama 2 is about on par with Palm and [[using_gpt_api_for_dialogue_generation | GPT 3.5]] <a class="yt-timestamp" data-t="01:00:26">[01:00:26]</a>.
*   For the GSM8K (Grade School Math 8K) dataset of math word problems <a class="yt-timestamp" data-t="01:00:49">[01:00:49]</a>, Llama 2 performs significantly worse than [[capabilities_of_gpt4 | GPT-4]] <a class="yt-timestamp" data-t="01:01:16">[01:01:16]</a>. However, [[using_gpt_api_for_dialogue_generation | GPT 3.5]] is comparable to Llama 2 on this task <a class="yt-timestamp" data-t="01:01:21">[01:01:21]</a>. The difference might be due to [[gpt4_ensemble_of_models | GPT-4 ensemble of models]] approach, which uses "eight slightly larger [[using_gpt_api_for_dialogue_generation | GPT 3.5]]s" <a class="yt-timestamp" data-t="01:01:31">[01:01:31]</a>.
*   Llama 2 is considered the "best open source LLM" available, surpassing Falcon 40B, MPT 7, and Vicuna <a class="yt-timestamp" data-t="02:43:24">[02:43:24]</a>.

## Model Training and Data
Meta states that Llama 2 is trained on a new mix of publicly available data, explicitly not including data from Meta's products or services <a class="yt-timestamp" data-t="02:22:54">[02:22:54]</a>. This is seen as a potential "huge amount of juice" that Meta could still leverage in the future <a class="yt-timestamp" data-t="02:32:31">[02:32:31]</a>. The pre-training corpus was increased by 40% compared to Llama 1, reaching two trillion tokens <a class="yt-timestamp" data-t="01:18:18">[01:18:18]</a>.

## Safety and Helpfulness Alignment

Llama 2 Chat models are optimized for dialogue and are fine-tuned using a combination of supervised fine-tuning and reinforcement learning from human feedback (RLHF) <a class="yt-timestamp" data-t="01:19:55">[01:19:55]</a>. This involves training two separate reward models: one for helpfulness and one for safety <a class="yt-timestamp" data-t="01:21:35">[01:21:35]</a>.

*   **Trade-off:** Helpfulness and safety can sometimes trade off <a class="yt-timestamp" data-t="01:27:27">[01:27:27]</a>. A maximally helpful model might assist in building a pipe bomb, while a maximally safe model might refuse to answer a question about a "bath bomb" due to the word "bomb" <a class="yt-timestamp" data-t="02:47:24">[02:47:24]</a>.
*   **Mitigation:** Meta uses techniques like "context distillation" to generate safer responses by initially prefixing prompts with a safety instruction, then fine-tuning the model on these safer responses without the explicit prefix <a class="yt-timestamp" data-t="02:05:05">[02:05:05]</a>.
*   **Impact on Capabilities:** Models with more safety mitigation tend to answer certain questions in a more conservative manner <a class="yt-timestamp" data-t="02:08:40">[02:08:40]</a>. It's suggested that this focus on safety might contribute to proprietary models like [[using_gpt_api_for_dialogue_generation | ChatGPT]] becoming "stupider and stupider" over time as they are increasingly constrained <a class="yt-timestamp" data-t="02:09:08">[02:09:08]</a>.
*   **False Refusals:** Llama 2 Chat sometimes struggles to distinguish safe prompts containing words frequently associated with unsafe generations (e.g., "Christmas crack" or "bomb" in "bath bomb") <a class="yt-timestamp" data-t="02:09:54">[02:09:54]</a>.
*   **Transparency:** The paper is criticized for not fully disclosing the source of human annotators used for safety and helpfulness evaluations <a class="yt-timestamp" data-t="01:55:54">[01:55:54]</a>.

## Context Length

Llama 2 has doubled its context length from 2048 tokens to 4096 tokens <a class="yt-timestamp" data-t="02:29:16">[02:29:16]</a>. This is useful for longer histories in dialogue, summarization, and understanding longer documents <a class="yt-timestamp" data-t="02:11:03">[02:11:03]</a>. However, this is still less than [[using_gpt_api_for_dialogue_generation | GPT]]'s 8000 tokens or Claude's 32,000 tokens <a class="yt-timestamp" data-t="02:29:25">[02:29:25]</a>.

## Key Takeaways

*   Llama 2 aims to democratize access to LLMs by being openly released for both research and commercial use <a class="yt-timestamp" data-t="02:34:04">[02:34:04]</a>.
*   The 13B (13 billion parameter) version is considered a "sweet spot" for performance and local usability, as the 7B model is "kind of stupid" and the 70B model requires significant GPU resources <a class="yt-timestamp" data-t="02:42:32">[02:42:32]</a>.
*   Areas for future [[advancements_in_language_models | advancements in language models]] for Llama 2 include potentially leveraging Meta's internal proprietary data, using a more modern tokenizer, and training for longer periods without saturation <a class="yt-timestamp" data-t="02:45:47">[02:45:47]</a>.
*   The debate between safety and helpfulness, and how much control companies should exert over models, is highlighted as a significant future challenge <a class="yt-timestamp" data-t="02:00:46">[02:00:46]</a>.

> [!NOTE] The concept of "whitening" in reward function normalization for Llama 2 refers to decorrelating the dimensions of the score vector, making them independent <a class="yt-timestamp" data-t="01:39:11">[01:39:11]</a>. This differs from simple normalization (mean of zero, standard deviation of one), which Llama 7B incorrectly described as whitening <a class="yt-timestamp" data-t="01:40:09">[01:40:09]</a>.

> [!WARNING] The report mentions a Llama 2 34B model in some benchmarks but states it was not released due to "lack of time to sufficiently Red Team" <a class="yt-timestamp" data-t="02:52:54">[02:52:54]</a>. This model showed a higher safety violation rate compared to the 7B, 13B, and 70B versions <a class="yt-timestamp" data-t="01:16:59">[01:16:59]</a>.