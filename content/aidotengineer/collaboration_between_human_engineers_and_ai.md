---
title: Collaboration between human engineers and AI
videoId: VZzUhELgYk4
---

From: [[aidotengineer]] <br/> 

The rapid advancements in AI are ushering in a new era of collaboration between humans and artificial intelligence, particularly in the field of engineering. This shift is compared to the impact of microprocessors or the transition to Software as a Service (SaaS), where intelligence becomes "too cheap to meter," leading to increased expectations for AI's capabilities <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. At DataDog, this means evolving from a platform solely for human use to one where [[human_ai_collaboration_and_cocreation | AI agents]] leverage the platform on behalf of users <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

## AI Agents as Collaborators

DataDog is developing [[human_ai_collaboration_and_cocreation | AI agents]] designed to act as partners or "co-workers" for engineers, similar to how human teammates would operate <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a> <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. These agents are built to handle specific, vertical tasks rather than being generalized, making their performance measurable and verifiable at each step <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a> <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

### The AI On-Call Engineer

One such agent is the AI On-Call Engineer, which aims to reduce the need for human engineers to wake up for 2 AM alerts <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. This agent:
*   Proactively starts an investigation when an alert occurs <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   Situates itself by reading runbooks and gathering context <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   Performs common troubleshooting steps like looking through logs, metrics, and traces <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   Automatically runs investigations and provides summaries before a human even reaches their computer <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   Operates by forming hypotheses, testing them with tools, and validating or invalidating each one, much like a human Site Reliability Engineer (SRE) or DevOps engineer <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   Can suggest remediations, such as paging another team or scaling infrastructure <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
*   Integrates with existing DataDog workflows, allowing the agent to understand and map to remediation processes <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   Can even write postmortems after an incident is remediated, summarizing what occurred and the actions taken by both humans and the agent <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

### The AI Software Engineer

This agent acts as a proactive developer or DevOps/software engineering assistant <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. It observes and acts on errors, automatically analyzing them, identifying causes, and proposing solutions <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. This can include generating code fixes and creating tests to prevent future occurrences, significantly reducing manual work for human engineers <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a> <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.

## Fostering Human-AI Collaboration

A key aspect of building these agents is enabling effective [[human_ai_collaboration_and_cocreation | human-AI collaboration]]. This involves designing systems where humans can:
*   **Verify and Oversee**: Humans need to be able to verify what agents have done and oversee their actions to learn from them <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
*   **Build Trust**: Transparency in the agent's reasoning helps earn trust. Users can see how hypotheses were generated and what the agent found, allowing them to agree or disagree with decisions <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   **Ask Follow-Up Questions**: The agent can be treated like a "junior engineer" who has performed work, allowing human engineers to ask questions about the steps taken or reasoning <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **UI/UX Considerations**: The user experience (UX) is crucial for effective collaboration with agents and assistants. Old UX patterns are changing, and designs should prioritize agents working more like human teammates <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a> <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.

## Lessons Learned in Building AI Agents

Developing [[challenges_and_innovations_in_ai_engineering | AI agents]] for collaboration has provided several key learnings:

*   **Scoping Tasks for Evaluation**: It's easy to build demos, but much harder to properly scope and evaluate an agent's performance. Tasks should be clearly defined and measurable, focusing on vertical, task-specific agents rather than generalized ones <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a> <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
*   **Prioritizing Evaluation**: Deeply thinking about evaluation (offline, online, and living) from the start is critical. It's easy to create demos that *look* like they work, but rigorous evaluation is needed for improvement over time <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. Domain experts should serve as design partners and task verifiers, not as sole rule-setters <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   **Building the Right Team**: While some ML experts are needed, a team of optimistic generalists who can code fast and embrace ambiguity is vital. Team members should be excited to be [[human_ai_collaboration_and_cocreation | AI augmented]] themselves, as the field is rapidly changing <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a> <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
*   **Observability for AI**: For complex agent workflows, robust observability is essential for debugging and situational awareness. This includes specialized "LLM observability" to track interactions and calls to models, regardless of how they are hosted or accessed <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a> <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. Visual tools like an "agent graph" can help understand multi-step calls and identify issues in complex decision-making processes <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.
*   **Leveraging General Methods**: The "bitter lesson" of AI engineering suggests that general methods leveraging new, off-the-shelf models are often the most effective. It's crucial to remain agile and not be stuck to a specific model, as new advancements can quickly solve reasoning challenges <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a> <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.

## The [[the_future_of_ai_engineering | Future of Human-AI Collaboration]]

It is anticipated that AI agents may surpass humans as users of platforms and products within the next five years <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. This means companies should not only build for human users or their own agents but also consider how third-party agents might directly interact with their platforms, providing them with necessary context and API information <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.

In the future, a team of DevSecOps agents may be available "for hire," handling on-call duties and platform integration directly <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>. This collaborative ecosystem will enable a significantly greater number of ideas to be brought to life, with automated developers like Cursor or Devin for creation and agents for operations and security <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.