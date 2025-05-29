---
title: Understanding Bayes theorem
videoId: HZGCoVF3YvM
---

From: [[3blue1brown]] <br/> 

[[bayesian_probability_concepts_and_bayes_rule | Bayes' theorem]] is one of the most important formulas in all of [[bayesian_probability_concepts_and_bayes_rule | probability]] <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It is central to [[applications_of_bayes_theorem_in_various_fields | scientific discovery]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>, a core tool in [[applications_of_bayes_theorem_in_various_fields | machine learning and AI]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>, and has even been used for treasure hunting <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. For example, in the 1980s, a team led by Tommy Thompson used [[applications_of_bayes_theorem_in_various_fields | Bayesian search tactics]] to uncover a sunken ship carrying approximately $700 million worth of gold in today's terms <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Levels of Understanding

Understanding Bayes' theorem can occur at several levels <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>:
*   **Basic**: Knowing what each part of the formula means to plug in numbers <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   **Conceptual**: Understanding why the formula is true, often aided by diagrams <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
*   **Application**: Recognizing when and why to use it <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

The most important level is the ability to recognize when to use it, which involves understanding the underlying reasoning <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## The Steve Example: Intuitive Reasoning

To understand Bayes' theorem more deeply, consider the "Steve" example from a study by psychologists Daniel Kahneman and Amos Tversky, whose work on human judgments won a Nobel Prize <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. Their research often focused on how human judgments irrationally contradict the [[bayesian_probability_concepts_and_bayes_rule | laws of probability]] <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### The Scenario
Steve is described as: "very shy and withdrawn, invariably helpful but with very little interest in people or the world of reality. A meek and tidy soul, he has a need for order and structure, and a passion for detail." <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>

The question posed is: Which is more likely? Steve is a librarian, or Steve is a farmer? <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>

### Common Human Judgment
Most people, when given this description, say Steve is more likely to be a librarian because the traits align with the stereotypical view of a librarian <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. Kahneman and Tversky considered this irrational <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

### The Missing Information: Base Rates
The irrationality, according to Kahneman and Tversky, stems from almost nobody incorporating information about the ratio of farmers to librarians <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. In their paper, this ratio in the U.S. was estimated at about 20 farmers to 1 librarian <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. Rationality is not about knowing every fact, but about recognizing which facts are relevant <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### Rational Reasoning with a Representative Sample
To reason about this question rationally, which contains the essential logic of Bayes' theorem <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>:
1.  **Start with a sample**: Imagine a representative sample reflecting the base rate, e.g., 200 farmers and 10 librarians (a 20:1 ratio) <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
2.  **Estimate likelihoods**: Based on Steve's description, if you estimate:
    *   40% of librarians fit the description <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
    *   10% of farmers fit the description <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
3.  **Calculate numbers in sample**:
    *   Out of 10 librarians, 4 would fit the description (40% of 10) <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
    *   Out of 200 farmers, 20 would fit the description (10% of 200) <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
4.  **Determine updated probability**: Among those who fit the description (4 librarians + 20 farmers = 24 total), the probability that a random person is a librarian is 4 out of 24, or approximately 16.7% <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

This demonstrates that even if a librarian is four times more likely to fit the description, the much larger number of farmers means it's still more probable that Steve is a farmer <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

The key mantra underlying Bayes' theorem is: **New evidence does not completely determine your beliefs in a vacuum; it should [[bayesian_approach_to_updating_beliefs_with_new_evidence | update prior beliefs]]** <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. If this reasoning makes sense, you understand the heart of Bayes' theorem <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

## Formalizing Bayes' Theorem

[[bayesian_probability_concepts_and_bayes_rule | Bayes' theorem]] is relevant when you have a **hypothesis (H)** (e.g., Steve is a librarian) and see new **evidence (E)** (e.g., Steve's description) <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. You want to know the probability that your hypothesis holds given the evidence is true, written as P(H|E) <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. The vertical bar "|" means "given that" <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

The components of Bayes' Theorem are:
*   **Prior Probability, P(H)**: The probability that the hypothesis holds before considering new evidence <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. In the Steve example, this was 1/21 (1 librarian for every 20 farmers) <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Likelihood, P(E|H)**: The probability of seeing the evidence given that the hypothesis is true <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. This is the proportion of librarians who fit Steve's description (e.g., 40%) <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Marginal Likelihood or Evidence Probability, P(E)**: The total probability of seeing the evidence <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. In practice, this is calculated by summing the probability of evidence given the hypothesis is true, and the probability of evidence given the hypothesis is false (P(E|~H)P(~H)) <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. The "~" symbol means "not" <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

The formula is:

$$P(H|E) = \frac{P(E|H)P(H)}{P(E|H)P(H) + P(E|\neg H)P(\neg H)}$$ <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>

*   The numerator, $P(E|H)P(H)$, represents the total number of cases where both the hypothesis and the evidence are true (e.g., 4 librarians fitting the description) <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
*   The denominator, $P(E)$, is the total number of cases where the evidence is true, regardless of the hypothesis (e.g., 4 librarians + 20 farmers = 24 people fitting the description) <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

The result, $P(H|E)$, is called the **posterior**, representing your belief about the hypothesis after seeing the evidence <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

## Visualizing Bayes' Theorem

Instead of memorizing the formula, it's often helpful to sketch a diagram <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. Think of the space of all possibilities as a 1x1 square, where the probability of an event is the area of its subset within that square <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

Imagine the hypothesis (H) occupying the left part of the square, with a width equal to P(H) <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. When evidence (E) is observed, the space of possibilities is restricted <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. The crucial point is that this restriction might not be even between the hypothesis and its negation <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. The new probability for the hypothesis (the posterior) is the proportion it occupies within this restricted, "wonky" shape defined by the evidence <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

If the likelihoods ($P(E|H)$ and $P(E|\neg H)$) are very different, your belief will change significantly <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. If they are similar, the evidence is irrelevant and doesn't change your beliefs <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.

Geometrically, $P(H) \times P(E|H)$ represents the area where both the hypothesis and the evidence occur together <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

## Making Probability More Intuitive

### The Linda Example: Power of Frequencies
Kahneman and Tversky conducted another experiment with a woman named Linda, described as a philosophy major concerned with social justice <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. Participants were asked which was more likely:
1.  Linda is a bank teller.
2.  Linda is a bank teller and is active in the feminist movement.

Surprisingly, 85% of participants chose the second option, even though the set of "bank tellers active in the feminist movement" is a subset of "bank tellers" and must therefore be smaller <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. This is known as the conjunction fallacy.

However, when the question was rephrased to use counts (e.g., "Out of 100 people who fit this description, how many are bank tellers vs. bank tellers active in the feminist movement?"), the error rate dropped to 0% <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>. This suggests that phrasing probability in terms of "40 out of 100" kickstarts our intuitions more effectively than "40%" or "0.4" <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.

### Probability as Proportions and Geometry
While representative samples are helpful, they don't easily capture the continuous nature of [[bayesian_probability_concepts_and_bayes_rule | probability]] <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. Turning to area (like the 1x1 square) is a good alternative as it's flexible and easy to sketch <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

Though probability is often seen as the study of uncertainty, its underlying math is fundamentally the math of proportions <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. Viewing [[bayesian_probability_concepts_and_bayes_rule | Bayes' theorem]] through the lens of proportions makes it conceptually straightforward: it tells you to look at cases where the evidence is true and then consider the proportion of those cases where the hypothesis is also true <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>. The formula simply spells out how to compute this proportion <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.

## Debates and Takeaways

While the Steve example from Kahneman and Tversky has faced some debate regarding its context ambiguity (e.g., whether Steve is a randomly sampled American or someone the interrogator might know), the core mathematical principle holds <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>. Questions about context affect the [[bayesian_probability_concepts_and_bayes_rule | prior probability]], and questions about stereotypes affect the [[bayesian_probability_concepts_and_bayes_rule | likelihoods]] <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

The ultimate point remains: **evidence should not determine beliefs, but [[bayesian_approach_to_updating_beliefs_with_new_evidence | update them]]** <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>. This principle is crucial for [[applications_of_bayes_theorem_in_various_fields | science]], [[applications_of_bayes_theorem_in_various_fields | artificial intelligence]], and any situation where you want to [[bayesian_approach_to_updating_beliefs_with_new_evidence | quantify belief]] <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.