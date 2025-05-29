---
title: Counting puzzle involving pi
videoId: HEfHFsfGXjs
---

From: [[3blue1brown]] <br/> 

Sometimes, mathematics and physics align in surprising ways that defy expectation <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. A peculiar counting puzzle demonstrates a deep connection between the number of collisions in a simple physical system and the digits of pi <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

## The Puzzle Setup

The puzzle involves a system of two sliding blocks and a wall <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.
*   One block starts by moving from the right with a certain velocity <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.
*   The second block begins stationary <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   Crucially, the system assumes ideal conditions: no friction, and all collisions are perfectly elastic, meaning no energy is lost <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

The objective of the [[puzzles_and_geometric_problemsolving | puzzle]] is to count the total number of collisions that occur between the blocks and the wall <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## The Unexpected Pattern

The number of collisions changes based on the mass ratio of the two blocks:

*   **Equal Masses**: If both blocks have the same mass, the first block hits the second, transferring all its momentum. The second block then bounces off the wall and transfers its momentum back to the first. This results in **3 total collisions** <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
*   **Mass Ratio of 100:1**: When the first block is 100 times the mass of the second, the smaller block repeatedly bounces between the wall and the larger block <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. This process slowly redirects the larger block's momentum <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. The total number of collisions is **31** <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Mass Ratio of 10,000:1**: With the first block 10,000 times heavier than the second, the collisions sum up to **314** <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   **Mass Ratio of 1,000,000:1**: If the mass ratio is 1,000,000 to 1, the total number of collisions is **3,141** <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

This surprising pattern reveals that when the mass of the first block is a power of 100 times the mass of the second block (specifically, $100^{d-1}$), the total number of collisions yields the first $d$ digits of pi <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

## Discovery

This remarkable phenomenon was discovered by mathematician Gregory Galperin in 1995 and later published in 2003 <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

## A Comically Inefficient Algorithm for Pi

The [[colliding_blocks_computing_pi | phenomenon]] can be conceptualized as an [[algorithm_for_computing_digits_of_pi | algorithm for computing digits of pi]], albeit an extremely impractical one <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

The steps would be:
1.  Implement a physics engine <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
2.  Choose the desired number of digits, $d$, for pi <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
3.  Set the mass of one block to $100^{d-1}$ times the mass of the other, and send it sliding on a frictionless surface <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
4.  Count all the collisions <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

This theoretical [[algorithm_for_computing_digits_of_pi | algorithm]] is wildly inefficient:
*   To compute just 20 digits of pi, one block would need to be $10^{38}$ times the mass of the other <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. If the small block is 1 kilogram, the larger block would have a mass about 10 times that of the supermassive black hole at the center of the Milky Way <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   This would require counting 31 billion billion collisions <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   At one point, the collision frequency could reach around $10^{38}$ clacks per second <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
*   The entire process relies on highly idealized physics, far removed from real-world possibilities <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

## The Hidden Connection

The puzzle's intrigue lies not in its practicality, but in why pi appears in such a discrete counting problem, especially when its value usually describes continuous phenomena <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. The key to understanding this lies in recognizing a [[geometric_intuition_of_pi | hidden circle]] within the system, which arises from the conservation of energy <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

This [[puzzles_and_geometric_problemsolving | puzzle]] presents a challenging problem, encouraging engagement and collaboration <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.