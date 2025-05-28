---
title: Oldest unsolved problem in mathematics
videoId: Zrv1EDIqHkY
---

From: [[veritasium]] <br/> 

The existence of odd perfect numbers is considered the [[challenges_in_finding_odd_perfect_numbers | oldest unsolved problem in mathematics]], dating back 2,000 years <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Many notable mathematicians have attempted to solve it without success <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. In 2000, Italian mathematician Piergiorgio Odifreddi listed it among four pressing open problems <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Solving it could be as simple as finding a single number, yet computers have checked numbers up to 10<sup>2,200</sup> without success <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. The problem is described as "old, simple, and beautiful" <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. The core question is: "Do any odd perfect numbers exist?" <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>

## What is a Perfect Number?

A perfect number is a positive integer that is equal to the sum of its proper positive divisors (divisors excluding the number itself) <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

*   **Example: Six** <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>
    *   Proper divisors of 6 are 1, 2, and 3 <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
    *   1 + 2 + 3 = 6, so 6 is a perfect number <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
*   **Example: Ten** <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>
    *   Proper divisors of 10 are 1, 2, and 5 <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
    *   1 + 2 + 5 = 8, so 10 is not a perfect number <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

Most numbers either "overshoot" or "undershoot" when their proper divisors are summed <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. Between 1 and 100, only 6 and 28 are perfect numbers <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. Up to 10,000, the next two are 496 and 8,128 <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

## Historical Discoveries and Properties of Perfect Numbers

These four perfect numbers (6, 28, 496, 8,128) were the only ones known to the ancient Greeks and for over a thousand years thereafter <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

Observed patterns and properties of these numbers include:
*   Each successive perfect number is one digit longer than the previous one <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   Their ending digit alternates between 6 and 8 <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   All known perfect numbers are even <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   They are all [[history_and_contributions_of_mathematicians_to_perfect_numbers | triangular numbers]], meaning they are the sum of consecutive integers (e.g., 6 = 1+2+3, 28 = 1+2+3+4+5+6+7) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   Every perfect number except 6 is the sum of consecutive odd cubes (e.g., 28 = 1³ + 3³) <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   When written in binary, they are a string of ones followed by a series of zeros (e.g., 6 is 110, 28 is 11100) <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. This means they are all products of consecutive powers of two <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

### Euclid's Formula for Even Perfect Numbers

Around 300 BC, Euclid discovered a pattern for generating perfect numbers <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. His method involves powers of two:
1.  Start with 1, and keep doubling: 1, 2, 4, 8, 16... <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
2.  Add consecutive numbers from this sequence: 1+2=3 <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
3.  If the sum is a prime number, multiply it by the last number in the sum sequence <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
    *   (1+2=3, which is prime) * 2 = 6 (the first perfect number) <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
    *   (1+2+4=7, which is prime) * 4 = 28 (the second perfect number) <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
    *   (1+2+4+8=15, not prime) -> (1+2+4+8+16=31, which is prime) * 16 = 496 (the third perfect number) <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

Euclid's formula can be generalized as 2<sup>(P-1)</sup>(2<sup>P</sup> - 1), where (2<sup>P</sup> - 1) must be a prime number <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. Since 2<sup>(P-1)</sup> is always even, this formula always produces an even number <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. Euclid found a way to generate even perfect numbers, but he did not prove it was the *only* way, leaving open the possibility of odd perfect numbers <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

### Nicomachus's Conjectures

Around 400 years after Euclid, the Greek philosopher Nicomachus published *Introductio Arithmetica*, stating five conjectures about perfect numbers, which were considered facts for a thousand years <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>:
1.  The nth perfect number has n digits <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
2.  All perfect numbers are even <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
3.  All perfect numbers end in 6 and 8 alternately <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
4.  Euclid's algorithm produces every even perfect number <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
5.  There are infinitely many perfect numbers <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

In the 13th century, Egyptian mathematician Ibn Fallus listed 10 perfect numbers, but 3 were incorrect <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. However, his list disproved two of Nicomachus's conjectures:
*   The fifth perfect number is eight digits long, disproving conjecture 1 <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
*   Both the fifth and sixth perfect numbers end in a 6, disproving conjecture 3 <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

## Renaissance Europe and Mersenne Primes

