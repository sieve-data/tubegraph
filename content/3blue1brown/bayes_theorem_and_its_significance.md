---
title: Bayes theorem and its significance
videoId: HZGCoVF3YvM
---

From: [[3blue1brown]] <br/> 

[[understanding_bayes_theorem_through_examples | Bayes' theorem]] is considered one of the most important formulas in probability <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It is central to scientific discovery, a core tool in machine learning and AI, and has even been used for [[bayesian_reasoning_in_treasure_hunting | treasure hunting]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. For example, in the 1980s, Tommy Thompson's team used Bayesian search tactics to uncover a sunken ship carrying an estimated $700 million in gold <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Levels of Understanding Bayes' Theorem

Understanding [[understanding_bayes_theorem_through_examples | Bayes' theorem]] can occur at different levels <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>:
*   **Basic Comprehension**: Knowing what each part of the formula means to plug in numbers <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   **Logical Derivation**: Understanding why the formula is true, often aided by diagrams that help in rediscovering it <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
*   **Practical Application**: Being able to recognize when and where the formula needs to be applied <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

To gain a deeper understanding, it's often helpful to first explore its application before dissecting the formula itself <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## Recognizing the Need: The Steve Example

Consider the following description of a man named Steve <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>:
> Steve is very shy and withdrawn, invariably helpful but with very little interest in people or the world of reality. A meek and tidy soul, he has a need for order and structure, and a passion for detail. <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>

Given this description, which do you find more likely?
1.  Steve is a librarian.
2.  Steve is a farmer. <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>

This example comes from a study by psychologists Daniel Kahneman and Amos Tversky, whose work on human judgments won a Nobel Prize <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. They researched how human judgments often irrationally contradict the laws of probability <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

According to Kahneman and Tversky, most people, after hearing Steve's description, conclude he is more likely to be a librarian <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. This is because the traits align with the stereotypical view of a librarian <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. However, this conclusion is deemed irrational because people often fail to incorporate crucial information about the ratio of farmers to librarians in their judgments <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

In the US, the ratio of farmers to librarians was about 20 to 1 at the time of their paper <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. Rationality isn't about knowing all facts, but about recognizing which facts are relevant <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### Bayesian Reasoning in Practice

To reason about Steve's profession, one can use the core logic behind [[introduction_to_bayesian_statistics | Bayes' theorem]] <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>:
1.  **Start with a representative sample**: Imagine a group, for instance, 200 farmers and 10 librarians, maintaining the 20:1 ratio <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
2.  **Apply the evidence**: Estimate what percentage of each group would fit Steve's description. For example, if 40% of librarians and 10% of farmers fit the description <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>:
    *   Librarians fitting description: 40% of 10 librarians = 4 librarians <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
    *   Farmers fitting description: 10% of 200 farmers = 20 farmers <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
3.  **Calculate the updated probability**: Among those who fit the description (4 librarians + 20 farmers = 24 people), the probability of a random person being a librarian is 4 out of 24, or approximately 16.7% <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

Even if a librarian is four times more likely than a farmer to fit the description, the sheer number of farmers means it's still more probable that Steve is a farmer <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. The key takeaway, which is the mantra of [[introduction_to_bayesian_statistics | Bayes' theorem]], is that **new evidence does not completely determine your beliefs in a vacuum; it should update prior beliefs** <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

## The Formal Formula of Bayes' Theorem

