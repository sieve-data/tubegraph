---
title: History of perfect numbers
videoId: Zrv1EDIqHkY
---

From: [[veritasium]] <br/> 

The existence of perfect numbers dates back over 2,000 years, representing one of the oldest unsolved problems in [[mathematics | math]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The problem has captivated mathematicians for centuries due to its age, simplicity, and inherent beauty <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. In the year 2000, Italian mathematician Piergiorgio Odifreddi listed it among four of the most pressing open problems of the time <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Solving the problem could involve finding a single number <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Definition of a Perfect Number

A perfect number is a positive integer that is equal to the sum of its proper positive divisors (divisors excluding the number itself) <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a> <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

For example:
*   **6**: Its proper divisors are 1, 2, and 3. Adding them gives 1 + 2 + 3 = 6 <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. Therefore, 6 is a perfect number <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   **10**: Its proper divisors are 1, 2, and 5. Adding them gives 1 + 2 + 5 = 8 <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Since 8 is not equal to 10, 10 is not a perfect number <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

## Early Discoveries and Properties

Between 1 and 100, only 6 and 28 are perfect numbers <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. Up to 10,000, the next two are 496 and 8,128 <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. These four numbers were the only perfect numbers known to the ancient Greeks and remained so for over a thousand years <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

Properties observed in these early perfect numbers include:
*   Each successive perfect number is one digit longer than the previous one <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   Their ending digit alternates between 6 and 8 <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   They are all even <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   They can be written as the sum of consecutive numbers, making them [[triangular numbers | triangular numbers]] (e.g., 6 = 1+2+3; 28 = 1+2+3+4+5+6+7) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a> <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
*   All perfect numbers except 6 are the sum of consecutive odd cubes (e.g., 28 = 1³ + 3³; 496 = 1³ + 3³ + 5³ + 7³) <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   When written in binary, they consist of a string of ones followed by a series of zeros (e.g., 6 = 110; 28 = 11100; 496 = 111110000) <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

## Euclid's Formula

Around 300 BC, Euclid discovered a pattern for generating even perfect numbers <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. His method involves powers of 2:
1.  Start with 1, and keep doubling it (1, 2, 4, 8, 16, etc.) <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
2.  Add the numbers in the sequence starting from 1 (1+2, 1+2+4, 1+2+4+8, etc.) <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
3.  If the sum is a prime number, multiply it by the last number in the sequence to get a perfect number <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
    *   1+2 = 3 (prime). Multiply by 2: 3 * 2 = 6 <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
    *   1+2+4 = 7 (prime). Multiply by 4: 7 * 4 = 28 <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
    *   1+2+4+8+16 = 31 (prime). Multiply by 16: 31 * 16 = 496 <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

This pattern can be generalized. A sum of consecutive powers of 2 (from 2^0 to 2^(n-1)) is equal to 2^n - 1 <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. Thus, Euclid's formula for a perfect number is (2^P - 1) * 2^(P-1), where (2^P - 1) must be a prime number <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. Since the formula involves multiplication by an even number (2^(P-1)), it always generates an even perfect number <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. Euclid's work showed a way to generate even perfect numbers, but he did not prove it was the *only* way <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

## Nicomachus's Conjectures

Four hundred years after Euclid, the Greek philosopher Nicomachus published *Introductio Arithmetica*, a standard arithmetic text for the next thousand years <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. In it, he stated five conjectures about perfect numbers that he believed were true but did not prove <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>:
1.  The nth perfect number has n digits <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
2.  All perfect numbers are even <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
3.  All perfect numbers end in 6 and 8 alternately <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
4.  Euclid's algorithm produces every even perfect number <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
5.  There are infinitely many perfect numbers <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

For a millennium, these conjectures were considered facts <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.

## Later Discoveries and Disproofs

In the 13th century, Egyptian mathematician Ibn Fallus published a list of 10 supposed perfect numbers <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. While three were incorrect, the remaining ones were valid <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.
*   The fifth perfect number was found to be eight digits long, disproving Nicomachus's first conjecture (the nth perfect number has n digits) <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
*   Both the fifth and sixth perfect numbers ended in 6, disproving Nicomachus's third conjecture (alternating 6 and 8 endings) <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

By the Renaissance in Europe, the fifth, sixth, and seventh perfect numbers had been rediscovered <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. All known perfect numbers at this point fit Euclid's form <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.

### Mersenne Primes

French polymath Marin Mersenne extensively studied numbers of the form 2^P - 1, which are critical for generating perfect numbers <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. In 1644, he published a list of 11 values of P for which he claimed 2^P - 1 would be prime <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. Numbers of this form that are prime are now called [[the_prime_number_phenomenon | Mersenne Primes]] <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. The first seven exponents on his list did correspond to primes and the first seven perfect numbers <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. Mersenne admitted that he had not checked the primality of larger numbers, noting that checking a 15-to-20-digit number for primality would take too long <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.

## Descartes' Contributions

Mersenne discussed perfect numbers with other prominent mathematicians like Pierre de Fermat and Rene Descartes <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. In 1638, Descartes conjectured that all even perfect numbers conform to Euclid's formula <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. He also believed that if an odd perfect number existed, it must be the product of a prime number and the square of a different number <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. However, Descartes could not prove these statements, remarking on the difficulty of finding odd perfect numbers <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

## Euler's Breakthroughs

[[contributions_of_notable_mathematicians_to_perfect_numbers | Leonhard Euler]] took up the problem about a century later <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.
*   **Discovery of the 8th Perfect Number**: In 1732, Euler discovered the eighth perfect number by verifying that 2^31 - 1 is prime, as Mersenne had predicted <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
*   **The Sigma Function**: Euler invented the sigma function, denoted σ(n), which sums all divisors of a number *n*, including *n* itself <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. For a perfect number, σ(n) = 2n <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. The power of the sigma function lies in its multiplicative property: if a number is a product of relatively prime factors (like prime powers), its sigma function can be split into the product of the sigma functions of those factors <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
*   **The Euclid-Euler Theorem**: Using the sigma function, Euler proved that every even perfect number has Euclid's form <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. This is known as the [[euclid_euler_theorem | Euclid-Euler theorem]] and solved a 1600-year-old problem, proving Nicomachus's fourth conjecture <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>.
*   **Form of Odd Perfect Numbers**: Euler also set out to prove Descartes' statement about the form of odd perfect numbers <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>. By analyzing the parity of the sigma function of prime powers, he proved that if an odd perfect number exists, it must have the form P^(k) * M², where P is a prime number, k is an odd integer, and M is a product of prime powers raised to even integers <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a> <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>. Even with this breakthrough, Euler could not prove whether odd perfect numbers existed, calling it "a most difficult question" <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.

## Modern Search and Computational Advances

For 150 years after Euler, little progress was made, and no new perfect numbers were discovered <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. English mathematician Peter Barlow famously stated in the 19th century that Euler's eighth perfect number "is the greatest that ever will be discovered" due to their perceived lack of usefulness <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.

However, Barlow was wrong. Mathematicians continued the search, often focusing on Mersenne's list <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.
*   **Lucas and Cole**: In 1876, Edouard Lucas proved that Mersenne's 2^67 - 1 was not prime <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>. Twenty-seven years later, Frank Nelson Cole famously demonstrated its factors (193,707,721 * 761,838,257,287) in a silent presentation, a task that took him three years of Sunday work <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>. A modern computer could perform this calculation in less than a second <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>.

### Computer-Assisted Discovery
From 500 BC until 1952, only 12 Mersenne primes (and thus 12 perfect numbers) had been found, primarily due to the difficulty of checking large numbers for primality <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.
*   **Raphael Robinson and SWAC**: In 1952, American mathematician Raphael Robinson wrote a computer program to test for Mersenne primes on the SWAC, the fastest computer at the time <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>. Within 10 months, he discovered the next five Mersenne primes and their corresponding perfect numbers <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>.
*   **GIMPS**: As numbers grew astronomically large, finding new Mersenne primes became increasingly difficult <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>. In 1996, computer scientist George Woltman launched the Great Internet Mersenne Prime Search (GIMPS), a distributed computing project that allows volunteers to contribute their computer power to the search <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>. GIMPS has been highly successful, discovering 17 new Mersenne primes, 15 of which were the largest known primes at the time <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>. Discoverers are credited, and there's a $250,000 prize for the first billion-digit prime <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.

Recent discoveries include:
*   **50th Mersenne Prime**: In 2017, Church Deacon John Pace discovered 2^(77,232,917) - 1, a number over 23 million digits long, via GIMPS. It was the largest known prime at the time <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>.
*   **51st Mersenne Prime**: A year later, 2^(82,589,933) - 1 was discovered, boasting over 24 million digits <a class="yt-timestamp" data-t="00:20:31">[00:20:31]</a>. As of today, this is still the largest known prime <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>.

## Current Status and Conjectures about Perfect Numbers

Despite the success of computers, only 51 perfect numbers have been found <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>. The Lenstra and Pomerance Wagstaff conjecture predicts the distribution of Mersenne primes and suggests that there are infinitely many Mersenne primes, and therefore infinitely many even perfect numbers <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>. This would confirm Nicomachus's fifth conjecture <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>. However, this remains a conjecture, not a proof <a class="yt-timestamp" data-t="00:22:17">[00:22:17]</a>.

### [[current_status_and_conjectures_about_odd_perfect_numbers | Odd Perfect Numbers]]

The question "Do any odd perfect numbers exist?" remains one of the oldest unsolved problems in [[mathematics | math]] <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.
*   **Lower Bounds**: Researchers have used algorithms to show that if an odd perfect number exists, it must be larger than 10^2200 <a class="yt-timestamp" data-t="00:22:40">[00:22:40]</a>.
*   **Web of Conditions**: The primary approach to proving or disproving their existence is to establish more and more conditions that odd perfect numbers must satisfy, hoping to find a contradiction or strain the possibilities to non-existence <a class="yt-timestamp" data-t="00:23:15">[00:23:15]</a>.
*   **Spoofs**: Numbers that are very close to being odd perfect numbers are called "spoofs" <a class="yt-timestamp" data-t="00:24:34">[00:24:34]</a>. Odd perfect numbers share all properties of spoofs plus additional ones. The goal is to find properties of spoofs that prevent them from being odd perfect numbers <a class="yt-timestamp" data-t="00:24:40">[00:24:40]</a>. For example, if spoofs must be divisible by 105, and odd perfect numbers cannot be, this would prove non-existence <a class="yt-timestamp" data-t="00:24:55">[00:24:55]</a>. Recent work in 2022 by Pace Nielsen and a BYU team found 21 spoof numbers but no properties that rule out odd perfect numbers <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>.
*   **Heuristic Arguments**: Some mathematicians, like Carl Pomerance, use heuristic arguments based on the expected occurrence of prime numbers to suggest that odd perfect numbers do not exist <a class="yt-timestamp" data-t="00:25:47">[00:25:47]</a>. However, these are not proofs and have limitations, as the same heuristic predicts that there should be no large even perfect numbers, which contradicts expectations based on Mersenne primes <a class="yt-timestamp" data-t="00:26:40">[00:26:40]</a>.

## Applications and Importance

Currently, there are no known direct applications of perfect numbers to the real world <a class="yt-timestamp" data-t="00:27:29">[00:27:29]</a>. However, the study of pure [[mathematics | mathematics]], like [[number_theory | number theory]] (which perfect numbers belong to), has historically led to unexpected applications <a class="yt-timestamp" data-t="00:27:50">[00:27:50]</a>. For example, [[number_theory | number theory]], once considered useless, became the foundation for modern [[cryptography | cryptography]] in the 20th century, protecting everything from text messages to government secrets <a class="yt-timestamp" data-t="00:28:04">[00:28:04]</a>. Similarly, non-Euclidean geometries, developed as intellectual curiosities, formed the basis of Einstein's general relativity <a class="yt-timestamp" data-t="00:28:45">[00:28:45]</a>.

The pursuit of solutions to such problems drives the creation of new mathematical ideas and tools, which may later prove invaluable <a class="yt-timestamp" data-t="00:28:16">[00:28:16]</a>.