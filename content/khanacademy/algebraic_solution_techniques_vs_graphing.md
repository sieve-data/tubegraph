---
title: Algebraic solution techniques vs graphing
videoId: V7H1oUHXPkg
---

From: [[khanacademy]] <br/> 

When solving a system of equations, there are various techniques. While [[graphical_interpretation_of_systems_of_equations | graphing]] can provide a visual understanding, algebraic methods offer precise solutions <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Limitations of Graphing
Previously, systems of equations could be solved by [[graphing_linear_equations | graphing]] each line and finding their intersection point <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Although equations like `x + 2y = 9` and `3x + 5y = 20` represent lines and are typically in standard form, they can be converted to slope-intercept or point-slope form for [[graphing_linear_equations | graphing]] <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. However, visually identifying the exact point of intersection can be challenging <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## The Substitution Method
The substitution method is an algebraic technique that provides an exact answer for the solution to a system of equations <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This method involves [[using_algebraic_steps_to_solve_equations | using algebraic steps to solve equations]] to isolate a variable in one equation, and then substituting that expression into the other equation <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

### Step-by-Step Example
Consider the system of equations:
1.  `x + 2y = 9` <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>
2.  `3x + 5y = 20` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>

#### 1. Solve one equation for one variable
Begin by solving one of the equations for either `x` or `y`. Using the first equation (`x + 2y = 9`), subtract `2y` from both sides to solve for `x` <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>:
`x = 9 - 2y` <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>

#### 2. Substitute the expression into the other equation
Now, substitute the expression `(9 - 2y)` for `x` into the second equation (`3x + 5y = 20`) <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>:
`3(9 - 2y) + 5y = 20` <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>

#### 3. Solve the resulting single-variable equation
This new equation has only one unknown (`y`), allowing for its direct solution <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>:
*   Distribute the `3`: `27 - 6y + 5y = 20` <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>
*   Combine like terms: `27 - y = 20` <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>
*   Subtract `27` from both sides: `-y = -7` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>
*   Multiply by `-1`: `y = 7` <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>

#### 4. Substitute back to find the other variable
With the value of `y` found, substitute it back into the equation solved in step 1 (`x = 9 - 2y`) <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>:
*   `x = 9 - 2(7)` <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>
*   `x = 9 - 14` <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>
*   `x = -5` <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>

The solution to the system is `x = -5` and `y = 7` <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

#### 5. Verification
To verify the solution, [[using_substitution_to_verify_algebraic_solutions | substitute]] both `x` and `y` values into the original equations:
*   For `x + 2y = 9`: `-5 + 2(7) = -5 + 14 = 9`. This is correct <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   For `3x + 5y = 20`: `3(-5) + 5(7) = -15 + 35 = 20`. This is also correct <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

This means that if these two lines were [[graphing_linear_equations | graphed]], they would intersect at the point `(-5, 7)` <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

## Applying to Word Problems
The substitution method is also effective for solving word problems by first translating the problem into a system of equations.

> [!EXAMPLE] Word Problem Example
> The sum of two numbers is 70, and they differ by 11. What are the numbers? <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>

#### 1. Define variables
Let `x` be the larger number and `y` be the smaller number <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

#### 2. Formulate the system of equations
*   "The sum of two numbers is 70": `x + y = 70` <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>
*   "They differ by 11": `x - y = 11` <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>

#### 3. Solve the system using substitution
*   From `x - y = 11`, solve for `x`: `x = 11 + y` <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
*   Substitute `(11 + y)` for `x` into `x + y = 70`: `(11 + y) + y = 70` <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
*   Simplify and solve for `y`:
    *   `11 + 2y = 70` <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>
    *   `2y = 59` <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>
    *   `y = 59 / 2 = 29.5` <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>
*   Substitute `y = 29.5` back into `x = 11 + y`:
    *   `x = 11 + 29.5` <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>
    *   `x = 40.5` <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>

The two numbers are `40.5` and `29.5` <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.

#### 4. Verification
*   Sum: `40.5 + 29.5 = 70`. Correct <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
*   Difference: `40.5 - 29.5 = 11`. Correct <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

> [!TIP] Flexibility in Substitution
> Any variable from any equation can be isolated and substituted, as long as both original equations (constraints) are ultimately used in the solving process <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. The key is to transform a system with multiple unknowns into a single equation with one unknown, which is a core concept in [[introduction_to_algebra | algebra]] and a [[systematic_approach_to_solving_equations | systematic approach to solving equations]].