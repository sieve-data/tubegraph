---
title: Introduction to trigonometric functions
videoId: yBw67Fb31Cs
---

From: [[3blue1brown]] <br/> 

The study of [[trigonometry_in_relation_to_angles_and_triangles | trigonometry]] fundamentally connects to [[complex_numbers_introduction | complex numbers]] <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. Understanding this [[connection_between_trigonometry_and_complex_numbers | connection between trigonometry and complex numbers]] can strengthen comprehension of both mathematical fields <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Exploring Trigonometric Functions Graphically

Even without formal definitions, the behavior of [[understanding_sine_and_cosine_using_unit_circles | trigonometric functions]] can be explored using a graphing calculator <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. For instance, graphing the cosine function reveals a sinusoidal wave, which is relevant to phenomena like waves and cycling dynamics <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. Manipulating the input (`x`) can compress or stretch the wave, affecting its frequency <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, while altering the output (`y`) can stretch the wave vertically <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### The Cosine Squared Identity

An interesting observation arises when squaring the cosine function, i.e., graphing `f(x) = cos(x)^2` <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
When `cos(x)` is squared, values of `1` (at `x=0` or `x=2pi`) remain `1`, and values of `-1` (at `x=pi`) also become `1` <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. This means the squared graph will always be positive, oscillating between `0` and `1` <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

Through graphical exploration, it can be determined that `cos(x)^2` looks like a sinusoidal wave that is entirely positive and oscillates between `0` and `1` within a span of `pi` <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

> What will the graph of f(X) = cosine of X squared look like? <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>
> **Answer: C** (a sinusoidal wave that is entirely positive, oscillating between 0 and 1 in the span of pi) <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>

It appears that squaring `cos(x)` (affecting the y-direction output) results in another cosine wave that oscillates more quickly <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. This leads to the identity:
`cos(x)^2 = (1 + cos(2x))/2` <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

This identity can be derived by observing that:
1.  `cos(x)` can be shifted up by `1` to make it entirely positive <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
2.  This shifted graph can be chopped in half (`/2`) to match the height of `cos(x)^2` <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
3.  The resulting function still cycles once every `2pi`, so it needs to be "squished" in the x-direction by multiplying the input by `2` (`cos(2x)`) to complete its cycle in `pi` <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

> Working from the assumption that the graph of cosine of x squared looks like a scaled-down version of the graph of cosine of x, which of the following equations is true? <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>
> **Answer: B** (`(1/2)cos(2x) + 1`) <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>

This behavior, where squaring a function is related to scaling its input, is also seen in exponential functions <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. For example, `(2^x)^2` is equivalent to `2^(2x)` <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. This similarity suggests that [[trigonometry_and_complex_numbers | cosine]] might be related to exponents, a connection that is explored further when introducing [[complex_numbers_introduction | complex numbers]] <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

## Defining Sine and Cosine

While often thought of in terms of [[trigonometry_in_relation_to_angles_and_triangles | triangles]], [[trigonometry_in_relation_to_angles_and_triangles | trigonometry]] is fundamentally about [[understanding_sine_and_cosine_using_unit_circles | circles]] <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.

### Unit Circle Definition

On a [[understanding_sine_and_cosine_using_unit_circles | unit circle]] (a circle with a radius of one) <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>:
*   The input to [[understanding_sine_and_cosine_using_unit_circles | sine and cosine]] functions is a measure of the distance walked around the circle, starting from the rightmost point (1,0) <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>. This distance is often thought of as an angle <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>.
*   **Sine (sin(theta))**: Represents the y-coordinate (height) of the point on the circle after walking `theta` distance <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. It starts at zero and oscillates <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.
*   **Cosine (cos(theta))**: Represents the x-coordinate of the point on the circle after walking `theta` distance <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>. It starts at one and oscillates <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.

For example, walking a distance of `pi` (approximately 3.14) gets you halfway around the circle, where the x-coordinate (cosine) is -1 <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.

> Without looking it up or using a calculator, which of the following is true (for an input of 3 radians)? <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>
> **Answer: B** (sine of 3 is around 0.14 and cosine of 3 is around -0.99) <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>
> *Explanation:* Walking 3 units around the unit circle is slightly less than `pi` (3.14), which is halfway around. At this point, the x-coordinate (cosine) is very close to -1, and the y-coordinate (sine) is a small positive value <a class="yt-timestamp" data-t="00:19:13">[00:19:13]</a>.

### Right Triangle Definition (SOH CAH TOA)

The traditional definition of [[trigonometry_in_relation_to_angles_and_triangles | trigonometric functions]] involves right triangles and the mnemonic "SOH CAH TOA" <a class="yt-timestamp" data-t="00:20:42">[00:20:42]</a>:
*   **SOH**: **S**ine = **O**pposite / **H**ypotenuse <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>
*   **CAH**: **C**osine = **A**djacent / **H**ypotenuse <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>
*   **TOA**: **T**angent = **O**pposite / **A**djacent <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>

