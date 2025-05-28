---
title: Period doubling and chaos theory
videoId: ovJcsL7vyrk
---

From: [[veritasium]] <br/> 

A single, simple equation can describe seemingly unrelated phenomena such as a dripping faucet, the Mandelbrot set, rabbit populations, thermal convection, and the firing of neurons in the brain <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## The Logistic Map: Modeling Populations

The logistic map is a mathematical model often used to represent population growth, such as that of rabbits <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. The simplest model for population growth involves multiplying the current population (X) by a growth rate (R) <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. However, this leads to exponential, infinite growth <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. To account for environmental constraints, a term `(1 - X)` is added, where `X` represents the population as a percentage of the theoretical maximum (0 to 1) <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. As `X` approaches its maximum, this term goes to zero, limiting the population <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

The logistic map equation is: `X_n+1 = R * X_n * (1 - X_n)` <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
Graphing the next year's population (`X_n+1`) versus this year's (`X_n`) reveals an inverted parabola, representing the simplest equation with a negative feedback loop <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. This means a larger population in one year leads to a smaller population the next <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Long-Term Population Behavior

When the growth rate `R` is, for example, 2.6 and the initial population is 40% (0.4), iterating the equation shows the population stabilizing at an equilibrium value (e.g., 0.615) <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. This stability is common in wild populations where births and deaths balance <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. The initial population value doesn't affect the final equilibrium, only the path to it <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

Plotting the equilibrium population against the growth rate `R` (the bifurcation diagram) reveals different behaviors <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>:
*   For `R` values below 1, the population goes extinct (equilibrium is zero) <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   Once `R` hits 1, the population stabilizes to a constant value, which increases as `R` increases <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

## Period Doubling Bifurcations

The behavior becomes more complex when `R` increases further:
*   **Period 2**: Once `R` passes 3, the graph splits <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. The population no longer settles on a single value but oscillates between two values (a "two-year cycle") <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. This cyclic nature is observed in natural populations <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   **Higher Periods**: As `R` continues to increase, each branch splits again, leading to a four-year cycle, then eight, then sixteen, and so on <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. These events are known as "period doubling bifurcations" <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. The bifurcations occur faster and faster <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

## Chaos

At approximately `R` equals 3.57, the system enters a state of chaos <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. In this chaotic regime, the population never settles down and bounces around as if at random <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. This equation provided one of the first methods for generating pseudo-random numbers on computers, producing unpredictable results from a deterministic machine <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

### Windows of Stability

Despite the overall chaotic nature beyond `R` = 3.57, order can return within certain ranges of `R` <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. For example, at `R` = 3.83, there is a stable cycle with a period of 3 years <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. As `R` increases further within these "windows of stability," this 3-year cycle also undergoes period doubling, splitting into 6, 12, 24, and so on, before returning to chaos <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. Remarkably, this single equation contains periods of every possible length <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

## Connection to the Mandelbrot Set

The bifurcation diagram itself has a fractal appearance, with large-scale features repeating on smaller scales <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. Surprisingly, this diagram is actually part of the [[mandelbrot_set_and_fractals|Mandelbrot set]] <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

The [[mandelbrot_set_and_fractals|Mandelbrot set]] is based on the iterated equation `Z_n+1 = Z_n^2 + C`, where `C` is a complex number <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. If, starting with `Z`=0, iterating this equation keeps the value of `Z` finite, then `C` is part of the [[mandelbrot_set_and_fractals|Mandelbrot set]] <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. If `Z` "blows up" to infinity, `C` is not part of the set <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

When the Mandelbrot set is visualized by plotting the iterated `Z` value on a third axis, a side view reveals the bifurcation diagram <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   Numbers within the main "cardioid" of the [[mandelbrot_set_and_fractals|Mandelbrot set]] correspond to values that stabilize to a single constant (period 1) <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   The main "bulb" next to it corresponds to values that oscillate between two values (period 2) <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   Successive bulbs represent periods of 4, 8, 16, 32, and so on <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   The chaotic part of the bifurcation diagram corresponds to the "needle" of the [[mandelbrot_set_and_fractals|Mandelbrot set]] <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.
*   Windows of stability, like the period 3 cycle, correspond to smaller, self-similar medallions within the [[mandelbrot_set_and_fractals|Mandelbrot set]] <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
While the bifurcation diagram exists on the real line, the various "bulbs" off the main cardioid of the [[mandelbrot_set_and_fractals|Mandelbrot set]] also exhibit periodic cycles (e.g., period 3, 4, 5), creating "ghostly images" when viewed on the z-axis <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

