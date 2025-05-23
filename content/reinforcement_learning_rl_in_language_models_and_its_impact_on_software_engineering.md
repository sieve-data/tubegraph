---
title: Reinforcement Learning (RL) in language models and its impact on software engineering
videoId: 64lXQP6cs5M
---

From: [[dwarkesh | The Dwarkesh Podcast]]

Reinforcement Learning (RL) in language models has seen significant advancements, particularly in the last year (referring to the period between early 2024 and early 2025 in the podcast's timeline). These developments have led to proof-of-concept algorithms capable of achieving expert human reliability and performance in specific domains, notably competitive programming and mathematics, given the right feedback mechanisms [[reinforcement_learning_from_human_feedback_rlhf | Reinforcement Learning from Human Feedback (RLHF)]] <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>, <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. While models can reach high levels of intellectual complexity, demonstrating long-running agentic performance remains an ongoing challenge [[ai_alignment_and_safety_concerns | AI alignment and safety concerns]] <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>, <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## Key Advancements in RL

The primary breakthrough has been the success of **RL from Verifiable Rewards (RLVR)**, also referred to as RL with a "clean reward signal" <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>, <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. This contrasts with earlier RL from Human Feedback (RLHF), which, while aligning outputs closer to human preferences, didn't necessarily improve performance on complex problem-solving tasks due to human biases (e.g., length bias) and imperfect judgment <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>, <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

RLVR relies on objective, verifiable signals of correctness, such as:
*   The correct answer to a math problem <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   Passing unit tests in code <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

Even these "clean" signals can be susceptible to "hacking" by models, which might hardcode values or find ways around tests if they can inspect the test mechanisms <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>, <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### Why Software Engineering Benefits Significantly

Software engineering has emerged as a prime domain for RLVR due to its inherent verifiability [[impact_of_ai_on_software_development_and_productivity | Impact of AI on software development and productivity]] <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. Questions like "Does the code compile?", "Does it run?", "Does it pass the tests?" provide clear, objective feedback <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. Platforms like LeetCode offer immediate validation of problem-solving success <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. This is unlike tasks involving subjective taste, such as writing a great essay, where defining a clean reward signal is much harder [[challenges_and_opportunities_in_deploying_ai_at_scale | Challenges and opportunities in deploying AI at scale]] <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. This verifiability is also why a Nobel Prize (often involving verifiable steps in research) is considered more likely for AI assistance in the near term than a Pulitzer Prize-winning novel <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.

## Current Capabilities and Limitations of RL-Powered Agents

### Software Engineering Agents
There is an expectation of seeing real software engineering agents performing substantial work by the end of 2025 (podcast timeline) <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. A prediction for early 2026 is that these agents will be capable of performing close to a day's worth of work for a junior engineer, or a couple of hours of competent, independent work <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. Already, for certain tasks like generating boilerplate website code, these models can save significant time <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

### Limitations
Previously, the "extra nines of reliability" was thought to be the main bottleneck <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. However, the current understanding points more towards limitations in:
*   **Context and Scope:** Lack of context, difficulty with complex, multi-file changes, and managing the overall scope of a task <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>, <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. Models excel at intellectually complex tasks within a focused, scoped problem but struggle with amorphous tasks or those requiring extensive discovery and iteration with an environment <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   **Time Horizon:** While intellectual complexity peaks can be reached, sustained, long-running agentic performance is less developed <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>, <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. An example is `ClaudePlaysPokemon`, where the model's struggles are attributed more to memory system limitations over extended play <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>, <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
*   **Feedback Loop Quality:** Performance is strong if a good feedback loop can be established for the desired task; otherwise, models struggle [[ai_alignment_and_safety_research | AI alignment and safety research]] <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

## The Role of Compute in RL

### Current Spending vs. Pre-training
Currently, spending on RL compute is significantly less than on pre-training base models (e.g., an order of $1 million for RL versus hundreds of millions for base models) <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>. While not yet in a compute-limited regime for RL, this is expected to change soon [[role_of_compute_in_ai_development | Role of compute in AI development]] <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>. The strategy is to ensure algorithmic correctness before committing to large-scale RL compute spends, akin to choosing when to launch a space mission with advancing technology <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>, <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>. RL is more iterative than pre-training; capabilities are progressively added, whereas a pre-training run can be ruined if issues arise midway <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>, <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. OpenAI's progression from o1 to o3 involved a 10x compute multiplier for RL, indicating a phased scaling approach [[ai_scalability_and_breakthroughs | AI scalability and breakthroughs]] <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. Most labs are now scaling up their RL compute <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.

### Potential for Adding New Knowledge
RL is not merely refining pre-existing capabilities or "carving away marble" <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. Evidence from DeepMind's research with Go and chess-playing agents shows that RL can imbue models with new knowledge, even achieving superhuman performance, provided the RL signal is sufficiently clean <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>. The amount of compute used in training is a proxy for new knowledge or capabilities added <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

## The Nature of Learning in RL

Both pre-training and RL involve gradient descent; the signal differs <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.
*   **Pre-training:** Involves predicting the next token, offering a very dense reward signal (feedback at every token) <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>.
*   **RL:** Rewards are typically sparser (e.g., did you win the game?) and gradients may not propagate through discrete actions, making it potentially less efficient but still capable of teaching new abilities [[ai_systems_and_planning_mechanisms | AI Systems and Planning Mechanisms]] <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>, <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.

### Feedback Loops and Learning Curves
Language models benefit from their pre-training, which provides a strong prior for tasks humans care about [[ai_alignment_and_existential_risks | AI alignment and existential risks]] <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>. Unlike traditional RL learning curves that often show a "dead zone" while basic mechanics are learned, LLMs show an initial spike in performance <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. Even a single example can be enough to elicit existing knowledge related to formatting or backtracking, allowing the model to gain initial rewards <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.

### Learning from Failure
Humans often learn significantly from failures, provided they receive feedback that helps them understand where they went wrong <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>, <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>. Current RL implementations in LLMs (based on open-source examples like DeepSeek's) do not appear to have a "conscious process" of analyzing the specifics of a failure to inform subsequent attempts, relying instead on pure gradient descent, which could be a limitation <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>, <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>.

## Future Predictions and Outlook

### Software Engineering Automation
The trajectory for software engineering agents involves increasing autonomy and capability [[the_future_of_programming_and_ai_tools_like_github_copilot | The Future of Programming and AI Tools like GitHub Copilot]].
*   **Near-term (by early 2026):** Agents performing a junior engineer's day of work or several hours of independent, competent work <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   **Async Workflows:** A shift towards dispatching work to software engineering agents asynchronously is expected. Instead of direct interaction in an IDE, users will assign tasks much like they would to a human team member <a class="yt-timestamp" data-t="01:34:32">[01:34:32]</a>, <a class="yt-timestamp" data-t="01:35:38">[01:35:38]</a>. The next six months (from early 2025) will explore this trend <a class="yt-timestamp" data-t="01:35:56">[01:35:56]</a>. This is exemplified by tools like Claude Code with GitHub integration for pull requests <a class="yt-timestamp" data-t="01:34:44">[01:34:44]</a>, and the evolution of coding startups like Cursor and Windsurf, which bet on increasing agenticness <a class="yt-timestamp" data-t="01:35:09">[01:35:09]</a>, <a class="yt-timestamp" data-t="01:35:22">[01:35:22]</a>.
*   **Bottlenecks:** Current limitations include tooling, permissions, sandboxing, and the need for agents to access necessary resources like GPUs securely <a class="yt-timestamp" data-t="01:36:04">[01:36:04]</a>. Humans also tend to give up on models quickly if they don't succeed immediately, unlike the patience afforded to human learners <a class="yt-timestamp" data-t="01:36:45">[01:36:45]</a>. Async workflows might mitigate this <a class="yt-timestamp" data-t="01:37:04">[01:37:04]</a>.

### General Computer Use
Progress in software engineering is expected to translate to broader computer use tasks.
*   **By early 2026:** Tasks like using Photoshop for specific effects or booking flights are predicted to be "totally solved" <a class="yt-timestamp" data-t="01:05:21">[01:05:21]</a>, <a class="yt-timestamp" data-t="01:05:34">[01:05:34]</a>.
*   **Taxes:** Models are expected to navigate interfaces like TurboTax by early 2026 [[ai_for_science_and_societal_challenges | AI for Science and Societal Challenges]] <a class="yt-timestamp" data-t="01:09:04">[01:09:04]</a>, but fully autonomous, highly trusted tax completion is not anticipated by then <a class="yt-timestamp" data-t="01:08:47">[01:08:47]</a>. However, reliable completion of tasks like expense reports is predicted by the end of 2026 <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.
*   **Underlying Principle:** There's no fundamental difference seen between computer use and software engineering if tasks can be represented in tokens and appropriate feedback loops are established. The main hurdle is that computer use can be harder to frame within these feedback loops <a class="yt-timestamp" data-t="01:02:51">[01:02:51]</a>, <a class="yt-timestamp" data-t="01:03:12">[01:03:12]</a>.

If robust computer use agents are not evident by early 2026, it would be surprising and might suggest an unforeseen difficulty specific to this domain, potentially lengthening timelines, though not necessarily indicating a "bust" scenario <a class="yt-timestamp" data-t="01:40:37">[01:40:37]</a>, <a class="yt-timestamp" data-t="01:40:43">[01:40:43]</a>.

## Broader Implications for Software Engineering and White-Collar Work

The advancements in RL-powered agents point towards a significant [[ais_economic_impact_and_the_future_of_whitecollar_work_automation | AI's economic impact and the future of white-collar work automation]], with software engineering being a leading indicator <a class="yt-timestamp" data-t="01:34:29">[01:34:29]</a>.
*   **Timeline:** A "drop-in white-collar worker" is considered very likely within the next two years (from early 2025) and almost overdetermined within five years <a class="yt-timestamp" data-t="01:57:24">[01:57:24]</a>.
*   **Algorithmic Sufficiency:** Even if current algorithmic progress were to stall, the existing suite of algorithms is deemed sufficient to automate white-collar work, provided enough of the right kinds of data (e.g., screen recordings of all white-collar work) can be collected and utilized for RL <a class="yt-timestamp" data-t="02:03:34">[02:03:34]</a>, <a class="yt-timestamp" data-t="02:10:30">[02:10:30]</a>, <a class="yt-timestamp" data-t="02:11:48">[02:11:48]</a>. The economic incentive to do so is considered trivially worthwhile compared to the total addressable market of salaries <a class="yt-timestamp" data-t="02:03:44">[02:03:44]</a>.

This necessitates proactive planning by individuals, companies, and nations regarding compute resources, economic policies (e.g., to prevent extreme capital lock-in), and retraining/upskilling [[impact_of_ai_on_economic_and_societal_structures | Impact of AI on economic and societal structures]] <a class="yt-timestamp" data-t="01:58:53">[01:58:53]</a>, <a class="yt-timestamp" data-t="01:59:39">[01:59:39]</a>. The development of benchmarks similar to SWE-bench for other white-collar tasks is suggested for governments to track automation progress [[ai_alignment_challenges_and_ethical_considerations | AI alignment challenges and ethical considerations]] <a class="yt-timestamp" data-t="02:07:08">[02:07:08]</a>.