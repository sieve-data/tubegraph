---
title: Application of least common multiple in problem solving
videoId: znmPfDfsir8
---

From: [[khanacademy]] <br/> 

The [[least_common_multiple | least common multiple]] (LCM) is the smallest number that is a multiple of two or more given numbers <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. It is commonly denoted as LCM(a, b) <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Solving for the [[least_common_multiple | LCM]] can be approached using different methods depending on the numbers involved.

## Finding the [[least_common_multiple | LCM]] of Two Numbers

### Case 1: One Number is a Multiple of the Other

When one of the numbers is already a multiple of the other, the larger number is the [[least_common_multiple | LCM]] <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

**Example: LCM of 36 and 12**
Since 36 is a multiple of 12 (12 x 3 = 36) <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a> and 36 is also a multiple of 36 (1 x 36 = 36) <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>, the smallest number that is a multiple of both 36 and 12 is 36 itself <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

### Case 2: General Approach (LCM of 18 and 12)

When neither number is a direct multiple of the other, more systematic methods are required to find the [[least_common_multiple | LCM]] <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

#### [[prime_factorization_method_for_finding_least_common_multiple | Prime Factorization Method]]

This method involves finding the prime factors of each number and then constructing the smallest number that includes all necessary prime factors from both <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

1.  **Find the prime factorization of each number:**
    *   For 18:
        *   18 = 2 x 9 <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>
        *   9 = 3 x 3 <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>
        *   So, 18 = 2 x 3 x 3 <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>
    *   For 12:
        *   12 = 2 x 6 <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>
        *   6 = 2 x 3 <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>
        *   So, 12 = 2 x 2 x 3 <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>

2.  **Construct the [[least_common_multiple | LCM]]:**
    *   The [[least_common_multiple | LCM]] must contain all prime factors of both numbers, with the highest power of each factor present in either factorization <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
    *   Start with the factors for 18: 2 x 3 x 3 <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This ensures the number is divisible by 18 <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
    *   Now, consider the factors for 12 (2 x 2 x 3):
        *   One '3' is already present <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
        *   One '2' is already present <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
        *   A second '2' is needed to accommodate 12's factors <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
    *   So, the [[least_common_multiple | LCM]] = 2 x 3 x 3 x 2 <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
    *   Calculating the product: 2 x 2 = 4; 4 x 3 = 12; 12 x 3 = 36 <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
    *   Therefore, LCM(18, 12) = 36 <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

#### [[brute_force_method_for_finding_least_common_multiple | Brute Force Method]] (Listing Multiples)

This method involves listing the multiples of each number until the first common multiple is found <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

1.  **List multiples for each number:**
    *   Multiples of 18: 18, 36, 54... <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>
    *   Multiples of 12: 12, 24, 36... <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>

2.  **Identify the smallest common multiple:**
    *   The first common multiple identified is 36 <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
    *   Therefore, LCM(18, 12) = 36 <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

## [[comparison_of_methods_for_calculating_least_common_multiple | Comparing Methods]]

While the [[brute_force_method_for_finding_least_common_multiple | brute force method]] can be quick for smaller numbers, the [[prime_factorization_method_for_finding_least_common_multiple | prime factorization approach]] offers a more systematic way to find the [[least_common_multiple | LCM]] <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. It is particularly advantageous when dealing with very large or complex numbers, as listing all multiples might become impractical <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.