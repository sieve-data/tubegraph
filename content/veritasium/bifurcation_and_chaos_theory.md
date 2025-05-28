---
title: Bifurcation and chaos theory
videoId: ovJcsL7vyrk
---

From: [[veritasium]] <br/> 

The study of [[Bifurcation and chaos theory | chaotic systems]] reveals surprising connections between seemingly unrelated phenomena like a dripping faucet, population dynamics, thermal convection, and the firing of neurons in the brain, all governed by a single, simple equation <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## The Logistic Map: Modeling Populations

A simple model for a population, such as rabbits, can be represented by the logistic map equation <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Initially, a population might be modeled by multiplying the current population `X` by a growth rate `R` <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. However, this leads to exponential growth forever <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. To account for environmental constraints, a term `(1 - X)` is added, where `X` is expressed as a percentage of the theoretical maximum population (0 to 1) <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. As the population approaches the maximum, this term goes to zero, constraining growth <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

The resulting equation is:
`Xn+1 = R * Xn * (1 - Xn)`
where `Xn+1` is the population next year and `Xn` is the population this year <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. When graphed, the population next year versus this year forms an inverted parabola, representing the simplest equation with a negative feedback loop: larger populations lead to smaller populations the following year <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

### Iteration and Equilibrium

When iterating this equation, the population often stabilizes onto a constant value over many generations <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. For example, with `R = 2.6` and a starting population of `0.4`, the population eventually settles at `0.615` <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. The initial population choice does not affect this long-term equilibrium value <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

The equilibrium population varies with the growth rate `R` <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. If `R` is below 1, the population goes extinct (equilibrium value is zero) <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. Above `R = 1`, the population stabilizes at a constant value, which increases as `R` increases <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

## Period Doubling Bifurcations

A peculiar phenomenon occurs when `R` passes 3: the equilibrium point splits in two <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. The population no longer settles on a single constant value but oscillates between two distinct values, exhibiting a two-year cycle <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. This cyclic nature is observed in natural populations <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

As `R` continues to increase, each of these two values splits again, leading to a four-year cycle before repeating <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. These events are known as **period doubling bifurcations** <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. This process continues, leading to cycles of 8, 16, 32, 64, and so on, occurring faster and faster <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

## Emergence of Chaos

At `R = 3.57`, the system enters a state of [[Bifurcation and chaos theory | chaos]] <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. In this state, the population never settles down but bounces around seemingly at random, without any repeating pattern <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. Despite being a deterministic equation, it provided one of the first methods for generating pseudo-random numbers on computers <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

Surprisingly, as `R` increases further, order can return in "windows of stable periodic behavior" amid the [[Bifurcation and chaos theory | chaos]] <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. For example, at `R = 3.83`, a stable cycle with a period of 3 years emerges <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. This period then undergoes its own period doubling, splitting into cycles of 6, 12, 24, and so on, before returning to [[Bifurcation and chaos theory | chaos]] <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. In fact, this single equation contains periods of every possible length <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

## Connection to [[fractals_and_the_mandelbrot_set | Fractals and the Mandelbrot Set]]

The bifurcation diagram, which plots the long-term population values against `R`, exhibits self-similarity, a characteristic of [[fractals_and_the_mandelbrot_set | fractals]] <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. Zooming in reveals this fractal nature <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

Remarkably, the bifurcation diagram is directly part of the [[fractals_and_the_mandelbrot_set | Mandelbrot set]] <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. The [[fractals_and_the_mandelbrot_set | Mandelbrot set]] is based on the iterated equation `Zn+1 = Zn^2 + C`, where `C` is a complex number <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. Numbers `C` for which `Z` remains finite after unlimited iterations are part of the set <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

When the iteration of `Zn+1 = Zn^2 + C` is plotted with the iterated value on the Z-axis, looking from the side reveals the bifurcation diagram <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. This visualization shows:
*   Numbers in the main cardioid stabilize to a single constant value <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
*   Numbers in the main bulb oscillate between two values <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   Subsequent bulbs correspond to oscillations of periods 4, 8, 16, and so on <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
*   The chaotic part of the bifurcation diagram corresponds to the "needle" of the [[fractals_and_the_mandelbrot_set | Mandelbrot set]] <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.
*   A medallion resembling a smaller version of the entire [[fractals_and_the_mandelbrot_set | Mandelbrot set]] corresponds to the period-3 stability window in the bifurcation plot <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

## Real-World Manifestations of Chaos

The logistic map's behavior extends beyond theoretical models, appearing in diverse scientific fields <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>:

*   **Fluid Convection**: Fluid dynamicist Lib Taber observed period doubling and [[Bifurcation and chaos theory | chaos]] in a rectangular box of mercury with a temperature gradient inducing convection <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. Regular temperature spikes transitioned to a wobble, then period-2, period-4, and eventually chaotic behavior as the temperature gradient increased <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. This provided a "spectacular confirmation of the theory" <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.
*   **Biological Systems**:
    *   **Eye Response**: Studies on human and salamander eyes show period doubling in response to flickering lights; beyond a certain flicker rate, eyes respond only to every other flicker <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
    *   **Heart Fibrillation**: Experiments with rabbits demonstrated the period doubling route to [[Bifurcation and chaos theory | chaos]] in heart fibrillation <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>. A periodic beat progressed to a two-cycle, then a four-cycle, and eventually to aperiodic behavior <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. Scientists even used [[Bifurcation and chaos theory | chaos theory]] to determine optimal timing for electrical shocks to return the heart to periodicity <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.
*   **Dripping Faucets**: While often perceived as regular, dripping faucets can exhibit period doubling and eventually chaotic dripping by subtly adjusting the flow rate <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>. This makes it an easily observable chaotic system <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.

## The Feigenbaum Constant and Universality

Physicist Mitchell Feigenbaum discovered a universal constant related to these bifurcations <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>. By dividing the width of each bifurcation section by the next, he found the ratio converged to approximately `4.669` <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. This value is now known as the **Feigenbaum constant** <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>.

This constant is considered a fundamental constant of nature, independent of other known physical constants, and its origin is still unknown <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>. Even more remarkably, this universality means that *any* iterated equation with a single hump (like `xn+1 = sin(X)`) will exhibit period doubling bifurcations with the *same* scaling ratio of `4.669` <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>. This suggests a fundamental and universal aspect of how simple systems can generate complex behaviors <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.

## Significance

In 1976, biologist Robert May published a pivotal paper in *Nature* about the logistic equation, which "sparked a revolution" in the study of [[Bifurcation and chaos theory | chaos]] <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>. May advocated for teaching students about this simple equation to provide intuition for how simple rules can lead to very complex behaviors <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.