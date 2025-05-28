---
title: Micromouse robotics competition
videoId: ZMQbHMgK2rw
---

From: [[veritasium]] <br/> 

The Micromouse competition is the oldest robotics race, challenging participants to build tiny autonomous robots that can navigate a maze as quickly as possible <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The goal is simple: get to the end of the maze as fast as possible <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Competition can be extremely fierce, with races decided by as little as 20 milliseconds <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Origins of Micromouse

The concept of a maze-solving mouse dates back to 1952, when mathematician Claude Shannon constructed an electronic mouse named Theseus <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Theseus solved mazes using a computer built into the maze itself, made of telephone relay switches, and the mouse was essentially a magnet on wheels following an electromagnet <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. This system used a trial-and-error strategy, remembering correct paths to reach the goal without false turns on subsequent attempts <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Theseus is considered one of the first examples of machine learning and inspired the field of AI <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

The modern Micromouse competition began due to a misunderstanding in the mid-1970s <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. Editors at the Institute of Electrical and Electronics Engineers (IEEE) heard about a contest for "le mouse electronique," believing they were intelligent successors to Theseus <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. While the mice were merely batteries in cases, the IEEE decided to hold their own competition <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. The first "Amazing Micro-Mouse Maze Contest" announcement in 1977 attracted over 6,000 entrants <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. By the 1979 finals, the number of successful competitors dwindled to 15, but the event garnered nationwide public interest <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. The competition then spread globally <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

## Competition Rules and Maze Structure

A Micromouse must be fully autonomous, operating without internet, GPS, or remote control <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. Its computing, motors, sensors, and power supply must fit within a frame no longer or wider than 25 centimeters <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. While height is not limited, rules prohibit climbing, flight, or combustion <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

The maze is a square, approximately three meters on each side, subdivided by walls into corridors 18 centimeters across <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. In 2009, a half-size Micromouse category was introduced for mice smaller than 12.5 centimeters with paths only nine centimeters across <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. The maze layout is only revealed at the start of each competition, and competitors cannot change their mouse's code afterward <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.

Major competitions, such as All Japan, Taiwan, and USA's APEC, typically limit mice to seven or ten minutes in the maze and five runs from start to goal <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. This means extensive searching is penalized <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. The standard strategy is to use the first run to carefully learn the maze and find the best path without wasting time, then use subsequent runs to sprint along that path for the fastest possible time <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

## [[flood_fill_algorithm_and_micromouse_strategies | Micromouse Strategies and Algorithms]]

Solving a maze, especially with only a few infrared sensors for eyes, is complex <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. Early strategies included:

*   **Wall-following:** A simple approach where the mouse keeps one hand (or sensor) on a wall <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. This won the first finals, leading organizers to move the goal away from edges and add free-standing walls to defeat it <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
*   **Depth-first search:** The mouse runs as deep into the maze as it can, noting every fork, and turns back only when it hits a dead end or loop to try a different path <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>. This strategy guarantees reaching the goal but not necessarily the shortest route <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Breadth-first search:** This strategy finds the shortest path by checking every option it reaches, running down one branch to the next intersection, then backtracking to check skipped paths before moving to the next layer <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>. However, the extensive backtracking makes it time-consuming <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

The most popular strategy is the [[flood_fill_algorithm_and_micromouse_strategies | flood fill algorithm]] <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. This algorithm involves:
1.  **Optimistic Journeys:** Initially, the mouse's map has no walls, and it draws the shortest path to the goal <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
2.  **Dynamic Mapping:** When it hits an unmapped wall, it marks it down and updates its new shortest path <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
3.  **Distance Tracking:** The mouse marks the distance from every square in the maze to the goal, following decreasing numbers <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
4.  **Refinement:** The process resembles flooding the maze with water, updating values based on flow <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
5.  **Return Trip Utilization:** While not guaranteed to find the best path on the first pass, Micromice use their return trip to the start as a new journey, further searching the maze <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. This allows for efficient discovery of the shortest path, often leaving irrelevant areas untouched <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

