---
title: Interpreting and solving word problems with systems of equations
videoId: vA-55wZtLeE
---

From: [[khanacademy]] <br/> 

When faced with [[word_problems_involving_systems_of_equations | word problems]] that involve multiple unknown quantities, we can often translate them into a [[introduction_to_systems_of_equations | system of equations]] to find their solutions. This approach allows us to define variables for each unknown and then set up equations based on the information provided in the problem. The solution to the system then represents the values of the unknown quantities.

## Setting Up Equations from Word Problems

The first step in solving a [[word_problems_involving_systems_of_equations | word problem]] using a [[introduction_to_systems_of_equations | system of equations]] is to define your variables and translate the given information into algebraic equations <a class="yt-timestamp" data-t="06:30:04">[06:30:04]</a>.

### Example: Candy Store Purchase

Consider the following problem:
Nadia and Peter visit the candy store. Nadia buys 3 candy bars and 4 Fruit Roll-Ups for $2.84. Peter also buys 3 candy bars, but can only afford 1 additional Fruit Roll-Up, costing $1.79. What is the cost of each candy bar and each Fruit Roll-Up? <a class="yt-timestamp" data-t="06:07:07">[06:07:07]</a>

1.  **Define Variables**:
    *   Let `x` equal the cost of a candy bar <a class="yt-timestamp" data-t="06:33:43">[06:33:43]</a>.
    *   Let `y` equal the cost of a Fruit Roll-Up <a class="yt-timestamp" data-t="06:46:01">[06:46:01]</a>.

2.  **Translate into Equations**:
    *   **Nadia's purchase**: 3 candy bars (3x) plus 4 Fruit Roll-Ups (4y) cost $2.84 <a class="yt-timestamp" data-t="07:00:15">[07:00:15]</a>.
        Equation 1: `3x + 4y = 2.84` <a class="yt-timestamp" data-t="07:19:07">[07:19:07]</a>
    *   **Peter's purchase**: 3 candy bars (3x) plus 1 Fruit Roll-Up (1y) cost $1.79 <a class="yt-timestamp" data-t="07:29:04">[07:29:04]</a>.
        Equation 2: `3x + y = 1.79` <a class="yt-timestamp" data-t="07:40:48">[07:40:48]</a>

Now we have a [[introduction_to_systems_of_equations | system of equations]]:
1.  `3x + 4y = 2.84`
2.  `3x + y = 1.79`

## Solving Systems of Equations Using Elimination

One common method for solving [[introduction_to_systems_of_equations | systems of equations]] is [[solving_systems_of_equations_using_elimination | elimination]]. This method involves adding or subtracting the equations to eliminate one of the variables <a class="yt-timestamp" data-t="00:38:15">[00:38:15]</a>.

### The Principle of Elimination

When you have two equations, `A = B` and `C = D`, you can add or subtract them because you are essentially adding or subtracting the same value to both sides of an equation <a class="yt-timestamp" data-t="01:37:37">[01:37:37]</a>. For example, if you add `C` to the left side of `A = B` and `D` to the right side, it's valid because `C` is equal to `D` <a class="yt-timestamp" data-t="02:28:18">[02:28:18]</a>. This means `A + C = B + D`. The same logic applies to subtraction <a class="yt-timestamp" data-t="08:36:06">[08:36:06]</a>.

### Applying Elimination to the Candy Store Problem

Looking at our system:
1.  `3x + 4y = 2.84`
2.  `3x + y = 1.79`

Notice that both equations have a `3x` term. This makes them ideal for [[solving_systems_of_equations_using_elimination | elimination]] by subtraction <a class="yt-timestamp" data-t="08:22:15">[08:22:15]</a>.

1.  **Subtract the second equation from the first**:
    We can subtract `(3x + y)` from the left side of the first equation and `1.79` from the right side <a class="yt-timestamp" data-t="08:27:00">[08:27:00]</a>.
    `(3x + 4y) - (3x + y) = 2.84 - 1.79` <a class="yt-timestamp" data-t="08:48:12">[08:48:12]</a>

    *   Alternatively, imagine multiplying the second equation by -1 and then adding the two equations:
        Equation 1: `3x + 4y = 2.84`
        Equation 2 (multiplied by -1): `-3x - y = -1.79` <a class="yt-timestamp" data-t="09:23:09">[09:23:09]</a>

    *   Now, add the modified second equation to the first:
        `(3x - 3x) + (4y - y) = 2.84 - 1.79` <a class="yt-timestamp" data-t="09:45:00">[09:45:00]</a>

2.  **Solve for the remaining variable**:
    *   The `3x` terms cancel out (`3x - 3x = 0x`) <a class="yt-timestamp" data-t="09:49:55">[09:49:55]</a>.
    *   `4y - y = 3y` <a class="yt-timestamp" data-t="09:54:08">[09:54:08]</a>.
    *   `2.84 - 1.79 = 1.05` <a class="yt-timestamp" data-t="10:00:15">[10:00:15]</a>.
    *   So, `3y = 1.05` <a class="yt-timestamp" data-t="10:12:08">[10:12:08]</a>.
    *   Divide both sides by 3: `y = 1.05 / 3` <a class="yt-timestamp" data-t="10:15:28">[10:15:28]</a>.
    *   `y = 0.35` <a class="yt-timestamp" data-t="10:54:19">[10:54:19]</a>.

    This means the cost of a Fruit Roll-Up is $0.35 <a class="yt-timestamp" data-t="10:57:11">[10:57:11]</a>.

3.  **Substitute back to find the other variable**:
    Now that we have `y = 0.35`, substitute this value into either of the original equations to solve for `x` <a class="yt-timestamp" data-t="11:01:00">[11:01:00]</a>. Let's use the second equation: `3x + y = 1.79` <a class="yt-timestamp" data-t="11:12:12">[11:12:12]</a>.
    *   `3x + 0.35 = 1.79` <a class="yt-timestamp" data-t="11:22:15">[11:22:15]</a>
    *   Subtract `0.35` from both sides: `3x = 1.79 - 0.35` <a class="yt-timestamp" data-t="11:32:05">[11:32:05]</a>.
    *   `3x = 1.44` <a class="yt-timestamp" data-t="11:45:00">[11:45:00]</a>.
    *   Divide both sides by 3: `x = 1.44 / 3` <a class="yt-timestamp" data-t="11:52:00">[11:52:00]</a>.
    *   `x = 0.48` <a class="yt-timestamp" data-t="12:26:00">[12:26:00]</a>.

    This means the cost of a candy bar is $0.48 <a class="yt-timestamp" data-t="12:34:00">[12:34:00]</a>.

## Conclusion

By defining variables, translating the [[word_problems_involving_systems_of_equations | word problem]] into a [[introduction_to_systems_of_equations | system of equations]], and then using a method like [[solving_systems_of_equations_using_elimination | elimination]], we can systematically solve for the unknown quantities <a class="yt-timestamp" data-t="12:31:00">[12:31:00]</a>.

The solution to the candy store problem is:
*   **Cost of a candy bar**: $0.48 <a class="yt-timestamp" data-t="12:34:00">[12:34:00]</a>
*   **Cost of a Fruit Roll-Up**: $0.35 <a class="yt-timestamp" data-t="12:39:00">[12:39:00]</a>

You can always verify your answers by plugging these values back into the original equations to ensure they hold true <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>.