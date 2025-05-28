---
title: Perfect numbers and their properties
videoId: Zrv1EDIqHkY
---

From: [[veritasium]] <br/> 

The question of whether [[challenges_in_finding_odd_perfect_numbers | odd perfect numbers]] exist is considered the oldest unsolved problem in mathematics, dating back 2000 years <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It was listed by Italian mathematician Piergiorgio Odifreddi in 2000 among four of the most pressing open problems <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Mathematicians have used computers to check numbers up to 10 to the power of 2,200, but no [[challenges_in_finding_odd_perfect_numbers | odd perfect numbers]] have been found <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## What is a Perfect Number?

A perfect number is a positive integer that is equal to the sum of its proper divisors (divisors excluding the number itself) <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

### Examples of Perfect Numbers
*   **6**: Its proper divisors are 1, 2, and 3. Adding them up (1 + 2 + 3) equals 6, making it a perfect number <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   **28**: This is also a perfect number <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

Most numbers either overshoot or undershoot when their proper divisors are summed <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. For example, the proper divisors of 10 (1, 2, 5) sum to 8, so 10 is not perfect <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

Between 1 and 100, only 6 and 28 are perfect numbers <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. Going up to 10,000, the next two perfect numbers are 496 and 8,128 <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. These four numbers were the only perfect numbers known to the ancient Greeks and for over a thousand years thereafter <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## Properties of Known Perfect Numbers

Early perfect numbers reveal several interesting patterns:
*   Each successive perfect number is one digit longer than the previous one <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   The ending digit alternates between 6 and 8 <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   All known perfect numbers are even <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   They are [[hailstone_numbers_and_patterns | triangular numbers]], meaning they can be written as the sum of consecutive integers:
    *   6 = 1 + 2 + 3 <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>
    *   28 = 1 + 2 + 3 + 4 + 5 + 6 + 7 <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>
*   Every perfect number except 6 is the sum of consecutive odd cubes:
    *   28 = 1³ + 3³ <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>
    *   496 = 1³ + 3³ + 5³ + 7³ <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>
    *   8,128 = 1³ + 3³ + 5³ + 7³ + 9³ + ... + 15³ <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>
*   When written in binary, perfect numbers are a string of ones followed by a series of zeros, which corresponds to consecutive powers of two:
    *   6 = 110 (binary) <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>
    *   28 = 11100 (binary) <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>
    *   496 = 111110000 (binary) <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>
    *   8,128 is also of this form <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>

## Euclid's Formula for Even Perfect Numbers

Around 300 BC, [[history_and_contributions_of_mathematicians_to_perfect_numbers | Euclid]] discovered a pattern for generating even perfect numbers <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. His method involves powers of two:
1.  Start with 1, double it (2, 4, 8, 16, etc.) <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
2.  Sum these powers of two consecutively (1+2=3, 1+2+4=7, etc.) <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
3.  If the sum is a prime number, multiply it by the last power of two in the sequence to get a perfect number <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
    *   (1+2=3, which is prime) * 2 = 6 <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>
    *   (1+2+4=7, which is prime) * 4 = 28 <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>
    *   (1+2+4+8+16=31, which is prime) * 16 = 496 <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>

