---
title: Measure theory in probability
videoId: ZA4JkHKZM50
---

From: [[3blue1brown]] <br/> 

The concept of [[probability_and_information_measurement | probability]] can become complex when dealing with continuous values, such as the unknown weight `h` of a coin that could be any real number between 0 and 1 <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This leads to a particular challenge when asking for the probability of a specific continuous value, like `h` being precisely 0.7 <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## Addressing the Paradox of Continuous Probabilities

### The Challenge: Probability of Probabilities
A "probability of a probability" question, such as asking for the likelihood that the true probability of flipping heads is 0.7, can be difficult to conceptualize <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. The unknown value itself is a long-run frequency for a random event <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

### The Problem with Individual Values
The more pressing issue arises when considering probabilities in the setting of continuous values <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. If every specific value within a continuous range (an uncountably infinite number of them) had a non-zero probability, even minuscule, their sum would "blow up to infinity" <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. Conversely, if all individual probabilities were zero, their sum would be zero, but it should be one, as the coin's weight `h` *is* some value <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. This presents an apparent paradox <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Resolution: Probability Density Functions

The key to resolving this paradox is to focus not on individual values, but on ranges of values <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

### Area Represents Probability
Instead of the height of a bar representing probability, the *area* of the bar should represent the probability for a given range <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. As these ranges (or "buckets") become finer and finer, the probability of falling into any one bucket approaches zero due to its thinner width, while the heights remain roughly the same <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. This process approaches a smooth curve <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>, preserving and refining the overall shape of the distribution <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

### Introducing Probability Density
Since probability is represented by area (width times height), the height of this curve represents a "probability per unit in the x-direction," known as a **probability density** <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. Associating a probability density to each value in a continuous range gives rise to a **probability density function (PDF)** <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

### Interpreting a PDF
When encountering a PDF, the probability of a random variable lying between two values is given by the area under the curve between those values <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
*   The probability of getting one very specific number (e.g., 0.7) is 0, because the area of an infinitely thin slice is 0 <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   The total probability of all possible values put together is 1, as the area under the full curve is 1 <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
This approach effectively sidesteps the paradox <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

## The Role of Measure Theory

The shift in rules from a finite setting (where probabilities sum) to a continuous one (where probabilities are areas) can be unsettling <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. Mathematicians address this through [[the_concept_of_measure_theory | measure theory]] <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

[[the_concept_of_measure_theory | Measure theory]] is a field of mathematics that provides a rigorous foundation for associating numbers (like probabilities) to various subsets of all possibilities in a way that combines and distributes consistently <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. It unifies the treatment of discrete and continuous settings <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

### Handling Mixed Distributions
[[the_concept_of_measure_theory | Measure theory]] smoothly handles situations that are a hybrid of discrete and continuous contexts <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. For example, a random number that equals 0 with 50% [[probability_and_information_measurement | probability]], and for the remaining 50% follows a continuous distribution like half of a bell curve, is precisely the sort of scenario [[the_concept_of_measure_theory | measure theory]] manages <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### Integrals as Continuous Sums
A common rule of thumb is to use an integral in a continuous context where a sum would be used in a discrete context <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. Integrals are the calculus tool used to find areas under curves <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. The theoretical underpinnings of integrals reveal a more powerful definition based on [[the_concept_of_measure_theory | measure theory]], which serves as the formal foundation of [[probability_and_information_measurement | probability]] <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

Ultimately, the understanding of continuous probabilities clicked for many when it was realized that the rules for combining probabilities of different sets were not what was intuitively assumed, and a different axiom system, provided by [[the_concept_of_measure_theory | measure theory]], underpins it all <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.