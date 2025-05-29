---
title: Solving linear systems with substitution
videoId: V7H1oUHXPkg
---

From: [[khanacademy]] <br/> 

The substitution method is an algebraic technique used to [[methods_for_solving_systems_of_equations | solve systems of equations]] without relying on graphing. This method provides an exact algebraic answer for the point of intersection of the lines represented by the equations <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## How the Substitution Method Works

The core idea behind the substitution method is to use one equation to express one variable in terms of the other, and then substitute that expression into the second equation <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. This reduces the problem to a single equation with a single unknown, which can then be solved <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

### Example 1: Solving a System with Numbers

Consider the following system of linear equations:
1.  `x + 2y = 9` <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>
2.  `3x + 5y = 20` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>

**Steps:**

1.  **Solve one equation for one variable.**
    It is often easiest to pick the equation where a variable has a coefficient of 1 or -1. In this case, use the first equation to solve for `x`:
    `x + 2y = 9` <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
    Subtract `2y` from both sides:
    `x = 9 - 2y` <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>

2.  **Substitute this expression into the *other* equation.**
    Now that `x` is expressed in terms of `y`, substitute `(9 - 2y)` for `x` in the second equation:
    `3(9 - 2y) + 5y = 20` <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>

3.  **Solve the resulting single-variable equation.**
    *   Distribute the 3:
        `27 - 6y + 5y = 20` <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>
    *   Combine like terms:
        `27 - y = 20` <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>
    *   Subtract 27 from both sides:
        `-y = 20 - 27` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>
        `-y = -7` <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>
    *   Multiply both sides by -1:
        `y = 7` <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>

4.  **Substitute the found value back into one of the original or rearranged equations to find the other variable.**
    Use the rearranged equation `x = 9 - 2y` and substitute `y = 7`:
    `x = 9 - 2(7)` <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>
    `x = 9 - 14` <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>
    `x = -5` <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>

**Solution:**
The solution to the system is `x = -5` and `y = 7`, or the point `(-5, 7)` <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. If these equations were graphed, they would intersect at this point <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

### Verification
*   For `x + 2y = 9`:
    `-5 + 2(7) = -5 + 14 = 9` (True) <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>
*   For `3x + 5y = 20`:
    `3(-5) + 5(7) = -15 + 35 = 20` (True) <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>

## Example 2: Word Problem Application

The substitution method can also be used to solve word problems by first converting them into a system of equations <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

**Problem:** The sum of two numbers is 70. They differ by 11. What are the numbers? <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>

**Steps:**

1.  **Define variables.**
    Let `x` be the larger number and `y` be the smaller number <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

2.  **Formulate the system of equations.**
    *   "The sum of two numbers is 70": `x + y = 70` <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>
    *   "They differ by 11": `x - y = 11` <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>

3.  **Solve the system using substitution.**
    *   Solve the second equation for `x`:
        `x - y = 11`
        Add `y` to both sides:
        `x = 11 + y` <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>
    *   Substitute `(11 + y)` for `x` in the first equation:
        `(11 + y) + y = 70` <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>
    *   Solve for `y`:
        `11 + 2y = 70` <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>
        Subtract 11 from both sides:
        `2y = 70 - 11` <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>
        `2y = 59` <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>
        Divide by 2:
        `y = 59/2 = 29.5` <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>
    *   Substitute `y = 29.5` back into `x = 11 + y` to find `x`:
        `x = 11 + 29.5` <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>
        `x = 40.5` <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>

**Solution:**
The two numbers are 40.5 and 29.5 <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.

### Verification
*   Sum: `40.5 + 29.5 = 70` (True) <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>
*   Difference: `40.5 - 29.5 = 11` (True) <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>