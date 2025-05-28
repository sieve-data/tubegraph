---
title: Fractals and the Mandelbrot set
videoId: ovJcsL7vyrk
---

From: [[veritasium]] <br/> 

The relationship between seemingly disparate phenomena like a dripping faucet, a population of rabbits, thermal convection, and the firing of neurons can be explained by a single simple equation [00:00:01]. This equation, when iterated, reveals complex behaviors including [[bifurcation_and_chaos_theory | chaos]] and fractal patterns, most notably exemplified by the Mandelbrot set.

## The Logistic Map

The core equation illustrating these concepts is the **Logistic Map** [00:01:16]. It is a mathematical model often used to represent how a population, such as rabbits, changes over time [00:00:30].

Initially, a simple model might suggest exponential growth by multiplying the current population (X) by a growth rate (R) [00:00:39]. However, this implies infinite growth [00:00:49]. To introduce environmental constraints, a term `(1 - X)` is added, where X is a percentage of the theoretical maximum population (from 0 to 1) [00:00:52]. As the population approaches its maximum, this term approaches zero, thus constraining growth [00:01:05].

The Logistic Map equation is:
`Xn+1 = R * Xn * (1 - Xn)` [00:01:16]
*   `Xn+1` is the population next year
*   `Xn` is the population this year
*   `R` is the growth rate

Graphing `Xn+1` versus `Xn` reveals an inverted parabola, representing a negative feedback loop: the larger the population gets, the smaller it will be the following year [00:01:27].

### Long-Term Behavior and Equilibrium

When the Logistic Map is iterated over many generations, its long-term behavior is observed [00:02:05]. For certain values of R, the population will stabilize at a constant equilibrium value, regardless of the initial population [00:02:50]. For example, with R=2.6 and a starting population of 0.4, the population eventually stabilizes around 0.615 [00:01:42, 00:02:30, 00:02:50].

If the growth rate R falls below 1, the population drops and eventually goes extinct, resulting in an equilibrium value of zero [00:03:27].

### Period Doubling Bifurcations and Chaos

As the growth rate (R) increases, the system exhibits more complex behaviors:

*   **Period-1 Stable State**: For low values of R (e.g., R=1 to R=3), the population stabilizes at a single constant value [00:03:59].
*   **Period-2 Cycle**: Once R passes 3, the equilibrium value splits into two [00:04:11]. The population no longer settles on a single value but oscillates between two distinct values, cycling between a higher and lower population each year [00:04:20]. This is known as a period doubling [[bifurcation_and_chaos_theory | bifurcation]] [00:05:00].
*   **Period-4, 8, 16, etc. Cycles**: As R continues to increase, each branch splits again, leading to cycles of four, eight, sixteen, and more values before repeating [00:04:45, 00:05:08]. These bifurcations occur faster and faster [00:05:06].
*   **[[bifurcation_and_chaos_theory | Chaos]]**: At approximately R = 3.57, the system enters a chaotic regime [00:05:11]. The population never settles and bounces around as if at random [00:05:17]. This equation was one of the first methods for generating pseudo-random numbers on computers [00:05:24].
*   **Windows of Stability**: Surprisingly, within the chaotic region, there are "windows" where stable, periodic behavior returns [00:05:46]. For instance, at R = 3.83, a stable cycle with a period of three years emerges [00:05:54]. As R further increases, this three-year cycle undergoes its own period doubling bifurcations, splitting into 6, 12, 24, and so on, before returning to chaos [00:06:03]. In fact, this single equation contains periods of every possible length [00:06:10].

## The Bifurcation Diagram and Fractals

The graph plotting the equilibrium population (y-axis) against the growth rate R (x-axis) is called a **[[bifurcation_and_chaos_theory | bifurcation]] diagram** [00:03:37]. When viewed, it appears self-similar, where large-scale features are repeated on smaller scales [00:06:23]. Zooming in confirms that it is indeed a **fractal** [00:06:30].

## The Mandelbrot Set Connection

The **Mandelbrot set** is arguably the most famous fractal [00:06:37]. It is based on a different iterated equation:
`Z(n+1) = Z(n)^2 + C` [00:06:52]
*   `C` is a starting complex number (any number in the complex plane) [00:06:57].
*   The iteration starts with `Z = 0` [00:07:02].

A number `C` is part of the Mandelbrot set if the iterated value of Z remains finite after unlimited iterations; otherwise, it is not [00:07:06]. For example, for C=1, the values quickly "blow up" to [[mathematical_paradoxes_of_infinity | infinity]] (0, 1, 2, 5, 26...), so 1 is not in the set [00:07:19]. For C=-1, the values oscillate between -1 and 0 (0, -1, 0, -1...), remaining finite, so -1 is in the set [00:07:43].

