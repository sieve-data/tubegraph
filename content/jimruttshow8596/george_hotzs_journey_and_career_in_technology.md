---
title: George Hotzs journey and career in technology
videoId: 2WmczROXzco
---

From: [[jimruttshow8596]] <br/> 

George Hotz is a notable figure in the technology world, known for his precocious talent and contributions to various fields, including hacking, artificial intelligence, and self-driving cars <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Early Life and Hacking Career

As a teenager, George Hotz was selected for the Johns Hopkins Center for Talented Youth (CTY), a highly selective program <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. Notably, Lady Gaga also participated in this program, leading to a humorous observation that she could have been a mathematical physicist <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

At age 17, Hotz gained recognition in hacker circles as the first person to [[interoperability_in_the_tech_industry | break the carrier lock on the iPhone]] <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. His stance against Apple's closed systems, reminiscent of the open Apple II versus the closed Mac, fueled this early endeavor <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. A few years later, he encountered legal trouble with Sony for allegedly hacking the PlayStation 3 to break its copy protection, a case that was eventually settled out of court <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

## Transition to AI and Google Project Zero

Following his early hacking exploits, Hotz worked briefly for Facebook <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a> before being recruited into Google's Project Zero <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. This elite team of "white hat" hackers was tasked with probing widely distributed or critical infrastructure technologies to find "zero days" <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. A zero day is a previously unknown software exploit <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

Hotz's time at Project Zero led him to AI, as he began contemplating how to automate the search for vulnerabilities, a recurring theme in his life – automating his own work <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. He believes that much of the world's progress is driven by "lazy people" seeking non-sweat ways of doing things <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

## Comma.ai and Self-Driving Cars

Hotz founded Comma.ai, a company that develops an open-source self-driving car system <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

### Motivation and Initial Challenges
The idea for Comma.ai emerged after a contract with Elon Musk to build software for Tesla to replace the Mobileye chip (later acquired by Intel) did not materialize <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Hotz decided to build an autopilot clone and sell it to car companies <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. He found that building the software was easier than selling it to established car manufacturers <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

His first approach involved training a camera to predict the steering wheel angle using supervised learning (f(x) = y, where x is the image and y is the steering angle) <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. This method failed on the road, despite good test set performance <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. The reason was the temporal dependence of samples; the machine's actions affect subsequent input data, leading to accumulating "Epsilon errors" <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.

To address this, Hotz initially added a small amount of "corrective pressure" using an algorithm that detected lane lines and computed corrections based on the car's deviation from the lane center <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>. He refers to lane lines as the "original sin" of Comma.ai because they lack a physics-based definition, leading to human disagreement on labeling <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. Comma.ai eventually succeeded in removing reliance on lane lines <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>. Their current model asks: "given this road, where would a human drive the car?" <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>

Hotz dismisses the "zillion corner cases" argument often cited by AI experts like Gary Marcus as absurd, pointing out that humans also generalize well from less data than AI systems are trained on <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. He argues that issues like the Uber accident (where a pedestrian on a bicycle was struck) were more akin to classical software bugs (e.g., misclassification as "unknown" object) than fundamental failures of deep learning or corner cases <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. While acknowledging the importance of a "world model" for predicting complex scenarios, he notes this is still cutting-edge machine learning not yet fully deployed in self-driving cars <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.

### Data and Simulation
Comma.ai addresses the behavioral cloning problem by training in simulation, where the model's own policy generates data, allowing it to learn corrective pressure <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>. Their "hugging test" involves initializing a car in different lane positions in an Unreal Engine simulator to measure how quickly it returns to the center <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>.

Comma.ai boasts the second-largest driving dataset in the world after Tesla, with 10,000 weekly active users uploading data <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>. This provides a massively diverse dataset across the globe, unlike Waymo's geographically limited data <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>. Comma.ai's simulator, called the "small offset simulator," differs from Waymo's game engine approach by using reprojection of human video data with small geometric perturbations, allowing it to avoid the complexity of simulating other car behaviors <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.

