---
title: George Hotzs career and expertise
videoId: 2WmczROXzco
---

From: [[jimruttshow8596]] <br/> 

George Hotz is an inventor and entrepreneur known for his early work in hacking and later for his contributions to artificial intelligence, particularly in the realm of self-driving cars and machine learning frameworks.

## Early Life and Hacking Endeavors
As a teenager, George Hotz was selected for the Johns Hopkins Center for Talented Youth, an "extremely selective program" [00:00:43]. At age 17, he gained notoriety in hacker circles as the first person to "break the carrier lock on the iPhone" [00:01:27]. A few years later, he was involved in a legal dispute with Sony for "hacking the PlayStation 3" [00:01:57], which allegedly involved breaking copy protection, a matter that was "settled out of court" [00:02:08].

## From Facebook to Google Project Zero
After a brief period at Facebook [00:02:13], Hotz was recruited into Google's Project Zero, described as one of the "most elite white hat hackers in the world" [00:02:33]. Their mission was to "probe broadly distributed Technologies or ones that were in critical pieces of infrastructure and find so-called zero days" [00:02:39]. Hotz explains that a "zero day is an exploit in a piece of software" that is "previously unknown" [00:02:58].

## Transition to Artificial Intelligence
Hotz's work at Project Zero sparked his interest in AI, leading him to consider "how do I write software that looks for vulnerabilities" [00:03:10]. This marked a recurring theme in his life: "how do I make stuff that can automate any work I'm doing" [00:03:17]. He attributes much of the world's progress to "lazy people" looking for "non sweat ways of doing things" [00:03:38].

## Comma.ai and Self-Driving Cars
Hotz founded Comma.ai, a company that develops an open-source self-driving car system [00:03:57].

### Motivation and Initial Challenges
His journey into self-driving technology began with a contract discussion with Elon Musk to "build software for Tesla that could replace the Mobileye chip" [00:04:47]. Although the contract did not materialize, Hotz decided to "build autopilot clone and sell to the car companies" [00:05:16].

Initially, Hotz attempted a straightforward supervised learning approach, training a camera to "predict the angle the steering wheel should be at" [00:10:50]. This method, despite appearing successful in testing, "doesn't drive at all" on the road [00:11:17]. The core issue is that the model's actions affect future inputs, meaning "your samples are not IID" (independent and identically distributed) [00:11:59]. This "Epsilon error" accumulates over time, leading to the car drifting out of its lane [00:11:18].

### Core Philosophy and Technical Approach
Hotz's approach to self-driving relies on cameras, emulating human vision [00:06:41]. He holds a contrarian view to those who believe lidar or other "penetrative sensing systems" are necessary [00:06:14]. He argues that the "only system that can drive cars" is "human beings" [00:06:21], who primarily use "two cameras" (eyes) [00:06:42]. He asserts that the idea that lidar is still a contrarian viewpoint is incorrect, stating, "it's correct now everyone accepts it" [00:06:52].

Regarding the six levels of self-driving automation, Hotz contends that they "say more about liability than capability" [00:07:22].
*   **Level Two**: The human is "still fully liable for decisions that the car makes" [00:07:28].
*   **Level Three**: The human is liable in "certain scenarios" [00:07:41].
*   **Level Four**: The human is "not liable in cities or certain areas" [00:07:43].
*   **Level Five**: The human is "never liable" [00:07:48].
He argues that claiming full automation where one can "sleep in the back seat" [00:08:12] was "total hubris" [00:10:31] from some in the industry.

Hotz also challenges the notion that self-driving is difficult due to "a zillion corner cases" [00:12:43], arguing that humans see "so much less data than the data we actually train our system on" [00:13:10]. He dismisses the concept of [[Ben Goertzels views on artificial general intelligence AGI | general intelligences]] as a "meaningless term" [00:13:21] when discussing AI. He believes the Uber accident, where a car struck a pedestrian, was "much more like a bug in classical software than any failing of AI" [00:14:13].

To address the "behavioral cloning" problem, where small errors accumulate, Comma.ai incorporated a "small amount of corrective pressure" [00:15:16]. This initially involved using "two lane lines" to compute a corrective pressure [00:15:22]. Hotz refers to this as the "original sin of comma" [00:15:38] because "there is no physics based definition of a lan line" [00:16:02], and they "did end up removing Lane lines" [00:16:06] after many years.

Their current model asks, "given this road where would a human drive the car" [00:17:04], using training data from human driving to inform the machine's actions [00:17:15]. They utilize a unique "small offset simulator" [00:19:48] that applies "small perturbations geometrically" to human video [00:19:56], allowing the model to learn corrective pressure. This contrasts with Waymo's approach of creating fully flexible game engine simulators [00:20:09].

