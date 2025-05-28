---
title: Micromouse competition history and rules
videoId: ZMQbHMgK2rw
---

From: [[veritasium]] <br/> 

Micromouse is the oldest robotics race, challenging tiny autonomous robots to navigate and solve mazes as fast as possible <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The competition is fierce, with outcomes often decided by milliseconds <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a> <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## Origins

The concept of intelligent maze-solving robots was inspired by Claude Shannon's electronic mouse, Theseus, constructed in 1952 <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Theseus could solve a maze using a computer built into the maze itself, made of telephone relay switches <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. The mouse itself was essentially a magnet on wheels, guided by an electromagnet controlled by the relay switches <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. Theseus would explore the maze using a trial-and-error strategy, registering information in its memory as it found the correct path <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. Once a path was explored, the mouse could go directly to the goal without false turns <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Theseus is often regarded as one of the first examples of machine learning and inspired the field of AI <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a> <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. For more on this, see [[Inspiration and future of mazesolving robots]].

The official Micromouse competition began due to a misunderstanding <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. Around 1977, editors at the Institute of Electrical and Electronics Engineers (IEEE) heard of a contest for "le mouse electronique" and believed these were successors to Theseus <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a> <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. It turned out these "mice" were merely batteries in cases, not intelligent robots <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. Despite the confusion, the idea stuck, leading IEEE to hold their own competition <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a> <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

## Competition History and Spread

The first "Amazing Micro-Mouse Maze Contest" announcement in 1977 attracted over 6,000 entrants <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. However, the number of successful competitors quickly dwindled, with only 15 reaching the finals in 1979 <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a> <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. By then, the contest had gained national interest and was broadcast on the evening news <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. Micromouse soon spread globally <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

## Rules and Maze Environment

Micromice must be fully autonomous, with no internet, GPS, or remote control <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. They cannot be nudged or helped if stuck <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. All computing, motors, sensors, and power supply must fit within a frame no longer or wider than 25 centimeters <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. While there's no height limit, rules prohibit climbing, flight, or combustion <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

The maze itself is typically a square about three meters on each side, divided by walls into corridors 18 centimeters wide <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. In 2009, a half-size Micromouse category was introduced for mice smaller than 12.5 centimeters per side, navigating paths just nine centimeters across <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

The final maze layout is only revealed at the start of each competition, and competitors are not allowed to change their mouse's code afterward <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. Major competitions like All Japan, Taiwan, and USA's APEC usually limit a mouse's time in the maze to 7 or 10 minutes and allow only five runs from start to goal <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

## Maze-Solving Strategies and Their Evolution

Early Micromouse competitors utilized simple strategies like wall-following, which was successful until the maze rules were updated to move the goal away from edges and add free-standing walls, making such a strategy ineffective <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a> <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

Other common search algorithms included:
*   **Depth-first search**: The mouse runs as deep into the maze as possible, turning back only when it hits a dead end <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. This strategy guarantees reaching the goal but doesn't necessarily find the shortest route <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
*   **Breadth-first search**: The mouse checks every branch of an intersection layer by layer, backtracking to explore skipped paths <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>. While it finds the shortest path, extensive backtracking often makes it slower than searching the entire maze <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

The most popular and efficient strategy for Micromouse is the **flood fill algorithm** <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. This approach involves:
1.  Initially, the mouse operates with an "optimistic" map, assuming no walls and drawing the shortest path to the goal <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
2.  When the mouse encounters an actual wall, it updates its internal map and recalculates the new shortest path <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
3.  Under the hood, the mouse marks the distance from every square to the goal and follows decreasing numbers <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. This resembles water flooding the maze, hence the name <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
4.  Although not guaranteed to find the best path on the first try, flood fill takes advantage of the rule that mice must return to the start for subsequent runs <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. By treating the return trip as another search, the mouse can efficiently discover the shortest path, often leaving irrelevant maze areas untouched <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. For more on this, see [[Evolution of mazesolving algorithms in robotics]].

