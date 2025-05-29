---
title: Interpreting and creating equations from word problems
videoId: V7H1oUHXPkg
---

From: [[khanacademy]] <br/> 

Solving systems of equations is a fundamental skill in algebra. While [[graphical_interpretation_of_systems_of_equations | graphical interpretation of systems of equations]] can provide a [[visual_representation_of_equations | visual representation of equations]] and their solutions, it's often difficult to find an exact intersection point just by looking <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Algebraic techniques, such as the substitution method, offer a precise way to find solutions <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## The Substitution Method for Systems of Equations

The substitution method is an algebraic technique used to [[solving_algebraic_equations | solve algebraic equations]] within a [[understanding_systems_of_equations | system of equations]] without requiring a graph <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

### How the Substitution Method Works

The core idea is to use one equation to express one variable in terms of the other, and then substitute this expression into the second equation <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. This reduces the problem to [[solving_algebraic_equations | solving a single equation with one unknown]] <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

Let's consider a system of two linear equations:
*   Equation 1: `x + 2y = 9` <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>
*   Equation 2: `3x + 5y = 20` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>

1.  **Isolate a Variable**: Choose one of the equations and solve for one of the variables. For example, from `x + 2y = 9`, subtract `2y` from both sides to get `x = 9 - 2y` <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

    ```
    x + 2y = 9
    x = 9 - 2y <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>
    ```

2.  **Substitute the Expression**: Substitute the expression for the isolated variable into the *other* equation. In this case, replace `x` in the second equation (`3x + 5y = 20`) with `(9 - 2y)` <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>, <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

    ```
    3(9 - 2y) + 5y = 20 <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>
    ```

3.  **Solve the Single-Variable Equation**: Now you have an equation with only one variable (`y`). Solve for `y`:

    ```
    27 - 6y + 5y = 20 <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>
    27 - y = 20 <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>
    -y = 20 - 27 <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>
    -y = -7 <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>
    y = 7 <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>
    ```

4.  **Find the Second Variable**: Substitute the value you found back into the expression from Step 1 (or any of the original equations) to find the value of the other variable. Using `x = 9 - 2y`:

    ```
    x = 9 - 2(7) <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>
    x = 9 - 14 <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>
    x = -5 <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>
    ```

The solution to the system is `x = -5` and `y = 7` <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. This means if you were to graph both lines, they would intersect at the point `(-5, 7)` <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. You can verify this by plugging the values back into the original equations <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

## [[translating_word_problems_into_equations | Translating Word Problems into Equations]]

The substitution method is incredibly useful for [[translating_word_problems_into_equations | translating word problems into equations]] and then solving them. This involves [[interpreting_mathematical_statements | interpreting mathematical statements]] given in text form and converting them into algebraic expressions and equations.

### Example: "The Sum of Two Numbers is 70, and they Differ by 11"

To solve this word problem <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>:

1.  **Define Variables**: Assign variables to the unknown quantities. Let `x` be the larger number and `y` be the smaller number <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

2.  **Formulate Equations**:
    *   "The sum of two numbers is 70": This translates to `x + y = 70` <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
    *   "They differ by 11": This means the larger number minus the smaller number is 11, or `x - y = 11` <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

    Now you have a [[understanding_systems_of_equations | system of two equations]] with two unknowns <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>:
    *   `x + y = 70`
    *   `x - y = 11`

3.  **Solve the System Using Substitution**:
    *   **Isolate a Variable**: From the second equation, `x - y = 11`, add `y` to both sides to get `x = 11 + y` <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
    *   **Substitute**: Substitute `(11 + y)` for `x` in the first equation (`x + y = 70`) <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

        ```
        (11 + y) + y = 70 <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>
        ```

    *   **Solve for y**:

        ```
        11 + 2y = 70 <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>
        2y = 70 - 11 <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>
        2y = 59 <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>
        y = 59 / 2 <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>
        y = 29.5 <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>
        ```

    *   **Solve for x**: Substitute `y = 29.5` back into `x = 11 + y` <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

        ```
        x = 11 + 29.5 <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>
        x = 40.5 <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>
        ```

The two numbers are 40.5 and 29.5 <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. You can check the solution: `40.5 + 29.5 = 70` and `40.5 - 29.5 = 11` <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.

This [[systematic_approach_to_solving_equations | systematic approach to solving equations]] demonstrates the power of algebraic methods for [[understanding_relationships_and_equations_in_algebra | understanding relationships and equations in algebra]].