The "angle" in this context is typically measured in degrees <a class="yt-timestamp" data-t="00:26:33">[00:26:33]</a>.

> Suppose that a tower is 100 meters high. After several years, the tower starts to lean. So instead of making a 90 degree angle with the ground, it makes an 80 degree angle. When the sun is directly overhead, what is the length of the shadow cast by this leaning tower? <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>
> **Answer: B** (100 times the cosine of 80 degrees) <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>
> *Explanation:* Drawing a right triangle with the tower as the hypotenuse (100m) and the shadow as the adjacent side to the 80-degree angle. Using CAH: `cos(80°) = Shadow / 100`, so `Shadow = 100 * cos(80°)`.

This triangle-based definition can be connected to the [[understanding_sine_and_cosine_using_unit_circles | unit circle]] by imagining triangles where the hypotenuse is scaled to `1` <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>. In such a [[understanding_sine_and_cosine_using_unit_circles | unit circle]] context, for an angle `theta`, the x-coordinate is `cos(theta)` and the y-coordinate is `sin(theta)` <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>.

### Radians vs. Degrees

Mathematicians prefer radians as a "natural unit" for angles <a class="yt-timestamp" data-t="00:27:17">[00:27:17]</a>. In a [[understanding_sine_and_cosine_using_unit_circles | unit circle]], a radian is the distance walked along the outside arc <a class="yt-timestamp" data-t="00:29:28">[00:29:28]</a>.
*   `180 degrees` is equivalent to `pi radians` <a class="yt-timestamp" data-t="00:29:46">[00:29:46]</a>.
*   `60 degrees` is `pi/3 radians` <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>.
*   `30 degrees` is `pi/6 radians` <a class="yt-timestamp" data-t="00:32:32">[00:32:32]</a>.

When working with [[introduction_to_calculus | calculus]] and [[understanding_sine_and_cosine_using_unit_circles | trigonometric functions]], it is almost always easier to think of the input in terms of radians <a class="yt-timestamp" data-t="00:30:33">[00:30:33]</a>.

## Computing Trigonometric Values

Calculating specific values for [[understanding_sine_and_cosine_using_unit_circles | sine and cosine]] by hand can be challenging <a class="yt-timestamp" data-t="00:30:52">[00:30:52]</a>. Values are often derived from geometric settings with sufficient symmetry, such as equilateral triangles <a class="yt-timestamp" data-t="00:31:29">[00:31:29]</a>.

An equilateral triangle with side lengths of 1 can be bisected to form two 30-60-90 right triangles <a class="yt-timestamp" data-t="00:31:54">[00:31:54]</a>.

> What is the sine of pi sixths? <a class="yt-timestamp" data-t="00:33:33">[00:33:33]</a>
> **Answer: One half** <a class="yt-timestamp" data-t="00:35:03">[00:35:03]</a>
> *Explanation:* For an angle of `pi/6` (30 degrees) in a right triangle derived from a unit-sided equilateral triangle, the opposite side is `1/2` and the hypotenuse is `1` <a class="yt-timestamp" data-t="00:35:46">[00:35:46]</a>.

> What is the cosine of pi divided by six? <a class="yt-timestamp" data-t="00:36:13">[00:36:13]</a>
> **Answer: Square root of three divided by two** <a class="yt-timestamp" data-t="00:37:23">[00:37:23]</a>
> *Explanation:* Using the Pythagorean theorem (`a^2 + b^2 = c^2`) for the same triangle, with hypotenuse `1` and one leg `1/2`: `adjacent^2 + (1/2)^2 = 1^2`, leading to `adjacent = sqrt(3/4) = sqrt(3)/2` <a class="yt-timestamp" data-t="00:38:01">[00:38:01]</a>.

### The Pythagorean Identity

The [[trigonometry_in_relation_to_angles_and_triangles | Pythagorean theorem]] directly translates into a fundamental [[trigonometry_in_relation_to_angles_and_triangles | trigonometric identity]]:
`cos(x)^2 + sin(x)^2 = 1^2` <a class="yt-timestamp" data-t="00:39:31">[00:39:31]</a>.
This identity shows that if one of [[understanding_sine_and_cosine_using_unit_circles | sine or cosine]] is known, the other can be found <a class="yt-timestamp" data-t="00:39:43">[00:39:43]</a>.

**Notation Alert**: In [[trigonometry_in_relation_to_angles_and_triangles | trigonometry]], `cos^2(x)` (or `sin^2(x)`) conventionally means `(cos(x))^2` (or `(sin(x))^2`), which is a specific exception to standard mathematical notation where `f^2(x)` typically implies applying a function to itself or a second [[derivatives_of_trigonometric_functions | derivative]] <a class="yt-timestamp" data-t="00:40:17">[00:40:17]</a>.

