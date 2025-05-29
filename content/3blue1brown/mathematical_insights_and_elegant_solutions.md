---
title: Mathematical Insights and Elegant Solutions
videoId: OkmNXy7er84
---

From: [[3blue1brown]] <br/> 

The pursuit of mathematical insights often leads to elegant solutions, particularly evident in challenging competitions like the [[Putnam Competition]]. These solutions frequently arise from a subtle shift in perspective, transforming a complex problem into a solvable one <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. The focus in [[teaching_and_understanding_mathematical_concepts | understanding mathematical concepts]] and [[conceptualizing_mathematical_problems | conceptualizing mathematical problems]] is less on the direct answer and more on the [[ProblemSolving Strategies in Mathematics | problem-solving process]] itself <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## The Putnam Competition

The Putnam is a mathematics competition designed for undergraduate students <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. It consists of a six-hour test with only 12 questions, divided into two three-hour sessions <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Each question is scored from 1 to 10, making a perfect score 120 <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. Despite attracting students already keen on mathematics, the median score typically hovers around 1 or 2, underscoring its difficulty <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Problems usually escalate in difficulty from question 1 to 6 within each section <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. Often, the seemingly hardest problems (questions five and six) are the ones that yield the most elegant solutions <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Approaches to Mathematical Problem Solving

A common strategy for tackling difficult mathematical problems, especially those that appear [[paradoxical_and_nonintuitive_mathematical_truths | nonintuitive]], is to start with [[problemsolving_strategies_in_math | simpler versions of the question]] to gain a foothold <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>, <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

### Example: Probability of a Center-Containing Polygon

Consider a problem from the Putnam competition:
"If you choose four random points on a sphere, and consider the tetrahedron with these points as its vertices, what is the probability that the center of the sphere is inside that tetrahedron?" <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>

#### Simplifying to Two Dimensions

To approach this [[mathematical_exercises_and_problemsolving_in_geometry | geometry problem]], one might first simplify it to two dimensions <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>:
"What's the probability that a triangle formed by three random points on a circle contains the center of the circle?" <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>

This simplified scenario is easier to visualize but remains challenging <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

#### Fixing Variables and Identifying Special Regions

A useful [[problemsolving_strategies_in_math | strategy]] is to fix some variables. If P1 and P2 are fixed on the circle, and only P3 varies, a "special region" or arc emerges <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. The triangle contains the center only if P3 lies within a specific arc <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. This arc is defined by drawing lines from P1 and P2 through the circle's center; P3 must be in the arc on the opposite side of P1 and P2 <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

Assuming all points on the circle are equally likely, the probability of P3 landing in this arc is its length divided by the circle's circumference <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. The average size of this relevant arc, considering P1 and P2 are chosen randomly, is one quarter of the full circle <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. This leads to an overall probability of one-fourth for the triangle containing the center <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

#### Reframing the Problem

The elegant and "clean" answer of one-fourth suggests a deeper insight <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. A key [[approaches_to_mathematical_problem_solving | lesson]] in [[problemsolving_strategies_in_math | mathematical problem solving]] is to reframe the entire question around any constructs that simplify the problem conceptually <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

Instead of choosing three random points, imagine choosing two random lines that pass through the circle's center <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. For each line, flip a coin to decide which of its two endpoints will be P1 and P2 <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. Then, consider P3 as a random point chosen *before* these coin flips <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

With the two lines and P3 fixed, there are four equally likely possibilities for P1 and P2 based on the coin flips <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. Crucially, only one of these four outcomes places P1 and P2 on the opposite side of P3 such that the triangle contains the center <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. Thus, regardless of the initial positions, there is always a 1/4 chance the triangle contains the center <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

#### Extending to Three Dimensions

This reframing strategy generalizes seamlessly to three dimensions <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. Instead of picking four random points, choose three random lines through the sphere's center and a random point P4 <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. For each of the three lines, flip a coin to determine which of its two endpoints becomes P1, P2, and P3 <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

There are eight equally likely outcomes from these coin flips (2^3 = 8) <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. Only one of these eight outcomes will position P1, P2, and P3 on the opposite side of the center relative to P4, resulting in a tetrahedron that contains the center <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. Therefore, the probability is 1/8 <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

## Intuition Versus Formal Proof

While this solution, based on [[mathematical_intuition_versus_analysis | visual intuition]] and reframing, is elegant and valid <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>, formalizing it for [[mathematical proofs and logical deduction | rigorous proof]] often requires a different set of skills, such as linear algebra <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. The ability to grasp the key insight is distinct from the ability to articulate it formally, a skill undergraduate math students actively develop <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

## Key Takeaways

The primary lesson from such problems is not just the specific solution, but the [[problemsolving_strategies in math | method of discovery]] <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. This involves:
*   Consistently asking for simpler versions of the problem until a foothold is established <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
*   If any new constructs or simplifications prove useful, reframing the entire question around them <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.