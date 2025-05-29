---
title: 2011 IMO problem 2 analysis
videoId: M64HUIJFTZM
---

From: [[3blue1brown]] <br/> 

The International Math Olympiad (IMO) is an annual contest where over 100 countries send six of their brightest teenagers to represent them [00:00:02]. The IMO serves as a culminating symbol for the extensive world of contest math [00:00:14]. The contest itself is a test split over two days, with three proof-based questions given over four and a half hours each day [00:00:26]. Participants must discover and articulate rigorous lines of reasoning for each difficult question, with each problem scored on a scale from 0 to 7 [00:00:37].

In 2011, the IMO had 563 total participants representing 101 countries [00:00:51]. Notably, 563 and 101 are prime numbers [00:00:56]. Out of all participants, only one, Lisa Sauermann from Germany, achieved a perfect score [00:01:03]. For the next two runners-up that year, the only obstacle to a perfect score was problem number two [00:01:09].

## The Windmill Problem Description

The 2011 IMO Problem 2, known as the "windmill" problem, is described as follows:

> Let S be a finite set of at least two points on the plane [00:01:29]. Assume that no three points of S are collinear [00:01:38]. A windmill is a process that starts with the line L going through a single point P in S [00:01:51]. The line rotates clockwise around the pivot P until the first time that line meets some other point belonging to S [00:01:57]. This new point, Q, takes over as the new pivot, and the line now rotates clockwise about Q until it next meets a point of S [00:02:12]. This process continues indefinitely [00:02:21].

The question asks: "Show that we can choose a point P in S and a line L going through P such that the resulting windmill uses each point of S as a pivot infinitely many times" [00:02:42]. The condition that no three points are collinear prevents ambiguity about which pivot to switch to [00:02:30].

## Uniqueness and Difficulty

This problem is considered beautiful and, despite its apparent simplicity, evaded many of the world's best mathematicians of their age [00:01:15]. The solution is understandable to a wide audience [00:01:19].

Unlike other Olympiad problems that might involve function analysis, numerical patterns, [[techniques_for_olympiad_level_counting_problems | counting setups]], or elaborate [[geometric_problem_solving_and_state_space_analysis | geometric constructions]], Problem 2 is an unusually pure puzzle [00:03:15]. Proving that an initial condition leads to the windmill hitting all points infinitely many times doesn't test knowledge of a particular theorem, but rather the ability to find a clever perspective [00:03:31].

The problem's results suggest it was much harder than the contest organizers expected [00:03:55]. Typically, the three problems each day are designed to get progressively harder [00:04:00]:
*   Problems one and four are considered "doable" [00:04:06].
*   Problems two and five are "challenging" [00:04:10].
*   Problems three and six can be "brutal" [00:04:13].

However, for the 2011 IMO:
*   Only 22 out of 563 participants achieved full marks for Problem 2 [00:04:16].
*   By contrast, 170 got a perfect score on Problem 5, which was supposed to be of similar difficulty [00:04:28].
*   More than twice as many participants (over 44) got a perfect score for Problem 3, which was supposed to be harder [00:04:34].
*   Problem 6 had only 6 perfect scores, making it the hardest by some measures [00:04:40].

Interestingly, out of the six students who solved Problem 6 (clearly world-class problem solvers), five out of six were unable to solve this windmill puzzle [00:04:55]. This highlights that the problem's difficulty stems from its demand for insight rather than background knowledge [00:05:09].

## Approaching the Solution

The first step in approaching such a puzzle is to "play around with it and get a feel for it" [00:05:18]. This involves starting with simple cases and gradually increasing complexity:

*   **Two points**: The line simply trades off between each point [00:05:27].
*   **Three points**: The line rotates around them [00:05:34].
*   **Four points**: This is where it becomes interesting [00:05:47]. If one point is inside a triangle formed by the other three, the windmill might not hit it if started from the outside points [00:05:48]. However, if the process starts with the line going through that "troublesome middle point," it does bounce off all points in a cycle [00:06:09].

Initial observations suggest that when the line starts passing through the "middle" of the points, it tends to stay there and never ventures to the outside [00:06:51]. The goal is to rigorously define this "middle" condition and prove that all points will be hit infinitely many times [00:07:09].

### Key Insight 1: Formalizing the "Middle" with an Invariant

A general problem-solving tip is to formalize vague ideas, preferably by assigning numbers and asking questions about them [00:07:39]. For the windmill problem, the "middle" can be formalized by counting how many points are on either side of the line [00:07:53].

