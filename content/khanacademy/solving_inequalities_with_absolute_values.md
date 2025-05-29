---
title: Solving inequalities with absolute values
videoId: iI_2Piwn_og
---

From: [[khanacademy]] <br/> 

Solving [[absolute_value_inequalities | inequalities that also have absolute values]] can often be confusing, but understanding the true meaning of [[understanding_absolute_value | absolute value]] simplifies the process <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Understanding Absolute Value <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>
The [[understanding_absolute_value | absolute value]] of a number signifies its distance from 0 on a number line <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. For instance, the expression "$|x| < 12$" translates to finding all values of 'x' that are less than 12 units away from 0 <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Case 1: Absolute Value Less Than a Number (e.g., |f(x)| < a)

When an [[absolute_value_inequalities | absolute value inequality]] states that the absolute value of an expression is *less than* a certain number, it means the expression must lie *between* the negative and positive values of that number.

> [!EXAMPLE] Problem: Solve $|x| < 12$ <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>
1.  **Interpret the meaning**: Find all 'x' values that are less than 12 units away from 0 <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
2.  **Visualize on a number line**: Numbers that are less than 12 away from 0 fall between -12 and 12 <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
    *   This includes numbers like -6 (absolute value 6) <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a> and -11 (absolute value 11) <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
3.  **Translate to a [[compound_inequalities | compound inequality]]**: This means x must be greater than -12 AND less than 12 <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
    *   Written as: $-12 < x < 12$ <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

> [!INFO] General Rule for $|f(x)| < a$ <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>
If you have an [[absolute_value_inequalities | inequality]] of the form $|f(x)| < a$, it translates to the [[compound_inequalities | compound inequality]]:
$-a < f(x) < a$ <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>

> [!EXAMPLE] Problem: Solve $|5x + 3| < 7$ <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>
1.  **Interpret**: The expression `5x + 3` must be less than 7 units away from 0 <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
2.  **Translate**: This means `5x + 3` must be greater than -7 AND less than 7 <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
    *   Written as: $-7 < 5x + 3 < 7$ <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>
3.  **[[solving_linear_equations | Solve for x]]**:
    *   Subtract 3 from all parts of the [[compound_inequalities | inequality]]:
        $-7 - 3 < 5x + 3 - 3 < 7 - 3$ <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>
        $-10 < 5x < 4$ <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>
    *   Divide all parts by 5:
        $\frac{-10}{5} < \frac{5x}{5} < \frac{4}{5}$ <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>
        $-2 < x < \frac{4}{5}$ <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>
4.  **Solution set**: All x values between -2 and 4/5 (not including -2 and 4/5) <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

## Case 2: Absolute Value Greater Than a Number (e.g., |f(x)| > a)

When an [[absolute_value_inequalities | absolute value inequality]] states that the absolute value of an expression is *greater than* a certain number, it means the expression must be *further away from zero* than that number. This typically leads to two separate [[compound_inequalities | inequalities]] connected by "or".

> [!EXAMPLE] Problem: Solve $|7x| \ge 21$ <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>
1.  **Interpret the meaning**: The expression `7x` must be 21 or more units away from 0 <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
2.  **Visualize on a number line**: Numbers that are 21 or more units away from 0 are either:
    *   Greater than or equal to positive 21 (e.g., 21, 30, etc.) <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>
    *   Less than or equal to negative 21 (e.g., -21, -30, etc.) <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>
3.  **Translate to two separate inequalities**:
    *   `7x` must be greater than or equal to 21 ($7x \ge 21$) <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>
    *   OR `7x` must be less than or equal to -21 ($7x \le -21$) <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>
4.  **[[solving_linear_equations | Solve for x]] in each inequality**:
    *   For $7x \ge 21$: Divide both sides by 7 $\rightarrow x \ge 3$ <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>
    *   For $7x \le -21$: Divide both sides by 7 $\rightarrow x \le -3$ <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>
5.  **Solution set**: $x \le -3$ OR $x \ge 3$ <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

> [!INFO] General Rule for $|f(x)| > a$ <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>
If you have an [[absolute_value_inequalities | inequality]] of the form $|f(x)| > a$, it translates to two separate [[compound_inequalities | inequalities]]:
$f(x) > a \quad \text{OR} \quad f(x) < -a$ <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>

> [!EXAMPLE] Problem: Solve $\left|\frac{2x}{7} + 9\right| > \frac{5}{7}$ <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>
1.  **Interpret**: The expression $\frac{2x}{7} + 9$ must be more than $\frac{5}{7}$ units away from 0 <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.
2.  **Translate to two separate inequalities**:
    *   $\frac{2x}{7} + 9 > \frac{5}{7}$ <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>
    *   OR $\frac{2x}{7} + 9 < -\frac{5}{7}$ <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>
3.  **[[solving_linear_equations | Solve for x]] in each inequality**:
    *   **First inequality**: $\frac{2x}{7} + 9 > \frac{5}{7}$
        *   Multiply everything by 7 to clear denominators: $2x + 63 > 5$ <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>
        *   Subtract 63 from both sides: $2x > 5 - 63 \implies 2x > -58$ <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>
        *   Divide by 2: $x > -29$ <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>
    *   **Second inequality**: $\frac{2x}{7} + 9 < -\frac{5}{7}$
        *   Multiply everything by 7: $2x + 63 < -5$ <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>
        *   Subtract 63 from both sides: $2x < -5 - 63 \implies 2x < -68$ <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>
        *   Divide by 2: $x < -34$ <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>
4.  **Solution set**: $x > -29$ OR $x < -34$ <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.

> [!TIP]
> Always visualize the problem on a number line to prevent confusion and solidify understanding rather than memorizing rules <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.