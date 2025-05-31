---
title: Customer feedback and AI model refinement
videoId: lwtU_NfFH8o
---

From: [[redpointai]] <br/> 

Adobe leverages its millions of users to refine its AI models, ensuring they meet user expectations and maintain high standards of safety and quality <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This extensive user engagement provides crucial data for [[evaluation_methodologies_and_user_feedback_for_ai_models | model refinement]] and improvement.

## Data Collection and User Feedback Mechanisms

Adobe's terms of use for platforms like Firefly.com allow the company to store user prompts and the resulting generated images <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. This data is then used in [[finetuning_and_reinforcement_learning_techniques_for_ai | training]] their models, which is essentially their way of doing reinforcement learning from human feedback (RHF) <a class="yt-timestamp" data-t="00:34:05">[00:34:05]</a>.

Key feedback mechanisms include:
*   **Direct Feedback** Beta customers on Firefly.com can explicitly provide feedback on what they like or dislike, and report issues like bias or harmful content <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a>. This explicit feedback includes "like/dislike" and "report" signals <a class="yt-timestamp" data-t="00:34:18">[00:34:18]</a>.
*   **Implicit Signals** Actions such as downloading, saving, or sharing generated content are strong implicit signals indicating a user liked a particular generation <a class="yt-timestamp" data-t="00:34:25">[00:34:25]</a>.
*   **Inspiration Stream** Users can submit their own creations to an inspiration stream, which is then curated by Adobe's design team to showcase the best examples for new users to build upon <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a><a class="yt-timestamp" data-t="00:20:46">[00:20:46]</a>. This allows new users to find something they like and start "riffing from it," seeing the prompt and making their own variations <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.

## Model Refinement through Feedback

The collected feedback, both explicit and implicit, is logged and integrated into the feedback loop for future [[ai_model_pretraining_and_finetuning_decisions | model training]] <a class="yt-timestamp" data-t="00:34:32">[00:34:32]</a>. This process teaches the generative models to produce content that users prefer and to avoid generating content that users dislike <a class="yt-timestamp" data-t="00:34:40">[00:34:40]</a>.

### Addressing Bias and Harmful Content
A significant aspect of model refinement is addressing bias and harmful content. Adobe trains its Firefly models exclusively on data from Adobe Stock, which undergoes both automated and manual curation to ensure high-quality and compliant content <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a><a class="yt-timestamp" data-t="00:27:25">[00:27:25]</a>. This process helps reduce the risk of harmful or infringing content being generated <a class="yt-timestamp" data-t="00:27:39">[00:27:39]</a>.

Despite data curation, inherent biases can exist <a class="yt-timestamp" data-t="00:28:07">[00:28:07]</a>. Adobe conducts extensive internal testing with tens of thousands of employees to stress-test models and identify areas for improvement regarding bias and harm <a class="yt-timestamp" data-t="00:28:29">[00:28:29]</a>.

Specific methods for debiasing include:
*   **Person Detector** A model detects if a prompt references a person, especially in relation to a job <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>.
*   **Distribution Adjustment** To counter bias (e.g., a "lawyer" prompt generating only older Caucasian males), the model introduces a fair distribution of skin tones, genders, and age groups based on the country of origin of the request <a class="yt-timestamp" data-t="00:29:52">[00:29:52]</a>.
*   **Toxicity Detectors and Filters** Various toxicity detector models, deny lists, and block lists are employed to prevent the generation of "not safe for work" content <a class="yt-timestamp" data-t="00:31:01">[00:31:01]</a>. NSFW filters are also applied at the end of the generation process <a class="yt-timestamp" data-t="00:31:13">[00:31:13]</a>.
*   **Child-Referencing Systems** Specialized systems detect prompts referencing children and implement negative prompting to avoid generating inappropriate content in relation to them (e.g., children with tobacco) <a class="yt-timestamp" data-t="00:31:31">[00:31:31]</a>.

This combination of [[posttraining_model_optimization_in_ai | machine learning models]], algorithms, and rules helps continuously refine the output, although the process is acknowledged as not perfect <a class="yt-timestamp" data-t="00:31:49">[00:31:49]</a>. User feedback continues to provide new training data points for these rules and models <a class="yt-timestamp" data-t="00:32:11">[00:32:11]</a>.

> [!NOTE] Differentiating Content
> Adobe ensures that models are not trained on customer data stored in Creative Cloud, which might contain proprietary brand campaigns. Instead, they focus on Adobe Stock data and potentially licensed museum/art content <a class="yt-timestamp" data-t="00:33:33">[00:33:33]</a>.

## Organizational Structure for AI Refinement

Adobe employs a hybrid organizational structure that supports continuous AI model refinement:
*   **Horizontal AI Teams** Adobe Research, part of the CTO organization, conducts foundational research across modalities (images, video, vector, 3D) and publishes papers <a class="yt-timestamp" data-t="00:41:52">[00:41:52]</a>. The Sensei team provides a horizontal, distributed training platform and curated high-quality data sets for both research and applied research <a class="yt-timestamp" data-t="00:42:19">[00:42:19]</a>.
*   **Applied Research** Once models are ready for pre-production, they move to applied research groups. Here, models are refined, which can involve additional training or even architectural changes, preparing them for productization <a class="yt-timestamp" data-t="00:42:50">[00:42:50]</a><a class="yt-timestamp" data-t="00:39:51">[00:39:51]</a>.
*   **Gen Services Team** This team creates services that run the refined models efficiently, building optimized inference platforms and APIs for product teams <a class="yt-timestamp" data-t="00:43:09">[00:43:09]</a>.
*   **Vertical "Tech Transfer" Subgroups** Within each product line (e.g., Photoshop, Adobe Express, Illustrator), there are "Tech Transfer" subgroups. These teams leverage the APIs and services from the horizontal teams to build tailored user experiences around the AI capabilities, acting as product experts <a class="yt-timestamp" data-t="00:44:19">[00:44:19]</a>. This approach allows product teams to focus on core workflows that benefit most from AI <a class="yt-timestamp" data-t="00:44:42">[00:44:42]</a>.

This "AI Super Highway" model, which acts as a managed model zoo, accelerates innovation and the transfer of advanced AI capabilities to customers <a class="yt-timestamp" data-t="00:45:01">[00:45:01]</a>.