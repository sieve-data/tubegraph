---
title: Problemsolving strategies in mathematics
videoId: OkmNXy7er84
---

From: [[3blue1brown]] <br/> 
The Putnam is a math competition for undergraduate students, consisting of a six-hour test with 12 questions, each scored from 1 to 10 for a maximum possible score of 120 <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Despite attracting students already interested in mathematics, the median score is typically around 1 or 2, indicating its significant difficulty <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Problems usually increase in difficulty from 1 to 6 within each section <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

Often, the hardest problems on the Putnam (like questions five and six) are those with the most elegant solutions, requiring a subtle shift in perspective to transform a challenging problem into a solvable one <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. The focus is on the [[problem_solving_strategies_in_mathematics | problem-solving process]] and where the insight for a solution comes from, rather than just presenting the solution itself <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### General Approach to [[problem_solving_strategies_in_mathematics | Problem Solving]]

When faced with a difficult math problem, such as determining the probability that the center of a sphere lies within a tetrahedron formed by four random points on its surface, a structured approach is beneficial <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

#### Simplifying the Problem
A common and effective strategy is to consider [[problem_solving_strategies_in_mathematics | simpler cases]] <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. For example, to understand the 3D sphere problem, one can reduce it to two dimensions: choosing three random points on a circle and determining the probability that the triangle formed by these points contains the center of the circle <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

Further simplification within the 2D case might involve fixing two points (P1 and P2) and varying only the third (P3) <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. This allows for the identification of a specific arc where P3 must land for the triangle to contain the center <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. By drawing lines from P1 and P2 through the center, the circle is divided into four arcs, with only one arc on the opposite side of P1 and P2 allowing the triangle to contain the center <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. Analyzing the average size of this arc (a quarter of the circle) leads to the conclusion that the probability for the 2D case is one-fourth <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

#### Reframing the Question
If a particular element added to the problem setup makes it conceptually easier, consider [[problem_solving_strategies_in_mathematics | reframing the entire question]] in terms of those new elements <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. For the 2D problem, instead of choosing three random points, consider choosing two random lines that pass through the circle's center <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. For each line, a coin flip determines which of its two endpoints becomes P1 and P2 <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. The third point, P3, is chosen randomly on the circle <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

With the two lines and P3 fixed, there are four equally likely outcomes for P1 and P2 based on the coin flips <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. Only one of these four outcomes places P1 and P2 on the opposite side of the circle from P3, ensuring the triangle contains the center <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. This reframing demonstrates that the probability is always one-fourth, regardless of the initial points <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. This method generalizes seamlessly to three dimensions <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

For the 3D problem, one can imagine choosing three random lines through the sphere's center and a random fourth point P4 <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. Coin flips decide which of the two endpoints of each line become P1, P2, and P3 <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. There are eight equally likely outcomes from these coin flips <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. Only one of these outcomes places P1, P2, and P3 on the opposite side of the center as P4, resulting in a tetrahedron that contains the center <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. This yields a probability of one-eighth <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

#### Role of Visual Intuition and Rigor
While a solution derived through visual intuition and clever reframing can be valid, formal mathematical rigor often requires translating these insights into a more abstract language, such as linear algebra <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. The ability to find a key insight and the background to formally articulate it are distinct skills that undergraduate math students develop <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

### Key Takeaways for [[problem_solving_strategies_in_mathematics | Problem Solving]]
The primary lesson is not just the solution itself, but the method to discover such insights <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. This involves:
*   Continuously asking simpler versions of the question until a foothold is found <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
*   If any added construct or simplification proves useful, reframe the entire problem around that new construct <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.