### Comma.ai Product and Functionality
The Comma.ai system operates via a small box, the Comma 3X, which costs $1250 <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>. Installation typically takes 15-30 minutes and involves a Y-splitter plug connected to the car's existing camera behind the rearview mirror <a class="yt-timestamp" data-t="00:21:37">[00:21:37]</a>. The system is not "hacking" the car but rather intercepts and modifies messages from the camera to the car's steering and braking systems <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>. It selectively blocks or passes emergency braking signals, and changes lane keep assist messages to provide smooth lane centering <a class="yt-timestamp" data-t="00:22:17">[00:22:17]</a>. This functionality is achieved using only two cameras, emulating human eyes <a class="yt-timestamp" data-t="00:22:58">[00:22:58]</a>.

For popular cars like the Toyota Corolla or Rav4, the Comma.ai system enables continuous, relaxed highway driving for hours without human intervention <a class="yt-timestamp" data-t="00:24:45">[00:24:45]</a>. While primarily focused on highway driving, an experimental mode allows for city driving, including stopping at stop signs and lights, though it is "a little worse than Tesla FSD" <a class="yt-timestamp" data-t="00:25:07">[00:25:07]</a>.

### Comparisons with Waymo and Tesla
Hotz is critical of Waymo's approach, which relies on high-precision maps and costly, specialized hardware, leading to a "trackless monorail" system that is fragile and centralized <a class="yt-timestamp" data-t="00:26:50">[00:26:50]</a>. Waymo's reliance on constant remote human intervention (multiple operators per car) is also a point of concern, as evidenced by their cars stopping when cellular networks go down <a class="yt-timestamp" data-t="00:29:32">[00:29:32]</a>. Hotz believes Waymo's business model, assuming a static world and sole market dominance, is flawed <a class="yt-timestamp" data-t="00:32:28">[00:32:28]</a>. He argues that if Comma.ai can provide a solution using a $500 cellphone, Waymo's expensive robotic taxis ($500,000) will struggle to compete <a class="yt-timestamp" data-t="00:32:09">[00:32:09]</a>.

Comparing Comma.ai with Tesla, Hotz highlights that both have positive unit economics by selling products to consumers profitably <a class="yt-timestamp" data-t="00:33:40">[00:33:40]</a>. Hotz prefers building value slowly over time rather than relying on "hockey stick growth" <a class="yt-timestamp" data-t="00:33:51">[00:33:51]</a>.

Their autonomy approaches differ:
*   **Tesla**: Views driving as a "fiscus problem," employing a more rigid, modernist approach with virtual 3D displays and explicit localization of every car <a class="yt-timestamp" data-t="00:34:25">[00:34:25]</a>. They use a powerful, cost-based planner (MPC) that can sometimes lead to jarring or sketchy mistakes <a class="yt-timestamp" data-t="00:36:22">[00:36:22]</a>. Tesla uses significantly more CPU power (around 100x more) for both training and testing than Comma.ai <a class="yt-timestamp" data-t="00:35:25">[00:35:25]</a>.
*   **Comma.ai**: Employs a more holistic, human-emulating approach, focusing on "where a human drives the car" and "when a human hits the brakes" <a class="yt-timestamp" data-t="00:34:45">[00:34:45]</a>. Their system is designed for a "chill" driving experience, with lower torque limits and more human-like failure modes <a class="yt-timestamp" data-t="00:36:51">[00:36:51]</a>.

While Tesla has more high-end capabilities and can execute complex maneuvers like right turns at lights, Comma.ai believes it is ahead in practical day-to-day usability due to its smoother driving experience <a class="yt-timestamp" data-t="00:36:14">[00:36:14]</a>. Both companies perform all processing locally on the vehicle once the model is uploaded <a class="yt-timestamp" data-t="00:39:10">[00:39:10]</a>.

As of December 2023, Waymo had logged only 7 million miles in "no driver mode," while Tesla's engaged autopilot had accumulated an estimated 3.3 billion miles <a class="yt-timestamp" data-t="00:40:26">[00:40:26]</a>. Comma.ai has driven over 100 million miles, making them 10x larger than Waymo, with Tesla being 30x larger than Comma.ai <a class="yt-timestamp" data-t="00:40:42">[00:40:42]</a>.

