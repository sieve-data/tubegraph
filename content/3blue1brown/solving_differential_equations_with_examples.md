---
title: Solving differential equations with examples
videoId: p_di4Zn4wz4
---

From: [[3blue1brown]] <br/> 

Differential equations are fundamental to describing the laws of physics and are widely applicable beyond just physical phenomena <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Understanding them provides a new perspective on the world <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This article provides an overview of [[basics_and_significance_of_differential_equations | differential equations]], offering a big-picture view while also delving into specific examples <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Basic calculus knowledge (derivatives, integrals) is assumed, with some linear algebra needed for later concepts <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Why Differential Equations Arise <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>

[[basics_and_significance_of_differential_equations | Differential equations]] are used when it's simpler to describe how something *changes* rather than its absolute state <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. For instance, it's easier to explain why population sizes grow or shrink than their exact values at a specific time <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. In [[differential_equations_in_physics | Newtonian mechanics]], motion is described by force, and force determines acceleration, which is a statement about change <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Types of Differential Equations <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>

[[ordinary_differential_equations_odes_vs_partial_differential_equations_pdes | Differential equations]] generally come in two forms:
*   **Ordinary Differential Equations (ODEs)**: Involve functions with a single input, often representing time <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. These focus on a finite collection of values changing over time <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **Partial Differential Equations (PDEs)**: Deal with functions having multiple inputs <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. They typically involve a continuum of values changing, such as temperature at every point of a solid body or fluid velocity in space <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. [[introduction_to_partial_differential_equations | Partial differential equations]] will be explored more closely in subsequent discussions <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## Solving a Simple ODE: Projectile Motion <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>

[[differential_equations_in_physics | Physics]] offers a good starting point for simple examples <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. Consider the trajectory of an object thrown in the air <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. Near Earth's surface, gravity causes a downward acceleration of 9.8 meters per second per second (denoted as 'g') <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. This means that velocity vectors gain an additional downward component of 9.8 m/s every second <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

### Setting up the Equation <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>
Focus on the y-coordinate as a function of time. Its first derivative (`y-dot`) is the vertical velocity, and its second derivative (`y-double-dot`) is the vertical acceleration <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. The equation is:
$$ \frac{d^2y}{dt^2} = y\text{-double-dot} = -g $$ <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>

### Solving by Integration <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>
To solve this, we integrate backwards:
1.  **Find Velocity**: What function has `-g` as a derivative?
    $$ y\text{-dot} = -gt + v_0 $$
    where $v_0$ is the initial velocity. An extra degree of freedom (the constant of integration) is determined by an initial condition <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
2.  **Find Position**: What function has `-gt + v_0` as a derivative?
    $$ y = -\frac{1}{2}gt^2 + v_0t + y_0 $$
    where $y_0$ is the initial position. Again, an additional constant is determined by the initial position <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

This demonstrates how a [[basics_and_significance_of_differential_equations | differential equation]] is solved by finding a function based on information about its rate of change <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

## More Complex ODEs: Gravitational Force & Pendulum <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>

Problems become more complex when forces depend on the body's position <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. For instance, in planetary motion, gravity is not constant but inversely proportional to the square of the distance between bodies <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. Here, acceleration is a function of position, creating a "dance between two mutually interacting variables" <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. Often, puzzles in [[basics_and_significance_of_differential_equations | differential equations]] involve finding a function whose derivatives are defined in terms of the function itself <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.

In [[differential_equations_in_physics | physics]], second-order [[ordinary_differential_equations_odes_vs_partial_differential_equations_pdes | differential equations]] (where the highest derivative is the second derivative) are common <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. Solving them feels like an "infinite continuous jigsaw puzzle" <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

### The Pendulum Example <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>
The pendulum is a classic example. While often approximated as simple harmonic motion (a sine wave) with a period of $2\pi\sqrt{l/g}$ for small angles, actual pendulums behave differently at larger angles <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. The period is longer, and the motion doesn't look like a sine wave <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

#### Setting up the Pendulum Equation <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>
Let $\theta$ be the angle with the vertical, and $x = l\theta$ be the distance along the arc <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. The component of gravity in the direction of motion (opposite to displacement) is $-g \sin(\theta)$ <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
The acceleration along the arc is $x\text{-double-dot} = -g \sin(\theta)$ <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
Since $x = l\theta$, we have $x\text{-double-dot} = l \theta\text{-double-dot}$. Thus, the equation for $\theta$ is:
$$ \theta\text{-double-dot} = -\frac{g}{l} \sin(\theta) $$ <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>
Adding air resistance (proportional to velocity), represented by a constant $\mu$:
$$ \theta\text{-double-dot} = -\frac{g}{l} \sin(\theta) - \mu \theta\text{-dot} $$ <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>
This equation is "particularly juicy" because it's not easy to solve analytically <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>. The $\sin(\theta)$ term is precisely why real pendulums *don't* oscillate with a sine wave pattern <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

