---
title: Comparative analysis of jumping in animals and robots
videoId: daaDuC1kbds
---

From: [[veritasium]] <br/> 

Jumping, whether performed by biological organisms or engineered robots, adheres to specific physical principles. For an action to be considered a jump, two criteria must be met: motion must be created by pushing off the ground, and no mass can be lost during the process <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This means quadcopters, which push off the air, do not jump <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>, nor do rockets that eject fuel <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Similarly, an arrow launched from a bow is not jumping unless the bow comes with the arrow <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## Animal Jumping

Many animals, including sand fleas, grasshoppers, and kangaroos, jump by launching their bodies into the air with a single stroke of their muscles <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. The height of an animal's jump is determined by the amount of energy delivered in that single stroke <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>, meaning maximizing muscle strength is key to jumping higher <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

The Galago, also known as the Bush baby, is considered the best jumper in the animal kingdom <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. This is because 30% of their entire muscle mass is dedicated to jumping <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>, allowing the squirrel-sized primate to leap over two meters from a standstill <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. The Galago achieves this not by having better muscles, but simply by having more of them dedicated to the task <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

Some biological organisms utilize latches, similar to engineered systems, to aid their jumps. For example, the sand flea uses a "torque reversal mechanism" with two muscles: a large power muscle and a trigger muscle, to store and then release energy for its jumps <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. While internal [[work_multiplication_in_robotics | work multiplication]] for a jump from a standstill hasn't been observed in organisms, some do use external methods:
*   **Spider Monkeys** have been seen pulling back a branch hand over hand, using multiple muscle strokes, to store energy in the branch's bend and then catapult themselves forward <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Slingshot Spiders** shoot out a silky string, which they pull back multiple times to slingshot themselves to another location <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

## Robot Jumping

Early jumping toys, like poppers, demonstrate the basic principle of elastic jumping: energy is stored in a deformed shape (acting as a spring) and then released in a single stroke to apply force to the ground and launch into the air <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. All elastic jumpers follow this same principle of storing energy in a spring and releasing it in one stroke <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### The Record-Breaking Jumper

A tiny robot weighing less than a tennis ball holds the world record for jumping, reaching 31 meters—higher than a 10-story building <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This significantly surpasses the previous record of 3.7 meters <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. The robot's takeoff is incredibly fast, accelerating from a standstill to over 100 kilometers per hour in just nine milliseconds <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>, resulting in an acceleration of over 300 g's <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

#### [[potential_applications_for_jumping_robots | Potential Applications]]

While seemingly a niche skill, engineered jumpers have significant [[potential_applications_for_jumping_robots | potential applications]], particularly for space exploration on worlds with thin or non-existent atmospheres <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. On the Moon, with one-sixth of Earth's gravity, this robot could leap 125 meters high and half a kilometer forward <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. Jumpers could navigate steep cliffs and deep craters that challenge rovers, hopping in and out to fetch samples <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. The high efficiency of jumping, especially if kinetic energy could be stored back in the spring upon landing, could lead to near-perfect energy retention <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

Teams are already building fleets of these robots, some capable of righting themselves after landing for immediate re-takeoff <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Others are steerable, featuring three adjustable legs that form a tripod, allowing the robot to launch in any direction <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

#### [[jumping_robot_engineering_and_design | Engineering and Design]]

The remarkable height achieved by this jumper is due to three special [[jumping_robot_engineering_and_design | design features]]:

1.  **Lightweight Construction**: The robot weighs just 30 grams <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>, achieved by using a tiny motor and battery, and a structure made of lightweight carbon fiber and rubber that doubles as the spring <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. Natural latex rubber is highly efficient, capable of storing 7,000 joules per kilogram <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
2.  **Optimized Spring Design**: The main structure consists of four pieces of carbon fiber bound by elastic bands, creating a spring <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. Early designs using only rubber bands had a force profile that peaked and then decreased during compression <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. Designs with only carbon fiber slats required significant initial force and then increased linearly <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. The ultimate design is a hybrid, yielding an almost flat force profile across the entire compression range <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. This allows it to store double the energy of a typical spring and is considered "the most efficient spring ever made" <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.
3.  **[[work_multiplication_in_robotics | Work Multiplication]]**: Unlike animals, which rely on a single muscle stroke, this engineered jumper can store energy from many "strokes" or revolutions of its motor <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. A small motor winds up a string, compressing the robot and gradually storing energy in the carbon fiber and rubber bands over about a minute and a half <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. A latch then releases the string, allowing the stored energy to be released all at once <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. This allows a small motor to deliver a large burst of energy, trading time for power <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. This principle of [[work_multiplication_in_robotics | work multiplication]] is the "real secret" to its height <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

#### Scaling and Limitations

While lighter is generally better for a jumper, adding weight to the top of the robot can paradoxically make it jump higher <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. This is because the part of the body that moves needs to weigh at least as much as the foot to ensure efficient energy transfer during the collision with the ground <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

The current jumper has nearly maximized the achievable height with its spring design <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. Even with an infinitely light motor and infinite winding time, the highest possible jump with this compression spring is only about 19% higher than what has been achieved <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

Another way to increase jump height is to scale the jumper up. Making it 10 times isometrically larger could lead to a 15-20% higher jump, partly by avoiding air drag <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. This works because scaling up by 10 times increases cross-sectional area by 100 (which increases drag force) but increases mass by 1,000 (meaning more inertia and less effect from drag) <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

## Comparative Analysis and Future of Robotics

For years, engineered jumping primarily mimicked biological jumping <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. However, the introduction of [[work_multiplication_in_robotics | work multiplication]] provides a significant advantage for robots <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. With this principle, the power of the motor is no longer the limiting factor; instead, the focus shifts to designing the most powerful spring possible <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.

The concept of [[work_multiplication_in_robotics | work multiplication]] could revolutionize robotics beyond just jumping <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>. By building up energy gradually over time from multiple turns of a motor, robots could store and release massive amounts of energy while remaining portable, allowing them to achieve new feats and set new world records <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>. This innovation required a deep understanding of [[physics_of_jumping_and_energy_storage | physics]] and mathematics <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.