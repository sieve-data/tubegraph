---
title: Solving absolute value inequalities
videoId: iI_2Piwn_og
---

From: [[khanacademy]] <br/> 

Solving inequalities that include [[absolute_value_in_algebra | absolute values]] can often seem confusing, but by understanding the core meaning of [[absolute_value_in_algebra | absolute value]], the process becomes much clearer <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Understanding Absolute Value in Inequalities

The [[absolute_value_in_algebra | absolute value]] of a number represents its distance from zero <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This fundamental concept is key to solving [[absolute_value_in_algebra | absolute value]] inequalities <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. [[visualizing_number_line_for_inequalities | Visualizing a number line]] is highly recommended to avoid confusion and memorization of rules <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### Case 1: Absolute Value Less Than a Number (e.g., `|x| < a`)

Consider the inequality `|x| < 12` <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
This asks: "What are all the x's that are less than 12 units away from 0?" <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

On a [[visualizing_number_line_for_inequalities | number line]], if 0 is the center, numbers less than 12 away from 0 include anything between -12 and +12 <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

This translates to a [[compound_inequalities_with_absolute_values | compound inequality]]:
`x > -12` AND `x < 12` <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
This can be written compactly as `-12 < x < 12` <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

In [[interval_notation_and_set_notation_in_inequalities | interval notation]], the solution is `(-12, 12)` <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

### Case 2: Absolute Value Greater Than or Equal to a Number (e.g., `|f(x)| >= a`)

Consider `|7x| >= 21` <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
This asks: "What must `7x` be so that its [[absolute_value_in_algebra | absolute value]] is 21 or more away from 0?" <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

Using a [[visualizing_number_line_for_inequalities | number line]] with 0, -21, and +21:
Numbers whose [[absolute_value_in_algebra | absolute value]] is greater than or equal to 21 are those less than or equal to -21 (e.g., -30, whose [[absolute_value_in_algebra | absolute value]] is 30) OR those greater than or equal to +21 <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

This translates into two separate inequalities connected by "OR":
1.  `7x <= -21` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>
2.  `7x >= 21` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>

Solving these:
1.  `x <= -3` (divide both sides by 7) <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>
2.  `x >= 3` (divide both sides by 7) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>

The solution set is `x <= -3` OR `x >= 3` <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. On a [[visualizing_number_line_for_inequalities | number line]], this means values outside the range of (-3, 3) <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

### Case 3: Absolute Value Less Than a Number (e.g., `|f(x)| < a`)

Consider `|5x + 3| < 7` <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
This means that `5x + 3` must be less than 7 units away from 0 <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
This translates to the [[compound_inequalities_with_absolute_values | compound inequality]]:
`-7 < 5x + 3 < 7` <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

To solve:
1.  Subtract 3 from all parts: `-7 - 3 < 5x < 7 - 3`
    `-10 < 5x < 4` <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>
2.  Divide all parts by 5: `-10/5 < x < 4/5`
    `-2 < x < 4/5` <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>

The solution is `x > -2` AND `x < 4/5` <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. In [[interval_notation_and_set_notation_in_inequalities | interval notation]], `(-2, 4/5)` <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

## General Rules for Absolute Value Inequalities

While understanding is key, here are the general transformations:

*   **If `|f(x)| < a` (or `<= a`)**:
    This means `f(x)` is less than `a` units away from 0.
    It translates to `-a < f(x) < a` (or `-a <= f(x) <= a`) <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

*   **If `|f(x)| > a` (or `>= a`)**:
    This means `f(x)` is more than `a` units away from 0.
    It translates to `f(x) < -a` OR `f(x) > a` (or `f(x) <= -a` OR `f(x) >= a`) <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

### Example with Fractions

Consider `|2x/7 + 9| > 5/7` <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
Using the rule for `|f(x)| > a`, this splits into two inequalities:
1.  `2x/7 + 9 > 5/7` <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>
2.  `2x/7 + 9 < -5/7` <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>

To solve these, multiply all terms by 7 to clear the denominators <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>:
1.  `2x + 63 > 5` <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>
    Subtract 63: `2x > -58` <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>
    Divide by 2: `x > -29` <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>

2.  `2x + 63 < -5` <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>
    Subtract 63: `2x < -68` <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>
    Divide by 2: `x < -34` <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>

The solution set is `x > -29` OR `x < -34` <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>. This means numbers greater than -29 or less than -34 satisfy the original inequality <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.