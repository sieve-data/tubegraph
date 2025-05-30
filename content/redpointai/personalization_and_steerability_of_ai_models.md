---
title: Personalization and steerability of AI models
videoId: NNGbaiN1L7Y
---

From: [[redpointai]] <br/> 

Michelle Pokris, Post-Training Research Lead at OpenAI, discusses the focus on real-world utility and developer experience for models like GPT-4.1, shifting away from solely optimizing for benchmarks <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. This focus on utility necessitates strong personalization and steerability features for AI models.

## Prioritizing User Utility and Feedback
The primary goal for models like GPT-4.1 was to be a "joy to use for developers" <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. This contrasts with models optimized only for benchmarks, which might stumble on basic real-world issues like instruction following or formatting <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

To achieve user utility, OpenAI heavily relies on:
*   **User Feedback** Talking to users and gathering their feedback is crucial for identifying key insights and problems <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. This feedback is then transformed into internal evaluations (evals) that can be used during research and development <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   **Internal Usage** OpenAI uses its own models internally and has internal customers building on top of them, providing additional insights into performance <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   **"North Star" Evals** An internal instruction following eval, based on real API usage and user feedback, served as a "north star" during the development of GPT-4.1 <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. However, the shelf life of an eval is short (around three months) due to rapid progress, meaning there's a constant need for new and relevant evaluations <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

> "There's an interesting insight I got recently from talking to a user where it turns out our models could do better on kind of sometimes you want to tell them ignore everything you know about the world and only use the information in context." <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>

## Model Development and Iteration
Shipping a model like GPT-4.1 involves significant work from various teams <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>:
*   **Pre-training:** The three models (standard, mini, nano) are based on "semi-new pre-trains" or "mid-trains," which are freshness updates <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. [[Pretraining and finetuning AI models | Pretraining and finetuning AI models]] is a foundational step.
*   **Post-training:** Michelle's team focuses on post-training, determining the best mix of data, parameters for [[The role of reinforcement and finetuning in AI | reinforcement learning (RL)]] training, and weighting of different rewards <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   **Rapid Iteration:** The process involved months of evaluation setup, followed by a flurry of training experiments, and then alpha testing to incorporate feedback rapidly <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

## Strategies for Personalization and Steerability

### 1. Fine-tuning
[[Finetuning approaches and considerations in AI | Fine-tuning]] has seen a "renaissance" in its perceived helpfulness with newer models <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>.
*   **SFT (Supervised Fine-tuning):** Primarily used for speed and latency improvements. A 4.1 model can be fine-tuned to achieve a fraction of the latency <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>. It's useful for simpler classification tasks or when a small percentage of errors needs to be closed <a class="yt-timestamp" data-t="00:24:13">[00:24:13]</a>.
*   **RFT (Reinforcement Fine-tuning):** This method, based on the same RL process used internally by OpenAI, allows users to "push the frontier in your specific area" <a class="yt-timestamp" data-t="00:22:08">[00:22:08]</a>. It is data-efficient, requiring only hundreds of samples <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>.
    *   **Applications:** RFT is effective for teaching agents specific workflows, decision processes <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>, and deep tech applications where verifiable, unique data is available (e.g., chip design, biology/drug discovery) <a class="yt-timestamp" data-t="00:22:48">[00:22:48]</a>.
*   **Preference Fine-tuning:** Useful for stylistic adjustments to model output <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>.

### 2. Prompting and Instruction Following
Instruction following is one of the "hardest thing to define in ML" because it means hundreds of different things to different people <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
*   **Structured Prompts:** Using XML or well-structured prompts improves model performance <a class="yt-timestamp" data-t="00:28:23">[00:28:23]</a>.
*   **"Keep Going" Prompt:** Explicitly telling the model to "please don't come back to me until you've solved the problem" can lead to "remarkably better performance" <a class="yt-timestamp" data-t="00:28:30">[00:28:30]</a>.
*   **Custom Instructions:** Users can employ custom instructions to tweak the model's personality or behavior, such as avoiding capital letters or follow-up questions <a class="yt-timestamp" data-t="00:39:29">[00:39:29]</a>.

### 3. Enhanced Memory
[[Learning from experience and model personalization | Enhanced memory]] is a powerful lever for personality and personalization <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a>. As a model learns more about a user, it can adapt to their preferences, making the interaction more useful <a class="yt-timestamp" data-t="00:39:13">[00:39:13]</a>. Michelle notes that her ChatGPT experience is "so different from like my mom's or my husband's" due to this personalization <a class="yt-timestamp" data-t="00:39:07">[00:39:07]</a>.

## Challenges and Future Directions
### General vs. Purpose-Built Models
While GPT-4.1 was purpose-built for developers by upweighting coding data and removing chat-specific data <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>, Michelle's general philosophy leans towards making one "general" model (AGI) that simplifies the product offering <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>. Combining capabilities typically produces a much better result due to cross-domain generalization <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.

