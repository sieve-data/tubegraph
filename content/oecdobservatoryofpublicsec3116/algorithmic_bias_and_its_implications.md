---
title: Algorithmic Bias and its Implications
videoId: VJES_jPWf70
---

From: [[oecdobservatoryofpublicsec3116]] <br/> 

Algorithmic bias refers to systematic and repeatable errors in a computer system that create unfair outcomes, such as favoring or disfavoring certain groups of people. This issue is a significant concern in the broader discussion surrounding the [[Impact of AI on Human Decision Making | impact of AI on human decision making]] and the [[Challenges and Issues with Trusting AI in Decision Making | challenges and issues with trusting AI in decision making]].

## Understanding Algorithmic Bias
The problem of algorithmic bias is often highlighted in public discourse, with concerns about "algorithmic injustice," "racist algorithms," and "sexist algorithms" being widely discussed <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>.

### Examples of Bias
*   **Recidivism Prediction Software:** A ProPublica report highlighted software used to predict recidivism, given to bail judges, which was found to be biased against Black individuals <a class="yt-timestamp" data-t="00:31:11">[00:31:11]</a>. This bias manifested as different error rates for Black and White individuals; for instance, wrongly sending Black individuals to jail more often when they wouldn't have been recidivists, and wrongly leaving White individuals out who later turned out to be recidivists <a class="yt-timestamp" data-t="00:31:26">[00:31:26]</a>.
*   **Apple Card Algorithm:** The Apple Card algorithm has been cited for being gender-biased <a class="yt-timestamp" data-t="00:30:56">[00:30:56]</a>.
*   **Amazon Recruiting Tool:** Amazon's recruiting algorithm was found to be sexist, essentially replicating past hiring decisions that favored men <a class="yt-timestamp" data-t="00:35:20">[00:35:20]</a>. The algorithm learned that to be successful in Amazon's past hiring, it "helps to be a man" <a class="yt-timestamp" data-t="00:35:43">[00:35:43]</a>.
*   **Google Image Generation:** Google's image generation algorithm, when asked for "Vikings" or "German soldiers in 1943," generated images of diverse groups, including Black Nazis, indicating it was "forced" to show fewer white men and ensure women and Black individuals were included in proportion <a class="yt-timestamp" data-t="00:34:14">[00:34:14]</a>. This illustrates the challenge of instructing algorithms to reflect desired societal outcomes without unintended, nonsensical results <a class="yt-timestamp" data-t="00:34:51">[00:34:51]</a>.

### Origins of Bias
The [[Types of AI and their Similarity to Human Thinking | two types of AI]], symbolic AI and machine learning, exhibit different behaviors. Machine learning models, particularly large language models like ChatGPT, are trained on massive datasets <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. When these models are tested for biases common in human [[Types of AI and their Similarity to Human Thinking | System 1 thinking]], they often fail initial tests, demonstrating that they "replicate the same biases that we have" <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. For instance, an early version of ChatGPT could fall for the "bat and ball" cognitive trap <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. This is because they associate things that frequently appear together in their training data <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

In the case of the Amazon recruiting tool, the algorithm's bias was a reflection of Amazon's own past hiring practices, acting as a "mirror of your past behavior" <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>. Scrapping such an algorithm might hide the truth of existing biases rather than addressing them <a class="yt-timestamp" data-t="00:36:09">[00:36:09]</a>.

## Challenges in Addressing Algorithmic Bias

### Defining "Unbiased"
A major challenge is the difficulty in defining what constitutes an unbiased algorithm <a class="yt-timestamp" data-t="00:33:18">[00:33:18]</a>. For example, in bail decisions, two seemingly intuitive definitions of bias (different error rates vs. different risk scores for the same data across racial groups) are mathematically mutually exclusive, except in extremely rare cases <a class="yt-timestamp" data-t="00:32:31">[00:32:31]</a>. This highlights that "unbiased" is not intuitive and can lead to complex scientific debates <a class="yt-timestamp" data-t="00:33:25">[00:33:25]</a>. A universally accepted definition of bias, considering various issues and protected groups, is virtually impossible to achieve <a class="yt-timestamp" data-t="00:33:50">[00:33:50]</a>.

### The Need for Clear Priorities
To make an AI system "unbiased" or aligned with ethical standards, human users and regulators must clearly define their priorities <a class="yt-timestamp" data-t="00:34:51">[00:34:51]</a>. Forcing an algorithm to reflect societal wishes (e.g., specific gender proportions in hiring) requires explicit decisions about what is wanted <a class="yt-timestamp" data-t="00:35:59">[00:35:59]</a>. For instance, an algorithm could be instructed to find the best candidate under the constraint that 50% must be women, or even 60% to compensate for past discrimination <a class="yt-timestamp" data-t="00:36:47">[00:36:47]</a>.

Similarly, in the context of bail decisions, an algorithm can be designed to be less biased and more accurate than human judges <a class="yt-timestamp" data-t="00:37:35">[00:37:35]</a>. But this requires judges to explicitly decide between conflicting objectives, such as having 42% fewer people in jail for the same recidivism rate, or the same number of people in jail but 25% fewer crimes <a class="yt-timestamp" data-t="00:37:45">[00:37:45]</a>. Such decisions are often avoided by human judges who prefer to maintain ambiguous criteria in their case-by-case judgments <a class="yt-timestamp" data-t="00:38:50">[00:38:50]</a>.

Paradoxically, while AI is often marketed as simplifying decision-making, it actually forces users to "define your priorities much more clearly and much less ambiguously than you were doing in your current system" <a class="yt-timestamp" data-t="00:39:12">[00:39:12]</a>. This is a key aspect of [[Ethics in behavioral insights | ethics in behavioral insights]] and [[Ethical challenges in behavior analysis | ethical challenges in behavior analysis]] within the context of AI.

## Implications for Regulators
Regulators face crucial questions regarding algorithmic bias <a class="yt-timestamp" data-t="00:39:56">[00:39:56]</a>:
*   **Defining Unacceptable Bias:** What specific criteria constitute a legally, politically, or socially unacceptable bias <a class="yt-timestamp" data-t="00:41:01">[00:41:01]</a>?
*   **Quality of Human Decisions:** Before regulating AI, regulators should also assess the quality of human decisions, which are often not as good as perceived <a class="yt-timestamp" data-t="00:40:02">[00:40:02]</a>.
*   **Validation of AI Models:** Who will validate the quality and fairness of AI models <a class="yt-timestamp" data-t="00:40:30">[00:40:30]</a>? Relying solely on the seller's assurance that a model is good is insufficient <a class="yt-timestamp" data-t="00:40:46">[00:40:46]</a>.

The challenge of algorithmic bias underscores the complex [[Intersection of AI and Behavioral Science | intersection of AI and behavioral science]], as it forces a deeper examination of human biases and societal values when designing and deploying AI systems.