Typically, images of the Mandelbrot set show only the boundary between numbers that remain finite and those that blow up [00:08:07]. However, if the iteration is performed thousands of times and the value of Z is plotted on a third axis, the **[[bifurcation_and_chaos_theory | bifurcation]] diagram** is revealed when viewed from the side [00:08:25, 00:08:38].

This connection shows that:
*   Numbers within the main cardioid of the Mandelbrot set correspond to systems that stabilize on a single constant value [00:08:53].
*   Numbers in the main bulb (to the left of the main cardioid) correspond to systems oscillating between two values (period 2) [00:09:03].
*   Subsequent bulbs correspond to cycles of four, eight, sixteen, and thirty-two values, and so on [00:09:09].
*   The chaotic part of the [[bifurcation_and_chaos_theory | bifurcation]] diagram corresponds to the "needle" of the Mandelbrot set, where it becomes very thin [00:09:19].
*   Stable windows of periodicity, like the period-3 window in the [[bifurcation_and_chaos_theory | bifurcation]] plot, correspond to smaller, self-similar medallions within the Mandelbrot set [00:09:31].

The other bulbs off the main cardioid of the Mandelbrot set, which exist in the complex plane, also have periodic cycles (e.g., period 3, 4, 5), and viewing them in the Z-axis reveals "ghostly images" of these oscillations [00:09:48].

## Universality and the Feigenbaum Constant

In 1976, physicist Mitchell Feigenbaum observed a remarkable pattern in the bifurcations [00:14:29]. He divided the width of each [[bifurcation_and_chaos_theory | bifurcation]] section by the next one and found that this ratio consistently converged on a specific number: approximately **4.669** [00:14:35]. This number is now known as the **Feigenbaum constant** [00:14:46].

What makes this constant particularly profound is its universality [00:15:51]:
*   It does not depend on the specific form of the iterated equation [00:15:10].
*   Any equation that has a single hump (e.g., `Xn+1 = sin(Xn)`) will exhibit period doubling bifurcations at the same scaling ratio, approaching 4.669 [00:15:16].

This universality suggests something fundamental about these iterative processes [00:15:55]. The Feigenbaum constant is considered a fundamental constant of nature, yet its origin is not related to any other known physical constant [00:14:59].

## Real-World Applications

The Logistic Map and its emergent [[bifurcation_and_chaos_theory | chaotic]] behaviors have found applicability across various scientific fields:

*   **Population Modeling**: The equation accurately models animal populations, especially in controlled laboratory environments [00:10:28]. Natural populations also exhibit cyclic behavior, akin to the Logistic Map's two-year cycle [00:04:34].
*   **Fluid Dynamics**: Physicist Lib Taber demonstrated period doubling in fluid convection. By increasing the temperature gradient in mercury, he observed a stable periodic temperature spike that then developed a wobble (period-2), followed by period-4, and then period-8 behaviors, strikingly confirming the theoretical predictions [00:10:49].
*   **Physiology**:
    *   **Eye Response**: Studies on human and salamander eyes to flickering lights show a period doubling effect, where the eyes respond to every other flicker once the rate reaches a certain threshold [00:12:03].
    *   **Heart Fibrillation**: Research involving rabbits given a drug to induce heart fibrillation showed a period doubling route to [[bifurcation_and_chaos_theory | chaos]]. The heart's beat progressed from periodic to a two-cycle, then a four-cycle, and eventually to aperiodic behavior [00:12:30]. This understanding allowed scientists to use [[bifurcation_and_chaos_theory | chaos theory]] to determine when to apply electrical shocks to return the heart to periodicity [00:13:06].
*   **Dripping Faucets**: While seemingly regular, dripping faucets can exhibit period doubling and even [[bifurcation_and_chaos_theory | chaotic]] behavior as the flow rate increases, with drips coming in cycles of two or more before becoming entirely unpredictable [00:13:33]. This demonstrates that even a seemingly simple system with constant pressure and aperture can produce [[bifurcation_and_chaos_theory | chaos]] [00:13:57].

## Significance

In 1976, biologist Robert May published a paper in *Nature* about this simple equation, sparking a revolution in how scientists viewed complex systems [00:16:06]. He advocated for teaching this equation to students, emphasizing how simple rules can generate very complex behaviors [00:16:18]. This intuition challenges the traditional teaching of simple equations leading only to simple outcomes [00:16:39]. The ability of such a straightforward equation to generate [[bifurcation_and_chaos_theory | chaos]] and reveal universal constants like the Feigenbaum constant is a testament to the profound nature of iterated functions [00:16:55].