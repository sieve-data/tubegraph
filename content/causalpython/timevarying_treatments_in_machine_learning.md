---
title: timevarying treatments in machine learning
videoId: OvmpcL1CKqM
---

From: [[causalpython]] <br/> 
The transcript discusses [[Machine Learning and Treatment Effect Estimation | time-varying treatments]] in the context of product analytics, focusing on the challenges of accurately attributing user conversions to specific product features. The speaker, Mr. I Ly, emphasizes the importance of preserving temporal information to avoid biased conclusions.

## The Challenge of [[Time-Varying Treatments in Machine Learning | Time-Varying Treatments]]

In product analytics, [[Time-Varying Treatments in Machine Learning | time-varying treatments]] refer to actions or features users adopt within an application, such as engaging with specific functionalities in a freemium product during a trial period, which may influence their conversion to paid users or their likelihood of churn <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. The challenge lies in determining which features truly drive conversions, rather than merely correlating with user behavior <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.

## The Problem of Confounding and Data Loss

A significant challenge is that users who adopt a certain feature are often already more engaged and have a higher initial intent than those who don't <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. This "initial intent" acts as a confounder, making it difficult to disentangle whether observed differences in conversion rates are due to feature adoption or pre-existing user attributes like personality or preferences <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.

Traditional methods of controlling for baseline attributes (e.g., country, device, marketing campaign) are often too coarse to capture the nuances of user behavior <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. Furthermore, organizing data for analysis of [[Time-Varying Treatments in Machine Learning | time-varying treatments]] and outcomes is not straightforward <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.

One common issue is the need to specify a time frame for adoptions that precedes the outcome <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>. For example, measuring first-day adoptions and comparing them with conversions after the first day can lead to discarding a significant amount of data, such as conversions that happen on the first day or adoptions that occur after the first day <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>. This discarding of information is problematic not only because it reduces data quantity but also because it introduces bias; features that lead to immediate conversions might be falsely perceived as ineffective if those rapid conversions are discarded <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>.

## Solution: Survival Analysis and [[Time-Varying Covariates | Time-Varying Covariates]]

To address these challenges, the speaker advocates for the use of survival analysis, which is described as an "underrated" third branch of supervised learning, alongside classification and regression <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>.

Survival analysis allows for the modeling of time-varying treatments (e.g., feature adoption) and time-varying outcomes (e.g., conversions), as well as time-varying confounders (e.g., in-app activity) <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.

> "Using survival lets you solve the problem I was mentioning earlier. You'd go about and use what is called [[Time-Varying Covariates | time-varying covariates]] to encode those instances where users have adopted the feature but haven't converted yet and those instances where users haven't adopted the feature and you would build a survival curve for both groups and then compare the um, you know, the survival or one minus survival which is the conversion rate at the end of the period." <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>

