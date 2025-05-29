---
title: The role of evaluations evals in AI product management
videoId: scsW6_2SPC4
---

From: [[lennyspodcast]] <br/> 

In the rapidly evolving landscape of artificial intelligence, the concept of "evals" has emerged as a crucial component for product development. As technology progresses at an unprecedented pace, with new capabilities emerging every couple of months, understanding and utilizing evaluations is becoming a core skill for product builders <a class="yt-timestamp" data-t="01:14:16">[01:14:16]</a>.

## What are Evals?
Evals, or evaluations, can be thought of as a "quiz for a model" or "a test to gauge how much it, how well it knows a certain set of subject material or how good it is at responding to a certain set of questions" <a class="yt-timestamp" data-t="01:57:57">[01:57:57]</a>. They function similarly to "unit tests for models," providing benchmarks for a model's intelligence and capability <a class="yt-timestamp" data-t="02:04:04">[02:04:04]</a>. These tests assess a model's proficiency in various areas, such as creative writing, graduate-level science, or competitive coding <a class="yt-timestamp" data-t="01:57:57">[01:57:57]</a>.

## Why Evals are Crucial for AI Product Development
Unlike traditional software development where underlying technology is relatively fixed (e.g., databases improving by only 5% over two years) <a class="yt-timestamp" data-t="01:53:07">[01:53:07]</a>, [[AI in product management | AI models]] are constantly advancing. This necessitates a fundamental shift in how products are built <a class="yt-timestamp" data-t="01:53:07">[01:53:07]</a>.

Evals are critical because they determine the viability and design of a product based on the model's performance <a class="yt-timestamp" data-t="02:21:51">[02:21:51]</a>:
*   **Confidence in Model Performance**: Knowing whether a model is 60%, 95%, or 99.5% accurate on a specific task dictates how a product is built <a class="yt-timestamp" data-t="02:21:51">[02:21:51]</a>. For instance, a 60% accuracy rate requires a vastly different product design than a 99.5% rate <a class="yt-timestamp" data-t="02:33:35">[02:33:35]</a>.
*   **Continuous Learning**: Evals are not static. They enable a continuous learning process, allowing developers to fine-tune models to improve performance on specific use cases <a class="yt-timestamp" data-t="02:12:12">[02:12:12]</a>. This means a model can be taught and refined over time <a class="yt-timestamp" data-t="02:12:12">[02:12:12]</a>.
*   **Fuzzy Inputs and Outputs**: Unlike traditional software with defined inputs and outputs, [[AI in product management | AI models]], especially Large Language Models (LLMs), handle fuzzy, subtle human language nuances <a class="yt-timestamp" data-t="01:44:45">[01:44:45]</a>. Evals help manage this variability, where models might not give the exact same answer every time but "spiritually the same answer" <a class="yt-timestamp" data-t="01:44:45">[01:44:45]</a>.

## Evals in Practice: The Deep Research Product Example
For products like OpenAI's Deep Research feature, evals are designed simultaneously with the product vision <a class="yt-timestamp" data-t="02:07:09">[02:07:09]</a>. This involves:
1.  **Identifying Hero Use Cases**: Defining specific, complex questions that users should be able to ask and the ideal answers for those questions <a class="yt-timestamp" data-t="02:16:19">[02:16:19]</a>.
2.  **Turning into Evals**: Converting these ideal scenarios into evaluation tests <a class="yt-timestamp" data-t="02:20:05">[02:20:05]</a>.
3.  **Hill Climbing**: Iteratively testing and improving the model's performance on these evals, using the results to fine-tune the model <a class="yt-timestamp" data-t="02:20:05">[02:20:05]</a>. This feedback loop ensures the model gets better at the intended use cases <a class="yt-timestamp" data-t="02:20:05">[02:20:05]</a>.

## Evals as a Core Skill for Product Builders
The ability to write effective evals is "quickly becoming a core skill for product builders" <a class="yt-timestamp" data-t="01:14:16">[01:14:16]</a>. This is because:
*   **Model Intelligence and Knowledge**: AI models are "incredibly smart, very like factually aware intelligences" <a class="yt-timestamp" data-t="02:29:29">[02:29:29]</a>, but much of the world's data and processes are not publicly available <a class="yt-timestamp" data-t="02:30:29">[02:30:29]</a>.
*   **Teaching the Model**: Just as a new employee needs onboarding and access to company-specific data, models need "raw data" to learn from <a class="yt-timestamp" data-t="02:37:37">[02:37:37]</a>. Product managers, through evals, guide this learning process, enabling models to perform well on "company-specific or use case specific things" <a class="yt-timestamp" data-t="02:44:07">[02:44:07]</a>.
*   **Customization**: Evals are essential for customizing models to specific industries or companies, as many use cases are unique and not covered in general training data <a class="yt-timestamp" data-t="02:44:07">[02:44:07]</a>.

## The Impact on Model Capabilities and the Future of Product Teams
Evals are integral to the specialization and improvement of [[AI in product management | AI models]]:
*   **Multi-Dimensional Intelligence**: Models excel in different areas (e.g., competitive coding vs. front-end coding) <a class="yt-timestamp" data-t="02:28:50">[02:28:50]</a>. Evals help identify and target these specific dimensions for improvement.
*   **Fine-Tuned Models**: The future will involve "incredibly smart broad base models that are fine-tuned and tailored with company specific or use case specific data" <a class="yt-timestamp" data-t="02:44:07">[02:44:07]</a>. Fine-tuning involves providing thousands of "problem, good answer" examples to teach the model to excel at specific tasks <a class="yt-timestamp" data-t="02:59:29">[02:59:29]</a>.
*   **Ensembles of Models**: Companies internally use "ensembles of models" much more than public perception suggests <a class="yt-timestamp" data-t="01:00:01">[01:00:01]</a>. This means different models (potentially fine-tuned or of varying sizes/costs) are used for specific parts of a problem, with a final model integrating their outputs <a class="yt-timestamp" data-t="01:00:01">[01:00:01]</a>. This mirrors how human teams with diverse skills collaborate to solve problems <a class="yt-timestamp" data-t="01:02:53">[01:02:53]</a>.
*   **Product Team Structure**: This shift implies that product teams will increasingly include "quasi researcher machine learning engineer types" because fine-tuning models will become a core workflow for building most products <a class="yt-timestamp" data-t="02:58:28">[02:58:28]</a>.

While prompt engineering is currently important, the long-term goal is for models to become so advanced that users won't need detailed knowledge of prompting <a class="yt-timestamp" data-t="02:59:52">[02:59:52]</a>. However, for now, including examples within prompts can act as a "poor man's fine-tuning," significantly improving model responses <a class="yt-timestamp" data-t="02:59:52">[02:59:52]</a>.