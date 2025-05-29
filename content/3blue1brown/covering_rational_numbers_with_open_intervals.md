---
title: Covering rational numbers with open intervals
videoId: cyW5z-M2yzw
---

From: [[3blue1brown]] <br/> 

The concept of covering rational numbers with [[measure_theory_and_open_intervals | open intervals]] is a foundational result in [[measure_theory_and_open_intervals | measure theory]], which underpins how mathematicians define integration and probability <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This counterintuitive problem involves "covering numbers with open sets" <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## The Challenge

The challenge is to cover all [[rational_and_irrational_numbers_in_music | rational numbers]] between 0 and 1 with [[measure_theory_and_open_intervals | open intervals]] <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. An [[measure_theory_and_open_intervals | open interval]] is defined as a continuous stretch of real numbers strictly greater than some number 'a' but strictly less than some other number 'b', where 'b' is greater than 'a' <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

The conditions for this challenge are:
*   Every [[rational_and_irrational_numbers_in_music | rational number]] must lie within at least one of the intervals <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   The sum of the lengths of all chosen intervals must be strictly less than 1 <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
*   Infinitely many intervals are allowed <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

This task seems impossible because [[rational_and_irrational_numbers_in_music | rational numbers]] are dense in the real numbers, meaning any continuous stretch, no matter how small, contains infinitely many [[rational_and_irrational_numbers_in_music | rational numbers]] <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.

## The Solution

The solution involves two key steps:
1.  **Enumerating Rational Numbers**: Organize all [[rational_and_irrational_numbers_in_music | rational numbers]] between 0 and 1 into an infinitely long list <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. One natural way is to list them by increasing denominator, ensuring each reduced fraction appears exactly once: 1/2, 1/3, 2/3, 1/4, 3/4, and so on <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. This allows referring to the first, second, or *n*th [[rational_and_irrational_numbers_in_music | rational number]] <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
2.  **Assigning Intervals**: Assign one specific [[measure_theory_and_open_intervals | open interval]] to each [[rational_and_irrational_numbers_in_music | rational number]] in the enumerated list <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

To ensure the sum of lengths is less than 1, we can use an infinite sum with positive terms that converges. For example, the sum 1/2 + 1/4 + 1/8 + ... converges to 1 <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. To make the total sum of lengths arbitrarily small (less than 1), choose any desired value of epsilon (ε) greater than 0 (e.g., 0.5 or 0.01) <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. Multiply all terms in the converging sum by epsilon, so the new sum converges to epsilon <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. Then, scale the *n*th interval to have a length equal to the *n*th term in this scaled sum <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

This means intervals assigned to [[rational_and_irrational_numbers_in_music | rational numbers]] later in the list (typically those with larger denominators) become very small, very fast <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. Despite their individual small size, each interval covers its designated [[rational_and_irrational_numbers_in_music | rational number]] <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. The total sum of the lengths of these intervals can be arbitrarily small, chosen by the value of epsilon <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

## Counter-Intuition and Visualization

This result often defies intuition <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. The proof approaches the problem analytically by listing the [[rational_and_irrational_numbers_in_music | rational numbers]], while intuition tends to think geometrically, seeing them as a dense set where skipping any continuous stretch seems impossible due to the infinite presence of [[rational_and_irrational_numbers_in_music | rationals]] <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

To visualize this, consider an irrational number like the square root of 2 divided by 2. If you zoom in on it, even though [[rational_and_irrational_numbers_in_music | rational numbers]] will always be found in your field of view, the intervals placed on top of those [[rational_and_irrational_numbers_in_music | rationals]] get extremely small, very quickly <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. This happens because intervals are smaller for [[rational_and_irrational_numbers_in_music | rationals]] that appear late in the enumerated list, which typically means those with larger denominators <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. This formalizes the idea that the only [[rational_and_irrational_numbers_in_music | rational numbers]] close to an irrational number have large denominators <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

## Connection to Musical Harmony

This concept can be surprisingly connected to musical harmony. The first challenge presented involves determining whether a ratio (R) of frequencies between two musical notes sounds harmonious or cacophonous <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. Early theories, like Pythagoras', suggested harmony arises when the ratio is a [[rational_and_irrational_numbers_in_music | rational number]] (e.g., 3/2 for a musical fifth, 4/3 for a musical fourth) <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. This is thought to be because [[rational_and_irrational_numbers_in_music | rational ratios]] create detectable patterns in beats that the brain perceives as rhythm <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

However, most [[rational_and_irrational_numbers_in_music | rational numbers]] sound bad (e.g., 211/198), as their complexity (measured by the size of the denominator in reduced form) makes the pattern too difficult for the ear to pick up <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. Furthermore, many notes sound harmonious even if their frequency ratio is irrational, as long as it's close to a harmonious [[rational_and_irrational_numbers_in_music | rational number]] <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. For instance, pianos are often tuned using the 12th root of 2 for half-steps, which is irrational <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. A musical fifth on a piano might be 2 to the 7/12, an irrational number very close to 3/2 <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

Thus, a harmonious ratio is defined as one sufficiently close to a [[rational_and_irrational_numbers_in_music | rational number]] with a sufficiently small denominator <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

When considering a "musical savant" who finds pleasure in all [[rational_and_irrational_numbers_in_music | rational ratios]], even the complicated ones, and tolerates error exponentially for more complex [[rational_and_irrational_numbers_in_music | rationals]] <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>, the problem of covering [[rational_and_irrational_numbers_in_music | rational numbers]] with small intervals provides insight. If we apply the interval covering setup to the range of musical ratios (e.g., 1 to 2) with a very small epsilon (e.g., 0.01), only a small percentage of numbers (the 1% covered by intervals) would be harmonious for the savant <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. The harmonious numbers would include simple [[rational_and_irrational_numbers_in_music | rationals]] and irrationals very close to them, while the cacophonous ones would be [[rational_and_irrational_numbers_in_music | rationals]] with high denominators and irrationals very close to those <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.

The paradoxical fact that a collection of intervals can densely populate a range while only covering a tiny percentage of its values corresponds to the idea that harmonious numbers are rare, even for a savant <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. This connection highlights the deep relationship between seemingly disparate mathematical and sensory concepts <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.