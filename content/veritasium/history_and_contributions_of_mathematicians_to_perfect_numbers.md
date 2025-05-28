---
title: History and contributions of mathematicians to perfect numbers
videoId: Zrv1EDIqHkY
---

From: [[veritasium]] <br/> 

The existence of odd perfect numbers is considered the oldest unsolved problem in mathematics, dating back 2000 years <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Despite efforts by many brilliant mathematicians, it remains uncracked <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. In 2000, Italian mathematician Piergiorgio Odifreddi listed it as one of four pressing open problems <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Solving it could be as simple as finding a single number <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>, but computer searches up to 10<sup>2,200</sup> have yielded no results <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## What is a Perfect Number?

A perfect number is a positive integer that is equal to the sum of its proper positive divisors (divisors excluding the number itself) <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   **Example: 6**
    Its proper divisors are 1, 2, and 3 <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
    1 + 2 + 3 = 6 <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Therefore, 6 is a [[perfect_numbers_and_their_properties | perfect number]] <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   **Example: 10**
    Its proper divisors are 1, 2, and 5 <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
    1 + 2 + 5 = 8 <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. Since 8 ≠ 10, 10 is not a perfect number <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

Between 1 and 100, only 6 and 28 are perfect numbers <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. Up to 10,000, the next two are 496 and 8,128 <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. These four were the only perfect numbers known to the ancient Greeks and remained so for over a thousand years <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## Characteristics of Even Perfect Numbers

The first few perfect numbers exhibit several patterns:
*   Each subsequent perfect number is one digit longer than the previous one <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   Their ending digits alternate between 6 and 8, implying they are all even <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   They can be written as the sum of consecutive integers:
    *   6 = 1 + 2 + 3 <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>
    *   28 = 1 + 2 + 3 + 4 + 5 + 6 + 7 <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>
    These are known as triangular numbers <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   Every perfect number except 6 is the sum of consecutive odd cubes <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>:
    *   28 = 1³ + 3³ <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>
    *   496 = 1³ + 3³ + 5³ + 7³ <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>
    *   8,128 = 1³ + 3³ + 5³ + 7³ + 9³ + ... + 15³ <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>
*   When written in binary, they are a string of ones followed by a series of zeros <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>, representing consecutive powers of two <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

## Key Mathematicians and Their Contributions

### Euclid (c. 300 BC)
Around 300 BC, Euclid discovered a pattern for generating perfect numbers <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. His formula involves summing powers of two (1 + 2 + 4 + ... + 2<sup>n-1</sup>) <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. If this sum results in a [[mathematical_uniqueness_of_prime_numbers | prime number]], then multiplying it by the last power of two in the sequence (2<sup>n-1</sup>) yields a perfect number <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   1 + 2 = 3 (prime) → 3 × 2 = 6 <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>
*   1 + 2 + 4 = 7 (prime) → 7 × 4 = 28 <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>
*   1 + 2 + 4 + 8 + 16 = 31 (prime) → 31 × 16 = 496 <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>

Euclid's formula can be generalized as 2<sup>P-1</sup>(2<sup>P</sup> - 1), where (2<sup>P</sup> - 1) is a prime number <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. This formula always generates an even number <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. Euclid found a way to generate even perfect numbers but did not prove it was the only way <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

### Nicomachus (c. 100 AD)
Four hundred years after Euclid, the Greek philosopher Nicomachus published *Introductio Arithmetica*, which became a standard arithmetic text <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. He stated five conjectures about perfect numbers, which he believed to be true but did not prove <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>:
1.  The nth perfect number has n digits <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
2.  All perfect numbers are even <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
3.  All perfect numbers end in 6 and 8 alternately <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
4.  Euclid's algorithm produces every even perfect number <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
5.  There are infinitely many perfect numbers <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

For the next thousand years, these conjectures were considered facts as no one could prove or disprove them <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.

### Ibn Fallus (13th Century)
In the 13th century, Egyptian mathematician Ibn Fallus published a list of 10 perfect numbers <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. While three turned out to be incorrect, the remaining ones were valid <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. The fifth perfect number was found to be eight digits long, disproving Nicomachus's first conjecture <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. Additionally, the fifth and sixth perfect numbers both ended in 6, disproving Nicomachus's third conjecture about alternating endings <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

