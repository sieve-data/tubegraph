---
title: Historical perspective and physics behind rotational dynamics
videoId: 1VPfZ_XzisU
---

From: [[veritasium]] <br/> 

The phenomenon known as the Dzhanibekov effect, also referred to as the tennis racket theorem or the intermediate axis theorem, describes the counterintuitive behavior of rotating objects <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Discovery and Initial Secrecy: The Dzhanibekov Effect

In 1985, Soviet cosmonaut Vladimir Dzhanibekov observed this effect while on a mission to rescue the Salyut 7 space station <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. After unpacking supplies, he noticed a wing-nut spinning off a bolt <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. The wing-nut maintained its orientation for a short time, then flipped 180 degrees, and continued to flip back and forth at regular intervals without any external forces or torques acting on it <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This strange and counterintuitive phenomenon was kept secret by the Russians for ten years <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. The mission itself was so dramatic that Russia made a movie about it in 2017 <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## Public Recognition: The Tennis Racket Theorem

Six years later, in 1991, a paper titled "The Twisting Tennis Racket" was published in the *Journal of Dynamics and Differential Equations* <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. This paper described how a tennis racket, when flipped in the air, not only rotates as intended but also performs a half-turn around an axis passing through its handle, resulting in the side originally facing the flipper facing away upon catching <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

Although the paper suggested this twisting phenomenon seemed new and was not mentioned in general classical mechanics texts <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>, it was actually present in the Landau and Lifshitz textbook cited by the authors <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. An understanding of the intermediate axis theorem dates back at least 150 years to Louis Poinsot's book "The New Theory of Rotating Bodies" <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. The effect is particularly striking in microgravity <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

## [[weight_and_torque_dynamics | Physics of Rotational Dynamics]]

Understanding this effect requires basic [[physics_of_flywheels | rotational dynamics]] concepts related to an object's moment of inertia.

### Principal Axes and Moment of Inertia

An object, like a tennis racket, has three principal axes around which it can spin <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>:

1.  **Smallest Moment of Inertia (Easiest to Spin)**: An axis running through the handle of the racket <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. Spinning around this axis is easiest, achieving the greatest angular velocity for a given torque <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. This is because the mass is distributed closest to this axis <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. Spins about this axis are stable <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

2.  **Greatest Moment of Inertia (Hardest to Spin)**: An axis running perpendicular to the head of the racket <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. Spinning about this axis is slowest because the mass is distributed farthest from it <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. This is the maximum moment of inertia axis <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. Spins about this axis are also stable <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

3.  **Intermediate Moment of Inertia (Unstable Spin)**: An axis running parallel to the head of the racket <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. When spinning about this axis, the intermediate axis, the half-twist phenomenon occurs <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This effect is not unique to tennis rackets but can be observed with cell phones or discs <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. The key requirement for the intermediate axis effect is an object possessing three different moments of inertia about its three principal axes <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. Objects with spherical symmetry or only two different moments of inertia (like a spinning ring) will not demonstrate this theorem <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. The objects that demonstrate this phenomenon are called "asymmetric tops" <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

### Intuitive Explanation by Terry Tao

Richard Feynman, a famous physicist, reportedly stated there was no intuitive way to understand the intermediate axis theorem <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. However, mathematician Terry Tao, a Fields Medal winner, provided an intuitive explanation in 2011 on Math Overflow <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

Imagine a thin, rigid, massless disc with heavy point masses on opposite edges of the x-axis and light point masses on opposite edges of the y-axis <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

*   Rotating around the x-axis (small masses moving) yields the smallest moment of inertia <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
*   Rotating about the z-axis (all four masses moving) yields the greatest moment of inertia <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   Rotating about the y-axis (intermediate moment of inertia) is where the effect occurs <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.

When the disc spins perfectly about the y-axis, centripetal forces keep the large masses in uniform circular motion <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. If we switch to a rotating frame of reference, centrifugal forces appear, pushing masses away from the rotation axis proportional to their distance <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>. In a perfect y-axis spin, only the big masses experience centrifugal force, balanced by centripetal forces <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

If the disc is bumped slightly off the y-axis <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>:
1.  The small masses now experience some centrifugal force due to their distance from the y-axis <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
2.  Tension forces within the disc ensure the small masses remain orthogonal to the big masses <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
3.  The large masses, due to their significant inertia, constrain the small masses to largely remain in the y-z plane <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
4.  The centrifugal forces on the small masses accelerate them, causing them to move further from the y-axis, increasing these forces <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
5.  This acceleration continues until the small masses flip to opposite sides <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
6.  For the first half of the flip, centrifugal forces accelerate the masses; in the second half, they slow them down, causing them to come to rest on the opposite side <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.
7.  This pattern repeats indefinitely, with the disc flipping back and forth at regular intervals <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

## Implications and Misconceptions: Could the Earth Flip?

The secrecy surrounding the Dzhanibekov effect might have stemmed from Dzhanibekov's subsequent experiment: he attached modeling clay to the wing-nut and observed the same periodic flipping <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. This led to speculation that if a spinning ball in space could flip, the Earth might too <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. Amidst the Mayan prophecies of the end of the world in 2012, conspiracy theorists and media outlets found this idea irresistible <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. The official Russian federal space agency, Roscosmos, even published an article in 2012, acknowledging the "astonishment and simultaneous danger to a certain part of the scientific world" caused by the Dzhanibekov effect and the hypothesis of the Earth's potential overturn <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

However, experiments by astronaut Don Pettit aboard the space station provide clues to the Earth's stability <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. A solid object (like a book or a cylinder) spins stably about its smallest or largest moment of inertia axes <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. But a liquid-filled cylinder spinning about its smallest moment of inertia axis is unstable and will eventually rotate about its largest moment of inertia axis <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.

This occurs because, while an isolated object's angular momentum remains constant, its kinetic energy can be converted into other forms, such as heat <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. Spinning about the axis with the smallest moment of inertia corresponds to the greatest kinetic energy <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. As this energy dissipates (e.g., through liquid sloshing), the object tends towards the state of minimum kinetic energy, which is spinning about the axis with the largest moment of inertia <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. This is the lowest energy state for a given angular momentum <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.

The U.S. learned this with Explorer One, their first satellite <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. Designed for spin stabilization about its long axis, it rotated end-over-end within hours <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. Its flexible antennas allowed energy dissipation, forcing it to rotate about the axis that maximized its moment of inertia <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>.

Like Explorer One, Earth has internal mechanisms for dissipating energy <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. Over time, it has come to spin about the axis with its maximum moment of inertia <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>. Most astronomical objects behave similarly; for example, Mars's Tharsis Rise, a major mass concentration, is located at its equator, maximizing its distance from the rotation axis and ensuring Mars rotates with its maximum moment of inertia <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>. Therefore, the Earth will not flip; it is stably spinning about its axis of maximum moment of inertia <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.

---
*This video was sponsored by LastPass, a password manager that offers unlimited password storage and free cross-device sync, allowing users to automate password entry and improve online security <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.*