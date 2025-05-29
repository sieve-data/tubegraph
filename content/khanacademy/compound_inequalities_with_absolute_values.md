---
title: Compound inequalities with absolute values
videoId: iI_2Piwn_og
---

From: [[khanacademy]] <br/> 

[[Solving absolute value inequalities | Solving inequalities]] that involve [[absolute_value_in_algebra | absolute values]] can often be confusing, but understanding the core meaning of absolute value helps simplify the process <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The absolute value of a number represents its distance from zero on a number line <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Basic Absolute Value Inequalities

### Absolute Value Less Than a Number

Consider the inequality:
`|x| < 12` <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>

This asks: "What are all the x's that are less than 12 units away from 0?" <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

> [!INFO] Visualization
> On a [[visualizing_number_line_for_inequalities | number line]], if 0 is at the center, numbers less than 12 units away would fall between -12 and 12 <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
>
> ```
> <----|--------------------|--------------------|-------------------->
>     -12                     0                    12
> ```
> Anything between -12 and 12 (exclusive) has an absolute value less than 12 <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

This translates to a compound inequality:
`x > -12` AND `x < 12` <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>

In [[interval_notation_and_set_notation_in_inequalities | interval notation]], the solution is `(-12, 12)` <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
Alternatively, it can be written as `-12 < x < 12` <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Absolute Value Greater Than or Equal to a Number

Consider the inequality:
`|7x| >= 21` <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>

This means that whatever is inside the absolute value, `7x`, must be 21 or more units away from 0 <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

> [!INFO] Visualization
> On a [[visualizing_number_line_for_inequalities | number line]], numbers 21 or more units away from 0 would be either 21 or greater, or -21 or less <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
>
> ```
> <----|--------------------|--------------------|-------------------->
>     -21                     0                    21
> ```
> Numbers to the left of -21 (e.g., -30) have an absolute value greater than 21 (e.g., `|-30| = 30`) <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. Similarly, numbers to the right of 21 have an absolute value greater than 21 <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

This translates into two separate inequalities connected by "OR":
1.  `7x <= -21` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>
2.  `7x >= 21` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>

[[Understanding and manipulating equalities | Solving]] each:
1.  `7x <= -21`  =>  `x <= -3` (divide by 7) <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>
2.  `7x >= 21`   =>  `x >= 3` (divide by 7) <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>

The solution set on a [[visualizing_number_line_for_inequalities | number line]]:
```
<---------|--------------------|--------------------|--------->
         -3                     0                    3
<========]                      [========>
```
So, `x <= -3` OR `x >= 3` <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

## More Complex Absolute Value Inequalities

### Absolute Value Less Than a Number (with Expression)

Consider the inequality:
`|5x + 3| < 7` <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>

This means the expression `5x + 3` must be less than 7 units away from 0 <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.

> [!INFO] Visualization
> The value of `5x + 3` must be between -7 and 7 <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
> ```
> <----|--------------------|--------------------|-------------------->
>     -7                     0                    7
> ```

This translates to a compound inequality:
`-7 < 5x + 3 < 7` <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>

To [[understanding_and_manipulating_equalities | solve]] this, perform operations on all three parts simultaneously:
1.  Subtract 3 from all parts:
    `-7 - 3 < 5x + 3 - 3 < 7 - 3`
    `-10 < 5x < 4` <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>
2.  Divide all parts by 5:
    `-10 / 5 < 5x / 5 < 4 / 5`
    `-2 < x < 4/5` <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>

The solution set is `x` is greater than -2 AND `x` is less than 4/5 <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

### Absolute Value Greater Than a Number (with Expression)

Consider the inequality:
`|2x/7 + 9| > 5/7` <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>

This means the expression `2x/7 + 9` must be more than 5/7 units away from 0 <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.

This translates into two separate inequalities:
1.  `2x/7 + 9 > 5/7` <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>
2.  `2x/7 + 9 < -5/7` <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>

[[Understanding and manipulating equalities | Solving]] each:
**For the first inequality:**
`2x/7 + 9 > 5/7`
Multiply the entire inequality by 7 to eliminate denominators <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>:
`7 * (2x/7) + 7 * 9 > 7 * (5/7)`
`2x + 63 > 5` <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>
Subtract 63 from both sides:
`2x > 5 - 63`
`2x > -58` <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>
Divide by 2:
`x > -29` <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>

**For the second inequality:**
`2x/7 + 9 < -5/7`
Multiply the entire inequality by 7:
`7 * (2x/7) + 7 * 9 < 7 * (-5/7)`
`2x + 63 < -5` <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>
Subtract 63 from both sides:
`2x < -5 - 63`
`2x < -68` <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>
Divide by 2:
`x < -34` <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>

The solution set on a [[visualizing_number_line_for_inequalities | number line]]:
```
<---------|--------------------|--------------------|--------->
         -34                  -29                    0
<========)                      (========>
```
So, `x < -34` OR `x > -29` <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.

## General Rules for Absolute Value Inequalities

While understanding the visualization is key, these patterns can be summarized:

> [!NOTE] Absolute Value Less Than
> If `|f(x)| < a` (where `a` is a positive number) <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>:
> This means `f(x)` is less than `a` units away from 0 <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
> It translates to: `-a < f(x) < a` <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

> [!NOTE] Absolute Value Greater Than
> If `|f(x)| > a` (where `a` is a positive number) <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>:
> This means `f(x)` is more than `a` units away from 0 <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
> It translates to: `f(x) > a` OR `f(x) < -a` <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

These rules also apply to `>=` and `<=` inequalities. It is important to grasp the underlying meaning rather than just memorizing the formulas <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.