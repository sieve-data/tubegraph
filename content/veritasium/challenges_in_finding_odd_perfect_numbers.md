---
title: Challenges in finding odd perfect numbers
videoId: Zrv1EDIqHkY
---

From: [[veritasium]] <br/> 

The existence of odd [[perfect_numbers_and_their_properties | perfect numbers]] is one of the [[oldest_unsolved_problem_in_mathematics | oldest unsolved problems in math]], dating back 2000 years <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Despite attempts by some of the brightest [[history_and_contributions_of_mathematicians_to_perfect_numbers | mathematicians]] throughout history, this problem remains unsolved <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. In 2000, Italian [[history_and_contributions_of_mathematicians_to_perfect_numbers | mathematician]] Piergiorgio Odifreddi listed it among four of the most pressing open problems <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Solving it could be as simple as finding a single number <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>, yet computers have checked numbers up to 10<sup>2200</sup> without success <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## What is a Perfect Number?
A [[perfect_numbers_and_their_properties | perfect number]] is a positive integer that is equal to the sum of its proper divisors (divisors excluding the number itself) <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Example: 6**
    *   Proper divisors: 1, 2, 3 <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>
    *   Sum: 1 + 2 + 3 = 6 <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>
    *   Since the sum equals the number, 6 is a [[perfect_numbers_and_their_properties | perfect number]] <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   **Example: 10**
    *   Proper divisors: 1, 2, 5 <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>
    *   Sum: 1 + 2 + 5 = 8 <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>
    *   Since the sum (8) does not equal the number (10), 10 is not a [[perfect_numbers_and_their_properties | perfect number]] <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

Between 1 and 100, only 6 and 28 are [[perfect_numbers_and_their_properties | perfect numbers]] <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. Up to 10,000, the next two are 496 and 8,128 <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. These four were the only [[perfect_numbers_and_their_properties | perfect numbers]] known by the ancient Greeks and for over a thousand years <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## Properties of Even Perfect Numbers
All known [[perfect_numbers_and_their_properties | perfect numbers]] share several properties <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>:
*   Each subsequent [[perfect_numbers_and_their_properties | perfect number]] is one digit longer than the previous one <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   Their ending digit alternates between 6 and 8, meaning they are all even <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   They are all triangular numbers (sum of consecutive integers) <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   Every [[perfect_numbers_and_their_properties | perfect number]] except 6 is the sum of consecutive odd cubes <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a> (e.g., 28 = 1³ + 3³ <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>).
*   When written in binary, they are a string of ones followed by a series of zeros <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

### Euclid's Formula for Even Perfect Numbers
Around 300 BC, [[history_and_contributions_of_mathematicians_to_perfect_numbers | Euclid]] discovered a pattern for generating [[perfect_numbers_and_their_properties | perfect numbers]] <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>:
*   Start with 1, double it (2, 4, 8, 16, etc.) <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   Sum these powers of two (e.g., 1 + 2 = 3) <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   If the sum is a [[mersenne_primes_and_their_significance | prime]] number, multiply it by the last power of two in the sum <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
    *   (1+2) * 2 = 3 * 2 = 6 (first [[perfect_numbers_and_their_properties | perfect number]]) <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>
    *   (1+2+4) * 4 = 7 * 4 = 28 (second [[perfect_numbers_and_their_properties | perfect number]]) <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>
    *   (1+2+4+8+16) * 16 = 31 * 16 = 496 (third [[perfect_numbers_and_their_properties | perfect number]]) <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>
*   This formula can be expressed as 2<sup>P-1</sup> * (2<sup>P</sup> - 1), where (2<sup>P</sup> - 1) is a [[mersenne_primes_and_their_significance | prime]] number <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   Since the formula includes multiplication by an even number (2<sup>P-1</sup>), it always generates an even [[perfect_numbers_and_their_properties | perfect number]] <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

## The Quest for Odd Perfect Numbers

[[history_and_contributions_of_mathematicians_to_perfect_numbers | Euclid]] found a way to generate even [[perfect_numbers_and_their_properties | perfect numbers]], but he did not prove that it was the *only* way <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. This left open the possibility of [[perfect_numbers_and_their_properties | odd perfect numbers]] <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

