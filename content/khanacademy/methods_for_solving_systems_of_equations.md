---
title: Methods for solving systems of equations
videoId: vA-55wZtLeE
---

From: [[khanacademy]] <br/> 

[[Understanding systems of equations | Solving systems of equations]] involves finding the values for variables that satisfy all equations in the system simultaneously <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Graphically, this represents the intersection point of the lines (or planes, etc.) that represent the solution sets for each individual equation <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. While methods like [[solving_linear_systems_with_substitution | substitution]] and [[graphical_interpretation_of_systems_of_equations | graphing]] can be used <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>, the elimination method offers an alternative [[systematic_approach_to_solving_equations | systematic approach]] <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

## Elimination Method

The core idea behind the elimination method is to add or subtract equations in a way that eliminates one of the variables, leaving a single equation with a single variable that can then be solved <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

### Justification for Adding/Subtracting Equations
When performing operations on an equation, any change made to one side must also be made to the other side to maintain equality <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. For example, if you add 'D' to the left side of `Ax + By = C`, you must also add 'D' to the right side <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

When adding or subtracting two equations, for example:
Equation 1: `3x + 4y = 2.5`
Equation 2: `5x - 4y = 25.5`

You are essentially adding the left side of Equation 2 (`5x - 4y`) to the left side of Equation 1, and the right side of Equation 2 (`25.5`) to the right side of Equation 1 <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. This is permissible because, according to Equation 2, the expression `5x - 4y` is *equal* to `25.5` <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Therefore, you are adding the same quantity to both sides of Equation 1, preserving its equality <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

### Example 1: Direct Elimination by Addition
Consider the system:
1.  `3x + 4y = 2.5` <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>
2.  `5x - 4y = 25.5` <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>

Notice the `4y` and `-4y` terms <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. If you add these two equations together, the `y` terms will cancel out <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

*   Add the left-hand sides: `(3x + 4y) + (5x - 4y) = 8x + 0y = 8x` <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>
*   Add the right-hand sides: `2.5 + 25.5 = 28` <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>

This results in the equation: `8x = 28` <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

Now, [[solving_simple_linear_equations | solve for x]]:
*   `x = 28 / 8` <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>
*   `x = 7/2` <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>

Next, [[solving_linear_systems_with_substitution | substitute]] this value of `x` back into either of the original equations to [[solving_algebraic_equations | solve for y]] <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. Using the first equation:
*   `3 * (7/2) + 4y = 2.5` <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a> (or `5/2` as a fraction <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>)
*   `21/2 + 4y = 5/2` <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>
*   Subtract `21/2` from both sides: `4y = 5/2 - 21/2` <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>
*   `4y = -16/2` <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>
*   `4y = -8` <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>
*   Divide by 4: `y = -2` <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>

The solution is `x = 7/2` and `y = -2` <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This can be verified by substituting these values into the second original equation <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

### Example 2: Elimination in a Word Problem
Consider a problem where Nadia buys 3 candy bars and 4 Fruit Roll-Ups for $2.84, and Peter buys 3 candy bars and 1 Fruit Roll-Up for $1.79 <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. The goal is to find the cost of each item <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.

Let `x` be the cost of a candy bar and `y` be the cost of a Fruit Roll-Up <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
The problem translates to the system of equations:
1.  `3x + 4y = 2.84` (Nadia's purchase) <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>
2.  `3x + y = 1.79` (Peter's purchase) <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>

Notice that both equations have a `3x` term <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. By subtracting the second equation from the first, the `x` terms will be eliminated <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
Subtracting `3x + y` from `3x + 4y` on the left side, and `1.79` from `2.84` on the right side:
*   `(3x + 4y) - (3x + y) = 3x + 4y - 3x - y = 0x + 3y = 3y` <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>
*   `2.84 - 1.79 = 1.05` <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>

This leaves: `3y = 1.05` <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.

Now, [[solving_simple_linear_equations | solve for y]]:
*   `y = 1.05 / 3` <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>
*   `y = 0.35` <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>

So, the cost of a Fruit Roll-Up is $0.35 <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

Finally, [[solving_linear_systems_with_substitution | substitute]] `y = 0.35` into the second original equation (`3x + y = 1.79`) to [[solving_algebraic_equations | solve for x]] <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>:
*   `3x + 0.35 = 1.79` <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>
*   Subtract `0.35` from both sides: `3x = 1.79 - 0.35` <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>
*   `3x = 1.44` <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>
*   Divide by 3: `x = 1.44 / 3` <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>
*   `x = 0.48` <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>

Therefore, the cost of a candy bar is $0.48, and the cost of a Fruit Roll-Up is $0.35 <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.

---
### Other relevant methods
*   [[solving_linear_systems_with_substitution | Substitution]] <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>
*   [[graphical_interpretation_of_systems_of_equations | Graphing]] <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>