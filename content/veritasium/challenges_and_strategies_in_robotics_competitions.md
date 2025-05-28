---
title: Challenges and strategies in robotics competitions
videoId: ZMQbHMgK2rw
---

From: [[veritasium]] <br/> 

The Micromouse competition is recognized as the oldest robotics race globally <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Its core objective is straightforward: navigate a maze as quickly as possible <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. The competition is incredibly intense, with winners sometimes decided by mere milliseconds <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Origins and Evolution

The concept of autonomous maze-solving robots was inspired by Claude Shannon's electronic mouse, Theseus, built in 1952 <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Theseus could solve a maze through a process of trial and error, registering information in its memory, which is often considered one of the earliest examples of machine learning and inspired the field of AI <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a><a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a><a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

In 1977, a misunderstanding about "electronic mice" led the IEEE to announce their "Amazing Micro-Mouse Maze Contest" <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a><a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. Initially attracting over 6,000 entrants, the number of successful competitors rapidly dwindled, but the contest gained significant public interest, even being broadcast on national news by 1979 <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a><a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a><a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. From there, Micromouse spread globally <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

## Competition Rules and Design Constraints

Micromice must operate as fully autonomous robots, without external connections like the internet, GPS, or remote control, and no human intervention for assistance <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. They must contain all their computing, motors, sensors, and power supply within a frame no longer or wider than 25 centimeters <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a><a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Climbing, flying, or any form of combustion propulsion (like rockets) are prohibited <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a><a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

The maze itself is typically a three-meter square subdivided into corridors 18 centimeters wide <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a><a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. A half-size category introduced in 2009 features mice smaller than 12.5 centimeters with 9-centimeter wide paths <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a><a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. The maze layout is only revealed at the start of each competition, and competitors cannot modify their mouse's code afterward <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a><a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. Mice are usually allowed 7 to 10 minutes and five runs to complete the maze from start to goal <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a><a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

## Evolution of Strategies and Algorithms

Micromice, with only a few infrared sensors for vision, have a very limited view from inside the maze <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. The [[Evolution of mazesolving algorithms in robotics | strategies]] have evolved significantly:

### Early Approaches

*   **Wall-Following:** Initially, a simple wall-following strategy, where the mouse keeps one hand (or sensor) on a single wall, proved effective in the first finals <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a><a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. However, maze designs were quickly updated to move the goal away from edges and add free-standing walls, rendering this approach ineffective <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
*   **Depth-First Search:** This strategy involves running as deep into the maze as possible, noting every fork, and turning back only when a dead end or loop is encountered <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a><a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. While it guarantees reaching the goal, it doesn't necessarily find the shortest route <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   **Breadth-First Search:** This algorithm guarantees finding the shortest path by systematically checking every option at each layer of intersections <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a><a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. However, the extensive backtracking required means rerunning paths multiple times, which can be time-consuming <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

### The Flood Fill Algorithm

The most popular and intelligent strategy for Micromice is the **Flood Fill algorithm** <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a><a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. This approach involves:
1.  **Optimistic Initial Journey:** The mouse begins by assuming no walls exist and plots the shortest possible path to the goal <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a><a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
2.  **Dynamic Mapping:** When an actual wall is encountered, the mouse marks it on its internal map and recalculates the new shortest path <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a><a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
3.  **Distance-Based Navigation:** Under the hood, the mouse assigns a "distance to goal" value to every square in the maze and always travels towards squares with decreasing numbers <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a><a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. This process resembles "flooding the maze with water" <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
4.  **Optimized Runs:** While not guaranteed to find the absolute shortest path on the first pass, the algorithm leverages the fact that mice must return to the start for subsequent runs <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a><a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. The return trip can also be used to explore and refine the map, making it highly likely to find the optimal path efficiently over two attempts <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a><a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

## Beyond the Shortest Path: The Fastest Path

Despite the sophistication of algorithms like Flood Fill, Micromouse competitions are not about finding the shortest path, but the *fastest* path <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>. In 2017, Masakazu Utsunomiya's "Red Comet" won the All Japan Micromouse Competition by taking a path 5.5 meters longer than the shortest route <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a><a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. Red Comet's algorithm determined this longer path had fewer turns, allowing for higher speeds and ultimately a faster overall time <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a><a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. This highlights that the challenge is a true [[strategies for complex problem solving | robotics problem]], intertwining both software (brains) and hardware (body) interaction <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a><a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.

## "Fosbury Flops" in Micromouse Innovation

The competition has seen paradigm shifts, akin to Dick Fosbury's revolutionary "Fosbury Flop" in high jump <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a><a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>:

### 1. Diagonal Movement

One of the earliest innovations was the introduction of diagonal movement, first implemented by the mouse "Mitee 3" <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a><a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. This required reducing the mouse's chassis width to less than 11 centimeters (5 cm for half-size) <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a><a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>. Diagonals also necessitated entirely new algorithms and sensor setups, as maintaining a precise path without parallel walls to guide the mouse is challenging <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a><a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>. Despite being a major source of crashes due to precision requirements, diagonal movement transforms jagged turns into narrow straightaways, offering dramatic speed payoffs <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a><a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a><a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.

### 2. Vacuum Fans for Increased Traction

By the early 2000s, Micromice were limited not by speed, but by control of that speed, struggling with friction during turns <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a><a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>. Competitors had to lower the center of gravity and slow down on turns to avoid slipping or flipping <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>.

The second "Fosbury Flop" involved the use of vacuum fans, first seen with the mouse Mokomo08 <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a><a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>. While flying is against the rules, vacuuming the mouse to the ground to prevent slipping is not <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a><a class="yt-timestamp" data-t="00:19:39">[00:19:39]</a>. These fans, often built from handheld drone parts, can generate a downward force five times the mouse's weight <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a><a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a><a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>. This increased friction allows Micromice to turn corners with centripetal acceleration approaching six Gs, comparable to F1 cars <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a><a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>. With this enhanced control, Micromice can now reach speeds of up to seven meters per second <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a><a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>.

## Ongoing Innovation

Micromouse continues to innovate, with experimentations in six- and eight-wheel designs, omnidirectional movement, and computer vision <a class="yt-timestamp" data-t="00:21:57">[00:21:57]</a><a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a><a class="yt-timestamp" data-t="00:22:02">[00:22:02]</a>. The competition serves as an excellent platform for learning about robotics, engineering, programming, and embedded systems <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a><a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a><a class="yt-timestamp" data-t="00:22:33">[00:22:33]</a>. It reminds us that there is no such thing as a simple problem <a class="yt-timestamp" data-t="00:23:21">[00:23:21]</a><a class="yt-timestamp" data-t="00:23:23">[00:23:23]</a>.