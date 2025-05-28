---
title: Methods and challenges in discovering new perfect numbers
videoId: Zrv1EDIqHkY
---

From: [[veritasium]] <br/> 

Perfect numbers are positive integers where the sum of their proper divisors (divisors excluding the number itself) equals the number itself <a class="yt-timestamp" data-t="01:09:09">[01:09:09]</a>. For example, the proper divisors of 6 are 1, 2, and 3, which sum to 6, making 6 a perfect number <a class="yt-timestamp" data-t="01:09:09">[01:09:09]</a>. In contrast, for a number like 10, its proper divisors (1, 2, 5) sum only to 8, so 10 is not perfect <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>.

## Early Discoveries and Conjectures
Among numbers between 1 and 100, only 6 and 28 are perfect <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>. Expanding to 10,000, the next two perfect numbers discovered were 496 and 8,128 <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>. These four numbers were the only perfect numbers known to the [[history_of_perfect_numbers | ancient Greeks]] and remained the only known ones for over a millennium <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>.

The Greek philosopher Nicomachus, around 400 years after Euclid, published *Introductio Arithmetica*, which served as the standard arithmetic text for the next thousand years <a class="yt-timestamp" data-t="07:05:00">[07:05:00]</a>. In it, he proposed five conjectures about perfect numbers, which were considered facts until the 13th century <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>:
1.  The nth perfect number has n digits <a class="yt-timestamp" data-t="07:23:00">[07:23:00]</a>.
2.  All perfect numbers are even <a class="yt-timestamp" data-t="07:26:00">[07:26:00]</a>.
3.  All perfect numbers end in 6 and 8 alternately <a class="yt-timestamp" data-t="07:29:00">[07:29:00]</a>.
4.  Euclid's algorithm produces every even perfect number <a class="yt-timestamp" data-t="07:33:00">[07:33:00]</a>.
5.  There are infinitely many perfect numbers <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>.

These conjectures were largely unproven or disproven for centuries. For example, the 5th perfect number, discovered by Egyptian mathematician Ibn Fallus in the 13th century, was 8 digits long, disproving Nicomachus's first conjecture <a class="yt-timestamp" data-t="08:05:00">[08:05:00]</a>. Also, both the 5th and 6th perfect numbers ended in 6, disproving the third conjecture about alternating endings <a class="yt-timestamp" data-t="08:12:00">[08:12:00]</a>.

## Euclid's Formula for Even Perfect Numbers
Around 300 BC, Euclid discovered a pattern for generating even perfect numbers <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>. His formula states that if a number of the form (1 + 2 + 4 + ... + 2^(P-1)) results in a prime number (now known as a [[significance_of_mersenne_primes | Mersenne Prime]]), then multiplying this prime by the last power of 2 in the sum (2^(P-1)) will yield a perfect number <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>. This can be expressed as 2^(P-1) * (2^P - 1), where (2^P - 1) is prime <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>. Since 2^(P-1) is always even, this formula inherently generates only even perfect numbers <a class="yt-timestamp" data-t="06:42:00">[06:42:00]</a>.

While Euclid found a way to generate these numbers, he did not prove it was the *only* way to get perfect numbers, leaving open the possibility of odd perfect numbers <a class="yt-timestamp" data-t="06:50:00">[06:50:00]</a>.

### Marin Mersenne and Mersenne Primes
French polymath Marin Mersenne extensively studied numbers of the form 2^P - 1 <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>. In 1644, he published a list of 11 values of P for which he claimed 2^P - 1 were prime numbers <a class="yt-timestamp" data-t="08:53:00">[08:53:00]</a>. Numbers of this form that are prime are now called [[significance_of_mersenne_primes | Mersenne Primes]] <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>. Mersenne confessed that for larger numbers on his list, he hadn't even checked their primality <a class="yt-timestamp" data-t="09:13:00">[09:13:00]</a>.

