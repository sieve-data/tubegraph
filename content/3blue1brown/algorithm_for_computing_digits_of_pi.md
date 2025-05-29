---
title: Algorithm for computing digits of pi
videoId: HEfHFsfGXjs
---

From: [[3blue1brown]] <br/> 

Sometimes, mathematical and physical phenomena converge in unexpectedly elegant ways <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. One such phenomenon involves a seemingly simple setup of colliding blocks that, remarkably, yields the digits of [[colliding_blocks_computing_pi | pi]] <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

## The Colliding Blocks Setup
The experiment involves two sliding blocks and a wall <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.
*   The first block approaches from the right with a certain velocity <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.
*   The second block begins stationary <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   Idealistic physics assumptions are applied: no friction and all collisions are perfectly elastic, meaning no energy is lost <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

The goal is to count the total number of collisions <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Collision Counts and the Emergence of Pi
The number of collisions observed depends on the mass ratio between the two blocks.

*   **Equal Masses (1:1)**: If both blocks have the same mass, there are a total of 3 collisions <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a> <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
    1.  The first block hits the second, transferring all momentum <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
    2.  The second block bounces off the wall <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
    3.  The second block transfers all its momentum back to the first, which then slides away <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

*   **Mass Ratio of 100:1**: If the first block is 100 times the mass of the second, the smaller block repeatedly bounces between the wall and the larger block <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a> <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This process gradually redirects the larger block's momentum <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. In this scenario, there are 31 total collisions <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

*   **Mass Ratio of 10,000:1**: With the first block 10,000 times heavier, the number of collisions increases significantly to 314 <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a> <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

*   **Mass Ratio of 1,000,000:1**: When the first block is 1,000,000 times heavier, the total number of collisions observed is 3,141 <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a> <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

### The Pattern
When the mass of the first block is a power of 100 times the mass of the second block (e.g., 100, 10,000, 1,000,000), the total number of collisions corresponds to the digits of [[colliding_blocks_computing_pi | pi]] <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a> <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

This surprising fact was discovered by mathematician Gregory Galperin in 1995 and published in 2003 <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a> <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

## An Algorithm for Computing Pi (in Theory)
This physical setup can be conceptualized as an algorithm for calculating the digits of [[colliding_blocks_computing_pi | pi]] <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>:

1.  **Implement a physics engine** capable of simulating elastic collisions <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
2.  **Choose the desired number of digits** `d` of [[colliding_blocks_computing_pi | pi]] <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
3.  **Set Block Masses and Initial Conditions**:
    *   Mass of the first block: $100^{(d-1)}$ <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
    *   Mass of the second block: 1 (e.g., 1 kilogram) <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
    *   Send the first block traveling on a frictionless surface towards the second stationary block <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
4.  **Count all collisions** that occur <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

### Impracticality
While elegant, this algorithm is comically inefficient and impractical for actual [[colliding_blocks_computing_pi | pi]] computation <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

*   **Extreme Mass Ratios**: To compute just 20 digits of [[colliding_blocks_computing_pi | pi]], one block would need to be $100^{19}$ (100 billion billion billion billion) times the mass of the other <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a> <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. If the smaller block were 1 kg, the larger block would be approximately 10 times the mass of the supermassive black hole at the center of the Milky Way <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a> <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   **Astronomical Collision Counts**: Calculating 20 digits would require counting 31 billion billion collisions <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Impossible Frequencies**: At one point, the frequency of collisions could reach around 100 billion billion billion billion clacks per second <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a> <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. This demands extremely high numerical precision and an exceedingly long computation time <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Over-Idealization**: The process departs significantly from anything possible in real-world physics <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

## The Underlying Mystery
The profound question raised by this phenomenon is why [[colliding_blocks_computing_pi | pi]], typically associated with continuous geometric properties like circles and curves, appears in the discrete count of collisions in a linear system <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a> <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. The explanation lies in a "hidden circle" derived from the principle of conservation of energy within the system <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a> <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. The detailed physical and mathematical explanation is explored in subsequent discussions <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a> <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.