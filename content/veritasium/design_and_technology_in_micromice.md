---
title: Design and technology in Micromice
videoId: ZMQbHMgK2rw
---

From: [[veritasium]] <br/> 

The [[micromouse_robotics_competition | Micromouse competition]], an endurance in robotics, challenges tiny autonomous robots to solve mazes as quickly as possible <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Originating from a misunderstanding about intelligent "electronic mice" in 1977, the competition has evolved into a demanding test of combined hardware and software ingenuity <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

## Historical Context and Early Influences

The concept of an intelligent maze-solving device dates back to 1952, when mathematician Claude Shannon constructed an electronic mouse named Theseus <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Theseus solved mazes by using a computer built into the maze itself, made of telephone relay switches <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. The mouse itself was essentially a magnet on wheels, controlled by an electromagnet linked to the relay switches <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. Theseus was capable of "learning" the correct path through trial and error, registering information in its memory to find the goal directly without false turns on subsequent runs <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. It is often cited as an early example of machine learning and inspired the field of AI <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

In 1977, the Institute of Electrical and Electronics Engineers (IEEE) announced the "Amazing Micro-Mouse Maze Contest" <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This competition was spurred by a misunderstanding about existing "electronic mice" that were not intelligent robots, leading the IEEE to wonder if they could hold such a contest themselves <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

## Micromouse Competition Rules and Design Constraints

Micromice must be fully autonomous, with no external control, GPS, or internet connection <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. All computing, motors, sensors, and power supply must be contained within a frame no longer or wider than 25 centimeters <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. While there's no height limit, rules prohibit climbing, flight, or combustion <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

The maze is a square, approximately three meters on each side, with 18-centimeter-wide corridors <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. A half-size category, introduced in 2009, features mice smaller than 12.5 centimeters per side and paths just nine centimeters across <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. The maze layout is revealed only at the start of each competition, and competitors cannot change their mouse's code afterward <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. Mice typically have seven to ten minutes and five runs to complete the maze from start to goal <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

## Evolution of Navigation Strategies

Early strategies included simple wall-following, which was quickly made ineffective by changing maze designs that moved the goal away from edges and added free-standing walls <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

More advanced search algorithms emerged:
*   **Depth-First Search:** Explores as deep into the maze as possible, backtracking only when a dead end or loop is reached <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. While it finds a path, it may not be the shortest <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   **Breadth-First Search:** Checks every option at each intersection layer by layer, guaranteeing the shortest path <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>. However, this involves significant backtracking and rerunning paths, often taking more time <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

The most popular strategy became the [[flood_fill_algorithm_and_micromouse_strategies | flood fill algorithm]] <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. This approach involves optimistic journeys through the maze, initially assuming no walls <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. When a wall is encountered, the mouse marks it and updates its internal map with the new shortest path to the goal, essentially "flooding" the maze with distance values from the goal <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. This algorithm, while not guaranteed to find the absolute shortest path on the first pass, leverages the return trip to the start as a second search, making it highly efficient in discovering the shortest route <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

By the late 1980s, some believed the competition had "outlived itself" as the problem of finding the shortest path seemed solved <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. However, the focus shifted from finding the shortest path to finding the *fastest* path <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. For example, Masakazu Utsunomiya's Red Comet won the 2017 All Japan Micromouse Competition by taking a path 5.5 meters longer than the shortest route, because it had fewer turns, allowing for higher speed <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

## Design Innovations: "Fosbury Flops"

Just as Dick Fosbury revolutionized the high jump, two key innovations profoundly changed Micromouse design and performance <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>:

### Diagonal Movement
One of the earliest innovations was the ability to cut corners diagonally <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>. The Mitee 3 mouse first implemented diagonals, proving it to be a much better idea than initially thought, to the point that maze designers now often incorporate diagonal paths <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. This required reducing the mouse's chassis to less than 11 centimeters wide (five centimeters for half-size mice) <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>. It also demanded new algorithms and sensor configurations, as guiding the mouse diagonally is more challenging than maintaining equal distance between parallel walls <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>. Diagonal movement transforms jagged paths of turns into narrow straightaways, significantly reducing travel time despite the risk of crashes <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.

### Sweeping Turns and Advanced Turning
In addition to diagonals, mice began to perform sweeping U-turns instead of stopping and pivoting through multiple right turns <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>. The combination of diagonals and sweeping turns exponentially increased the number of possible turn options, making pathfinding more complex but leading to a single, fluid, snaking motion through the maze <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.

## Technological Upgrades

Over the years, Micromice have seen continuous technological upgrades:
*   **Sensors:** Tall, unwieldy arms for wall detection were replaced by smaller arrays of infrared sensors <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>.
*   **Motors:** Precise stepper motors were traded for continuous DC motors with encoders, offering more power for less size and weight <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.
*   **Gyroscopes:** These were added to provide an extra sense of orientation, derived from mobile phone technology, making turning much more reliable than counting wheel pulses <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.

### Vacuum Fans for Increased Friction
One of the most significant physical innovations, initially considered a gimmick, was the use of vacuum fans <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>. Introduced by Mokomo08, these fans (often built from handheld drone parts) create a downward force up to five times the mouse's weight <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>. This dramatically increases friction, allowing Micromice to turn corners with centripetal acceleration approaching six Gs, comparable to F1 cars <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a>. This added control allowed builders to push speed limits; a Micromouse can out-accelerate a Tesla Roadster, albeit not for long, reaching speeds of up to seven meters per second <a class="yt-timestamp" data-t="00:21:04">[00:21:04]</a>.

## Future Developments

The [[micromouse_robotics_competition | Micromouse competition]] continues to drive innovation, as it remains a complex robotics problem involving both software and hardware <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. While four-wheeled mice became the norm after 22 years of experimentation <a class="yt-timestamp" data-t="00:21:43">[00:21:43]</a>, current designs are experimenting with six- and eight-wheel configurations, omnidirectional movement, and even computer vision <a class="yt-timestamp" data-t="00:21:57">[00:21:57]</a>.

## Designing Micromouse Parts with Onshape

Designing precise parts for a Micromouse often requires 3D CAD (Computer-Aided Design) software <a class="yt-timestamp" data-t="00:24:02">[00:24:02]</a>. [[Onshape]] is a modern CAD and PDM (Product Data Management) system built entirely in the cloud, allowing engineering and design teams to collaborate in real-time on the same design <a class="yt-timestamp" data-t="00:24:13">[00:24:13]</a>. This eliminates the need to email large files and manage different versions, facilitating agile methodologies in hardware development <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>. [[Onshape]] is free for makers and hobbyists, and can be used on various devices, including computers and phones <a class="yt-timestamp" data-t="00:24:54">[00:24:54]</a>.