---
title: Putnam Mathematics Competition
videoId: OkmNXy7er84
---

From: [[3blue1brown]] <br/> 

The Putnam is a math competition for undergraduate students <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Format and Difficulty

The competition is a six-hour test with 12 questions, broken into two three-hour sessions <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Each question is scored from 1 to 10, making the highest possible score 120 <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. Despite participants being students already interested in math, the median score typically hovers around 1 or 2, indicating its significant difficulty <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Within each section of six questions, problems generally increase in difficulty from 1 to 6 <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. However, the hardest problems (fives and sixes) often have the most [[mathematical_insights_and_elegant_solutions | elegant solutions]] <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>, which can transform a challenging problem into a solvable one through a subtle shift in perspective <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## Problem-Solving Strategies

The focus for tackling Putnam problems is often on the [[problemsolving_strategies_in_mathematics | problem-solving process]] itself <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

### General Approach
*   **Simplify the Problem**: A good starting point is to consider simpler cases <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. This means breaking down the question into more manageable components to find a foothold <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   **Reframe the Question**: If adding a construct to the problem setup makes it conceptually easier, try to reframe the entire question in terms of these new elements <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. This technique can lead to [[mathematical_insights_and_elegant_solutions | elegant]] and subtle solutions <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

### Example: Sphere/Tetrahedron Probability

One specific problem from a Putnam test asked: If four random points are chosen on a sphere, what is the probability that the tetrahedron formed by these points contains the center of the sphere? <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>

#### Simplification to 2D
To approach this [[conceptualizing_mathematical_problems | conceptual problem]], it's helpful to simplify it to two dimensions <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. The analogous 2D problem asks: What is the probability that a triangle formed by three random points on a circle contains the circle's center? <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>

*   **Fixed Points Analysis**: If two points, P1 and P2, are fixed, and only P3 varies, a specific arc exists where P3's placement ensures the triangle contains the center <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. This arc is on the opposite side of the circle from P1 and P2, defined by lines drawn from P1 and P2 through the center <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **Average Proportion**: Assuming all points on the circle are equally likely <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>, the average size of this relevant arc, considering P1 and P2 are also chosen randomly, is one-quarter of the full circle <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. Thus, the overall probability for the 2D case is 1/4 <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

#### Reframing the 2D Problem
The "1/4" answer suggests an elegant underlying structure <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. Instead of choosing three random points:
1.  Choose two random lines that pass through the circle's center <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
2.  For each line, flip a coin to decide which of its two endpoints becomes P1 and P2 <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
3.  Choose P3 as a random point on the circle <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

With the two lines and P3 set, there are four equally likely outcomes for P1 and P2 based on the coin flips <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. Only one of these four outcomes places P1 and P2 on the opposite side of the circle as P3, resulting in a triangle containing the center <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. Therefore, the probability is always 1/4, regardless of the specific lines or P3's position <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.

#### Generalization to 3D
This reframing generalizes seamlessly to three dimensions <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
1.  Choose three random lines through the center of the sphere <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
2.  Choose a random point for P4 <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.
3.  For each of the three lines, flip a coin to decide which of its two endpoints becomes P1, P2, and P3 <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

There are eight equally likely outcomes from these coin flips <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. Only one of these outcomes places P1, P2, and P3 on the opposite side of the center as P4, forming a tetrahedron that contains the center <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. Thus, the probability is 1/8 <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. While the visual intuition is strong, a formal write-up in linear algebra can provide a non-visual proof <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

## Related Puzzles

The video presents another probability puzzle that could be encountered in a similar problem-solving context:
*   Eight students are sitting in a circle taking the Putnam <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
*   Each student randomly chooses one of their two neighbors to cheat from <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
*   What is the expected number of students who are not being cheated off of? <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>