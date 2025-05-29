---
title: International Math Olympiad overview
videoId: M64HUIJFTZM
---

From: [[3blue1brown]] <br/> 

The International Math Olympiad (IMO) is an annual contest where over 100 countries send six of their brightest teenagers, or occasional prepubescent prodigies, to represent them <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. It serves as the culminating symbol for the expansive world of contest math, with each country having its own elaborate system of contests leading to their representatives' selection <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Contest Format

The IMO is a two-day test, with three proof-based questions given over four and a half hours each day <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a>. Participants must discover and articulate rigorous lines of reasoning to answer each difficult question, rather than simply finding a numerical answer <a class="yt-timestamp" data-t="00:34:00">[00:34:00]</a>. Each question is scored on a scale from 0 to 7 <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>.

### 2011 IMO Problem 2 Analysis

The 2011 IMO had 563 participants representing 101 countries <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>. Only one participant, Lisa Sauermann from Germany, achieved a perfect score <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>. For the next two top scorers, the only obstacle to a perfect score was [[2011_imo_problem_2_analysis | problem number two]] <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>.

Typically, the three problems each day are designed to get progressively harder <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. Problems one and four are considered "doable," two and five are "challenging," and three and six can be "brutal" <a class="yt-timestamp" data-t="04:06:00">[04:06:00]</a>. However, in 2011, [[2011_imo_problem_2_analysis | problem two]] proved unusually difficult:
*   Only 22 out of 563 participants achieved full marks for [[2011_imo_problem_2_analysis | question number two]] <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>.
*   By contrast, 170 participants got a perfect score on problem five (supposedly similar difficulty) <a class="yt-timestamp" data-t="04:28:00">[04:28:00]</a>.
*   More than twice as many got a perfect score for problem three (supposedly harder) <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>.
*   Even among the six students who solved problem six (the hardest that year), five of them were evaded by the windmill puzzle <a class="yt-timestamp" data-t="04:55:00">[04:55:00]</a>.

#### The Windmill Problem Description

[[2011_imo_problem_2_analysis | Problem two]] is described as an "unusually pure puzzle" <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>. It does not primarily test knowledge of a particular theorem, but rather the ability to find a clever perspective <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>.

The problem states:
> Let S be a finite set of at least two points on the plane <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>. Assume that no three points of S are collinear <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>. A windmill is a process that starts with the line L going through a single point P in S <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>. The line rotates clockwise around the pivot P until the first time that line meets some other point belonging to S <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. This new point, Q, takes over as the new pivot, and the line rotates clockwise about Q until it next meets a point of S <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>. This process continues indefinitely <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.

The question is:
> Show that we can choose a point P in S and a line L going through P such that the resulting windmill uses each point of S as a pivot infinitely many times <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>.

#### Solving the Windmill Problem

Solving this problem involves finding a clever perspective <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>.
A general [[mathematical_problemsolving_and_flexibility | problem-solving]] tip is to play around with the puzzle and get a feel for it, starting simple and gradually increasing complexity <a class="yt-timestamp" data-t="05:18:00">[05:18:00]</a>. For this problem, it's helpful to start drawing examples using a [[visual_approach_to_math_concepts | visual approach to math concepts]] <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>, <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>.
*   With two points, the line trades off between each point <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>.
*   With three points, the line rotates around them <a class="yt-timestamp" data-t="05:34:00">[05:34:00]</a>.
*   With four points, the behavior becomes more complex, especially if one point is inside a triangle formed by the others <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>. If the windmill starts with the line going through a "troublesome middle point," it appears to bounce off all points and cycle <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>.
*   Playing around suggests that if the line starts in the middle, it tends to stay there and never ventures to the outside <a class="yt-timestamp" data-t="06:51:00">[06:51:00]</a>, <a class="yt-timestamp" data-t="07:04:00">[07:04:00]</a>.

To make the idea of "starting in the middle" more rigorous, one should [[challenges_of_formalizing_mathematical_insights | formalize mathematical insights]] by quantifying aspects of the system <a class="yt-timestamp" data-t="07:12:00">[07:12:00]</a>, <a class="yt-timestamp" data-t="07:39:00">[07:39:00]</a>. A key insight for this problem is to count how many points are on either side of the line <a class="yt-timestamp" data-t="07:53:00">[07:53:00]</a>. By giving the line an orientation, points can be colored "blue" (left half) or "brown" (right half) <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>.

#### The Key Insight: Invariance

