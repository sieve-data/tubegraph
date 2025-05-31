---
title: Challenges and opportunities in AI model development and infrastructure
videoId: JW6DiD_V9hk
---

From: [[redpointai]] <br/> 

DeepL, an AI translation company with a $2 billion valuation, supports over 100,000 businesses worldwide <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. CEO and founder Jarek Kutylowski discusses the [[Challenges and opportunities in AI development | challenges and opportunities in AI model development and infrastructure]], drawing from DeepL's extensive experience in cutting-edge AI research prior to the widespread adoption of large language models (LLMs) <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Evolution of AI Models and Infrastructure

The release of models like ChatGPT significantly increased public awareness of AI's capabilities <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. DeepL had been building language models as part of their translation solutions for a while, so the academic surprise wasn't significant, but the "magic" aspect and increased public understanding were notable <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. The advent of LLM technology allows DeepL to bring the next level of translation to users, enabling more interactivity between humans and AI <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

### Specialized vs. General Models

A key perspective from DeepL is the emphasis on specialized models over generalized ones <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. For high-value use cases, particularly for businesses, specialized models prove to be more effective <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. While general models are useful, there are many areas where building specialized solutions is financially impractical, especially for long-tail use cases where companies cannot afford the significant compute resources for training <a class="yt-timestamp" data-t="00:36:34">[00:36:34]</a>. However, for critical applications like translation, specialized models are seen as making a lot of sense <a class="yt-timestamp" data-t="00:37:14">[00:37:14]</a>.

DeepL aims for models that are smarter and require less compute, focusing on architectural improvements similar to the impact of the Transformer architecture <a class="yt-timestamp" data-t="00:25:10">[00:25:10]</a>. While large general AI players might not be incentivized to invest in smaller, more efficient models due to their "monopoly on huge compute," it falls to specialized players like DeepL to innovate in this area <a class="yt-timestamp" data-t="00:25:32">[00:25:32]</a>.

### Vertical Integration and Full Stack Ownership

DeepL has adopted a "build it yourself" philosophy, owning the entire vertical stack from product and go-to-market to engineering and research <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. This comprehensive ownership allows for better identification and resolution of problems that might be missed with prompt engineering alone. Having control over model parameters, training, and architecture enables more effective problem-solving for customers <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. An example of this benefit is DeepL's ability to allow customers to embed terminology into models, a crucial feature for businesses that other translation providers have struggled to integrate effectively <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

## Challenges in AI Model Training and Scalability

### Data Scarcity and Language Pairs
A significant [[Challenges in AI model training and scalability | challenge in AI model training and scalability]] arises from the varying sizes of available datasets for different language pairs <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>. For example, there's much more translated material for German-English than Polish-English <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. This disparity means that model sizes and architectures might differ, and it can be more efficient from an inference compute perspective to use smaller models optimized for individual language pairs <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.

### Data Labeling and Human Input
The influence of human data has consistently risen in AI development and is expected to become even more crucial <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. DeepL has run large-scale data annotation projects internally for years, utilizing human translators to train models and ensure quality assurance <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>. This in-house approach ensures top-notch quality, which is vital for specialized models where customer expectations for consistent quality are high <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>. While DeepL is considering outsourcing parts of this process, the decision hinges on the level of control and quality required for specific tasks <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.

### Innovation and Iteration
Being an innovative, cutting-edge company means embracing the process of "throwing away a lot of results" <a class="yt-timestamp" data-t="00:20:32">[00:20:32]</a>. This can happen due to competition or internal research revealing better approaches. Even failed attempts in creating new model architectures provide valuable understanding of the problem, contributing to overall progress <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>. For instance, DeepL experimented with building custom models for individual customers, a historical practice in the translation industry, but found that the overall quality of out-of-the-box translation models has surpassed any gains from such bespoke solutions <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>. This indicates that constant evaluation and adaptation are necessary in a rapidly evolving field.

## Infrastructure and GPU Compute

### Data Centers vs. Hyperscalers
DeepL has operated its own data centers since its inception, largely because no other viable options were available at the time <a class="yt-timestamp" data-t="00:27:07">[00:27:07]</a>. While hyperscalers are excellent for starting and can provide a good kickstart, for companies reaching DeepL's scale, running their own data centers offers significant cost advantages and hardware availability for the newest GPU technology <a class="yt-timestamp" data-t="00:29:15">[00:29:15]</a>. This ensures faster access to cutting-edge hardware, which is crucial for staying competitive <a class="yt-timestamp" data-t="00:29:20">[00:29:20]</a>.

