---
title: Jumping robot engineering and design
videoId: daaDuC1kbds
---

From: [[veritasium]] <br/> 

A new tiny robot, weighing less than a tennis ball <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, holds the world record for jumping, reaching heights of 31 meters <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a> – equivalent to a 10-story building <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a> or from the Statue of Liberty's feet to eye level <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. This significantly surpasses the previous record of 3.7 meters <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Defining a Jump

For something to qualify as a jump, it must meet two criteria <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>:
1.  Motion must be created by pushing off the ground <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a> (e.g., quad-copters pushing off air do not count <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>).
2.  No mass can be lost during the process <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a> (e.g., rockets ejecting fuel or arrows launched from a bow do not count <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>).

## Inspiration from the Animal Kingdom

Many animals, from sand fleas to kangaroos, execute jumps by launching their bodies into the air with a single muscle stroke <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. The height of the jump is determined by the energy delivered in that single stroke <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The Galago, or Bush Baby, is considered the best jumper in the animal kingdom, dedicating 30% of its muscle mass to jumping <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>, allowing it to leap over two meters from a standstill <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. This is due to having more jumping muscles, not necessarily better ones <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## How the Robot Jumps

The robot's main structure consists of four pieces of carbon fiber held together by elastic bands, forming a spring that stores energy <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. A small motor at the top of the robot winds a string connected to the bottom, compressing the structure and storing energy in the carbon fiber and rubber bands <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. After about 90 seconds of compression <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>, a trigger releases a latch, unspooling the string and releasing the stored energy <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. This propels the jumper from a standstill to over 100 kilometers per hour in just nine milliseconds <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>, experiencing an acceleration of over 300 g's <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

## Key Design Features

This robot's ability to jump nearly 10 times higher than the previous record holder <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a> is attributed to three special design features:

### Lightweight Construction
The jumper weighs only 30 grams <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>, achieved through a tiny motor and battery, and a structure made entirely of lightweight carbon fiber and rubber that doubles as the spring <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. Natural latex rubber can store 7,000 joules per kilogram, more energy per unit mass than almost any other elastic material <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

### Optimized Spring Design
The spring's design is crucial for its performance <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
*   Early designs using only rubber bands with hinged aluminum rods showed a force profile that peaked and then decreased upon compression <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   Another design with only carbon fiber slats required significant initial force, which then increased linearly with compression <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
*   The ultimate design is a hybrid of these two, creating a force profile that is almost flat over the entire range of compression <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. This allows it to store double the energy of a typical spring where force is proportional to displacement <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>, making it potentially the most efficient spring ever made <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.

### Work Multiplication
The robot's primary advantage comes from [[work_multiplication_in_robotics | work multiplication]] <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. Unlike animals, which use a single muscle stroke, engineered jumpers can store energy from many strokes (or motor revolutions) <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. This allows the motor to be small, as it doesn't need to deliver all energy at once but builds it up gradually over several minutes <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. This process is enabled by a latch that prevents the spring from unspooling until full compression is reached <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

While some biological organisms, like the sand flea <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a> and the slingshot spider <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>, utilize latches or external elements to store energy over multiple "strokes," no organism has developed internal [[work_multiplication_in_robotics | work multiplication]] for a jump from a standstill <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. [[Comparative analysis of jumping in animals and robots | Historically]], engineered jumping aimed to mimic biology <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>, but [[work_multiplication_in_robotics | work multiplication]] provides a unique advantage by shifting the limiting factor from motor power to spring power <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

## Potential Applications and Future Developments

This jumping robot concept holds significant [[potential_applications_for_jumping_robots | potential applications for jumping robots]], particularly for exploring other worlds where the atmosphere is thin or non-existent <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   On the Moon, with one-sixth of Earth's gravity, this robot could leap 125 meters high and half a kilometer forward <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   Jumpers could navigate challenging terrains like steep cliffs and deep craters, acting as sample-fetchers for rovers <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   With the ability to store kinetic energy back in the spring upon landing, the efficiency could be near perfect <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

The development team is already building a fleet of jumping robots with advanced capabilities <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>:
*   Some can right themselves after landing for immediate re-launch <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   Others are steerable, featuring three adjustable legs that allow directional launches <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

### Scaling and Air Resistance
The robot has nearly maximized the achievable height with its current spring design <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. To jump even higher, future designs could focus on incorporating air resistance and aerodynamics <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>. Scaling the jumper up ten times isometrically could lead to a 15-20% higher jump <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. This is because while the cross-sectional area (and thus drag force) increases by a hundred, the mass increases by a thousand, giving it significantly more inertia and reducing the effect of drag <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

The broader concept of [[work_multiplication_in_robotics | work multiplication]] could revolutionize robotics, allowing robots to store and release enormous amounts of energy over time, overcoming the portability limitations of small motors <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>. This innovation showcases the deep understanding of math and [[physics_of_jumping_and_energy_storage | physics of jumping and energy storage]] required for such advanced engineering <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.