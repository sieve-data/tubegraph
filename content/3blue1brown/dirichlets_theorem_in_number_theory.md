---
title: Dirichlets theorem in number theory
videoId: EK32jo7i5LQ
---

From: [[3blue1brown]] <br/> 

The observation of patterns when plotting prime numbers in polar coordinates, where both the radius and angle are given by a prime number, led to insights connecting to [[distribution_of_prime_numbers | the distribution of prime numbers]] and rational approximations for [[relation_between_pi_and_prime_numbers | pi]] <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This unique data visualization, initially observed by a user named Dwymark on Math Stack Exchange and answered by Greg Martin, reveals complex patterns <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. While the initial setup might seem arbitrary, it ultimately points towards fundamental concepts in number theory, specifically Dirichlet's theorem <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>.

## Visualizing Number Patterns in Polar Coordinates

Points are plotted in 2D space using a distance from the origin (r) and an angle (theta) <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>. For these patterns, both r and theta are the same number <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>. Angles are measured in radians, where [[relation_between_pi_and_prime_numbers | pi]] radians is a half-turn and 2[[relation_between_pi_and_prime_numbers | pi]] radians is a full circle <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>. Each step forward in the sequence involves a turn of one radian and an increase of one unit in distance <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>. When all whole numbers are plotted this way, they form an Archimedean spiral <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>.

When only prime numbers are plotted, the initial result appears random due to the chaotic nature of primes <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. However, zooming out reveals distinct spiral patterns, some with missing arms <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>. Further zooming out transforms these spirals into outward-pointing rays, often appearing in clumps of four with occasional gaps <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>. These visual phenomena are not unique to primes, as plotting all whole numbers also produces similar spirals, albeit cleaner and more numerous <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>. This indicates that the origin of the spirals is separate from the filtering by primes <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>.

## The Role of Residue Classes

The emergence of these patterns can be explained by examining "residue classes" (also known as "remainder classes") <a class="yt-timestamp" data-t="06:02:00">[06:02:00]</a>.

### Modulo 6 Spirals
At a smaller scale, six distinct spirals are visible when plotting all integers <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>. Each arm consists of numbers that share the same remainder when divided by 6 (e.g., multiples of 6, numbers 1 above a multiple of 6, etc.) <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>. This is because 6 radians is slightly less than a full turn (2[[relation_between_pi_and_prime_numbers | pi]] radians), causing points in the same residue class to form a gentle spiral <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>.

When filtering for primes:
*   Primes (except 2 and 3) cannot be multiples of 6, or 2 or 4 above a multiple of 6 (as they would be even) <a class="yt-timestamp" data-t="05:34:00">[05:34:00]</a>.
*   Primes (except 3) cannot be 3 above a multiple of 6 (as they would be divisible by 3) <a class="yt-timestamp" data-t="05:46:00">[05:46:00]</a>.
*   Therefore, only two spiral arms remain visible: primes that are 1 or 5 above a multiple of 6 (with exceptions for 2 and 3) <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>.

### Modulo 44 Spirals
The larger pattern of 44 spirals is due to 44 radians being very close to 7 full turns (44 / (2[[relation_between_pi_and_prime_numbers | pi]]) ≈ 7.000095) <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>. This approximation is related to 22/7 as an approximation for [[relation_between_pi_and_prime_numbers | pi]] <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>. Each of these 44 spirals corresponds to a residue class modulo 44 <a class="yt-timestamp" data-t="08:19:00">[08:19:00]</a>.

When filtering for primes:
*   Primes cannot be in residue classes that share common factors with 44 (e.g., multiples of 44, or numbers 2, 4, 6, 8, etc., above multiples of 44, as they are even) <a class="yt-timestamp" data-t="08:33:00">[08:33:00]</a>.
*   Similarly, primes cannot be in residue classes that are multiples of 11 (e.g., 11, 22, 33 above multiples of 44, except for 11 itself) <a class="yt-timestamp" data-t="08:48:00">[08:48:00]</a>.
*   The remaining spirals correspond to residue classes that do not share any prime factors with 44 <a class="yt-timestamp" data-t="09:04:00">[09:04:00]</a>. Numbers that don't share prime factors are called "relatively prime" or "co-prime" <a class="yt-timestamp" data-t="09:35:00">[09:35:00]</a>.
*   There are 20 such numbers between 1 and 44 that are co-prime to 44. This is represented by Euler's totient function, phi(44) = 20 <a class="yt-timestamp" data-t="09:43:00">[09:43:00]</a>. These numbers are sometimes called "totitives" <a class="yt-timestamp" data-t="10:12:00">[10:12:00]</a>.
*   The initial observation suggests that primes appear to be randomly distributed within these remaining 20 arms <a class="yt-timestamp" data-t="09:14:00">[09:14:00]</a>.

