---
title: Introduction to calculus series
videoId: WUvTyaaNkzM
---

From: [[3blue1brown]] <br/> 

This article introduces a video series titled "The Essence of Calculus," aiming to present the core of the subject in a binge-watchable format <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. The series consists of approximately ten videos, with new content published daily <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Series Philosophy

The primary goal of the series is to move beyond the memorization of rules and formulas, such as [[introduction_to_derivatives_and_calculus_concepts | derivative formulas]], the product rule, the chain rule, implicit differentiation, and [[fundamental_theorem_of_calculus | the relationship between integrals and derivatives]] <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Instead, it seeks to reveal the origins and meaning of these concepts, fostering a feeling that one could have invented calculus oneself <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. This is achieved through an [[visualization_in_calculus | all-around visual approach]] <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. The series encourages viewers to adopt the mindset of an early mathematician, pondering ideas and drawing diagrams to discover mathematical truths naturally <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Stumbling into Core Ideas: The Area of a Circle

The series begins by exploring how one might intuitively discover [[fundamental_concepts_of_calculus | core calculus ideas]] by deeply considering a specific geometry problem: the area of a circle <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. The common formula, pi times radius squared, is questioned to understand its origin <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

This contemplation can lead to insights into three major [[fundamental_concepts_of_calculus | calculus ideas]]: [[fundamental_concepts_of_calculus#Integrals | integrals]], [[introduction_to_derivatives_and_calculus_concepts#Derivatives | derivatives]], and their inverse relationship <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

### Slicing the Circle

To find the area of a circle (e.g., with radius 3), one might try slicing it into many concentric rings <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This approach respects the circle's symmetry, which often simplifies mathematical problems <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

Each ring, with inner radius `r` and a tiny thickness `dr`, can be approximated as a rectangle when straightened out <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. The width of this rectangle is the ring's circumference, `2 * pi * r` <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>, and its height is `dr` <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. Thus, the approximate area of one ring is `2 * pi * r * dr` <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. This approximation improves as `dr` becomes smaller <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

### Connecting to Area Under a Graph

The sum of these approximate rectangular areas for all rings (from radius 0 to the circle's full radius R) can be visualized as the aggregate area of many thin rectangles placed side-by-side <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. The height of each rectangle corresponds to `2 * pi * r` (the circumference), and its width is `dr` <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

When plotting the function `y = 2 * pi * r`, these rectangles fit snugly beneath its graph <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. As `dr` becomes infinitesimally small, the sum of these rectangle areas approaches the exact area under the graph <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. In this case, the area under the graph of `2 * pi * r` from `r = 0` to `R` forms a triangle <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. The area of this triangle (1/2 * base * height) calculates to `pi * R^2` <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>, which is the exact formula for the area of a circle <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

This demonstrates how [[approximating_solutions_using_calculus | approximating a problem]] with a sum of many small quantities can lead to finding the exact area under a graph <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. Many other problems in math and science, such as calculating distance traveled from velocity, can be reframed as finding the area under a graph <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

## The Concept of Integrals

This process of finding the area under a graph is central to [[fundamental_concepts_of_calculus | calculus]] <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. For a general function, like `y = x^2`, the area under the curve between two points (e.g., `x=0` and `x=3`) is more complex than a simple triangle <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. A function `a(x)` that gives the area under a graph between a fixed starting point and a variable `x` is called an [[fundamental_concepts_of_calculus#Integrals | integral]] <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

## Stumbling into Derivatives

When tackling a hard problem like finding an integral, a productive strategy is to play around with the idea and build familiarity <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. By slightly increasing `x` by a tiny nudge `dx`, the resulting change in area (`da`) can be approximated as a thin rectangle with height `x^2` and width `dx` <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. The smaller `dx` is, the better this approximation <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

This leads to the relationship `da / dx ≈ x^2` <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. This ratio, `da` divided by `dx`, is known as the [[introduction_to_derivatives_and_calculus_concepts#Derivatives | derivative]] of `a` <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>. More technically, the derivative is what this ratio approaches as `dx` gets smaller and smaller <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>. A derivative measures how sensitive a function is to small changes in its input <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>. The series promises to delve deeper into [[visual_intuition_in_calculus | visualizing derivatives]] in subsequent videos <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.

## The Fundamental Theorem of Calculus

[[introduction_to_derivatives_and_calculus_concepts | Derivatives]] are crucial for solving [[fundamental_concepts_of_calculus#Integrals | integral]] problems <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>. If one knows that a function's derivative should be `x^2`, it's possible to reverse-engineer what the original function must be <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.

This inverse relationship, where the derivative of a function representing the area under a graph returns the function defining the graph itself, is known as the [[fundamental_theorem_of_calculus | Fundamental Theorem of Calculus]] <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>. It shows that [[fundamental_concepts_of_calculus#Integrals | integrals]] and [[introduction_to_derivatives_and_calculus_concepts#Derivatives | derivatives]] are inverses of each other <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.

## Series Outlook

This initial video provides a high-level overview and a glimpse into the core ideas of [[fundamental_concepts_of_calculus | calculus]] <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>. Subsequent videos in the series will explore [[introduction_to_derivatives_and_calculus_concepts | derivatives]], [[fundamental_concepts_of_calculus#Integrals | integrals]], and more in detail <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>. The overarching aim remains for the viewer to feel capable of having invented calculus independently through visual and playful exploration <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>.

The creation of this series was supported by Patreon backers, who also provided suggestions during development and received early access to videos <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>. New videos are released without ads for their first month as a thank you to the community <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.