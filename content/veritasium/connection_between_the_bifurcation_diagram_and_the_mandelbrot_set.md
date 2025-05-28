---
title: Connection between the bifurcation diagram and the Mandelbrot set
videoId: ovJcsL7vyrk
---

From: [[veritasium]] <br/> 
The **logistic map** is a simple mathematical equation used to model population growth and explore complex behaviors like chaos <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. Despite its simplicity, it reveals profound connections to fractal geometry and other scientific phenomena <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## The Logistic Map

The equation for the logistic map is:
$x_{n+1} = R * x_n * (1 - x_n)$ <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>

Here:
*   $x_n$ represents the population in the current year, expressed as a percentage of the theoretical maximum (from 0 to 1) <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   $x_{n+1}$ is the population in the next year <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   $R$ is the growth rate <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

This equation incorporates a negative feedback loop: as the population ($x_n$) approaches the maximum (1), the $(1-x_n)$ term goes to zero, constraining the population growth <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Graphing $x_{n+1}$ versus $x_n$ produces an inverted parabola <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

### Behavior of the Logistic Map

The long-term behavior of the population depends critically on the value of $R$:

*   **Extinction ($R < 1$)**: For low growth rates, the population eventually drops to zero <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   **Stable Equilibrium ($1 \le R < 3$)**: The population stabilizes onto a single constant value, matching observations in natural populations <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>, <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. This equilibrium value increases as $R$ increases <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   **Period Doubling ($R > 3$)**:
    *   Once $R$ passes 3, the population no longer settles on a single value but oscillates between two values <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. This is known as a period-doubling bifurcation <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
    *   As $R$ continues to increase, each of these two values splits again, leading to a four-year cycle <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
    *   This process continues rapidly, creating cycles of 8, 16, 32, 64, and so on <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   **Chaos ($R \approx 3.57$)**: At approximately $R = 3.57$, the system enters a chaotic state <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. The population never settles down, appearing to bounce around randomly <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. This equation provided one of the earliest methods for generating pseudo-random numbers on computers <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   **Windows of Stability (e.g., $R \approx 3.83$)**: Amidst the chaos, stable periodic behaviors return in specific "windows." For example, at $R = 3.83$, a stable cycle with a period of 3 years emerges <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>, which then also undergoes period doubling (to 6, 12, 24, etc.) before returning to chaos <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. The equation contains periods of every length <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

## The Bifurcation Diagram

Plotting the long-term population values (on the y-axis) against the growth rate $R$ (on the x-axis) creates the **bifurcation diagram** <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. This diagram visually demonstrates the transitions from stability to period doubling and then to chaos, with periodic windows appearing within the chaotic regions <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>, <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

The bifurcation diagram itself possesses [[feigenbaum_constant_and_universality | fractal properties]], meaning large-scale features are repeated on smaller scales <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

## The Mandelbrot Set

The [[Mandelbrot Set]] is a famous fractal defined by a different iterated equation in the complex plane:
$Z_{n+1} = Z_n^2 + C$ <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>

To determine if a complex number $C$ is part of the Mandelbrot set:
1.  Start with $Z = 0$ <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
2.  Iterate the equation repeatedly <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
3.  If the value of $Z$ remains finite after unlimited iterations, $C$ is part of the set <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. If it "blows up" to infinity, $C$ is not <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

For example:
*   If $C = 1$, the sequence becomes $0, 1, 2, 5, 26, \dots$ which blows up, so 1 is not in the set <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
*   If $C = -1$, the sequence is $0, -1, 0, -1, \dots$ which oscillates and remains finite, so -1 is in the set <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

Typically, images of the Mandelbrot set show the boundary between numbers that remain finite and those that don't <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

## The Connection: Bifurcation Diagram as Part of the Mandelbrot Set

Surprisingly, the bifurcation diagram is actually part of the Mandelbrot set <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. While the bifurcation diagram is traditionally plotted on the real number line (for the growth rate $R$), the Mandelbrot set exists in the complex plane.

The connection becomes clear when visualizing the Mandelbrot set in 3D:
1.  Plot the complex number $C$ on the x-y plane (the usual Mandelbrot set view).
2.  Plot the *value* that the iteration $Z$ takes after many iterations on the z-axis <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.

When viewed from the side, this 3D plot of the Mandelbrot set reveals the bifurcation diagram <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.

Specific parts of the Mandelbrot set correspond to specific behaviors in the bifurcation diagram:
*   **Main Cardioid**: Numbers in the main cardioid of the Mandelbrot set correspond to regions where the iterated value stabilizes onto a single constant <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
*   **Main Bulb (Period-2)**: The large circular bulb attached to the cardioid represents values of $C$ where the iteration oscillates back and forth between two values (period 2) <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   **Successive Bulbs**: The smaller bulbs along the main axis represent period 4, then period 8, 16, 32, and so on, just like the period-doubling bifurcations <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   **The "Needle"**: The thin chaotic part of the bifurcation diagram corresponds to the "needle" of the Mandelbrot set, where it becomes extremely thin <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.
*   **Medallions/Smaller Mandelbrots**: The smaller, self-similar copies of the Mandelbrot set that appear along the needle correspond to the windows of stability (e.g., the period-3 window) found within the chaotic region of the bifurcation diagram <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

While the bifurcation diagram only exists on the real line, the various "bulbs" off the main cardioid in the complex plane also exhibit similar periodic cycles of 3, 4, 5, etc., when viewed in 3D <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

## Universality and Impact

The phenomenon of period doubling leading to chaos and the emergence of the bifurcation diagram is not unique to the logistic map. Any equation with a single "hump" that is iterated will exhibit similar bifurcations <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>. This concept is known as [[feigenbaum_constant_and_universality | universality]] <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.

Mitchell Feigenbaum discovered that the ratio of the widths of successive bifurcations converges to a constant value, approximately 4.669 <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>. This [[feigenbaum_constant_and_universality | Feigenbaum constant]] is considered a fundamental constant of nature, unrelated to other known physical constants <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>, <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.

The discovery of these complex behaviors from simple equations, particularly highlighted by biologist Robert May's 1976 paper in *Nature*, sparked a [[definition_and_implications_of_revolutions_in_mathematics | revolution]] in how scientists and mathematicians understand complex systems <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>. It introduced the idea that simple rules can generate very complex, seemingly random, outcomes <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>. This understanding has been applied to various fields, including fluid dynamics (thermal convection in mercury) <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>, neurophysiology (response of eyes to flickering lights) <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>, cardiology (heart fibrillation) <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>, and even the seemingly simple dripping of a faucet <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.