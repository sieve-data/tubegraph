---
title: Elimination method in algebra
videoId: vA-55wZtLeE
---

From: [[khanacademy]] <br/> 

The [[solving_systems_of_equations_using_elimination | elimination method]] is a technique used to [[solving_systems_of_equations_using_elimination | solve systems of equations]] by removing one of the variables <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This approach aims to simplify a system of two equations with two variables into a single equation with one variable, making it solvable <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Graphically, the solution to a system of equations represents the intersection point of the lines that correspond to each equation's solution set <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Principle of Elimination

The core idea of the [[solving_systems_of_equations_using_elimination | elimination method]] is to [[solving_systems_of_equations_using_elimination | eliminate one of the variables]] by either adding or subtracting the equations <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This is based on the algebraic principle that if you [[understanding_equality_in_algebra | add or subtract the same thing to both sides]] of an equation, the equation remains true <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

Consider a system of equations where `Ax + By = C` <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. If you add `D` to both sides, you get `Ax + By + D = C + D`, maintaining equality <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. In the context of systems, if you have two equations, say:
1.  `3x + 4y = 2.5` <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>
2.  `5x - 4y = 25.5` <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>

You can add the left-hand side of the second equation to the left-hand side of the first, and the right-hand side of the second equation to the right-hand side of the first <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. This is valid because `5x - 4y` is known to be equal to `25.5` <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Therefore, you are effectively [[understanding_equality_in_algebra | adding the same quantity to both sides]] of the first equation <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

## Example 1: Solving a System of Linear Equations

Let's [[solving_systems_of_equations_using_elimination | solve the system of equations]] mentioned above:
1.  `3x + 4y = 2.5` <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>
2.  `5x - 4y = 25.5` <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>

### Step 1: Eliminate a Variable
Notice the `+4y` in the first equation and `-4y` in the second <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. If these equations are added together, the `y` terms will cancel out <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

```
  3x + 4y = 2.5
+ 5x - 4y = 25.5
-----------------
  8x + 0y = 28
```
This simplifies to `8x = 28` <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

### Step 2: Solve for the Remaining Variable
Divide both sides by 8:
`x = 28 / 8` <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>
Simplify the fraction by dividing numerator and denominator by 4:
`x = 7 / 2` <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>

### Step 3: Solve for the Eliminated Variable using Substitution
[[Using substitution to verify algebraic solutions | Substitute]] the value of `x` (7/2) into either of the original equations to solve for `y` <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. Using the first equation:
`3(7/2) + 4y = 2.5` <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>
`21/2 + 4y = 5/2` (since 2.5 is 5/2) <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>
Subtract `21/2` from both sides:
`4y = 5/2 - 21/2` <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>
`4y = -16/2` <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>
`4y = -8` <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>
Divide both sides by 4:
`y = -2` <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>

The solution is `x = 7/2` and `y = -2` <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This represents the coordinate of the intersection point of the two lines <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

### Step 4: Verify the Solution
Check if the solution satisfies the second original equation:
`5x - 4y = 25.5` <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
`5(7/2) - 4(-2)` <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>
`35/2 - (-8)` <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>
`17.5 + 8 = 25.5` <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>
The solution satisfies both equations <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

## Example 2: Real-World Application (Word Problem)

The [[applying_elimination_method_to_realworld_scenarios | elimination method]] can be applied to solve word problems that translate into systems of equations <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

### Problem Statement
Nadia buys 3 candy bars and 4 Fruit Roll-Ups for $2.84. Peter buys 3 candy bars and 1 Fruit Roll-Up for $1.79. What is the cost of each candy bar and each Fruit Roll-Up? <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>

### Step 1: Define Variables
Let `x` = cost of a candy bar <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>
Let `y` = cost of a Fruit Roll-Up <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>

### Step 2: Formulate the System of Equations
*   Nadia's purchase: `3x + 4y = 2.84` <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>
*   Peter's purchase: `3x + 1y = 1.79` <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>

### Step 3: Eliminate a Variable (by Subtraction)
In this system, both equations have `3x` <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>. To [[solving_systems_of_equations_using_elimination | eliminate the 'x' term]], subtract the second equation from the first. This is equivalent to multiplying the second equation by -1 and then adding them <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>:

Original equations:
1.  `3x + 4y = 2.84`
2.  `3x + y = 1.79`

Multiply the second equation by -1:
`-(3x + y) = -(1.79)`
`-3x - y = -1.79` <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>

Now, add the modified second equation to the first:
```
  3x + 4y = 2.84
+ -3x - y = -1.79
-----------------
  0x + 3y = 1.05
```
This simplifies to `3y = 1.05` <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

### Step 4: Solve for the Remaining Variable
Divide both sides by 3:
`y = 1.05 / 3` <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>
`y = 0.35` <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>
So, the cost of a Fruit Roll-Up is $0.35 <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

### Step 5: Solve for the Eliminated Variable using Substitution
[[Using substitution to verify algebraic solutions | Substitute]] `y = 0.35` into Peter's original equation (`3x + y = 1.79`) <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>:
`3x + 0.35 = 1.79` <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>
Subtract 0.35 from both sides:
`3x = 1.79 - 0.35` <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>
`3x = 1.44` <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>
Divide both sides by 3:
`x = 1.44 / 3`
`x = 0.48` <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>
So, the cost of a candy bar is $0.48 <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.

### Conclusion
Using the [[solving_systems_of_equations_using_elimination | elimination method]], it's determined that the cost of a candy bar is $0.48 and the cost of a Fruit Roll-Up is $0.35 <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.