---
title: Evals and their importance in AI product management
videoId: scsW6_2SPC4
---

From: [[lennyspodcast]] <br/> 

Evals, or evaluations, are rapidly becoming a core skill for product builders, particularly within the field of [[ai_in_product_management | AI product management]] <a class="yt-timestamp" data-t="02:04:15">[02:04:15]</a>. Understanding and utilizing evals is crucial for developing effective AI products, as they provide a mechanism to assess and improve model performance <a class="yt-timestamp" data-t="01:17:16">[01:17:16]</a>.

## What are Evals?
An eval can be thought of as a "quiz" or a "test" for an AI model <a class="yt-timestamp" data-t="01:19:24">[01:19:24]</a>. They are designed to gauge how well a model understands a certain subject or how adept it is at responding to specific questions <a class="yt-timestamp" data-t="01:29:32">[01:29:32]</a>.
<a class="yt-timestamp" data-t="02:03:55">[02:03:55]</a>
Evals serve as benchmarks for a model's intelligence and capabilities, similar to how unit tests function for software code <a class="yt-timestamp" data-t="02:07:06">[02:07:06]</a>. For example, evals can test a model's proficiency in creative writing, graduate-level science, or competitive coding <a class="yt-timestamp" data-t="01:19:47">[01:19:47]</a>.

## Why Evals are Important in AI Product Management
The importance of evals stems from the inherent nature of AI models, especially Large Language Models (LLMs), which differ significantly from traditional software <a class="yt-timestamp" data-t="01:17:01">[01:17:01]</a>.

### Understanding Model Reliability
Unlike conventional databases or systems that provide defined outputs for defined inputs, LLMs operate with "fuzzier" inputs and outputs <a class="yt-timestamp" data-t="01:18:03">[01:18:03]</a>. They are adept at handling the nuances of human language but don't always yield the exact same answer even for the same query <a class="yt-timestamp" data-t="01:17:50">[01:17:50]</a>.

For [[impact_of_ai_on_product_management | product managers]], knowing the model's accuracy is critical <a class="yt-timestamp" data-t="01:18:11">[01:18:11]</a>:
*   If a model is 99.5% accurate for a use case, one type of product might be built <a class="yt-timestamp" data-t="01:24:27">[01:24:27]</a>.
*   If it's 95% accurate, a different product design is needed <a class="yt-timestamp" data-t="01:22:22">[01:22:22]</a>.
*   If it's only 60% accurate, the product must be built "totally differently" <a class="yt-timestamp" data-t="01:22:33">[01:22:33]</a>.

Evals provide this crucial understanding, allowing product teams to design experiences that account for the model's performance capabilities <a class="yt-timestamp" data-t="01:18:30">[01:18:30]</a>.

### Continuous Learning and Fine-Tuning
AI models are not static; they can be continuously taught and improved <a class="yt-timestamp" data-t="01:22:12">[01:22:12]</a>. Evals facilitate this continuous learning process. For example, with OpenAI's deep research product, evals were designed simultaneously with the product, transforming "hero use cases" into specific tests <a class="yt-timestamp" data-t="01:21:41">[01:21:41]</a>. By "hill climbing" on these evals, the models could be fine-tuned to perform better on specific queries, like answering complex research questions that would normally take a week to complete <a class="yt-timestamp" data-t="01:22:05">[01:22:05]</a>.

### Unlocking Model Potential
The speaker notes that AI's potential is somewhat "capped" by the quality of evals <a class="yt-timestamp" data-t="01:22:35">[01:22:35]</a>. Models are highly intelligent but require specific data to learn industry-specific or use-case-specific knowledge that isn't publicly available <a class="yt-timestamp" data-t="01:23:58">[01:23:58]</a>. The future of AI will involve "incredibly smart broad base models" that are fine-tuned and tailored with proprietary data <a class="yt-timestamp" data-t="01:24:07">[01:24:07]</a>. Custom evals are essential to measure the performance of these specialized models <a class="yt-timestamp" data-t="01:24:23">[01:24:23]</a>.

## [[Role and impact of AI in product management | Role and Impact of Evals on Product Teams]]
The need for detailed understanding of model performance through evals leads to significant shifts in how [[ai_in_product_management | product management]] teams are structured and operate <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

### Integration of Researchers
In the future, product teams will increasingly include "quasi-researcher" or machine learning engineer types <a class="yt-timestamp" data-t="00:58:37">[00:58:37]</a>. This integration is vital because fine-tuning models will become a core workflow for building most products <a class="yt-timestamp" data-t="00:58:46">[00:58:46]</a>. This iterative feedback loop, where product design and research work as a single team, is crucial for building novel AI products <a class="yt-timestamp" data-t="00:47:19">[00:47:19]</a>.

### Fine-Tuning in Practice
Fine-tuning a model involves providing it with thousands of examples of problems and their corresponding good answers <a class="yt-timestamp" data-t="00:59:29">[00:59:29]</a>. This process teaches the model to be significantly better at particular tasks than its generic version <a class="yt-timestamp" data-t="00:59:49">[00:59:49]</a>.

For instance, OpenAI uses ensembles of models internally, where different models are fine-tuned for specific tasks <a class="yt-timestamp" data-t="01:00:01">[01:00:01]</a>. In customer support, tailored models understand internal resources, knowledge bases, and personality guidelines to automate answers <a class="yt-timestamp" data-t="01:01:52">[01:01:52]</a>. When a model lacks full confidence, it can suggest an answer for human review, and that human correction then serves as fine-tuning data for the model, improving its future performance <a class="yt-timestamp" data-t="01:02:09">[01:02:09]</a>.

This approach reflects how humans solve problems: different individuals (like models) are fine-tuned with different skills, and grouping them together (ensembling) yields better overall results <a class="yt-timestamp" data-t="01:02:51">[01:02:51]</a>.

## Evals and Prompt Engineering
While "prompt engineering" is currently a recognized skill for interacting with LLMs, the speaker believes that if AI developers do their jobs correctly, the need for intricate prompt engineering will diminish <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>. As models become more broadly adopted, users shouldn't need to understand minute prompting details <a class="yt-timestamp" data-t="01:27:32">[01:27:32]</a>.

However, for now, a practical "poor man's fine-tuning" trick is to include examples directly in the prompt <a class="yt-timestamp" data-t="01:27:56">[01:27:56]</a>. By providing "here's an example, here's a good answer" multiple times before asking a question, the model will "listen and learn" from these examples, performing much better than without them <a class="yt-timestamp" data-t="01:28:06">[01:28:06]</a>.