This pattern can be formalized. A sum of consecutive powers of two, from 2⁰ to 2^(n-1), is equal to 2^n - 1 <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
Thus, [[history_and_contributions_of_mathematicians_to_perfect_numbers | Euclid's formula]] for a perfect number is:
`2^(P-1) * (2^P - 1)` <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>

This formula generates a perfect number *whenever* `2^P - 1` is a [[mathematical_uniqueness_of_prime_numbers | prime]] number <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. Since the formula involves multiplication by an even number (2^(P-1)), it will always produce an even number <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. [[history_and_contributions_of_mathematicians_to_perfect_numbers | Euclid]] found a way to generate even perfect numbers, but he did not prove that this was the *only* way to get them, leaving open the possibility of [[challenges_in_finding_odd_perfect_numbers | odd perfect numbers]] <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

## Nicomachus's Conjectures

Four hundred years after [[history_and_contributions_of_mathematicians_to_perfect_numbers | Euclid]], the Greek philosopher Nicomachus published *Introductio Arithmetica*, a standard arithmetic text for the next thousand years <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. In it, he stated five conjectures about perfect numbers that he believed to be true but did not prove <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>:
1.  The nth perfect number has n digits <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
2.  All perfect numbers are even <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
3.  All perfect numbers end in 6 and 8 alternately <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
4.  [[history_and_contributions_of_mathematicians_to_perfect_numbers | Euclid's algorithm]] produces every even perfect number <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
5.  There are [[infinity_in_mathematics | infinitely many perfect numbers]] <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

For a millennium, these conjectures were considered facts <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. However, in the 13th century, Egyptian mathematician [[history_and_contributions_of_mathematicians_to_perfect_numbers | Ibn Fallus]] published a list of 10 perfect numbers <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
*   The fifth perfect number was eight digits long, disproving Nicomachus's first conjecture <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
*   Both the fifth and sixth perfect numbers ended in 6, disproving Nicomachus's third conjecture about alternating 6 and 8 endings <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

## Mersenne Primes and Descartes' Contributions

The problem reached Renaissance Europe, leading to the rediscovery of the fifth, sixth, and seventh perfect numbers <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. All found perfect numbers so far adhered to [[history_and_contributions_of_mathematicians_to_perfect_numbers | Euclid's form]] <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. The key to finding new ones became identifying values of P that make `2^P - 1` prime <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

French polymath [[mersenne_primes_and_their_significance | Marin Mersenne]] extensively studied numbers of this form, publishing a list in 1644 of 11 values of P for which he claimed they corresponded to primes <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. Numbers of the form `2^P - 1` that are prime are now called [[mersenne_primes_and_their_significance | Mersenne Primes]] <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. The first seven exponents on his list did result in primes, corresponding to the first seven perfect numbers <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. [[mersenne_primes_and_their_significance | Mersenne]] acknowledged the difficulty of checking large numbers for primality <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

[[history_and_contributions_of_mathematicians_to_perfect_numbers | René Descartes]], corresponding with [[mersenne_primes_and_their_significance | Mersenne]], believed he could show that no even perfect numbers existed outside [[history_and_contributions_of_mathematicians_to_perfect_numbers | Euclid's form]] <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. He also conjectured that if an [[challenges_in_finding_odd_perfect_numbers | odd perfect number]] did exist, it must be the product of a prime and the square of a different number <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. However, [[history_and_contributions_of_mathematicians_to_perfect_numbers | Descartes]] could not prove either statement <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

## Euler's Breakthroughs

Around 100 years later, [[history_and_contributions_of_mathematicians_to_perfect_numbers | Leonhard Euler]] took up the problem <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
1.  In 1732, he discovered the eighth perfect number by verifying that `2^31 - 1` is prime, as [[mersenne_primes_and_their_significance | Mersenne]] had predicted <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
2.  For his second breakthrough, [[history_and_contributions_of_mathematicians_to_perfect_numbers | Euler]] invented the [[mathematical_uniqueness_of_prime_numbers | sigma function]], which sums all divisors of a number, including the number itself <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. For a perfect number, the [[mathematical_uniqueness_of_prime_numbers | sigma function]] returns twice the number itself <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. This function is powerful because it allows the `[[mathematical_uniqueness_of_prime_numbers | sigma function]]` of a composite number to be split into the `[[mathematical_uniqueness_of_prime_numbers | sigma functions]]` of its prime powers <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. Using this, [[history_and_contributions_of_mathematicians_to_perfect_numbers | Euler]] proved the **Euclid-Euler theorem**: every even perfect number has [[history_and_contributions_of_mathematicians_to_perfect_numbers | Euclid's form]] <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. This solved a 1600-year-old problem and proved Nicomachus's fourth conjecture <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>.
3.  For his third breakthrough, [[history_and_contributions_of_mathematicians_to_perfect_numbers | Euler]] proved [[history_and_contributions_of_mathematicians_to_perfect_numbers | Descartes']] conjecture about the specific form an [[challenges_in_finding_odd_perfect_numbers | odd perfect number]] must take <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>. Using the [[mathematical_uniqueness_of_prime_numbers | sigma function]], he showed that if an [[challenges_in_finding_odd_perfect_numbers | odd perfect number]] (n) exists, it must have exactly one prime factor raised to an odd power, while all other prime factors must be raised to an even power <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. This can be expressed as `n = p^k * m^2`, where `p` is a prime number and `k` is an odd exponent, and `m` is an integer <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. Despite this, [[history_and_contributions_of_mathematicians_to_perfect_numbers | Euler]] could not prove or disprove the existence of [[challenges_in_finding_odd_perfect_numbers | odd perfect numbers]] <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.

## The Modern Search for Perfect Numbers

After [[history_and_contributions_of_mathematicians_to_perfect_numbers | Euler]], progress in finding new perfect numbers stalled for 150 years <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. The focus shifted to verifying [[mersenne_primes_and_their_significance | Mersenne's]] list of proposed primes <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>.

*   In 1876, Edouard Lucas proved that `2^67 - 1` was not prime, disproving another of [[mersenne_primes_and_their_significance | Mersenne's]] claims <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>.
*   In 1903, Frank Nelson Cole famously demonstrated the factors of `2^67 - 1` manually at a meeting of the American Mathematical Society <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>.

The advent of computers revolutionized the search:
*   By 1952, only 12 [[mersenne_primes_and_their_significance | Mersenne Primes]] (and thus 12 perfect numbers) had been discovered <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.
*   In 1952, American mathematician Raphael Robinson wrote a computer program for the SWAC (Standards Western Automatic Computer) that found the next five [[mersenne_primes_and_their_significance | Mersenne Primes]] within 10 months <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   Over the next 50 years, new [[mersenne_primes_and_their_significance | Mersenne Primes]] were discovered rapidly using computers <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.

### Great Internet Mersenne Prime Search (GIMPS)

In 1996, computer scientist George Woltman launched the [[mersenne_primes_and_their_significance | Great Internet Mersenne Prime Search (GIMPS)]] <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>. This distributed computing project allows volunteers to contribute their computer's processing power to search for [[mersenne_primes_and_their_significance | Mersenne Primes]] <a class="yt-timestamp" data-t="00:19:09">[00:19:09]</a>.
*   [[mersenne_primes_and_their_significance | GIMPS]] has discovered 17 new [[mersenne_primes_and_their_significance | Mersenne Primes]], 15 of which were the largest known primes at the time <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>.
*   In 2017, John Pace discovered the 50th [[mersenne_primes_and_their_significance | Mersenne Prime]], `2^(77,232,917) - 1`, which is more than 23 million digits long <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>. A Japanese publisher even printed this number in a 719-page book <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>.
*   A year later, the 51st [[mersenne_primes_and_their_significance | Mersenne Prime]] was discovered, `2^(82,589,933) - 1`, which has over 24 million digits <a class="yt-timestamp" data-t="00:20:31">[00:20:31]</a>. This remains the largest known prime as of today <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>.

## The Enduring Question: Odd Perfect Numbers

As of today, only 51 perfect numbers have been found, all of which are even <a class="yt-timestamp" data-t="00:21:31">[00:21:31]</a>.

### Infinitely Many Perfect Numbers?
Nicomachus's fifth conjecture, that there are [[infinity_in_mathematics | infinitely many perfect numbers]], remains unproven <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. However, the Lenstra and Pomerance Wagstaff conjecture predicts an infinite number of [[mersenne_primes_and_their_significance | Mersenne Primes]], and thus [[infinity_in_mathematics | infinitely many even perfect numbers]] <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>. While this is a strong prediction, it is not a mathematical proof <a class="yt-timestamp" data-t="00:22:17">[00:22:17]</a>.

### The Search for Odd Perfect Numbers
The question of whether [[challenges_in_finding_odd_perfect_numbers | odd perfect numbers]] exist is still the oldest unsolved problem in mathematics <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.
*   **Computational Search**: In 1991, researchers used a factor chain algorithm to show that if an [[challenges_in_finding_odd_perfect_numbers | odd perfect number]] exists, it must be larger than 10^300 <a class="yt-timestamp" data-t="00:22:40">[00:22:40]</a>. This lower bound has been pushed up to 10^2200 <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>.
*   **"Web of Conditions"**: Mathematicians are attempting to prove the non-existence of [[challenges_in_finding_odd_perfect_numbers | odd perfect numbers]] by defining more and more conditions that such a number would have to satisfy (e.g., number of prime factors, size) <a class="yt-timestamp" data-t="00:23:15">[00:23:15]</a>. The hope is that these conditions will become so restrictive that no number can meet them all <a class="yt-timestamp" data-t="00:23:40">[00:23:40]</a>.
*   **Spoofs**: Numbers that are very close to being [[challenges_in_finding_odd_perfect_numbers | odd perfect numbers]] are called "spoofs" <a class="yt-timestamp" data-t="00:24:34">[00:24:34]</a>. [[history_and_contributions_of_mathematicians_to_perfect_numbers | Descartes]] encountered one such number, `198,585,576,189` <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>. Spoofs share properties with [[challenges_in_finding_odd_perfect_numbers | odd perfect numbers]], and researchers look for properties of spoofs that prevent them from being true [[challenges_in_finding_odd_perfect_numbers | odd perfect numbers]] <a class="yt-timestamp" data-t="00:24:40">[00:24:40]</a>. In 2022, Pace Nielsen and a BYU team found 21 spoof numbers, but no property has yet ruled out [[challenges_in_finding_odd_perfect_numbers | odd perfect numbers]] <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>.
*   **Heuristic Arguments**: Carl Pomerance's heuristic argument predicts that between 10^2200 and [[infinity_in_mathematics | infinity]], there are no more than 10^-540 perfect numbers of the form `N = pm^2` <a class="yt-timestamp" data-t="00:26:09">[00:26:09]</a>. This argument suggests that [[challenges_in_finding_odd_perfect_numbers | odd perfect numbers]] shouldn't exist <a class="yt-timestamp" data-t="00:26:24">[00:26:24]</a>. However, this same heuristic also predicts no large even perfect numbers, which contradicts the expectation of [[infinity_in_mathematics | infinitely many even perfect numbers]] <a class="yt-timestamp" data-t="00:26:40">[00:26:40]</a>.

## Applications of Pure Mathematics

While the problem of perfect numbers may seem to lack real-world applications <a class="yt-timestamp" data-t="00:27:32">[00:27:32]</a>, the history of mathematics demonstrates the value of pursuing pure curiosity:
*   For over 2000 years, number theory had no real-world applications, but in the 20th century, it became the foundation for modern cryptography, protecting everything from text messages to government secrets <a class="yt-timestamp" data-t="00:27:50">[00:27:50]</a>.
*   Einstein's general relativity was built on [[the_parallel_postulate_and_noneuclidean_geometry | non-Euclidean geometries]], which were developed as intellectual curiosities without foresight of their future impact <a class="yt-timestamp" data-t="00:28:45">[00:28:45]</a>.

Unsolved problems in mathematics, even those without immediate applications, drive the development of new ideas and build foundational knowledge that may prove useful in unexpected ways in the future <a class="yt-timestamp" data-t="00:28:16">[00:28:16]</a>.