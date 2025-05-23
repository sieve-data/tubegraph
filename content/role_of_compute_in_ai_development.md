---
title: Role of compute in AI development
videoId: a42key59cZQ
---

From: [[dwarkesh | The Dwarkesh Podcast]]

Gwern Branwen, an anonymous researcher and writer, has extensively discussed the pivotal role of computing power in the advancement of artificial intelligence. His views, shaped over years of observation and analysis, highlight compute not just as a resource but as a fundamental enabler of algorithmic discovery and the [[scaling of AI capabilities | challenges_and_opportunities_in_deploying_ai_at_scale]].

## Early Skepticism and Evolving Perspectives

Initially, Gwern was skeptical of the idea that simply having enough computing power would lead to advanced AI. He found the "build it and they will come" view of progress, suggesting that matching the human brain's compute power would summon the correct algorithms, to be unlikely <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. He believed algorithms were complex and required deep insight, not just computational brute force <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.

However, his perspective began to shift through exposure to the arguments of figures like Hans Moravec, Ray Kurzweil, and Shane Legg, who posited a connectionist view: sufficient computing power could lead to discovering neural network architectures matching the human brain <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. Gwern paid close attention to Legg's extrapolations and predictions based on Moore's Law and updated compute numbers <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.

The emergence of successes like DanNet and AlexNet served as impressive examples of connectionism, making Gwern reconsider whether these were isolated incidents or evidence supporting the predictions that better algorithms would "just show up" with enough GPU power <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>, <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.

## Compute as a Catalyst for Algorithmic Discovery

A central theme in Gwern's analysis is that compute power is a prerequisite for the discovery and refinement of AI algorithms.

### Trial, Error, and Serendipity
Gwern argues that many algorithmic breakthroughs are not solely the product of "deep insight" but are heavily reliant on trial and error, which is only feasible with substantial compute resources <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>, <a class="yt-timestamp" data-t="00:18:43">[00:18:43]</a>. Compute allows researchers to:
*   Test numerous variations in hyperparameters and architectures <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>.
*   Persist through initial failures, eventually hitting upon configurations that work <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.
*   Once a working solution is found, simplify and understand it to create robust solutions <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.

He notes that the research literature often obscures this messy, compute-intensive discovery process, presenting a "nice sounding story" that downplays the role of trial and error <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>. This creates a bias where researchers might attribute their own compute-heavy successes to luck, while believing others achieve breakthroughs through pure intellect <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>.

### Historical Precedents and Missed Opportunities
The lack of sufficient compute in the past led to potentially [[revolutionary ideas | ai_trajectory_and_scaling_hypothesis]] being overlooked or deemed irrelevant. Gwern points to concepts like ResNets being published as early as 1988 but failing to make an impact because the available compute could only demonstrate them at a small, impractical scale <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>, <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>. It took until 2015, with far greater compute, for ResNets to revolutionize deep learning <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>.

## Scaling Laws and the Primacy of Compute

Gwern's conviction in the importance of compute solidified with the rise of large language models and the empirical demonstration of scaling laws.

### The Gradual Realization
Observing the deep learning literature, Gwern noticed a consistent trend: dataset sizes, model sizes, and GPU usage (from one to two, then eight) were continually increasing <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>. Neural networks expanded from niche applications to broader capabilities <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>. This led him to increasingly consider that "maybe intelligence really is just a lot of compute applied to a lot of data, applied to a lot of parameters" <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>, vindicating the views of Moravec, Legg, and Kurzweil.

### Landmark Models and Papers
*   **GPT-1:** Its ability to learn an unsupervised sentiment neuron with a compute-centric approach was an early indicator <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>.
*   **GPT-2:** Prompted a "holy shit!" moment regarding the potential of scaling <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.
*   **GPT-3:** Represented a massive scale-up in compute and was a crucial test for the scaling hypothesis. Its impressive few-shot learning capabilities confirmed to Gwern that "we are living in the scaling world" <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>, <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>.
*   **Baidu Scaling Laws Paper (2017):** This paper, which showed that scaling laws continued to hold over vast ranges, was highly significant but largely overlooked at the time <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>.

Gwern emphasizes that the common ingredient across various successful generative architectures is "lots and lots of GPUs" <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>.

## Compute's Role in Specific AI Breakthroughs

*   **AlphaZero:** Its discovery was aided by DeepMind using Bayesian optimization on hyperparameters, a process requiring significant compute to train many model versions and observe the effects of changes like reducing tree search <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>. Read more about [[AlphaZero and Efficient Search Techniques | alphazero_and_efficient_search_techniques]].
*   **BigGAN:** Its ability to handle 300 million images demonstrated that GANs could scale effectively, contrary to what some believed, provided enough compute was available <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>.

## Intelligence, Compute, and Turing Machines

Gwern's view of intelligence itself is tied to compute. He theorizes that "all intelligence is is search over Turing machines" <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. More intelligent entities, in this view, simply have more compute to search over a larger space of longer Turing machines <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. Large neural networks are seen as gigantic ensembles of smaller, specialized models (Turing machines) found and tailored through the application of compute to vast datasets <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

## Misconceptions and Underappreciation of Compute

Gwern identifies two main reasons why many people, particularly in 2020, were not grasping the full implications of scaling and compute's role in AI progress:
1.  **Lack of Attention to Key Scaling Results:** Many were unaware of or did not appreciate the significance of prior results like the Baidu scaling paper or the full implications of AlphaZero's development process <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>, <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>.
2.  **Overemphasis on Algorithmic Insight:** A shared error, which Gwern himself initially made, was believing algorithms were more important than compute <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>. This was compounded by the way research papers often present discoveries, downplaying the crucial role of compute-intensive trial and error <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>.

He concludes that compute comes first because it enables the necessary experimentation and serendipity required to find and refine complex AI systems <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a>. Without it, even correct ideas may fail to be validated or developed due to the inability to explore the parameter space sufficiently <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>.