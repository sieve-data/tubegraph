---
title: Graphical vs algebraic approaches to finding intersections
videoId: V7H1oUHXPkg
---

From: [[khanacademy]] <br/> 

When solving a system of equations, which involves two or more equations with the same variables, there are primarily two methods to find their intersection point(s): graphical and algebraic <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This article explores both approaches, highlighting their advantages and disadvantages.

## Graphical Approach

A system of linear equations, when plotted on a graph, represents two lines <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The solution to the system is the point where these lines intersect <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. This method offers a [[visual_representation_of_equations | visual representation of equations]] and their relationship.

While equations can be put into [[graphing_equations | slope-intercept form]] or point-slope form for easier [[graphing_equations | graphing]] <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>, the main challenge with the [[graphical_interpretation_of_systems_of_equations | graphical interpretation of systems of equations]] is accurately identifying the exact intersection point by simply looking at a graph <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This limitation leads to the need for algebraic methods for precise answers <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Algebraic Approach: The Substitution Method

[[algebraic_techniques_for_solving_equations | Algebraic techniques]] provide an exact solution to systems of equations, eliminating the need to estimate from a graph <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. One common [[algebraic_techniques_for_solving_equations | algebraic technique]] is the substitution method <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

### Steps for the Substitution Method

The substitution method involves using one equation to solve for a variable and then substituting that expression into the other equation <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

1.  **Isolate a Variable**: Choose one of the equations and solve for one of the variables (e.g., solve for 'x' in terms of 'y') <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
    *   *Example:* Given the system:
        1.  `x + 2y = 9`
        2.  `3x + 5y = 20`
    *   From the first equation, subtract `2y` from both sides: `x = 9 - 2y` <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

2.  **Substitute the Expression**: Substitute the expression found in step 1 into the *other* equation for the isolated variable <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. This creates a single equation with only one unknown variable <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
    *   *Example:* Substitute `(9 - 2y)` for `x` in the second equation:
        `3(9 - 2y) + 5y = 20` <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

3.  **Solve for the Remaining Variable**: Solve the resulting equation for the single unknown variable <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
    *   *Example:*
        *   `27 - 6y + 5y = 20` <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>
        *   `27 - y = 20` <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>
        *   `-y = -7` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>
        *   `y = 7` <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>

4.  **Substitute Back to Find the Other Variable**: Use the value found in step 3 and substitute it back into the expression from step 1 to find the value of the first variable <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
    *   *Example:*
        *   `x = 9 - 2y`
        *   `x = 9 - 2(7)` <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>
        *   `x = 9 - 14` <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>
        *   `x = -5` <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>

The solution for this system is `x = -5` and `y = 7` <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. This means if the two original equations were graphed, they would intersect at the point `(-5, 7)` <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

### Application to Word Problems

Systems of equations and the substitution method are valuable for solving word problems <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

*   **Example Problem**: The sum of two numbers is 70, and they differ by 11 <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. What are the numbers?
    *   **Define Variables**: Let `x` be the larger number and `y` be the smaller number <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
    *   **Formulate Equations**:
        *   Sum: `x + y = 70` <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>
        *   Difference: `x - y = 11` <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>
    *   **Solve using Substitution**:
        1.  From `x - y = 11`, solve for `x`: `x = 11 + y` <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
        2.  Substitute `(11 + y)` into the first equation: `(11 + y) + y = 70` <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
        3.  Simplify and solve for `y`:
            *   `11 + 2y = 70` <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>
            *   `2y = 59` <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>
            *   `y = 59/2 = 29.5` <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>
        4.  Substitute `y = 29.5` back into `x = 11 + y`:
            *   `x = 11 + 29.5` <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>
            *   `x = 40.5` <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>
    *   **Solution**: The two numbers are 40.5 and 29.5 <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. (40.5 + 29.5 = 70, and 40.5 - 29.5 = 11) <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.

Regardless of which equation or variable is chosen to begin the substitution process, the important aspect is to utilize both constraints (equations) to find the solution <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. The [[comparison_with_algebraic_equations | comparison with algebraic equations]] highlights that while [[graphical_representation_and_visual_understanding_of_functions | graphical representation and visual understanding of functions]] can provide an intuitive sense of the solution, [[algebraic_techniques_for_solving_equations | algebraic techniques]] are essential for precision.