## Euler's Contributions and the Sigma Function
Leonhard Euler, a mathematical prodigy, picked up the problem of perfect numbers in the 18th century <a class="yt-timestamp" data-t="10:45:00">[10:45:00]</a>.
His breakthroughs include:
*   **Discovery of the 8th Perfect Number**: In 1732, Euler discovered the eighth perfect number by verifying that 2^31 - 1 is prime, as Mersenne had predicted <a class="yt-timestamp" data-t="10:58:00">[10:58:00]</a>.
*   **The Sigma Function**: Euler invented the sigma function, which sums all divisors of a number, including the number itself <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>. For a perfect number (N), the sigma function always returns 2N <a class="yt-timestamp" data-t="11:28:00">[11:28:00]</a>. This function is powerful because if a number is composed of factors that do not share common factors, its sigma function can be split into the sigma functions of its prime powers <a class="yt-timestamp" data-t="12:30:00">[12:30:00]</a>.
*   **Euclid-Euler Theorem**: Using the sigma function, Euler proved that every even perfect number has Euclid's form <a class="yt-timestamp" data-t="13:01:00">[13:01:00]</a>. This resolved a 1600-year-old problem and validated Nicomachus's fourth conjecture <a class="yt-timestamp" data-t="13:09:00">[13:09:00]</a>.
*   **Form of Odd Perfect Numbers**: Euler also proved that if an odd perfect number exists, it must have a specific form: a product of a prime raised to an odd power and other prime factors raised to even powers <a class="yt-timestamp" data-t="13:30:00">[13:30:00]</a>, <a class="yt-timestamp" data-t="15:32:00">[15:32:00]</a>. This significantly narrowed the search space for [[current_status_and_conjectures_about_odd_perfect_numbers | odd perfect numbers]] <a class="yt-timestamp" data-t="15:40:00">[15:40:00]</a>. Despite this, Euler could not prove their existence, calling it "a most difficult question" <a class="yt-timestamp" data-t="15:50:00">[15:50:00]</a>.

## Modern Search and Computational Challenges
For 150 years after Euler, little progress was made, and no new perfect numbers were found <a class="yt-timestamp" data-t="15:56:00">[15:56:00]</a>. English mathematician Peter Barlow even stated that Euler's eighth perfect number might be the last ever discovered due to their lack of utility <a class="yt-timestamp" data-t="16:04:00">[16:04:00]</a>.

