---
title: Advancements in AI and future implications
videoId: VZzUhELgYk4
---

From: [[aidotengineer]] <br/> 

Diamond, who has been working in AI for about 15 years, discusses the [[ai_technological_advancements | advancements in AI]] and their implications, focusing on DataDog's development of AI agents <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. His career includes work at Microsoft Cortana, Amazon Alexa, Meta (PyTorch), and his own AI startup focused on a devops assistant <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## DataDog and AI Agents

DataDog, known as an observability and security platform for cloud applications, has been incorporating AI since around 2015 <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. While not always overtly branded as AI, features like proactive alerting, root cause analysis, impact analysis, and change tracking have utilized AI <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

The current landscape represents a clear "era shift" in AI, comparable to the advent of microprocessors or the move to Software-as-a-Service (SaaS) <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. This shift is characterized by bigger, smarter models, enhanced reasoning capabilities, multimodal AI, and a "Foundation model Wars" where intelligence becomes "too cheap to meter" <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. People now expect more and more from AI <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

DataDog is leveraging these [[advancements_in_ai_model_technology_and_performance | advancements in AI model technology and performance]] to move up the stack, aiming for customers to use DataDog not just as a devops platform, but as AI agents that utilize the platform on their behalf <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. This involves developing agents, conducting evaluations, and building new types of observability <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

### Current AI Agents in Private Beta

DataDog is developing several AI agents in private beta <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>:

*   **AI Software Engineer**: This agent analyzes problems and errors, recommends and generates code to improve systems <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. It can catch issues like recursion, propose fixes, create tests, and generate pull requests or open diffs in VS Code <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. This significantly reduces the time engineers spend manually writing and testing code <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
*   **AI On-Call Engineer**: Designed to automate tasks for on-call engineers, this agent activates upon an alert, gathers context from runbooks, and investigates issues by analyzing logs, metrics, and traces <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. It can automatically run investigations, provide summaries before a human even reaches their computer, and offer insights into alert causes or trace errors <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. This agent can also suggest remediations, such as paging other teams or scaling infrastructure <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. After an incident, it can write post-mortems by reviewing all actions taken by both the agent and humans <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

### Human-AI Collaboration

DataDog emphasizes human-AI collaboration, providing an interface where users can verify agent actions, learn from their processes, and build trust <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. Users can see the reasoning behind an agent's hypotheses, what it found, and ask follow-up questions <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. The agent operates by forming hypotheses, testing them with tools (like querying logs or metrics), and validating or invalidating them <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. Existing DataDog workflows can be integrated so agents understand and utilize them for remediation <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

## Lessons Learned in AI Engineering

Diamond shares key lessons from building these AI agents, relevant to [[the_future_of_ai_engineering | the future of AI engineering]] and [[challenges_and_innovations_in_ai_engineering | challenges and innovations in AI engineering]]:

*   **Scoping Tasks for Evaluation**: It's crucial to define "jobs to be done" clearly and understand tasks step-by-step from a human perspective <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. Building vertical, task-specific agents is preferred over generalized ones <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. Measurability and verifiability at each step are essential, as demos can be misleading without proper evaluation <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. Domain experts should act as design partners or task verifiers, not as code or rule writers, due to the stochastic nature of AI models <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   **Evaluation (Eval)**: Deeply thinking about evaluation is paramount <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. In the "fuzzy stochastic world" of AI, good evaluation is necessary, even starting small with offline, online, and living evaluations <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. End-to-end task measurements and appropriate instrumentation to gauge human usage and feedback are vital for a "living breathing test set" <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
*   **Building the Right Team**: While ML experts are valuable, the team should be seeded with one or two, augmented by optimistic generalists who are proficient at coding and willing to iterate quickly <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. UX and front-end development are surprisingly critical for effective human-agent collaboration <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. Teammates should be excited by the prospect of being AI-augmented themselves and eager to learn in a rapidly changing field <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
*   **Evolving UX**: Traditional UX patterns are changing, and being comfortable with this shift is important <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. The focus is on agents that behave more like human teammates rather than requiring new pages or buttons <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
*   **Importance of Observability**: For complex AI workflows, observability is crucial, not an afterthought <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>. Situational awareness is key to debugging problems <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. DataDog's "LM Observability" view helps monitor interactions and calls to models, whether hosted, running, or via APIs, in a unified view <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. Agent workflows can involve hundreds of complex, multi-step calls, making specialized "agent graph" views essential for human readability and debugging <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

### The "Bitter Lesson" of AI

A significant lesson is that general methods leveraging new off-the-shelf models are often the most effective <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>. While fine-tuning for specific tasks is common, new foundational models can quickly solve many reasoning problems, making it important for systems to easily switch between models and not be tied to one <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>.

## Future Implications

Looking ahead, the future of AI is rapidly accelerating, impacting [[future_prospects_in_ai_and_agentbased_technologies | future prospects in AI and agent-based technologies]] and [[applications_and_future_of_ai_technology | applications and future of AI technology]].

*   **AI Agents as Users**: There's a strong belief that AI agents will surpass humans as users of SaaS products like DataDog within the next five years <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>. This means product developers should consider providing context and API information optimized for agents, not just humans <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
*   **Agents For Hire**: DataDog anticipates offering "a team of DevSecOps agents for hire" in the near future, where agents will handle platform integration and on-call responsibilities directly for users <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.
*   **Empowering Small Companies**: Small companies will likely be built by individuals leveraging automated developers (like Cursor or Devon) to bring ideas to life <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. Agents like DataDog's will then handle operations and security, enabling an order of magnitude more ideas to reach the market <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.

These [[future_prospects_in_ai_and_agentbased_technologies | future prospects in AI and agent-based technologies]] highlight a transformative period where AI not only assists but also operates autonomously, changing how software is developed and maintained.