By giving the line an orientation (e.g., a left "blue" half and a right "brown" half), a line is considered "in the middle" if there are an equal number of blue and brown points [00:08:00]. If the total number of points is odd, the pivot point is considered "white" or neutral [00:08:17]. For example, with 11 points, there would be 5 blue, 5 brown, and 1 white pivot [00:08:26].

A crucial question then arises: what happens to the number of blue and brown points as the windmill process plays out? [00:08:39] Through observation, it appears these numbers remain constant [00:08:48].

The reason these numbers don't change lies in how the line shifts its pivot [00:09:19]:
*   If the line hits a blue point (on its left), this must happen below the pivot. When the new pivot takes over and the line continues rotating, the old pivot (now above the new one) ends up in the blue region [00:09:31].
*   Symmetrically, if it hits a brown point (on its right), this happens above the pivot, and the old pivot ends up in the brown region [00:09:46].

Thus, the number of points on a given side of the line does not change, except for the instant the line passes through two points at once, which is transient [00:09:54]. When a blue point is "lost" as a pivot, a new one is "gained" on that side, and similarly for brown points [00:10:02]. This constancy of points on either side is a key insight [00:10:07].

### Key Insight 2: Cycle Completion

The second key insight is to consider what happens when the line has turned 180 degrees [00:10:18].
*   When the line rotates 180 degrees, it becomes parallel to its starting position [00:10:25].
*   Because the number of points on each side must remain constant, the line must be passing through the *same point* it started on [00:10:28]. If it ended on any other point, the distribution of points on either side would change [00:10:37].
*   Additionally, after a 180-degree rotation, everything that was on the "blue" side has become "brown," and vice-versa [00:10:48]. The only way for points to change sides is by being hit by the line [00:10:55].

For the **odd-numbered case**: After a half rotation (180 degrees), the line returns to its starting point and has hit all other points [00:11:07]. This means the process repeats, cycling through all points infinitely many times [00:11:16].

For the **even-numbered case**: The scheme needs a slight alteration for the initial setup. The pivot point is now counted as a brown point [00:11:32]. The initial condition is still that half the points are blue (on the left) and half are brown (on the right or the pivot) [00:11:39]. The same argument implies that after a 180-degree turn, colors have swapped [00:11:53]. This time, the line will be passing through a *different* point after the first half turn (specifically, one that used to be blue) [00:11:56]. However, after *another* 180 degrees (a full 360-degree rotation in total), it must be passing through the point it started on [00:12:07]. Again, this is because it's parallel to its starting position, and the number of points on a given side would be different otherwise [00:12:13]. This full cycle also hits all points and ensures the process repeats infinitely [00:12:23].

## Lessons Learned

This puzzle offers two important lessons:

### Social Lesson: [[challenges_in_assessing_problem_difficulty | Difficulty in Assessing Problem Difficulty]]

Once the solution is known, it's easy to mistakenly believe the problem is simpler than it actually is [00:12:47]. Ideas like counting points on a side might seem obvious in hindsight [00:12:57]. However, the IMO context provides empirical data: it was a genuinely hard problem, even for world-class students [00:13:08]. In mathematics, it's difficult to empathize with not understanding something [00:13:23]. People, including math exercise creators, often struggle to judge the difficulty of their own problems [00:13:35]. The core challenge lies in discerning *why* a particular insight (like counting points on a side) would emerge from the vast space of possible considerations [00:13:54].

### Mathematical Lesson: The Power of Invariants

The ultimate path to solving this problem was identifying something within the complex system that remains constant during its chaotic unfolding [00:14:12]. This concept is known as an "invariant" and is a ubiquitous theme in mathematics and physics [00:14:20].
*   Topologists use invariants to count holes in surfaces [00:14:27].
*   Physicists define energy and momentum as invariants, or more abstract concepts like proper time in special relativity [00:14:30].

While students often take handed-down definitions for granted, solving puzzles where the insight involves finding an invariant reveals that each such definition was once a clever discovery [00:14:38].

Terence Tao, a prominent modern mathematician and the world's youngest IMO medalist, likened mathematical puzzles to fables or anecdotes for understanding real life [00:14:53]. Though contrived, these puzzles carry lessons relevant to useful problems that might need to be solved one day [00:15:09]. The "windmill" puzzle, like a mathematical Aesop, teaches the moral of seeking quantities that remain constant [00:15:17]. Finding an invariant can lead to elegant solutions and make the solver appear ingenious [00:15:26].