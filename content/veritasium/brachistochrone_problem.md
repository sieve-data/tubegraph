---
title: Brachistochrone Problem
videoId: Q10_srZ-pbs
---

From: [[veritasium]] <br/> 

The **Brachistochrone Problem**, also known as the problem of fastest descent, asks what shape of ramp will allow a mass to slide from point A to point B in the shortest possible time <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>. Common sense might suggest the shortest path, a straight line, but this is not the fastest <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>. Bending the ramp down at the start allows the mass to accelerate to a higher speed earlier, which can reduce overall travel time even if the path is slightly longer <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. The challenge is to find the perfect balance between acceleration and path length to minimize travel time <a class="yt-timestamp" data-t="01:24:00">[01:24:00]</a>.

## Historical Attempts and Solutions

### Galileo's Hypothesis
According to Galileo, the arc of a circle was the fastest path <a class="yt-timestamp" data-t="01:32:00">[01:32:00]</a>. He demonstrated that this path was faster than any polygon <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>. However, it was later proven not to be the absolute fastest <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>.

### Bernoulli's Challenge
Nearly 60 years after Galileo, in June 1696, Johann Bernoulli issued this problem as a challenge to the world's leading mathematicians <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>. His motivation was largely to demonstrate his superiority over others, particularly Isaac Newton <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. He initially gave a six-month deadline, but no solutions were submitted <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. Gottfried Leibniz, a friend of Bernoulli's, persuaded him to extend the deadline to allow foreigners (like Newton) a chance <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a>.

### Newton's Contribution
On January 29, 1697, Newton received Bernoulli's challenge <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>. Despite his irritation at being "dunned and teased by foreigners about mathematical things," the problem's allure led him to solve it overnight, completing it by 4:00 a.m. <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>. Bernoulli himself took two weeks to find a solution <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>. Newton submitted his anonymous solution to the journal *Philosophical Transactions* <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>. Upon seeing it, Johann Bernoulli famously remarked, "I recognize the lion by his claw," acknowledging Newton's unique brilliance <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>. While Newton generally dominated Bernoulli, in this specific instance, Bernoulli's solution was considered more elegant <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>.

## Bernoulli's Clever Solution: Inspired by Light

Bernoulli's approach to the [[Brachistochrone Problem]] took inspiration from how light travels <a class="yt-timestamp" data-t="03:46:00">[03:46:00]</a>.

### Hero of Alexandria and Light Paths
In the 1st century AD, Hero of Alexandria contemplated how light travels <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>. He realized that in a single medium, like air, light always follows the shortest path <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>. This principle explains why, when light reflects, the angle of incidence equals the angle of reflection <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>. However, when light passes from one medium to another (e.g., air to water), it bends or refracts, and in this case, it does not follow the shortest path <a class="yt-timestamp" data-t="04:18:00">[04:18:00]</a>.

### Snell's Law and Fermat's Principle of Least Time
Over 1600 years, the relationship governing light refraction was discovered: [[Snell's Law]], stating that the sine of the angle of incidence divided by the sine of the angle of refraction is a constant *n*, dependent on the media <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>. The reason *why* it worked remained unknown until Pierre Fermat, a judge and mathematician, took interest in 1657 <a class="yt-timestamp" data-t="05:06:00">[05:06:00]</a>.

Fermat proposed that while Hero of Alexandria was on the right track, it's not distance but *time* that is being minimized by light <a class="yt-timestamp" data-t="05:34:00">[05:34:00]</a>. He mathematically demonstrated that Snell's Law emerges from the principle that light takes the path of shortest travel time <a class="yt-timestamp" data-t="06:18:00">[06:18:00]</a>. This constant *n* in Snell's Law is simply the ratio of the speed of light in the first medium to the speed of light in the second medium <a class="yt-timestamp" data-t="06:30:00">[06:30:00]</a>. This discovery, known as [[Fermat's Principle of Least Time]], was hailed by Fermat as "the most extraordinary, the most unforeseen, and the happiest calculation" of his life <a class="yt-timestamp" data-t="06:42:00">[06:42:00]</a>. It marked the first known instance of nature obeying an optimization principle <a class="yt-timestamp" data-t="07:04:00">[07:04:00]</a>.

### Solving the Brachistochrone with Optics
Bernoulli, aware of [[Fermat's Principle of Least Time]], realized he could convert the mechanical problem of a particle sliding down a chute into an optics problem <a class="yt-timestamp" data-t="07:19:00">[07:19:00]</a>. He imagined a ray of light accelerating as it passes through layers of increasingly less dense media, mimicking a mass accelerated by gravity <a class="yt-timestamp" data-t="07:35:00">[07:35:00]</a>. If these layers are made infinitesimally thin, a continuous curve emerges <a class="yt-timestamp" data-t="07:45:00">[07:45:00]</a>.

By applying the conservation of energy for the falling particle (where velocity squared is proportional to the vertical distance fallen, *y*, i.e., velocity goes as the square root of *y*) <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a>, he could relate the speed of light in his analogous optical system to the particle's velocity <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>. Plugging this into Snell's Law for each infinitesimally thin layer, he found that the ratio of the sine of the angle of incidence to the square root of *y* remained constant <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>.

This specific equation was immediately recognized by Bernoulli as the equation of a **cycloid** <a class="yt-timestamp" data-t="09:28:00">[09:28:00]</a>.

## The Cycloid: The Fastest Path

The **cycloid** is the path traced out by a point attached to the rim of a rolling wheel <a class="yt-timestamp" data-t="09:35:00">[09:35:00]</a>. It is also known as a **brachistochrone curve**, derived from the Greek words for "shortest time" <a class="yt-timestamp" data-t="09:40:00">[09:40:00]</a>. Therefore, the astonishing solution to the [[Brachistochrone Problem]] is that the fastest way to get from point A to point B is by following an arc of a cycloid, not a circle <a class="yt-timestamp" data-t="09:47:00">[09:47:00]</a>.

### The Tautochrone Property
The cycloid possesses another remarkable property: no matter where a mass is released along its curve, it always reaches the lowest point at the same time <a class="yt-timestamp" data-t="09:59:00">[09:59:00]</a>. For this reason, it is also known as the **tautochrone curve**, from the Greek for "same time" <a class="yt-timestamp" data-t="10:05:00">[10:05:00]</a>.

## Legacy and Impact
Bernoulli's solution, which unified an optical and a mechanical problem, hinted at a much larger underlying principle <a class="yt-timestamp" data-t="10:13:00">[10:13:00]</a>. This insight paved the way for the development of the [[principle of least action]], a single rule that underpins all of physics, from classical mechanics and electromagnetism to quantum theory and general relativity <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The [[Brachistochrone Problem]] thus played a pivotal role in revealing nature's optimization principles.