---
title: Logistic map and population modeling
videoId: ovJcsL7vyrk
---

From: [[veritasium]] <br/> 

The logistic map is a simple equation that connects seemingly disparate phenomena such as a dripping faucet, the Mandelbrot set, rabbit populations, thermal convection in fluids, and the firing of neurons in the brain <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. It provides a foundational understanding of how simple systems can generate highly complex and chaotic behaviors.

## The Logistic Map Equation

To model a population, for instance, of rabbits, a simple approach might be to multiply the current population ($X$) by a growth rate ($R$) to predict the next year's population <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. However, this model would lead to exponential and infinite growth, which is unrealistic <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

To introduce environmental constraints, a term `(1 - X)` is added, where $X$ represents the population as a percentage of the theoretical maximum (ranging from 0 to 1) <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. As the population approaches this maximum, the `(1 - X)` term approaches zero, thus constraining the population growth <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

This leads to the **logistic map** equation:
$X_{n+1} = R * X_n * (1 - X_n)$
where $X_{n+1}$ is the population next year and $X_n$ is the population this year <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
When graphed, plotting the population next year versus the population this year reveals an inverted parabola <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. This equation is considered the simplest that incorporates a negative feedback loop: the larger the population, the smaller it will be in the subsequent year <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## Behavior of the Logistic Map

The long-term behavior of the population modeled by the logistic map largely depends on the value of the growth rate ($R$).

### Stable Equilibrium

For certain values of $R$, the population stabilizes to a constant value. For example, with $R = 2.6$ and an initial population of 0.4, the population quickly stabilizes around 0.615 over many iterations <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. This stable state matches observations in wild populations where births and deaths are balanced <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. The initial population choice does not affect this equilibrium value <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

As $R$ decreases, the equilibrium population also decreases <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. If $R$ falls below 1, the population eventually goes extinct, stabilizing at zero <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. Above $R=1$, the population stabilizes onto a constant, non-zero value, which increases as $R$ increases <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

### [[Period doubling and chaos theory | Period Doubling Bifurcations]]

A significant change occurs when $R$ passes 3 <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. Instead of settling on a single constant value, the population begins to oscillate back and forth between two distinct values, exhibiting a two-year cycle <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. This cyclic nature is also observed in natural populations <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

As $R$ continues to increase, each of these two values splits again, leading to a four-year cycle before repeating <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. These splits are known as **period doubling bifurcations** <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. As $R$ increases further, more bifurcations occur, leading to cycles of 8, 16, 32, and 64, with the bifurcations happening at an increasingly rapid pace <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

### Chaos

At approximately $R = 3.57$, the system transitions into [[Period doubling and chaos theory | chaos]] <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. In this state, the population never settles down and bounces around as if at random, with no discernible pattern or repeating cycle <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. The logistic map provided one of the earliest methods for generating pseudo-random numbers on computers, offering a way to achieve unpredictable output from a deterministic machine <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. These numbers are considered pseudo-random because if the exact initial conditions were known, the values could be calculated precisely <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

Despite the onset of [[Period doubling and chaos theory | chaos]], as $R$ continues to increase, windows of stable periodic behavior can reappear <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. For example, at $R = 3.83$, a stable cycle with a period of 3 years emerges, which then undergoes its own sequence of period doubling into 6, 12, 24, and so on, before returning to [[Period doubling and chaos theory | chaos]] <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. Intriguingly, this single equation contains periods of every possible length, given the right $R$ value <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

## Connection to Fractals and the Mandelbrot Set

The bifurcation diagram, which plots the long-term population values against the growth rate ($R$), exhibits fractal properties. Its large-scale features are seen to be repeated on smaller and smaller scales <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. Upon zooming in, it is confirmed to be a fractal <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

Remarkably, the bifurcation diagram is actually a part of the Mandelbrot set <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. The Mandelbrot set is based on the iterated equation $Z_{n+1} = Z_n^2 + C$, where $C$ is a complex number <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. A number $C$ is part of the Mandelbrot set if, starting with $Z=0$, the iterated value remains finite after unlimited iterations; otherwise, it "blows up" to infinity <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. For example, $C=1$ causes the iteration to blow up, while $C=-1$ oscillates between -1 and 0, remaining finite <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

