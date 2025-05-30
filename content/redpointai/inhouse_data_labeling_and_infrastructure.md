---
title: Inhouse Data Labeling and Infrastructure
videoId: JW6DiD_V9hk
---

From: [[redpointai]] <br/> 

DeepL, a company founded by Yarkovsky, which was recently valued at $2 billion and serves over 100,000 businesses globally in AI translation, has been involved in cutting-edge AI research long before its recent surge in popularity <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The company's unique approach to building its own [[ai_infrastructure_and_data_center_challenges | data centers]] and managing [[data_labeling_and_the_role_of_synthetic_data_in_ai | data labeling]] in-house has been central to its success against larger competitors like Google Translate <a class="yt-timestamp" data-t="00:22:22">[00:22:22]</a>.

## In-house Data Labeling

DeepL emphasizes the increasing importance of human data in AI development, especially with the rise of reinforcement learning in Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. The company has run large-scale [[data_labeling_and_the_role_of_synthetic_data_in_ai | data annotation]] projects internally for years, utilizing human translators to train models and ensure quality assurance <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.

This in-house approach is deemed crucial for the specialized models DeepL builds, where customers have high expectations for consistent quality <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.

### Role of Human Translators
DeepL works with thousands of human translators globally <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>. The company prioritizes hiring native speakers for specific language translations, such as Brazilian Portuguese for Brazilian Portuguese <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>. These translators help in two key ways:
*   **Model Training**: They assist in training models to achieve the desired translation style <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
*   **Quality Assurance**: They are vital for maintaining top-notch quality assurance, which is critical for specialized models <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>.

The process also involves constant monitoring of performance, as even a short absence of a high-performing translator can impact quality <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>. This close touch helps manage quality issues and ensure data requirements are met <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>.

### Rationale for In-house Data Labeling
DeepL's decision to keep [[data_labeling_and_the_role_of_synthetic_data_in_ai | data labeling]] in-house stems from the desire for maximum control over the process and the importance of quality for their specific tasks <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>. While considering outsourcing parts of it, the core reason for internal management is the need for high-quality, specialized data that can be meticulously chosen and managed <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>. This granular control allows for direct feedback loops between application performance and model adjustments <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.

For example, DeepL's ability to allow customers to embed specific terminology into their models, while adhering to grammatical rules and managing word ambiguities, is a result of this tight feedback loop and deep control over their models <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

## AI Infrastructure

DeepL operates as a "build it yourself" company <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. This philosophy originated from the early days when necessary tools, [[ai_infrastructure_and_data_center_challenges | data centers]], and models were not readily available <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. Owning the entire vertical stack, from go-to-market to product, engineering, and research, allows the company to effectively identify and solve complex customer problems that simple prompt engineering might not address <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.

### Building Own Data Centers
DeepL chose to build and operate its own [[ai_infrastructure_and_data_center_challenges | data centers]] from the beginning, primarily due to the lack of alternatives at the time <a class="yt-timestamp" data-t="00:27:04">[00:27:04]</a>.

Advantages of this approach include:
*   **Cost Efficiency**: Running their own [[ai_infrastructure_and_data_center_challenges | data centers]] offers significant cost advantages at scale <a class="yt-timestamp" data-t="00:27:22">[00:27:22]</a>.
*   **Hardware Availability**: It ensures access to the newest hardware, enabling faster market entry and innovation <a class="yt-timestamp" data-t="00:29:20">[00:29:20]</a>.
*   **Optimization**: Given the scarcity and power of GPU compute, optimizing operations by running their own infrastructure is crucial for sustainability, both environmentally and commercially <a class="yt-timestamp" data-t="00:28:18">[00:28:18]</a>.

### Challenges and Future Considerations
While beneficial, operating own [[ai_infrastructure_and_data_center_challenges | data centers]] adds complexity and can impact development speed <a class="yt-timestamp" data-t="00:29:47">[00:29:47]</a>. DeepL is currently moving large parts of its stack towards [[ai_infrastructure_and_data_center_challenges | hyperscalers]] and a hybrid cloud model <a class="yt-timestamp" data-t="00:29:56">[00:29:56]</a>. This allows them to cut out only what needs to be run on-premise for efficiency, security, or data protection reasons <a class="yt-timestamp" data-t="00:30:02">[00:30:02]</a>.

The overall tooling for GPU compute is still in early stages <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>. While CPU compute has seen sophisticated abstraction layers making it cheap and sustainable, GPU compute is scarce and powerful, requiring careful optimization for large-scale operations <a class="yt-timestamp" data-t="00:27:43">[00:27:43]</a>.

For other companies, using [[ai_infrastructure_and_data_center_challenges | hyperscalers]] is recommended for kickstarting operations, but transitioning to their own [[ai_infrastructure_and_data_center_challenges | data centers]] may become advantageous when reaching significant scale due to cost and hardware availability <a class="yt-timestamp" data-t="00:26:51">[00:26:51]</a>.