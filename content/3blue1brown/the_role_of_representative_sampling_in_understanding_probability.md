---
title: The role of representative sampling in understanding probability
videoId: HZGCoVF3YvM
---

From: [[3blue1brown]] <br/> 

Understanding complex probability concepts, particularly those related to [[bayesian_probability_concepts_and_bayes_rule | Bayes' theorem]], can be greatly aided by picturing a representative sample of individuals or events <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. This approach transforms abstract probabilities into concrete numbers or proportions, making the underlying logic more intuitive <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.

## Intuition through Representative Samples

When faced with a question involving probabilities, using a representative sample can simplify the reasoning process <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. Instead of directly manipulating percentages or abstract likelihoods, one can imagine a specific number of individuals within defined groups <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. The specific total number chosen for the sample is arbitrary, as it ultimately cancels out in the calculation, but it serves as a useful visualization tool <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

For example, in the "Steve" problem, where the goal is to determine if Steve is more likely to be a librarian or a farmer based on a personality description, a representative sample can be employed <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
If the ratio of farmers to librarians in the US is approximately 20 to 1, one might picture a sample of 200 farmers and 10 librarians <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a><a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. Then, by estimating that perhaps 40% of librarians fit the description and 10% of farmers fit it, one can calculate:
*   4 librarians fit the description (40% of 10) <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>
*   20 farmers fit the description (10% of 200) <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>

This makes it clear that among those fitting the description, 4 out of 24 (or 16.7%) are librarians <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a><a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. This tangible representation helps in understanding that even if a librarian is four times more likely to fit the description, the sheer number of farmers can outweigh that likelihood <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a><a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. This line of reasoning embodies the core of [[bayesian_probability_concepts_and_bayes_rule | Bayes' theorem]]: new evidence updates, rather than completely determines, prior beliefs <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a><a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a><a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

## Overcoming Cognitive Biases

The psychological research of Daniel Kahneman and Amos Tversky highlights how thinking in terms of specific counts rather than abstract probabilities can mitigate common cognitive errors <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a><a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

### The Linda Problem
In one famous experiment, participants were given a description of a woman named Linda and asked to assess the likelihood of two statements:
1.  Linda is a bank teller.
2.  Linda is a bank teller and is active in the feminist movement.
<a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>

A significant majority (85%) incorrectly stated that the second option was more likely, even though the set of "bank tellers who are active in the feminist movement" is a subset of "bank tellers" and therefore must be smaller <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a><a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a><a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.

However, when the question was rephrased to use a representative sample, the error rate dropped to zero <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a><a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>. Participants were told to imagine 100 people fitting Linda's description and then asked to estimate how many were "bank tellers" versus "bank tellers active in the feminist movement" <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a><a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>. In this format, everyone correctly assigned a higher number to the broader category <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a><a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

This demonstrates that phrases like "40 out of 100" activate intuition more effectively than "40%" or "0.4," or abstract ideas of likelihood <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a><a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.

## Limitations and Alternatives

While helpful for discrete problems, representative samples with specific counts may not easily capture the continuous nature of probability <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a><a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. In such cases, visualizing probabilities as areas within a 1x1 square can be a useful alternative <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a><a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. This geometric approach maintains the "proportions" logic central to probability math, offering flexibility for sketching problems <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a><a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a><a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>.

Ultimately, whether using specific counts or abstract areas, the core idea is to transform the study of uncertainty into the math of proportions <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a><a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a><a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a><a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>. This helps make concepts like [[bayesian_probability_concepts_and_bayes_rule | Bayes' theorem]], which is a straightforward fact about proportions, intuitively obvious <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a><a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a><a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.