When the Mandelbrot set equation is iterated thousands of times and its values are plotted on a Z-axis, looking from the side reveals the bifurcation diagram <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. This visualization shows that:
*   Numbers in the main cardioid (the large central bulb) stabilize onto a single constant value <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   Numbers in the main bulb oscillate between two values <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   Subsequent bulbs correspond to oscillations between four, eight, sixteen, and thirty-two values <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   The chaotic part of the bifurcation diagram corresponds to the "needle" of the Mandelbrot set, where it becomes very thin <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.
*   A "medallion" on the Mandelbrot set that resembles a smaller version of the entire set corresponds to the window of stability with a period of three in the bifurcation plot <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

While the bifurcation diagram exists only on the real line (using real numbers), other bulbs off the main cardioid of the Mandelbrot set also exhibit periodic cycles of lengths like 3, 4, or 5 <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

## [[realworld_experiments_and_simulations_demonstrating_the_effect | Real-world Applications and Demonstrations]]

The logistic map, despite its simplicity, demonstrates surprising predictive power in various scientific fields:

*   **Population Modeling:** It accurately models animal populations, especially in controlled laboratory environments <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
*   **Fluid Convection:** Physicist Lib Taber observed [[Period doubling and chaos theory | period doubling]] in mercury undergoing thermal convection. As he increased the temperature gradient, a regular temperature spike first developed a wobble at half the original frequency (period two), then split into four, and then eight distinct temperature values before repeating, providing a "spectacular confirmation" of the theory <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
*   **Biological Responses:**
    *   Human and salamander eyes exhibit [[Period doubling and chaos theory | period doubling]] in response to flickering lights. Beyond a certain flicker rate, the eyes respond only to every other flicker, showcasing the emergence of the bifurcation diagram from real-world data <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
    *   Studies on rabbits given a drug to induce heart fibrillation found that the heart's path to fibrillation followed the [[Period doubling and chaos theory | period doubling route to chaos]]. The heart beat transitioned from periodic to a two-cycle, then a four-cycle, and eventually to aperiodic (chaotic) behavior <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>. Scientists were able to monitor the heart in real-time and use [[Period doubling and chaos theory | chaos theory]] to determine when to apply electrical shocks to restore periodic beating <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.
*   **Dripping Faucet:** A seemingly regular dripping faucet can exhibit [[Period doubling and chaos theory | period doubling]] and eventually chaotic behavior simply by adjusting the flow rate <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>. Even with constant water pressure and aperture size, the dripping can become chaotic <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.

## The Feigenbaum Constant and Universality

The prevalence of the bifurcation diagram in diverse systems is further underscored by the discovery of the Feigenbaum constant. Physicist Mitchell Feigenbaum observed that the ratio of the width of each [[Period doubling and chaos theory | bifurcation]] section to the next one converges on a universal constant, approximately 4.669 <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>. This constant, now named the Feigenbaum constant, describes how the bifurcations occur faster and faster but at a fixed ratio <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.

What makes this even more remarkable is that this constant is considered a fundamental constant of nature, yet its origin is not linked to any other known physical constant <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>. Furthermore, this universality extends beyond the specific form of the logistic equation; *any* iterated equation that has a single "hump" (like `sine X`) will exhibit [[Period doubling and chaos theory | bifurcations]] with the same Feigenbaum constant scaling for their occurrence <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>. This principle of "universality" suggests something fundamental about these processes <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.

## Significance and Educational Value

In 1976, biologist Robert May published a pivotal paper in *Nature* about the logistic equation, which sparked a revolution in the study of [[Period doubling and chaos theory | chaos]] <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>. In his paper, May advocated for teaching students about this simple equation because it provides new intuition into how simple systems can generate very complex behaviors <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>. The concept highlights that simplicity in underlying rules does not necessarily equate to simple outcomes, a concept that is not always emphasized in traditional education <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>. The fascination with [[Period doubling and chaos theory | chaos]] and the logistic equation continues, as exemplified by James Gleick's book "Chaos" <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.