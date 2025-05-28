---
title: Applications of logistic equations in science
videoId: ovJcsL7vyrk
---

From: [[veritasium]] <br/> 
The [[logistic_map_and_population_modeling|logistic map]] is a simple equation that connects seemingly disparate phenomena such as a dripping faucet, the Mandelbrot set, rabbit populations, thermal convection, and neuron firing <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. This single equation, despite its simplicity, can generate highly complex and unpredictable behaviors, including chaos <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

### The Logistic Map
The [[logistic_map_and_population_modeling|logistic map]] is expressed as `Xn+1 = R * Xn * (1 - Xn)` <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   `Xn` represents the population this year (as a percentage of the theoretical maximum, from 0 to 1) <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   `Xn+1` is the population next year <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   `R` is the growth rate <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

This equation is considered the simplest mathematical model that incorporates a negative feedback loop <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. The term `(1 - Xn)` represents environmental constraints; as the population `Xn` approaches its theoretical maximum, this term goes to zero, limiting exponential growth <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. When graphed, the relationship between the population next year and this year forms an inverted parabola <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

### Population Modeling
Initially, the logistic map was used to model animal populations, such as rabbits <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   **Equilibrium**: For low values of `R`, the population either stabilizes at a constant value (if `R` > 1) or goes extinct (if `R` < 1) <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. This stable equilibrium is observed in wild populations where births and deaths are balanced <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Period Doubling Bifurcations**: As `R` increases past 3, the equilibrium splits, causing the population to oscillate between two values <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. Further increases in `R` lead to more period doubling, resulting in cycles of 4, 8, 16, 32, and so on <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. This cyclic nature of populations is also observed in nature <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   **Chaos**: At approximately `R` = 3.57, the system enters a chaotic state <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. In this region, the population never settles down, bouncing around as if at random <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. This behavior led to the logistic equation providing one of the first methods for generating pseudo-random numbers on computers <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   **Windows of Stability**: Amidst the chaos, as `R` continues to increase, there are "windows of stable periodic behavior," such as a stable cycle with a period of 3 years at `R` = 3.83, which then also undergoes period doubling before returning to chaos <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. This equation can contain cycles of any length <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

### Connection to the Mandelbrot Set
The bifurcation diagram created by plotting the equilibrium values against `R` is a fractal <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. Zooming in reveals repeated patterns on smaller scales <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. This bifurcation diagram is actually part of the Mandelbrot set <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

The Mandelbrot set is based on the iterated equation `Zn+1 = Zn^2 + C`, where `C` is a complex number <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. If the iteration remains finite, `C` is part of the set <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. When the Mandelbrot set is visualized by plotting the iterated value on the z-axis and viewed from the side, the bifurcation diagram emerges <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.
*   Numbers within the main cardioid of the Mandelbrot set stabilize to a single constant value <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
*   Numbers in the main bulb oscillate between two values <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   Successive bulbs correspond to cycles of 4, 8, 16, 32, and so on <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   The chaotic part of the bifurcation diagram corresponds to the "needle" of the Mandelbrot set <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.
*   The stable window with a period of 3 in the bifurcation plot corresponds to a medallion resembling a smaller Mandelbrot set <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

### Diverse Scientific Applications
Beyond population modeling, the logistic equation and its period-doubling route to chaos have been observed in numerous other scientific fields:

*   **Fluid Dynamics**: Physicist Lib Taber's experiment with thermal convection in mercury demonstrated period doubling <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. As he increased the temperature gradient, the stable, periodic temperature spikes developed a wobble (period 2), then period 4, and then period 8, confirming the theoretical predictions <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.
*   **Biology**:
    *   **Visual Response**: Studies on human and salamander eyes show period doubling in response to flickering lights. Beyond a certain flicker rate, eyes respond to only every other flicker <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
    *   **Cardiac Rhythms**: Research on rabbit hearts induced into fibrillation revealed the period doubling route to chaos <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. The heart beat progressed from a periodic rhythm to a two-cycle, then a four-cycle, and eventually to aperiodic behavior <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>. Scientists used chaos theory to determine when to apply electrical shocks to return the heart to periodicity successfully <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.
*   **Everyday Phenomena**: A dripping faucet, often perceived as regular, can exhibit period doubling and eventually chaotic behavior by adjusting the flow rate <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. Despite constant water pressure and aperture size, chaotic dripping can occur <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.

### The Feigenbaum Constant and Universality
Mitchell Feigenbaum, a physicist, observed that the ratio of the widths of successive period doubling bifurcations in the [[logistic_map_and_population_modeling|logistic map]] converges to a constant value: 4.669 <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>. This is known as the Feigenbaum constant <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>. What makes it extraordinary is that this constant is considered a fundamental constant of nature, independent of other known physical constants <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>.

Furthermore, this universality extends to *any* iterated equation that has a single "hump" <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>. For example, iterating `Xn+1 = sine(Xn)` will also produce bifurcations, and the ratio of their occurrences will approach the same Feigenbaum constant <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>. This "universality" suggests a fundamental and pervasive process underlying complex behavior in various systems <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.

### Educational Significance
In 1976, biologist Robert May published a paper in *Nature* discussing the logistic equation, sparking a revolution in the study of chaos <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>. He advocated for teaching this simple equation to students because it provides intuition for how simple rules can generate very complex behaviors <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>. This perspective challenges traditional education that often focuses on simple equations with simple outcomes, suggesting that introducing chaos could offer a deeper understanding of natural phenomena <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>.