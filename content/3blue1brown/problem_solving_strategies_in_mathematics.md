---
title: Problem solving strategies in mathematics
videoId: YtkIWDE36qU
---

From: [[3blue1brown]] <br/> 

Moser's circle problem, a famous cautionary tale in mathematics, serves as an excellent exercise in [[problemsolving_strategies_in_mathematics | problem solving]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, providing valuable insights into effective strategies. The problem involves placing *n* points on a circle, connecting them with all possible chords, and counting the number of regions the circle is divided into <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>. While the initial results (2, 4, 8, 16 regions for 2, 3, 4, 5 points respectively) suggest a pattern of powers of two, this sequence breaks at six points, yielding 31 regions instead of 32 <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>, <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>, <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>, <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>, <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>. This phenomenon is an example of what mathematician Richard Guy called the "strong law of small numbers," stating "there aren't enough small numbers to meet the many demands made of them" <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>, <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.

Understanding the true pattern behind this problem reveals several powerful [[problemsolving_strategies_in_mathematics | mathematical problemsolving strategies]].

## Solving Easier, Related Questions

When faced with a complex problem, a fundamental [[problemsolving_strategies_in_mathematics | problem solving strategy]] is to [[problemsolving_strategies_in_mathematics | try solving easier questions somehow related to the problem at hand]] <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>. This approach helps gain a foothold and can provide answers directly applicable to the main problem <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.

In the case of Moser's circle problem, two helpful warm-up questions are:
1.  How many total chords are there in the diagram? <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>
2.  At how many points within the circle do those chords intersect each other? <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>

### Counting Chords

Each chord uniquely corresponds to a pair of points on the circle <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>. Therefore, the problem reduces to counting the number of distinct pairs of points. This is given by the combination formula "n choose two" (C(n, 2) or $\binom{n}{2}$) <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>. This formula calculates the number of distinct pairs that can be chosen from a set of *n* items where order does not matter <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>.
$\binom{n}{2} = \frac{n \times (n-1)}{2}$ <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>.

### Counting Intersection Points

Counting intersection points is trickier, as not all pairs of chords intersect within the circle <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>. However, a key observation is that every intersection point is uniquely associated with a quadruplet of points on the circle's boundary <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>. For any chosen quadruplet of points, their two diagonal chords will intersect exactly once inside the circle <a class="yt-timestamp" data-t="04:37:00">[04:37:00]</a>. Thus, the number of intersection points is given by "n choose four" (C(n, 4) or $\binom{n}{4}$) <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>.
$\binom{n}{4} = \frac{n \times (n-1) \times (n-2) \times (n-3)}{4!}$ <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>.

## Applying Established Mathematical Principles

Another powerful strategy is to leverage known mathematical theorems or formulas that might apply to the problem.

### Euler's Characteristic Formula for Planar Graphs

The trick to solving the Moser's circle problem is using a fact about planar graphs <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>. In graph theory, a graph has nodes (vertices, *v*) and lines (edges, *e*), and is planar if it can be drawn without lines intersecting <a class="yt-timestamp" data-t="06:31:00">[06:31:00]</a>.

Euler's characteristic formula states that for any planar graph, the number of vertices (*v*) minus the number of edges (*e*) plus the number of regions (faces, *f*, including the infinite outer region) is always two:
$v - e + f = 2$ <a class="yt-timestamp" data-t="07:23:00">[07:23:00]</a>.

This formula can be rearranged to find the number of regions:
$f = e - v + 2$ <a class="yt-timestamp" data-t="08:51:00">[08:51:00]</a>.

For Moser's circle problem, which doesn't consider the infinite outer region, the formula becomes:
$f_{internal} = e - v + 1$ <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>, <a class="yt-timestamp" data-t="09:04:00">[09:04:00]</a>.

### Reframing the Problem for Applicability

Initially, Euler's formula might seem inapplicable because the chords in Moser's circle problem clearly intersect <a class="yt-timestamp" data-t="09:07:00">[09:07:00]</a>. However, the key is to treat this as a *new* graph where the intersection points *themselves* are considered vertices <a class="yt-timestamp" data-t="09:20:00">[09:20:00]</a>.

With this reframing:
*   **Total Vertices (*v*)**: The initial *n* points on the circle plus the $\binom{n}{4}$ intersection points inside the circle.
    $v = n + \binom{n}{4}$ <a class="yt-timestamp" data-t="09:28:00">[09:28:00]</a>.
*   **Total Edges (*e*)**: Each intersection point effectively adds two more "chopped" segments (edges) <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a>. The initial number of chords is $\binom{n}{2}$. So, the edges created by chords are $\binom{n}{2} + 2 \times \binom{n}{4}$ <a class="yt-timestamp" data-t="10:17:00">[10:17:00]</a>. Additionally, the *n* arcs on the circle's circumference also count as edges <a class="yt-timestamp" data-t="10:30:00">[10:30:00]</a>.
    $e = \binom{n}{2} + 2 \times \binom{n}{4} + n$ <a class="yt-timestamp" data-t="10:56:00">[10:56:00]</a>.

