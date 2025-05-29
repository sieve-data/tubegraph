---
title: International Math Olympiad overview
videoId: M64HUIJFTZM
---

From: [[3blue1brown]] <br/> 

The International Math Olympiad (IMO) is an annual contest where over 100 countries send six of their brightest teenagers, or occasionally younger prodigies, to represent them <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. It stands as a culminating symbol for the extensive world of contest math, with each participating country having its own elaborate system of contests to select its representatives <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Contest Format

The IMO competition is a test split over two days <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. Each day, participants are given three questions to solve over four and a half hours <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. All questions require proofs, meaning contestants must discover and articulate a rigorous line of reasoning rather than simply finding a numerical answer <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. Each question is scored on a scale from 0 to 7 <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

Typically, the three problems each day are designed to get progressively harder <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>:
*   **Problems 1 and 4**: Considered "doable" <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
*   **Problems 2 and 5**: Challenging <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
*   **Problems 3 and 6**: Can be brutal <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

## The 2011 IMO Problem 2: The Windmill Problem

The 2011 IMO had 563 participants representing 101 countries <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. Only one participant, Lisa Sauermann from Germany, achieved a perfect score <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. The only obstacle preventing the next two runners-up from a perfect score was Problem 2 <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. This problem, despite stumping many of the world's best young mathematicians, has a solution comprehensible to a general audience <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

### Problem Statement

"Let S be a finite set of at least two points on the plane. Assume that no three points of S are collinear. A windmill is a process that starts with the line L going through a single point P in S. The line rotates clockwise around the pivot P until the first time that line meets some other point belonging to S. This point, Q, takes over as the new pivot, and the line now rotates clockwise about Q until it next meets a point of S. This process continues indefinitely. Show that we can choose a point P in S and a line L going through P such that the resulting windmill uses each point of S as a pivot infinitely many times." <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a> <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>

The condition that no three points are collinear is crucial to avoid ambiguity about which point to switch to as the new pivot <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

### Unconventional Nature of the Problem

Problem 2 is considered an unusually pure puzzle, differing from other Olympiad problems that often involve function analysis, numerical patterns, counting setups, or elaborate geometric constructions <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. It does not test knowledge of a particular theorem but rather the ability to find a clever perspective <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This reliance on [[mathematical_insights_and_elegant_solutions | insight]] rather than existing mathematical results makes it challenging to prepare for <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

### Difficulty Statistics

The 2011 IMO results showed Problem 2 was unexpectedly difficult <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. Only 22 out of 563 participants achieved a perfect score on Problem 2, compared to 170 for Problem 5 (supposedly similar difficulty) and over twice as many for Problem 3 (supposedly harder) <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. Even among the six students who solved Problem 6 (the hardest problem that year), five out of six were unable to solve the windmill puzzle <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

### [[approaches_to_mathematical_problem_solving | Approaches to Mathematical Problem Solving]]: Finding an Invariant

The first step in solving any puzzle is to [[problemsolving_strategies_in_math | play around]] with it to get a feel, starting with simple cases and gradually increasing complexity <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   **Two points**: The line simply trades off between the two points <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Three points**: The line rotates around them <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Four points**: This is where it gets interesting. If one point is inside a triangle formed by the others, the windmill might not hit it unless the line starts by passing through that inner point <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. Initial observation suggests that if the line starts passing through the "middle" of the points, it tends to stay there, never venturing to the outside <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

To formalize the idea of "starting in the middle," a key [[problemsolving_strategies in math | problem-solving strategy]] is to put numbers to vague ideas <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. This led to considering the number of points on either side of the line <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. By giving the line an orientation, points can be categorized as "blue" (on the left) or "brown" (on the right) <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. A line is "in the middle" if there are an equal number of blue and brown points <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

The crucial [[mathematical_insights_and_elegant_solutions | insight]] is that the number of points on a given side of the line remains constant throughout the windmill process <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. This is because when the line changes its pivot, the old pivot point moves from being "neutral" (on the line) to either the blue or brown region, effectively replacing a point that moved off that side of the line <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>. This unchanging quantity is known as an [[role_of_invariants_in_mathematics | invariant]] <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.

### Solution Using the Invariant

*   **Odd number of points**: If the total number of points is odd, and the initial line is chosen such that there are an equal number of points on either side (with the pivot being neutral), the number of points on each side remains constant <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. After the line has rotated 180 degrees, it will be parallel to its starting position and must be passing through the same point it started on, maintaining the equal distribution of points <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. During this half-rotation, every point not on the line has effectively swapped sides, meaning it must have been "hit" by the line <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. Thus, after a half-rotation, the line is back where it started, having hit all other points, and the process repeats infinitely <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Even number of points**: The scheme is slightly altered. The pivot point is now counted as belonging to one side (e.g., brown) <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. The initial condition still dictates an equal number of blue and brown points <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>. After a 180-degree turn, the line will be parallel to its starting position, but it will be passing through a different point that was previously "blue" <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>. After another 180-degree turn (a full 360-degree rotation from the start), the line will return to its initial point and orientation <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. This cycle, which hits all points, then repeats indefinitely <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.

### Lessons from the Puzzle

*   **Perception of Difficulty**: Once a solution is known, a problem often appears simpler than it truly is <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>. The IMO data confirms that the windmill problem was genuinely hard for even the world's best students <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. Knowing when math is hard is often more difficult than the math itself, a crucial point for [[teaching_and_understanding_mathematical_concepts | teaching and understanding mathematical concepts]] <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.
*   **Mathematical Takeaway**: The solution highlights the ubiquitous theme in mathematics and physics of finding an [[role_of_invariants_in_mathematics | invariant]] – something that stays constant within a complex and seemingly chaotic system <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. This concept is central to fields like topology (counting holes in a surface) and physics (energy, momentum, proper time) <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>. Recognizing these definitions as clever discoveries rather than given facts is part of appreciating their significance <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.

Terence Tao, a renowned mathematician and the youngest IMO medalist, likened [[conceptualizing_mathematical_problems | mathematical problems]] and puzzles to fables: "important to real mathematics, like solving real-life problems, just as fables, stories, and anecdotes are important to the young in understanding real life" <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. While seemingly contrived, these puzzles offer lessons, such as seeking invariants, that can be applied to real-world problems <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.