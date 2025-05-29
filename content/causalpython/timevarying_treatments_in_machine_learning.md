---
title: Timevarying treatments in machine learning
videoId: OvmpcL1CKqM
---

From: [[causalpython]] <br/> 

Iley, a guest on the Causal Bandits podcast, shares his journey from studying political science and statistics to becoming a leading figure in [[Causality and Machine Learning | causal machine learning]]. His work focuses on helping companies make better, data-driven decisions by addressing the complexities of time-varying treatments and confounders in real-world scenarios <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.

## The Limitations of Traditional Statistics
Iley realized early in his career at Viasat, a satellite internet company, that statistics alone was insufficient to answer interesting business questions <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. While statistical significance could be found, it often didn't translate to meaningful results because it failed to account for the underlying data-generating process <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. This revelation led him to explore a "parallel dimension" of data analysis focused on causality <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

### First Encounter with Causal Thinking
His first direct encounter with [[Causality and Machine Learning | causal thinking]] came while working on email campaigns to retain customers <a class="yt-timestamp" data-t="00:27:09">[00:27:09]</a>. The initial approach was to predict which customers were likely to churn and then send them discounts <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. However, Iley quickly learned that many of these customers would churn regardless of the discount <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. The true question wasn't *who* would churn, but *who would respond best* to the discount <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

He observed scenarios where:
*   Customers too upset might not be swayed by a small voucher <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
*   Satisfied customers might become aware of their bills and consider competitors after receiving a discount <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

This highlighted that simple statistical associations were insufficient for effective decision-making; understanding how variables *react* within a system was crucial <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

## Deep Dive into Causal Inference
Recognizing the complexity and lack of readily available expertise in [[Causality and Machine Learning | causal inference]], Iley embarked on a self-study journey <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

### The Power of Explaining: Writing a Blog
To gain a deeper understanding, Iley started a blog. The act of writing and explaining concepts forced him to truly grasp the subject matter <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. He also made a point to include code examples and simulations, which revealed nuances and limitations not always apparent from simply reading papers <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. This practice helped him understand how models behave in different real-world settings <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

Remarkably, this blog led to him being contacted by a CEO and offered a job to apply [[Causality and Machine Learning | causal inference]] professionally <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. This "triple win" — helping himself, the community, and a company — was an unexpected but welcome outcome <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

### Applying Causality in Practice
Working in the field presented new challenges, particularly the need to answer tough questions from superiors about the validity and utility of causal models <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

## Addressing Confounding with the Time Domain
Iley works for a company providing an analytics platform for product and growth teams <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>. A common problem involves understanding which product features drive conversions (e.g., from trial to paid user) <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.

### The Confounding Problem in Feature Adoption
Simply comparing conversion rates between users who adopted a feature and those who didn't is problematic because users who adopt features are often more engaged or had higher initial intent <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>. This "initial intent" or "user personality" acts as a confounder, making it difficult to disentangle the feature's true effect from pre-existing user attributes <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.

Traditional controls like country or device are often too coarse to capture this nuance <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.

### Leveraging User Activity as a Confounder Proxy
Iley's team used a method that measures user activity within the app as a proxy for initial intent or personality <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. For example, by comparing users who have *already* interacted with at least five features, and then one group additionally adopted the feature of interest, the comparison becomes much more believable and less confounded <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>. This is because users who have adopted five features are unlikely to be low-intent users, making any further difference more attributable to the specific feature <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>.

### Challenges with Time-Varying Data
Measuring the effect of time-varying treatments (feature adoption), time-varying outcomes (conversions), and time-varying confounders (in-app activity) presents significant data organization challenges <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.

A common pitfall is the need to discard data to maintain temporal order. For instance, if feature adoption and conversion both happen quickly (e.g., within the first day), forcing the adoption to *precede* the conversion might lead to discarding a large portion of data <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>. This discarding is not just about losing data quantity, but also introduces bias, as strong features that cause immediate conversion might be overlooked <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>.

