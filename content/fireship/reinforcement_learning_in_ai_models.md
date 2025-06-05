---
title: Reinforcement learning in AI models
videoId: -2k1rcRzsLA
---

From: [[fireship]] <br/> 

DeepSeek R1, a Chain of Thought model, utilizes a unique approach to [[training and finetuning AI models | training and finetuning]] that sets it apart from traditional methods: direct [[reinforcement_learning_and_chain_of_thought_in_ai_models | reinforcement learning]] <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

## How it Works
Unlike supervised [[training and finetuning AI models | fine-tuning]], where a model is shown step-by-step solutions to examples and then evaluated <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>, DeepSeek R1 employs a "pure" or direct [[reinforcement_learning_and_chain_of_thought_in_ai_models | reinforcement learning]] method <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. In this approach:
*   The model is given examples without being shown the solution first <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   It attempts various solutions on its own <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   The model learns and reinforces itself by eventually discovering the correct solution, similar to human reasoning <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

## DeepSeek R1's Algorithm
DeepSeek has released a paper detailing their [[reinforcement_learning_and_chain_of_thought_in_ai_models | reinforcement learning]] algorithm <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. For each problem, the [[Artificial Intelligence and reasoning models | AI]] generates multiple answers (outputs) <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. These answers are then grouped and assigned a "reward score" <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. The [[Artificial Intelligence and reasoning models | AI]] adjusts its approach to favor answers with higher scores, iteratively improving its performance <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

## Advantages for Chain of Thought Models
When prompting a Chain of Thought model like DeepSeek R1, it's recommended to keep the prompt concise and direct <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. The intention is for the model to perform the thinking independently <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. For instance, when solving a math problem, the model will first display its internal thinking steps before presenting the final solution <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

[[reinforcement_learning_and_chain_of_thought_in_ai_models | Chain of Thought models]] are particularly effective for [[Comparison with other AI models in coding | complex problem-solving]], including advanced math problems, puzzles, and coding challenges that require detailed planning <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

## Availability
DeepSeek R1 is available with a web-based user interface, via platforms like Hugging Face, or can be downloaded locally using tools such as Olama <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. The 7 billion parameter model weighs approximately 4.7 GB <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. For its full capability, the 671 billion parameter model requires over 400 GB and substantial hardware <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. A 32 billion parameter version is comparable to OpenAI's O1 Mini <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.