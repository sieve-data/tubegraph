---
title: Teaching and understanding mathematical concepts
videoId: M64HUIJFTZM
---

From: [[3blue1brown]] <br/> 

The International Math Olympiad (IMO) is a prestigious competition where over 100 countries send six of their brightest teenagers to represent them annually <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. It serves as a culminating symbol for the contest math world <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. The contest is a two-day test, with three proof-based questions given over four and a half hours each day <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. Each question requires discovering and articulating a rigorous line of reasoning, scored from 0 to 7 <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## The 2011 IMO Problem 2: The Windmill

In 2011, with 563 participants from 101 countries <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>, only one participant, Lisa Sauermann from Germany, achieved a perfect score <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. The only obstacle preventing the next two runners-up from a perfect score was problem number two, often referred to as the Windmill Problem <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Despite its difficulty for many top young mathematicians, its solution is accessible <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

### Problem Statement
The problem begins by defining a finite set `S` of at least two points on a plane, with no three points being collinear <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This non-collinear condition is crucial, as it prevents ambiguity when the line meets multiple points <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

A "windmill" is a process:
1.  It starts with a line `L` passing through a single point `P` in `S` <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
2.  The line `L` rotates clockwise around `P` until it first meets another point `Q` in `S` <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
3.  `Q` then becomes the new pivot, and the line rotates clockwise around `Q` until it meets another point of `S` <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
4.  This process continues indefinitely <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

The question is to demonstrate that one can choose an initial point `P` in `S` and a line `L` through `P` such that the resulting windmill process uses every point of `S` as a pivot infinitely many times <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

### Uniqueness and Difficulty
This problem is distinctive because it is an "unusually pure puzzle" <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. Unlike typical Olympiad problems that might involve analyzing [[mathematical_functions_and_graphs | functions]], deducing numerical patterns, complex counting, or elaborate [[mathematical_exercises_and_problemsolving_in_geometry | geometric constructions]] <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>, the Windmill Problem doesn't test knowledge of a specific theorem <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. Instead, it tests one's ability to find a clever perspective <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

The problem proved to be unexpectedly difficult for participants. While problems one and four are typically considered "doable", and problems two and five "challenging", with three and six being "brutal" <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>, Problem 2 of 2011 deviated significantly:
*   Only 22 out of 563 participants got full marks for Problem 2 <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   In contrast, 170 got a perfect score on Problem 5 (supposedly similar difficulty) <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
*   More than twice as many got a perfect score on Problem 3 (supposedly harder) <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   Even among the six students who solved the hardest problem (Problem 6), five out of six were stumped by this windmill puzzle <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

This highlights that the problem's difficulty stems not from required background knowledge but purely from the need for insight <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

## [[approaches_to_mathematical_problem_solving | Approaches to Mathematical Problem Solving]]

### Play and Experimentation
The first step in any puzzle is to simply play around and get a feel for it, starting simple and gradually increasing complexity <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   **Two points:** The line smoothly trades off between each point <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Three points:** The line clearly rotates around them <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Four points:** This is where it gets interesting. If one point is inside a triangle formed by the others, the windmill might not hit it <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. However, the problem asks to *choose* a starting position. If the line starts through the troublesome middle point, the windmill *does* bounce off all points and ends up back where it started <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. Playing around reveals that if the line starts passing through the "middle" of the points, it tends to stay there, never venturing to the outside <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

This iterative process of [[conceptualizing_mathematical_problems | conceptualizing mathematical problems]] and testing small cases is a crucial [[problemsolving_strategies_in_mathematics | problem-solving strategy in mathematics]].