### Marin Mersenne (1588-1648)
During the [[Mathematical breakthroughs in the Renaissance | Renaissance]], mathematicians rediscovered perfect numbers and found that all known perfect numbers conformed to Euclid's form <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. Finding new ones required identifying values of P that make 2<sup>P</sup> - 1 prime <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. French polymath Marin Mersenne extensively studied numbers of this form, now known as Mersenne Primes <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. In 1644, he published a list of 11 values of P for which he claimed 2<sup>P</sup> - 1 were prime <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. The first seven exponents on his list did result in primes, corresponding to the first seven perfect numbers <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. Mersenne admitted that he did not check whether some of the larger numbers, such as 2<sup>67</sup> - 1, were prime due to the computational difficulty <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.

### René Descartes (1596-1650)
Mersenne discussed the problem of perfect numbers with other prominent thinkers like Pierre de Fermat and René Descartes <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. In 1638, Descartes conjectured that all even perfect numbers conform to Euclid's form <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. He also believed that if an odd perfect number existed, it must be the product of a prime and the square of a different number <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. However, Descartes could not prove either of these statements <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

### Leonhard Euler (1707-1783)
A century later, the problem captivated Leonhard Euler, who was introduced to number theory by Christian Goldbach <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. Euler built upon Descartes' work and made three significant breakthroughs:
1.  **Discovery of the 8th Perfect Number**: In 1732, Euler discovered the eighth perfect number by verifying that 2<sup>31</sup> - 1 is prime, as Mersenne had predicted <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
2.  **The Sigma Function and Euclid-Euler Theorem**: Euler invented the sigma function (σ), which sums all divisors of a number, including the number itself <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. For a perfect number *n*, σ(*n*) = 2*n* <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. The power of the sigma function lies in its multiplicative property: if numbers are coprime, their sigma function can be split into the product of their individual sigma functions <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. Using this, Euler proved that *every even perfect number has Euclid's form* <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. This is known as the Euclid-Euler theorem and solved a 1600-year-old problem, proving Nicomachus's fourth conjecture <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>. Math historian William Dunham called it "the greatest mathematical collaboration in history" <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.
3.  **Refined Form for Odd Perfect Numbers**: Euler also set out to prove Descartes' statement about the specific form of odd perfect numbers <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>. He showed that if an odd perfect number *n* exists, it must have exactly one prime factor raised to an odd power, while all other prime factors must be raised to an even power <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>. He further refined the form of odd perfect numbers, but even he could not prove their existence <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>, writing, "Whether there are any odd perfect numbers is a most difficult question" <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.

### Peter Barlow (1776-1862)
For the next 150 years, little progress was made <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. English mathematician Peter Barlow incorrectly predicted that Euler's eighth perfect number "is the greatest that ever will be discovered" because they were "merely curious without being useful" <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.

### Edouard Lucas (1842-1891)
Mathematicians continued their pursuit, often focusing on Mersenne's list <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>. In 1876, 230 years after Mersenne published his list, Edouard Lucas proved that 2<sup>67</sup> - 1 was not prime, though he couldn't find its factors <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>.

### Frank Nelson Cole (1861-1926)
Twenty-seven years later, in 1903, Frank Nelson Cole famously demonstrated the factors of 2<sup>67</sup> - 1 to the American Mathematical Society without speaking <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>. He wrote 2<sup>67</sup> - 1 on one side of the blackboard and its two prime factors (193,707,721 and 761,838,257,287) on the other, then multiplied them to get the same result <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>. He admitted it took him three years of Sunday work <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>.

### Raphael Robinson (1911-1995)
From 500 BC until 1952, only 12 Mersenne primes (and thus 12 perfect numbers) were known <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>. The main challenge was verifying the primality of large Mersenne numbers <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>. In 1952, American mathematician Raphael Robinson wrote a computer program to perform this task on the SWAC, the fastest computer at the time <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>. Within 10 months, he discovered the next five Mersenne primes <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>. This marked a new era of rapid discovery using computers <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.

### George Woltman and GIMPS
As Mersenne primes became astronomically large, finding them grew increasingly difficult even for supercomputers <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>. In 1996, computer scientist George Woltman launched the Great Internet Mersenne Prime Search (GIMPS) <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>. GIMPS distributes the computational work across many volunteer computers worldwide <a class="yt-timestamp" data-t="00:19:09">[00:19:09]</a>. GIMPS has been highly successful, discovering 17 new Mersenne primes, 15 of which were the largest known primes at the time <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>.

### John Pace
In 2017, Church Deacon John Pace discovered the 50th Mersenne Prime using GIMPS: 2<sup>77,232,917</sup> - 1, a number more than 23 million digits long and the largest known prime at the time <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>. In 2018, the 51st Mersenne Prime was discovered, 2<sup>82,589,933</sup> - 1, which has over 24 million digits and remains the largest known prime today <a class="yt-timestamp" data-t="00:20:31">[00:20:31]</a>.