### The Solution: Survival Analysis
To overcome these issues, Iley advocates for **Survival Analysis**, an underrated branch of supervised learning that handles time-to-event data <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>.

Key benefits of Survival Analysis:
*   It solves the problem of discarding data by using time-varying covariates to encode instances where users adopted a feature but haven't converted yet, or haven't adopted the feature at all <a class="yt-timestamp" data-t="00:21:43">[00:21:43]</a>.
*   It provides an equal footing for both groups in terms of time to convert <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>.
*   It preserves the temporal dimension, ensuring that treatments always precede outcomes and user profiles precede treatments <a class="yt-timestamp" data-t="00:23:21">[00:23:21]</a>.

Preserving the time dimension is crucial to avoid backward relationships <a class="yt-timestamp" data-t="00:26:08">[00:26:08]</a>. Collapsing data can lead to controlling for *mediators* (actions caused by the treatment), which can bias the estimated effect of the treatment, making it appear lower than it should be <a class="yt-timestamp" data-t="00:26:51">[00:26:51]</a>. In terms of Pearl's language, this means blocking the flow of information from the treatment to the outcome <a class="yt-timestamp" data-t="00:27:16">[00:27:16]</a>. From a decision-making standpoint, the total effect (including mediated effects) is usually what matters <a class="yt-timestamp" data-t="00:28:16">[00:28:16]</a>.

While time-ordering helps resolve biases like mediators, it's not a panacea for all confounding, especially hidden confounding <a class="yt-timestamp" data-t="00:30:14">[00:30:14]</a>. However, assuming no hidden confounders, sorting by time can resolve many issues <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>.

## Costs and Risks in Causal Inference
Iley views the "cost" of [[Causality and Machine Learning | causal assumptions]] (e.g., randomized controlled trials, consulting experts, making data-generating process assumptions) primarily as man-hours <a class="yt-timestamp" data-t="00:33:40">[00:33:40]</a>. His work focuses on enabling [[Causality and Machine Learning | causal inference]] in low-resource environments, which means accepting a lower degree of guarantees <a class="yt-timestamp" data-t="00:34:46">[00:34:46]</a>.

He emphasizes that [[Causality and Machine Learning | causality]] isn't a binary state but a spectrum <a class="yt-timestamp" data-t="00:35:34">[00:35:34]</a>. Making estimates "somewhat more causal" is always better than relying on plain correlations <a class="yt-timestamp" data-t="00:35:48">[00:35:48]</a>. The goal is to find methods that yield the highest guarantees with the lowest costs <a class="yt-timestamp" data-t="00:35:54">[00:35:54]</a>.

## Real-World Impact
Iley's team successfully applied these methods to a golfing app customer <a class="yt-timestamp" data-t="00:36:13">[00:36:13]</a>. A feature that wasn't getting much traction was intuitively dismissed as "not good" <a class="yt-timestamp" data-t="00:36:23">[00:36:23]</a>. However, after disentangling biases with causal methods, they found the feature had great potential <a class="yt-timestamp" data-t="00:36:57">[00:36:57]</a>. By pushing it into the onboarding process, the customer saw significant increases in top-line KPIs <a class="yt-timestamp" data-t="00:37:13">[00:37:13]</a>. This success story illustrates the power of [[Causality and Machine Learning | causal inference]] to reveal hidden opportunities.

## Main Challenges in Application
The biggest challenge isn't technical, but rather convincing organizations of the value of [[Causality and Machine Learning | causal inference]] methods <a class="yt-timestamp" data-t="00:38:44">[00:38:44]</a>. Companies already collect and use data for decision-making, so introducing a new, seemingly complex way of aggregating it requires significant persuasion <a class="yt-timestamp" data-t="00:39:02">[00:39:02]</a>.