By the end of the 1980s, some believed the problem was solved, as a clear strategy and the necessary microcontrollers and sensors became common <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>. However, the challenge evolved from finding the shortest path to finding the *fastest* path <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. In the 2017 All Japan Micromouse Competition, the winning mouse, "Red Comet," took a path 5.5 meters longer than the shortest route <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. Its search algorithm identified that this longer path had fewer turns, allowing it to be faster, winning by 131 milliseconds <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.

## [[design_and_technology_in_micromice | Design and Technology in Micromice]]: "Fosbury Flops"

The evolution of Micromouse, akin to Dick Fosbury's revolutionary high jump technique, saw two major innovations that completely changed how Micromice ran <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.

### 1. Diagonals

The first "Fosbury flop" involved a way of thinking outside the box: cutting through the box <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>. Traditionally, mice turned corners by stopping and pivoting <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>. The mouse Mitee 3 implemented diagonals for the first time, which proved to be a much better idea <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.
To achieve diagonals, the mouse chassis had to be significantly reduced in width (less than 11 cm, or 5 cm for half-size Micromouse), and its sensors and software had to adapt <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>. Maintaining a path on a diagonal is challenging, as the mouse cannot continuously see a wall, making it prone to crashing <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>. Despite the risk, diagonals transform jagged paths into narrow straightaways, and nearly every competitive Micromouse is now designed to take this risk <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>. This innovation also opened up exponential possibilities for turns, from simple U-turns to more complex, fluid motions, making the maze no longer just a grid of square hallways <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.

### 2. Vacuum Fans

The second "Fosbury flop" involved engineering an entirely new mechanism to solve the problem of control at high speeds <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>. By the early 2000s, the limiting factor for faster Micromice was not speed itself, but control of that speed, as they had to slow down during turns to avoid slipping or flipping <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a>.
The mouse Mokomo08 introduced a vacuum fan, initially considered a gimmick <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>. While flying over walls is against the rules, there's nothing preventing a mouse from vacuuming itself to the ground to increase friction and prevent slipping <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>. These fans, often built from handheld drone parts, can generate a downward force five times the mouse's weight <a class="yt-timestamp" data-t="00:20:18">[00:20:18]</a>. With this added friction, modern Micromice can turn corners with centripetal acceleration approaching six Gs, comparable to F1 cars <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a>. This increased control allowed builders to push speeds up to seven meters per second <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>.

## Continued [[impact_of_innovations_in_robotics_competitions | Innovation in Robotics Competitions]]

Beyond these "Fosbury flops," [[design_and_technology_in_micromice | design and technology in Micromice]] continues to advance:
*   **Sensors:** Tall, unwieldy arms for finding walls were replaced by smaller arrays of infrared sensors <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>.
*   **Motors:** Precise stepper motors were traded for continuous DC motors and encoders, providing more power for less size and weight <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.
*   **Gyroscopes:** Added an extra sense of orientation, like a compass, becoming more reliable for turning than counting wheel pulses <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.
*   **Wheel Design:** The first four-wheeled Micromouse won in 1988, but it took 22 more years for four-wheeled designs to become the norm <a class="yt-timestamp" data-t="00:21:43">[00:21:43]</a>. Experimentation continues with six- and eight-wheel designs, omnidirectional movement, and even computer vision <a class="yt-timestamp" data-t="00:21:57">[00:21:57]</a>.

Even with advanced hardware, keeping wheels clean is crucial, as tiny dust specs can ruin a run due to changes in friction <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>.

Micromouse is far from "solved" because it is a complex robotics problem, combining both software and hardware challenges <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. It's about navigation and speed <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>, with continuous innovation leading to smaller, faster, and lighter robots <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. The competition serves as a "perfect combination of all the major disciplines" needed for robotics and engineering, including programming and embedded systems, making it accessible for enthusiasts to engage with <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>. After nearly 50 years, the "simple problem" of a mouse solving a maze remains a reminder that "there is no such thing as a simple problem" <a class="yt-timestamp" data-t="00:23:19">[00:23:19]</a>.