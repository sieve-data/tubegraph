---
title: GPT4 ensemble of models
videoId: MVWYTFs9M-s
---

From: [[hu-po]] <br/> 

A significant report, based on a tweet by Sumit referencing a podcast by George Hotz, suggests that [[capabilities_of_gpt4 | GPT-4]] is not a single large language model but rather an ensemble of models <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. This revelation, while not widely discussed initially, could become major news <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## Architecture and Scale
According to George Hotz, [[capabilities_of_gpt4 | GPT-4]] is an ensemble of eight distinct models <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Each of these models is estimated to have approximately 220 billion parameters <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. It is likely that these individual models are subtly different, possibly due to varying fine-tuning datasets <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## Rationale for Ensembling
The strategy of using multiple models to enhance final performance is known as [[model_ensembling_in_machine_learning | model ensembling]] or a mixture model <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This approach makes "a ton of sense" for several reasons <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

### Performance Improvement
Ensembling is a popular technique in Kaggle competitions, where the goal is to extract the maximum performance from models <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Competitors often train numerous versions of the same model on slightly different subsets of data <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. This diversification in training leads to more varied outputs for a given input <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Selecting the best output from these multiple models typically yields superior results compared to relying on a single "best" model <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. This method explains the high performance of [[capabilities_of_gpt4 | GPT-4]] <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

### Explaining High Inference Costs
The ensemble architecture also provides an explanation for Sam Altman's frequent statements about the high cost of inference for [[capabilities_of_gpt4 | GPT-4]] <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. While models like Bard.google.com perform inference on a single model per query <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>, [[capabilities_of_gpt4 | GPT-4]], if the ensemble claim is correct, conducts 16 inferences for each query <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. This implies that OpenAI's inference costs could be 16 times higher than those of other [[comparisons_with_proprietary_models_like_chatgpt_and_bard | proprietary models like ChatGPT and Bard]] <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. The final output seen by the user is the result of these 16 inferences, likely with a "value function" model selecting the best one <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

## Supporting Evidence
The claim of [[capabilities_of_gpt4 | GPT-4]] being an ensemble is supported by three pieces of evidence:

1.  **Popularity in Kaggle Competitions**: As mentioned, [[model_ensembling_in_machine_learning | model ensembling]] is a common and effective strategy in competitive machine learning <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
2.  **Consistency with OpenAI's Narrative**: The high inference cost aligns with Sam Altman's repeated public comments <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
3.  **OpenAI's Historical Practices**: OpenAI's own 2021 Codex paper demonstrates a similar strategy <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. In Codex, they generated 100 samples per token to solve "little LeetCode problems" and then filtered them down <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. They also fine-tuned Codex on training problems to produce a "set of supervised fine-tuned models," referred to as "Codex S" <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. Given the timing of this paper (2021), it is plausible they extended this strategy to [[capabilities_of_gpt4 | GPT-4]] <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

## Implications
This understanding puts the performance jump seen with ChatGPT and the subsequent hype into context <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. It suggests that OpenAI essentially created an ensemble of eight slightly different models that are "masquerading as a single model" <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.