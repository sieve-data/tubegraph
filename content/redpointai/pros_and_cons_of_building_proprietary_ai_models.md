---
title: Pros and cons of building proprietary AI models
videoId: n6PazYmo_Qo
---

From: [[redpointai]] <br/> 

Building proprietary AI models involves creating and maintaining an organization's own artificial intelligence models rather than relying exclusively on commercial or third-party solutions. This approach comes with distinct advantages and disadvantages, particularly concerning customization, control, and cost <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>.

## Pros of Building Proprietary AI Models

### Tailored Characteristics and Performance
One significant advantage is the ability to achieve specific model characteristics that off-the-shelf commercial models may not offer <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>. For companies like Replit, low latency is crucial for features like code suggestions, which may not be consistently met by general-purpose commercial models <a class="yt-timestamp" data-t="00:30:10">[00:30:10]</a>.

### Cost Efficiency
While the initial investment might seem substantial (e.g., $100,000 for training a 3B parameter model at Replit <a class="yt-timestamp" data-t="00:29:37">[00:29:37]</a>), building a proprietary model can be more cost-effective in the long run than being a continuous customer of commercial models, especially if the features need to be part of a free offering <a class="yt-timestamp" data-t="00:28:56">[00:28:56]</a> <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>. Small models, in particular, can be both capable and affordable to train and deploy <a class="yt-timestamp" data-t="00:29:17">[00:29:17]</a> <a class="yt-timestamp" data-t="00:29:27">[00:29:27]</a>.

### Control Over Data and Training
Proprietary models offer complete control over the training data and process. This is vital because [[the_future_of_ai_models_and_open_source_development | LLMs]] are fundamentally a function of the data they are fed, making the data akin to the "source code" <a class="yt-timestamp" data-t="01:12:17">[01:12:17]</a> <a class="yt-timestamp" data-t="00:35:12">[00:35:12]</a>.
Control over the data means:
*   **Quality Improvement**: The ability to curate high-quality, diverse, and fresh data, even performing multiple training epochs on the same high-quality data for better performance <a class="yt-timestamp" data-t="01:16:35">[01:16:35]</a>.
*   **Domain Specificity**: Training on specific types of data (e.g., application code from Replit's user base, rather than just infrastructure code from GitHub) can yield better results for particular use cases <a class="yt-timestamp" data-t="01:18:14">[01:18:14]</a>.
*   **Security**: Understanding the training process and data mitigates significant security risks, such as hidden "backdoors" that could be activated by certain prompts <a class="yt-timestamp" data-t="00:36:51">[00:36:51]</a> <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.

### Strategic and Talent Development
[[building_custom_ai_models_for_enterprises | Building custom AI models for enterprises]] allows companies to develop internal AI talent and position themselves as an "AI company," which can be a strong strategic consideration <a class="yt-timestamp" data-t="00:29:45">[00:29:45]</a> <a class="yt-timestamp" data-t="00:30:37">[00:30:37]</a>.

## Cons of Building Proprietary AI Models

### Capital and Resource Intensity
While it can be cost-effective for specific use cases like Replit's, training large, general-purpose models requires substantial capital expenditure on compute and data annotation <a class="yt-timestamp" data-t="00:29:40">[00:29:40]</a> <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>. The rapid affordability of commercial models like GPT-3.5 makes the decision to train internally less universally rational for many companies <a class="yt-timestamp" data-t="00:27:59">[00:27:59]</a>.

### Limited True Openness and Dependence
The concept of "[[open_source_ai_models_and_limitations | open source AI models]]" is debated. If a model's training process cannot be reproduced, or if the compiler for its source code is unavailable, it's not truly open source <a class="yt-timestamp" data-t="00:31:58">[00:31:58]</a> <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>. This means companies relying on open source models might still be dependent on the "goodwill" of the releasing entity (e.g., Meta for Llama) and their continued investment <a class="yt-timestamp" data-t="00:32:30">[00:32:30]</a>. Strategically, long-term dependence on such external factors without control over the underlying data or training process can be risky <a class="yt-timestamp" data-t="00:33:22">[00:33:22]</a>.

### Competition with Giants
Companies building proprietary models face stiff competition from major players like Microsoft and OpenAI, who have vast resources, established install bases, sales teams, and continuous advancements in their models <a class="yt-timestamp" data-t="00:52:01">[00:52:01]</a>. It's challenging for smaller entities to match the scale, compute, and comprehensive data collection of these large labs <a class="yt-timestamp" data-t="00:54:37">[00:54:37]</a>.

### Staying Ahead of Model Advancements
The rapid pace of AI model development means a proprietary model, once built, risks being leapfrogged by subsequent releases from major labs <a class="yt-timestamp" data-t="00:54:56">[00:54:56]</a>. This requires continuous investment in research and development to maintain competitiveness <a class="yt-timestamp" data-t="00:56:18">[00:56:18]</a>.

## Hybrid Approach
Many companies adopt a hybrid strategy, using proprietary models for core, latency-sensitive features and leveraging commercial models for other use cases that don't require the same specific characteristics <a class="yt-timestamp" data-t="00:30:10">[00:30:10]</a> <a class="yt-timestamp" data-t="00:31:10">[00:31:10]</a>. This allows companies to "start from the problem, from the customer pain point, explore potential solutions, run the numbers," and make strategic investments where it makes the most sense <a class="yt-timestamp" data-t="00:30:24">[00:30:24]</a>.

The landscape for [[the_future_of_ai_models_and_open_source_development | AI models]] is not yet set, with ongoing debates about the long-term viability of relying solely on commercial APIs versus the strategic advantage of internal model development <a class="yt-timestamp" data-t="00:33:55">[00:33:55]</a>.