### Key Insight 1: Counting Points on Each Side (An Invariant)
To make the idea of "starting in the middle" more rigorous, one can formalize it by counting points on either side of the line <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
1.  Orient the line to define a "left half" (blue points) and a "right half" (brown points) <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
2.  A line is "in the middle" if there are equal numbers of blue and brown points <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
3.  If the total number of points `N` is odd, the pivot point can be considered neutral (white), with `(N-1)/2` blue and `(N-1)/2` brown points <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
4.  The crucial observation is that the number of blue and brown points *does not change* as the windmill process plays out <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
    *   When the line rotates and hits a new point `Q` (e.g., a blue point below the pivot), `Q` becomes the new pivot. The old pivot, now above `Q`, moves to the left side and becomes a blue point <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
    *   Symmetrically, if it hits a brown point, the old pivot moves to the right and becomes a brown point <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
    *   This means for every point that leaves a side (by becoming the pivot), another point enters that side (the old pivot) <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
    *   This "number of points on a given side of the line" is the first [[mathematical_insights_and_elegant_solutions | key insight]] and an invariant of the system <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

### Key Insight 2: Half-Rotation and Cycle
The second key insight involves observing what happens when the line turns 180 degrees <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
*   **Odd number of points:** After turning 180 degrees, the line is parallel to its starting position <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. Because the number of points on each side must remain constant, the line must be passing through the *same point* it started on <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. Additionally, everything that was blue is now brown, and vice-versa, meaning every point (except the pivot) must have been hit by the line <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. Thus, after a half rotation, the line is back where it started, having hit all other points. This creates a cycle that repeats indefinitely, hitting all points infinitely many times <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Even number of points:** The scheme needs a slight alteration. To maintain equal counts, the pivot point itself can be counted as belonging to one side (e.g., the brown side) <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. The argument that the number of points on each side remains constant still holds <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>. After a 180-degree turn, the line will be parallel to its starting position, but it will be passing through a *different point* (one that was previously blue) <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>. However, after another 180-degree turn (a full 360-degree rotation), the line must be passing through the *original starting point* again, as it's parallel to the start and maintains the same side counts <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. This creates a 360-degree cycle that hits all points and returns to the initial state, thus ensuring all points are hit infinitely many times <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.

This constitutes a rigorous [[mathematical_proofs_and_logical_deduction | mathematical proof]] of the windmill problem.

## Lessons on [[conceptualizing_mathematical_problems | Conceptualizing Mathematical Problems]]

### The Social Lesson: Perceiving Difficulty
Once a solution is known, it is easy to be fooled into thinking the problem was simpler than it actually was <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. For example, the constancy of points on each side might seem "obvious" in hindsight <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. However, the IMO data clearly demonstrates that this was a genuinely hard problem, even for the world's best students <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.

In mathematics, it's challenging to empathize with the state of not understanding something <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>. As observed by a former Khan Academy coworker involved in creating [[educational_resources_for_teaching_linear_algebra | math exercises]], contributors often struggle to assess the difficulty of their own exercises <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. Knowing when math is hard is often harder than the math itself <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>. This is a vital consideration both for teaching and for being taught <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>. When faced with the vast array of possible ideas to consider, why would one's mind turn to the specific idea of counting points on each side <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>?

### The Mathematical Lesson: Invariants
The ultimate solution relied on finding something within the complex system that *stays constant* during its chaotic unfolding <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. This concept, known as an **invariant**, is a ubiquitous theme in mathematics and physics <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.
*   Topologists use invariants like the number of holes in a surface <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.
*   Physicists define invariants such as energy, momentum, or proper time in special relativity <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.

Students often take definitions for granted, but solving puzzles where the insight comes from an invariant fosters an appreciation that these definitions were once clever discoveries <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.

## The Value of Mathematical Puzzles
Terence Tao, a renowned modern mathematician and the youngest IMO medalist, likened mathematical puzzles to fables or anecdotes that help the young understand real life <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. While contrived, these puzzles carry lessons relevant to useful, real-world problems <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>. The Windmill Problem, like a mathematical Aesop, teaches the moral to seek quantities that stay constant <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>. Finding an invariant can lead to an elegant solution, making one appear ingenious, and this skill, honed through seemingly abstract puzzles, can be invaluable in solving practical problems <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.