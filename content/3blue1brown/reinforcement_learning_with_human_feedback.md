---
title: Reinforcement learning with human feedback
videoId: LPZh9BOjkQs
---

From: [[3blue1brown]] <br/> 

Reinforcement learning with human feedback is a crucial phase in the [[training_process_of_language_models | training process of language models]], specifically for developing chatbots <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.

## Purpose

While pre-training enables a language model to auto-complete random text passages, this goal differs significantly from that of being an effective AI assistant <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>. To bridge this gap and make models more suitable for interactive assistance, chatbots undergo reinforcement learning with human feedback <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.

## How it Works

During this stage, human workers review and flag unhelpful or problematic predictions made by the model <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>. These corrections lead to further changes in the model's parameters (or weights), making the model more inclined to generate predictions that users prefer <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>. This process of [[adjusting_weights_and_biases_in_neural_networks | adjusting the model's parameters]] based on human input is essential for fine-tuning its behavior beyond the initial pre-training <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>.