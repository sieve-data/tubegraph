---
title: Safety and helpfulness in AI models
videoId: 1ZwXkw9_Xq8
---

From: [[hu-po]] <br/> 

The Llama 2 paper extensively details Meta's approach to incorporating and evaluating safety and helpfulness in their large language models (LLMs) [[00:04:27]]. These two attributes are crucial for the responsible [[Ethical considerations and societal impacts of AI simulations | development of LLMs]] and their widespread adoption [[00:04:32], [00:15:14]].

## Defining Safety and Helpfulness

*   **Helpfulness** refers to how well Llama 2 Chat responses fulfill user requests and provide the desired information [[01:16:16]].
*   **Safety** refers to whether Llama 2 Chat responses are unsafe, such as providing detailed instructions on making a bomb [[01:12:24]].

These two objectives can sometimes conflict, as being maximally helpful might lead to unsafe responses, while being maximally safe might lead to excessive refusal of legitimate queries [[01:27:53]].

## Evaluation Methods

Meta employs various methods to evaluate the helpfulness and safety of Llama 2 models:

### Human Evaluation
Human evaluation is considered the gold standard for assessing LLMs [[01:27:00]].

*   **Helpfulness:** Human raters compare model generations on around 4,000 prompts, including single and multi-turn conversations [[00:08:15]]. Llama 2 models generally outperform other open-source chat models like Falcon 40B on these benchmarks [[00:09:04], [00:09:09]]. Llama 2 70B performs on par with Google's PaLM Bison and close to ChatGPT-3 [[00:09:38], [00:10:41]].
*   **Safety:** Human raters judge model generations for safety violations across 2,000 adversarial prompts [[01:16:31]]. Llama 2 Chat models consistently show a lower safety violation rate compared to other models like Falcon and ChatGPT-3 [[01:17:52]].
*   **Inter-rater Reliability (IRR):** To ensure consistency, three different human annotators provide independent assessments for each model generation comparison. An IRR score between 0.37 and 0.5 was observed, indicating varying levels of agreement among human evaluators [[01:56:55], [01:57:31]].

### Model-Based Evaluation (using GPT-4)
GPT-4 is also used as a "more capable model" to evaluate Llama 2's performance against commercially licensed baselines [[01:11:44]].

*   Llama 2 is found to be better than GPT-3, PaLM Bison, and Falcon 40B in terms of both helpfulness and safety when judged by GPT-4 [[01:22:22]].
*   However, concerns exist regarding potential biases in GPT-4's evaluation, as it has been shown to be influenced by the order of responses [[01:13:05], [01:13:19]].

### Specific Benchmarks
Llama 2 is evaluated against various academic benchmarks covering world knowledge, reading comprehension, and common sense reasoning [[00:59:02]].

*   **GSM8K (Grade School Math):** Llama 2 performs significantly worse than GPT-4 on math word problems, suggesting [[Model Architecture and Data Quality in AI | model architecture and data quality in AI]] differences or optimization strategies. Notably, GPT-3.5 performs similarly to Llama 2 on this benchmark [[01:01:16], [01:01:21]].
*   **Toxigen:** Llama 2 Chat shows very good performance on the Toxigen benchmark, which measures the prevalence of toxicity [[02:03:37], [02:19:41]].
*   **TruthfulQA:** Llama 2 Chat is less proficient on the TruthfulQA benchmark, which assesses factual accuracy and resistance to generating falsehoods [[02:04:34], [02:19:43]].

## Techniques for Improvement

### [[Selfimprovement in AI models | Reinforcement Learning from Human Feedback (RLHF)]]
RLHF is a core training procedure applied to fine-tuned language models to align them with human preferences [[01:10:36]].

*   **Reward Model Training:** Human annotators select preferred model outputs from binary comparisons, and this feedback is used to train a separate neural network called a "reward model" [[01:10:51], [01:11:02]]. This model learns patterns in human preferences and automates preference decisions [[01:11:10]].
*   **Separate Reward Models:** Meta trains two distinct reward models: one optimized for helpfulness and another for safety, to address the inherent trade-off between the two objectives [[01:17:33]].
*   **Iterative Fine-tuning:** Successive versions of RLHF models (V1 to V5) are trained by iteratively collecting more human preference data and using the latest Llama 2 Chat iterations to gather new preference data [[01:29:00], [01:14:11]]. This self-labeling strategy, where the model's output is used to generate more training data, has also been observed in other Meta models like Segment Anything [[01:29:46]].
*   **PPO Algorithm:** Proximal Policy Optimization (PPO), a robust reinforcement learning algorithm, is used to optimize the Llama 2 models based on the reward models [[01:30:16]].