However, mathematicians persisted. One significant challenge was verifying the primality of large Mersenne numbers. In 1876, Edouard Lucas proved that 2^67 - 1 (a number from Mersenne's list) was not prime <a class="yt-timestamp" data-t="16:45:00">[16:45:00]</a>. Later, in 1903, Frank Nelson Cole famously demonstrated its factors without speaking a word, revealing the sheer computational effort involved in primality testing for large numbers before computers <a class="yt-timestamp" data-t="16:57:00">[16:57:00]</a>. Cole's work took him three years of Sunday effort <a class="yt-timestamp" data-t="17:44:00">[17:44:00]</a>.

### The Age of Computers
The search for perfect numbers was revolutionized in 1952 when American mathematician Raphael Robinson wrote a computer program to test Mersenne numbers for primality on the SWAC, the fastest computer of its time <a class="yt-timestamp" data-t="18:06:00">[18:06:00]</a>. Within 10 months, Robinson found the next five Mersenne primes, leading to five new perfect numbers <a class="yt-timestamp" data-t="18:18:00">[18:18:00]</a>. Over the subsequent 50 years, new Mersenne primes were discovered rapidly, all with the aid of computers <a class="yt-timestamp" data-t="18:24:00">[18:24:00]</a>.

As the numbers grew astronomically large, finding new Mersenne primes became increasingly difficult even for supercomputers <a class="yt-timestamp" data-t="18:53:00">[18:53:00]</a>. To address this, computer scientist George Woltman launched the Great Internet Mersenne Prime Search (GIMPS) in 1996 <a class="yt-timestamp" data-t="19:02:00">[19:02:00]</a>. GIMPS distributes the computational work across many volunteered computers, allowing anyone to contribute to the search <a class="yt-timestamp" data-t="19:09:00">[19:09:00]</a>. This project has been highly successful, discovering 17 new Mersenne primes, 15 of which were the largest known primes at the time of their discovery <a class="yt-timestamp" data-t="19:17:00">[19:17:00]</a>. There's even a $250,000 prize for the first billion-digit prime <a class="yt-timestamp" data-t="19:37:00">[19:37:00]</a>.

As of today, the largest known prime is the 51st Mersenne Prime, 2^82,589,933 - 1, discovered in 2018, which has over 24 million digits <a class="yt-timestamp" data-t="20:31:00">[20:31:00]</a>. Due to the rapid growth of these numbers, the largest Mersenne Prime is almost always the largest known prime <a class="yt-timestamp" data-t="21:15:00">[21:15:00]</a>.

## Current Status and Conjectures about Odd Perfect Numbers
While computers have been successful in finding even perfect numbers, only 51 have been discovered so far <a class="yt-timestamp" data-t="21:24:00">[21:24:00]</a>. The Lenstra and Pomerance Wagstaff conjecture predicts an infinite number of Mersenne primes and thus an infinite number of even perfect numbers, but this remains unproven <a class="yt-timestamp" data-t="21:48:00">[21:48:00]</a>.

The question of whether [[current_status_and_conjectures_about_odd_perfect_numbers | odd perfect numbers]] exist remains one of the oldest unsolved problems in mathematics <a class="yt-timestamp" data-t="22:24:00">[22:24:00]</a>. Researchers in 1991 showed that if an odd perfect number exists, it must be larger than 10^300 <a class="yt-timestamp" data-t="22:40:00">[22:40:00]</a>. Recent progress has pushed this lower bound to 10^2,200 <a class="yt-timestamp" data-t="22:53:00">[22:53:00]</a>.

Due to the immense size, direct computational search is unlikely to succeed soon <a class="yt-timestamp" data-t="23:05:00">[23:05:00]</a>. The primary approach involves identifying more and more conditions that [[current_status_and_conjectures_about_odd_perfect_numbers | odd perfect numbers]] must satisfy (a "web of conditions"), hoping that these conditions eventually prove their non-existence <a class="yt-timestamp" data-t="23:15:00">[23:15:00]</a>. For example, it is known that odd perfect numbers cannot be divided by 105 <a class="yt-timestamp" data-t="24:55:00">[24:55:00]</a>.

Researchers also study "spoofs," numbers that are very close to being [[current_status_and_conjectures_about_odd_perfect_numbers | odd perfect numbers]] but fail one condition (e.g., a prime factor turns out to be composite) <a class="yt-timestamp" data-t="24:34:00">[24:34:00]</a>. Odd perfect numbers would share all properties of spoofs plus a few extra ones, so identifying properties of spoofs that prevent them from being odd perfect numbers could prove their non-existence <a class="yt-timestamp" data-t="24:48:00">[24:48:00]</a>.

Heuristic arguments, like one made by Carl Pomerance, suggest that [[current_status_and_conjectures_about_odd_perfect_numbers | odd perfect numbers]] shouldn't exist based on the frequency of prime types <a class="yt-timestamp" data-t="25:47:00">[25:47:00]</a>. However, these heuristics are not proofs and can sometimes contradict other predictions (e.g., predicting no large even perfect numbers while an infinite number are expected) <a class="yt-timestamp" data-t="26:41:00">[26:41:00]</a>.

The search for perfect numbers continues, embodying the nature of mathematical inquiry where curiosity drives the exploration of problems without immediate practical applications, yet often leads to foundational discoveries with unforeseen real-world significance, such as in cryptography <a class="yt-timestamp" data-t="27:50:00">[27:50:00]</a>.