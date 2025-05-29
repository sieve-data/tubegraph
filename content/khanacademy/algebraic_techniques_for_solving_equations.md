---
title: Algebraic techniques for solving equations
videoId: V7H1oUHXPkg
---

From: [[khanacademy]] <br/> 

While [[understanding_systems_of_equations | systems of equations]] can sometimes be solved by graphing lines to find their intersection point <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, this method often makes it difficult to pinpoint the exact intersection <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>, <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. [[Systematic approach to solving equations | Algebraic techniques]] offer a precise way to find solutions without relying on visual graphs <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>, <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## The Substitution Method

The substitution method is an [[methods_for_solving_systems_of_equations | algebraic technique]] for [[solving_algebraic_equations | solving systems of equations]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>, <a class="yt-timestamp" data-t="00:56:00">[00:56:00]</a>. This method involves:
1.  Using one equation to [[isolating_variables_in_algebraic_equations | solve for one variable]] <a class="yt-timestamp" data-t="00:59:00">[00:59:00]</a>.
2.  Substituting that [[understanding_algebraic_expressions | expression]] for the variable into the other equation <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>.
3.  Solving the resulting single-variable equation <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.
4.  Substituting the found value back into one of the original (or rearranged) equations to find the value of the other variable <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>.

### Example 1: Solving a System of Linear Equations

Consider the following [[understanding_relationships_and_equations_in_algebra | system of equations]]:
*   Equation 1: `x + 2y = 9` <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>
*   Equation 2: `3x + 5y = 20` <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>

#### Step-by-Step Solution:

1.  **Solve for one variable in one equation**:
    From Equation 1, [[isolating_variables_in_algebraic_equations | isolate x]]:
    `x + 2y = 9` <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>
    Subtract `2y` from both sides:
    `x = 9 - 2y` <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>

2.  **Substitute into the other equation**:
    Substitute `(9 - 2y)` for `x` in Equation 2:
    `3(9 - 2y) + 5y = 20` <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>

3.  **Solve the resulting single-variable equation**:
    *   Distribute the 3: `27 - 6y + 5y = 20` <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>
    *   Combine `y` terms: `27 - y = 20` <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>
    *   Subtract 27 from both sides: `-y = -7` <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>
    *   Multiply by -1: `y = 7` <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>

4.  **Substitute back to find the other variable**:
    Now that `y = 7`, substitute it back into the expression for `x`:
    `x = 9 - 2(7)` <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>
    `x = 9 - 14` <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>
    `x = -5` <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>

The solution to the system is `x = -5` and `y = 7` <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>.

#### [[Checking solutions in algebra | Checking the Solution]]:
*   For `x + 2y = 9`: `-5 + 2(7) = -5 + 14 = 9` (Correct) <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>
*   For `3x + 5y = 20`: `3(-5) + 5(7) = -15 + 35 = 20` (Correct) <a class="yt-timestamp" data-t="04:12:00">[04:12:00]</a>

### Example 2: Application to a Word Problem

Word problems can be translated into [[understanding_relationships_and_equations_in_algebra | systems of equations]] and solved algebraically <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a>.

**Problem**: The sum of two numbers is 70. They differ by 11. What are the numbers? <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>

#### Step-by-Step Solution:

1.  **Define variables**:
    Let `x` be the larger number and `y` be the smaller number <a class="yt-timestamp" data-t="05:18:00">[05:18:00]</a>.

2.  **Formulate equations**:
    *   "The sum of two numbers is 70": `x + y = 70` <a class="yt-timestamp" data-t="05:44:00">[05:44:00]</a>
    *   "They differ by 11": `x - y = 11` <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>

3.  **Solve for one variable in one equation**:
    From the second equation (`x - y = 11`), [[isolating_variables_in_algebraic_equations | isolate x]]:
    Add `y` to both sides: `x = 11 + y` <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>

4.  **Substitute into the other equation**:
    Substitute `(11 + y)` for `x` in the first equation (`x + y = 70`):
    `(11 + y) + y = 70` <a class="yt-timestamp" data-t="07:04:00">[07:04:00]</a>

5.  **Solve the resulting single-variable equation**:
    *   Combine `y` terms: `11 + 2y = 70` <a class="yt-timestamp" data-t="07:32:00">[07:32:00]</a>
    *   Subtract 11 from both sides: `2y = 59` <a class="yt-timestamp" data-t="07:45:00">[07:45:00]</a>
    *   Divide by 2: `y = 59/2 = 29.5` <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>

6.  **Substitute back to find the other variable**:
    Now that `y = 29.5`, substitute it back into the expression for `x`:
    `x = 11 + 29.5` <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>
    `x = 40.5` <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>

The two numbers are 40.5 and 29.5 <a class="yt-timestamp" data-t="08:36:00">[08:36:00]</a>.

#### [[Checking solutions in algebra | Checking the Solution]]:
*   **Sum**: `40.5 + 29.5 = 70` (Correct) <a class="yt-timestamp" data-t="09:07:00">[09:07:00]</a>
*   **Difference**: `40.5 - 29.5 = 11` (Correct) <a class="yt-timestamp" data-t="09:11:00">[09:11:00]</a>

The key to using the substitution method is to utilize both constraints (equations) within the [[systematic_approach_to_solving_equations | system]] <a class="yt-timestamp" data-t="08:58:00">[08:58:00]</a>.