### Data and Capabilities
Comma.ai possesses the "second largest driving data set in the world after Tesla," with "tens of millions of miles" from "10,000 weekly active users" globally [00:19:12]. This diversity is key, as Waymo's data, for instance, is concentrated in a few cities like "Scottdale Arizona" [00:19:32].

Comma.ai's system, accessible via a "comma 3X" device [00:21:08], is easy to install, taking about "15 minutes" [00:21:39]. It connects to the car's existing camera system, intercepting and modifying "lane keep assist messages" [00:22:30] to provide continuous lane centering, even on roads without markings [00:22:43]. The system does not disable critical safety features like "emergency breaking by default" [00:22:21].

The main benefit of Comma.ai's system is its ability to drive for "an hour without you having to do anything" on interstate highways [00:24:56]. An "experimental mode" allows for city driving, including stopping at lights and stop signs, though Hotz notes these "turn out to be a lot less useful in day-to-day usage" [00:25:33]. Unlike some competitors, Comma.ai "don't use maps" [00:25:56], relying instead on "normal standard definition map" like humans use [00:26:16], dismissing "high Precision Maps" as a "nonrobust system" [00:26:34].

### Business Model and Competition
Hotz emphasizes that Comma.ai operates with "positive unit economics" and is "selling boxes today and making a profit today" [00:33:43], similar to Tesla, which he sees as crucial for long-term viability over "hockey stick growth" [00:33:50]. He contrasts this with Waymo, which he states has "hilariously negative unit economics" [00:33:29] with its "$500,000 Robo taxi" [00:32:20]. He views Waymo's approach as building "trackless monorails" [00:28:48] that are "so fragile" [00:30:19] and "so centralized" [00:30:22], requiring constant remote human intervention and cellular network connectivity [00:30:07].

Comparing with Tesla, Hotz notes that Tesla's system uses about "100x" more CPU power and is "multiple years ahead" in "high-end capabilities" [00:36:01]. However, he believes Comma.ai is "ahead of Tesla in usability" [00:36:16], as Tesla's system can make "sketchy mistake[s]" or "fan break" [00:36:24], leading to a "jarring experience" [00:36:40]. Comma.ai, with its "Smooth driving is safe driving" [00:36:51] philosophy, prioritizes a less jarring, more "chill" experience [00:37:10]. Both companies train their models in data centers, but the processing for driving is done "local[ly] on the car" [00:39:19].

### Legal and Regulatory Stance
Comma.ai maintains a Level 2 system, meaning the human driver is "in control of the vehicle at all times" [00:43:17]. They guarantee the car "will never become uncontrollable" and that the human can always override the system [00:43:24]. Hotz explicitly states, "if the car crashes yeah I mean it's on you but pay attention at all times" [00:43:37].

Comma.ai has "the best driver monitoring in the world" [00:44:42], ensuring that users keep their "eyes on the road at all times" [00:44:01], and that alerts are not excessive, avoiding "alert fatigue" [00:45:00]. While Telemetry data collection is opt-out, Hotz encourages it as a "common good" to improve the system [00:45:47]. He asserts that in cases of software bugs leading to an incident, "the software didn't run over somebody the human driving the car ran over somebody" [00:50:06]. He applies a firm stance against patent trolls, stating, "we are not going to settle" [00:51:50].

### Future Vision for Comma.ai
Hotz sees self-driving cars as a "stepping stone" to "general purpose robotics" [00:47:28]. His "end dream of comma is to sell you the comma body the $25,000 robot companion that comes home and cooks for you cleans for you and you know does whatever else you might want" [00:47:34].

## Tinygrad: A Machine Learning Framework
Hotz is also the CEO of Tinygrad [00:55:55], a machine learning framework that "competes with tensorflow pie torch and Jacks" [00:56:01]. Its primary distinguishing feature is its simplicity, with a codebase of "5200 lines" [00:56:15]. Despite its small size, it is "fully featured" and "pretty fast" [00:56:27], capable of running "stable diffusion," "llama," and training "resnet" [00:56:23].

Tinygrad achieves this simplicity by supporting devices, data types, and operations in a "generic way" [00:56:48], preventing the "combinatorial explosion" seen in other frameworks [00:56:33]. The long-term goal of Tinygrad is to "build machine learning ASICs" by starting with software [00:57:12]. Tinygrad is currently used in Openpilot (Comma.ai's software) to run the model on devices and is well-suited for "embedded weird" systems like microcontrollers [00:57:36].

## Overall Philosophy
Hotz describes himself as "the quiet scientist guy who like I want to solve this problem very carefully I don't want problems from other people I don't want to oversell anything buy it or don't buy it that's up to you" [00:52:15]. He finds progress in AI "amazing," noting that "heavy lifting is being done by others" and that his work involves being "basically smart appliers of tools being built by other folks" [00:55:35].