The problem of perfect numbers reached Renaissance Europe, leading to the rediscovery of the fifth, sixth, and seventh perfect numbers <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. Finding new perfect numbers relied on finding prime numbers of the form (2<sup>P</sup> - 1) <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

French polymath Marin Mersenne extensively studied numbers of this form, now called Mersenne Primes <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. In 1644, he published a list of 11 values of P for which he claimed (2<sup>P</sup> - 1) were prime <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. The first seven exponents on his list correctly correspond to the first seven perfect numbers <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. Mersenne admitted he hadn't checked some of the larger numbers, noting the difficulty of primality testing for large numbers <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

Mersenne discussed the problem with Pierre de Fermat and René Descartes <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. In 1638, Descartes conjectured that all even perfect numbers conform to Euclid's form <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. He also believed that if an odd perfect number existed, it must be the product of a prime and the square of a different number <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. However, Descartes could not prove these statements <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

## Euler's Breakthroughs

About a century later, Leonhard Euler, introduced to number theory by Christian Goldbach, made three significant breakthroughs on the problem of perfect numbers <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

1.  **Discovery of the Eighth Perfect Number**: In 1732, Euler discovered the eighth perfect number by verifying that (2<sup>31</sup> - 1) is prime, as Mersenne had predicted <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
2.  **Introduction of the Sigma Function**: Euler invented the sigma function (σ(n)), which sums all divisors of a number, including the number itself <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. For a perfect number, σ(n) = 2n <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. This function is powerful because it can be split for numbers made of factors that don't share common factors (e.g., σ(20) = σ(2²) * σ(5)) <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
3.  **Euclid-Euler Theorem**: Using the sigma function, Euler proved that every even perfect number has Euclid's form <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. This solved a 1600-year-old problem and proved Nicomachus's fourth conjecture <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>. This achievement is considered a monumental mathematical collaboration <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.
4.  **Characterization of Odd Perfect Numbers**: Euler also set out to prove Descartes' statement about the form of odd perfect numbers <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>. By analyzing the properties of the sigma function, he showed that if an odd perfect number (n) exists, it must have the form of a prime raised to an odd power multiplied by other primes raised to even powers <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. That is, n = p<sup>k</sup>m², where p is a prime, k is odd, and m is an integer whose prime factors are all different from p <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>. Despite this, Euler could not prove whether they existed, calling it "a most difficult question" <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.

## Modern Search for Perfect Numbers

For 150 years after Euler, little progress was made <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. English mathematician Peter Barlow wrongly predicted that Euler's eighth perfect number would be the last one discovered due to their perceived lack of usefulness <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.

Mathematicians, however, continued their pursuit, focusing on Mersenne's list of proposed primes <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>.
*   **Edouard Lucas**: In 1876, 230 years after Mersenne's list, Lucas proved that (2<sup>67</sup> - 1) was not prime, though he couldn't find its factors <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>.
*   **Frank Nelson Cole**: 27 years later, Cole famously demonstrated the factors of (2<sup>67</sup> - 1) (193,707,721 and 761,838,257,287) to the American Mathematical Society, a calculation that took him three years of Sunday work <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>. A modern computer can perform this in less than a second <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>.

### The Age of Computers

From 500 BC until 1952, only 12 Mersenne primes (and thus 12 perfect numbers) had been discovered <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>. The challenge was checking primality of large numbers <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.

*   **Raphael Robinson**: In 1952, American mathematician Raphael Robinson wrote a computer program for primality testing and ran it on the SWAC, the fastest computer at the time <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>. Within 10 months, he found the next five Mersenne primes <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>.
*   **Rapid Discoveries**: Over the next 50 years, new Mersenne primes were discovered rapidly using computers <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>. The largest Mersenne prime at the end of 1952 was (2<sup>2,281</sup> - 1) (687 digits long) <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>, growing to (2<sup>859,433</sup> - 1) (258,716 digits long) by 1994 <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>.
*   **Great Internet Mersenne Prime Search (GIMPS)**: In 1996, computer scientist George Woltman launched GIMPS, a distributed computing project that allows volunteers to contribute their computer power to search for Mersenne primes <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>. GIMPS has discovered 17 new Mersenne primes, 15 of which were the largest known primes at the time <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>. There is a $250,000 prize for the first billion-digit prime <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>.
*   **Recent Discoveries**: In 2017, John Pace discovered the 50th Mersenne Prime, (2<sup>77,232,917</sup> - 1), which is over 23 million digits long <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>. In 2018, the 51st Mersenne Prime, (2<sup>82,589,933</sup> - 1), was discovered, boasting over 24 million digits <a class="yt-timestamp" data-t="00:20:31">[00:20:31]</a>. These are almost always the largest known prime numbers <a class="yt-timestamp" data-t="00:21:15">[00:21:15]</a>.

