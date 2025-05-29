---
title: Understanding Bayes theorem through examples
videoId: HZGCoVF3YvM
---

From: [[3blue1brown]] <br/> 

[[Bayes theorem and its significance | Bayes' theorem]] is a fundamental formula in probability, crucial for scientific discovery, machine learning, and artificial intelligence <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Its practical applications include aiding in treasure hunting, such as when Tommy Thompson's team used [[bayesian_reasoning_in_treasure_hunting | Bayesian search tactics]] to locate a sunken ship carrying $700 million worth of gold in the 1980s <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

Understanding [[bayes_theorem_and_its_significance | Bayes' theorem]] can occur at multiple levels:
*   **Basic Comprehension:** Knowing the meaning of each part to plug in numbers <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   **Conceptual Understanding:** Grasping why the formula is true, often aided by diagrams <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
*   **Application Recognition:** Identifying situations where the theorem is needed <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

To facilitate a deeper understanding, it is often helpful to first consider *when* to use [[bayes_theorem_and_its_significance | Bayes' theorem]] through examples, before dissecting the formula itself <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## The Steve Example: Librarian or Farmer?

This example, from a study by psychologists Daniel Kahneman and Amos Tversky, illustrates a common human judgment error in probability <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Their work on [[human_judgment_and_probability_misconceptions | human judgments and probability misconceptions]] earned a Nobel Prize <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

Consider the following description of a man named Steve:
> Steve is very shy and withdrawn, invariably helpful but with very little interest in people or the world of reality. A meek and tidy soul, he has a need for order and structure, and a passion for detail <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

Which is more likely: Steve is a librarian, or Steve is a farmer? <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>

According to Kahneman and Tversky, most people conclude Steve is more likely to be a librarian because his traits align with the stereotypical view of a librarian <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. However, this conclusion is considered irrational because it often fails to incorporate the *base rate* information: the ratio of farmers to librarians in the population <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

At the time of the study, the ratio of farmers to librarians in the US was about 20 to 1 <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. Rationality involves recognizing which facts are relevant, not just knowing facts <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### Reasoning with a Representative Sample

To reason about Steve's profession using [[introduction_to_bayesian_statistics | Bayesian reasoning]], one can imagine a representative sample <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>:
1.  **Start with the prior:** Assume a group reflecting the population ratio, for instance, 200 farmers and 10 librarians <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
2.  **Apply the evidence (likelihood):** Estimate how many in each group fit the description. For example:
    *   40% of librarians fit the description (0.40 * 10 librarians = 4 librarians) <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
    *   10% of farmers fit the description (0.10 * 200 farmers = 20 farmers) <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
3.  **Calculate the posterior:** Of those who fit the description (4 librarians + 20 farmers = 24 people), the probability that a random person is a librarian is 4 out of 24, or approximately 16.7% <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

Even if a librarian is four times more likely to fit the description than a farmer, the significantly larger number of farmers means it's still more probable that Steve is a farmer <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

The core mantra underlying [[bayes_theorem_and_its_significance | Bayes' theorem]] is that new evidence does not completely determine your beliefs in a vacuum; it should *update* prior beliefs <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

## Formulating Bayes' Theorem

[[Bayes' theorem]] is relevant when you have a **hypothesis (H)** (e.g., Steve is a librarian) and new **evidence (E)** (e.g., Steve's description), and you want to know the probability of the hypothesis given the evidence, written as **P(H|E)** <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. The vertical bar "|" means "given that," indicating a restriction to possibilities where the evidence holds <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

The formula involves three key components:
1.  **Prior (P(H))**: The probability of the hypothesis before considering new evidence <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. In the Steve example, this was 1/21 (1 librarian out of 21 people, considering the 20:1 farmer-to-librarian ratio) <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
2.  **Likelihood (P(E|H))**: The probability of seeing the evidence given that the hypothesis is true <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. This represents the proportion of librarians who fit Steve's description <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
3.  **P(E|¬H)**: The probability of seeing the evidence given that the hypothesis is *not* true. The symbol "¬" means "not" <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. This represents the proportion of non-librarians (farmers) who fit Steve's description <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

The final answer, **P(H|E)**, is called the **posterior**: your updated belief about the hypothesis after seeing the evidence <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

The complete formula for [[bayes_theorem_and_its_significance | Bayes' theorem]] is:
```
P(H|E) = [P(H) * P(E|H)] / P(E)
```
Where P(E), the total probability of seeing the evidence, can be broken down as:
```
P(E) = [P(H) * P(E|H)] + [P(¬H) * P(E|¬H)]
```
Substituting this, the full formula looks like:
```
P(H|E) = [P(H) * P(E|H)] / [P(H) * P(E|H) + P(¬H) * P(E|¬H)]
```
This formula allows for quantifying and systematizing the idea of changing beliefs, useful in fields like science (validating models), artificial intelligence (modeling machine belief), and even for personal reflection on how one's own opinions change <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

## Visualizing Probability with Geometry

Instead of memorizing the formula, it is beneficial to visualize [[bayes_theorem_and_its_significance | Bayes' theorem]] using a diagram, which is a distilled version of thinking with a representative sample but using areas instead of counts <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. This approach leverages [[using_geometry_for_understanding_probability | geometry for understanding probability]] and is more flexible for sketching <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

Imagine the space of all possibilities as a 1x1 square <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. Any event occupies a subset of this space, and its probability is represented by the area of that subset <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. For example, the hypothesis (H) could occupy the left part of the square with a width proportional to P(H) <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

When evidence (E) is observed, the space of possibilities is restricted <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. This restriction might not be uniform across different parts of the space. The new probability for the hypothesis (P(H|E)) becomes the proportion it occupies within this restricted, evidence-consistent shape <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. If the likelihood of the evidence is the same whether the hypothesis is true or not, then the evidence is irrelevant, and beliefs do not change <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>. However, when likelihoods differ significantly, beliefs change considerably <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

Geometrically, P(H) multiplied by P(E|H) represents the area where both the hypothesis and the evidence occur together <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

## Enhancing Probability Intuition

Beyond [[bayes_theorem_and_its_significance | Bayes' theorem]], several general takeaways can make probability more intuitive:

### The Power of Representative Samples
Thinking about a representative sample with specific numbers, like the 210 librarians and farmers, is highly beneficial <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.

Another Kahneman and Tversky experiment, known as the "Linda problem," highlights this <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. Participants were given a description of Linda:
> Linda is 31 years old, single, outspoken, and very bright. She majored in philosophy. As a student she was deeply concerned with issues of discrimination and social justice, and also participated in the anti-nuclear demonstrations <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

They were then asked which was more likely:
1.  Linda is a bank teller.
2.  Linda is a bank teller and is active in the feminist movement <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.

Remarkably, 85% of participants chose option 2 <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. This is irrational because the set of "bank tellers who are active in the feminist movement" is a *subset* of "bank tellers," meaning it must be smaller <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.

However, when the question was rephrased using counts, the error rate dropped to 0% <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>. If participants were told, "There are 100 people who fit this description," and asked how many are bank tellers versus how many are bank tellers *and* active in the feminist movement, everyone correctly assigned a higher number to the first option <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>. Phrases like "40 out of 100" activate intuition more effectively than "40%" or "0.4" <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.

### Probability as Proportions and Geometry
While representative samples are great for discrete scenarios, [[applications_of_probability_density | using geometry for understanding probability]] is helpful for continuous probability and for quick sketching during problem-solving <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. The math of probability fundamentally deals with proportions <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. When viewed as a statement about proportions (of people, areas, etc.), [[bayes_theorem_and_its_significance | Bayes' theorem]] becomes quite intuitive <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>. It essentially states that to find the proportion of cases where the evidence is true that also have the hypothesis true, you can compute it using the parts on the right-hand side of the formula <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.

Ultimately, the profound insight from [[bayes_theorem_and_its_significance | Bayes' theorem]] is that evidence should *update* beliefs rather than determine them entirely <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>. Reprogramming one's intuition to reflect this mathematical implication can greatly enhance understanding <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.