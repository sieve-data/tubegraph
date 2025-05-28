---
title: History and evolution of mazesolving algorithms
videoId: ZMQbHMgK2rw
---

From: [[veritasium]] <br/> 

Maze-solving algorithms have evolved significantly, particularly within the context of the Micromouse competition, a robotics race where small autonomous robots navigate a maze as fast as possible <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Early Maze-Solving Robots and Machine Learning

In 1952, mathematician Claude Shannon created Theseus, an electronic mouse capable of solving a maze <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The intelligence of Theseus was embedded in a computer built into the maze itself, using telephone relay switches <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. Theseus explored the maze using a "rather involved strategy of trial and error" <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>, registering information about the correct path in its memory as it found it <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. This allowed it to navigate directly to the goal without false turns in explored areas <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. Theseus is considered one of the first examples of machine learning and inspired the field of AI <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

The Micromouse competition, established by IEEE in 1977, was inspired by a misunderstanding about "electronic mice" being intelligent robots <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. Early Micromice, much like Theseus, needed to learn the maze layout during their first run <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

## Initial Strategies for Micromice

### Wall-Following
One of the simplest maze-solving strategies is wall-following <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. By keeping one hand (or sensor) on a single wall, a mouse can eventually reach the end of most common mazes <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. This strategy was initially successful, with a wall-following mouse winning the first Micromouse finals <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. However, competition rules were updated to counter this, moving the goal away from edges and adding free-standing walls, which would cause a wall-following mouse to search indefinitely <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

### Depth-First Search
A more advanced strategy involves exploring the maze by noting every fork in the road and backtracking from dead ends or loops to try a different path <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>. This is known as depth-first search <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. While it guarantees reaching the goal, it may not find the shortest route as it only turns back when necessary, potentially missing shortcuts <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

### Breadth-First Search
The sibling to depth-first search, breadth-first search, *would* find the shortest path <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>. In this strategy, the mouse explores one branch of an intersection, then returns to check skipped paths before moving to the next layer of intersections <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. However, this approach involves extensive backtracking, leading to paths being rerun multiple times <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>, often making it slower than simply searching the entire maze <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

## The [[flood_fill_algorithm_and_micromouse_strategies | Flood Fill Algorithm]]

The most popular strategy for Micromice is the [[flood_fill_algorithm_and_micromouse_strategies | flood fill algorithm]] <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. This algorithm involves the mouse making "optimistic journeys" <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. Initially, the mouse's internal map assumes no walls and plans the shortest path directly to the goal <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. When it inevitably encounters a wall not on its map, it marks the wall and updates its new shortest path to the goal <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

Under the hood, the mouse marks the distance from every square to the goal on its map <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. It then follows the trail of decreasing numbers down to zero <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. When a wall is hit, the numbers on the map are updated to reflect the new shortest distances <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. This process resembles flooding the maze with water, updating values based on the flow, which gives the algorithm its name <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

While not guaranteed to find the best path on the first pass <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>, this algorithm leverages the rule that mice must return to the start for subsequent runs <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. By treating the return trip as a new journey to search the maze <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>, the mouse efficiently discovers the shortest path, often leaving irrelevant areas untouched <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. The [[flood_fill_algorithm_and_micromouse_strategies | flood fill algorithm]] provides both an intelligent and practical way for Micromice to find the shortest path <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

## Evolution Beyond Shortest Path: Fastest Path Optimization

By the end of the 1980s, some believed the Micromouse Contest had "outlived itself" as the problem of finding the shortest path seemed "solved" <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. However, the goal of Micromouse is not the shortest path, but the *fastest* path <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

This distinction was dramatically demonstrated by Masakazu Utsunomiya's mouse, "Red Comet," in the 2017 All Japan Micromouse Competition <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. While other top mice took the shortest path (7.4 seconds), Red Comet took a path 5.5 meters longer <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. Its search algorithm determined that this longer path had fewer turns, which allowed it to maintain speed and ultimately win by 131 milliseconds <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. This demonstrated that the problem wasn't just about solving the maze, but about navigation and speed <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

## Algorithmic Changes Driven by Physical Innovation

The evolution of algorithms was also influenced by physical innovations:

*   **Diagonal Movement**: An early innovation, known as a "Fosbury flop" in Micromouse, was the implementation of diagonal movement by the mouse "Mitee 3" <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. Instead of turning corners in a right-angle fashion, mice could cut diagonally through cells <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>. This required reducing the chassis size and a new algorithm to guide the mouse, as it couldn't rely on constant wall readings <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>. While diagonals increase the risk of crashes, they transform jagged paths into narrow straightaways, significantly reducing run times <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.
*   **Sweeping Turns**: Similar to diagonals, mice began to apply strategies for sweeping turns, replacing multiple abrupt right turns with a single, fluid U-turn motion <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>. The addition of diagonal possibilities, combined with sweeping turns, exponentially increased the number of possible turns <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>. This made figuring out the best path much more complex, as the maze was no longer just a grid of square hallways <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.

These innovations meant that how Micromice imagined and moved through the maze "had changed completely" <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>, requiring more sophisticated path-finding and navigation algorithms that optimize for fluidity and speed rather than just shortest distance.

## Future Directions

The field of Micromouse is still evolving, with ongoing experimentation in designs such as six- and eight-wheel configurations, omnidirectional movement, and the integration of computer vision <a class="yt-timestamp" data-t="00:21:57">[00:21:57]</a>. The problem is far from solved, being a complex robotics challenge that integrates both software and hardware <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. The continuous innovation ensures that new algorithmic "Fosbury flops" are always possible <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>.