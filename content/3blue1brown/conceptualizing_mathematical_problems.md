---
title: Conceptualizing Mathematical Problems
videoId: OkmNXy7er84
---

From: [[3blue1brown]] <br/> 

Mathematical [[problemsolving_strategies_in_mathematics | problem-solving]] often involves finding a novel way to approach a challenge, especially in complex scenarios. The Putnam competition, a notoriously difficult six-hour math test for undergraduate students, features problems that often conceal [[mathematical_insights_and_elegant_solutions | elegant solutions]] behind their apparent difficulty <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. These solutions often require a "subtle shift in perspective" to transform a very challenging problem into something doable <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This article explores an [[approaches_to_mathematical_problem_solving | approach to problem-solving]] exemplified by a specific Putnam question.

## The Core Problem

Consider the following problem, which appeared as the sixth question on a Putnam test:
"If you choose four random points on a sphere, and consider the tetrahedron with these points as its vertices, what is the probability that the center of the sphere is inside that tetrahedron?" <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

When faced with such a problem, initial questions arise: Which tetrahedra contain the center? How can they be systematically distinguished? And most importantly, how do you even begin to [[problemsolving_strategies_in_math | approach a problem]] like this <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>?

## Step 1: Simplify the Problem

A common and effective [[problemsolving_strategies_in_math | strategy]] is to consider simpler versions of the problem <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. Let's reduce the dimensions from three to two:
"What is the probability that a triangle formed by choosing three random points on a circle contains the center of the circle?" <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

### Initial 2D Approach

Visualizing the 2D case is easier, but it remains a hard question <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. One way to simplify further is to fix two points (P1, P2) and vary only the third point (P3) <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
If lines are drawn from P1 and P2 through the circle's center, they divide the circle into four arcs <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. The triangle formed will contain the center only if P3 lands in the arc opposite to P1 and P2 <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

The probability of P3 landing in this "relevant arc" is the ratio of its length to the circle's circumference <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. This proportion depends on the angular separation of P1 and P2 <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. By fixing P1 and letting P2 vary, every angle from 0 to 180 degrees (or proportion from 0 to 0.5) is equally likely <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
The average proportion of this relevant arc is 0.25 <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. Thus, the overall probability for the 2D case is 1/4 <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

Attempting to extend this "average size" calculation to the 3D case for three fixed points (P1, P2, P3) and a varying fourth point (P4) becomes significantly more difficult. The three lines from the fixed points through the center divide the sphere into eight spherical triangles <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>, and the tetrahedron contains the center only if P4 is in the opposite spherical triangle <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. Calculating the average size of this section is challenging, even with multivariable calculus <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

## Step 2: Reframe the Problem

The answer of one-fourth for the 2D case appears suspiciously clean <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. This suggests looking for a more elegant way to derive it. A key [[mathematical_insights_and_elegant_solutions | insight]] in [[problemsolving_strategies_in_mathematics | mathematical problem solving]] is to reframe the entire question around any constructs that made it conceptually easier <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

In the 2D problem, drawing lines through the center from P1 and P2 was helpful. Instead of choosing three points randomly, consider an equivalent process:
1.  Choose two random lines that pass through the circle's center <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
2.  For each line, flip a coin to decide which of its two endpoints will be P1 and P2 <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
3.  Choose a random third point, P3 <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

Crucially, imagine P3 is chosen *before* the two coin flips for P1 and P2 <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. Once the two lines and P3 are fixed, there are four equally likely outcomes for where P1 and P2 land based on the coin flips <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. Exactly one of these four outcomes places P1 and P2 on the opposite side of the circle from P3 such that the triangle contains the center <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

Therefore, regardless of where the lines and P3 are, there's always a 1/4 chance that the coin flips result in a triangle containing the center <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

## Step 3: Generalize to 3D

This reframing [[problemsolving_strategies_in_math | strategy]] generalizes seamlessly to three dimensions <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
Instead of choosing four random points, follow this process:
1.  Choose three random lines through the center of the sphere <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
2.  Choose a random fourth point, P4 <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.
3.  For each of the three lines, flip a coin to decide which of its two endpoints will be P1, P2, and P3 respectively <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

There are 2 x 2 x 2 = 8 equally likely outcomes for these three coin flips <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. Only one of these eight outcomes will place P1, P2, and P3 on the opposite side of the center from P4, resulting in a tetrahedron that contains the center <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.

Thus, the probability that the tetrahedron contains the sphere's center is 1/8 <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

## Broader Lessons for [[problemsolving_strategies_in_mathematics | Problem Solving]]

The main [[teaching_and_understanding_mathematical_concepts | takeaway]] from this problem is not just the solution, but the [[approaches_to_mathematical_problem_solving | approach]] to finding the key [[mathematical_insights_and_elegant_solutions | insight]] <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>:
*   **Simplify:** Always try to ask simpler versions of the question until you find a foothold <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
*   **Reframe:** If an added construct (like drawing lines through the center) proves useful, try to reframe the entire problem around that new construct <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

While this solution relies on visual intuition, it can be formalized using linear algebra <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. Developing the ability to articulate such insights formally is a significant part of undergraduate math education <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

### Related [[puzzles_and_geometric_problemsolving | Puzzles]]

Another example of a probability [[mathematical_exercises_and_problemsolving in geometry | puzzle]] demonstrating strategic [[problemsolving_strategies_in_math | problem-solving]] is as follows:
"Suppose you have eight students sitting in a circle taking the Putnam. It's a hard test, so each student tries to cheat off of his neighbor, choosing randomly which neighbor to cheat from. Now circle all of the students that don't have somebody cheating off of their test. What is the expected number of such circled students?" <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

Resources like Brilliant.org offer courses and questions to practice and enhance [[problemsolving_strategies_in_math | problem-solving]] abilities in various mathematical and scientific fields <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.