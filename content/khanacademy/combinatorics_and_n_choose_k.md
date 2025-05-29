---
title: Combinatorics and n choose k
videoId: iPwrDWQ7hPc
---

From: [[khanacademy]] <br/> 

The concept of "n choose k" is fundamental in [[binomial_coefficients_and_combinatorics | combinatorics]] <a class="yt-timestamp" data-t="04:44:00">[04:44:00]</a>. It represents the number of ways to choose *k* items from a set of *n* distinct items, without regard to the order of selection. These values serve as coefficients in the [[introduction_to_the_binomial_theorem | binomial theorem]] <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a>.

## Definition of "n choose k"

The notation "n choose k" can be written as $C(n, k)$ or $\binom{n}{k}$ <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>. Its formula is defined as:

$\binom{n}{k} = \frac{n!}{k!(n-k)!}$ <a class="yt-timestamp" data-t="05:18:00">[05:18:00]</a>

Where '!' denotes the factorial operation (e.g., $n! = n \times (n-1) \times \dots \times 1$). For these purposes, 0 factorial ($0!$) is defined as 1 <a class="yt-timestamp" data-t="09:31:00">[09:31:00]</a>.

## Calculating "n choose k" Examples

Let's apply this formula to calculate specific "n choose k" values, using $n=4$ as an example, as seen in the [[application_of_the_binomial_theorem_to_a_plus_b_to_the_4th_power | expansion of (a+b)⁴]] <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>:

### 4 choose 0

$\binom{4}{0} = \frac{4!}{0!(4-0)!} = \frac{4!}{0!4!} = \frac{4!}{1 \times 4!} = 1$ <a class="yt-timestamp" data-t="09:17:00">[09:17:00]</a>, <a class="yt-timestamp" data-t="09:31:00">[09:31:00]</a>, <a class="yt-timestamp" data-t="09:35:00">[09:35:00]</a>

### 4 choose 1

$\binom{4}{1} = \frac{4!}{1!(4-1)!} = \frac{4!}{1!3!} = \frac{4 \times 3 \times 2 \times 1}{1 \times (3 \times 2 \times 1)} = 4$ <a class="yt-timestamp" data-t="09:42:00">[09:42:00]</a>, <a class="yt-timestamp" data-t="09:58:00">[09:58:00]</a>, <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>

### 4 choose 2

$\binom{4}{2} = \frac{4!}{2!(4-2)!} = \frac{4!}{2!2!} = \frac{4 \times 3 \times 2 \times 1}{(2 \times 1) \times (2 \times 1)} = \frac{24}{4} = 6$ <a class="yt-timestamp" data-t="10:20:00">[10:20:00]</a>, <a class="yt-timestamp" data-t="10:36:00">[10:36:00]</a>, <a class="yt-timestamp" data-t="10:49:00">[10:49:00]</a>

### 4 choose 3

$\binom{4}{3} = \frac{4!}{3!(4-3)!} = \frac{4!}{3!1!} = \frac{4 \times 3 \times 2 \times 1}{(3 \times 2 \times 1) \times 1} = 4$ <a class="yt-timestamp" data-t="10:59:00">[10:59:00]</a>, <a class="yt-timestamp" data-t="11:14:00">[11:14:00]</a>, <a class="yt-timestamp" data-t="11:23:00">[11:23:00]</a>

### 4 choose 4

$\binom{4}{4} = \frac{4!}{4!(4-4)!} = \frac{4!}{4!0!} = \frac{4!}{4! \times 1} = 1$ <a class="yt-timestamp" data-t="11:27:00">[11:27:00]</a>, <a class="yt-timestamp" data-t="11:39:00">[11:39:00]</a>

These calculated values (1, 4, 6, 4, 1) are the coefficients found in the expansion of $(a+b)⁴$: $1a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + 1b^4$ <a class="yt-timestamp" data-t="11:48:00">[11:48:00]</a>.