The first key insight is that the number of points on a given side of the line remains constant throughout the windmill process <a class="yt-timestamp" data-t="09:54:00">[09:54:00]</a>. This happens because as the line changes its pivot:
*   If the line hits a blue point (on its left) below the pivot, the old pivot moves to the blue region <a class="yt-timestamp" data-t="09:24:00">[09:24:00]</a>.
*   If it hits a brown point (on its right) above the pivot, the old pivot moves to the brown region <a class="yt-timestamp" data-t="09:46:00">[09:46:00]</a>.
*   This means that when a point leaves a side, another enters, maintaining the count <a class="yt-timestamp" data-t="10:02:00">[10:02:00]</a>.

For an odd number of points:
If the line starts such that there are an equal number of points on the left and right (e.g., 5 blue, 5 brown, and 1 white pivot point), the number of points on each side will not change <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a>, <a class="yt-timestamp" data-t="08:48:00">[08:48:00]</a>. When the line rotates 180 degrees, it will be parallel to its starting position and must be passing through the same point it started on, otherwise the counts on each side would change <a class="yt-timestamp" data-t="10:21:00">[10:21:00]</a>. During this half-rotation, every point not on the line changes from blue to brown or vice-versa, meaning every point has been hit by the line <a class="yt-timestamp" data-t="10:51:00">[10:51:00]</a>. Thus, after a half rotation, the line is back where it started, having hit all other points, and the process repeats infinitely <a class="yt-timestamp" data-t="11:07:00">[11:07:00]</a>.

For an even number of points:
The scheme is slightly altered: the pivot point is counted as a "brown" point <a class="yt-timestamp" data-t="11:28:00">[11:28:00]</a>. The initial condition is defined as a line with half the points blue (left) and half brown (right, including the pivot) <a class="yt-timestamp" data-t="11:39:00">[11:39:00]</a>. The same argument implies that after a 180-degree turn, everything has swapped colors <a class="yt-timestamp" data-t="11:53:00">[11:53:00]</a>. This time, the line will be passing through a different point after the first half-turn <a class="yt-timestamp" data-t="11:56:00">[11:56:00]</a>, but after another 180-degree turn (total 360 degrees), it must be passing through the point it started on <a class="yt-timestamp" data-t="12:07:00">[12:07:00]</a>. This creates a cycle that hits all points and ends in the same starting position, ensuring all points are hit infinitely many times <a class="yt-timestamp" data-t="12:23:00">[12:23:00]</a>.

## Lessons from the Puzzle

### Social Lesson: Assessing Difficulty
It's easy to underestimate the difficulty of a problem once its solution is known <a class="yt-timestamp" data-t="12:47:00">[12:47:00]</a>. The IMO data proves that this problem was genuinely hard, even for world-class problem solvers <a class="yt-timestamp" data-t="13:08:00">[13:08:00]</a>. In mathematics, it's difficult to empathize with not understanding something, and people often struggle to accurately gauge the difficulty of their own mathematical exercises <a class="yt-timestamp" data-t="13:23:00">[13:23:00]</a>.

### Mathematical Lesson: The Power of Invariants
The solution to the windmill puzzle highlights a ubiquitous theme in mathematics and physics: finding something about a complex system that stays constant during its chaotic unfolding <a class="yt-timestamp" data-t="14:12:00">[14:12:00]</a>. This is known as finding an [[mathematical_invariants_and_their_significance | invariant]] <a class="yt-timestamp" data-t="14:24:00">[14:24:00]</a>. Examples include:
*   Topologists counting holes in a surface <a class="yt-timestamp" data-t="14:27:00">[14:27:00]</a>.
*   Physicists defining energy and momentum, or proper time in special relativity <a class="yt-timestamp" data-t="14:30:00">[14:30:00]</a>.

The more puzzles one solves where the insight involves an [[mathematical_invariants_and_their_significance | invariant]], the more one appreciates that these fundamental definitions were once clever discoveries <a class="yt-timestamp" data-t="14:42:00">[14:42:00]</a>.

Terence Tao, an accomplished mathematician and youngest IMO medalist, likened mathematical problems or puzzles to fables for understanding real life, as they carry lessons relevant to useful problems that might be encountered one day <a class="yt-timestamp" data-t="14:53:00">[14:53:00]</a>. The "moral" of the windmill story is to seek quantities that stay constant <a class="yt-timestamp" data-t="15:17:00">[15:17:00]</a>.