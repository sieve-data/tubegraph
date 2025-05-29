---
title: P versus NP problem
videoId: KllCrlfLuzs
---

From: [[lexfridman]] <br/> 

The P versus NP problem is one of the most central questions in theoretical computer science and involves the classes of problems denoted by P and NP. In simple terms, it asks whether every problem for which a solution can be verified quickly (in polynomial time) can also be solved quickly (also in polynomial time) <a class="yt-timestamp" data-t="00:50:30">[00:50:30]</a>.

## Definitions

- **P (Polynomial Time)**: This class consists of decision problems (problems with a yes/no answer) for which a solution can be determined in polynomial time relative to the size of the input <a class="yt-timestamp" data-t="00:44:02">[00:44:02]</a>.
  
- **NP (Nondeterministic Polynomial Time)**: This class consists of decision problems for which, given a solution, the correctness of the solution can be checked in polynomial time. These problems might not be solvable in polynomial time, but their solutions are verifiable <a class="yt-timestamp" data-t="00:45:10">[00:45:10]</a>.

- **NP-Complete**: These are problems that are both in NP and as hard as any problem in NP. The class contains the hardest problems in NP, such that if any NP-complete problem can be solved quickly, every problem in NP can be <a class="yt-timestamp" data-t="00:51:03">[00:51:03]</a>.

## The Famous Question: P = NP?

The question of whether P equals NP is whether every problem for which a solution can be verified in polynomial time can also be solved in polynomial time <a class="yt-timestamp" data-t="00:50:30">[00:50:30]</a>. The implications of resolving this question are profound:
- If P = NP, problems that currently seem unsolvable in a reasonable time frame would suddenly become efficiently solvable <a class="yt-timestamp" data-t="01:11:16">[01:11:16]</a>.
- If P ≠ NP, it confirms that some problems truly require time that grows faster than any polynomial in the size of the input <a class="yt-timestamp" data-t="00:51:01">[00:51:01]</a>.

## Key Insights and Historical Context

Richard Karp's landmark paper "Reducibility Among Combinatorial Problems" identified 21 NP-complete problems, demonstrating the pervasiveness and interconnectivity of NP-complete problems. This was a significant catalyst in the study of [[p_vs_np_problem_in_theoretical_computer_science | P versus NP]] <a class="yt-timestamp" data-t="01:00:27">[01:00:27]</a>.

Stephen Cook demonstrated that the satisfiability problem is as hard as any problem in NP, establishing the concept of NP-completeness <a class="yt-timestamp" data-t="01:00:39">[01:00:39]</a>.

## Impact and Current Views

The consensus among computer scientists is that P is not equal to NP. Many problems that fit into NP have been extensively studied without finding polynomial-time solutions. For instance, factoring large integers remains an NP problem despite centuries of investigation <a class="yt-timestamp" data-t="00:51:11">[00:51:11]</a>.

Theoretical computer science continues to explore the ramifications of this problem, developing more sophisticated heuristics and approximation algorithms to tackle NP-complete problems when exact polynomial-time solutions are unreachable <a class="yt-timestamp" data-t="01:12:11">[01:12:11]</a>.

> [!info] Geeks and Computational Elegance
>
> According to Don Knuth, some derive great aesthetic pleasure from contemplating computational processes. Such people are often engrossed by the artistry of how algorithms operate, exemplified by the numerous contributions of researchers like Richard Karp <a class="yt-timestamp" data-t="01:09:41">[01:09:41]</a>.

In conclusion, the P versus NP problem remains a fundamental open question in computer science, shaping our understanding of what can be computed efficiently and inspiring ongoing research and innovation in computational theory.