### Difficulty of Analytic Solutions <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>
[[basics_and_significance_of_differential_equations | Differential equations]] are "really freaking hard to solve" <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. For the pendulum without damping, an analytic solution exists but is "hilariously complicated," involving functions rarely seen and complex integrals <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. With the damping term, often no known exact analytic solution exists <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. This means we often "short circuit" the actual solution process and go directly to building understanding and making computations from the equations <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

## Understanding without Analytic Solutions: Phase Space <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>

A powerful way to understand the behavior of systems governed by [[ordinary_differential_equations_odes_vs_partial_differential_equations_pdes | differential equations]] is through visualizing their "state" in a [[applications_of_phase_space_in_differential_equations | phase space]] <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.

### What is Phase Space? <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>
The "state" of a pendulum can be described by two numbers: its angle ($\theta$) and its angular velocity ($\theta\text{-dot}$) <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. These two values define a point in a two-dimensional [[applications_of_phase_space_in_differential_equations | phase space]] <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>. Each point in this space represents a possible initial condition <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.

For a damped pendulum, a typical trajectory in [[applications_of_phase_space_in_differential_equations | phase space]] is an inward spiral, signifying that peak velocity and displacement decrease with each swing <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. The point spirals towards the origin ($\theta=0, \theta\text{-dot}=0$), where the pendulum is still <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. It's crucial to remember that [[applications_of_phase_space_in_differential_equations | phase space]] is an abstract representation, distinct from the physical space of the pendulum <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

### Vector Fields in Phase Space <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>
A [[basics_and_significance_of_differential_equations | differential equation]] can be visualized as a vector field in [[applications_of_phase_space_in_differential_equations | phase space]] <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>. The pendulum's state is a vector $(\theta, \theta\text{-dot})$ <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. Its rate of change (how it moves in this diagram) is given by its derivative: $(\theta\text{-dot}, \theta\text{-double-dot})$ <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>. Since $\theta\text{-double-dot}$ is expressed in terms of $\theta$ and $\theta\text{-dot}$ by the [[basics_and_significance_of_differential_equations | differential equation]], every point in [[applications_of_phase_space_in_differential_equations | phase space]] has a specific velocity vector <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.

This effectively breaks a single second-order [[ordinary_differential_equations_odes_vs_partial_differential_equations_pdes | differential equation]] into a system of two first-order equations <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>. Solving the equation means finding a trajectory in this space where the point's velocity at every moment matches the vector from the field <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>.

#### Insights from Phase Space <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>
*   **High Initial Velocity**: Regions where $\theta\text{-dot}$ is high show vectors guiding the point to travel far right before spiraling inward <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>. This corresponds to a pendulum with enough initial velocity to rotate fully multiple times before settling into decaying oscillations <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>.
*   **Parameter Effects**: Changing the air resistance term ($\mu$) in the equation immediately shows how trajectories spiral inward faster, meaning the pendulum slows down quicker <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>. This provides intuition that might not be obvious from the equations alone <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.

### Higher Dimensions and Generalization <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>
Any system of [[ordinary_differential_equations_odes_vs_partial_differential_equations_pdes | ordinary differential equations]] can be described by a vector field like this, making it a very general way to understand their behavior <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>. While the pendulum is 2D, systems like the three-body problem (three masses in 3D space with gravity) have 18 degrees of freedom, resulting in an 18-dimensional [[applications_of_phase_space_in_differential_equations | phase space]] <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.

The concept of [[applications_of_phase_space_in_differential_equations | phase space]] has been called "one of the most powerful inventions of modern science" <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>. It allows for questions about a whole spectrum of initial states, not just a single one <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>. The collection of all possible trajectories is called **phase flow** <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>.

#### Stability Analysis <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>
[[applications_of_phase_space_in_differential_equations | Phase space]] is useful for analyzing stability. Fixed points in the space (where $\theta$ and $\theta\text{-dot}$ are zero, representing a still pendulum, either hanging down or perfectly balanced upright) can be assessed for stability: do tiny nudges cause the system to return to the fixed point or move away from it? <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a> This is intuited by observing whether the phase flow tends to contract or expand around the fixed point <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>.

