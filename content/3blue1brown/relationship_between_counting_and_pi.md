---
title: Relationship between counting and pi
videoId: HEfHFsfGXjs
---

From: [[3blue1brown]] <br/> 

Sometimes, mathematics and physics unexpectedly align in profound ways <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. A peculiar experiment involving colliding blocks reveals an astonishing connection between discrete collision counts and the continuous digits of pi.

## The Colliding Blocks Experiment

The setup for this thought experiment involves two sliding blocks and a wall <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. One block starts moving from the right, while the second block remains stationary <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. Key assumptions for this idealized physics scenario include no friction and perfectly elastic collisions, meaning no energy is lost <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. The objective is to count the total number of collisions <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

Let's observe the collision counts for different mass ratios between the two blocks:

*   **Equal Mass:** If both blocks have the same mass, the first block hits the second, transferring all its momentum <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. The second block then bounces off the wall, transferring momentum back to the first block, which then slides away <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This results in 3 total collisions <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

*   **Mass Ratio 100:1:** If the first block is 100 times the mass of the second one <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>, the smaller block will repeatedly bounce between the wall and the larger block <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This process gradually redirects the larger block's momentum <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>, resulting in 31 total collisions before both blocks move away indefinitely <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

*   **Mass Ratio 10,000:1:** When the first block is 10,000 times the mass of the second <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>, the number of collisions dramatically increases <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. The total count becomes 314 collisions <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

*   **Mass Ratio 1,000,000:1:** With the first block being 1,000,000 times the mass of the other, the total number of collisions reaches 3,141 <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>, <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

### The Emerging Pattern
A remarkable pattern emerges: when the mass of the first block is a power of 100 times the mass of the second block, the total number of collisions corresponds to the digits of [[pi_and_its_formulas_involving_primes | pi]] <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>, <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

## Discovery and Its Implications

This counter-intuitive fact was introduced by viewer Henry Cavill <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a> and was originally discovered by mathematician [[gregory_galperins_discovery_and_pi_puzzles | Gregory Galperin]] in 1995, with findings published in 2003 <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>, <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

This phenomenon highlights a unique [[algorithm_for_computing_pi_using_physics | algorithm for computing pi using physics]] <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>, which is both elegant and comically inefficient <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. The conceptual steps for this algorithm are:

1.  Implement a physics engine <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
2.  Choose the desired number of digits *d* of pi to compute <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
3.  Set the mass of one block to be 100<sup>(d-1)</sup> times the mass of the second block (e.g., 1 unit of mass) <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Send the larger block towards the smaller one on a frictionless surface <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
4.  Count all the collisions <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

To illustrate its impracticality, calculating just 20 digits of pi would require one block to have a mass 100 billion billion billion billion times that of the other <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>, <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. If the smaller block weighed 1 kilogram, the larger block's mass would be approximately 10 times that of the supermassive black hole at the center of the Milky Way <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. This would necessitate counting 31 billion billion collisions <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>, with collision frequencies reaching around 100 billion billion billion billion clacks per second at one point <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>, <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. Such a process would demand extremely high numerical precision and an immense amount of time to complete accurately <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>, <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

It's crucial to remember that this process is highly idealized and deviates significantly from what could occur in real-world physics <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

## The Hidden Circle and the Mystery of Pi

The true intrigue of this problem lies not in its utility as a pi-computing algorithm or a practical physics demonstration <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. Instead, it's mind-boggling because of the unexpected appearance of [[pis_relationship_to_circles_and_geometry | pi]] <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. Pi's decimal digits are appearing in a counting context, which is unusual, as pi typically describes continuous phenomena <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>, <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

The explanation for this connection lies in a hidden circle that arises from the conservation of energy <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>, <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. The full explanation of how this [[colliding_blocks_and_pi_computation | colliding blocks and pi computation]] works, involving two distinct methods, will be explored in a subsequent discussion <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. The problem is a challenging puzzle, encouraging collaborative thinking <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.