The challenge for future models like GPT-5 will be to combine different skill sets, such as being a delightful conversationalist while also knowing when to engage in hard reasoning <a class="yt-timestamp" data-t="00:37:57">[00:37:57]</a>.

### Agentic Capabilities and Ambiguity
Agents work "remarkably well in well scoped domains" where tools and user intent are clear <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. The current challenge is bridging the gap to "fuzzy and messy real world" scenarios <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>, where users might not know what the agent can do or the agent lacks awareness of its own capabilities <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.

*   **Improving Ambiguity Handling:** Models need to be more steerable regarding ambiguity—should they ask for more information or proceed with assumptions? <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>
*   **Robustness and "Grit":** On the modeling side, there's a need for more robustness, particularly when external APIs encounter errors. This is referred to as training in more "grit" <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.
*   **Tool Use Generalization:** OpenAI has found that learning to use one set of tools makes a model better at other sets of tools, indicating a strong generalization capability that reduces the need for "tool-specific training" <a class="yt-timestamp" data-t="00:34:21">[00:34:21]</a>.

### Future Research Areas
*   **Models Improving Models:** Using AI models to make other models better, particularly in [[The role of reinforcement and finetuning in AI | reinforcement learning]] for figuring out if a model is on the right track <a class="yt-timestamp" data-t="00:32:04">[00:32:04]</a>. Synthetic data has been an "incredibly powerful trend" in this area <a class="yt-timestamp" data-t="00:33:18">[00:33:18]</a>.
*   **Speed of Iteration:** A focus on improving the speed of running experiments by optimizing GPU usage and ensuring sufficient scale for signal extraction <a class="yt-timestamp" data-t="00:32:26">[00:32:26]</a>.

## Recommendations for Companies
*   **Develop Strong Evals:** The most successful companies know their use case well and have robust evals to quickly test new models when they are released <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>. It's beneficial to break down problems into subcomponents with specific evals to pinpoint what is and isn't working <a class="yt-timestamp" data-t="00:30:21">[00:30:21]</a>.
*   **Adapt Prompts and Scaffolding:** Be prepared to switch prompts and scaffolding to tune them to particular models <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
*   **Build "Just Out of Reach" Features:** Focus on use cases that are "just out of reach" for current models (e.g., working 1 out of 10 times, but capable of 50% with fine-tuning). These are likely to be "crushed" by future models, allowing companies to be first to market <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.
*   **Anticipate [[Future trends in AI and personalization | Future trends in AI and personalization]]:** While building scaffolding to ship value today is essential, always have an eye on future trends like improving context windows, reasoning capabilities, and instruction following <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>. Multimodal capabilities are also rapidly improving and are currently "underhyped" <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>.
*   **AI Expertise for App Companies:** Michelle believes that successful app companies will need "scrappy engineers" who understand the product, rather than deep AI research expertise, as models become easier to combine and use <a class="yt-timestamp" data-t="00:31:31">[00:31:31]</a>.

### Model Selection Guide for [[Enterprise AI model management | Enterprise AI Model Management]]
For enterprise users, Michelle suggests a decision tree for model selection <a class="yt-timestamp" data-t="00:27:31">[00:27:31]</a>:
1.  **Start with GPT-4.1:** See if it meets the use case requirements <a class="yt-timestamp" data-t="00:27:35">[00:27:35]</a>.
2.  **For Speed/Cost Optimization:** If 4.1 works, consider fine-tuning or using smaller models like Mini and Nano for faster and cheaper inference <a class="yt-timestamp" data-t="00:27:39">[00:27:39]</a>.
3.  **For Harder Problems:** If 4.1 is insufficient, try GPT-4 Mini for its reasoning capabilities, then GPT-3, and finally [[The role of reinforcement and finetuning in AI | RFT with GPT-4 Mini]] for frontier pushing in specific domains <a class="yt-timestamp" data-t="00:27:48">[00:27:48]</a>.

<div class="callout">
    <div class="callout-title">
        <div class="callout-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-megaphone"><path d="m3 11 18-8-2 20-16-5a2 2 0 0 1-1.27-2.61L3 11Z"/><path d="M12 11h9"/><path d="M7 21h10"/></svg>
        </div>
        <div class="callout-title-inner">Overhyped vs. Underhyped</div>
    </div>
    <div class="callout-content">
        <p>
            **Overhyped:** Benchmarks, especially agentic ones that are saturated or presented with unrealistic numbers <a class="yt-timestamp" data-t="00:43:38">[00:43:38]</a>.
        </p>
        <p>
            **Underhyped:** Companies' own internal evals using real usage data to understand model performance <a class="yt-timestamp" data-t="00:43:55">[00:43:55]</a>.
        </p>
    </div>
</div>