## Real-World Demonstrations of Period Doubling and Chaos

This simple equation applies to a vast range of seemingly unrelated scientific areas <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.

### Fluid Dynamics
The first major experimental confirmation came from fluid dynamicist Lib Taber <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. He created a system with mercury and a temperature gradient to induce convection, resulting in two counter-rotating cylinders of fluid <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   Initially, temperature measurements showed regular, periodic spikes, similar to the logistic equation converging on a single value <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
*   As the temperature gradient increased, a "wobble" developed, causing spikes of two different heights (period 2) <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.
*   Further increases in temperature led to period doubling again, with four distinct temperatures before the cycle repeated, then eight <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. This was a significant confirmation of the theory <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.

### Biology and Medicine
*   **Eyesight**: Studies on human and salamander eyes exposed to flickering lights show period doubling. At a certain flicker rate, the eyes only respond to every other flicker, mimicking the bifurcation diagram <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
*   **Heart Fibrillation**: Scientists induced fibrillation in rabbits' hearts and observed the period doubling route to chaos <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>. The heart beat would transition from a periodic rhythm to a two-beat cycle, then a four-beat cycle, and eventually exhibit [[chaos_theory_and_predictability|aperiodic behavior]] <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. Crucially, researchers used [[chaos_theory_and_predictability|chaos theory]] to determine when to apply electrical shocks to successfully return the heart to periodicity <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.

### Dripping Faucet
While seemingly simple, a dripping faucet can exhibit complex behavior <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.
*   Increasing the flow rate slightly can lead to period doubling, where drips come in pairs ("tip-tip") <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.
*   Further adjustment can result in chaotic dripping, even with constant water pressure and aperture size <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. This makes it an easy system to observe chaotic behavior at home <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.

## The Feigenbaum Constant and Universality

The bifurcation diagram appears in so many disparate systems that it can seem "spooky" <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>. Physicist Mitchell Feigenbaum discovered a profound aspect of this phenomenon:
*   He observed the ratio of the widths of successive bifurcation sections <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.
*   This ratio converges to a universal constant: **4.669**, now known as the Feigenbaum constant <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.
*   This constant describes the rate at which bifurcations accelerate towards chaos <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.
*   The Feigenbaum constant is considered a fundamental constant of nature, distinct from other known physical constants <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>.

Even more remarkably, this universality is not limited to the specific form of the logistic map. *Any* iterated equation that has a single "hump" (e.g., `X_n+1 = R * sin(X_n)`) will exhibit the same period doubling behavior, and the ratio of where these bifurcations occur will converge to the same Feigenbaum constant <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>. This concept is referred to as "universality" because it points to something fundamental about this type of equation and the constant value <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.

## Historical Impact and Educational Significance

In 1976, biologist Robert May published a paper in *Nature* about the logistic equation, which sparked a revolution in the study of [[chaos_theory_and_predictability|chaos]] <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>. May advocated for teaching this simple equation to students because it provides intuition for how simple rules can generate very complex behaviors <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>. Despite its importance, the complexities of [[chaos_theory_and_predictability|chaos]] are not widely taught in conventional education <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.

> [00:16:26] "it gives you a new intuition for ways in which simple things simple equations can create very complex behaviors"
> [00:16:51] "maybe we should throw at least a little bit which is why I've been so excited about chaos and I am so excited about this equation"
> [00:16:55] "you know how did I get to be 37 years old without hearing of the Feigenbaum constant"

The study of [[chaos_theory_and_predictability|chaos]] and the logistic map provides a fascinating insight into the intricate patterns hidden within simple deterministic systems <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.