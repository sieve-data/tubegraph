---
title: Windmill puzzle explanation and solution
videoId: M64HUIJFTZM
---

From: [[3blue1brown]] <br/> 

The International Math Olympiad (IMO) is an annual contest where over 100 countries send six of their brightest teenagers to compete in contest math <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. The contest is a two-day test, with three proof-based questions given over four and a half hours each day <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. Each question is scored from 0 to 7 <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

The focus here is on Problem Number Two from the 2011 IMO <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. Out of 563 participants from 101 countries, only Lisa Sauermann from Germany achieved a perfect score <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. Problem number two was the only obstacle preventing the next two runners-up from also achieving perfect scores <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Despite its difficulty, the solution to this "beautiful" problem is understandable by anyone <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

## The Windmill Puzzle Defined

Let S be a finite set of at least two points on a plane <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. A crucial condition is that no three points of S are collinear <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This condition prevents ambiguity in choosing a pivot if a line were to pass through more than two points simultaneously <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

The "windmill" is a process that begins with a line L passing through a single point P in S <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   The line rotates clockwise around the pivot P <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   It continues rotating until it first encounters another point, Q, belonging to S <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   This point Q then becomes the new pivot <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   The line then rotates clockwise about Q until it next meets another point in S, and this process continues indefinitely <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

The question is: Show that we can choose a point P in S and a line L through P such that the resulting windmill uses each point of S as a pivot infinitely many times <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

## Why This Puzzle Is Challenging

The windmill problem is an "unusually pure puzzle" <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. Unlike other Olympiad problems that might involve analyzing functions, deducing numerical patterns, counting setups, or elaborate [[geometry_puzzles_involving_tiling_and_shapes | geometric constructions]], this problem doesn't test knowledge of a particular theorem <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. Instead, it tests one's ability to find a clever perspective <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

The IMO 2011 results demonstrate its unexpected difficulty <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>:
*   Typically, problems 1 and 4 are considered "doable," 2 and 5 "challenging," and 3 and 6 "brutal" <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   Only 22 out of 563 participants achieved a perfect score on Problem Two <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   In contrast, 170 got perfect scores on Problem Five (supposedly similar difficulty), and more than twice as many on Problem Three (supposedly harder) <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
*   Even among the six students who solved Problem Six (the actual hardest problem that year), five out of six were evaded by the windmill puzzle <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

The problem's difficulty stems not from demanding background knowledge but from requiring pure insight <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

## Approaching the Solution

### Playing Around with Examples

The first step in any puzzle is to experiment and gain intuition <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. Starting simple and gradually increasing complexity is a good [[problemsolving_strategies_in_mathematical_puzzles | problem-solving strategy]] <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>:
*   **Two points**: The line simply trades off between the two points <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Three points**: The line rotates around them <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Four points**: This is where it becomes interesting <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. If a point is inside the triangle formed by the other three, the windmill might not hit it if the starting line is on the outside <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. However, if the line starts through the "troublesome middle point," the windmill *does* bounce off all points in a cycle <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

Initial play suggests that if the line starts "passing through the middle of the points, it tends to stay there" <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. The challenge is to formalize this idea and prove that all points will be hit infinitely many times <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

### Key Insight 1: An Invariant Quantity

A general [[problemsolving_strategies_in_mathematical_puzzles | problem-solving tip]] is to formalize vague ideas, preferably by assigning numbers and asking questions about those numbers <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. To formalize the idea of a line being "in the middle," we can count the number of points on either side of the line <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

*   Give the line an orientation (e.g., left and right) <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   Color points on the left "blue" and points on the right "brown" <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
*   A line is "in the middle" if there are an equal number of blue and brown points <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   If the total number of points is odd, the pivot point (white) is neutral <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. For example, 11 points could have 5 blue, 5 brown, and 1 white pivot <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

The crucial question becomes: What happens to the number of blue and brown points as the windmill process unfolds <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>?

The answer: The number of points on a given side of the line **does not change** <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
*   When the line rotates clockwise and hits a blue point (on its left), it must be below the pivot <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   When that blue point becomes the new pivot, the old pivot (now above the new one) ends up on the left side, becoming a blue point <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.
*   Symmetrically, if it hits a brown point (on its right), the old pivot ends up in the brown region <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
*   Thus, when a point is "lost" from one side (by becoming the pivot), a "new" point is "gained" on that same side (the old pivot), maintaining the balance <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.

This constant count of points on each side is the **first key insight**: it's an [[gregory_galperins_discovery_and_pi_puzzles | invariant]] <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

### Key Insight 2: Completing the Cycle

How does this [[gregory_galperins_discovery_and_pi_puzzles | invariant]] ensure all points are hit infinitely many times?
*   Consider what happens after the line has turned 180 degrees <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. At this point, it is parallel to its starting position <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
*   Because the number of points on each side must remain constant, the line must be passing through the *same* point it started on (for an odd number of total points) <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. If it were passing through a different point, the count of points on either side would change <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
*   Additionally, after a 180-degree rotation, everything that was "blue" has become "brown" and vice-versa <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. The only way for a point to change its color is if it was "hit" by the line during the rotation <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

This implies that for an odd number of points, after a half rotation, the line is back where it started and has hit all of the other points <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. Since the state is identical, the process will repeat this exact set of motions, hitting all points infinitely many times <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.

For an even number of points, the scheme needs a slight alteration <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. To allow for equal numbers of blue and brown points, let the pivot count as a brown point <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.
*   The initial condition is set so half points are blue (left) and half are brown (right or pivot) <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>.
*   The same argument applies: after a 180-degree turn, colors swap, but this time the line will be passing through a *different* point (one that was blue) <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   However, after another 180 degrees (a full 360-degree rotation), the line *must* return to the point it started on, again because its orientation is parallel to the initial state and the side counts must be maintained <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.
*   This creates a 360-degree cycle that hits all points and returns to the starting position, ensuring all points are used infinitely many times <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.

Therefore, by choosing an initial line that balances the number of points on either side, the windmill process guarantees that every point in S will be used as a pivot infinitely many times.

## Lessons from the Puzzle

There are two main lessons from the windmill puzzle <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>:

### 1. The Social Aspect of Difficulty Perception
Once a solution is known, it's easy to fall into the trap of thinking the problem was simpler than it actually was <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. The IMO data unequivocally shows that this was a genuinely hard problem, even for the world's best students <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. This highlights a common challenge in mathematics: it is "extremely hard to empathize with what it feels like to not understand something" <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>. Knowing when math is hard is often harder than the math itself <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.

### 2. The Mathematical Takeaway: Invariants
The ultimate key to solving this puzzle was identifying something in the complex system that remained constant during its chaotic unfolding <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. This concept is known as an **[[gregory_galperins_discovery_and_pi_puzzles | invariant]]** <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.

[[gregory_galperins_discovery_and_pi_puzzles | Invariants]] are ubiquitous in mathematics and physics:
*   Topologists use them when counting the number of holes in a surface <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.
*   Physicists define energy and momentum, or abstract concepts like proper time in special relativity, as [[gregory_galperins_discovery_and_pi_puzzles | invariants]] <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.

Solving puzzles where the insight comes from finding an [[gregory_galperins_discovery_and_pi_puzzles | invariant]] helps one appreciate that fundamental definitions in math were once clever discoveries <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.

As Terence Tao, a renowned mathematician and the youngest IMO medalist, stated, mathematical problems or puzzles are "important to real mathematics, like solving real-life problems, just as fables, stories, and anecdotes are important to the young in understanding real life" <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. While contrived, these puzzles offer lessons relevant to useful problems one might face, emphasizing the moral to seek quantities that stay constant <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.