---
title: Comparison of methods for finding least common multiple
videoId: znmPfDfsir8
---

From: [[khanacademy]] <br/> 

The [[least_common_multiple | least common multiple]] (LCM) is the smallest number that is a multiple of two or more given numbers <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. It can be written in notation as LCM(a, b) <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Methods for Finding the LCM

There are several approaches to [[finding_the_least_common_multiple | finding the least common multiple]] <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

### 1. Listing Multiples (Brute Force Method)

This method involves listing out the multiples of each number until a common multiple is found <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. The smallest number that appears in both lists is the LCM <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

**Example 1: LCM of 36 and 12**
In this case, 36 is already a multiple of 12 (12 x 3 = 36) <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. Since 36 is also a multiple of itself (36 x 1 = 36) <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>, the smallest number that is a multiple of both 36 and 12 is 36 <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

**Example 2: LCM of 18 and 12**
To find the LCM of 18 and 12 using this method:
*   Multiples of 18: 18, 36, 54... <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>
*   Multiples of 12: 12, 24, 36... <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>
The first common multiple found is 36 <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>, which is the [[least_common_multiple | least common multiple]] <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

### 2. Prime Factorization Method

The [[prime_factorization_method | prime factorization approach]] involves finding the prime factors of each number and then constructing the smallest number that contains all the "ingredients" (prime factors) of both <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. This method is more systematic and is generally better for larger numbers <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.

**Example: LCM of 18 and 12**

1.  **Find the prime factorization of each number:**
    *   18: 2 × 9 = 2 × 3 × 3 <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>
    *   12: 2 × 6 = 2 × 2 × 3 <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>

2.  **Construct the LCM using the prime factors:**
    The LCM must contain all the prime factors required to be divisible by both numbers <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
    *   To be divisible by 18, the LCM needs one '2' and two '3's (2 × 3 × 3) <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
    *   To be divisible by 12, the LCM needs two '2's and one '3' (2 × 2 × 3) <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

    Start with the factors for 18: 2 × 3 × 3.
    Now, compare with 12's factors: 2 × 2 × 3.
    The current set (2 × 3 × 3) has one '2' and one '3' needed for 12, but it's missing the second '2' from 12 <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
    Add the missing '2': 2 × 2 × 3 × 3 <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

3.  **Calculate the product:**
    2 × 2 × 3 × 3 = 4 × 3 × 3 = 12 × 3 = 36 <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
    Thus, the LCM of 18 and 12 is 36 <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

## Comparison of Methods

While the brute force method (listing multiples) might seem intuitive and straightforward for small numbers, the [[prime_factorization_method | prime factorization method]] is more robust <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. For very large or complex numbers, listing multiples can become tedious and time-consuming, requiring one to go "pretty far" to find the LCM <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. The prime factorization method allows for a more systematic and efficient calculation, particularly when dealing with "hairy numbers" <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.