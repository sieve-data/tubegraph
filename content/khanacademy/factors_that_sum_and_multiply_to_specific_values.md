---
title: Factors that sum and multiply to specific values
videoId: eF6zYNzlZKQ
---

From: [[khanacademy]] <br/> 

When factoring a second-degree polynomial, often called a quadratic, with a leading coefficient of 1, the goal is to express it as the product of two binomials <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This method relies on finding two numbers that satisfy specific sum and product conditions.

## The Sum and Product Rule

Consider the general form of a quadratic expression and its factored form:
$$ x^2 + (a+b)x + ab $$ <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>
This form is derived by [[basic_multiplication_concepts | multiplying]] two binomials `(x + a)` and `(x + b)`:
$$ (x+a)(x+b) = x \cdot x + x \cdot b + a \cdot x + a \cdot b $$ <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>
$$ (x+a)(x+b) = x^2 + bx + ax + ab $$ <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
By combining the `x` terms, we get:
$$ x^2 + (a+b)x + ab $$ <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>

From this, the fundamental rule for factoring a quadratic in the form $x^2 + Bx + C$ emerges:
*   The coefficient of the $x$ term (B) is the sum of two numbers, $a$ and $b$ ($a+b=B$) <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
*   The constant term (C) is the product of the same two numbers, $a$ and $b$ ($ab=C$) <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

It is generally assumed that the numbers $a$ and $b$ are integers when beginning to factor polynomials <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. If the quadratic is not in standard form (e.g., $x^2 + Bx + C$), it should be rearranged first <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

## Examples of Factoring

### Case 1: Both Sum and Product are Positive

**Example 1:** Factor $x^2 + 10x + 9$ <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>

1.  Identify target sum and product:
    *   Sum: $a+b = 10$ <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>
    *   Product: $ab = 9$ <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>
2.  List [[factors_and_multiples | factors]] of 9: (1, 9), (3, 3) <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
3.  Test sums:
    *   $3+3 = 6$ (Does not equal 10) <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>
    *   $1+9 = 10$ (Equals 10) <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>
4.  The numbers are 1 and 9.
5.  Factored form: $(x+1)(x+9)$ <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

**Example 2:** Factor $x^2 + 15x + 50$ <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>

1.  Identify target sum and product:
    *   Sum: $a+b = 15$ <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>
    *   Product: $ab = 50$ <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>
2.  List [[factors_and_multiples | factors]] of 50: (1, 50), (2, 25), (5, 10) <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
3.  Test sums:
    *   $1+50 = 51$ (Does not equal 15) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>
    *   $2+25 = 27$ (Does not equal 15) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>
    *   $5+10 = 15$ (Equals 15) <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>
4.  The numbers are 5 and 10.
5.  Factored form: $(x+5)(x+10)$ <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

### Case 2: Product is Positive, Sum is Negative

When the product ($ab$) is positive but the sum ($a+b$) is negative, both numbers ($a$ and $b$) must be negative <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

**Example:** Factor $x^2 - 11x + 24$ <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>

1.  Identify target sum and product:
    *   Sum: $a+b = -11$ <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>
    *   Product: $ab = 24$ <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>
2.  Since the product is positive and the sum is negative, both $a$ and $b$ must be negative <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
3.  List [[factors_and_multiples | factors]] of 24: (1, 24), (2, 12), (3, 8), (4, 6) <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
4.  Test sums with negative values:
    *   $(-1)+(-24) = -25$
    *   $(-2)+(-12) = -14$
    *   $(-3)+(-8) = -11$ (Equals -11) <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>
5.  The numbers are -3 and -8.
6.  Factored form: $(x-3)(x-8)$ <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

### Case 3: Product is Negative

When the product ($ab$) is negative, one number must be positive and the other must be negative <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. The sign of the sum ($a+b$) determines which of the absolute values is larger.

#### Subcase 3a: Product Negative, Sum Positive

If the sum is positive, the number with the larger absolute value must be positive.

**Example:** Factor $x^2 + 5x - 14$ <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>

1.  Identify target sum and product:
    *   Sum: $a+b = 5$ <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>
    *   Product: $ab = -14$ <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>
2.  Since the product is negative, one number is positive and one is negative. Since the sum is positive, the positive number will have a larger absolute value.
3.  List [[factors_and_multiples | factors]] of 14: (1, 14), (2, 7) <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
4.  Test combinations (one positive, one negative):
    *   $-1+14 = 13$ (Does not equal 5) <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>
    *   $1+(-14) = -13$
    *   $-2+7 = 5$ (Equals 5) <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>
5.  The numbers are -2 and 7.
6.  Factored form: $(x-2)(x+7)$ <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

#### Subcase 3b: Product Negative, Sum Negative

If the sum is negative, the number with the larger absolute value must be negative.

**Example:** Factor $x^2 - x - 56$ <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>

1.  Identify target sum and product:
    *   Sum: $a+b = -1$ (coefficient of $-x$) <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>
    *   Product: $ab = -56$ <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>
2.  Since the product is negative, one number is positive and one is negative. Since the sum is negative, the negative number will have a larger absolute value <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
3.  Consider [[factors_and_multiples | factors]] of 56 that are close to each other: (7, 8) <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.
4.  Test combinations:
    *   $8+(-7) = 1$
    *   $-8+7 = -1$ (Equals -1) <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>
5.  The numbers are -8 and 7.
6.  Factored form: $(x-8)(x+7)$ <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

### Factoring with a Negative Leading Coefficient

If the leading coefficient of the quadratic is negative (e.g., $-x^2$), factor out $-1$ from the entire expression first. This transforms the problem into a standard form with a leading coefficient of 1 <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

**Example 1:** Factor $-x^2 - 5x + 24$ <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>

1.  Factor out $-1$: $-1(x^2 + 5x - 24)$ <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.
2.  Now factor the inner quadratic $x^2 + 5x - 24$:
    *   Sum: $a+b = 5$ <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>
    *   Product: $ab = -24$ <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>
    *   One positive, one negative number. Since sum is positive, the larger absolute value is positive.
    *   Consider [[factors_and_multiples | factors]] of 24: (3, 8) <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
    *   Numbers are -3 and 8, because $-3+8=5$ and $-3 \times 8 = -24$ <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.
3.  Factored form: $-1(x-3)(x+8)$ <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.

**Example 2:** Factor $-x^2 + 18x - 72$ <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>

1.  Factor out $-1$: $-1(x^2 - 18x + 72)$ <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.
2.  Now factor the inner quadratic $x^2 - 18x + 72$:
    *   Sum: $a+b = -18$ <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>
    *   Product: $ab = 72$ <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>
    *   Since the product is positive and sum is negative, both numbers must be negative <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
    *   Consider [[factors_and_multiples | factors]] of 72: (6, 12) <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.
    *   Numbers are -6 and -12, because $(-6)+(-12)=-18$ and $(-6) \times (-12) = 72$ <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.
3.  Factored form: $-1(x-6)(x-12)$ <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.

Factoring quadratics is a skill that improves with practice, becoming "second nature" through repeated exposure to various examples <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a> <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.