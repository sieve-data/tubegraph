---
title: Inspiration and future of mazesolving robots
videoId: ZMQbHMgK2rw
---

From: [[veritasium]] <br/> 

Maze-solving robots have a rich history, beginning with early mechanical and electronic predecessors and evolving into sophisticated autonomous systems. The competition surrounding these robots has continuously pushed the boundaries of their design and algorithms, leading to ongoing innovation.

## Historical Inspiration

The concept of intelligent machines solving mazes dates back to 1952, when mathematician Claude Shannon constructed an electronic mouse named Theseus <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The intelligence of Theseus was derived from a computer built directly into the maze itself, composed of telephone relay switches <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. The mouse, essentially a magnet on wheels, followed an electromagnet controlled by these switches <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

Theseus explored the maze using a "trial and error" strategy and registered information in its memory as it found the correct path <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This allowed it to return to any explored part of the maze and go directly to the goal without false turns <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Theseus is often regarded as one of the earliest examples of machine learning and is credited with inspiring the entire field of AI <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

Twenty-five years later, in 1977, a misunderstanding about a Japanese contest for "le mouse electronique" led the Institute of Electrical and Electronics Engineers (IEEE) to launch their own "Amazing Micro-Mouse Maze Contest" <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. Although the initial "electronic mice" they heard about were merely batteries in cases, not intelligent robots <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>, the IEEE decided to create a competition for actual intelligent, autonomous maze-solving robots <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. This contest attracted over 6,000 entrants <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a> and quickly gained public interest, being broadcast nationwide by 1979 <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This marked the birth of the [[technological_innovations_in_Micromouse_design | Micromouse]] competition, which subsequently spread globally <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

## Current State and Challenges

[[technological_innovations_in_Micromouse_design | Micromouse]] robots must be fully autonomous, without external connections like internet, GPS, or remote control <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. They must contain all their computing, motors, sensors, and power supply within a 25-centimeter frame (or 12.5cm for half-size mice) <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. The maze layout is revealed only at the start of each competition, with no code changes allowed afterwards <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.

### Evolution of Mazesolving Algorithms

The [[evolution_of_mazesolving_algorithms_in_robotics | evolution of mazesolving algorithms in robotics]] has seen several stages:
*   **Wall-Following:** Early mice used a simple wall-following strategy <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. This was rendered ineffective by moving the goal away from edges and adding free-standing walls <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
*   **Depth-First Search:** This strategy involves running deep into the maze, noting forks, and turning back only at dead ends or loops <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. While it eventually finds a path, it may not be the shortest <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   **Breadth-First Search:** This algorithm finds the shortest path by checking every option at each layer of intersections <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>. However, extensive backtracking means it often takes longer than simply searching the entire maze <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   **Flood Fill:** The most popular [[evolution_of_mazesolving_algorithms_in_robotics | Micromouse]] strategy, it involves optimistic journeys through the maze, updating a map of distances to the goal as walls are encountered <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. The mouse follows decreasing numbers to zero, akin to flooding the maze with water <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. This method is efficient and often leaves irrelevant areas untouched <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

Despite these advancements, the goal is not always the shortest path, but the *fastest*. In 2017, the winning [[technological_innovations_in_Micromouse_design | Micromouse]], Red Comet, took a path 5.5 meters longer than the shortest route but won by 131 milliseconds because it had fewer turns to slow it down <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. This highlights that [[technological_innovations_in_Micromouse_design | Micromouse]] is a robotics problem, where the interaction between software (brain) and hardware (body) is key <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.

### Technological Innovations

Significant "Fosbury flops"—innovations that completely changed how [[technological_innovations_in_Micromouse_design | Micromice]] ran—have occurred:
*   **Diagonals:** The mouse Mitee 3 first implemented diagonal movement, which transformed jagged paths into straightaways <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. This required smaller chassis designs (less than 11cm wide) and new algorithms to navigate without constant wall feedback <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>. Today, nearly every competitive [[technological_innovations_in_Micromouse_design | Micromouse]] uses diagonals <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>.
*   **Sweeping Turns:** Instead of stopping and pivoting, mice began using single U-turn motions, contributing to a more fluid, snaking motion through the maze <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>.
*   **Hardware Upgrades:**
    *   Early tall arms for wall finding were replaced by arrays of infrared sensors <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>.
    *   Precise stepper motors were exchanged for continuous DC motors with encoders, offering more power in a smaller, lighter package <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.
    *   Gyroscopes, thanks to mobile phone technology, provide crucial orientation sensing, making turns more reliable than wheel pulse counting <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.
*   **Vacuum Fans:** A key innovation for control at high speeds, vacuum fans, often built from handheld drone parts, generate a downward force up to five times the mouse's weight <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>. This greatly increases friction, allowing mice to turn corners with centripetal acceleration approaching six Gs, comparable to F1 cars <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a>. This increased control enabled builders to push speed limits, with mice zipping along at up to seven meters per second <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>.

### The Future of [[technological_innovations_in_Micromouse_design | Micromouse]]

The [[challenges_and_strategies_in_robotics_competitions | challenges and strategies in robotics competitions]] remain dynamic. [[technological_innovations_in_Micromouse_design | Micromouse]] is far from a "solved problem" <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. Every standard feature today was once an experiment <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>. Ongoing experimentation includes:
*   Six- and eight-wheel designs <a class="yt-timestamp" data-t="00:21:57">[00:21:57]</a>.
*   Omnidirectional movement <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>.
*   Computer vision <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>.

The competition continues to drive innovation in robotics, combining major disciplines like engineering, programming, and embedded systems <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>. Nearly 50 years after its inception, [[technological_innovations_in_Micromouse_design | Micromouse]] remains a vibrant field, reminding us that even a "simple problem" can lead to complex and continuous advancements <a class="yt-timestamp" data-t="00:23:19">[00:23:19]</a>.