Initially, some believed the problem was "solved" once a clear strategy like flood fill emerged <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>. However, the objective shifted from finding the *shortest path* to finding the *fastest path* <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. This was famously demonstrated by Masakazu Utsunomiya's Red Comet in 2017, which won by taking a path 5.5 meters longer than the shortest route but had fewer turns, making it faster overall <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a> <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. This highlights the continuous [[challenges_and_strategies_in_robotics_competitions|challenges and strategies in robotics competitions]].

## Major Innovations: "Fosbury Flops" in Micromouse

Just like the high jump's "Fosbury Flop" revolutionized the sport by changing the approach, Micromouse has seen two fundamental innovations that dramatically altered competition <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a> <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>. These demonstrate the ongoing [[Technological innovations in Micromouse design]].

### 1. Diagonal Movement

One of the earliest "Fosbury Flops" was the introduction of diagonal movement by the mouse Mitee 3 <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. Traditionally, mice would navigate by making sharp 90-degree turns <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>. Mitee 3 demonstrated that cutting diagonally through grid cells could be much faster, despite being a longer path, by reducing the number of slowdowns for turns <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>.

Implementing diagonals required significant changes:
*   **Chassis size**: Mice had to be reduced to less than 11 centimeters wide (5 cm for half-size) to fit <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>.
*   **Sensors and Software**: A new algorithm was needed, as the traditional method of maintaining equal distance from parallel walls was no longer applicable <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>. Diagonal movement is also more prone to crashes due to the difficulty of maintaining precise alignment <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.

Diagonals, along with sweeping U-turns, exponentially increased the number of possible paths and made figuring out the best route far more complex <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.

### 2. Vacuum Fan for Increased Friction

For decades, the biggest physical challenge for Micromice was maintaining control at high speeds, especially during turns <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>. Like race cars, mice rely on friction for centripetal force <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>. To avoid slipping or flipping, mice had to lower their center of gravity and slow down for turns <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>.

The second "Fosbury Flop" addressed this: the use of a vacuum fan <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>. First widely adopted by the mouse Mokomo08, this innovation involves a propeller that spins to create a downward force, effectively "vacuuming" the mouse to the ground <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a> <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>. While flying over walls is against the rules, creating downforce is not <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>. At the Micromouse scale, a fan built from handheld drone parts can generate a downward force five times the mouse's weight <a class="yt-timestamp" data-t="00:20:18">[00:20:18]</a>. This allows Micromice to turn corners with centripetal acceleration approaching six Gs, comparable to F1 cars <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a>. With this added control, builders could push the speed limits, with mice now reaching speeds of up to seven meters per second <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>.

## Technological Advancements

Beyond these "Fosbury Flops," [[Technological innovations in Micromouse design]] have consistently improved the robots:
*   **Sensors**: Tall, unwieldy arms for wall detection were replaced by smaller arrays of infrared sensors <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>. Gyroscopes, derived from mobile phone technology, added precise orientation sensing, making turning more reliable than relying on wheel pulse counts <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.
*   **Motors**: Precise stepper motors were superseded by continuous DC motors and encoders, offering more power for less size and weight <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.
*   **Friction Management**: Competitors are often seen with tape to clean dust off wheels between rounds, as tiny changes in friction can ruin a run at these speeds <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>.
*   **Wheel Designs**: While four-wheeled Micromice became the norm after 22 years of experimentation following the first win in 1988, current designs still experiment with six- and eight-wheel configurations, omnidirectional movement, and even computer vision <a class="yt-timestamp" data-t="00:21:43">[00:21:43]</a> <a class="yt-timestamp" data-t="00:21:57">[00:21:57]</a>.

## Current State and Accessibility

Micromouse remains far from a "solved" problem because it is a complex robotics challenge involving both software and hardware <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. Innovation continues, with robots getting smaller, faster, and lighter <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. Despite its complexity, Micromouse is considered an accessible combination of major disciplines like robotics, engineering, programming, and embedded systems, which can be pursued without a specialized laboratory <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>.