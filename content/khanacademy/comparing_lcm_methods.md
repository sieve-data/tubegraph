---
title: Comparing LCM methods
videoId: znmPfDfsir8
---

From: [[khanacademy]] <br/> 

The [[least_common_multiple | least common multiple]] (LCM) of two or more numbers is the smallest number that is a multiple of all of them <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. It can be referred to as "LCM (x, y)" notation <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Methods for Finding the Least Common Multiple

There are two primary methods discussed for finding the [[least_common_multiple | least common multiple]]:

### 1. Prime Factorization Approach

This method involves breaking down each number into its prime factors <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. The [[least_common_multiple | LCM]] is then constructed by taking enough prime factors to cover all the "ingredients" of both numbers, but no more <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

**Example: Finding the LCM of 18 and 12**
1.  **Prime Factorization of 18**:
    *   18 = 2 × 9 <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>
    *   9 = 3 × 3 <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>
    *   So, 18 = 2 × 3 × 3 <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>
2.  **Prime Factorization of 12**:
    *   12 = 2 × 6 <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>
    *   6 = 2 × 3 <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>
    *   So, 12 = 2 × 2 × 3 <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>
3.  **Constructing the LCM**:
    *   To be divisible by 18, the LCM must include 2 × 3 × 3 <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
    *   To be divisible by 12, the LCM must include 2 × 2 × 3 <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
    *   We already have one 3 and one 2 from the 18's factors <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
    *   To satisfy 12's factors, we need an additional '2' <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
    *   Therefore, the [[least_common_multiple | LCM]] is 2 × 3 × 3 (for 18) × 2 (additional factor for 12) = 36 <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

### 2. Brute Force Method (Listing Multiples)

This [[brute_force_method_for_lcm | brute force method]] involves listing out the multiples of each number until the smallest common multiple is identified <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

**Example: Finding the LCM of 18 and 12**
1.  **Multiples of 18**: 18, 36, 54, ... <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>
2.  **Multiples of 12**: 12, 24, 36, ... <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>
3.  The smallest common multiple found is 36 <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

## When to Use Each Method

| Method                 | Description                                                                                                                                                                                                                                                                                                                                        |
| :--------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Prime Factorization** | This method is systematic and generally more effective for larger or more complex numbers <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. It involves decomposing numbers and building them back up, which can be an insightful process <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.                                                 |
| **Brute Force**        | This method can be quick for small numbers, especially when one number is already a multiple of the other (e.g., LCM of 36 and 12 is 36, because 36 is 12 × 3) <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. However, for "hairy" or very large numbers, you might have to list many multiples before finding a common one <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. |

The choice of method often depends on the complexity of the numbers involved.