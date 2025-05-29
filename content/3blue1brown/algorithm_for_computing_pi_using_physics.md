---
title: Algorithm for computing pi using physics
videoId: HEfHFsfGXjs
---

From: [[3blue1brown]] <br/> 

Mathematics and physics can sometimes align in unexpectedly profound ways <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. One such instance involves a system of colliding blocks that astonishingly computes the digits of [[rational_approximations_for_pi | pi]] <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

## The Setup

The setup involves two sliding blocks and a wall <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.
*   One block starts by moving from the right with a certain velocity <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.
*   The second block begins stationary <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

For this "mathematical croquet" to work, ideal physics conditions are assumed <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>:
*   No friction <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.
*   All collisions are perfectly elastic, meaning no energy is lost <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

The objective is to count the total number of collisions <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Collision Counts and Pi's Digits

The number of collisions observed in this system directly relates to the digits of [[rational_approximations_for_pi | pi]], depending on the mass ratio of the blocks <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

*   **Equal Mass (1:1 ratio):** If both blocks have the same mass, the first block transfers all its momentum to the second, which then bounces off the wall and transfers momentum back to the first. This results in **3 total collisions** <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a> <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   **Mass Ratio 100:1:** If the first block is 100 times the mass of the second, the smaller block repeatedly bounces between the wall and the larger block <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This process redirects the larger block's momentum <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. There will be **31 collisions** before both blocks slide away <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Mass Ratio 10,000:1 (100^2):** If the first block is 10,000 times the mass of the second, the total number of collisions increases to **314** <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a> <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a> <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   **Mass Ratio 1,000,000:1 (100^3):** With the first block being 1,000,000 times the mass of the second, the system yields **3,141 collisions** <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a> <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

When the mass of the first block is a power of 100 times the mass of the second, the total number of collisions directly corresponds to the digits of [[rational_approximations_for_pi | pi]] <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a> <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. This phenomenon is surprising because [[relationship_between_counting_and_pi | pi]]'s digits are here counting discrete events rather than describing something continuous <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a> <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

## Origin of the Discovery

This unusual property was first discovered by mathematician [[gregory_galperins_discovery_and_pi_puzzles | Gregory Galperin]] in 1995 and was subsequently published in 2003 <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a> <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

## The Impractical "Algorithm"

While fascinating, this method is considered "comically inefficient" as an algorithm for computing [[rational_approximations_for_pi | pi]] <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>:

1.  **Implement a physics engine** <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
2.  **Choose the number of digits** `d` of [[rational_approximations_for_pi | pi]] desired <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
3.  **Set block masses:** One block's mass is `100^(d-1)` times the mass of the other (e.g., 1 unit of mass) <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
4.  **Count all collisions** <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

### Practical Limitations
*   **Extreme Mass Ratios:** To calculate just 20 digits of [[rational_approximations_for_pi | pi]], one block would need to be `100^19` (100 billion billion billion billion) times the mass of the other <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a> <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. If the smaller block was 1 kg, the larger block's mass would exceed 10 times that of the supermassive black hole at the center of the Milky Way <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Immense Collision Counts:** Calculating 20 digits would require counting 31 billion billion collisions <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **High Frequency:** At certain points, the collision frequency could reach 100 billion billion billion billion clacks per second <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a> <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **Numerical Precision:** Achieving accuracy would demand extremely high numerical precision from the physics simulation <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Idealized Conditions:** The process is highly idealized, quickly diverging from anything physically possible in reality <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a> <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

## The Underlying Mathematics

The appearance of [[rational_approximations_for_pi | pi]] in this discrete counting problem is "mind-boggling" <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a> <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. The key to understanding it lies in the presence of a "hidden circle" derived from the conservation of energy within the system <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a> <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. The detailed explanation involves surprising mathematical methods <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a> <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.