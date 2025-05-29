---
title: solving linear systems by substitution
videoId: V7H1oUHXPkg
---

From: [[khanacademy]] <br/> 

In previous discussions, we explored what a [[systems_of_equations | system of equations]] is <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article introduces an algebraic technique for [[solving_systems_of_equations | solving systems of equations]] without needing to graph the lines to find their intersection point <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This method provides an exact algebraic answer <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

While graphing can show the intersection of lines, it's often difficult to precisely determine the exact coordinates just by looking <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. The substitution method offers a precise algebraic approach to find the solution <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## The Substitution Method

The core idea of the substitution method is to use one of the equations to solve for one variable and then substitute that expression into the other equation <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. This process results in a single equation with a single unknown, which can then be solved <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

### Example 1: Basic Linear System

Consider the following [[systems_of_equations | system of equations]]:
*   Equation 1: `x + 2y = 9` <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>
*   Equation 2: `3x + 5y = 20` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>

These equations are currently in standard form <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

#### Steps to Solve:

1.  **Solve one equation for one variable:**
    From the first equation, `x + 2y = 9`, we can solve for `x` by subtracting `2y` from both sides <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>:
    `x = 9 - 2y` <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>

2.  **Substitute the expression into the other equation:**
    Substitute `(9 - 2y)` for `x` in the second equation, `3x + 5y = 20` <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>:
    `3(9 - 2y) + 5y = 20` <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>

3.  **Solve the resulting single-variable equation:**
    *   Distribute the `3`: `27 - 6y + 5y = 20` <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>
    *   Combine like terms: `27 - y = 20` <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>
    *   Subtract `27` from both sides: `-y = -7` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>
    *   Multiply by `-1`: `y = 7` <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>

4.  **Substitute the found value back into the expression for the first variable:**
    Now that we know `y = 7`, substitute it back into `x = 9 - 2y` <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>:
    `x = 9 - 2(7)` <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>
    `x = 9 - 14` <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>
    `x = -5` <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>

The solution to the system is `x = -5` and `y = 7` <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. If these two equations were graphed, they would intersect at the point `(-5, 7)` <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

#### Verification
To verify the solution, substitute `x = -5` and `y = 7` into both original equations:
*   **Equation 1:** `x + 2y = 9`
    `-5 + 2(7) = -5 + 14 = 9` (True) <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>
*   **Equation 2:** `3x + 5y = 20`
    `3(-5) + 5(7) = -15 + 35 = 20` (True) <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>

### Example 2: Word Problem Application

The substitution method is also useful for [[word_problems_involving_systems_of_equations | word problems involving systems of equations]] <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

**Problem:** The sum of two numbers is 70, and they differ by 11. What are the numbers? <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>

#### Translating to a System of Equations:

1.  **Define variables:** Let `x` be the larger number and `y` be the smaller number <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
2.  **Formulate equations:**
    *   "The sum of two numbers is 70": `x + y = 70` <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>
    *   "They differ by 11": `x - y = 11` <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>

This creates a [[systems_of_equations | system of two equations]] with two unknowns <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

#### Steps to Solve:

1.  **Solve one equation for one variable:**
    From the second equation, `x - y = 11`, solve for `x` by adding `y` to both sides <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>:
    `x = 11 + y` <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>

2.  **Substitute the expression into the other equation:**
    Substitute `(11 + y)` for `x` in the first equation, `x + y = 70` <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>:
    `(11 + y) + y = 70` <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>

3.  **Solve the resulting single-variable equation:**
    *   Combine like terms: `11 + 2y = 70` <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>
    *   Subtract `11` from both sides: `2y = 59` <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>
    *   Divide by `2`: `y = 59/2` or `y = 29.5` <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>

4.  **Substitute the found value back into the expression for the first variable:**
    Now that we know `y = 29.5`, substitute it back into `x = 11 + y` <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>:
    `x = 11 + 29.5` <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>
    `x = 40.5` <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>

The two numbers are `40.5` and `29.5` <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.

#### Verification
*   **Sum:** `40.5 + 29.5 = 70` (True) <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>
*   **Difference:** `40.5 - 29.5 = 11` (True) <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>

Regardless of which variable or equation is chosen first, the important aspect is to use both constraints provided by the [[systems_of_equations | system of equations]] to find the unique solution <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.