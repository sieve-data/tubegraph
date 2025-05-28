---
title: Newtons Second Law and Variational Principles
videoId: Q10_srZ-pbs
---

From: [[veritasium]] <br/> 

A single, simple rule underpins all of physics, from classical mechanics to electromagnetism, quantum theory, and general relativity, down to the fundamental particles [00:00:00]. This rule can explain the behavior of life itself [00:00:30]. It suggests that the traditional "local picture" or differential equation way of thinking about the universe might be backwards [00:00:37].

## The Brachistochrone Problem: The Problem of Fastest Descent

The journey to uncovering this fundamental rule began with a simple problem: determining the shape of a ramp that would allow a mass to slide from point A to point B in the fastest possible time [00:00:51]. This is known as the problem of fastest descent [00:01:03].

Common sense might suggest a straight line from A to B [00:01:06]. However, bending the ramp downwards at the start allows the mass to accelerate to a higher speed earlier, which can result in a faster overall travel time, even if the distance traveled is slightly longer [00:01:12]. The challenge was to find the perfect balance between acceleration and path length to minimize travel time [00:01:24].

Galileo suggested that the arc of a circle would be the fastest, demonstrating it was quicker than any polygonal path [00:01:32]. However, this was not the ultimate solution [00:01:39].

In June 1696, Johann Bernoulli posed this problem as a challenge to the world's leading mathematicians [00:01:43]. Initially, no solutions were submitted within the six-month deadline [00:01:59]. Gottfried Leibniz persuaded Bernoulli to extend the deadline, likely targeting Isaac Newton, who was considered the best mathematician [00:02:04]. Despite Newton's current role as warden of the Mint, he received Bernoulli's challenge on January 29, 1697 [00:02:25]. Irritated but intrigued, Newton solved the problem by 4:00 AM the next morning, a feat that took Bernoulli two weeks [00:02:39]. Newton submitted his anonymous solution, which Bernoulli famously recognized, stating, "I recognize the lion by his claw" [00:03:02]. While Newton's solution was impressive, Bernoulli's approach was considered more clever and creative [00:03:27].

## Fermat's Principle of Least Time

Bernoulli's "truly creative, beautiful solution" [00:03:42] was inspired by an ancient problem concerning how light travels [00:03:46].

### Hero of Alexandria and Light Reflection
In the 1st century AD, Hero of Alexandria contemplated light's path [00:03:56]. He observed that in a single medium, such as air, light always follows the shortest path [00:04:01]. A consequence of this is that when light reflects, the angle of incidence equals the angle of reflection [00:04:07]. Any other path between the start and end points would be longer [00:04:15].

### Light Refraction and Snell's Law
However, when light passes from one medium into another (e.g., from air into water), it bends in a peculiar way, a phenomenon known as refraction [00:04:18]. This refracted light does not follow the shortest path [00:04:25]. For centuries, people gradually discovered that the sine of the angle of incidence divided by the sine of the angle of refraction is equal to a constant 'n', which depends on the two media [00:04:47]. This became known as [[Application of Calculus in Physics | Snell's Law]] [00:05:01]. The reason why it worked remained unknown until 1657 [00:05:04].

### Pierre Fermat's Contribution
Pierre Fermat, a judge by day and a mathematician by night, became interested in explaining why light obeys refraction [00:05:09]. He hypothesized that Hero of Alexandria was on the right track, but it wasn't distance that was being minimized, but rather *time* [00:05:34]. Fermat realized that if light takes the path of shortest travel time, [[Application of Calculus in Physics | Snell's Law]] naturally emerges [00:06:18]. The constant 'n' in Snell's Law is simply the ratio of the speed of light in the first medium to the speed of light in the second medium [00:06:30]. Fermat described this calculation as "the most extraordinary, the most unforeseen, and the happiest calculation" of his life [00:06:42]. This was significant as it was one of the first demonstrations that nature obeys an optimization principle [00:07:04].

## Bernoulli's Optical Solution to the Brachistochrone