### Nicomachus's Conjectures
Around 400 years later, the Greek philosopher Nicomachus published *Introductio Arithmetica*, stating five conjectures about [[perfect_numbers_and_their_properties | perfect numbers]] <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>:
1.  The nth [[perfect_numbers_and_their_properties | perfect number]] has n digits <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. (Disproved by Ibn Fallus's fifth [[perfect_numbers_and_their_properties | perfect number]], which was 8 digits long <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.)
2.  All [[perfect_numbers_and_their_properties | perfect numbers]] are even <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. (Still an open question).
3.  All [[perfect_numbers_and_their_properties | perfect numbers]] end in 6 and 8 alternately <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. (Disproved by Ibn Fallus's fifth and sixth [[perfect_numbers_and_their_properties | perfect numbers]], both ending in 6 <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.)
4.  [[history_and_contributions_of_mathematicians_to_perfect_numbers | Euclid's]] algorithm produces every even [[perfect_numbers_and_their_properties | perfect number]] <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. (Proven true by [[history_and_contributions_of_mathematicians_to_perfect_numbers | Euler]] <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.)
5.  There are infinitely many [[perfect_numbers_and_their_properties | perfect numbers]] <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. (Still an open question, though evidence suggests it's true for even ones <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>.)

### Contributions of [[history_and_contributions_of_mathematicians_to_perfect_numbers | Descartes]] and [[history_and_contributions_of_mathematicians_to_perfect_numbers | Euler]]

[[history_and_contributions_of_mathematicians_to_perfect_numbers | Rene Descartes]] in 1638, though unable to prove it, conjectured that if an odd [[perfect_numbers_and_their_properties | perfect number]] exists, "it must be the product of a [[mersenne_primes_and_their_significance | prime]] and the square of a different number" <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

[[history_and_contributions_of_mathematicians_to_perfect_numbers | Leonhard Euler]], a century later, picked up where [[history_and_contributions_of_mathematicians_to_perfect_numbers | Descartes]] left off <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. He made three significant breakthroughs:
1.  Discovered the eighth [[perfect_numbers_and_their_properties | perfect number]] in 1732, by verifying that 2<sup>31</sup> - 1 is a [[mersenne_primes_and_their_significance | prime]] <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
2.  Invented the [[history_and_contributions_of_mathematicians_to_perfect_numbers | sigma function]] <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a> (sum of all divisors including the number itself). Using this, [[history_and_contributions_of_mathematicians_to_perfect_numbers | Euler]] proved the [[history_and_contributions_of_mathematicians_to_perfect_numbers | Euclid-Euler theorem]]: *every even [[perfect_numbers_and_their_properties | perfect number]] has [[history_and_contributions_of_mathematicians_to_perfect_numbers | Euclid's]] form* <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. This solved a 1600-year-old problem and proved Nicomachus's fourth conjecture <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>.
3.  [[history_and_contributions_of_mathematicians_to_perfect_numbers | Euler]] then sought to prove [[history_and_contributions_of_mathematicians_to_perfect_numbers | Descartes']] statement about the form of odd [[perfect_numbers_and_their_properties | perfect numbers]] <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>. He proved that if an odd [[perfect_numbers_and_their_properties | perfect number]] exists, it must have exactly one [[mersenne_primes_and_their_significance | prime]] factor raised to an odd power, and all other [[mersenne_primes_and_their_significance | prime]] factors must be raised to an even power <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>. This is known as [[history_and_contributions_of_mathematicians_to_perfect_numbers | Euler's]] theorem on odd [[perfect_numbers_and_their_properties | perfect numbers]].

Despite this refinement, [[history_and_contributions_of_mathematicians_to_perfect_numbers | Euler]] could not prove or disprove their existence, calling it "a most difficult question" <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.

### Modern Challenges and Approaches

The challenges in finding odd [[perfect_numbers_and_their_properties | perfect numbers]] include:

#### Enormous Size
Researchers have used algorithms to establish lower bounds for the size of any potential odd [[perfect_numbers_and_their_properties | perfect number]] <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>:
*   In 1991, it was shown that an odd [[perfect_numbers_and_their_properties | perfect number]], if it exists, must be larger than 10<sup>300</sup> <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>.
*   By 2012, Pascal Ochem and Michael Rao raised this bound to 10<sup>1500</sup> <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>.
*   Recent progress has pushed this number up to 10<sup>2200</sup> <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.
Numbers this large make it unlikely a computer will find one by brute force anytime soon <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.

#### "Web of Conditions"
The primary approach to solving the problem is to derive more and more conditions that odd [[perfect_numbers_and_their_properties | perfect numbers]] must satisfy <a class="yt-timestamp" data-t="00:23:15">[00:23:15]</a>. This "web of conditions" includes properties like:
*   Having a minimum number of [[mersenne_primes_and_their_significance | prime]] factors (e.g., at least 10 [[mersenne_primes_and_their_significance | prime]] factors) <a class="yt-timestamp" data-t="00:23:26">[00:23:26]</a>.
*   Being larger than 10<sup>3000</sup> <a class="yt-timestamp" data-t="00:23:35">[00:23:35]</a>.
The hope is that eventually, the sheer number of constraints will make their existence impossible, thus proving that they don't exist <a class="yt-timestamp" data-t="00:23:40">[00:23:40]</a>.

#### Spoofs
Numbers that are "very close" to being odd [[perfect_numbers_and_their_properties | perfect numbers]] are called "spoofs" <a class="yt-timestamp" data-t="00:24:34">[00:24:34]</a>. Odd [[perfect_numbers_and_their_properties | perfect numbers]] share all properties of spoofs plus a few extra ones <a class="yt-timestamp" data-t="00:24:40">[00:24:40]</a>. The goal is to find properties of spoofs that prevent them from being odd [[perfect_numbers_and_their_properties | perfect numbers]] <a class="yt-timestamp" data-t="00:24:48">[00:24:48]</a>. For example, if it were proven that spoofs must be divisible by 105, and odd [[perfect_numbers_and_their_properties | perfect numbers]] cannot be divisible by 105, this would prove their non-existence <a class="yt-timestamp" data-t="00:24:55">[00:24:55]</a>. In 2022, Pace Nielsen and a team at BYU found 21 spoof numbers, including one identified by [[history_and_contributions_of_mathematicians_to_perfect_numbers | Descartes]], and identified new properties of spoofs, but none that rule out odd [[perfect_numbers_and_their_properties | perfect numbers]] <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>.

#### Heuristic Arguments
Some [[mathematicians]] believe odd [[perfect_numbers_and_their_properties | perfect numbers]] do not exist <a class="yt-timestamp" data-t="00:25:27">[00:25:27]</a>. Carl Pomerance put forward a "heuristic argument" which suggests that based on the frequency of certain types of [[mersenne_primes_and_their_significance | primes]], there should be no odd [[perfect_numbers_and_their_properties | perfect numbers]] <a class="yt-timestamp" data-t="00:26:09">[00:26:09]</a>. While not a proof, this argument suggests that "on average" numbers of the required form should not be [[perfect_numbers_and_their_properties | perfect]] <a class="yt-timestamp" data-t="00:26:05">[00:26:05]</a>. However, this same heuristic also predicts no large *even* [[perfect_numbers_and_their_properties | perfect numbers]], which contradicts the current expectation of infinitely many even ones <a class="yt-timestamp" data-t="00:26:40">[00:26:40]</a>.

## Why Pursue an "Useless" Problem?
Despite the problem having no known real-world applications <a class="yt-timestamp" data-t="00:27:32">[00:27:32]</a>, its pursuit highlights a fundamental aspect of mathematics:
*   For over 2000 years, number theory was considered to have no real-world applications, yet it formed a foundation later used for cryptography <a class="yt-timestamp" data-t="00:27:50">[00:27:50]</a>.
*   Similarly, [[challenges_in_solving_einsteins_equations | Einstein's general relativity]] was built on non-[[history_and_contributions_of_mathematicians_to_perfect_numbers | Euclidean geometries]], which were developed purely as intellectual curiosities <a class="yt-timestamp" data-t="00:28:45">[00:28:45]</a>.
*   Engaging with such problems, even if they initially seem without practical use, leads to new ideas and processes that can later have unforeseen applications <a class="yt-timestamp" data-t="00:28:16">[00:28:16]</a>. Around 10-15 [[mathematicians]] are currently publishing papers in this area <a class="yt-timestamp" data-t="00:29:02">[00:29:02]</a>.
*   The act of solving the math is the only way to know for sure what its outcome or implications will be <a class="yt-timestamp" data-t="00:29:33">[00:29:33]</a>.