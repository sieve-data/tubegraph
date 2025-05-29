---
title: Applying elimination method to realworld scenarios
videoId: vA-55wZtLeE
---

From: [[khanacademy]] <br/> 

The [[elimination_method_in_algebra | elimination method]] is a powerful technique used for [[solving_systems_of_equations_using_elimination | solving systems of equations]] by eliminating one of the variables to simplify the system into a single equation with a single unknown <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This method is particularly useful when variables in the equations have coefficients that are either the same or additive inverses.

## How the Elimination Method Works

Consider the following system of linear equations:
> 3x + 4y = 2.5 <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>
> 5x - 4y = 25.5 <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>

The goal is to find an 'x' and 'y' value that satisfies both equations simultaneously <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Graphically, this solution represents the intersection point of the two lines <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

The core idea of the [[elimination_method_in_algebra | elimination method]] is to add or subtract the equations in such a way that one of the variables cancels out <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

### The Principle of Adding Equations

When adding two equations, you are essentially adding equal quantities to both sides of an existing equation <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. If `5x - 4y` is known to be equal to `25.5` from the second equation, then adding `5x - 4y` to the left side of the first equation and `25.5` to its right side is valid because `5x - 4y` and `25.5` are the same quantity <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

### Solving the System

Given the system:
```
  3x + 4y = 2.5
+ 5x - 4y = 25.5
-----------------
```
Adding the two equations vertically:
*   `3x + 5x = 8x` <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>
*   `4y + (-4y) = 0y` (the 'y' terms cancel out) <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>
*   `2.5 + 25.5 = 28` <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>

This results in a single equation with one variable:
> 8x = 28 <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>

Dividing both sides by 8, we find:
> x = 28 / 8 = 7 / 2 <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>

Now, substitute the value of x (7/2) back into either of the original equations to solve for y <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. Using the first equation:
> 3(7/2) + 4y = 2.5 (or 5/2) <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>
> 21/2 + 4y = 5/2 <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>

Subtract 21/2 from both sides:
> 4y = 5/2 - 21/2 <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>
> 4y = -16/2 <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>
> 4y = -8 <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>

Divide both sides by 4:
> y = -2 <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>

Thus, the solution to the system is x = 7/2 and y = -2 <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This solution can be verified by substituting these values into the original equations <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

## Real-World Application: Candy Store Problem

The [[elimination_method_in_algebra | elimination method]] can be effectively applied to [[word_problems_involving_systems_of_equations | word problems involving systems of equations]] <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

### Problem Statement

Nadia buys 3 candy bars and 4 Fruit Roll-Ups for $2.84. Peter buys 3 candy bars and 1 Fruit Roll-Up for $1.79. What is the cost of each candy bar and each Fruit Roll-Up? <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>

### Formulating the Equations

First, define variables:
*   Let `x` be the cost of a candy bar <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   Let `y` be the cost of a Fruit Roll-Up <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

From Nadia's purchase:
> 3x + 4y = 2.84 <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>

From Peter's purchase:
> 3x + y = 1.79 <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>

### Solving Using Elimination

Notice that both equations have `3x`. This makes them ideal for elimination through subtraction <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. Subtracting the second equation from the first means subtracting `(3x + y)` from the left side and `1.79` from the right side. Since `3x + y` is equal to `1.79`, you are subtracting the same value from both sides, which is a valid algebraic operation <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.

Alternatively, you can multiply the second equation by -1 and then add it to the first equation:
```
  3x + 4y = 2.84
- (3x +  y = 1.79)
-----------------
```
This is equivalent to:
```
  3x + 4y =  2.84
- 3x -  y = -1.79
-----------------
```
Performing the subtraction (or addition with the negative second equation):
*   `3x - 3x = 0x` (the 'x' terms cancel out) <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>
*   `4y - y = 3y` <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>
*   `2.84 - 1.79 = 1.05` <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>

This results in:
> 3y = 1.05 <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>

Divide both sides by 3:
> y = 1.05 / 3 = 0.35 <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>

So, the cost of a Fruit Roll-Up is $0.35 <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

Now, [[example_problems_using_substitution_method | substitute]] `y = 0.35` back into one of the original equations to find `x` <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. Using Peter's equation (`3x + y = 1.79`):
> 3x + 0.35 = 1.79 <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>

Subtract 0.35 from both sides:
> 3x = 1.79 - 0.35 <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>
> 3x = 1.44 <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>

Divide both sides by 3:
> x = 1.44 / 3 = 0.48 <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>

Therefore, the cost of a candy bar is $0.48, and the cost of a Fruit Roll-Up is $0.35 <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. This demonstrates the practical application of the [[elimination_method_in_algebra | elimination method]] in solving everyday problems.