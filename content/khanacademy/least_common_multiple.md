---
title: Least common multiple
videoId: znmPfDfsir8
---

From: [[khanacademy]] <br/> 

The least common multiple (LCM) of two or more numbers is the smallest number that is a [[multiples_of_numbers | multiple]] of all of them <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. It is also referred to as the smallest common multiple <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

The notation `LCM(a, b)` or `lcm(a, b)` is used to denote the [[finding_the_least_common_multiple | least common multiple]] of numbers 'a' and 'b' <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Examples of Finding the Least Common Multiple

### Example 1: LCM of 36 and 12

To find the [[finding_the_least_common_multiple | least common multiple]] of 36 and 12 <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>:
*   36 is a [[multiples_of_numbers | multiple]] of 12 <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.
*   36 is also a [[multiples_of_numbers | multiple]] of 36 (1 times 36) <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

Since 36 is a [[multiples_of_numbers | multiple]] of both 36 and 12, and it is the smallest such number, the LCM of 36 and 12 is 36 <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

### Example 2: LCM of 18 and 12

To find the [[finding_the_least_common_multiple | least common multiple]] of 18 and 12 <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>:

#### Method 1: [[prime_factorization_method | Prime Factorization Method]]

This approach involves taking the [[prime_factorization_method | prime factorization]] of both numbers and then constructing the smallest number whose [[prime_factorization_method | prime factorization]] includes all the necessary factors from both <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

1.  **Find the [[prime_factorization_method | prime factorization]] of 18:**
    *   18 = 2 x 9 <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>
    *   9 = 3 x 3 <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>
    *   So, 18 = 2 x 3 x 3 <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>

2.  **Find the [[prime_factorization_method | prime factorization]] of 12:**
    *   12 = 2 x 6 <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>
    *   6 = 2 x 3 <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>
    *   So, 12 = 2 x 2 x 3 <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>

3.  **Construct the LCM:**
    The LCM must contain enough prime factors to be divisible by both numbers <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
    *   To be divisible by 18, it needs 2 x 3 x 3 <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
    *   To be divisible by 12, it needs 2 x 2 x 3 <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
    *   We already have one 3 from 18, so the 3 from 12 is covered <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
    *   We already have one 2 from 18, but 12 requires two 2s, so an additional 2 is needed <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

    Therefore, the LCM is 2 x 3 x 3 (for 18) x 2 (additional 2 for 12) <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
    LCM (18, 12) = 2 x 2 x 3 x 3 = 36 <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

#### Method 2: Listing [[multiples_of_numbers | Multiples]] (Brute Force)

This method involves listing the [[multiples_of_numbers | multiples]] of each number until a common multiple is found <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

1.  **[[multiples_of_numbers | Multiples]] of 18:** 18, 36, 54, ... <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>
2.  **[[multiples_of_numbers | Multiples]] of 12:** 12, 24, 36, ... <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>

The smallest [[multiples_of_numbers | multiple]] common to both 18 and 12 is 36 <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

## [[comparison_of_methods_for_finding_least_common_multiple | Comparison of Methods]]

While listing [[multiples_of_numbers | multiples]] might seem simpler for small numbers <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>, the [[prime_factorization_method | prime factorization method]] is generally preferred <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>, especially for really large numbers <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. It provides a more systematic way to find the LCM without having to list potentially many [[multiples_of_numbers | multiples]] <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.