Key strategies for communication with stakeholders:
*   **Setting expectations**: Frame causal methods as providing a *higher probability* of correctness or being *more correct* than regular associations, rather than claiming to know "the truth" <a class="yt-timestamp" data-t="00:39:56">[00:39:56]</a>.
*   **Transparency and traceability**: The ability to clearly tie results back to the raw data and show how every calculation is derived is paramount <a class="yt-timestamp" data-t="00:41:07">[00:41:07]</a>. This transparency empowers stakeholders, builds trust, and allows them to reproduce and own the results <a class="yt-timestamp" data-t="00:43:05">[00:43:05]</a>. This is especially crucial when delivering counterintuitive or challenging recommendations <a class="yt-timestamp" data-t="00:41:54">[00:41:54]</a>.

## The Future of Causality
Iley believes the future is "more causal" <a class="yt-timestamp" data-t="00:43:35">[00:43:35]</a>. Its adoption will depend on resources:
*   Organizations with more resources will use state-of-the-art methods to answer big questions with high guarantees <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>.
*   Smaller players will likely adopt automation or SaaS solutions, offering lower guarantees but still deriving more causal conclusions <a class="yt-timestamp" data-t="00:44:04">[00:44:04]</a>.

The rise of LLMs (Large Language Models) has significantly boosted awareness and belief in complex concepts like [[Causality and Machine Learning | causality]], as their human-like behavior makes people more open to "ultra-intelligent machines" <a class="yt-timestamp" data-t="00:45:00">[00:45:00]</a>. This is driving increased industry investment and interest beyond academia <a class="yt-timestamp" data-t="00:45:38">[00:45:38]</a>.

## Advice for Aspiring Causal Practitioners
For those feeling overwhelmed by the amount of information in [[Causality and Machine Learning | machine learning]] and [[Causality and Machine Learning | causality]]:
*   **Don't take shortcuts**: Especially with tools like ChatGPT, a deep level of understanding is required for [[Causality and Machine Learning | causal inference]] <a class="yt-timestamp" data-t="00:46:43">[00:46:43]</a>.
*   **Meticulous study**: True understanding comes from diligent effort <a class="yt-timestamp" data-t="00:47:06">[00:47:06]</a>.
*   **Teach to learn**: Writing a blog, giving lectures, or doing presentations forces a deeper understanding as you must explain concepts specifically and clearly, often with code examples and simulations <a class="yt-timestamp" data-t="00:48:31">[00:48:31]</a>. This process helps identify gaps in understanding and reveals how methods behave in various settings <a class="yt-timestamp" data-t="00:49:06">[00:49:06]</a>.
*   **Seek practical application**: The next step is to find a job where you can actively apply these skills <a class="yt-timestamp" data-t="00:49:52">[00:49:52]</a>.

## Resources and Recommendations
*   **Blog**: Iley's blog can be found at [aaron.io](http://aaron.io/) <a class="yt-timestamp" data-t="01:01:22">[01:01:22]</a>.
*   **Judea Pearl's Causal Inference Primer for Statistics**: A small, to-the-point booklet for understanding Directed Acyclic Graphs (DAGs) <a class="yt-timestamp" data-t="00:58:13">[00:58:13]</a>.
*   **"A Tale of Two Cultures"**: A paper that discusses the differences between the statistics and computer science communities, advocating for a blend of mindsets <a class="yt-timestamp" data-t="00:58:37">[00:58:37]</a>.

### Message to the Causal Python Community
Iley urges practitioners to persist in their journey to become better <a class="yt-timestamp" data-t="01:00:21">[01:00:21]</a>. Doing science correctly, by handling confounding and accounting for the time dimension, is essential to avoid hurting the business rather than helping it <a class="yt-timestamp" data-t="00:59:43">[00:59:43]</a>. Applying [[Causality and Machine Learning | causal inference]] isn't just a formal exercise, but a practical necessity to drive better decision-making and ensure business thrives <a class="yt-timestamp" data-t="01:00:34">[01:00:34]</a>.