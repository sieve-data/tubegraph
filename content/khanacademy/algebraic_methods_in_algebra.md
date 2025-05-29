---
title: algebraic methods in algebra
videoId: V7H1oUHXPkg
---

From: [[khanacademy]] <br/> 

[[introduction_to_algebra | Algebra]] provides several techniques for solving systems of equations without relying on graphing. These [[algebraic_operations_and_their_legitimacy | algebraic]] techniques yield exact answers, unlike graphical methods which can sometimes be imprecise in determining intersection points <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. One such method is the substitution method <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. Future discussions will cover other [[elimination_method_in_algebra | elimination methods]] for solving systems of equations <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## The Substitution Method

The substitution method involves using one equation to solve for one of the variables and then substituting that expression into the other equation <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. This reduces the system to a single equation with a single unknown, which can then be solved <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

### Example: Solving a System of Linear Equations

Consider the following system of equations:
1.  `x + 2y = 9` <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>
2.  `3x + 5y = 20` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>

Traditionally, one might graph these lines to find their intersection point, but this can be difficult to determine precisely <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. [[graphing_versus_algebraic_solutions | Algebraic methods]] offer an exact solution <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

#### Steps for Substitution

1.  **Solve one equation for one variable:**
    From the first equation, `x + 2y = 9`, solve for `x` by subtracting `2y` from both sides <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>:
    `x = 9 - 2y` <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>

2.  **Substitute the expression into the other equation:**
    Substitute `(9 - 2y)` for `x` in the second equation, `3x + 5y = 20` <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>, <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>:
    `3(9 - 2y) + 5y = 20` <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>

3.  **Solve the resulting single-variable equation:**
    *   Distribute the `3`: `27 - 6y + 5y = 20` <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>
    *   Combine like terms: `27 - y = 20` <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>
    *   Subtract `27` from both sides: `-y = 20 - 27` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>
    *   Simplify: `-y = -7` <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>
    *   Multiply by `-1`: `y = 7` <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>

4.  **Substitute the found value back into one of the original or rearranged equations to find the other variable:**
    Using `x = 9 - 2y` and `y = 7` <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>:
    `x = 9 - 2(7)` <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>
    `x = 9 - 14` <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>
    `x = -5` <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>

The solution is `x = -5` and `y = 7` <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. This represents the point `(-5, 7)` where the two lines intersect <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

#### [[checking_solutions_in_algebra | Checking Solutions]]

To verify the solution, substitute `x = -5` and `y = 7` into both original equations:
*   For `x + 2y = 9`:
    `-5 + 2(7) = -5 + 14 = 9` (Correct) <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>
*   For `3x + 5y = 20`:
    `3(-5) + 5(7) = -15 + 35 = 20` (Correct) <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>

Both equations are satisfied, confirming the solution <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

## [[word_problems_in_algebra | Word Problems]] and Applications

The substitution method is useful for solving [[applications_of_algebra_in_various_domains | word problems]] by translating them into a system of equations <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

### Example: Finding Two Numbers

**Problem:** The sum of two numbers is 70, and they differ by 11. What are the numbers? <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>

#### Steps

1.  **Define variables:**
    Let `x` be the larger number and `y` be the smaller number <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

2.  **Formulate equations from the given statements:**
    *   "The sum of two numbers is 70": `x + y = 70` <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>
    *   "They differ by 11": `x - y = 11` <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>

3.  **Solve the system using substitution:**
    *   Solve the second equation for `x`:
        `x - y = 11`
        Add `y` to both sides: `x = 11 + y` <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>
    *   Substitute this expression for `x` into the first equation:
        `(11 + y) + y = 70` <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>
    *   Solve for `y`:
        `11 + 2y = 70` <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>
        Subtract `11` from both sides: `2y = 59` <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>
        Divide by `2`: `y = 59/2` or `y = 29.5` <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>
    *   Substitute `y = 29.5` back into `x = 11 + y` to find `x`:
        `x = 11 + 29.5` <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>
        `x = 40.5` <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>

The two numbers are `40.5` and `29.5` <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.

#### Verification

*   Sum: `40.5 + 29.5 = 70` (Correct) <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>
*   Difference: `40.5 - 29.5 = 11` (Correct) <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>

Both constraints are satisfied <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.