Plugging these into the modified Euler's formula ($f_{internal} = e - v + 1$):
$f_{internal} = (\binom{n}{2} + 2 \binom{n}{4} + n) - (n + \binom{n}{4}) + 1$ <a class="yt-timestamp" data-t="10:43:00">[10:43:00]</a>.
Simplifying the expression through cancellation of *n* and one $\binom{n}{4}$ term <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>, the final formula for the number of regions is:
$f_{internal} = 1 + \binom{n}{2} + \binom{n}{4}$ <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>.

## Connecting with Other Mathematical Concepts

Understanding *why* the powers of two pattern appears and then breaks requires connecting the derived formula to other mathematical concepts, specifically Pascal's Triangle.

### Pascal's Triangle and Combinations

Pascal's Triangle is constructed by summing the two terms directly above each position <a class="yt-timestamp" data-t="11:41:00">[11:41:00]</a>. Each term in the triangle corresponds to $\binom{n}{k}$, where *n* is the row index (starting from 0) and *k* is the column index (starting from 0) <a class="yt-timestamp" data-t="11:50:00">[11:50:00]</a>.

A well-known property of Pascal's Triangle is that the sum of the terms in any given row is a power of two <a class="yt-timestamp" data-t="12:31:00">[12:31:00]</a>. For example, row 0 sums to $1 = 2^0$, row 1 sums to $1+1=2=2^1$, row 2 sums to $1+2+1=4=2^2$, and so on <a class="yt-timestamp" data-t="12:35:00">[12:35:00]</a>. This occurs because each number in a row "donates" two copies of itself to the next row, causing the total to double with each iteration <a class="yt-timestamp" data-t="13:16:00">[13:16:00]</a>.

### Explaining the Pattern Break

The formula for the number of regions in Moser's circle problem is $1 + \binom{n}{2} + \binom{n}{4}$ <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>. This can be rewritten using combinations as $\binom{n}{0} + \binom{n}{2} + \binom{n}{4}$ <a class="yt-timestamp" data-t="13:37:00">[13:37:00]</a>.

For $n \le 5$, the formula $\binom{n}{0} + \binom{n}{2} + \binom{n}{4}$ includes *all* the non-zero terms in the even positions of row *n* of Pascal's Triangle. Furthermore, due to the structure and symmetry of Pascal's triangle, this sum corresponds to adding up a portion of the *previous* row. Specifically, for $n \le 5$, this sum equals the sum of the *entire* previous row, which is always a power of two <a class="yt-timestamp" data-t="13:51:00">[13:51:00]</a>, <a class="yt-timestamp" data-t="14:05:00">[14:05:00]</a>, <a class="yt-timestamp" data-t="14:11:00">[14:11:00]</a>.

However, when $n=6$, the formula becomes $\binom{6}{0} + \binom{6}{2} + \binom{6}{4} = 1 + 15 + 15 = 31$ <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>. In Pascal's Triangle, row 6 contains terms up to $\binom{6}{6}$. The sum $\binom{6}{0} + \binom{6}{2} + \binom{6}{4}$ does not include $\binom{6}{6}$. Because $\binom{6}{6}=1$, this sum falls short of the full row sum (which would be $2^6=64$) by exactly 1 ($31 \ne 32$) <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>, <a class="yt-timestamp" data-t="14:27:00">[14:27:00]</a>. This explains why the pattern of powers of two breaks at $n=6$ and why it is exactly one less than expected.

At $n=10$, the number of regions once again happens to be a power of two. This occurs because the sum $\binom{10}{0} + \binom{10}{2} + \binom{10}{4}$ represents exactly half of the sum of the 10th row of Pascal's Triangle (due to symmetry, including terms up to $\binom{10}{4}$), which results in half of a power of two, itself another power of two <a class="yt-timestamp" data-t="14:38:00">[14:38:00]</a>, <a class="yt-timestamp" data-t="14:42:00">[14:42:00]</a>, <a class="yt-timestamp" data-t="14:51:00">[14:51:00]</a>.

## Conclusion

Moser's circle problem is a powerful reminder that while initial patterns can be deceptive, a deeper understanding can be achieved through rigorous [[problemsolving_strategies_in_mathematics | mathematical problemsolving and flexibility]] <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>. By breaking down the problem into simpler components, applying established theorems like Euler's formula, reframing the problem to fit these theorems, and connecting findings to broader mathematical structures like Pascal's Triangle, a satisfying and complete explanation for the observed pattern emerges <a class="yt-timestamp" data-t="15:10:00">[15:10:00]</a>. This approach highlights that even apparent coincidences often have underlying mathematical reasons <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>, <a class="yt-timestamp" data-t="15:41:00">[15:41:00]</a>.