### Legal and Regulatory Environment
Comma.ai self-certifies its compliance with automotive standards, similar to major suppliers like Bosch and Continental <a class="yt-timestamp" data-t="00:42:43">[00:42:43]</a>. Their system is [[interoperability_in_the_tech_industry | a Level 2 self-driving system]], meaning the human driver is always in control and fully liable for decisions <a class="yt-timestamp" data-t="00:43:14">[00:43:14]</a>. Comma.ai guarantees that the car will never become uncontrollable; the driver can always use the brakes or overpower the steering <a class="yt-timestamp" data-t="00:43:21">[00:43:21]</a>.

They explicitly state that users must keep their eyes on the road at all times <a class="yt-timestamp" data-t="00:43:59">[00:43:59]</a>. Comma.ai implements a "best in the world" driver monitoring system using an internal camera that is non-intrusive and designed to genuinely assist the driver by alerting them only when necessary, preventing "alert fatigue" <a class="yt-timestamp" data-t="00:44:42">[00:44:42]</a>. Telemetry data collection is opt-out, with Hotz believing it's a "common good" for system improvement <a class="yt-timestamp" data-t="00:45:37">[00:45:37]</a>.

For liability, Hotz maintains that if an accident occurs, the human driver is responsible, as they are always in control <a class="yt-timestamp" data-t="00:50:06">[00:50:06]</a>. However, Comma.ai would be liable for any mechanical failures caused by its product that prevent the car from functioning properly (e.g., brakes stopping working), a distinction known as "functional safety" <a class="yt-timestamp" data-t="00:53:21">[00:53:21]</a>. They have a strong legal stance against patent trolls, refusing to settle <a class="yt-timestamp" data-t="00:50:57">[00:50:57]</a>.

## Tinygrad: A Machine Learning Framework

George Hotz is also the CEO of Tinygrad, a machine learning framework designed to compete with industry giants like TensorFlow, PyTorch, and JAX <a class="yt-timestamp" data-t="00:55:55">[00:55:55]</a>.

Tinygrad's key differentiator is its extreme simplicity, with a codebase of only 5200 lines of code <a class="yt-timestamp" data-t="00:56:11">[00:56:11]</a>. Despite its small size, it is fully featured, capable of running complex models like Stable Diffusion and Llama, and training models like ResNet <a class="yt-timestamp" data-t="00:56:21">[00:56:21]</a>. It achieves this by supporting devices, data types (dtypes), and operations in a generic way, avoiding the "combinatorial explosion" of kernels seen in frameworks like PyTorch <a class="yt-timestamp" data-t="00:56:47">[00:56:47]</a>.

The long-term goal for Tinygrad is to build machine learning ASICs (Application-Specific Integrated Circuits), starting with software development to avoid pitfalls like those encountered by Tesla's Dojo project <a class="yt-timestamp" data-t="00:57:11">[00:57:11]</a>. Tinygrad is already used in Comma.ai's OpenPilot to run models on devices and is well-suited for embedded systems and microcontrollers <a class="yt-timestamp" data-t="00:57:29">[00:57:29]</a>.

## Vision for the Future

Hotz sees self-driving cars as a stepping stone to [[technological_evolution_and_its_impact | general purpose robotics]] and ultimately, artificial life <a class="yt-timestamp" data-t="00:40:01">[00:40:01]</a>. He views AI as existing on a spectrum, with driving being a "narrow AI" problem <a class="yt-timestamp" data-t="00:40:06">[00:40:06]</a>, easier than general robotics because it's simpler to gather good driving data from a car's perspective, and driving is a "low dimensional" problem (primarily steering and acceleration) compared to the complex movements of a human hand <a class="yt-timestamp" data-t="00:46:56">[00:46:56]</a>.

His ultimate dream for Comma.ai is to sell the "Comma Body," a $25,000 robot companion capable of cooking, cleaning, and other tasks <a class="yt-timestamp" data-t="00:47:34">[00:47:34]</a>. Hotz emphasizes a focus on solving fundamental problems in technology, not on short-term profits or extensive marketing, believing that value should be built slowly over time <a class="yt-timestamp" data-t="00:41:00">[00:41:00]</a>.