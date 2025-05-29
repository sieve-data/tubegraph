---
title: Substitution method for solving linear systems
videoId: V7H1oUHXPkg
---

From: [[khanacademy]] <br/> 

The substitution method is an algebraic technique used for [[solving_systems_of_equations_using_elimination | solving systems of equations]] without having to graph the lines to find their intersection point <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This method provides an exact algebraic answer <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## How the Substitution Method Works

The core idea of the substitution method is to use one of the equations to solve for one of the variables, and then substitute that expression into the other equation <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. This process transforms a system of two equations with two unknowns into a single equation with one unknown, which can then be solved <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

### Steps:
1.  **Isolate a Variable**: Choose one of the equations and solve for one of its variables (e.g., isolate `x` or `y`) <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. This means rearranging the equation so that the chosen variable is on one side, and all other terms are on the other side <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
2.  **Substitute**: Substitute the expression obtained in step 1 into the *other* equation <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
3.  **Solve**: Solve the resulting single-variable equation <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. This will give you the value of one of the variables <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
4.  **Back-Substitute**: Substitute the value found in step 3 back into the expression from step 1 (or either of the original equations) to find the value of the second variable <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
5.  **Verify**: Optionally, [[using_substitution_to_verify_algebraic_solutions | verify]] the solution by plugging both values back into both original equations to ensure they are satisfied <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

## [[example_problems_using_substitution_method | Example Problem]]: Solving a System of Equations

Consider the following system of equations:
1.  `x + 2y = 9` <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>
2.  `3x + 5y = 20` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>

These equations represent lines, and their intersection point is the solution to the system <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

### Step-by-Step Solution:

1.  **Isolate x from the first equation**:
    *   Start with `x + 2y = 9` <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
    *   Subtract `2y` from both sides: `x = 9 - 2y` <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>, <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>

2.  **Substitute this expression for x into the second equation**:
    *   The second equation is `3x + 5y = 20` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>
    *   Substitute `(9 - 2y)` for `x`: `3(9 - 2y) + 5y = 20` <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>, <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>

3.  **Solve for y**:
    *   Distribute the 3: `27 - 6y + 5y = 20` <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>, <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>
    *   Combine like terms: `27 - y = 20` <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>
    *   Subtract 27 from both sides: `-y = 20 - 27` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>, <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>
    *   `-y = -7` <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>
    *   Multiply by -1: `y = 7` <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>, <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>

4.  **Back-substitute y to find x**:
    *   Use the expression `x = 9 - 2y` <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>
    *   Substitute `y = 7`: `x = 9 - 2(7)` <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>
    *   `x = 9 - 14` <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>
    *   `x = -5` <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>, <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>

The solution is `x = -5` and `y = 7`, which means the lines intersect at the point `(-5, 7)` <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

### Verification:
*   For `x + 2y = 9`: `-5 + 2(7) = -5 + 14 = 9` (Correct) <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>, <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>
*   For `3x + 5y = 20`: `3(-5) + 5(7) = -15 + 35 = 20` (Correct) <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>, <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>

## [[word_problems_involving_systems_of_equations | Word Problem Example]]

Let's use the substitution method to solve a [[word_problems_involving_systems_of_equations | word problem]]: "The sum of two numbers is 70, and they differ by 11. What are the numbers?" <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>, <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>, <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

### Step-by-Step Solution:

1.  **Define Variables**:
    *   Let `x` be the larger number <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
    *   Let `y` be the smaller number <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

2.  **Formulate Equations**:
    *   "The sum of two numbers is 70": `x + y = 70` <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>, <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>
    *   "They differ by 11": `x - y = 11` (larger minus smaller) <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>, <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>

3.  **Isolate a Variable (from the second equation)**:
    *   Start with `x - y = 11` <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>
    *   Add `y` to both sides: `x = 11 + y` <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>, <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>

4.  **Substitute this expression for x into the first equation**:
    *   The first equation is `x + y = 70` <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>
    *   Substitute `(11 + y)` for `x`: `(11 + y) + y = 70` <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>, <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>

5.  **Solve for y**:
    *   Combine like terms: `11 + 2y = 70` <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>, <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>
    *   Subtract 11 from both sides: `2y = 70 - 11` <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>
    *   `2y = 59` <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>
    *   Divide by 2: `y = 59 / 2` <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>
    *   `y = 29.5` <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>

6.  **Back-substitute y to find x**:
    *   Use the expression `x = 11 + y` <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>
    *   Substitute `y = 29.5`: `x = 11 + 29.5` <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>, <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>
    *   `x = 40.5` <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>

The two numbers are `40.5` and `29.5` <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.

### Verification:
*   Sum: `40.5 + 29.5 = 70` (Correct) <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>, <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>
*   Difference: `40.5 - 29.5 = 11` (Correct) <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>, <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>

The solution `(40.5, 29.5)` would also be the intersection point if these equations were graphed <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. The key to the substitution method is to utilize both constraints (equations) to find the solution <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.