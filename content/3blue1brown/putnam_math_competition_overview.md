---
title: Putnam Math Competition overview
videoId: OkmNXy7er84
---

From: [[3blue1brown]] <br/> 

The Putnam Competition, officially known as the William Lowell Putnam Mathematical Competition, is an annual mathematics competition designed for undergraduate university students <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Competition Format

The competition is a six-hour long test, divided into two separate three-hour sessions <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It consists of 12 questions in total <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Each question is scored on a scale of 1 to 10, making the highest possible score 120 points <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Difficulty

The Putnam is considered a very challenging test <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. Despite being taken by students who are already significantly interested in mathematics, the median score typically hovers around 1 or 2 points <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

Within each of the two six-question sections, problems generally increase in difficulty from question 1 to question 6 <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. The most difficult problems (questions 5 and 6) often have the most elegant solutions, which become apparent with a subtle shift in perspective <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Example Problem and [[problemsolving_strategies_in_mathematics | Problem-Solving]] Insights

The video features a specific problem that appeared as the sixth question on a past Putnam exam <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

### The Problem
If you choose four random points on a sphere and consider the tetrahedron formed by these points as its vertices, what is the probability that the center of the sphere is inside that tetrahedron? <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>

### General [[problem_solving_strategies_in_mathematics | Problem-Solving Strategies]] Illustrated

The discussion of this problem highlights several key [[problemsolving_strategies_in_mathematics | problem-solving strategies]]:

*   **Simplify the Problem**: It is often helpful to consider simpler versions of a problem to gain a foothold <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. For the sphere problem, this meant reducing it to two dimensions: choosing three random points on a circle and finding the probability that the resulting triangle contains the circle's center <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
*   **Fix Variables**: In the 2D case, fixing two points (P1 and P2) and varying the third point (P3) helped reveal a "special region" where P3 must lie for the triangle to contain the center <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   **Reframing the Question**: If a new construct (like lines through the center) makes the problem conceptually easier, try to reframe the entire question in terms of these new elements <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
    *   For the 2D circle problem, instead of choosing three random points, one can choose two random lines through the circle's center and then flip coins to determine P1 and P2, with P3 chosen randomly <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. This approach elegantly yields a probability of 1/4 <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
    *   This reframing generalizes to the 3D case: choose three random lines through the sphere's center, and a random point P4 <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. Each line has two endpoints, so there are 2^3 = 8 equally likely outcomes for P1, P2, and P3 based on coin flips <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. Only one of these 8 outcomes places P1, P2, and P3 on the opposite side of the center from P4, resulting in a tetrahedron that contains the center <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. Thus, the probability for the 3D problem is 1/8 <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

*   **Formal Articulation**: While key insights can be found through intuition, formally articulating the solution often requires a strong background in areas like [[overview_of_upcoming_series_on_linear_algebra | linear algebra]] <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. This distinction between finding an insight and formally proving it is a significant part of an undergraduate math student's development <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.