Despite these successes, only 51 perfect numbers have been found <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>. The Lenstra, Pomerance, and Wagstaff conjecture predicts infinitely many Mersenne primes, and thus infinitely many even perfect numbers, though they are rare and very large <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>.

## Current Status of Odd Perfect Numbers

The problem of odd perfect numbers remains unsolved <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.
*   **Lower Bounds**: Researchers have used algorithms to show that if an odd perfect number exists, it must be larger than 10<sup>300</sup> (1991) <a class="yt-timestamp" data-t="00:22:40">[00:22:40]</a>, then 10<sup>1,500</sup> (2012) <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>, and currently up to 10<sup>2,200</sup> <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>. Such large numbers make computer discovery unlikely anytime soon <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.
*   **"Web of Conditions"**: A common approach to finding an odd perfect number is to define more and more conditions they must satisfy, hoping the conditions become so numerous and restrictive that no such number can exist <a class="yt-timestamp" data-t="00:23:15">[00:23:15]</a>. For example, it is known that an odd perfect number must have at least 10 prime factors and be larger than 10<sup>3,000</sup> <a class="yt-timestamp" data-t="00:23:26">[00:23:26]</a>.
*   **Spoofs**: Numbers that are "very close" to being odd perfect numbers are called spoofs <a class="yt-timestamp" data-t="00:24:34">[00:24:34]</a>. An example is Descartes' number: 198,585,576,189. It is equal to 3² × 7² × 11² × 13² × 22021. Its sigma function is twice the number, but 22021 is not prime (it is 19² × 61), meaning it's not truly perfect <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>. Odd perfect numbers share all properties of spoofs, plus a few extra ones. The goal is to find a property of spoofs that prevents them from being odd perfect numbers <a class="yt-timestamp" data-t="00:24:43">[00:24:43]</a>. In 2022, Pace Nielsen and a BYU team found 21 spoof numbers, including Descartes' number, but did not find a property ruling out odd perfect numbers <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>.
*   **Heuristic Arguments**: Some mathematicians, like Carl Pomerance, believe odd perfect numbers do not exist, based on heuristic arguments that combine knowledge of prime occurrences to predict the average number of perfect numbers <a class="yt-timestamp" data-t="00:25:47">[00:25:47]</a>. Pomerance's argument predicts no more than 10<sup>-540</sup> perfect numbers of the form N = pm² between 10<sup>2,200</sup> and infinity <a class="yt-timestamp" data-t="00:26:09">[00:26:09]</a>. However, this argument also predicts no large *even* perfect numbers, which contradicts the expectation of infinitely many even perfect numbers <a class="yt-timestamp" data-t="00:26:40">[00:26:40]</a>. A heuristic is not a proof <a class="yt-timestamp" data-t="00:26:17">[00:26:17]</a>.

## The Value of Unsolved Problems in Mathematics

While the immediate applications of the perfect numbers problem are nonexistent <a class="yt-timestamp" data-t="00:27:29">[00:27:29]</a>, its pursuit highlights the value of pure mathematical inquiry:
*   **Foundation for Future Applications**: Number theory, for over 2000 years, had no real-world applications but now forms the foundation for modern cryptography, protecting everything from text messages to government secrets <a class="yt-timestamp" data-t="00:27:50">[00:27:50]</a>.
*   **Generating New Ideas**: Tackling challenging problems forces mathematicians to develop new ideas and methods, which can eventually lead to unexpected breakthroughs or applications <a class="yt-timestamp" data-t="00:28:16">[00:28:16]</a>.
*   **Intellectual Curiosity**: Einstein's general relativity, for instance, was built upon non-Euclidean geometries, which were initially developed purely out of intellectual curiosity <a class="yt-timestamp" data-t="00:28:45">[00:28:45]</a>.

Currently, around 10-15 people are actively working on the problem of perfect numbers <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>. The history of mathematics shows that pursuing even seemingly "useless" problems is the only way to discover their true long-term impact <a class="yt-timestamp" data-t="00:29:33">[00:29:33]</a>.