However, operating in-house infrastructure is more complex and can slow down development <a class="yt-timestamp" data-t="00:29:49">[00:29:49]</a>. DeepL is transitioning large parts of its stack towards hybrid cloud solutions, only keeping critical operations (for efficiency or security reasons) on-premise in their own data centers <a class="yt-timestamp" data-t="00:29:54">[00:29:54]</a>.

### Scarcity of GPU Compute
A major challenge is the scarcity of GPUs and GPU-like solutions <a class="yt-timestamp" data-t="00:26:23">[00:26:23]</a>. The tooling and platforms for GPU compute are still in their early stages. Unlike general-purpose CPU computing, where abstraction layers don't incur significant costs, GPU compute is scarce, powerful, and expensive. This necessitates optimizing operations for sustainability, both environmentally and commercially <a class="yt-timestamp" data-t="00:28:16">[00:28:16]</a>.

## The Future of AI Models

### Synchronous Speech Translation
DeepL is excited about the next frontier in translation: spoken language and voice <a class="yt-timestamp" data-t="00:39:14">[00:39:14]</a>. While AI-based text translation has significantly changed how content is consumed, real-time conversational translation is not yet seamless <a class="yt-timestamp" data-t="00:39:40">[00:39:40]</a>. Achieving synchronous speech translation would transform business operations, allowing globally distributed teams to communicate in their native languages in real-time, bridging language gaps for education, learning resources, and knowledge sharing <a class="yt-timestamp" data-t="00:40:50">[00:40:50]</a>.

Key [[Challenges and opportunities in AI development | technical challenges]] to overcome for synchronous speech translation include:
*   **Latency**: Ensuring real-time processing <a class="yt-timestamp" data-t="00:46:03">[00:46:03]</a>.
*   **Ambiguity and Unstructured Language**: Spoken language is often casual, unstructured, and filled with ambiguities, unlike written text. Models need to be taught to translate different types of spoken language <a class="yt-timestamp" data-t="00:46:10">[00:46:10]</a>.

### Impact on Language Learning
The availability of advanced AI translation tools raises questions about the future of human language learning <a class="yt-timestamp" data-t="00:41:47">[00:41:47]</a>. While AI might reduce the business requirement to learn multiple languages, potentially leading to fewer people learning them for practical purposes, Kutylowski believes personal interest and cultural connection will still drive language acquisition <a class="yt-timestamp" data-t="00:43:40">[00:43:40]</a>. Learning languages remains valuable for brain development and provides an enjoyable intellectual challenge, similar to playing chess despite AI's superiority in the game <a class="yt-timestamp" data-t="00:43:56">[00:43:56]</a>.

## Lessons from DeepL's Journey

### Beating Tech Giants
DeepL attributes its success against giants like Google Translate to intense focus on the market, continuous innovation, and building strong academic-level research within the company while specializing in high-value business translation <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. Being established in Europe, a hub of diverse languages, fostered a deep understanding and motivation within the team <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

### Beyond Technology Alone
Early on, Kutylowski believed that strong technology alone would suffice <a class="yt-timestamp" data-t="00:49:43">[00:49:43]</a>. However, he learned that to deploy technology effectively, especially in AI, a broader approach is necessary, encompassing product development, commercialization, and understanding the "big picture" <a class="yt-timestamp" data-t="00:49:56">[00:49:56]</a>.

### Evaluation of Models
Evaluating AI translation models involves both synthetic metrics (like BLEU score) and human evaluation <a class="yt-timestamp" data-t="00:34:05">[00:34:05]</a>. While synthetic metrics are useful for rough orientation during training, they quickly become insufficient as quality improves <a class="yt-timestamp" data-t="00:34:25">[00:34:25]</a>. The "real test" is human evaluation, where thousands of translators judge translations for accuracy, nuance, and native feel, often in a comparative way against other models <a class="yt-timestamp" data-t="00:34:55">[00:34:55]</a>. This is particularly relevant for business translations, which prioritize accuracy and fluency over subjective literary beauty <a class="yt-timestamp" data-t="00:33:19">[00:33:19]</a>.

The [[Challenges and strategies in deploying AI models for developers | challenges of building AI infrastructure companies]] are evident in DeepL's journey, highlighting the need for specialized solutions, robust data pipelines, and a flexible infrastructure strategy to manage evolving AI capabilities and market demands.