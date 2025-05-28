---
title: The BanachTarski Paradox
videoId: _cr46G2K5Fo
---

From: [[veritasium]] <br/> 

The [[the_axiom_of_choice_and_its_implications | Axiom of Choice]], when applied, leads to some deeply counterintuitive results, one of the most famous being the Banach-Tarski Paradox <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>. This paradox demonstrates that it's theoretically possible to take a single solid ball, split it into just five pieces, and then, by carefully rotating and moving those pieces, reassemble them into two balls, each identical to the one started with <a class="yt-timestamp" data-t="00:23:27">[00:23:27]</a>. This process can be repeated, theoretically leading to an infinite number of balls from a single original one <a class="yt-timestamp" data-t="00:23:41">[00:23:41]</a>.

> "The axiom of choice is something that's so obviously true and it's consequences are so obviously false that you're like, what the hell is going on?" <a class="yt-timestamp" data-t="00:27:53">[00:27:53]</a>

## How it Works: A Graph Analogy

To understand how the Banach-Tarski Paradox works, one can visualize it using an infinitely branching graph <a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>.

1.  **Movement Rules**: Imagine a starting point where you can move in four directions: up, down, left, and right <a class="yt-timestamp" data-t="00:23:56">[00:23:56]</a>.
2.  **Restriction**: The only rule is that you cannot immediately reverse a move <a class="yt-timestamp" data-t="00:24:10">[00:24:10]</a>.
3.  **Scaling**: Each new line drawn is half the size of the previous one, ensuring the graph fits on the screen <a class="yt-timestamp" data-t="00:24:17">[00:24:17]</a>.
4.  **Resulting Graph**: Continuously repeating this process creates an infinitely branching graph <a class="yt-timestamp" data-t="00:24:23">[00:24:23]</a>.
5.  **Sections**: This graph can be broken down into five sections: the middle starting section and four other sections that are all identical but rotated <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>.
6.  **Duplication**: By shifting one of these sections (e.g., the left section to the right) and adding back the single missing section, the entire original graph is recreated <a class="yt-timestamp" data-t="00:24:39">[00:24:39]</a>. This can also be done in a completely different way, such as moving the bottom section up <a class="yt-timestamp" data-t="00:24:57">[00:24:57]</a>. This demonstrates how one graph can be split, shifted, and end up as two identical copies <a class="yt-timestamp" data-t="00:25:18">[00:25:18]</a>.

### Applying to a Ball

Banach and Tarski applied this same logic to a solid ball <a class="yt-timestamp" data-t="00:25:30">[00:25:30]</a>:

1.  **Rotations**: Similar to the graph, there are four rotational "moves" possible (up, down, left, or right) <a class="yt-timestamp" data-t="00:25:37">[00:25:37]</a>.
2.  **Rule**: The rule against immediately reversing a move still applies <a class="yt-timestamp" data-t="00:25:41">[00:25:41]</a>.
3.  **Irrational Rotation**: To ensure no return to the same point, every rotation is by the same irrational portion of a circle <a class="yt-timestamp" data-t="00:25:45">[00:25:45]</a>.
4.  **Point Coloring**: A random starting point is picked and marked, and then the ball is rotated, coloring each point based on the direction of rotation used to reach it <a class="yt-timestamp" data-t="00:25:52">[00:25:52]</a>.
5.  **Countable Points**: Performing this infinitely results in a countably infinite collection of points <a class="yt-timestamp" data-t="00:26:04">[00:26:04]</a>.
6.  **Uncountable Surface**: However, the surface of a ball has uncountably infinite points, similar to the real number line <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>.
7.  **Role of the [[the_axiom_of_choice_and_its_implications | Axiom of Choice]]**: Since there are uncountably infinite possible starting points and the goal is to avoid already colored points, the [[the_axiom_of_choice_and_its_implications | Axiom of Choice]] is used to choose unique starting points, even though the exact method of choosing cannot be specified <a class="yt-timestamp" data-t="00:26:29">[00:26:29]</a>.
8.  **Five Groups**: Once every point on the ball is "colored," the points are split into five groups: one for the starting points and four others based on the final rotation used to arrive at those points <a class="yt-timestamp" data-t="00:26:49">[00:26:49]</a>.
9.  **Reassembly**: These groups are then treated like the sections of the graph. For example, the group of points ending with a left rotation can be rotated to the right, and by adding the group that ends with a right rotation, the original ball is recreated <a class="yt-timestamp" data-t="00:27:04">[00:27:04]</a>. This can be done a second time, resulting in two identical balls <a class="yt-timestamp" data-t="00:27:30">[00:27:30]</a>.

## Implications and Nature of the Paradox

While this infinite duplication is theoretically possible, the pieces the ball is split into are not simple shapes <a class="yt-timestamp" data-t="00:28:02">[00:28:02]</a>. They are what are known as "non-measurable" sets, similar to the Vitali set <a class="yt-timestamp" data-t="00:28:09">[00:28:09]</a>. Although the original and duplicated balls have a volume, the intermediate step violates our understanding of size <a class="yt-timestamp" data-t="00:28:14">[00:28:14]</a>. This is the mechanism by which the paradox arises <a class="yt-timestamp" data-t="00:28:22">[00:28:22]</a>.

> "Of course, those are not physically plausible cuts, but like there's a more meta physical question like, should this even remotely be possible if we could make such cuts? And the answer to almost every human I know is absolutely not." <a class="yt-timestamp" data-t="00:28:26">[00:28:26]</a>

The Banach-Tarski Paradox, along with other "disturbing results" caused by the [[the_axiom_of_choice_and_its_implications | Axiom of Choice]], led to a crisis in mathematics for over 30 years <a class="yt-timestamp" data-t="00:29:20">[00:29:20]</a>. It highlights that the [[the_axiom_of_choice_and_its_implications | Axiom of Choice]] cannot be proven or disproven from other axioms of set theory, meaning its inclusion or exclusion depends on the mathematical system one chooses to work within <a class="yt-timestamp" data-t="00:30:38">[00:30:38]</a>.