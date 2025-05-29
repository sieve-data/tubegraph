---
title: Using geometry for understanding probability
videoId: HZGCoVF3YvM
---

From: [[3blue1brown]] <br/> 

Understanding probability can be enhanced by [[importance_of_geometric_understanding_in_linear_algebra | geometric understanding]], particularly through visualizing concepts using areas and proportions <a class="yt-timestamp" data-t="08:48:00">[08:48:00]</a>. This approach can make abstract probabilistic ideas, such as Bayes' theorem, more intuitive <a class="yt-timestamp" data-t="10:18:00">[10:18:00]</a>.

## From Samples to Areas: Visualizing Possibilities

A helpful initial step in understanding probability problems is to picture a representative sample <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>. For instance, when considering the likelihood of "Steve" being a librarian or a farmer, one might imagine a group of 200 farmers and 10 librarians based on general population ratios <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>. If 40% of librarians and 10% of farmers fit a specific description, this would translate to 4 librarians and 20 farmers in that sample fitting the description <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>. Thus, the probability of a person fitting the description being a librarian is 4 out of 24 (16.7%) <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>. This method, while effective, relies on arbitrary sample sizes <a class="yt-timestamp" data-t="07:03:00">[07:03:00]</a>.

To generalize this idea and capture the continuous nature of [[applications_of_probability_density | probability]], one can use areas instead of counts <a class="yt-timestamp" data-t="08:48:00">[08:48:00]</a>. The space of all possibilities can be represented as a 1x1 square <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>. Any event then occupies a subset of this space, and its probability is the area of that subset <a class="yt-timestamp" data-t="09:05:00">[09:05:00]</a>. For example, a hypothesis can be thought of as occupying the left part of the square with a width proportional to its probability <a class="yt-timestamp" data-t="09:11:00">[09:11:00]</a>.

## Bayes' Theorem and Geometric Visualization

Bayes' theorem, a fundamental formula in [[probability_of_a_probability | probability]], can be effectively understood through geometric diagrams <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a> <a class="yt-timestamp" data-t="08:37:00">[08:37:00]</a>.

When new evidence is observed, the space of possibilities becomes restricted <a class="yt-timestamp" data-t="09:22:00">[09:22:00]</a>. The new probability for a hypothesis is the proportion it occupies within this restricted space <a class="yt-timestamp" data-t="09:29:00">[09:29:00]</a>.

The components of Bayes' theorem can be mapped to areas:
*   **Prior (P(H))**: The initial probability of the hypothesis, represented as the width of a section of the 1x1 square <a class="yt-timestamp" data-t="05:35:00">[05:35:00]</a> <a class="yt-timestamp" data-t="09:14:00">[09:14:00]</a>.
*   **Likelihood (P(E|H))**: The probability of seeing the evidence given the hypothesis is true <a class="yt-timestamp" data-t="05:42:00">[05:42:00]</a>. Geometrically, this relates to the height of the rectangle representing the intersection of the hypothesis and the evidence <a class="yt-timestamp" data-t="10:00:00">[10:00:00]</a>.
*   **Probability of both hypothesis and evidence (P(H and E))**: This is the area of the rectangle formed by P(H) as width and P(E|H) as height <a class="yt-timestamp" data-t="10:00:00">[10:00:00]</a>.
*   **Denominator (P(E))**: The total probability of seeing the evidence, which is the sum of the evidence occurring with the hypothesis and without it <a class="yt-timestamp" data-t="07:20:00">[07:20:00]</a>. This total area represents the restricted space of possibilities after observing the evidence <a class="yt-timestamp" data-t="09:22:00">[09:22:00]</a>.
*   **Posterior (P(H|E))**: The updated belief about the hypothesis after seeing the evidence <a class="yt-timestamp" data-t="07:40:00">[07:40:00]</a>. This is the ratio of the area where both the hypothesis and evidence occur to the total area where the evidence occurs <a class="yt-timestamp" data-t="09:33:00">[09:33:00]</a>.

> "If this line of reasoning makes sense to you, the way that seeing evidence restricts the space of possibilities, and the ratio you need to consider after that, then congratulations! You understand the heart of Bayes' theorem." <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>

## Advantages of Geometric and Proportional Thinking

1.  **Sketchability**: [[Spatial intuition in math | Visualizing probability]] with areas is easy to sketch with pencil and paper, aiding problem-solving <a class="yt-timestamp" data-t="12:16:00">[12:16:00]</a>.
2.  **Continuity**: Areas naturally capture the continuous nature of probability, unlike discrete counts <a class="yt-timestamp" data-t="12:09:00">[12:09:00]</a>.
3.  **Focus on Proportions**: The underlying math of probability is that of proportions <a class="yt-timestamp" data-t="12:34:00">[12:34:00]</a>. [[Geometry in higher dimensions | Geometry]] provides a direct way to think about and compute these proportions <a class="yt-timestamp" data-t="12:37:00">[12:37:00]</a>.
4.  **Clarity**: When presented as a statement about proportions, Bayes' theorem becomes "kind of obvious" <a class="yt-timestamp" data-t="12:44:00">[12:44:00]</a>. Both sides of the theorem direct one to consider cases where evidence is true and then find the proportion where the hypothesis is also true <a class="yt-timestamp" data-t="12:55:00">[12:55:00]</a>.
5.  **Overcoming Intuitive Biases**: Studies by Daniel Kahneman and Amos Tversky, like the "Linda" example, show that humans often make irrational judgments when asked about abstract likelihoods <a class="yt-timestamp" data-t="10:31:00">[10:31:00]</a>. However, when the question is rephrased in terms of counts out of a specific sample (e.g., "how many out of 100"), these errors can drop significantly or disappear entirely <a class="yt-timestamp" data-t="11:34:00">[11:34:00]</a>. This highlights how thinking in concrete numbers and proportions (even if discrete) can better activate our intuition <a class="yt-timestamp" data-t="11:54:00">[11:54:00]</a>. This [[connection_between_numerical_and_geometric_understandings | connection between numerical and geometric understandings]] helps clarify the concepts.

Ultimately, the key mantra from Bayes' theorem, reinforced by geometric visualization, is that new evidence should *update* prior beliefs, not completely determine them in a vacuum <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a> <a class="yt-timestamp" data-t="14:24:00">[14:24:00]</a>. [[Geometry and circles | Geometry]] offers a powerful way to visualize this process of updating beliefs as a restriction and re-proportioning of the space of possibilities <a class="yt-timestamp" data-t="14:08:00">[14:08:00]</a>.