### Modulo 710 Rays
At the largest scale, the observed rays are due to 710 radians being extremely close to a whole number of full turns (710 / (2[[relation_between_pi_and_prime_numbers | pi]]) ≈ 113.000095) <a class="yt-timestamp" data-t="11:06:00">[11:06:00]</a>. This relates to the highly accurate rational approximation of [[relation_between_pi_and_prime_numbers | pi]], 355/113 <a class="yt-timestamp" data-t="11:33:00">[11:33:00]</a>. When steps of 710 are taken, the angle changes microscopically, making the sequences appear as nearly straight lines <a class="yt-timestamp" data-t="12:02:00">[12:02:00]</a>.

Filtering by primes again removes many residue classes. The prime factors of 710 are 2, 5, and 71 <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>. Residue classes divisible by 2, 5, or 71 will contain few or no primes (except for the primes 2, 5, and 71 themselves). The remaining classes are those co-prime to 710 <a class="yt-timestamp" data-t="14:08:00">[14:08:00]</a>. The number of such classes is phi(710) = 280, explaining the count of 280 rays <a class="yt-timestamp" data-t="13:15:00">[13:15:00]</a>, <a class="yt-timestamp" data-t="03:15:00">[03:15:00]</a>. The visual "clumps of four" and "missing teeth" are explained by the removal of classes divisible by 2, 5, and 71 <a class="yt-timestamp" data-t="13:39:00">[13:39:00]</a>, <a class="yt-timestamp" data-t="13:48:00">[13:48:00]</a>.

## Dirichlet's Theorem on Arithmetic Progressions

The key observation from these visualizations is that the prime numbers appear to be quite evenly distributed among the remaining residue classes <a class="yt-timestamp" data-t="14:28:00">[14:28:00]</a>. This empirical finding is precisely what Dirichlet's theorem addresses <a class="yt-timestamp" data-t="14:38:00">[14:38:00]</a>.

### Statement of the Theorem
Consider the [[distribution_of_prime_numbers | distribution of prime numbers]] based on their last digit (residue modulo 10) <a class="yt-timestamp" data-t="14:51:00">[14:51:00]</a>. Beyond primes 2 and 5, primes must end in 1, 3, 7, or 9 <a class="yt-timestamp" data-t="15:04:00">[15:04:00]</a>. Dirichlet's theorem states that as one considers more and more primes, the proportion of primes ending in each of these digits approaches 25% <a class="yt-timestamp" data-t="15:52:00">[15:52:00]</a>.

More generally, Dirichlet's theorem on arithmetic progressions states:
> If you look at all prime numbers less than some large number x, and you consider what fraction of them have a residue of *r* modulo *n* (where *r* and *n* are [[multiplicative_functions_in_number_theory | co-prime]]), that fraction should approach `1 / phi(n)` as x approaches infinity <a class="yt-timestamp" data-t="17:52:00">[17:52:00]</a>.

Here, `phi(n)` is Euler's totient function, which counts the number of positive integers less than or equal to *n* that are [[multiplicative_functions_in_number_theory | co-prime]] to *n* <a class="yt-timestamp" data-t="09:56:00">[09:56:00]</a>. For example, for modulus 44, where `phi(44) = 20`, the proportion of primes in each allowed residue class approaches 1/20 <a class="yt-timestamp" data-t="17:08:00">[17:08:00]</a>.

### Significance and Proof
Dirichlet proved this theorem in 1837, establishing it as a foundational result in modern analytic number theory <a class="yt-timestamp" data-t="17:27:00">[17:27:00]</a>. The theorem provides a stronger statement than simply that there are infinitely many primes in certain arithmetic progressions (which is sometimes considered a more modest version of the theorem) <a class="yt-timestamp" data-t="18:47:00">[18:47:00]</a>. It shows that primes are "just as dense" in any one of these valid residue classes as in any other <a class="yt-timestamp" data-t="18:56:00">[18:56:00]</a>.

The proof of Dirichlet's theorem is complex and heavily relies on [[complex_numbers_in_discrete_math | complex analysis]] <a class="yt-timestamp" data-t="19:22:00">[19:22:00]</a>. This connection between prime numbers (discrete objects) and the continuous world of calculus and [[complex_numbers_in_discrete_math | complex numbers]] has been a common theme in number theory since the early 19th century <a class="yt-timestamp" data-t="19:40:00">[19:40:00]</a>.

### Modern Relevance
Understanding the [[distribution_of_prime_numbers | distribution of primes]] in residue classes continues to be a relevant area of modern research <a class="yt-timestamp" data-t="19:56:00">[19:56:00]</a>. Recent breakthroughs concerning small gaps between primes, moving closer to resolving the twin-prime conjecture, build upon these insights <a class="yt-timestamp" data-t="20:03:00">[20:03:00]</a>.

The journey from a seemingly whimsical data visualization to a deep result like Dirichlet's theorem highlights how even arbitrary explorations can lead to significant mathematical insights <a class="yt-timestamp" data-t="21:11:00">[21:11:00]</a>. It demonstrates that important mathematical facts often connect to many other topics, making "reinventing" concepts through playful exploration a valuable learning experience <a class="yt-timestamp" data-t="21:32:00">[21:32:00]</a>.