---
title: Windmill problem explanation
videoId: M64HUIJFTZM
---

From: [[3blue1brown]] <br/> 

The International Math Olympiad (IMO), established over 100 years ago, brings together six of the brightest teenagers from more than 100 countries annually to compete in contest math <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This event is the pinnacle of the expansive world of contest math <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. The contest is a two-day test, with three proof-based questions given over four and a half hours each day <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. Participants must discover and articulate a rigorous line of reasoning for each difficult question, with each scored from 0 to 7 <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## The 2011 Windmill Problem

The specific problem of interest is from the 2011 IMO, which had 563 participants representing 101 countries <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. Interestingly, 563 and 101 are both prime numbers <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. Only one participant, Lisa Sauermann from Germany, achieved a perfect score that year <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. Problem number two was the only obstacle for the next two runners-up in achieving a perfect score <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Despite its challenge to many top mathematicians, its solution is accessible <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

### Problem Statement

The problem is defined as follows <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>:
Let S be a finite set of at least two points on the plane <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. It is assumed that no three points of S are collinear, meaning no three points lie on the same straight line <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

A "windmill" is a process that begins with a line L passing through a single point P in S <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
1.  The line rotates clockwise around the pivot P until it first meets another point Q belonging to S <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
2.  This point Q then becomes the new pivot <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
3.  The line continues to rotate clockwise around Q until it meets another point of S <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
This process continues indefinitely <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. The "no three points collinear" rule prevents ambiguity about which point to switch the pivot to <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

The question is: Show that we can choose a point P in S and a line L going through P such that the resulting windmill uses each point of S as a pivot infinitely many times <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

## Unusually Hard Problem

This problem is considered an unusually pure puzzle, differing from typical Olympiad problems that might involve function analysis, numerical patterns, counting, or geometric constructions <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. It doesn't test knowledge of a specific theorem but rather the ability to find a clever perspective <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

The difficulty of Problem 2 was unexpected for the contest organizers <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. Typically, problems increase in difficulty over the two days, with problems one and four being "doable," two and five "challenging," and three and six "brutal" <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. However, only 22 of the 563 participants achieved a perfect score on Problem 2 <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. In contrast, 170 got a perfect score on Problem 5 (supposedly similar difficulty), and more than twice as many got a perfect score on Problem 3 (supposedly harder) <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. Even among the six students who solved the hardest problem, Problem 6, five out of six were evaded by this windmill puzzle <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. This highlights that its difficulty stems purely from the insight required, not background knowledge <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

## Approaching the Problem

The first step in solving any puzzle is to experiment and gain intuition, starting with simple cases <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   **Two points**: The line simply trades off between the two points <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Three points**: The line rotates around them in a cycle <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Four points**: This is where it becomes interesting <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. If one point is inside a triangle formed by the other three, the windmill might initially miss the inner point if started on the outside <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. However, the problem asks to *show that we can choose* a starting position <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>. If the line starts by going through the "troublesome middle point," it does indeed bounce off all points and returns to its starting position, cycling through all points <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

Through playing around, one might observe that when the line starts passing through the "middle" of the points, it tends to stay there and never ventures to the outside <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. The challenge is to formalize this "middle" idea and prove that all points will be hit infinitely many times <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

## The Solution: Finding an Invariant

A general problem-solving tip is to make vague productive ideas more exact, ideally by quantifying them and asking questions about those numbers <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

### Key Insight 1: Constant Number of Points on Each Side

One way to formalize the idea of a "middle" line is to count how many points are on either side of the line <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. By giving the line an orientation, points can be categorized as "blue" (on the left) or "brown" (on the right) <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. A line is considered "in the middle" if there are an equal number of blue and brown points <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

*   **Odd number of points**: If the total number of points is odd, the pivot point can be considered "white" or neutral <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. For example, with 11 points, there would be 5 blue, 5 brown, and 1 white pivot <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
*   **Even number of points**: For an even number of points, the scheme needs slight alteration. To maintain an equal count, the pivot point can be counted as part of one side, say brown <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. So, half the points are blue (on the left), and half are brown (on the right or the pivot) <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>.

The crucial observation is that the number of blue and brown points *remains constant* as the windmill process plays out <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
*   When the line hits a blue point (on its left), it happens below the current pivot <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. The old pivot, now above the new one, moves to the left side and becomes blue <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.
*   Symmetrically, when the line hits a brown point (on its right), it happens above the current pivot <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>. The old pivot moves to the right side and becomes brown <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
Thus, when a point is "lost" from one side (by becoming the pivot), a new one is "gained" (the old pivot shifts to that side) <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. This means the count of points on either side of the line, excluding the pivot, remains constant <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.

### Key Insight 2: Cycles and Infinitely Many Times

This constancy implies that the line must hit every point infinitely many times <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Odd number of points**: When the line rotates 180 degrees, it becomes parallel to its starting position <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. Because the number of points on each side must remain constant, the line *must* be passing through the same point it started on <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. Additionally, after a 180-degree rotation, every point that was blue has become brown, and vice-versa <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. The only way for points to change "color" (side) is if the line passes through them <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>. Therefore, in a half-rotation (180 degrees), the line returns to its starting point, having hit all other points <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. This exact set of motions then repeats indefinitely, hitting all points infinitely many times <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.

*   **Even number of points**: With the adjusted scheme (pivot counted as brown), the same argument applies <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>. After a 180-degree turn, everything has swapped colors, but the line will be passing through a *different* point (one that was previously blue) <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>. However, after another 180 degrees (a full 360-degree rotation), it *must* be passing through the point it started on <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. This is because it is parallel to its starting position, and if it were any other point, the side counts would differ <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>. Thus, a full cycle is formed, hitting all points and ending back in the initial position, ensuring all points are hit infinitely many times <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.

## Lessons from the Windmill Puzzle

There are two important takeaways from this problem <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>:

### 1. The Social Lesson: Judging Math Difficulty

It's easy to underestimate the difficulty of a problem once its solution is known <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. The IMO results clearly demonstrate that this problem was genuinely hard, even for world-class problem solvers <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. It is exceedingly difficult to empathize with not understanding something in mathematics <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>, and "knowing when math is hard is way harder than the math itself" <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>. This applies to both teaching and learning <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>. The key question remains: why would anyone's mind turn to the specific idea of counting points on either side, given the vast possibilities <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>?

### 2. The Mathematical Lesson: Finding Invariants

The solution to the windmill problem lies in finding an [[unsolved_problem_in_physics_and_math | invariant]]: something within a complex system that remains constant during its chaotic unfolding <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. This concept is ubiquitous in mathematics and especially in physics <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.
*   Topologists use invariants like the number of holes in a surface <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.
*   Physicists define invariants such as energy, momentum, or proper time in special relativity <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.
While definitions are often given to students as established facts, solving puzzles that rely on finding invariants helps one appreciate that each such definition was once a clever discovery <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.

Terence Tao, a renowned modern mathematician and the youngest IMO medalist, stated that mathematical problems or puzzles are "important to real mathematics, like solving real-life problems, just as fables, stories, and anecdotes are important to the young in understanding real life" <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. These "contrived" puzzles carry lessons relevant to useful problems, teaching the moral of seeking quantities that stay constant <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>. If a fictional windmill problem can prepare someone for a real problem, its artificiality is irrelevant <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.