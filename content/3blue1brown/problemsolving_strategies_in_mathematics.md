---
title: ProblemSolving Strategies in Mathematics
videoId: OkmNXy7er84
---

From: [[3blue1brown]] <br/> 

When approaching a mathematical problem, especially challenging ones, focusing on the [[problemsolving_strategies_in_math | problem-solving process]] itself can be more beneficial than just seeking a quick solution <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. This involves understanding where the insight comes from and how one might stumble upon a solution <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.

## Core Strategies for Problem Solving

### 1. Start with Simpler Cases
A fundamental [[approaches_to_mathematical_problem_solving | approach to mathematical problem solving]] is to simplify the problem <a class="yt-timestamp" data-t="01:51:30">[01:51:30]</a>. This helps in gaining a foothold from which to build up a more complex solution <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>.

*   **Dimensional Reduction**: If a problem is in three dimensions (e.g., points on a sphere), consider its two-dimensional analogue (e.g., points on a circle) <a class="yt-timestamp" data-t="01:54:10">[01:54:10]</a>.
*   **Fixing Variables**: In simpler cases, try fixing some of the variables or points and only letting a few vary. This can reveal patterns or special regions <a class="yt-timestamp" data-t="02:25:30">[02:25:30]</a>. For example, fixing two points on a circle and varying a third reveals a specific arc where the triangle formed contains the center <a class="yt-timestamp" data-t="02:34:10">[02:34:10]</a>.

### 2. Reframe the Problem
When a problem becomes conceptually easier by adding certain constructs (like drawing lines through the center of a circle), try to reframe the entire question in terms of these new constructs <a class="yt-timestamp" data-t="06:11:30">[06:11:30]</a>.

*   **Shift in Perspective**: Instead of choosing random points, consider choosing random lines through the center of the geometric shape <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>.
    *   For the 2D problem, this involves choosing two random lines through the circle's center, then flipping coins to determine which endpoints correspond to P1 and P2 <a class="yt-timestamp" data-t="06:28:00">[06:28:00]</a>.
    *   This reframing reveals that for any configuration of lines and a third point, there is always a 1-in-4 chance that the triangle contains the center, regardless of the initial points' positions <a class="yt-timestamp" data-t="07:27:00">[07:27:00]</a>.
*   **Generalization**: This strategy can seamlessly extend from two to three dimensions <a class="yt-timestamp" data-t="07:45:00">[07:45:00]</a>. For four points on a sphere, choose three random lines through the center and a random fourth point. With 8 equally likely outcomes from coin flips (for P1, P2, P3), only one will form a tetrahedron containing the sphere's center <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>. This reveals the probability of 1/8.

### 3. Contemplate the Answer
If an answer appears "suspiciously clean," consider what that number might represent <a class="yt-timestamp" data-t="05:46:00">[05:46:00]</a>. For example, the answer of 1/4 in the 2D case suggests a division into four possibilities.

### 4. Articulation and Formalization
Having the key [[Mathematical Insights and Elegant Solutions | insight]] and understanding is crucial, but articulating that understanding formally often requires a separate skill set, typically developed through practice in higher mathematics <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>. This can involve using tools like linear algebra for formal proofs <a class="yt-timestamp" data-t="08:52:00">[08:52:00]</a>.

## Example: Putnam Competition Problem

The Putnam competition is a rigorous math competition for undergraduate students, featuring a six-hour test with 12 questions, each scored 1 to 10 points <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. Despite the participants being highly interested in math, the median score is typically around 1 or 2, indicating its difficulty <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>. The problems tend to get harder from question 1 to 6 within each section <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>. However, the most challenging problems often have the most [[Mathematical Insights and Elegant Solutions | elegant solutions]] available, requiring a subtle shift in perspective to transform them from difficult to solvable <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>.

### The Problem
Consider the problem: If you choose four random points on a sphere, and consider the tetrahedron with these points as its vertices, what is the probability that the center of the sphere is inside that tetrahedron? <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a> This is a classic example of [[challenges_in_solving_geometric_problems | challenges in solving geometric problems]] and illustrates the power of these [[problemsolving_strategies_in_math | problem-solving strategies]].

### Applying the Strategies (2D Analogue)
To tackle the 3D problem, one would first consider a simpler 2D version: choosing three random points on a circle and finding the probability that the triangle formed contains the center of the circle <a class="yt-timestamp" data-t="01:54:10">[01:54:10]</a>.

1.  **Simplify**: Fix two points (P1, P2) and vary the third (P3) <a class="yt-timestamp" data-t="02:25:30">[02:25:30]</a>.
2.  **Observe Patterns**: Drawing lines from P1 and P2 through the circle's center divides the circle into four arcs <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>. The triangle contains the center only if P3 lands in the arc opposite P1 and P2 <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>.
3.  **Calculate Average**: The average size of this "relevant arc" is found by considering all possible angles between the lines through P1 and P2 (from 0 to 180 degrees), resulting in an average proportion of 0.25 (1/4) of the circle's circumference <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>. This suggests the probability is 1/4 <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>.
4.  **Reframe**: Instead of choosing points, choose two random lines through the center and then use coin flips to assign the points to the ends of these lines <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>. With a third point P3 also chosen randomly, there are four equally likely outcomes for P1 and P2 based on coin flips <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>. Only one of these four outcomes places P1 and P2 on the opposite side of P3 such that the triangle contains the center <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>. This confirms the 1/4 probability <a class="yt-timestamp" data-t="07:27:00">[07:27:00]</a>.

### Extending to 3D
The reframing strategy extends to the three-dimensional case <a class="yt-timestamp" data-t="07:45:00">[07:45:00]</a>. Choose three random lines through the center of the sphere and a random fourth point (P4) <a class="yt-timestamp" data-t="07:55:00">[07:55:00]</a>. For each of the three lines, flip a coin to decide which of the two endpoints will be P1, P2, and P3 <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>. This creates 2x2x2 = 8 equally likely outcomes from the coin flips <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>. In only one of these eight outcomes will P1, P2, and P3 be on the opposite side of the center as P4, forming a tetrahedron that contains the center <a class="yt-timestamp" data-t="08:18:00">[08:18:00]</a>. Therefore, the probability is 1/8. This method provides an [[Mathematical Insights and Elegant Solutions | elegant solution]] that is difficult to find through other means <a class="yt-timestamp" data-t="08:35:00">[08:35:00]</a>.

In summary, the key [[problemsolving_strategies_in_math | problem-solving strategies]] are to continually simplify the question until a foothold is found, and then, if useful constructs are introduced, to reframe the entire problem around those new constructs <a class="yt-timestamp" data-t="09:22:00">[09:22:00]</a>.