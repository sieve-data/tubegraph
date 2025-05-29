---
title: Comparison of methods for calculating least common multiple
videoId: znmPfDfsir8
---

From: [[khanacademy]] <br/> 

The [[least_common_multiple_definition_and_explanation | least common multiple]] (LCM) is the smallest number that is a multiple of two or more given numbers <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. It can also be expressed as "LCM(a, b)" notation <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Several methods can be used to find the [[least common multiple | LCM]], each with its own advantages.

## Direct Observation Method

In certain straightforward cases, the [[least common multiple | LCM]] can be identified by direct observation. This occurs when one of the numbers is already a multiple of the other <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

### Example: LCM of 36 and 12

*   The [[least common multiple | LCM]] of 36 and 12 is 36 <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.
*   This is because 36 is a multiple of 12 (12 x 3 = 36) <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.
*   Also, 36 is a multiple of itself (36 x 1 = 36) <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
*   Therefore, the smallest number that is a multiple of both 36 and 12 is 36 <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## [[prime_factorization_method_for_finding_least_common_multiple | Prime Factorization Method]]

The [[prime_factorization_method_for_finding_least_common_multiple | prime factorization approach]] is a systematic way to find the [[least common multiple | LCM]], especially useful for larger numbers <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. This method involves breaking down each number into its prime factors.

### Steps:

1.  **Find the prime factorization** for each number <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
2.  **Construct the LCM** by taking the highest power of all prime factors present in either number's factorization <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. The resulting number will have all the necessary "ingredients" to be divisible by both original numbers <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

### Example: LCM of 18 and 12

1.  **Prime factorization of 18:**
    *   18 = 2 x 9 <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>
    *   9 = 3 x 3 <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>
    *   So, 18 = 2 x 3 x 3 <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>

2.  **Prime factorization of 12:**
    *   12 = 2 x 6 <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>
    *   6 = 2 x 3 <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>
    *   So, 12 = 2 x 2 x 3 <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>

3.  **Constructing the LCM:**
    *   To be divisible by 18, the LCM needs at least one 2, one 3, and another 3 (2 x 3 x 3) <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
    *   To be divisible by 12, the LCM needs two 2s and one 3 (2 x 2 x 3) <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
    *   Combining these requirements, we start with 2 x 3 x 3 (for 18). We already have one 3 and one 2 for 12, but we need another 2 <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
    *   Therefore, the [[least common multiple | LCM]] = 2 x 2 x 3 x 3 <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
    *   Calculating the product: 2 x 2 = 4; 4 x 3 = 12; 12 x 3 = 36 <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
    *   The [[least common multiple | LCM]] of 18 and 12 is 36 <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

## [[brute_force_method_for_finding_least_common_multiple | Brute Force Method]] (Listing Multiples)

This [[brute_force_method_for_finding_least_common_multiple | method]] involves listing out the multiples of each number until the first common multiple is found <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

### Steps:

1.  **List multiples** for the first number.
2.  **List multiples** for the second number.
3.  **Identify the smallest common number** in both lists.

### Example: LCM of 18 and 12

*   **Multiples of 18:** 18, 36, 54... <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>
*   **Multiples of 12:** 12, 24, 36... <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>
*   The smallest common multiple found in both lists is 36 <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

## Comparison and Recommendation

While the [[brute_force_method_for_finding_least_common_multiple | brute force method]] might seem simpler for small numbers <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>, the [[prime_factorization_method_for_finding_least_common_multiple | prime factorization method]] offers a more structured and reliable approach <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

*   The [[prime_factorization_method_for_finding_least_common_multiple | prime factorization method]] involves decomposing numbers and then rebuilding them <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   For "really, really large and hairy numbers," listing multiples can become tedious and inefficient, potentially requiring one to go "pretty far" before finding the [[least common multiple | LCM]] <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   The [[prime_factorization_method_for_finding_least_common_multiple | prime factorization method]] provides a more systematic way to find the [[least common multiple | LCM]] regardless of the size of the numbers <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.