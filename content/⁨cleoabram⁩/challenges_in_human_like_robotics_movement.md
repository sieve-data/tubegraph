---
title: Challenges in Human Like Robotics Movement
videoId: nAgTgwak7ME
---

From: [[⁨cleoabram⁩]] <br/> 

While [[Development of Humanoid Robots by Companies | humanoid robots]] like [[Capabilities of Boston Dynamics Atlas Robot | Atlas]] from [[Development of Humanoid Robots by Companies | Boston Dynamics]] demonstrate incredible feats such as parkour and backflips, replicating the full spectrum of human movement presents significant challenges for engineers and developers <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## The Goal: Robots in a Human-Built World
Companies are developing [[Development of Humanoid Robots by Companies | humanoid robots]] to address limitations in automation, particularly by performing tasks that are unsafe, repetitive, or boring for humans <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. The primary reason for building human-shaped robots is that "we built our world for humans" <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. Legs are crucial for access, allowing robots to navigate stairs, climb ladders, enter woods, or even crumbling buildings, unlike wheeled robots <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. NASA's Valkyrie robot, for example, is intended for uncertain terrains like space <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

## Moravec's Paradox: The Easy Things Are Hard
A core principle in robotics, known as Moravec's Paradox, states that "the easy things are hard" <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. This means that actions humans take for granted, such as moving through the world and interacting with objects, are "extremely hard to get to work in robots" <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. For instance, while [[Capabilities of Boston Dynamics Atlas Robot | Atlas]] can perform a standing backflip <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>, it struggles with simpler tasks like sitting in a chair <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a> or jogging slowly <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. Humanoids currently find it a "real struggle" to perform "simple, low performance, interactive behaviors that we do all day long" <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.

## Specific Challenges in Movement

### Dynamic Stability and Recovery
[[Capabilities of Boston Dynamics Atlas Robot | Atlas]] demonstrates impressive stability. When shoved hard, it recovers its balance in a similar way to a human, sometimes even better, indicating robust recovery mechanisms <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. This ability to handle unexpected disturbances is crucial for robots operating in unpredictable environments <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. Tesla's Optimus robot also showed seamless correction when a block fell and adapted to blocks being moved around during a demo <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

### Complex Coordinated Actions
Actions like throwing an object while performing other movements are highly complex for robots. For example, for [[Capabilities of Boston Dynamics Atlas Robot | Atlas]] to grab a bag, accelerate it, jump, and turn 180 degrees so the bag lands in a specific spot, it has to "figure out all of those details on the fly" <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. This requires complex coordination and calculation of Newton's laws in real-time, especially considering how carrying an object changes the body's balance and angular momentum <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

### Lack of Automated Learning from Experience
Currently, [[Capabilities of Boston Dynamics Atlas Robot | Atlas]] does not automatically learn from new experiences or failures <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. For instance, if [[Capabilities of Boston Dynamics Atlas Robot | Atlas]] is shoved, a human engineer needs to modify its programming to help it accommodate such disturbances better <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. Any improvements derived from hardware experiments require human intervention <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.

## The Role of AI and Future Capabilities
While [[Capabilities of Boston Dynamics Atlas Robot | Atlas]] doesn't learn from individual physical interactions, it does leverage AI, specifically machine learning, in other ways <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. Its perception system relies almost entirely on machine learning to identify objects and localize itself using cameras <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. Additionally, machine learning is being used to generate behaviors, allowing systems to learn tasks through simulation, robot data, and trial-and-error, rather than relying solely on human engineers painstakingly writing control systems based on physics <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

Companies like Tesla are heavily investing in this approach. Their Optimus robot uses neural networks to process visual information and "decide" how to accomplish tasks given high-level goals, such as sorting blocks autonomously <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.

The future of [[Development of Humanoid Robots by Companies | humanoid robots]] in daily life depends on their ability to understand increasingly high-level concepts and commands <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>. There is a "massive difference" between giving precise instructions like "rotate your left hand, pick up the bag like this..." and a high-level command like "put my groceries away" <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>. For the latter, a robot would need to understand abstract concepts like "groceries" and "away," while also prioritizing safety (e.g., "Don't step on my dog!") <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.

The more one learns about [[Development of Humanoid Robots by Companies | humanoid robots]], the more evident it becomes how difficult their creation is, and how amazing both existing robots and human bodies are <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. The process of creating machines in our own image is an ambitious technological endeavor <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.