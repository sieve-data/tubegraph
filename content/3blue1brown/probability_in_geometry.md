---
title: Probability in Geometry
videoId: OkmNXy7er84
---

From: [[3blue1brown]] <br/> 

## The Putnam Mathematical Competition

The Putnam is a mathematics competition for undergraduate students, featuring a six-hour test with 12 questions split into two three-hour sessions <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Each question is scored from 1 to 10, making the highest possible score 120 <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. Despite attracting students already keen on math, the median score is typically around 1 or 2, indicating its difficulty <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Questions tend to increase in difficulty from 1 to 6 within each section <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. Often, the hardest problems (fives and sixes) have the most elegant solutions, requiring a subtle shift in perspective to become solvable <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## A Problem from the Putnam: Points on a Sphere

One such problem, which appeared as the sixth question on a Putnam test, involves [[mathematical_exercises_and_problemsolving_in_geometry | geometric reasoning]] and [[probability_and_information_measurement | probability]] <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>:

> If you choose four random points on a sphere, and consider the tetrahedron with these points as its vertices, what is the probability that the center of the sphere is inside that tetrahedron? <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>

Approaching such a problem involves considering which tetrahedra contain the sphere's center, which do not, and how to systematically distinguish between them <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

## Simplifying the Problem: Two Dimensions

A common strategy in [[challenges_in_solving_geometric_problems | problem-solving]] is to consider simpler cases <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. In this instance, the problem can be simplified to two dimensions:

> What is the probability that a triangle formed by three random points (P1, P2, P3) on a circle contains the center of the circle? <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>

This two-dimensional visualization is easier, but still challenging <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

### Fixing Points to Analyze Probability

To gain a foothold, one can fix two points, P1 and P2, and allow only the third point, P3, to vary <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. Drawing lines from P1 and P2 through the circle's center divides the circle into four arcs <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. The triangle contains the center if and only if P3 is located in the arc on the opposite side of P1 and P2 <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

Assuming all points on the circle are equally likely <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>, the [[understanding_probability_of_probabilities | probability]] that P3 lands in this specific arc is the ratio of that arc's length to the circle's full circumference <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. The size of this "relevant arc" depends on the placement of P1 and P2 <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. For example, if P1 and P2 are 90 degrees apart, the arc is one-quarter of the circle <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

Considering P1 and P2 are also chosen randomly, with every point equally likely <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>, one can fix P1 and consider all possible positions for P2. This means every angle between 0 and 180 degrees between the lines from P1 and P2 through the center is equally likely <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. Consequently, every proportion of the arc (from 0 to 0.5) is equally likely <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. The average proportion is 0.25 <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. Thus, the overall probability for the 2D case is 1/4 <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

## Extending to Three Dimensions

Attempting to extend this approach to the three-dimensional case, where three points are fixed and the fourth varies, is more complex <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. Drawing lines from the three fixed points through the sphere's center, along with planes determined by pairs of these lines, divides the sphere into eight "spherical triangles" <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. The tetrahedron will contain the sphere's center if the fourth point falls into the spherical triangle on the opposite side of the first three <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. However, calculating the average size of this section by varying the initial three points is difficult, potentially requiring surface integrals <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

## Reframing the Problem: A More Elegant Solution

The "clean" answer of 1/4 in the 2D case suggests a deeper underlying principle <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. A key insight in mathematical problem-solving is to reframe the question using constructs that simplify the problem <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

Instead of choosing three random points on a circle, consider choosing two random lines that pass through the circle's center <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. For each line, there are two possible endpoints for P1 and P2, so a coin flip can decide which endpoint corresponds to each point <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. This process is equivalent to choosing random points on the circle <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

Now, imagine P3 is chosen first, and then the two lines are set. Once the two lines and P3 are fixed, there are four equally likely outcomes for P1 and P2 based on the coin flips <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. Only one of these four outcomes places P1 and P2 on the opposite side of P3 such that the triangle contains the center <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. Therefore, regardless of the lines and P3, there is always a 1/4 chance that the coin flips result in a center-containing triangle <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

This elegant argument seamlessly generalizes to three dimensions <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. Instead of picking four random points on a sphere, imagine choosing three random lines through the sphere's center, and then a random point for P4 <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. Each of the three lines has two possible endpoints, so three coin flips decide the positions of P1, P2, and P3 <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. This yields eight equally likely outcomes from the coin flips <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. Only one of these eight outcomes will position P1, P2, and P3 on the opposite side of the center from P4, resulting in a tetrahedron that contains the center <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.

Thus, the [[geometric_reasoning_in_higher_dimensions | probability]] for the 3D case is 1/8 <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. While this solution relies on visual intuition, it can be formally articulated using linear algebra <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. The main takeaway is the problem-solving strategy: simplify the question to find a foothold, and then reframe the question around any useful added constructs <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

## Further Probability Puzzles

Another example of a [[probability_and_information_measurement | probability]] puzzle involves eight students sitting in a circle taking the Putnam <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. Each student randomly chooses one of their two neighbors to cheat from. The question asks for the expected number of students who are not being cheated off of <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. Such problems help practice [[mathematical_exercises_and_problemsolving_in_geometry | problem-solving]] abilities and illustrate various tactics in probability <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.