[[introduction_to_bayesian_statistics | Bayes' theorem]] is relevant when you have a **hypothesis (H)** (e.g., Steve is a librarian) and observe new **evidence (E)** (e.g., Steve's description), and you want to know the probability that your hypothesis holds given that the evidence is true <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. In standard notation, `P(H|E)` means "the probability of Hypothesis H given Evidence E" <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

The formula is derived from considering specific probabilities <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>:

*   **Prior Probability (P(H))**: The probability that the hypothesis holds *before* considering the new evidence <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. In the Steve example, this was 1 out of 21, based on the ratio of librarians to farmers in the general population <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Likelihood (P(E|H))**: The probability of observing the evidence *given that the hypothesis is true* <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. This represents the proportion of the hypothesis group that fits the evidence (e.g., 40% of librarians fitting Steve's description) <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Probability of Evidence (P(E))**: The total probability of seeing the evidence <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. This is typically broken down into two parts:
    *   `P(E|H) * P(H)`: The probability of evidence given the hypothesis *and* the hypothesis being true (e.g., 4 librarians out of 210 people total) <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.
    *   `P(E|¬H) * P(¬H)`: The probability of evidence given the hypothesis is *not* true (¬H means "not H") *and* the hypothesis not being true (e.g., 20 farmers out of 210 people total) <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

The formula for [[introduction_to_bayesian_statistics | Bayes' theorem]] is:

$$P(H|E) = \frac{P(E|H) \cdot P(H)}{P(E|H) \cdot P(H) + P(E|\neg H) \cdot P(\neg H)}$$ <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>

The result, `P(H|E)`, is called the **Posterior Probability**, representing your belief about the hypothesis *after* seeing the evidence <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

## Significance and Applications

While the formula might seem complex, its value lies in its ability to quantify and systematize the idea of changing beliefs <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.
*   **Scientific Discovery**: Scientists use it to analyze how new data validates or invalidates their models <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   **Artificial Intelligence**: Programmers use it to explicitly and numerically model a machine's beliefs <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   **Personal Thought**: [[introduction_to_bayesian_statistics | Bayes' theorem]] can reframe how one thinks about their own opinions and how they change <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

## Visualizing Bayes' Theorem

Instead of memorizing the formula, it's often more helpful to draw a diagram <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. This approach distills the idea of thinking with a representative sample, using areas instead of counts, making it more flexible and easier to sketch <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.

When using [[using_geometry_for_understanding_probability | geometry for understanding probability]], the space of all possibilities can be thought of as a 1x1 square <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. Any event occupies a subset of this space, and its probability is represented by the area of that subset <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. The hypothesis (H) can be visualized as living in the left part of the square with a width of `P(H)` <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

When evidence (E) is observed, the space of possibilities is restricted <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. The new probability for the hypothesis is the proportion it occupies within this restricted, transformed shape <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. If the likelihoods (P(E|H) and P(E|¬H)) are very different, the belief changes significantly <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. [[understanding_bayes_theorem_through_examples | Bayes' theorem]] geometrically describes this proportion, where `P(H) * P(E|H)` is the area of the region where both the hypothesis and evidence occur together <a class="yt-timestamp" data-t="00:09:55">[00:10:04]</a>.

## Broader Takeaways on Probability Intuition

The use of representative samples (like 210 librarians and farmers) is a powerful trick for intuition <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. Kahneman and Tversky conducted another experiment, known as the "Linda problem," which further illustrates this <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>:

Participants were given a description of Linda:
> Linda is 31 years old, single, outspoken, and very bright. She majored in philosophy. As a student she was deeply concerned with issues of discrimination and social justice, and also participated in the anti-nuclear demonstrations. <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>

Then asked which was more likely:
1.  Linda is a bank teller.
2.  Linda is a bank teller and is active in the feminist movement. <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>

85% of participants incorrectly chose option 2 as more likely, even though the set of "bank tellers who are active in the feminist movement" is a subset of "bank tellers" and must logically be smaller <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. However, when the question was rephrased using counts (e.g., "Out of 100 people who fit this description, how many are bank tellers vs. how many are bank tellers and active in the feminist movement?"), the error rate dropped to 0% <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>. This highlights that phrasing probabilities as "40 out of 100" can engage our intuition more effectively than percentages or abstract likelihoods <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.

While representative samples are helpful, they don't easily capture the continuous nature of probability. Therefore, turning to [[using_geometry_for_understanding_probability | area]] as a conceptual tool is a valuable alternative, especially for sketching problems with pencil and paper <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. Probability, at its mathematical core, is the study of proportions, where [[using_geometry_for_understanding_probability | geometry]] can be exceedingly helpful <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.

## Debates and Core Principle

Some psychologists debate Kahneman and Tversky's conclusions regarding the Steve example, arguing that the context is ambiguous <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>. Questions about the assumed general population of Steve (e.g., a randomly sampled American vs. someone personally known) determine the prior probability <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. Similarly, interpretations of personality stereotypes affect the likelihoods <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. All these debates can be visualized within the diagrammatic context, showing how they shift the prior and likelihoods <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.

Regardless of the specific experiment's interpretation, the ultimate point of [[introduction_to_bayesian_statistics | Bayes' theorem]] remains: **evidence should not determine beliefs, but update them** <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>. Reprogramming intuition to reflect this mathematical implication, often through effective visual aids, is key to understanding <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.