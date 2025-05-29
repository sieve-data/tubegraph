---
title: Rationality in human judgment
videoId: HZGCoVF3YvM
---

From: [[3blue1brown]] <br/> 

Human judgment often deviates from the laws of probability, a phenomenon extensively studied by psychologists Daniel Kahneman and Amos Tversky <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>. Their Nobel Prize-winning work, popularized in books like Kahneman's *Thinking, Fast and Slow*, focuses on instances where judgments [[bayesian_probability_concepts_and_bayes_rule | irrationally contradict probabilistic laws]] <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>. Understanding these deviations is crucial for grasping [[bayesian_probability_concepts_and_bayes_rule | Bayes' theorem]], a fundamental formula in probability central to scientific discovery, machine learning, and AI <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## The Steve Example: Librarian or Farmer?

One classic example used by Kahneman and Tversky to illustrate human judgment biases is the "Steve" problem <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.

### The Scenario
Participants are given a description of Steve: "Steve is very shy and withdrawn, invariably helpful but with very little interest in people or the world of reality. A meek and tidy soul, he has a need for order and structure, and a passion for detail" <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. They are then asked which is more likely: Steve is a librarian, or Steve is a farmer <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>.

### Intuitive vs. Probabilistic Reasoning
Most people tend to say Steve is more likely a librarian, aligning with stereotypical traits <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>. However, this response is considered irrational by Kahneman and Tversky because it typically fails to incorporate the base rate information regarding the ratio of farmers to librarians in the population <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>. In the US, the ratio of farmers to librarians was about 20 to 1 at the time of their paper <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>.

### Applying [[bayesian_probability_concepts_and_bayes_rule | Bayesian Probability Concepts and Bayes Rule]]
To reason about this question more accurately, one might consider a representative sample:
*   Imagine 200 farmers and 10 librarians (a 20:1 ratio) <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>.
*   Assume 40% of librarians fit Steve's description (4 librarians) and 10% of farmers fit it (20 farmers) <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>.
*   Among those who fit the description (4 librarians + 20 farmers = 24 people), the probability that a random person is a librarian is 4 out of 24, or 16.7% <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>.
*   Even if a librarian is four times as likely to fit the description, the much larger population of farmers means a farmer is still more probable <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>.

This demonstrates the core principle of [[bayesian_approach_to_updating_beliefs_with_new_evidence | Bayesian approach to updating beliefs with new evidence]]: new evidence does not completely determine beliefs in a vacuum; it should *update* prior beliefs <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>. [[bayesian_probability_concepts_and_bayes_rule | Bayes' theorem]] formalizes how to combine prior probabilities (like the base rate of farmers to librarians) with likelihoods (how well the description fits each group) to arrive at a posterior probability (the updated belief) <a class="yt-timestamp" data-t="07:40:00">[07:40:00]</a>.

## The Linda Example: Conjunction Fallacy

Another finding from Kahneman and Tversky highlights the "conjunction fallacy":
*   Participants were given a description of Linda: "Linda is 31 years old, single, outspoken, and very bright. She majored in philosophy. As a student she was deeply concerned with issues of discrimination and social justice, and also participated in the anti-nuclear demonstrations" <a class="yt-timestamp" data-t="10:46:00">[10:46:00]</a>.
*   They were then asked what's more likely:
    1.  Linda is a bank teller.
    2.  Linda is a bank teller and is active in the feminist movement <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>.
*   A significant majority (85%) chose option 2 <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>. This is irrational because the set of bank tellers who are active in the feminist movement is a subset of all bank tellers, and thus must be smaller <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>.

Interestingly, this error dropped from 85% to 0 when the question was rephrased using frequencies instead of probabilities. If participants were asked to estimate how many out of 100 people fitting Linda's description were bank tellers versus bank tellers active in the feminist movement, nobody made the error <a class="yt-timestamp" data-t="11:34:00">[11:34:00]</a>. This suggests that phrases like "40 out of 100" activate intuition more effectively than percentages or abstract likelihoods <a class="yt-timestamp" data-t="11:54:00">[11:54:00]</a>.

## Making Probability Intuitive

### Representative Samples and Frequencies
Thinking about a "representative sample" with specific numbers, like 210 librarians and farmers, helps make probability more intuitive <a class="yt-timestamp" data-t="10:23:00">[10:23:00]</a>. This approach of using frequencies instead of abstract probabilities can significantly improve human judgment, as seen in the Linda example <a class="yt-timestamp" data-t="11:34:00">[11:34:00]</a>.

### Geometric Intuition
While representative samples are helpful, they don't easily capture the continuous nature of probability. A beneficial alternative is to use area for visualizing probabilities, effectively [[converting_analytic_reasoning_to_geometric_intuition | converting analytic reasoning to geometric intuition]] <a class="yt-timestamp" data-t="12:09:00">[12:09:00]</a>. For instance, the space of all possibilities can be thought of as a 1x1 square, where the probability of an event is represented by the area of a subset within that square <a class="yt-timestamp" data-t="09:02:00">[09:02:00]</a>. When evidence restricts the possibilities, the new probability is the proportion of the hypothesis within that restricted space <a class="yt-timestamp" data-t="09:22:00">[09:22:00]</a>.

## Recognizing Relevant Facts

Rationality is not about knowing every fact, but about discerning which facts are relevant to a given judgment <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>. For example, in the Steve problem, the crucial insight was to consider the base rate of farmers to librarians <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>.

## Debates and Conclusion

While Kahneman and Tversky's conclusions about human irrationality have been debated (e.g., questions about the ambiguity of context or assumptions about random sampling) <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>, the ultimate principle remains: **evidence should not determine beliefs, but update them** <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>. Whether this aligns with natural human instinct or requires "reprogramming our intuition" <a class="yt-timestamp" data-t="14:38:00">[14:38:00]</a>, the mathematical implications of [[bayesian_probability_concepts_and_bayes_rule | Bayes' theorem]] provide a framework for quantifying and systematizing this process of belief change <a class="yt-timestamp" data-t="08:02:00">[08:02:00]</a>. This understanding is invaluable for science, artificial intelligence, and refining how we approach our own opinions and mental processes <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>.