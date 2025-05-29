---
title: Rational and irrational numbers in music
videoId: cyW5z-M2yzw
---

From: [[3blue1brown]] <br/> 

This article explores the relationship between musical harmony and the mathematical properties of rational and irrational numbers, culminating in a surprising connection to foundational results in measure theory.

## The Challenge of Musical Harmony

Imagine playing a musical note with a given frequency, for example, 220 Hz <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. If a second note is played whose frequency is R times the first note's frequency (where R is a number between 1 and 2), the two notes can sound either harmonious or cacophonous <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. For instance, a ratio R of 1.5 (or 3/2) results in a harmonious sound, while the square root of 2 creates a cacophonous one <a class="yt-timestamp" data-t="00:00:55">[00:01:05]</a>. The challenge is to determine whether a given ratio R will produce a pleasant or unpleasant sound purely by analyzing the number, without listening <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

### The Pythagorean Perspective on Harmony

Historically, figures like Pythagoras suggested that two notes sound good together when their frequency ratio is a rational number, and bad when it's irrational <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
Examples of harmonious rational ratios include:
*   A ratio of 3/2, which produces a musical fifth <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   A ratio of 4/3, which yields a musical fourth <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   A ratio of 8/5, resulting in a major sixth <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

This phenomenon is hypothesized to occur because when the ratio of frequencies is rational, there's a detectable pattern in the rapid succession of beats that the brain can pick up on, perceiving it as a rhythm rather than just a harmony <a class="yt-timestamp" data-t="00:01:42">[00:02:00]</a>.

### The Nuance of Rational Ratios

However, not all rational numbers produce pleasant sounds. Many, like 211/198 or 1093/826, sound "pretty bad" <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. This is because these rational numbers are "more complicated" than simpler ones, and our ears struggle to detect the underlying pattern in their beats <a class="yt-timestamp" data-t="00:02:17">[00:02:22]</a>.

One way to quantify the complexity of a rational number is by considering the size of its denominator when written in reduced form <a class="yt-timestamp" data-t="00:02:29">[00:02:33]</a>. Thus, the initial definition of harmony might be refined to include only fractions with "low denominators," perhaps less than 10 <a class="yt-timestamp" data-t="00:02:38">[00:02:43]</a>.

### The Role of Irrational Numbers in Modern Music

Despite the emphasis on rational numbers, many notes sound harmonious even when their frequency ratio is irrational, provided it is close to a harmonious rational number <a class="yt-timestamp" data-t="00:02:47">[00:02:54]</a>. This is crucial for instruments like pianos, which are not tuned using strictly rational intervals <a class="yt-timestamp" data-t="00:03:00">[00:03:04]</a>. Instead, each half-step increase in frequency corresponds to multiplying the original frequency by the 12th root of 2, which is an irrational number <a class="yt-timestamp" data-t="00:03:04">[00:03:15]</a>.

For example, a musical fifth, ideally a ratio of 3/2, is approximated on a piano by 2^(7/12) (the 12th root of 2 raised to the 7th power), which is irrational but very close to 3/2 <a class="yt-timestamp" data-t="00:03:25">[00:03:43]</a>. Similarly, a musical fourth corresponds to 2^(5/12), which is very close to 4/3 <a class="yt-timestamp" data-t="00:03:49">[00:03:53]</a>. The reason the chromatic scale has 12 notes is that powers of the 12th root of 2 tend to be within a 1% margin of error of simple rational numbers <a class="yt-timestamp" data-t="00:03:57">[00:04:06]</a>.

### A Refined Definition of Harmony

Based on these observations, a ratio R produces a harmonious pair of notes if it is sufficiently close to a rational number with a sufficiently small denominator <a class="yt-timestamp" data-t="00:04:14">[00:04:23]</a>. The degree of "closeness" depends on the listener's discernment, and the "smallness" of the denominator relates to the intricacy of patterns their ear can pick up <a class="yt-timestamp" data-t="00:04:23">[00:04:30]</a>. A person with an acute musical sense might find pleasure in more complicated fractions, such as 23/21 or 35/43, and numbers approximating them <a class="yt-timestamp" data-t="00:04:33">[00:04:43]</a>.

## Connecting Music to Measure Theory

Consider a hypothetical musical savant who finds pleasure in *all* pairs of notes with a rational ratio, even the "super complicated" ones that most would find cacophonous <a class="yt-timestamp" data-t="00:04:54">[00:05:01]</a>. A fascinating question arises: would such a savant find *all* ratios R between 1 and 2 harmonious, including irrational ones? It is known that for any real number, one can always find a rational number arbitrarily close to it <a class="yt-timestamp" data-t="00:05:13">[00:05:18]</a>.

