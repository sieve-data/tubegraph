---
title: Flood fill algorithm and Micromouse strategies
videoId: ZMQbHMgK2rw
---

From: [[veritasium]] <br/> 

The [[micromouse_robotics_competition|Micromouse robotics competition]] is a contest where tiny, autonomous robots solve mazes as fast as possible <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These robots must fit all their computing, motors, sensors, and power supply within a 25-centimeter frame and operate without remote control or external assistance <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. The final maze layout is revealed only at the start of each competition, and competitors cannot change their mouse's code afterward <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. Mice are typically allowed 7 to 10 minutes and five runs to complete the maze <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

The initial strategy for most Micromice is to use their first run to carefully learn the maze and identify the best path to the goal, followed by using their remaining runs to sprint along that path for the fastest possible time <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

## Early Maze Solving Approaches

Early attempts at maze-solving included:
*   **Claude Shannon's Theseus (1952):** An electronic mouse that could solve a maze using a computer built into the maze itself, made of telephone relay switches <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Theseus explored the maze using trial and error, registering information in its memory to later navigate directly to the goal without false turns <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This is considered one of the first examples of machine learning <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

In the early years of the [[micromouse_robotics_competition|Micromouse competition]], various search algorithms were considered:
*   **Wall-Following:** A simple strategy where the mouse keeps one hand (sensor) along a wall <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. While effective in some common mazes, this strategy became obsolete when the goal was moved away from edges and free-standing walls were added, causing a simple wall-following mouse to search indefinitely <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
*   **Depth-First Search:** This strategy involves running deep into the maze, noting every fork, and backtracking only when a dead end or loop is reached to try a different path <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>. While it eventually gets the mouse to the goal, it does not guarantee the shortest route, as shortcuts might be missed <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Breadth-First Search:** This algorithm finds the shortest path by checking every option at each intersection and systematically moving to the next layer of intersections <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>. However, the extensive backtracking means the mouse reruns paths numerous times, making it inefficient <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

## The Flood Fill Algorithm

The most popular strategy for [[micromouse_robotics_competition|Micromouse]] is the **flood fill algorithm** <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. This approach involves:
*   **Optimistic Journeys:** Initially, the mouse's map of the maze has no walls, and it calculates the shortest path to the goal <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   **Dynamic Mapping:** When the mouse inevitably hits a wall not on its optimistic map, it marks the wall and updates its internal map to reflect the new shortest path to the goal <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
*   **Distance Marking:** Under the hood, the mouse marks the distance from every square in the maze to the goal <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. It travels by following a trail of decreasing numbers down to zero <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.
*   **Fluid Movement:** The name "flood fill" comes from the process resembling flooding the maze with water and updating values based on the flow <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

While not guaranteed to find the best path on the first pass, this algorithm leverages the fact that Micromice must return to the start for subsequent runs <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. By treating the return trip as a new journey for searching, the mouse can efficiently discover the shortest path from start to finish within two attempts, often leaving irrelevant areas of the maze untouched <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.

## Evolution of Micromouse Strategies

By the end of the 1980s, some believed the Micromouse Contest had "outlived itself" because the problem of finding the shortest path seemed "solved" <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. However, the competition continued to evolve.

### From Shortest Path to Fastest Path
In the 2017 All Japan [[micromouse_robotics_competition|Micromouse Competition]], while many mice found and traversed the shortest path, Masakazu Utsunomiya's winning mouse, "Red Comet," took a different approach <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. Its path was 5.5 meters longer than the shortest route <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. This was because Micromice are not searching for the shortest path, but the *fastest* path <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. Red Comet's search algorithm determined that its chosen longer path had fewer turns, which allowed it to maintain higher speeds and ultimately win by 131 milliseconds <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>, <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. This highlights that Micromouse is a complex robotics problem combining both software and hardware <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.

### Strategic Innovations: The "Fosbury Flops"
Just as Dick Fosbury revolutionized the high jump, Micromouse has seen two major "Fosbury flops" that changed how mice run <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>:

1.  **Diagonal Movement:** Early mice turned corners with sharp pivots <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>. The mouse Mitee 3 introduced the concept of taking diagonals <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. This required reducing the mouse chassis width to less than 11 centimeters (5 cm for half-size mice) and developing new algorithms <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>. While more prone to crashes, diagonals transform jagged paths into narrow straightaways, significantly speeding up runs <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. This innovation, along with fluid U-turns, exponentially increased the number of possible turns and paths, making pathfinding more complex but dramatically faster <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.

2.  **Vacuum Fans for Downforce:** By the early 2000s, speed was limited by control, as mice had to slow down for turns to avoid slipping or flipping <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a>. The second "Fosbury flop" was the introduction of a spinning propeller that creates a downward vacuum force, effectively suctioning the mouse to the ground <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>. This fan, often built from handheld drone parts, can generate a downward force five times the mouse's weight <a class="yt-timestamp" data-t="00:20:18">[00:20:18]</a>. With this added friction, modern Micromice can turn corners with centripetal acceleration approaching six Gs, comparable to F1 cars <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a>, and reach speeds of up to seven meters per second <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.

These innovations demonstrate that Micromouse is far from a solved problem, requiring continuous innovation in both software algorithms and physical [[design_and_technology_in_micromice|design and technology]] <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. Future developments include experiments with six- and eight-wheel designs, omnidirectional movement, and computer vision <a class="yt-timestamp" data-t="00:21:57">[00:21:57]</a>.