By encoding user activity within the app as a proxy for initial intent or user personality, survival analysis generates stronger confounders to debias results <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. This approach makes comparisons much more believable by ensuring that groups being compared (e.g., users who adopted a feature vs. those who didn't) have similar levels of engagement or value from the product prior to the treatment <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>.

### Benefits of Preserving Temporal Information
The core benefit of this methodology is the preservation of the time dimension in the data <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a>.

*   **No Data Discarded**: It avoids the need to discard information, ensuring all relevant adoptions and conversions are included <a class="yt-timestamp" data-t="00:22:18">[00:22:18]</a>.
*   **Correct Event Ordering**: It naturally ensures that the treatment (feature adoption) always precedes the outcome (conversion) and that the confounders (user profile) precede the treatment <a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>.
*   **Millisecond Precision**: The data can be structured to capture millisecond-precise descriptions of user journeys, including when features were used and how users traversed through different app states <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>.

## Avoiding Bias from Backwards Relationships

Collapsing the time dimension can lead to "backwards relationships," where actions taken by users *after* a treatment (and potentially caused by it) are incorrectly treated as confounders that precede the treatment <a class="yt-timestamp" data-t="00:25:50">[00:25:50]</a>.

> "When you squash your data and you eliminate the time dimension then you can get all these backwards relationships that can really bias your analysis." <a class="yt-timestamp" data-t="00:26:08">[00:26:08]</a>

Controlling for such post-treatment actions (mediators or blockers) can bias the causal effect estimate downwards, making a feature appear less effective than it is <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>. This is because it removes the "mediated effect," focusing only on the direct effect when, for decision-making purposes, the total effect (direct + mediated) is usually what matters <a class="yt-timestamp" data-t="00:28:06">[00:28:06]</a>. By maintaining the time dimension, the methodology naturally avoids controlling for these misleading variables <a class="yt-timestamp" data-t="00:28:30">[00:28:30]</a>.

## Limitations and Practical Considerations

While preserving the time dimension helps resolve many biases, such as those caused by blockers or mediators, it does not solve all issues, particularly in the presence of [[Hidden Confounding | hidden confounding]] (e.g., M-bias) <a class="yt-timestamp" data-t="00:29:18">[00:29:18]</a>. If an assumption of no [[Hidden Confounding | hidden confounders]] is made, then sorting by time should address most problems <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>.

The application of [[Machine Learning and Treatment Effect Estimation | causal machine learning]] comes with costs, primarily in "man hours" for making well-judged assumptions or consulting domain experts <a class="yt-timestamp" data-t="00:33:40">[00:33:40]</a>. The speaker's work focuses on enabling [[Machine Learning and Treatment Effect Estimation | causal inference]] in low-resource environments by accepting a lower degree of guarantees, viewing causality as a spectrum <a class="yt-timestamp" data-t="00:35:02">[00:35:02]</a>. The goal is to find methods that yield the highest guarantees with the lowest costs <a class="yt-timestamp" data-t="00:35:56">[00:35:56]</a>.

> [!NOTE] Practical Impact
> In one instance, applying these methods helped a golfing app customer identify a feature that was not widely used but had great potential to drive KPIs. By making it part of the onboarding process, the customer significantly boosted their top-line metrics, demonstrating the tangible value of debiased causal analysis <a class="yt-timestamp" data-t="00:36:10">[00:36:10]</a>.

## Challenges in Adoption and Communication

The biggest challenge in applying [[Machine Learning and Treatment Effect Estimation | causal inference methods]] is convincing organizations of their value <a class="yt-timestamp" data-t="00:38:44">[00:38:44]</a>. Companies already collect and use data for decision-making, so a new approach needs to clearly demonstrate its unique value proposition <a class="yt-timestamp" data-t="00:39:02">[00:39:02]</a>.

Effective communication involves:
*   **Setting Expectations**: Clarifying that the methods offer a *higher probability* of truth or greater correctness compared to regular associations, rather than absolute truth (like an RCT) <a class="yt-timestamp" data-t="00:39:56">[00:39:56]</a>.
*   **Transparency**: Ensuring that results can be tied back to the data and calculations are transparent, allowing stakeholders to reproduce and gain ownership over the findings, especially when results are counterintuitive <a class="yt-timestamp" data-t="00:42:07">[00:42:07]</a>.

## Future of Causality and Learning Advice

The future is "more causal" <a class="yt-timestamp" data-t="00:43:35">[00:43:35]</a>. Larger organizations will use state-of-the-art methods for big questions, while smaller players will rely on automation or SaaS solutions to derive more causal conclusions with lower guarantees <a class="yt-timestamp" data-t="00:43:54">[00:43:54]</a>. The rise of LLMs and their human-like behavior is also contributing to a greater belief in advanced concepts, potentially accelerating the adoption of [[Machine Learning and Treatment Effect Estimation | causal inference]] in industry <a class="yt-timestamp" data-t="00:45:00">[00:45:00]</a>.

For individuals starting in the field, the key advice is:
*   **Don't Take Shortcuts**: [[Time-Varying Treatments in Machine Learning | Causal inference]] requires a deep understanding that cannot be achieved through quick answers from tools like ChatGPT <a class="yt-timestamp" data-t="00:46:47">[00:46:47]</a>.
*   **Meticulous Study**: Engage in thorough and meticulous study of the field <a class="yt-timestamp" data-t="00:47:06">[00:47:06]</a>.
*   **Active Learning**: Write a blog, give lectures, or do presentations. The act of explaining concepts and performing simulations or code examples forces a deeper understanding, revealing gaps in knowledge <a class="yt-timestamp" data-t="00:48:26">[00:48:26]</a>.
*   **Seek Practical Application**: Aim to work in a role where [[Machine Learning and Treatment Effect Estimation | causal inference]] is applied, as this is the best way to gain practical experience and deepen understanding <a class="yt-timestamp" data-t="00:49:52">[00:49:52]</a>.
*   **Prioritize Value**: Always consider how actions impact the business and strive to deliver tangible value, rather than focusing on the "shiniest algorithm" or job titles <a class="yt-timestamp" data-t="00:50:49">[00:50:49]</a>.

### Recommended Resources
*   **Alex Molak's Book**: Recommended as a great introductory text <a class="yt-timestamp" data-t="00:57:47">[00:57:47]</a>.
*   **Judea Pearl's Causal Inference Primer for Statistics**: A "small booklet" that is very "to the point" for those wanting to get into DAGs <a class="yt-timestamp" data-t="00:58:13">[00:58:13]</a>.
*   **A Tale of Two Cultures (Paper)**: Discusses the differences between the statistics and computer science communities, fostering an understanding of diverse mindsets in analytics <a class="yt-timestamp" data-t="00:58:37">[00:58:37]</a>.

> [!CAUTION] Message to the Causal Python Community
> It is crucial to persist in becoming better practitioners. Using data to drive recommendations incorrectly—by not handling confounding or by removing the time dimension without proper accounting—can hurt the business instead of helping it. Applying [[Machine Learning and Treatment Effect Estimation | causal inference methods]] is not just a formal exercise but a necessity for driving better decision-making and ultimately helping businesses thrive <a class="yt-timestamp" data-t="00:59:43">[00:59:43]</a>.