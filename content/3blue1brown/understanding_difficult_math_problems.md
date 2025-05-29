---
title: Understanding difficult math problems
videoId: OkmNXy7er84
---

From: [[3blue1brown]] <br/> 

Understanding difficult mathematics problems, particularly those found in competitions like the Putnam, often requires a focus on [[mathematical_problemsolving_and_flexibility | problem-solving strategies]] rather than just memorizing solutions <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. The hardest problems frequently possess the most elegant solutions, discoverable through a "subtle shift in perspective" <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## The Putnam Competition

The Putnam is a highly challenging mathematics competition for undergraduate students <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>, <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

### Format and Difficulty
*   It is a six-hour test consisting of 12 questions, divided into two three-hour sessions <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>, <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.
*   Each question is scored from 1 to 10, making the highest possible score 120 <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>, <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.
*   Despite being taken by students already deeply interested in math, the median score is typically around 1 or 2, indicating its extreme difficulty <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>, <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>, <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>, <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
*   Problems within each section generally increase in difficulty from question 1 to 6, although "difficulty is in the eye of the beholder" <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>, <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>, <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
*   Paradoxically, the "fives and sixes" (the hardest problems) often have the most elegant solutions <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>, <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>, <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

## Case Study: A Putnam Problem Example

One example of a Putnam question is: "If you choose four random points on a sphere, and consider the tetrahedron with these points as its vertices, what is the probability that the center of the sphere is inside that tetrahedron?" <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>, <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>, <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

## [[Problemsolving strategies in mathematics | Strategies for Approaching Difficult Math Problems]]

### 1. Simplify the Problem
A common and effective strategy is to start by thinking about simpler cases <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>, <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

#### Example: Two Dimensions
For the sphere problem, simplify to two dimensions: choosing three random points on a circle, and finding the probability that the triangle formed by these points contains the center of the circle <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>, <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>, <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>, <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

*   **Fix points:** Imagine fixing two points (P1, P2) and letting the third (P3) vary <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>, <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
*   **Identify critical regions:** Drawing lines from P1 and P2 through the center divides the circle into four arcs. The triangle contains the center only if P3 is in the arc opposite P1 and P2 <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>, <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>, <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>, <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>, <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
*   **Calculate average probability:** Assuming points are equally likely on the circle, the probability that P3 lands in the relevant arc is its length divided by the circumference <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>, <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>, <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>, <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. The size of this arc depends on P1 and P2 <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
*   **Average over random choices:** If P1 is fixed and P2 varies, every angle between 0 and 180 degrees is equally likely <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>, <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>, <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>, <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>, <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. This means every proportion between 0 and 0.5 for the arc is equally likely, leading to an average proportion of 0.25 <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. Thus, the overall probability for the 2D case is 1/4 <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>, <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>, <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

### 2. Reframe the Problem with New Constructs
When a construct (like lines through the center) simplifies the problem, reframe the entire question around it <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>, <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>, <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. This is a broader lesson for [[mathematical_problemsolving_and_flexibility | mathematical problem solving]] <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>, <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

#### Alternative Approach (2D)
Instead of choosing three random points, imagine choosing two random lines through the circle's center <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>, <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. For each line, flip a coin to decide which of its two endpoints becomes P1 and P2 respectively <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>, <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>, <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. This method is equivalent to choosing random points <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>, <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

*   Consider P3 chosen first, then the two lines <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>, <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
*   Once the lines and P3 are set, there are four equally likely outcomes for P1 and P2 based on the coin flips <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>, <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>, <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
*   Only one of these four outcomes places P1 and P2 on the opposite side of the circle as P3, making the triangle contain the center <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>, <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   Therefore, regardless of the lines and P3, the probability is always 1/4 <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>, <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

#### Generalizing to Three Dimensions
This reframing technique extends seamlessly to three dimensions <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>, <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

*   Choose three random lines through the center of the sphere and a random point P4 <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>, <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>, <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   For each line, flip a coin to decide which of the two endpoints becomes P1, P2, and P3 <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>, <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>, <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   There are 2 x 2 x 2 = 8 equally likely outcomes for these coin flips <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>, <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
*   Exactly one of these 8 outcomes places P1, P2, and P3 on the opposite side of the center as P4, resulting in a tetrahedron that contains the center <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>, <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>, <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>, <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   Therefore, the probability is 1/8 <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

While this solution relies on [[visual proofs and misconceptions in math | visual intuition]], it can be formally articulated using tools like linear algebra for a rigorous proof <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>, <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>, <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>, <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. This highlights that insight and formal articulation are distinct skills in mathematics <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>, <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>, <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

## Key Takeaways for [[Problemsolving strategies in mathematical puzzles | Mathematical Problem Solving]]

*   **Simplify:** Continuously break down a complex problem into simpler versions until a foothold is found <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>, <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
*   **Reframe:** If new constructs prove useful in simplification, attempt to reframe the entire problem around those constructs <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>, <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   **Practice:** Engaging with varied problems and practicing problem-solving abilities is crucial for improvement <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>, <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>, <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.