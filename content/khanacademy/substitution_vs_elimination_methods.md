---
title: Substitution vs elimination methods
videoId: vA-55wZtLeE
---

From: [[khanacademy]] <br/> 

Solving a system of equations involves finding the specific values for variables (e.g., *x* and *y*) that satisfy all equations in the system simultaneously <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Graphically, this represents the [[visualization_techniques_in_solving_equations | intersection]] of the lines that correspond to the solution sets of each equation <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. Two primary algebraic methods for achieving this are [[solving_linear_systems_by_substitution | substitution]] and [[elimination_method_in_algebra | elimination]].

## The Elimination Method

The core idea behind the [[elimination_method_in_algebra | elimination method]] is to [[elimination_method_in_algebra | eliminate one of the variables]] by adding or subtracting the equations in the system <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. This leaves a single equation with only one variable, which can then be easily solved <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

### Principle of Adding/Subtracting Equations

When performing [[operations_on_both_sides_of_an_equation | operations on both sides of an equation]], you must always add or subtract the same thing to both sides <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. When adding or subtracting entire equations, this principle is maintained because the quantities added to each side are themselves equal <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. For example, if you have `A = B` and `C = D`, you can add `C` to the left side of `A = B` and `D` to the right side because `C` is equal to `D` <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

### Example 1: Direct Elimination

Consider the system:
1.  `3x + 4y = 2.5` <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>
2.  `5x - 4y = 25.5` <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>

Notice the `4y` in the first equation and `-4y` in the second. If these two equations are added together, the `y` terms will cancel out <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>:

*   **Step 1: Add the equations.**
    `(3x + 4y) + (5x - 4y) = 2.5 + 25.5` <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>, <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>
    `8x + 0y = 28` <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>
    `8x = 28` <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>

*   **Step 2: Solve for the remaining variable.**
    [[dividing_both_sides_of_an_equation | Divide both sides by 8]]: `x = 28 / 8` <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>
    [[methods_for_simplifying_fractions | Simplify the fraction]]: `x = 7/2` <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>

*   **Step 3: Substitute the found value back into one of the original equations.**
    Using `3x + 4y = 2.5`:
    `3(7/2) + 4y = 2.5` (or `5/2`) <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>, <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>
    `21/2 + 4y = 5/2` <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>

*   **Step 4: Solve for the second variable.**
    Subtract `21/2` from both sides: `4y = 5/2 - 21/2` <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>
    `4y = -16/2` <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>
    `4y = -8` <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>
    [[dividing_both_sides_of_an_equation | Divide both sides by 4]]: `y = -2` <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>

The solution is `x = 7/2` and `y = -2` <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This can be verified by substituting these values into both original equations <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

### Example 2: Word Problem with Elimination

A system of equations can also be derived from word problems.
*   Nadia's purchase: `3x + 4y = $2.84` (where `x` is the cost of a candy bar and `y` is the cost of a Fruit Roll-Up) <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>
*   Peter's purchase: `3x + y = $1.79` <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>

Here, the `x` terms have the same coefficient.
*   **Step 1: Manipulate one equation to allow elimination.**
    To eliminate `3x`, subtract Peter's equation from Nadia's <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. This is equivalent to multiplying Peter's equation by -1 and then adding it to Nadia's equation <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.
    Original: `3x + 4y = 2.84`
    (Peter's equation multiplied by -1): `-3x - y = -1.79` <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>

*   **Step 2: Add the modified equations.**
    `(3x + 4y) + (-3x - y) = 2.84 + (-1.79)` <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>
    `0x + 3y = 1.05` <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>
    `3y = 1.05` <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>

*   **Step 3: Solve for the remaining variable.**
    [[dividing_both_sides_of_an_equation | Divide both sides by 3]]: `y = 1.05 / 3` <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>
    `y = $0.35` (cost of a Fruit Roll-Up) <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>

*   **Step 4: Substitute and solve for the second variable.**
    Using Peter's original equation: `3x + y = $1.79` <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>
    `3x + 0.35 = 1.79` <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>
    Subtract `0.35` from both sides: `3x = 1.79 - 0.35` <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>
    `3x = 1.44` <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>
    [[dividing_both_sides_of_an_equation | Divide both sides by 3]]: `x = 1.44 / 3` <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>
    `x = $0.48` (cost of a candy bar) <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>

## The Substitution Method

The [[solving_linear_systems_by_substitution | substitution method]] is another common approach to [[elimination_method_in_algebra | eliminate one of the variables]] in a system of equations <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. This involves solving one of the equations for a single variable and then substituting that [[expression_simplification_techniques | expression]] into the other equation. Although not detailed in the provided transcript for specific steps, it's mentioned as an alternative to elimination for solving systems <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

## Choosing a Method

Both [[solving_linear_systems_by_substitution | substitution]] and [[elimination_method_in_algebra | elimination]] are effective methods for solving systems of equations <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. The choice often depends on the specific structure of the equations. Elimination is particularly efficient when coefficients of one variable are opposites (e.g., `4y` and `-4y`) or identical (e.g., `3x` and `3x`), allowing for direct addition or subtraction to [[elimination_method_in_algebra | eliminate a variable]] <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.