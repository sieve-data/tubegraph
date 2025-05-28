---
title: Feigenbaum constant and universality
videoId: ovJcsL7vyrk
---

From: [[veritasium]] <br/> 

The Feigenbaum constant, named after physicist Mitchell Feigenbaum, is a fundamental constant in mathematics that describes the ratio at which period-doubling bifurcations occur in non-linear systems before they transition into chaos <a class="yt-timestamp" data-t="14:32:00">[14:32:00]</a>, <a class="yt-timestamp" data-t="14:46:00">[14:46:00]</a>. This constant is a manifestation of "universality," meaning it appears in a broad class of mathematical functions, not just the specific ones it was discovered with <a class="yt-timestamp" data-t="15:51:00">[15:51:00]</a>.

## The Logistic Map: A Model for Complex Behavior

The connection between diverse phenomena like dripping faucets, the [[fractals_and_the_mandelbrot_set | Mandelbrot set]], rabbit populations, thermal convection, and neuron firing can be understood through a single, simple equation known as the logistic map <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>, <a class="yt-timestamp" data-t="01:11:16">[01:11:16]</a>. This equation models a population's growth (represented as a percentage of its theoretical maximum, from 0 to 1) year after year, incorporating both a growth rate (R) and environmental constraints <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>, <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>, <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.

The logistic map is expressed as:
X<sub>n+1</sub> = R * X<sub>n</sub> * (1 - X<sub>n</sub>) <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>.
It features a negative feedback loop: as the population grows, the subsequent year's population is constrained <a class="yt-timestamp" data-t="01:32:00">[01:32:00]</a>.

### Behavior of the Logistic Map

The long-term behavior of the population (its equilibrium value) depends heavily on the growth rate, R <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>.

*   **Low Growth Rates (R < 1)**: The population drops and eventually goes extinct, with an equilibrium value of zero <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>, <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.
*   **Stable Equilibrium (1 < R < 3)**: The population stabilizes to a constant value. A higher R leads to a higher equilibrium population <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>, <a class="yt-timestamp" data-t="02:33:00">[02:33:00]</a>.
*   **Period Doubling (R > 3)**: When R passes 3, the population no longer settles on a single constant value. Instead, it oscillates between two values in a two-year cycle <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>, <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>. As R continues to increase, each of these two values splits again, leading to a four-year cycle, then an eight-year cycle, and so on (8, 16, 32, 64) <a class="yt-timestamp" data-t="04:45:00">[04:45:00]</a>, <a class="yt-timestamp" data-t="05:06:00">[05:06:00]</a>. These are known as period-doubling bifurcations <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.
*   **Chaos (R ≈ 3.57)**: At approximately R = 3.57, the system transitions into chaos. The population never settles, bouncing around unpredictably as if at random <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>. This equation was one of the first methods to generate pseudo-random numbers on computers <a class="yt-timestamp" data-t="05:24:00">[05:24:00]</a>, <a class="yt-timestamp" data-t="05:41:00">[05:41:00]</a>.
*   **Windows of Stability**: Amidst the chaotic behavior, as R continues to increase, there are "windows of stable periodic behavior" <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>. For example, at R = 3.83, a stable three-year cycle emerges, which then undergoes its own period-doubling sequence (6, 12, 24, etc.) before returning to chaos <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a>, <a class="yt-timestamp" data-t="06:03:00">[06:03:00]</a>. This single equation can generate cycles of every possible length <a class="yt-timestamp" data-t="06:10:00">[06:10:00]</a>.

## Connection to [[fractals_and_the_mandelbrot_set | Fractals]]

The graph illustrating the equilibrium population values for different R values is known as a bifurcation diagram. This diagram visually resembles a [[fractals_and_the_mandelbrot_set | fractal]], with large-scale features repeating on smaller scales <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>, <a class="yt-timestamp" data-t="06:30:00">[06:30:00]</a>.

Remarkably, the bifurcation diagram is actually part of the [[fractals_and_the_mandelbrot_set | Mandelbrot set]] <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a>. The [[fractals_and_the_mandelbrot_set | Mandelbrot set]] is based on the iterated equation Z<sub>n+1</sub> = Z<sub>n</sub><sup>2</sup> + C, where C is a complex number <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>, <a class="yt-timestamp" data-t="06:55:00">[06:55:00]</a>. A number C is part of the [[fractals_and_the_mandelbrot_set | Mandelbrot set]] if, after unlimited iterations (starting with Z=0), the value of Z remains finite; otherwise, it is not <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>, <a class="yt-timestamp" data-t="07:11:00">[07:11:00]</a>.

