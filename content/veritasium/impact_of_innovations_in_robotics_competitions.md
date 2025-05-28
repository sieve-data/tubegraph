---
title: Impact of innovations in robotics competitions
videoId: ZMQbHMgK2rw
---

From: [[veritasium]] <br/> 

The world of robotics competitions, particularly the long-standing [[micromouse_robotics_competition | Micromouse]] maze contest, serves as a fertile ground for innovation in both hardware and software design <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. What might seem like a simple problem at first glance—a mouse solving a maze—has continually pushed the boundaries of robotic engineering and artificial intelligence <a class="yt-timestamp" data-t="00:23:19">[00:23:19]</a>.

## Origins and Early Challenges

The inspiration for the [[micromouse_robotics_competition | Micromouse]] competition traces back to mathematician Claude Shannon's electronic mouse, Theseus, created in 1952, which could solve a maze using a built-in computer made of telephone relay switches <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Theseus is considered one of the first examples of machine learning and inspired the field of AI <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

In 1977, the IEEE announced its "Amazing Micro-Mouse Maze Contest," attracting over 6,000 entrants <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. Early iterations of the maze allowed for simple strategies, but rules quickly evolved to demand more sophisticated robotic intelligence <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

## Early Search Algorithms

Initially, some [[micromouse_robotics_competition | Micromouse]] competitors realized that a simple wall-following strategy could solve most common mazes <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. However, after a wall-following mouse won the first finals, the maze design was altered with the goal moved away from edges and free-standing walls added, rendering simple wall-following ineffective <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

More advanced search algorithms emerged:
*   **Depth-First Search**: This strategy involves running as deep into the maze as possible and turning back only when a dead end or loop is reached <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. While it guarantees reaching the goal, it does not guarantee the shortest route <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   **Breadth-First Search**: This algorithm would find the shortest path by checking every option at each layer of intersections <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>. However, it involves significant backtracking, leading to paths being rerun dozens of times <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   **Flood Fill Algorithm**: The most popular [[micromouse_robotics_competition | Micromouse]] strategy, flood fill, involves optimistic journeys through the maze <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. The mouse initially assumes no walls, drawing the shortest path to the goal, and updates its map and shortest path whenever it encounters a wall <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. This strategy updates distance values from every square to the goal, guiding the mouse along a path of decreasing numbers <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. By using both its outbound and return trips to search, this method efficiently discovers the shortest path <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.

Despite these advanced algorithms, by the end of the 1980s, some believed the [[micromouse_robotics_competition | Micromouse]] contest had "outlived itself" because the problem seemed "solved" <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

## Beyond Shortest Path: The Fastest Path

The perception that the problem was solved was shattered by innovations that recognized the competition was about the *fastest* path, not just the shortest <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. In the 2017 All Japan [[micromouse_robotics_competition | Micromouse]] Competition, Masakazu Utsunomiya's winning mouse, Red Comet, took a path 5.5 meters longer than the shortest route <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. Its search algorithm prioritized a path with fewer turns, which, despite being longer, allowed it to be faster, winning by 131 milliseconds <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. This demonstrated that [[micromouse_robotics_competition | Micromouse]] is a complex [[jumping_robot_engineering_and_design | robotics problem]] involving both software and hardware interaction <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.

## "Fosbury Flops" in Micromouse

Inspired by Dick Fosbury's revolutionary high jump technique, the [[micromouse_robotics_competition | Micromouse]] competition has seen its own "Fosbury flops"—innovations that completely changed how mice operate <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.

### Diagonal Movement
One of the earliest "Fosbury flops" was the implementation of diagonal movement <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>. The mouse Mitee 3 first introduced this, transforming jagged paths of turns into narrow straightaways <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. This required reducing the mouse chassis width to less than 11 centimeters (5 cm for half-size mice) and developing new algorithms for sensors and software to guide the mouse without constant wall references <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>. Diagonal movement is still a major source of crashes due to its unforgiving nature, but it significantly speeds up runs <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.

### Sweeping Turns
Following the diagonal innovation, mice began applying similar strategies to turning, performing single U-turn motions instead of stopping and pivoting <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>. The combination of diagonals and sweeping turns exponentially increased the number of possible turn options, making pathfinding more complex but leading to fluid, snaking motions through the maze <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.

## Hardware and Technological Advancements

Over the years, available technology also led to significant upgrades:
*   **Sensors**: Tall, unwieldy arms for finding walls were replaced by smaller arrays of infrared sensors <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>.
*   **Motors**: Precise stepper motors were traded for more powerful continuous DC motors and encoders, requiring servo feedback for control <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.
*   **Gyroscopes**: Miniaturized gyroscopes, popularized by mobile phones, provided an extra sense of orientation, making turning much more reliable than relying on wheel pulse counting <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.

### The Vacuum Fan Innovation
A significant physical innovation addressed the issue of friction during high-speed turns <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>. The second "Fosbury flop" for [[micromouse_robotics_competition | Micromouse]] was the introduction of a vacuum fan, first seen on Mokomo08 <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>. While flying is against the rules, vacuuming the mouse to the ground to prevent slipping is allowed <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>.

*   **Mechanism**: Built from handheld drone parts, these vacuum fans generate a downward force up to five times the mouse's weight <a class="yt-timestamp" data-t="00:20:18">[00:20:18]</a>.
*   **Impact**: This increased friction allows [[micromouse_robotics_competition | Micromouse]] to turn corners with centripetal acceleration approaching six Gs, comparable to F1 cars <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a>. With this added control, mice can reach speeds of up to seven meters per second and out-accelerate a Tesla Roadster over short distances <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>.

## Ongoing Evolution and Future Innovations

The field of [[micromouse_robotics_competition | Micromouse]] continues to evolve, with ongoing experimentation in:
*   **Wheel Designs**: Four-wheeled mice became the norm after 22 years of development <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>, and designs with six or eight wheels are now being explored <a class="yt-timestamp" data-t="00:21:57">[00:21:57]</a>.
*   **Movement**: Omnidirectional movement is an area of active development <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>.
*   **Perception**: The integration of computer vision could represent the next paradigm shift <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>.

The [[micromouse_robotics_competition | Micromouse]] contest exemplifies how competition drives innovation <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. It serves as an accessible platform for combining major disciplines of robotics, engineering, programming, and embedded systems <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>. Despite its seemingly simple core problem, nearly 50 years on, it remains a dynamic challenge that constantly reminds participants there is "no such thing as a simple problem" <a class="yt-timestamp" data-t="00:23:19">[00:23:19]</a>.

Modern [[jumping_robot_engineering and design | robotics design]] for competitions often utilizes 3D CAD programs like Onshape, which allow for precise part design and collaborative development in the cloud <a class="yt-timestamp" data-t="00:23:47">[00:23:47]</a>. This enables rapid iteration and the adoption of agile methodologies common in software development for hardware products <a class="yt-timestamp" data-t="00:24:39">[00:24:39]</a>.