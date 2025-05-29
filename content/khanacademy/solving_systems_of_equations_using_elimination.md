---
title: Solving systems of equations using elimination
videoId: vA-55wZtLeE
---

From: [[khanacademy]] <br/> 

The elimination method is a technique used to [[introduction_to_systems_of_equations | solve systems of equations]] by adding or subtracting the equations to eliminate one of the variables <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This method simplifies the system into a single equation with a single variable, which can then be solved <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## How Elimination Works

The core idea behind the [[elimination_method_in_algebra | elimination method]] is that you can add or subtract one entire equation from another, as long as you perform the same operation on both sides of the equation <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. If you have an equation like $A = B$, and another equation like $C = D$, you can add $C$ to one side and $D$ to the other, because $C$ and $D$ are equivalent values <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

By carefully choosing to add or subtract, you can make the coefficients of one variable cancel out, effectively "eliminating" that variable from the system <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. This leaves you with a simpler equation that can be solved for the remaining variable <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Example 1: Basic Application

Consider the following system of linear equations:
1.  $3x + 4y = 2.5$ <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>
2.  $5x - 4y = 25.5$ <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>

We are looking for an $x$ and $y$ value that satisfies both equations simultaneously <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Graphically, this represents the intersection point of the two lines <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

Notice that the coefficients for $y$ are $+4y$ and $-4y$. If we add these two equations together, the $y$ terms will cancel out <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

```
  3x + 4y =  2.5
+ 5x - 4y = 25.5
-----------------
  8x + 0y = 28
```

This simplifies to $8x = 28$ <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

### Solving for x
To [[solving_linear_equations | solve for x]], divide both sides by 8:
$x = \frac{28}{8}$ <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>
Simplify the fraction by dividing the numerator and denominator by 4:
$x = \frac{7}{2}$ <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>

### Solving for y
Now that we have the value of $x$, we can [[substitution_method_for_solving_linear_systems | substitute]] it back into either of the original equations to [[solving_linear_equations | solve for y]] <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. Let's use the first equation:
$3x + 4y = 2.5$
Substitute $x = \frac{7}{2}$:
$3(\frac{7}{2}) + 4y = 2.5$ <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>
$\frac{21}{2} + 4y = \frac{5}{2}$ (converting 2.5 to 5/2) <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>

Subtract $\frac{21}{2}$ from both sides:
$4y = \frac{5}{2} - \frac{21}{2}$ <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>
$4y = \frac{5 - 21}{2}$ <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>
$4y = \frac{-16}{2}$ <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>
$4y = -8$ <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>

Divide both sides by 4:
$y = \frac{-8}{4}$ <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>
$y = -2$ <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>

### Solution
The solution to the system is $x = \frac{7}{2}$ and $y = -2$ <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This means the lines intersect at the coordinate $(\frac{7}{2}, -2)$ <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

## Example 2: Word Problem Application

Let's apply the [[elimination_method_in_algebra | elimination method]] to a [[word_problems_involving_systems_of_equations | word problem]] <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

**Problem:** Nadia and Peter visit the candy store. Nadia buys 3 candy bars and 4 Fruit Roll-Ups for $2.84. Peter also buys 3 candy bars, but can only afford 1 additional Fruit Roll-Up, costing $1.79. What is the cost of each candy bar and each Fruit Roll-Up? <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>

### Defining Variables
First, define variables for the unknown quantities <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>:
*   Let $x$ = cost of one candy bar <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>
*   Let $y$ = cost of one Fruit Roll-Up <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>

### Forming Equations
Translate the information into a system of equations:
1.  **Nadia's purchase**: 3 candy bars ($3x$) + 4 Fruit Roll-Ups ($4y$) = $2.84
    $3x + 4y = 2.84$ <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>
2.  **Peter's purchase**: 3 candy bars ($3x$) + 1 Fruit Roll-Up ($1y$) = $1.79
    $3x + y = 1.79$ <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>

### Solving by Elimination
Notice that both equations have $3x$. We can eliminate the $x$ variable by subtracting the second equation from the first <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. Subtracting the second equation is equivalent to multiplying the second equation by -1 and then adding it to the first <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.

Let's write the second equation multiplied by -1:
$-(3x + y) = -(1.79)$
$-3x - y = -1.79$ <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>

Now, add this modified second equation to the first equation:
```
  3x + 4y =  2.84
+ -3x -  y = -1.79
-----------------
  0x + 3y =  1.05
```
This simplifies to $3y = 1.05$ <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

### Solving for y (Cost of Fruit Roll-Up)
Divide both sides by 3:
$y = \frac{1.05}{3}$ <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>
$y = 0.35$ <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>
So, the cost of a Fruit Roll-Up is $0.35 <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

### Solving for x (Cost of Candy Bar)
Substitute $y = 0.35$ back into either original equation. Let's use Peter's equation ($3x + y = 1.79$) as it's simpler <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>:
$3x + 0.35 = 1.79$ <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>

Subtract $0.35$ from both sides:
$3x = 1.79 - 0.35$ <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>
$3x = 1.44$ <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>

Divide both sides by 3:
$x = \frac{1.44}{3}$ <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>
$x = 0.48$ <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>

### Conclusion
The cost of a candy bar is $0.48, and the cost of a Fruit Roll-Up is $0.35 <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.