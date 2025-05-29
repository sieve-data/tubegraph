---
title: Eulers totient function and relative primality
videoId: EK32jo7i5LQ
---

From: [[3blue1brown]] <br/> 

This article explores the concepts of relative primality and Euler's totient function, as seen in the context of patterns formed by plotting prime numbers in polar coordinates.

## Context: Patterns in Polar Coordinates
The discussion originates from observing patterns when plotting points in 2D space using polar coordinates (r, θ), where both the radius `r` and angle `θ` are set to a given prime number [0:01:04]. While plotting all whole numbers forms an archimedean spiral [0:01:01], limiting the view to only prime numbers reveals distinct patterns, including spirals and rays [0:02:06]. These patterns are linked to rational approximations of pi, such as 22/7 for 2π ≈ 44/7, which results in spirals corresponding to "residue classes mod 44" [0:07:37].

## Relative Primality (Co-prime)
When examining the spirals formed by numbers plotted in polar coordinates, some residue classes contain very few or no prime numbers [0:10:39]. This occurs if the numbers in that class share common prime factors with the modulus (e.g., 44). For instance, residue classes mod 44 that are multiples of 2 or 11 will largely exclude primes [0:08:38].

The spirals that *do* contain prime numbers correspond to residue classes that don't share any prime factors with the modulus [0:09:04]. This concept is known as **relative primality** or **co-primality** [0:09:35]. Two numbers are considered relatively prime (or co-prime) if they do not share any common factors greater than 1 [0:09:35].

## Euler's Totient Function (Phi Function)
The number of integers between 1 and a given number `n` that are co-prime to `n` is precisely what [[eulers_formula_and_its_significance | Euler's totient function]] measures [0:10:00].
*   It is compactly written using the Greek letter phi (φ) [0:09:56].
*   For example, for the modulus 44, there are 20 different numbers between 1 and 44 that are co-prime to 44 [0:09:43]. This is expressed as φ(44) = 20 [0:09:53].
*   These numbers are sometimes obscurely referred to as "totatives of n" [0:10:15].

In the context of the polar plot, the `φ(n)` value indicates how many distinct spiral arms (residue classes mod `n`) are expected to contain prime numbers, as other arms will be filtered out due to common factors with `n` [0:10:48].

## Connection to Prime Distribution
The observation that primes appear to be evenly distributed among the remaining residue classes (those co-prime to the modulus) is a significant point [0:14:28]. For example, when looking at primes modulo 10, those greater than 5 must end in 1, 3, 7, or 9 [0:15:17]. As more primes are considered, the proportion of primes ending in each of these digits approaches 25% [0:15:52]. Similarly, for residue classes mod 44, the primes are evenly spread among the 20 allowable classes [0:17:08].

This empirical observation is formalized by [[distribution_of_prime_numbers_and_Dirichlets_theorem | Dirichlet's theorem on arithmetic progressions]] [0:14:42].
*   [[distribution_of_prime_numbers_and_Dirichlets_theorem | Dirichlet's theorem]] states that for any number `n` and any number `r` co-prime to `n` (i.e., `r` is a totative of `n`), the proportion of prime numbers less than some large number `x` that have a residue of `r` mod `n` approaches `1/φ(n)` as `x` approaches infinity [0:18:17].
*   This theorem guarantees that each residue class co-prime to `n` contains infinitely many primes, and that they are asymptotically equally dense within these classes [0:18:50].

## Significance
The study of prime distribution in residue classes, including the use of [[eulers_formula_and_its_significance | Euler's totient function]], is fundamental to modern analytic number theory [0:17:31]. The proofs often rely on complex analysis, illustrating a deep connection between the discrete world of prime numbers and continuous calculus [0:19:32]. This understanding remains relevant in contemporary research, such as breakthroughs related to small gaps between primes and the Twin Prime Conjecture [0:19:56]. The ability of arbitrary mathematical exploration, like plotting points in polar coordinates, to lead to profound concepts like [[eulers_formula_and_its_significance | Euler's totient function]] and [[distribution_of_prime_numbers_and_Dirichlets_theorem | Dirichlet's theorem]] underscores the interconnectedness of mathematical topics [0:21:04].