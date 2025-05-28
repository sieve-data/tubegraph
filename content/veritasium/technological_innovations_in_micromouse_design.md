---
title: Technological innovations in Micromouse design
videoId: ZMQbHMgK2rw
---

From: [[veritasium]] <br/> 

The [[micromouse_competition_history_and_rules | Micromouse]] competition, an annual event around the world, challenges participants to design tiny, autonomous robots to navigate and solve a maze as quickly as possible <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Originally inspired by Claude Shannon's maze-solving electronic mouse, Theseus, the competition has evolved significantly, driven by continuous [[technological_obsolescence_and_innovation | innovation]] in both software and hardware <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a> <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.

## Origins and Early Design
The concept of a maze-solving electronic mouse dates back to 1952, when mathematician Claude Shannon constructed "Theseus" <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This mouse was a [[use_of_magnets_for_controlling_spider_movement | magnet on wheels]] that followed an electromagnet controlled by telephone relay switches built into the maze itself <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Theseus is considered one of the first examples of machine learning <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

In 1977, the Institute of Electrical and Electronics Engineers (IEEE) launched its "Amazing Micro-Mouse Maze Contest," drawing over 6,000 initial entrants <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. Early [[micromouse_competition_history_and_rules | Micromouse competition rules]] dictated that the robots be fully autonomous, without external control, GPS, or internet connection <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. They had to fit within a 25 cm by 25 cm footprint, containing all computing, motors, sensors, and power supply <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. Climbing, flight, or combustion forms of propulsion were disallowed <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

## Evolution of Maze-Solving Algorithms
Initially, the objective was simply to find the shortest path to the maze's goal <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

### Early Search Strategies
*   **Wall-Following:** Some initial competitors found success by simply following one wall of the maze <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. However, [[micromouse_competition_history_and_rules | competition rules]] were adapted to prevent this strategy from working, by moving the goal away from edges and adding free-standing walls <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
*   **Depth-First Search:** This strategy involves the mouse running as deep into the maze as possible, turning back only when it hits a dead end or loop <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. While it guarantees reaching the goal, it doesn't necessarily find the shortest path <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   **Breadth-First Search:** This algorithm finds the shortest path by checking every option at each intersection <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. However, it requires extensive backtracking, which is time-consuming <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

### Flood Fill Algorithm
The most popular [[micromouse_competition_history_and_rules | Micromouse]] strategy is the **flood fill algorithm** <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   **Optimistic Mapping:** Mice initially assume no walls exist and calculate the shortest path to the goal <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   **Dynamic Updates:** As they encounter walls, they mark them on their map and update the shortest path <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
*   **Distance Values:** Under the hood, the mouse assigns a numerical distance from every square to the goal, following decreasing numbers to zero <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
*   **Efficiency:** This approach efficiently finds the shortest path, often leaving irrelevant areas of the maze unexplored <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

### Fastest Path vs. Shortest Path
By the late 1980s, some believed [[micromouse_competition_history_and_rules | Micromouse]] had "outlived itself" because the "problem was solved" <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. However, this view shifted significantly.
*   **Red Comet (2017):** Masakazu Utsunomiya's winning mouse, "Red Comet," in the 2017 All Japan competition, did not take the shortest path <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. Its path was 5.5 meters longer than the shortest route <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
*   **Paradigm Shift:** Red Comet's algorithm prioritized the *fastest path*, recognizing that a longer path with fewer turns could be quicker overall <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>. This showcased that the real challenge was not just solving the maze, but achieving optimal navigation at high speeds <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.

## Physical Innovations ("Fosbury Flops")
Inspired by Dick Fosbury's revolutionary high jump technique, [[micromouse_competition_history_and_rules | Micromouse]] has seen its own "Fosbury flops" – [[technological_obsolescence_and_innovation | innovations]] that dramatically changed how mice operate <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a> <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.

### 1. Diagonal Movement
*   **Mitee 3:** This mouse was the first to implement diagonal movements across the maze cells <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. This innovation transformed jagged paths of turns into single, narrow straightaways <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.
*   **Design Implications:** Achieving diagonals required reducing the mouse chassis to under 11 centimeters wide (5 cm for half-size mice) <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>. It also necessitated entirely new sensor algorithms, as the mouse operates with "blinders on," making it more prone to crashes if it veers off course <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.

### 2. Advanced Turning Strategies
With the introduction of diagonals, the number of possible turns increased exponentially, making path optimization even more complex <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>. Mice moved from stopping and pivoting to fluid, sweeping U-turn motions, allowing for a single, snaking motion through the maze <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a> <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>.

### 3. Sensor and Motor Upgrades
Over the years, [[micromouse_competition_history_and_rules | Micromouse]] technology has seen continuous improvements:
*   **Infrared Sensors:** Large, unwieldy arms used for wall finding were replaced by compact arrays of infrared sensors <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>.
*   **DC Motors and Encoders:** Precise stepper motors were traded for more powerful continuous DC motors and encoders, providing better feedback for control <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.
*   **Gyroscopes:** The integration of gyroscopes, stemming from mobile phone technology, provided an extra sense of orientation, making turning much more reliable than relying solely on wheel pulse counts <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.

### 4. Vacuum Fans (Downforce)
The second major "Fosbury flop" was the integration of vacuum fans to generate downforce <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.
*   **Problem:** As mice became faster, control during turns became a limiting factor, often requiring them to slow down to avoid slipping or flipping due to insufficient friction <a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>.
*   **Solution:** While flying is prohibited, generating downforce to "vacuum" the mouse to the ground is not <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>.
*   **Mechanism:** These fans, often built from handheld drone parts, can generate a downward force up to five times the mouse's weight <a class="yt-timestamp" data-t="00:20:18">[00:20:18]</a>. This drastically increases friction, allowing mice to turn corners with centripetal acceleration approaching six Gs, comparable to F1 cars <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a>.
*   **Impact:** The added control from fans allowed builders to push the speed limits, with mice reaching speeds of up to seven meters per second <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a> <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>.

## Future Innovations
[[micromouse_competition_history_and_rules | Micromouse]] continues to be a fertile ground for [[technological_obsolescence_and_innovation | innovation]]. Current experiments include:
*   **Multi-Wheeled Designs:** Beyond the standard four-wheeled mice, designs with six or eight wheels are being explored <a class="yt-timestamp" data-t="00:21:57">[00:21:57]</a>.
*   **Omnidirectional Movement:** This would allow for even more flexible and rapid changes in direction <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>.
*   **Computer Vision:** Incorporating computer vision could lead to new ways for mice to perceive and navigate the maze <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>.
*   **Miniaturization:** There is ongoing work on quarter-size [[micromouse_competition_history_and_rules | Micromouse]] designs <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.

The ongoing evolution in [[micromouse_competition_history_and_rules | Micromouse]] demonstrates that even seemingly simple problems can lead to deep and complex [[technological_obsolescence_and_innovation | innovation]] in robotics <a class="yt-timestamp" data-t="00:23:15">[00:23:15]</a>.