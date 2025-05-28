---
title: Logistic map and population modeling
videoId: ovJcsL7vyrk
---

From: [[veritasium]] <br/> 

The logistic map is a simple iterated equation that reveals a profound connection between seemingly unrelated phenomena like a dripping faucet, the Mandelbrot set, rabbit populations, thermal convection in fluids, and the firing of neurons in the human brain <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. It serves as a fundamental model for understanding how simple rules can lead to incredibly complex and even chaotic behaviors <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>.

## The Logistic Map Equation

The logistic map is typically used to model populations, such as rabbits, over time <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. A simple model where a population `X` is multiplied by a growth rate `R` would result in exponential growth forever <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. To account for environmental constraints, such as limited resources, a term `(1 - X)` is added <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. In this model, `X` represents the population as a percentage of its theoretical maximum, ranging from 0 to 1 <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. As `X` approaches this maximum, the `(1 - X)` term approaches zero, effectively constraining the population <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

The logistic map equation is defined as:
`Xn+1 = R * Xn * (1 - Xn)`
where `Xn+1` is the population in the next year, `Xn` is the population in the current year, and `R` is the growth rate <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. When graphed, the population next year versus the population this year forms an inverted parabola, illustrating a negative feedback loop: the larger the population, the smaller it will be the following year <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### Population Behavior and Bifurcations

The long-term behavior of the population modeled by the logistic map changes dramatically depending on the growth rate `R`:

*   **Stabilization or Extinction (R < 3)**:
    *   For `R` values less than 1, the population eventually goes extinct, reaching an equilibrium value of zero <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
    *   For `R` values between 1 and 3, the population stabilizes onto a single constant value, regardless of the initial population <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. This equilibrium value increases as `R` increases <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

*   **Period Doubling [[Bifurcation and chaos theory | Bifurcations]] (R > 3)**:
    *   Once `R` passes 3, the population no longer settles on a single constant value. Instead, it oscillates back and forth between two values, representing a two-year cycle <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. This phenomenon is known as a period doubling [[Bifurcation and chaos theory | bifurcation]] <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. Such cyclic population changes are observed in nature <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
    *   As `R` continues to increase, each of these two values splits again, leading to a four-year cycle, then an eight-year cycle, and so on (16, 32, 64) <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. The [[Bifurcation and chaos theory | bifurcations]] occur faster and faster <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

*   **[[Bifurcation and chaos theory | Chaos]] (R ≈ 3.57 and beyond)**:
    *   At approximately `R = 3.57`, the system enters a state of [[Bifurcation and chaos theory | chaos]] <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. In this chaotic region, the population never settles down but bounces around as if at random <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
    *   Despite being deterministic (given exact initial conditions, values can be calculated precisely), the behavior is unpredictable over time, making it one of the first methods used to generate [[random_number_selection | pseudo-random numbers]] on computers <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
    *   Even within the chaotic regime, there are "windows of stability" where order returns, exhibiting stable periodic behaviors, such as a stable cycle with a period of three years at `R = 3.83` <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. This simple equation can generate cycles of virtually any length <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

### Feigenbaum Constant and Universality

The bifurcation diagram, which plots the equilibrium population values against `R`, exhibits fractal properties, with large-scale features repeated on smaller scales <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

Physicist Mitchell Feigenbaum observed that the ratio of the width of each bifurcation section to the next one converges to a constant value, approximately 4.669 <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>. This is known as the Feigenbaum constant, a fundamental constant of nature that does not seem to relate to any other known physical constant <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>.

Even more remarkably, this universality means that any iterated equation with a single "hump" (like a quadratic or sine function) will exhibit period doubling [[Bifurcation and chaos theory | bifurcations]] with the same Feigenbaum constant governing the scaling of when these [[Bifurcation and chaos theory | bifurcations]] occur <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>. This indicates a deep, universal property of such non-linear systems <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.

## Connection to the Mandelbrot Set

The bifurcation diagram of the logistic map is intrinsically linked to the Mandelbrot set <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. The Mandelbrot set is based on the iterated equation `Zn+1 = Zn^2 + C`, where `C` is a complex number <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. A number `C` is part of the Mandelbrot set if the iterated value `Z` remains finite after unlimited iterations, starting with `Z = 0` <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

When the Mandelbrot set is visualized not just by its boundary but by plotting the actual values of the iteration on a third axis, looking at it from the side reveals the bifurcation diagram of the logistic map <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. Each "bulb" or feature on the Mandelbrot set corresponds to a specific periodic behavior in the iterated sequence:
*   The main cardioid corresponds to stabilization on a single constant value <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
*   The main bulb adjacent to the cardioid corresponds to oscillation between two values (period 2) <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   Subsequent bulbs correspond to periods of 4, 8, 16, and so on <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
*   The "needle" of the Mandelbrot set corresponds to the chaotic part of the bifurcation diagram <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
*   Windows of stability, like the period-3 window, correspond to smaller self-similar Mandelbrot sets within the larger structure <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

## [[applications_of_logistic_equations_in_science | Applications in Science]]

The logistic map and its associated phenomena, like period doubling and [[Bifurcation and chaos theory | chaos]], have been experimentally confirmed and applied across various scientific fields:

*   **Fluid Dynamics**
    *   Lib Taber's experiment with mercury inducing convection showed the transition from regular periodic temperature spikes to a period-two wobble, then period-four, and so on, confirming the period doubling route to [[Bifurcation and chaos theory | chaos]] <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

*   **Biology and Physiology**
    *   Studies on human and salamander eyes exposed to flickering lights show period doubling, where the eyes respond to every other flicker once the rate reaches a certain threshold <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
    *   Research on rabbit hearts induced into fibrillation revealed a period doubling route to [[Bifurcation and chaos theory | chaos]]: starting with a periodic beat, transitioning to a two-cycle, then a four-cycle, and eventually becoming aperiodic <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>. This understanding was used to apply electrical shocks strategically to return the heart to periodicity <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.

*   **Physics and Everyday Phenomena**
    *   Even a simple dripping faucet can exhibit period doubling and chaotic behavior just by adjusting its flow rate <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>. What appears to be a consistent system (constant pressure, constant aperture) can produce unpredictable dripping <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.

## Conclusion

The logistic map, despite its simple form, demonstrates how complex behaviors, including [[Bifurcation and chaos theory | chaos]], can emerge from straightforward deterministic equations <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>. Its universality, encapsulated by the Feigenbaum constant, reveals a fundamental mathematical structure underlying diverse natural phenomena. Robert May's 1976 paper on this equation sparked a revolution in the study of [[Bifurcation and chaos theory | chaos theory]], advocating for its inclusion in education to provide a new intuition for understanding complex systems <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.