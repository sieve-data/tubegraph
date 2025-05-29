---
title: Mathematical invariants and their significance
videoId: M64HUIJFTZM
---

From: [[3blue1brown]] <br/> 

The International Math Olympiad (IMO) is an annual competition where over 100 countries send six of their brightest teenagers to represent them in contest mathematics <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. The contest is a two-day test, with three proof-based questions given over four and a half hours each day, scored from 0 to 7 <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## IMO 2011 Problem 2: The Windmill Puzzle

In 2011, among 563 participants from 101 countries, only one student, Lisa Sauermann from Germany, achieved a perfect score on the entire test <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. The obstacle for the next two top-scoring participants was Problem Number Two, a "beautiful" problem with an understandable solution <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

The problem, known as the "Windmill Problem," is stated as follows:
> Let S be a finite set of at least two points on the plane. Assume that no three points of S are collinear. A windmill is a process that starts with the line L going through a single point P in S. The line rotates clockwise around the pivot P until the first time that that line meets some other point belonging to S. This point, Q, takes over as the new pivot, and the line now rotates clockwise about Q until it next meets a point of S. This process continues indefinitely. Show that we can choose a point P in S and a line L going through P such that the resulting windmill uses each point of S as a pivot infinitely many times <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

This problem is considered an unusually pure puzzle, unlike other Olympiad problems that might involve analyzing functions, deducing numerical patterns, solving complex counting setups, or elaborate [[importance_of_geometric_understanding_in_linear_algebra | geometric constructions]] <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. Its solution doesn't rely on knowledge of specific theorems but rather on finding a clever perspective <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

### Difficulty of the Problem

Despite being designated as a "challenging" problem (Problem 2), it proved significantly harder than anticipated <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. Typically, problems 1 and 4 are considered "doable," 2 and 5 "challenging," and 3 and 6 "brutal" <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. However, only 22 out of 563 participants achieved a perfect score on Problem 2, in stark contrast to 170 perfect scores on Problem 5 (supposedly similar difficulty) and more than twice as many on Problem 3 (supposedly harder) <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. Notably, five out of the six students who solved Problem 6 (the hardest problem that year) failed to solve Problem 2 <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. This highlights a common difficulty in mathematics: "Knowing when math is hard is way harder than the math itself" <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.

### Approaching the Puzzle

The first step in solving such a puzzle is to experiment and gain a feel for it, starting with simple cases. For two points, the line simply trades between them <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. With three points, the line rotates around them <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. The complexity emerges with four or more points, particularly when points are located "inside" the convex hull of others <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. The core of the problem asks to prove that *some* initial condition (a specific starting point and line) will lead to the windmill process hitting all points infinitely many times <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

## The Solution: Finding an Invariant

A powerful strategy in problem-solving is to formalize vague ideas, preferably by assigning numbers, and then asking questions about those numbers <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. For the Windmill Problem, the crucial insight lies in formalizing the idea of a line being "in the middle" of the points.

### Key Insight 1: Constant Number of Points on Each Side

One way to formalize "middle" is to count how many points are on either side of the line <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. By giving the line an orientation (e.g., left/blue and right/brown), a line is "in the middle" if there are an equal number of blue and brown points <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

Consider the case where the total number of points (N) is odd. If the line passes through one point (the pivot, "white"), there are `(N-1)/2` points on the left (blue) and `(N-1)/2` points on the right (brown) <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

As the line rotates and changes its pivot, the number of blue and brown points remains constant <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. This happens because:
*   If the line hits a blue point on its left, it does so below the pivot. When the line changes pivot, the old pivot moves to the left (becomes blue), replacing the point that just left the blue region <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   Symmetrically, if it hits a brown point, the old pivot moves to the right (becomes brown) <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
Therefore, the number of points on a given side of the line does not change, except for the instant the line passes through two points <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. When a blue point is "lost" as a pivot, a new one is "gained" on that side, and similarly for brown points <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. This is **Key Insight Number One** <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

### Key Insight 2: Cycles and Full Coverage

The second key insight involves observing what happens after the line has turned 180 degrees <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
*   After a 180-degree rotation, the line is parallel to its starting position <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
*   Because the number of points on each side must remain constant, the line *must* be passing through the same point it started on <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. If it ended on a different point, the counts would change <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
*   During this half-rotation, everything that was blue has become brown, and everything that was brown has become blue <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. The only way for a point to change its "color" (side of the line) is if the line hits it <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

For an odd number of points, after a 180-degree rotation, the line returns to its original pivot and has necessarily hit all other points <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. This cycle then repeats indefinitely, hitting all points infinitely many times <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.

For an even number of points, the scheme is slightly altered. If the pivot counts as a brown point, the number of blue points can equal the number of brown points <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. After 180 degrees, the line will pass through a different point (one that was previously blue), but after another 180 degrees (a full 360-degree rotation), it must return to the original starting pivot because it is parallel to the starting position and the side counts are maintained <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>. This 360-degree cycle also hits all points and ensures they are touched infinitely many times <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.

## The Power of Invariants

The solution to the Windmill Problem hinges on finding something within a complex, chaotic system that remains constant: an **invariant** <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. This is a recurring and crucial theme across various fields of mathematics and science:
*   **Topology:** Topologists identify invariants like the number of holes in a surface to classify shapes <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.
*   **Physics:** Physicists define concepts like energy and momentum as invariants in dynamic systems <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>. In special relativity, abstract invariants like proper time are fundamental <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.

Understanding invariants reveals that many fundamental definitions in mathematics and physics were once clever discoveries, not just arbitrary rules <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. As [[leonhard_eulers_role_in_mathematical_constants | Terence Tao]], a renowned mathematician and former IMO medalist, suggests, mathematical puzzles are akin to fables, teaching valuable lessons for real-life problem-solving <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. The moral of the Windmill Problem's story is to seek quantities that stay constant <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>, a powerful strategy for tackling complex problems.