---
title: Introduction to probability
videoId: uzkc-qNVoOk
---

From: [[khanacademy]] <br/> 

[[understanding_probability_concepts | Probability]] provides a basic overview of quantifying the chances of fundamentally random events <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. It helps to describe the likelihood of specific outcomes for an [[trial_and_event_in_probability | event]] where the result is uncertain <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Conceptualizing Probability

There are two primary ways to understand and [[calculating_probability | calculate probability]]:

### 1. Ratio of Equally Likely Possibilities
This method is commonly introduced in textbooks <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a> and involves a simple formula:

$$P(\text{event}) = \frac{\text{Number of possibilities that meet the conditions}}{\text{Number of equally likely possibilities}} \tag{00:01:59}$$

#### Example: Flipping a Fair Coin
A "fair coin" is one that has an equal chance of landing on either side, meaning its weight is distributed evenly <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. The two possible outcomes are heads or tails <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

*   **Question:** What is the [[understanding_probability_concepts | probability]] of getting heads? <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>
*   **Equally likely possibilities:** There are two equally likely possibilities: heads or tails <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **Possibilities that meet conditions:** Only one possibility meets the condition of getting heads <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   **Calculation:**
    $$P(\text{Heads}) = \frac{1 \text{ (Heads)}}{2 \text{ (Total possibilities)}} = \frac{1}{2} \tag{00:02:46}$$
    This can also be expressed as 50% <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

#### Example: Rolling a Fair Die
A "fair die" has six equally likely possibilities when rolled: 1, 2, 3, 4, 5, or 6 <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

*   **Question:** What is the [[understanding_probability_concepts | probability]] of getting a 1? <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>
*   **Equally likely possibilities:** There are six equally likely possibilities <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   **Possibilities that meet conditions:** Only one possibility meets the condition of rolling a 1 <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
*   **Calculation:**
    $$P(\text{1}) = \frac{1}{6} \tag{00:06:03}$$

*   **Question:** What is the [[understanding_probability_concepts | probability]] of getting a 1 or a 6? <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>
*   **Equally likely possibilities:** Six equally likely possibilities <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
*   **Possibilities that meet conditions:** Two possibilities meet the conditions: rolling a 1 or rolling a 6 <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
*   **Calculation:**
    $$P(\text{1 or 6}) = \frac{2}{6} = \frac{1}{3} \tag{00:06:38}$$

*   **Question:** What is the [[understanding_probability_concepts | probability]] of getting an even number? <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>
*   **Equally likely possibilities:** Six equally likely possibilities <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
*   **Possibilities that meet conditions:** The even numbers are 2, 4, and 6, so three possibilities meet the conditions <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   **Calculation:**
    $$P(\text{Even number}) = \frac{3}{6} = \frac{1}{2} \tag{00:08:11}$$

*   **Question:** What is the [[understanding_probability_concepts | probability]] of rolling a 2 and a 3 on a single roll? <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>
    *   This is impossible on a single roll of a standard die, as getting a 2 and a 3 are [[trial_and_event_in_probability | mutually exclusive events]] <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. The [[understanding_probability_concepts | probability]] is 0 <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

### 2. Long-Run Frequency
This method conceptualizes [[understanding_probability_concepts | probability]] by considering what would happen if an [[trial_and_event_in_probability | experiment]] (a random [[trial_and_event_in_probability | event]]) were repeated many, many times <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

*   If an [[trial_and_event_in_probability | experiment]] is conducted a large number of times (e.g., thousands, millions, or even an infinite number of times), the percentage of outcomes that meet a specific condition will approach the theoretical [[understanding_probability_concepts | probability]] <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
*   **Example:** If you flip a fair coin an infinite number of times, approximately 50% of those flips will result in heads <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **Practical Application:** You can simulate this by taking many coins, shaking them in a box, and counting the heads. The larger the number of coins, the closer the observed percentage of heads will be to 50% <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. Even with a million flips, there's a tiny chance of not getting exactly 50% heads, but the trend will always be towards that theoretical value <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.