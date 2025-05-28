---
title: Feigenbaum constant and universality
videoId: ovJcsL7vyrk
---

From: [[veritasium]] <br/> 

The [[Feigenbaum constant and universality | Feigenbaum constant]] is a fundamental constant in chaos theory that describes the ratio at which period-doubling bifurcations occur in non-linear systems before they transition to chaos <a class="yt-timestamp" data-t="14:32:00">[14:32:00]</a>. This constant, approximately 4.669, demonstrates a remarkable universality in how diverse systems behave <a class="yt-timestamp" data-t="14:40:00">[14:40:00]</a>, <a class="yt-timestamp" data-t="15:33:00">[15:33:00]</a>.

## The Logistic Map: A Simple Equation with Complex Behavior
The connection between seemingly disparate phenomena like a dripping faucet, population dynamics, thermal convection, and neuronal firing can be understood through a single simple equation: the logistic map <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>, <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

The logistic map is defined as:
$X_{n+1} = R X_n (1 - X_n)$
Where:
*   $X_n$ represents the population in the current year (as a percentage of the theoretical maximum, ranging from 0 to 1) <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.
*   $X_{n+1}$ represents the population in the next year <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>.
*   $R$ is the growth rate <a class="yt-timestamp" data-t="00:41:00">[00:41:00]</a>.

This equation is the simplest possible model that includes a negative feedback loop: as the population (X) approaches its theoretical maximum, the $(1-X)$ term constrains further growth <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>, <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>. When graphed, the relationship between $X_n$ and $X_{n+1}$ forms an inverted parabola <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>.

## Period Doubling Bifurcations and the Onset of Chaos
The long-term behavior of the logistic map varies significantly with the growth rate $R$:

*   **Stable Equilibrium (R < 3)**: For low values of R (e.g., R=2.6), the population eventually stabilizes onto a single constant value, regardless of the initial population <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>, <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. If R falls below 1, the population goes extinct <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>. As R increases, the equilibrium population also increases <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>.

*   **Period Doubling (R > 3)**: Once R exceeds 3, the stable equilibrium breaks down. The population no longer settles on a single value; instead, it oscillates between two distinct values <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>, <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>. As R further increases, each of these two values splits again, leading to an oscillation between four values, then eight, sixteen, and so on <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>, <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a>. These events are known as "period doubling bifurcations" because the length of the cycle doubles <a class="yt-timestamp" data-t="04:58:00">[04:58:00]</a>.

*   **Chaos (R ≈ 3.57)**: At approximately R = 3.57, the system enters a chaotic state <a class="yt-timestamp" data-t="05:11:00">[05:11:00]</a>. In this regime, the population never settles into a predictable cycle but instead bounces around seemingly at random <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>. This property made the logistic map one of the first methods for generating pseudo-random numbers on computers <a class="yt-timestamp" data-t="05:24:00">[05:24:00]</a>.

*   **Windows of Order**: Surprisingly, even within the chaotic region, there are "windows of stable periodic behavior" <a class="yt-timestamp" data-t="05:46:00">[05:46:00]</a>. For example, at R = 3.83, a stable cycle with a period of 3 years emerges, which then undergoes its own sequence of period doublings (6, 12, 24, etc.) before returning to chaos <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a>, <a class="yt-timestamp" data-t="06:03:00">[06:03:00]</a>. This one equation can contain periods of every possible length <a class="yt-timestamp" data-t="06:10:00">[06:10:00]</a>.

The graph plotting the equilibrium population values against R is known as the **bifurcation diagram**. This diagram exhibits fractal properties, meaning its large-scale features are repeated on smaller scales <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>, <a class="yt-timestamp" data-t="06:30:00">[06:30:00]</a>.

## Connection to the [[connection_between_the_bifurcation_diagram_and_the_mandelbrot_set | Mandelbrot Set]]
The bifurcation diagram of the logistic map is intrinsically linked to the [[connection_between_the_bifurcation_diagram_and_the_mandelbrot_set | Mandelbrot set]], arguably the most famous fractal <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>. The Mandelbrot set is based on the iterated equation $Z_{n+1} = Z_n^2 + C$, where C is a complex number <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>. A number C is part of the Mandelbrot set if the iterated values of Z remain finite; otherwise, it is not <a class="yt-timestamp" data-t="07:04:00">[07:04:00]</a>, <a class="yt-timestamp" data-t="07:09:00">[07:09:00]</a>.