## Applications Beyond Physics: Love Dynamics <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>

[[basics_and_significance_of_differential_equations | Differential equations]] extend beyond [[differential_equations_in_physics | physics]] <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>. Stephen Strogatz's work on modeling affection provides a whimsical example <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>.

Imagine a scenario where:
*   Your affection increases when your companion shows interest and decreases when they seem colder <a class="yt-timestamp" data-t="00:21:19">[00:21:19]</a>.
*   Your companion is attracted when you seem uninterested but turned off when you are too keen <a class="yt-timestamp" data-t="00:21:35">[00:21:35]</a>.

The [[applications_of_phase_space_in_differential_equations | phase space]] for these "romance equations" can look very similar to the pendulum diagram, showing endless cycles of affection and repulsion, like pendulum swings <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>. If your partner's feelings are slowed by fear of vulnerability (analogous to friction), the system trends towards an inward spiral of mutual ambivalence <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.

This highlights that two vastly different systems (a physical pendulum and interpersonal dynamics) can share a similar underlying mathematical structure, especially evident in their [[applications_of_phase_space_in_differential_equations | phase diagrams]] <a class="yt-timestamp" data-t="00:22:21">[00:22:21]</a>. The tactics developed for one case can often be transferred to many others <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>.

## Numerical Methods for Solving Differential Equations <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>

When exact analytic solutions are impossible, [[numerical_methods_for_solving_differential_equations | numerical methods for solving differential equations]] provide a way to approximate solutions <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.

### Basic Idea: Finite Time Steps <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>
The core idea is to simulate the system by taking small, finite time steps. If you are at a point in the [[applications_of_phase_space_in_differential_equations | phase diagram]], you take a step equal to `delta_t` (a small time increment) multiplied by the vector at that point <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>. Repeating this process for many small steps provides an approximation of the trajectory over time <a class="yt-timestamp" data-t="00:23:34">[00:23:34]</a>. A smaller `delta_t` leads to a more accurate approximation but requires more steps <a class="yt-timestamp" data-t="00:23:52">[00:23:52]</a>.

### Example: Python Program for Pendulum <a class="yt-timestamp" data-t="00:24:19">[00:24:19]</a>
A simple Python program can numerically solve the pendulum equation:
1.  Define initial `theta` and `theta_dot` (e.g., `theta = pi/3`, `theta_dot = 0`) <a class="yt-timestamp" data-t="00:24:34">[00:24:34]</a>.
2.  Set a small `delta_t` (e.g., 0.01) <a class="yt-timestamp" data-t="00:24:52">[00:24:52]</a>.
3.  Loop through time steps:
    *   Increase `theta` by `theta_dot * delta_t` <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>.
    *   Compute `theta_double_dot` using the [[ordinary_differential_equations_odes_vs_partial_differential_equations_pdes | differential equation]] <a class="yt-timestamp" data-t="00:25:02">[00:25:02]</a>.
    *   Increase `theta_dot` by `theta_double_dot * delta_t` <a class="yt-timestamp" data-t="00:25:06">[00:25:06]</a>.
4.  Return the final `theta` value after all steps <a class="yt-timestamp" data-t="00:25:11">[00:25:11]</a>.

This is a basic form of [[numerical_methods_for_solving_differential_equations | numerical methods for solving differential equations]], which can be made more sophisticated for better accuracy and efficiency <a class="yt-timestamp" data-t="00:25:20">[00:25:20]</a>.

## Limitations and Chaos Theory <a class="yt-timestamp" data-t="00:25:30">[00:25:30]</a>

Even with numerical solutions, there are inherent limits to how well we can use these systems for prediction <a class="yt-timestamp" data-t="00:25:54">[00:25:54]</a>. Chaos theory, a major field that emerged in the last century, reveals that for some systems, tiny variations in initial conditions (due to imperfect measurements) can lead to wildly different trajectories <a class="yt-timestamp" data-t="00:25:58">[00:25:58]</a>. The three-body problem, for example, contains elements of chaos <a class="yt-timestamp" data-t="00:26:23">[00:26:23]</a>.

While it seems "cruel" that the universe's language is full of riddles that are either unsolvable or useless for long-term prediction, it also offers reassurance <a class="yt-timestamp" data-t="00:26:28">[00:26:28]</a>. It suggests that the complexity observed in the world can be studied within the math itself, rather than being solely due to a mismatch between model and reality <a class="yt-timestamp" data-t="00:26:45">[00:26:45]</a>.