### Calculating More Complex Values

The identity `cos(x)^2 = (1 + cos(2x))/2` is useful for calculating values of angles that are half of known angles <a class="yt-timestamp" data-t="00:47:53">[00:47:53]</a>.

> What is the cosine of pi divided by 12? <a class="yt-timestamp" data-t="00:49:53">[00:49:53]</a>
> **Answer: sqrt((1 + sqrt(3)/2)/2)** <a class="yt-timestamp" data-t="00:52:15">[00:52:15]</a>
> *Explanation:* Substitute `x = pi/12` into the identity:
> `cos(pi/12)^2 = (1 + cos(2 * pi/12))/2` <a class="yt-timestamp" data-t="00:53:26">[00:53:26]</a>
> `cos(pi/12)^2 = (1 + cos(pi/6))/2` <a class="yt-timestamp" data-t="00:53:34">[00:53:34]</a>
> Since `cos(pi/6) = sqrt(3)/2` <a class="yt-timestamp" data-t="00:54:02">[00:54:02]</a>:
> `cos(pi/12)^2 = (1 + sqrt(3)/2)/2` <a class="yt-timestamp" data-t="00:54:13">[00:54:13]</a>
> `cos(pi/12) = sqrt((1 + sqrt(3)/2)/2)` <a class="yt-timestamp" data-t="00:54:23">[00:54:23]</a>
> This is also known as the [[connection_between_trigonometry_and_complex_numbers | half-angle identity]] <a class="yt-timestamp" data-t="01:12:18">[01:12:18]</a>.

## Geometric Interpretation of Tangent

While [[understanding_sine_and_cosine_using_unit_circles | sine and cosine]] are represented by coordinates on the [[understanding_sine_and_cosine_using_unit_circles | unit circle]], **Tangent (tan(theta))** can be geometrically interpreted as a length outside the circle <a class="yt-timestamp" data-t="00:57:37">[00:57:37]</a>.

Imagine a [[understanding_sine_and_cosine_using_unit_circles | unit circle]] with an angle `theta`. Draw a line perpendicular to the x-axis at `x=1` (this line is tangent to the circle). The length of the segment from `(1,0)` up to where this tangent line intersects the ray forming the angle `theta` is `tan(theta)` <a class="yt-timestamp" data-t="00:58:49">[00:58:49]</a>.

As `theta` approaches `pi/2` (90 degrees), the tangent length grows infinitely large, leading to vertical asymptotes in its graph <a class="yt-timestamp" data-t="01:03:08">[01:03:08]</a>.

> What does the tangent of theta looks like when we graph it? <a class="yt-timestamp" data-t="01:00:23">[01:00:23]</a>
> **Answer: A** (A graph starting at zero and blowing up to infinity as it approaches pi/2, repeating this pattern) <a class="yt-timestamp" data-t="01:02:55">[01:02:55]</a>

## Geometric Proof of the Pythagorean Identity

The Pythagorean identity, `cos^2(theta) + sin^2(theta) = 1`, can be visually demonstrated using the [[understanding_sine_and_cosine_using_unit_circles | unit circle]] and simple [[trigonometry_in_relation_to_angles_and_triangles | trigonometric]] definitions <a class="yt-timestamp" data-t="01:05:40">[01:05:40]</a>.

Consider a right triangle inscribed in a [[understanding_sine_and_cosine_using_unit_circles | unit circle]], with hypotenuse 1, horizontal leg `cos(theta)`, and vertical leg `sin(theta)` <a class="yt-timestamp" data-t="01:06:02">[01:06:02]</a>.
1.  Draw a perpendicular line from the vertex at `(cos(theta), sin(theta))` to the hypotenuse (which is the radius of the [[understanding_sine_and_cosine_using_unit_circles | unit circle]]) <a class="yt-timestamp" data-t="01:09:54">[01:09:54]</a>.
2.  This divides the original right triangle into two smaller similar right triangles.
3.  In the triangle on the left, the hypotenuse is `cos(theta)`. Applying the definition of cosine to `theta` within this smaller triangle, the adjacent side (which lies on the original hypotenuse of 1) is `cos(theta) * cos(theta) = cos^2(theta)` <a class="yt-timestamp" data-t="01:07:24">[01:07:24]</a>.
4.  In the triangle on the right, the hypotenuse is `sin(theta)`. The angle at the top is also `theta`. Applying the definition of sine to this `theta`, the opposite side (which also lies on the original hypotenuse of 1) is `sin(theta) * sin(theta) = sin^2(theta)` <a class="yt-timestamp" data-t="01:09:25">[01:09:25]</a>.
5.  Since these two segments (`cos^2(theta)` and `sin^2(theta)`) together make up the entire hypotenuse of the original triangle, which has a length of 1, it visually proves that `cos^2(theta) + sin^2(theta) = 1` <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>.