When the Mandelbrot set is visualized not just by its boundary but by plotting the actual iterated Z values on a third axis, a side view reveals the bifurcation diagram <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>, <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>.

*   Numbers C within the main cardioid of the Mandelbrot set correspond to systems that stabilize to a single constant value <a class="yt-timestamp" data-t="08:53:00">[08:53:00]</a>.
*   Numbers C in the primary bulb off the main cardioid correspond to systems oscillating between two values (period 2) <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>.
*   Subsequent bulbs correspond to periods of four, eight, sixteen, and so on <a class="yt-timestamp" data-t="09:11:00">[09:11:00]</a>.
*   The chaotic part of the bifurcation diagram corresponds to the "needle" of the Mandelbrot set, where it becomes very thin <a class="yt-timestamp" data-t="09:19:00">[09:19:00]</a>.
*   Smaller medallions within the needle, resembling the entire Mandelbrot set, correspond to windows of stability, such as the period 3 cycle <a class="yt-timestamp" data-t="09:31:00">[09:31:00]</a>, <a class="yt-timestamp" data-t="09:38:00">[09:38:00]</a>.

## Universality and the Feigenbaum Constant
The behavior observed in the logistic map is not unique to this specific equation but is a universal phenomenon. This universality extends to many other non-linear systems in nature:

*   **Population Dynamics**: The logistic map accurately models animal populations, especially in controlled laboratory environments <a class="yt-timestamp" data-t="10:28:00">[10:28:00]</a>.
*   **Thermal Convection**: Experiments by fluid dynamicist Lib Taber showed period doubling in mercury convection. As a temperature gradient was increased, stable convection patterns transitioned to oscillations between two states, then four, and so on, confirming the theory <a class="yt-timestamp" data-t="10:49:00">[10:49:00]</a>, <a class="yt-timestamp" data-t="11:35:00">[11:35:00]</a>.
*   **Biological Systems**:
    *   The response of human and salamander eyes to flickering lights exhibits period doubling <a class="yt-timestamp" data-t="12:03:00">[12:03:00]</a>.
    *   Studies on rabbit hearts induced into fibrillation revealed the period-doubling route to chaos (periodic beat to two-cycle, then four-cycle, and eventually aperiodic behavior). Chaos theory was even used to determine optimal timing for electrical shocks to restore normal heart rhythm <a class="yt-timestamp" data-t="12:30:00">[12:30:00]</a>, <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>.
*   **Dripping Faucets**: Even a common dripping faucet can exhibit period doubling and chaotic behavior simply by adjusting the flow rate <a class="yt-timestamp" data-t="13:30:00">[13:30:00]</a>, <a class="yt-timestamp" data-t="13:41:00">[13:41:00]</a>, <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>.

Physicist Mitchell Feigenbaum observed a peculiar pattern in these bifurcations <a class="yt-timestamp" data-t="14:32:00">[14:32:00]</a>. He found that the ratio of the width of each bifurcation section to the next one converges to a constant value, now known as the **Feigenbaum constant**, which is approximately 4.669 <a class="yt-timestamp" data-t="14:35:00">[14:35:00]</a>, <a class="yt-timestamp" data-t="14:40:00">[14:40:00]</a>. This constant is considered a fundamental constant of nature, unrelated to other known physical constants <a class="yt-timestamp" data-t="14:59:00">[14:59:00]</a>.

The most astonishing aspect is its **universality**: any iterated equation that has a single "hump" (a single maximum, like $X_{n+1} = \sin(X_n)$) will exhibit these same period-doubling bifurcations, and the ratio of their occurrences will converge to the same [[Feigenbaum constant and universality | Feigenbaum constant]] <a class="yt-timestamp" data-t="15:10:00">[15:10:00]</a>, <a class="yt-timestamp" data-t="15:22:00">[15:22:00]</a>, <a class="yt-timestamp" data-t="15:40:00">[15:40:00]</a>. This highlights something profoundly universal about how simple deterministic systems can lead to complex and chaotic behaviors <a class="yt-timestamp" data-t="15:51:00">[15:51:00]</a>.

In 1976, biologist Robert May published a paper in *Nature* about the logistic map, sparking a revolution in the study of chaos <a class="yt-timestamp" data-t="16:06:00">[16:06:00]</a>. He advocated for teaching this simple equation to students to illustrate how simple things can create very complex behaviors <a class="yt-timestamp" data-t="16:18:00">[16:18:00]</a>.