## The Pursuit of Odd Perfect Numbers
Despite extensive searches by computers, only 51 perfect numbers have been found so far <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>, all of them even. The question of whether any odd perfect numbers exist remains the oldest unsolved problem in math <a class="yt-timestamp" data-t="00:22:21">[00:22:21]</a>.

### Challenges in Finding Odd Perfect Numbers
Researchers have used sophisticated algorithms, such as factor chains, to determine that if an odd perfect number exists, it must be larger than 10<sup>300</sup> <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>. This lower bound has been pushed higher over time:
*   1991: > 10<sup>300</sup> <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>
*   2012 (Pascal Ochem and Michael Rao): > 10<sup>1,500</sup> <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>
*   Recent Progress: > 10<sup>2,200</sup> <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>

With such large numbers, it's unlikely that a computer will find an example soon <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.

### Current Approaches
Mathematicians are building a "web of conditions" that odd perfect numbers must satisfy <a class="yt-timestamp" data-t="00:23:15">[00:23:15]</a>. For instance, it is known that an odd perfect number must have at least 10 prime factors <a class="yt-timestamp" data-t="00:23:26">[00:23:26]</a> and must be larger than 10<sup>3000</sup> <a class="yt-timestamp" data-t="00:23:35">[00:23:35]</a>. The hope is that accumulating enough constraints will eventually prove their non-existence <a class="yt-timestamp" data-t="00:23:40">[00:23:40]</a>.

### Spoofs
Numbers that are very close to being odd perfect numbers are called "spoofs" <a class="yt-timestamp" data-t="00:24:34">[00:24:34]</a>. Descartes himself found an example of a spoof: 198,585,576,189 <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>. This number, when factored (3² × 7² × 11² × 13² × 22021), satisfies the condition σ(*n*) = 2*n* if 22021 were prime, but it is not (22021 = 19² × 61), thus it is not a true perfect number <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>. Odd perfect numbers would share all properties of spoofs plus additional ones <a class="yt-timestamp" data-t="00:24:43">[00:24:43]</a>. The goal is to find a property of spoofs that specifically prevents them from being odd perfect numbers <a class="yt-timestamp" data-t="00:24:48">[00:24:48]</a>. For example, it is known that odd perfect numbers cannot be divided by 105 <a class="yt-timestamp" data-t="00:24:55">[00:24:55]</a>. If spoofs *must* be divisible by 105, then this would prove the non-existence of odd perfect numbers <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>. In 2022, Pace Nielsen and a BYU team found 21 spoof numbers, including Descartes' example, but did not find a property that rules out odd perfect numbers <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>.

### Heuristic Arguments
Mathematicians like Carl Pomerance have developed heuristic arguments suggesting that odd perfect numbers should not exist <a class="yt-timestamp" data-t="00:26:09">[00:26:09]</a>. These arguments, based on the expected occurrence of prime numbers, predict that there are "no more than 10<sup>-540</sup> perfect numbers of the form N=pm²" between 10<sup>2,200</sup> and infinity <a class="yt-timestamp" data-t="00:26:09">[00:26:09]</a>. However, a heuristic is not a proof <a class="yt-timestamp" data-t="00:26:17">[00:26:17]</a>.

## Significance of Studying Perfect Numbers

Despite the lack of immediate "real-world applications" for perfect numbers <a class="yt-timestamp" data-t="00:27:32">[00:27:32]</a>, their study, like much of [[history of physics and mathematics discoveries | number theory]], exemplifies the importance of pursuing curiosity-driven research <a class="yt-timestamp" data-t="00:27:50">[00:27:50]</a>. For over 2000 years, [[history of physics and mathematics discoveries | number theory]] was considered "useless mathematics" <a class="yt-timestamp" data-t="00:27:51">[00:27:51]</a>. However, in the 20th century, this foundation proved essential for cryptography, which protects everything from text messages to government secrets <a class="yt-timestamp" data-t="00:28:04">[00:28:04]</a>. Similarly, Einstein's general relativity was built on [[Mathematical breakthroughs in the Renaissance | non-Euclidean geometries]], which were developed as intellectual curiosities <a class="yt-timestamp" data-t="00:28:45">[00:28:45]</a>.

The pursuit of challenging mathematical problems, even without knowing the outcome, often leads to new ideas and unforeseen applications <a class="yt-timestamp" data-t="00:28:36">[00:28:36]</a>. As of today, the question of whether odd perfect numbers exist remains the oldest unsolved problem in mathematics <a class="yt-timestamp" data-t="00:27:17">[00:27:17]</a>.