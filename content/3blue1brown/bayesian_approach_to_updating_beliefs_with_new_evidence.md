---
title: Bayesian approach to updating beliefs with new evidence
videoId: HZGCoVF3YvM
---

From: [[3blue1brown]] <br/> 

The Bayesian approach to updating beliefs is centered around [[bayesian_probability_concepts_and_bayes_rule | Bayes' theorem]], one of the most important formulas in probability <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This formula is crucial for scientific discovery, a core tool in machine learning and AI, and has even been used for treasure hunting <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. For instance, in the 1980s, a team led by Tommy Thompson used Bayesian search tactics to uncover a ship that had sunk 150 years earlier, carrying what amounts to $700 million worth of gold in today's terms <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

Understanding Bayes' theorem involves several levels: knowing its parts to plug in numbers, understanding why it's true, and most importantly, recognizing when to use it <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. The fundamental concept is that new evidence does not completely determine beliefs in a vacuum; it should update prior beliefs <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

## The Steve Example: Human Judgment and Probability

To illustrate the importance of updating beliefs, consider the "Steve" example from a study by psychologists Daniel Kahneman and Amos Tversky <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. Their work on [[rationality_in_human_judgment | human judgments]] and their irrational contradictions to probability laws won a Nobel Prize <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

The description of Steve is: "Steve is very shy and withdrawn, invariably helpful but with very little interest in people or the world of reality. A meek and tidy soul, he has a need for order and structure, and a passion for detail" <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

Given this description, people are asked which is more likely: Steve is a librarian, or Steve is a farmer <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

### The Common (Irrational) Response

According to Kahneman and Tversky, most people say Steve is more likely to be a librarian because the traits align better with the stereotypical view of a librarian <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. This is considered irrational because almost nobody incorporates information about the ratio of farmers to librarians in their judgments <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. In the U.S., Kahneman and Tversky noted the ratio was about 20 farmers to 1 librarian <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. [[rationality_in_human_judgment | Rationality]] is not about knowing facts, but recognizing which facts are relevant <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### Bayesian Reasoning Applied

A [[understanding_bayes_theorem | Bayesian]] approach involves considering the base rates:

1.  **Start with a representative sample:** Imagine a group of 200 farmers and 10 librarians (reflecting the 20:1 ratio) <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
2.  **Estimate likelihoods:** If 40% of librarians fit Steve's description and 10% of farmers fit it <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>:
    *   Librarians fitting description: 40% of 10 = 4 librarians <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
    *   Farmers fitting description: 10% of 200 = 20 farmers <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
3.  **Calculate the posterior probability:** The probability that a random person fitting the description is a librarian is 4 out of 24 (4 librarians + 20 farmers), which is 16.7% <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

Even if a librarian is 4 times as likely as a farmer to fit the description, the sheer number of farmers means it's still more probable that Steve is a farmer <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. This demonstrates the core idea of Bayes' theorem: new evidence updates, rather than completely determines, prior beliefs <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

## Formalizing Bayes' Theorem

[[understanding_bayes_theorem | Bayes' theorem]] is relevant when you have a hypothesis (H) and new evidence (E), and you want to find the probability that your hypothesis holds given that the evidence is true <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. In notation, P(H|E) represents "the probability of hypothesis H given evidence E" <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

The formula is:

$P(H|E) = \frac{P(E|H) * P(H)}{P(E)}$

Where:
*   **P(H|E)**: The **posterior probability**—your belief about the hypothesis *after* seeing the evidence <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   **P(E|H)**: The **likelihood**—the probability of seeing the evidence *given that* the hypothesis is true <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **P(H)**: The **prior probability**—the probability that the hypothesis holds *before* considering any new evidence <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. (In the Steve example, this was 1/21, representing the ratio of librarians to the total population of librarians and farmers <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.)
*   **P(E)**: The total probability of seeing the evidence <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. In practice, P(E) is often broken down into two cases:
    $P(E) = P(E|H) * P(H) + P(E|~H) * P(~H)$
    *   **P(E|~H)**: The probability of seeing the evidence *given that* the hypothesis is *not* true (~H denotes "not H") <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.
    *   **P(~H)**: The probability that the hypothesis is *not* true.

Substituting P(E), the full formula is:

$P(H|E) = \frac{P(E|H) * P(H)}{P(E|H) * P(H) + P(E|~H) * P(~H)}$ <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>

## Visualizing Bayes' Theorem

Instead of memorizing the formula, it can be helpful to visualize it using an area diagram <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. Think of the space of all possibilities as a 1x1 square, where the probability of an event is represented by the area of its subset within the square <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

1.  **Hypothesis Area:** The hypothesis (H) occupies a portion of the square, say the left part, with a width equal to P(H) <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
2.  **Evidence Restriction:** When evidence (E) is observed, the space of possibilities gets restricted to only those outcomes where E holds <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. This restriction might not be even across H and ~H.
3.  **Posterior Proportion:** The new probability for the hypothesis, P(H|E), is the proportion it occupies within this restricted, "wonky" shape of the evidence <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

If the likelihoods (P(E|H) and P(E|~H)) are very different, the belief changes significantly <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. The formula geometrically states that P(H and E) is the area of the intersection of H and E (P(H) * P(E|H)), divided by the total area of E (P(E)) <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

## Broader Takeaways for Intuition

### The Linda Problem and Representative Samples

Another example from Kahneman and Tversky, the "Linda problem," highlights how human intuition struggles with probabilities versus frequencies <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.

Linda is described as: "31 years old, single, outspoken, and very bright. She majored in philosophy. As a student she was deeply concerned with issues of discrimination and social justice, and also participated in the anti-nuclear demonstrations" <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

Participants were asked what's more likely:
1.  Linda is a bank teller.
2.  Linda is a bank teller and is active in the feminist movement.

Surprisingly, 85% of participants chose option 2 <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. This is a logical error because the set of bank tellers who are also active in the feminist movement is a *subset* of all bank tellers, and thus must be smaller <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. This is known as the conjunction fallacy.

However, if the question is rephrased using a representative sample, e.g., "Out of 100 people who fit this description, how many are bank tellers and how many are bank tellers active in the feminist movement?", the error rate drops to 0% <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>. People correctly assign a higher number to the first option <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. This shows that phrasing probabilities as frequencies or counts (e.g., "40 out of 100") kicks intuition into gear more effectively than percentages or abstract likelihoods <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.

### Probability as Proportions

While representative samples are helpful, they don't easily capture the continuous nature of probability <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. Turning to area diagrams is a good alternative for sketching and visualizing <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. The math of probability is fundamentally the math of proportions, and geometry is exceedingly helpful in this context <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. Bayes' theorem, at its heart, is a straightforward statement about proportions: it tells you to look at the cases where the evidence is true, and then consider the proportion of those cases where the hypothesis is also true <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

## Conclusion

The ability of such a straightforward fact about proportions to be profoundly significant for science, [[applications_of_bayes_theorem_in_various_fields | artificial intelligence]], and quantifying belief, underscores the power of [[understanding_bayes_theorem | Bayes' theorem]] <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. While there can be debates about the context or interpretation of specific examples like Steve's (e.g., questions about the prior probability or likelihoods <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>), the ultimate point remains: evidence should not determine beliefs, but update them <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.