When the [[fractals_and_the_mandelbrot_set | Mandelbrot set]] is plotted in 3D, with the iterated value on the Z-axis, a side view reveals the bifurcation diagram <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>, <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>.
*   Numbers within the main cardioid of the [[fractals_and_the_mandelbrot_set | Mandelbrot set]] correspond to parameters where the iteration stabilizes to a single constant value <a class="yt-timestamp" data-t="08:53:00">[08:53:00]</a>.
*   Numbers in the main bulbs off the cardioid correspond to parameters where the iteration oscillates between two, four, or more values, directly mirroring the period-doubling bifurcations <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>, <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>, <a class="yt-timestamp" data-t="09:11:00">[09:11:00]</a>.
*   The "needle" of the [[fractals_and_the_mandelbrot_set | Mandelbrot set]] is where the chaotic part of the bifurcation diagram occurs <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>.
*   Smaller copies of the [[fractals_and_the_mandelbrot_set | Mandelbrot set]] (medallions) within the chaotic region correspond to the windows of stability (e.g., the period-3 cycle) seen in the bifurcation diagram <a class="yt-timestamp" data-t="09:31:00">[09:31:00]</a>, <a class="yt-timestamp" data-t="09:35:00">[09:35:00]</a>.

## Real-World Manifestations of Chaos and Period Doubling

The patterns observed in the logistic map and the bifurcation diagram are not merely mathematical curiosities but are found in various scientific fields:

*   **Animal Populations**: The logistic map accurately models animal populations, especially in controlled laboratory environments <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>, <a class="yt-timestamp" data-t="10:28:00">[10:28:00]</a>.
*   **Thermal Convection**: Physicist Lib Taber observed period doubling in mercury convection experiments. As he increased the temperature gradient, the fluid's behavior transitioned from a regular periodic flow to a two-temperature oscillation, then four, and eight, confirming the period-doubling route to chaos <a class="yt-timestamp" data-t="10:49:00">[10:49:00]</a>, <a class="yt-timestamp" data-t="11:26:00">[11:26:00]</a>, <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>.
*   **Biological Systems**:
    *   **Eye Response**: Studies on human and salamander eyes show period doubling in response to flickering lights. Beyond a certain flicker rate, eyes respond to only every other flicker <a class="yt-timestamp" data-t="12:05:00">[12:05:00]</a>, <a class="yt-timestamp" data-t="12:11:00">[12:11:00]</a>.
    *   **Heartbeat**: In experiments on rabbits, a drug inducing heart fibrillation revealed the period-doubling route to chaos. The heart's beat pattern went from periodic, to a two-cycle, then a four-cycle, and eventually chaotic (fibrillation) <a class="yt-timestamp" data-t="12:31:00">[12:31:00]</a>, <a class="yt-timestamp" data-t="12:48:00">[12:48:00]</a>. Researchers successfully used chaos theory to predict and control when to apply electrical shocks to restore a normal heartbeat <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>, <a class="yt-timestamp" data-t="13:19:00">[13:19:00]</a>.
*   **Dripping Faucets**: Even a common dripping faucet can exhibit period doubling and chaotic behavior simply by adjusting its flow rate <a class="yt-timestamp" data-t="13:33:00">[13:33:00]</a>, <a class="yt-timestamp" data-t="13:41:00">[13:41:00]</a>, <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>.

## The Feigenbaum Constant and Universality

Mitchell Feigenbaum, while studying the period-doubling bifurcations, discovered a remarkable constant. He observed that if he divided the width of one bifurcation section by the width of the next, the ratio approached a specific number: 4.669 <a class="yt-timestamp" data-t="14:32:00">[14:32:00]</a>, <a class="yt-timestamp" data-t="14:40:00">[14:40:00]</a>, <a class="yt-timestamp" data-t="14:46:00">[14:46:00]</a>. This value is now known as the **Feigenbaum constant** <a class="yt-timestamp" data-t="14:46:00">[14:46:00]</a>.

What makes this constant extraordinary is its **universality** <a class="yt-timestamp" data-t="15:51:00">[15:51:00]</a>. It's not unique to the logistic map. Any iterated equation that has a "single hump" (meaning its graph is a parabola-like shape with a single peak) will exhibit the same period-doubling sequence, and the ratio of where those bifurcations occur will converge to the same Feigenbaum constant of 4.669 <a class="yt-timestamp" data-t="15:10:00">[15:10:00]</a>, <a class="yt-timestamp" data-t="15:16:00">[15:16:00]</a>, <a class="yt-timestamp" data-t="15:33:00">[15:33:00]</a>. This constant does not appear to relate to any other known physical constants, suggesting it is a fundamental constant of nature itself <a class="yt-timestamp" data-t="15:00:00">[15:00:00]</a>, <a class="yt-timestamp" data-t="15:03:00">[15:03:00]</a>, <a class="yt-timestamp" data-t="15:06:00">[15:06:00]</a>.

## Significance

In 1976, biologist Robert May published a groundbreaking paper in *Nature* about the logistic map, sparking a revolution in the study of complex systems <a class="yt-timestamp" data-t="16:06:00">[16:06:00]</a>, <a class="yt-timestamp" data-t="16:11:00">[16:11:00]</a>. May advocated for teaching this simple equation to students because it provides intuition into how simple underlying principles can generate incredibly complex behaviors <a class="yt-timestamp" data-t="16:20:00">[16:20:00]</a>, <a class="yt-timestamp" data-t="16:29:00">[16:29:00]</a>, <a class="yt-timestamp" data-t="16:31:00">[16:31:00]</a>. The concept of chaos, as explored in works like James Gleick's book *Chaos*, highlights the profound implications of these findings <a class="yt-timestamp" data-t="17:08:00">[17:08:00]</a>.