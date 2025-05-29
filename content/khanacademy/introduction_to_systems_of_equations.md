---
title: Introduction to systems of equations
videoId: V7H1oUHXPkg
---

From: [[khanacademy]] <br/> 

A system of equations involves two or more equations with common variables, where the goal is to find values for those variables that satisfy all equations simultaneously <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While [[Graphical interpretation of systems of equations | graphical interpretation of systems of equations]] can show where lines intersect, it's often challenging to find the exact intersection point by just looking <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This article introduces an algebraic technique to find precise solutions: the [[Substitution method for solving linear systems | substitution method]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>, <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## The Substitution Method

The [[Substitution method for solving linear systems | substitution method]] is an algebraic technique for [[solving linear equations | solving systems of equations]] without requiring you to graph the lines <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This method yields an exact algebraic answer <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

The core idea is to use one of the equations to solve for one variable, and then substitute that expression into the other equation <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. This reduces the problem to a single equation with a single unknown, which can then be solved <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

### Example 1: Solving a System of Equations

Consider the following system of equations:
1.  `x + 2y = 9` <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>
2.  `3x + 5y = 20` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>

These equations are in [[Linear equations representation | standard form]] <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a> and represent lines <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

#### Steps:

1.  **Solve one equation for one variable** <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
    Let's use the first equation, `x + 2y = 9`, to solve for `x` <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
    Subtract `2y` from both sides:
    `x = 9 - 2y` <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>
    This rearranged equation tells us what `x` must be in terms of `y` <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

2.  **Substitute the expression into the other equation** <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
    Substitute `(9 - 2y)` for `x` in the second equation (`3x + 5y = 20`) <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>:
    `3 * (9 - 2y) + 5y = 20` <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>
    Now, you have one equation with only one unknown (`y`) <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

3.  **Solve the resulting single-variable equation** <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
    *   Distribute the 3:
        `27 - 6y + 5y = 20` <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>
    *   Combine like terms (`-6y + 5y`):
        `27 - y = 20` <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>
    *   Subtract 27 from both sides:
        `-y = 20 - 27` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>
        `-y = -7` <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>
    *   Multiply by -1:
        `y = 7` <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>

4.  **Substitute the found value back into one of the original or rearranged equations to find the other variable** <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
    Use the rearranged equation `x = 9 - 2y` <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>:
    `x = 9 - 2 * (7)` <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>
    `x = 9 - 14` <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>
    `x = -5` <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>

5.  **Verify the solution** <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
    The solution is `x = -5` and `y = 7`.
    *   For `x + 2y = 9`:
        `-5 + 2 * (7) = -5 + 14 = 9` (Correct) <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>
    *   For `3x + 5y = 20`:
        `3 * (-5) + 5 * (7) = -15 + 35 = 20` (Correct) <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>

The point of intersection for these two lines is `(-5, 7)` <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

## Solving Word Problems Using Substitution

The [[Substitution method for solving linear systems | substitution method]] is also useful for [[Interpreting and solving word problems with systems of equations | interpreting and solving word problems with systems of equations]] <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. The key is to translate the verbal statements into a [[systematic approach to solving equations | system of equations]].

### Example 2: Numbers Word Problem

"The sum of two numbers is 70. They differ by 11. What are the numbers?" <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>

#### Steps:

1.  **Define variables** <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
    Let `x` be the larger number and `y` be the smaller number <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

2.  **Formulate equations from the problem statements** <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
    *   "The sum of two numbers is 70":
        `x + y = 70` <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>
    *   "They differ by 11": (larger minus smaller)
        `x - y = 11` <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>

3.  **Solve the system using substitution** <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
    *   From the second equation (`x - y = 11`), solve for `x`:
        Add `y` to both sides:
        `x = 11 + y` <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>
    *   Substitute `(11 + y)` for `x` in the first equation (`x + y = 70`) <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>:
        `(11 + y) + y = 70` <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>
    *   Simplify and solve for `y`:
        `11 + 2y = 70` <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>
        Subtract 11 from both sides:
        `2y = 59` <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>
        Divide by 2:
        `y = 59 / 2` or `y = 29.5` <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>
    *   Substitute `y = 29.5` back into `x = 11 + y` to find `x` <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>:
        `x = 11 + 29.5` <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>
        `x = 40.5` <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>

4.  **Verify the solution** <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
    The numbers are 40.5 and 29.5.
    *   Sum: `40.5 + 29.5 = 70` (Correct) <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>
    *   Difference: `40.5 - 29.5 = 11` (Correct) <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>

The [[Substitution method for solving linear systems | substitution method]] is a versatile tool for [[solving linear equations | solving systems of equations]] algebraically, providing exact solutions whether from direct equations or [[Word problems involving systems of equations | word problems]] <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.