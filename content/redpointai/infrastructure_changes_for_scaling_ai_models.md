---
title: Infrastructure changes for scaling AI models
videoId: atMRWzgHEGg
---

From: [[redpointai]] <br/> 

The evolution and deployment of AI models, particularly large language models (LLMs) like Gemini, necessitate significant shifts in underlying [[evolution_of_ai_models_and_infrastructure | infrastructure needs]] and computational strategies. Experts from Google's Gemini LLM efforts, Noam Shazeer and Jack Rae, discuss these changes, highlighting the growing importance of [[scaling_challenges_in_ai_and_test_time_compute | test time compute]] and the implications for future AI development <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## Shifting from Training to Inference
Historically, the primary focus of AI infrastructure has been on large-scale pre-training of models. However, with the advancements in models like Gemini, the emphasis is increasingly shifting towards efficient inference, or "[[scaling_challenges_in_ai_and_test_time_compute | test time compute]]" <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

Jack Rae notes that while initial efforts for Gemini Flash concentrated on reasoning tasks like math and code, the model's ability to generalize to creative tasks and improve output through "thinking" (applying more compute at inference time) was a pleasant surprise <a class="yt-timestamp" data-t="03:02:04">[03:02:04]</a>.

Noam Shazeer attributes this shift to the economic reality that LLM search is "too cheap" <a class="yt-timestamp" data-t="01:57:51">[01:57:51]</a>. Operations now cost under 10^-18 dollars, meaning users can get millions of tokens per dollar, which is orders of magnitude cheaper than other common activities <a class="yt-timestamp" data-t="02:27:01">[02:27:01]</a>. This presents a massive "unexploited flops" margin to apply more compute at inference time to make models smarter <a class="yt-timestamp" data-t="02:48:06">[02:48:06]</a>.

## Economic and Resource Considerations
The [[the_economics_and_resource_costs_of_ai_model_scaling | economics and resource costs of AI model scaling]] are crucial. While training larger models can be done to improve performance, model training costs tend to increase quadratically with model size <a class="yt-timestamp" data-t="02:09:47">[02:09:47]</a>. In contrast, if done correctly, inference remains relatively cheap <a class="yt-timestamp" data-t="02:22:04">[02:22:04]</a>. This drives the current trend of applying more compute at inference time through methods like Chain of Thought thinking <a class="yt-timestamp" data-t="02:30:30">[02:30:30]</a>.

Jack Rae states that if building AI becomes primarily an inference problem, the [[evolution_of_ai_models_and_infrastructure | infrastructure needs]] can be "much more flexible" <a class="yt-timestamp" data-t="06:50:52">[06:50:52]</a>. This means a more distributed approach to compute compared to large batch training used in pre-training <a class="yt-timestamp" data-t="06:58:24">[06:58:24]</a>. This distributed nature can help drive prices down as it optimizes for an intrinsically cheaper setup <a class="yt-timestamp" data-t="07:30:46">[07:30:46]</a>.

## Hardware and Distributed Systems
The Google team benefits from a codesign relationship with its TPU (Tensor Processing Unit) team, allowing them to provide feedback on compute profiles to tweak chip and data center designs within a few years <a class="yt-timestamp" data-t="07:41:09">[07:41:09]</a>.

A key [[challenges_and_opportunities_in_ai_model_development_and_infrastructure | challenge]] in inference compared to training is the loss of parallelism in the Transformer architecture, leading to memory-bound operations, particularly when looking at attention keys and values for every token generated <a class="yt-timestamp" data-t="08:04:46">[08:04:46]</a>. This requires significant work in both model architecture and hardware to fully apply massive computational power to inference <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>.

For [[challenges_in_deploying_ai_models_effectively | deploying AI models]], particularly agentic ones that interact with environments, there are significant engineering challenges beyond core algorithmic development <a class="yt-timestamp" data-t="09:09:34">[09:09:34]</a>. Defining these environments and ensuring efficient orchestration within structured codebases (like Google's monorepo) are crucial for accelerating agentic research <a class="yt-timestamp" data-t="09:12:06">[09:12:06]</a>.