### Supervised Fine-tuning (SFT)
SFT involves training the model with explicit input-output pairs where the "answer" is provided [[01:09:07]].

*   Meta started the SFT stage with publicly available instruction tuning data but found it lacked diversity and quality for dialogue alignment [[01:05:22], [01:05:38]].
*   They focused on collecting several thousand examples of high-quality SFT data from their own vendor-based annotation efforts [[01:05:44], [01:06:26]]. This data is created by humans, rather than merely "collected" [[01:06:10]].
*   A limited set of clean instruction tuning data is found to be sufficient for achieving a high level of quality [[01:06:33]].

### Safety Context Distillation
This technique refines the RLHF pipeline by generating safer model responses. It involves:
1.  Prefixing a prompt with a safety prompt (e.g., "You are a safe and responsible assistant") [[02:05:17]].
2.  Generating a safer response.
3.  Fine-tuning the model on these safer responses *without* the pre-prompt, effectively "distilling" the safety prompt's effect into the model itself [[02:05:25]].

### Ghost Attention (GAtt)
To address the issue of LLMs forgetting initial instructions in multi-turn dialogues, Meta introduced Ghost Attention [[01:43:23]]. This involves synthetically concatenating the original system instruction to all user messages in a conversation during training. This ensures the model continuously "pays attention" to the initial instruction, even across many turns [[01:44:11], [01:49:35]].

## [[Challenges and implications for AI safety | Challenges and Trade-offs]]

*   **Bias in Pre-training Data:** Llama 2's pre-training data, while publicly available and not from Meta's products, still reflects real-world biases (e.g., gender pronouns associated with professions) [[01:58:12], [01:59:50]]. Deciding whether to synthetically balance data to mitigate these biases or to allow the model to reflect real-world distributions is a complex [[Ethical considerations and societal impacts of AI simulations | ethical consideration]] [[02:01:22]].
*   **False Refusals:** Models can sometimes incorrectly refuse to answer legitimate user prompts, especially if the prompt contains words frequently associated with unsafe generations (e.g., "bomb" in "bath bomb") [[02:09:20], [02:09:54]].
*   **"Stupider" Models:** Excessive safety mitigation can lead to models becoming overly conservative and less helpful, potentially making them appear "stupider" over time [[02:08:46]].
*   **Proprietary Cleaning Processes:** Even when using publicly available data, companies perform their own internal data cleaning, which creates unique proprietary datasets that are not fully transparent [[02:45:30]].

## Red Teaming

Meta conducts extensive proactive risk identification, known as "red teaming," where internal and external teams (including 350 people with expertise in cybersecurity, ethics, civil rights, etc.) attempt to make the model generate unsafe content [[02:12:05], [02:12:30], [02:12:40]].

*   Red teaming revealed that early models might generate unsafe responses without recognizing the problematic content, while later models tend to display knowledge of the issue, even if they still provide the content [[02:15:15]].
*   A common strategy to bypass safety filters is to "hide" requests in language that is positive, progressive, and empowering, or in creative writing prompts [[02:15:45], [02:15:35]].

## Meta's Philosophy on Open Release

Meta's decision to release Llama 2 models for both research and commercial use is a strategic move to encourage responsible [[Ethical considerations and societal impacts of AI simulations | AI innovation]] [[02:34:04], [02:34:25]].

*   **Transparency:** Open releases promote transparency, allowing more people to access and rigorously analyze the models for risks and potential misuse [[02:35:13], [02:35:16], [02:37:19]].
*   **Collaboration:** Meta believes that an open approach draws upon the collective wisdom and diversity of the AI practitioner community, fostering real collaboration beyond the walls of big tech companies [[02:34:31], [02:35:00]].
*   **Innovation and Progress:** The decentralization of AI expertise stimulates innovation and accelerates progress, as smaller businesses can leverage these models without duplicating expensive training costs [[02:35:23], [02:35:41], [02:36:02]].
*   Meta acknowledges the risks of misuse and toxic content generation but views open science and collaboration as the best path to mitigation [[02:36:10], [02:36:25]].

> [!INFO] Llama 2 Models
> Llama 2 models are available in various scales from 7 billion to 70 billion parameters [[00:36:00], [00:55:00]]. The 13B model is often considered a "sweet spot" for performance and local usability [[02:42:41]]. The 34B model was reported in evaluations but not released due to a lack of time for sufficient red teaming [[00:09:24], [02:53:35]].