This leads to a connection with a foundational result in measure theory, specifically regarding [[covering_rational_numbers_with_open_intervals | covering rational numbers with open intervals]] <a class="yt-timestamp" data-t="00:05:25">[00:05:35]</a>.

### The Challenge of Covering Rational Numbers

The second challenge involves covering all rational numbers between 0 and 1 with a collection of open intervals, such that the sum of the lengths of these intervals is strictly less than 1 <a class="yt-timestamp" data-t="00:05:52">[00:06:15]</a>. This seems impossible because rational numbers are dense in the real numbers, meaning any continuous stretch, no matter how small, contains infinitely many rationals <a class="yt-timestamp" data-t="00:06:31">[00:06:39]</a>.

However, this *can* be done, even using infinitely many intervals <a class="yt-timestamp" data-t="00:06:23">[00:06:26]</a>.

#### The Solution

1.  **Enumerate the Rational Numbers**: First, the rational numbers between 0 and 1 are organized into an infinitely long list (e.g., 1/2, 1/3, 2/3, 1/4, 3/4, etc., in reduced form) <a class="yt-timestamp" data-t="00:07:06">[00:07:31]</a>. This allows referring to a "first," "second," or "nth" rational number <a class="yt-timestamp" data-t="00:07:38">[00:07:42]</a>.
2.  **Assign Intervals**: An open interval is assigned to each rational number in the list <a class="yt-timestamp" data-t="00:07:47">[00:07:53]</a>. Each interval is only responsible for covering its designated rational <a class="yt-timestamp" data-t="00:08:04">[00:08:07]</a>.
3.  **Sum of Lengths**: The total sum of the lengths of these intervals can be arbitrarily small <a class="yt-timestamp" data-t="00:08:10">[00:09:04]</a>. This is achieved by choosing an infinite sum with positive terms that converges to a desired small positive value (e.g., epsilon), like the geometric series 1/2 + 1/4 + 1/8 + ... <a class="yt-timestamp" data-t="00:08:14">[00:08:34]</a>. The nth interval's length is set equal to the nth term in this converging sum <a class="yt-timestamp" data-t="00:08:34">[00:08:42]</a>. This means intervals get "really small, really fast" <a class="yt-timestamp" data-t="00:08:42">[00:08:46]</a>.

The counterintuitive nature of this result arises from the conflict between analytical thinking (rationals in a list) and geometric intuition (rationals as a dense set) <a class="yt-timestamp" data-t="00:09:11">[00:09:28]</a>.

### The Musical Connection Formalized

This mathematical result offers a way to formalize the vague idea that the only rational numbers close to an irrational number have large denominators <a class="yt-timestamp" data-t="00:11:13">[00:11:22]</a>. For example, if the total length of the covering intervals is set to a very small value like 0.01, then 99% of the real numbers between 1 and 2 would *not* be covered by these intervals <a class="yt-timestamp" data-t="00:11:35">[00:11:45]</a>.

The harmonious numbers, such as 2^(7/12) (close to 3/2), would likely be among the elite 1% covered, as 3/2 would have a relatively "fat" interval due to its early position in the enumerated list of rationals (being a simple fraction) <a class="yt-timestamp" data-t="00:11:52">[00:12:03]</a>. Conversely, cacophonous rationals (those with high denominators) and irrationals very close to them would be among the *uncovered* 99% <a class="yt-timestamp" data-t="00:12:10">[00:12:17]</a>.

For the musical savant who finds patterns in *all* rational numbers, harmonious numbers could be defined as precisely those 1% covered by the intervals, *if* her tolerance for error decreases exponentially for more complicated rationals <a class="yt-timestamp" data-t="00:12:22">[00:12:35]</a>. This seemingly paradoxical fact—that a collection of intervals can densely populate a range while covering only a tiny fraction of its values—corresponds to the idea that harmonious numbers are rare, even for a savant <a class="yt-timestamp" data-t="00:12:41">[00:12:50]</a>.

In conclusion, the connection between the unexpected mathematical result of covering rational numbers with an arbitrarily small total length of intervals and the perception of musical harmony highlights how deeply intertwined seemingly disparate fields of study can be <a class="yt-timestamp" data-t="00:12:55">[00:13:04]</a>.