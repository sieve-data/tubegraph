---
title: Trust and safety in AIgenerated content
videoId: lwtU_NfFH8o
---

From: [[redpointai]] <br/> 

Trust and safety, including removing bias and minimizing the chance harmful content can be generated, are top priorities for Adobe, which maintains a very high bar in this area <a class="yt-timestamp" data-t="00:26:19">[00:26:19]</a>.

## Training Data Strategy

A core part of Adobe's differentiated Firefly strategy involves training models on data exclusively from their stock database, Adobe Stock <a class="yt-timestamp" data-t="00:26:32">[00:26:32]</a>, <a class="yt-timestamp" data-t="00:26:41">[00:26:41]</a>. They explicitly avoid training Firefly models on data scraped from the internet <a class="yt-timestamp" data-t="00:26:50">[00:26:50]</a>. This approach addresses concerns from artists regarding consent, control, or compensation for their work <a class="yt-timestamp" data-t="00:26:52">[00:26:52]</a>.

Training on Adobe Stock data provides several benefits:
*   **High-quality content** <a class="yt-timestamp" data-t="00:27:01">[00:27:01]</a>
*   **Legal right to train** on the data stored in their marketplace <a class="yt-timestamp" data-t="00:27:06">[00:27:06]</a>
*   **Reduced risk of IP infringement** <a class="yt-timestamp" data-t="00:27:10">[00:27:10]</a>, <a class="yt-timestamp" data-t="00:27:50">[00:27:50]</a>, <a class="yt-timestamp" data-t="00:35:18">[00:35:18]</a>
*   **Reduced risk of harmful content** <a class="yt-timestamp" data-t="00:27:13">[00:27:13]</a>. Harmful content is not approved in Adobe Stock, thanks to both automated and manual curation processes <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>.

## Addressing Bias

While Adobe Stock helps reduce harmful content, training data sets inherently contain some bias <a class="yt-timestamp" data-t="00:28:07">[00:28:07]</a>, <a class="yt-timestamp" data-t="00:28:10">[00:28:10]</a>. Adobe conducts extensive internal testing with employees to identify areas where the models are not performing well due to bias <a class="yt-timestamp" data-t="00:28:29">[00:28:29]</a>.

Key measures taken to reduce bias:
*   **Person Detector:** A model that detects references to people, often through job titles (e.g., "lawyer") <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>, <a class="yt-timestamp" data-t="00:29:55">[00:29:55]</a>.
*   **Debiasing Content:** When a person or job is referenced, the system debiases the content to introduce the correct distribution of skin tones, genders, and age groups based on the country of origin of the request <a class="yt-timestamp" data-t="00:30:02">[00:30:02]</a>, <a class="yt-timestamp" data-t="00:30:09">[00:30:09]</a>. This ensures a fair representation that counters the biases taught by the initial data set <a class="yt-timestamp" data-t="00:30:18">[00:30:18]</a>, <a class="yt-timestamp" data-t="00:30:33">[00:30:33]</a>.

## Preventing Harmful Content

Adobe has invested significantly in mechanisms to prevent harmful content, especially for its Firefly models <a class="yt-timestamp" data-t="00:31:35">[00:31:35]</a>. This includes:
*   **Toxicity Detector Models:** Trained to differentiate various terms and ensure content is safe for all age ranges, specifically avoiding "not safe for work" (NSFW) content <a class="yt-timestamp" data-t="00:31:01">[00:31:01]</a>, <a class="yt-timestamp" data-t="00:31:05">[00:31:05]</a>.
*   **Deny Lists and Block Lists:** Used to filter out undesirable content <a class="yt-timestamp" data-t="00:31:06">[00:31:06]</a>.
*   **NSFW Filters:** Applied at the end of the generation process <a class="yt-timestamp" data-t="00:31:13">[00:31:13]</a>.
*   **Child-Specific Safeguards:** Systems detect prompts referencing children and either avoid or use negative prompting to minimize the chances of generating inappropriate content in relation to children (e.g., children with tobacco) <a class="yt-timestamp" data-t="00:31:21">[00:31:21]</a>, <a class="yt-timestamp" data-t="00:31:41">[00:31:41]</a>.

## Customer Feedback for Refinement

Adobe recognizes that these systems are not perfect and has built robust feedback mechanisms within firefly.adobe.com and Photoshop <a class="yt-timestamp" data-t="00:32:02">[00:32:02]</a>.

*   **Explicit Signals:** Users can provide direct feedback through "like/dislike" or "report" functions <a class="yt-timestamp" data-t="00:34:18">[00:34:18]</a>. This feedback provides new training data points for refining rules and models <a class="yt-timestamp" data-t="00:32:11">[00:32:11]</a>.
*   **Implicit Signals:** Actions like downloading, saving, or sharing generated content are also strong indicators of user preference <a class="yt-timestamp" data-t="00:34:24">[00:34:24]</a>.

This feedback loop is crucial for reinforcing desired outcomes and avoiding disliked generations, effectively serving as Adobe's way of doing Reinforcement Learning from Human Feedback (RLHF) <a class="yt-timestamp" data-t="00:34:05">[00:34:05]</a>, <a class="yt-timestamp" data-t="00:34:38">[00:34:38]</a>. This ensures that the generated content is usable commercially <a class="yt-timestamp" data-t="00:32:41">[00:32:41]</a>.

[!IMPORTANT]
Adobe does *not* train models on customer data stored in Creative Cloud to avoid issues with brand guidelines, next-generation campaigns, or other sensitive information <a class="yt-timestamp" data-t="00:33:30">[00:33:30]</a>, <a class="yt-timestamp" data-t="00:33:40">[00:33:40]</a>.

## Brand Guidelines and Compliance

For Enterprise customers, [[challenges_of_integrating_ai_generated_content_with_traditional_content | brand guidelines]] and compliance are paramount <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>, <a class="yt-timestamp" data-t="00:24:52">[00:24:52]</a>. Adobe is innovating to enable marketers and creative departments within enterprises to automatically create content that complies with company or campaign brands <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>. This helps solve the content velocity problem by delivering beautiful, compliant content out of the gate, reducing the need for extensive quality assurance <a class="yt-timestamp" data-t="00:25:37">[00:25:37]</a>.