Johann Bernoulli, aware of [[Principle of Least Action | Fermat's principle of least time]], realized he could use it to solve the problem of fastest descent [00:07:18]. He ingeniously converted the mechanics problem of a sliding particle into an optics problem [00:07:26].

He imagined a ray of light that would accelerate as it passed through layers of less and less dense media, analogous to a mass falling under gravity [00:07:35]. By making these layers infinitesimally thin, where [[Application of Calculus in Physics | Snell's Law]] applies at each interface, a continuous curve emerges [00:07:45].

The key was to model the light's speed in each layer to accurately represent a falling object [00:07:55]. By applying the conservation of energy for a falling particle, Bernoulli found that its velocity squared is proportional to the vertical distance fallen (y), meaning velocity is proportional to the square root of y [00:08:01]. This implies that for the optical analogy, the speed of light should be proportional to the distance from the top [00:08:34].

Applying [[Application of Calculus in Physics | Snell's Law]] at an interface with this velocity relationship (velocity ∝ √y), Bernoulli found that the ratio of the sine of the angle to the square root of y remained constant across all layers [00:08:49]. This ratio's constancy immediately identified the path as a cycloid [00:09:28]. This curve is also known as a brachistochrone curve, meaning "shortest time" [00:09:40].

The astonishing solution was that the fastest path from A to B is indeed an arc of a cycloid, not a circle [00:09:47]. A surprising property of the cycloid is that no matter where a mass is released on it, it always reaches the end at the same time [00:09:58]. For this reason, it is also known as the tautochrone curve, meaning "same time" [00:10:05].

Bernoulli recognized the profound connection, noting, "In this way I have solved at one stroke two important problems, an optical and a mechanical one, and have achieved more than I demanded from others. I have shown that the two problems taken from entirely separate fields of mathematics have the same character" [00:10:14]. He unknowingly stumbled upon something much bigger [00:10:32].

## Maupertuis and the Principle of Least Action

About 40 years later, Pierre Louis de Maupertuis, one of Bernoulli's students, observed similarities in the behavior of light and particles [00:10:38]. This led him to question whether [[Principle of Least Action | Fermat's principle of least time]] was the most fundamental [00:10:50]. He hypothesized that a more foundational quantity was being minimized, one that governed both light and particles [00:10:54].

In the 1740s, Maupertuis proposed a new quantity he called the **action** [00:11:07]. He defined action as mass times velocity times distance [00:11:12]. His reasoning was that the farther something travels, the faster it goes, or the more massive it is, the greater the action [00:11:18]. For a journey with multiple segments, the total action is the sum of (mass × velocity × distance) for each segment [00:11:29].

Maupertuis claimed that out of all possible trajectories, the path a system will follow is the one that minimizes this action [00:12:06]. In 1744, he wrote, "This action is the true expense of Nature, which she manages to make as small as possible" [00:12:17].

### Reception and Criticism
Maupertuis's revolutionary idea was met with fierce attack and ridicule [00:12:31]. His friend Samuel Konig accused him of being wrong and plagiarizing Leibniz [00:12:35]. Voltaire, once a close friend, launched a scathing 32-page pamphlet mocking Maupertuis, accusing him of plagiarism, bad physics, and stupidity, potentially fueled by rumors of an affair between Maupertuis and Voltaire's lover [00:12:44].

Maupertuis received little mention in subsequent mathematical and physics education [00:13:08]. This criticism was somewhat justified because Maupertuis "kind of just picked" the principle "out of thin air" [00:13:37]. There was no obvious reason why nature should minimize "mass times velocity times distance," and the mathematical rigor was lacking [00:13:46].

## Euler's Defense and Refinements

Despite the widespread condemnation, Leonhard Euler vehemently defended the [[Principle of Least Action | principle of least action]] [00:14:01].

### Mathematical Advancements
Euler's first step was to replace the sum in Maupertuis's definition of action with an integral, allowing for continuous changes in speed or direction [00:14:09]. He used this to find the path of a particle orbiting a central mass, like a planet around a star [00:14:18]. This required finding the path with the smallest action among infinitely many possibilities [00:14:25].

Such a problem was arduous because the mathematical tools to handle it did not yet exist [00:14:45]. Euler himself invented a new, albeit "clunky and time consuming," method to solve it [00:14:54].

### Key Conditions
Through this process, Euler realized that the [[Principle of Least Action | principle of least action]] is only valid if the total energy is conserved and is the same for all paths considered [00:15:02]. These were crucial conditions that Maupertuis had not recognized [00:15:12]. Euler improved the principle's mathematical rigor by identifying these conditions and providing a specific working example [00:15:16]. Euler was known as a generous and empathetic mathematician who helped others understand complex concepts [00:15:27].

## Lagrange's General Proof

A general proof for the [[Principle of Least Action | principle of least action]] still eluded Euler [00:15:48]. This was achieved by Joseph-Louis Lagrange, a shy, mostly self-taught 19-year-old [00:15:59]. In 1754, Lagrange shared his results with Euler, who expressed "the greatest joy" and noted that Lagrange had "extolled the theory to the highest summit of perfection" [00:16:10].

Both Euler and Lagrange were strong proponents of the [[Principle of Least Action | principle of least action]] [00:16:22]. Approximately five years later, shortly after Maupertuis's death, Lagrange succeeded in providing a general proof for the principle [00:16:30].

## Understanding the Principle of Least Action: The Modern Form

The intuition behind "action" itself remains elusive to many [00:16:40]. However, the general approach developed by Euler and Lagrange provides a powerful method.

### The General Approach: Calculus of Variations
To find the path with the least action among infinite possibilities, Euler and Lagrange realized it could be done similarly to finding the minimum of a function in calculus: by taking the derivative and setting it to zero [00:17:25]. At a minimum, if you take a tiny step to the left or right, the function's value essentially doesn't change [00:17:40].

Similarly, if a path represents the least action, any small variation (or "tiny bump") to that path should result in essentially no change in the action [00:17:51]. This means that the difference in action between the optimal path and a slightly varied "trial path" is zero to the first order [00:19:09].

### Hamilton's Principle and the Lagrangian
Lagrange's proof involved rewriting the principle into its modern form. Starting with Maupertuis's action (sum of mass × velocity × distance) and Euler's integral form (integral of mass × velocity integrated over distance) [00:19:36]:
*   Velocity (v) can be expressed as ds/dt, so ds = v dt [00:19:48].
*   Substituting this into the integral gives the integral of mv² over time, which is twice the kinetic energy (2T) integrated over time [00:19:55].
*   Since total energy (E) is conserved (E = T + V, where V is potential energy), T can be rewritten as E - V [00:20:03].
*   Substituting this, the action integral becomes `∫(T + E - V)dt` [00:20:14].
*   Applying the variation and knowing E is constant (δE = 0), the equation simplifies to `δ∫(T - V)dt = 0` when paths have the same travel time [00:21:18].

This derived integral `∫(T - V)dt` is another way to express the action [00:22:00]. William Rowan Hamilton was the first to write the principle in this form in 1834, leading it to be named [[Principle of Least Action | Hamilton's Principle]] [00:22:07]. The term `(T - V)` is known as the **Lagrangian** (L) [00:22:18].

[[Principle of Least Action | Hamilton's Principle]] is the modern way of writing the [[Principle of least action in classical and quantum mechanics | principle of least action]] and is found in most physics textbooks [00:22:33]. It describes how objects move over time, not just the path's shape [00:22:40]. Key differences from Maupertuis's principle:
*   Action is an integral over time, not space [00:22:51].
*   It requires both start and end points, as well as start and end times [00:22:58].
*   Maupertuis's principle requires constant energy across paths, while time can vary [00:23:03]. Hamilton's principle requires constant time across paths, while energies can differ [00:23:10].

## Equivalence to Newton's Second Law

To illustrate how [[Principle of Least Action | Hamilton's Principle]] works, consider a ball thrown straight up [00:23:25]. Infinitely many possible trajectories can connect the start and end points within a given time [00:23:41]. The only conditions are that all paths share the same start and end points and the same elapsed time [00:23:52].

Assuming the true path (y(t)) has the least action, small variations (η(t)) can be added to create a trial path (q(t) = y(t) + η(t)) [00:24:04]. The principle states that the difference in action between these paths is zero to first order [00:24:26].

By computing the action for each path, substituting kinetic and potential energy in terms of y and η, and applying integration by parts, the equation simplifies to `m(d²y/dt²) - (dV/dy) = 0` [00:24:36].

This "curious differential equation" [00:25:34] is highly significant:
*   `-dV/dy` (minus the derivative of the potential energy with respect to height) is the force (F) [00:25:43].
*   `d²y/dt²` (the second derivative of height with respect to time) is the acceleration (a) [00:25:47].

Rearranging the equation yields `F = ma` [00:25:52]. This means the path that satisfies the [[Principle of least action in classical and quantum mechanics | principle of least action]] is precisely the one that obeys [[Isaac Newtons approach to estimating Pi | Newton's Second Law]] [00:25:54].

## Unification and Significance

The [[Principle of Least Action | principle of least action]] is equivalent to [[Isaac Newtons approach to estimating Pi | Newton's Second Law]] for mechanics but extends beyond it [00:26:04]. [[Principle of Least Action | Fermat's principle of least time]] (for light) is simply a special case of the [[Principle of least action in classical and quantum mechanics | principle of least action]] [00:26:14].

This single principle unifies seemingly separate fields of physics, from light's reflection and refraction to pendulums, planetary orbits, and galactic motion [00:26:21]. All are governed by the rule that the variation of the action is zero [00:26:35]. Euler, upon learning of Lagrange's proof, expressed his satisfaction that Maupertuis's principle had been "applied to the highest degree of dignity" [00:26:48].

### Advantages of the Lagrangian Approach
While [[Isaac Newtons approach to estimating Pi | Newton's Second Law]] (`F=ma`) might seem simpler, the [[Principle of Least Action | principle of least action]] provides an extremely powerful and often simpler method for solving mechanics problems [00:27:18].

Using the Euler-Lagrange equation (`d/dt(∂L/∂v) - ∂L/∂q = 0`), where L is the Lagrangian (T - V), allows one to solve any mechanics problem by simply writing down the kinetic and potential energies and plugging them into the equation [00:27:44]. This "machine" can "crank out the principle of least action" and provide the correct equations of motion, even for complex systems [00:28:23].

This approach is particularly advantageous when dealing with:
*   **Multiple Dimensions**: The Euler-Lagrange equation can be solved for each coordinate [00:28:39].
*   **Complex Coordinate Systems**: It allows the use of [[Historical perspective and physics behind rotational dynamics | non-Cartesian coordinate systems]] (e.g., polar coordinates for rotational problems), which can simplify problem-solving compared to vector-based force methods [00:28:46].
*   **Intricate Systems**: For systems like a double pendulum, deriving `F=ma` equations is "very nasty" due to moving reference frames, but the Lagrangian approach simplifies it significantly [00:29:06].

### Principle of Stationary Action
It's important to note that the term "principle of least action" is somewhat misleading [00:29:35]. Just as setting a derivative to zero in calculus can yield a minimum, maximum, or saddle point, the action is not always a true minimum [00:29:52]. More accurately, it is the **Principle of Stationary Action**, meaning the laws of motion arise from demanding a stationary point of the action integral [00:29:58].

### Beyond Classical Mechanics
Action is more fundamental than just classical mechanics [00:30:19]. Around the turn of the 20th century, action emerged as a key component in solving the UV catastrophe, one of the biggest problems in atomic physics, foreshadowing its crucial role in [[Principle of least action in classical and quantum mechanics | quantum theory]] [00:30:23]. This connection highlights the "spooky" nature of action appearing at the genesis of quantum theory, rather than energy or force [00:30:34].