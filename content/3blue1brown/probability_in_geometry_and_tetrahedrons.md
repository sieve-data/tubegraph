---
title: Probability in geometry and tetrahedrons
videoId: OkmNXy7er84
---

From: [[3blue1brown]] <br/> 

The Putnam Mathematical Competition is a notoriously difficult six-hour test for undergraduate students, featuring 12 questions scored 1 to 10 each, with a maximum score of 120 <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Despite attracting students already interested in math, the median score is typically around 1 or 2 <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. The problems tend to increase in difficulty from 1 to 6 within each section <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. However, even the hardest problems, like questions five and six, often possess the most elegant solutions, requiring a subtle shift in perspective <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

This article explores one such problem, which appeared as the sixth question on a Putnam test <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>, focusing on the problem-solving process rather than just the solution <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## The Problem: Tetrahedron and Sphere Center

The problem asks:
> If you choose four random points on a [[geometry_of_spheres_and_cylinders | sphere]], and consider the tetrahedron with these points as its vertices, what is the probability that the center of the sphere is inside that tetrahedron? <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>

Approaching such a problem involves considering which tetrahedra contain the center and how to distinguish them systematically <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

## Simplifying to Two Dimensions

A common strategy for difficult problems is to consider simpler cases <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. In this instance, the problem can be reduced to two dimensions:
> What is the probability that a triangle formed by three random points on a [[geometry_and_circles | circle]] contains the center of the circle? <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>

### Fixed Points and Varying the Third

To simplify further, imagine fixing two points, P1 and P2, on the circle and letting only the third point, P3, vary <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. When P3 is in a specific arc on the opposite side of the circle from P1 and P2 (defined by lines drawn from P1 and P2 through the center), the triangle contains the center <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

Assuming all points on the circle are equally likely, the probability that P3 lands in this arc is the length of the arc divided by the circle's circumference <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. This proportion depends on the separation of P1 and P2 <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. For example, if P1 and P2 are 90 degrees apart, the relevant arc is one-quarter of the circle <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

If P1 and P2 are chosen randomly, the angle between the lines connecting them to the center (from 0 to 180 degrees) is equally likely <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. This means every proportion of the arc size between 0 and 0.5 is equally likely, leading to an average proportion of 0.25 <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. Thus, the overall probability that the triangle contains the center is 1/4 <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. This demonstrates [[using_geometry_for_understanding_probability | using geometry for understanding probability]].

### Challenges in Three Dimensions

Extending this approach to the three-dimensional case is difficult <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. If three points (P1, P2, P3) are fixed on a sphere, the fourth point (P4) must be in a specific "spherical triangle" on the opposite side of the center for the tetrahedron to contain the center <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. This spherical triangle is defined by planes passing through pairs of lines drawn from P1, P2, P3 through the sphere's center, which divide the sphere into eight sections <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Calculating the average size of this section as the initial three points vary is complex, possibly involving surface integrals <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>, but this is a Putnam problem, so a simpler path is likely available <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

## The Key Insight: Reframing the Random Process

The solution to such problems often lies in reframing the question <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. If adding a construct (like the lines through the origin) makes the problem conceptually easier, try to express the entire question in terms of that new construct <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

### Application to the 2D Case

Instead of choosing three random points on a circle, imagine choosing two random lines that pass through the circle's center <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. For each line, there are two possible endpoints on the circle. A coin flip can decide which endpoint becomes P1 and which becomes P2 <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. This process is equivalent to choosing random points on the circle <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

Now, imagine P3 is chosen *before* the two coin flips <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. Once the two lines and P3 are set, there are four equally likely outcomes for P1 and P2 based on the coin flips <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. Crucially, *one and only one* of these four outcomes places P1 and P2 on the opposite side of the circle as P3, resulting in a triangle containing the center <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. Therefore, the probability is always 1/4, regardless of the lines' positions or P3's location <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

### Generalizing to the 3D Case

This elegant argument generalizes seamlessly to three dimensions <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. Instead of picking four random points on a [[geometry_of_spheres_and_cylinders | sphere]], imagine choosing three random lines through the sphere's center, and then a random point for P4 <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

Each of the three lines has two endpoints on the sphere. Three coin flips decide which endpoint corresponds to P1, P2, and P3 <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. There are 2 x 2 x 2 = 8 equally likely outcomes for these coin flips <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. Just as in the 2D case, only one of these eight outcomes will place P1, P2, and P3 on the opposite side of the center as P4, ensuring the tetrahedron contains the center <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. Thus, the probability for the three-dimensional case is 1/8 <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

While this solution relies on visual intuition, it can be formalized using linear algebra <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. The core insight remains: the problem-solving strategy of simplifying and reframing is key <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

> [!tip] Problem-Solving Tactic
> Keep asking simpler versions of the question until a foothold is gained. If an added construct proves useful, reframe the entire question around that new construct. <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>

## Related Probability Puzzle

As a further exercise in [[using_geometry_for_understanding_probability | probability]], consider this problem:
> Suppose eight students are sitting in a circle taking the Putnam. Each student tries to cheat off of one of their neighbors, choosing randomly which neighbor to cheat from. What is the expected number of students who are not being cheated off of? <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>