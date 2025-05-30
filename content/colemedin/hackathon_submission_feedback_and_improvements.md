---
title: Hackathon Submission Feedback and Improvements
videoId: BN2ozB7LfvE
---

From: [[colemedin]] <br/> 

The organizers of the [[automator_ai_agent_hackathon_finale_and_winners | Automator AI Agent Hackathon Finale]] expressed serious appreciation for every single submission, noting that each AI agent made was impressive and that they were super happy with how the hackathon turned out and what participants created <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. Even if an agent didn't win, it still demonstrated incredible effort <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. The event required a lot of work, including working with guest judges, communicating with submitters, and configuring agents on the Live Agent Studio <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

The hosts intend to organize another [[participating_in_ai_agent_hackathons | hackathon]] in the future, though likely not monthly due to the significant effort involved <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

## Key Feedback from Judges and Organizers

### Handling Agentic Steps
Max, an employee of n8n and one of the judges, highlighted a crucial point for building robust agents:
> "My one feedback across the board for everyone guys is consider what happens when your agentic steps go wrong. They're probabilistic by nature, they can fail, and a good production use case is going to keep that into account." <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>

This feedback emphasizes the importance of designing agents that can gracefully handle errors and unexpected outcomes.

### Modeling Solutions on Human Steps
Max also provided general advice for building non-trivial AI solutions:
> "I can highly recommend to anyone when you're building a non-rival AI agent or a non-trivial solution, think of the human steps to complete that task and try and try to model your solution like that." <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>

This approach can lead to more intuitive and effective agent designs.

### Documentation
A significant area for [[improvements_in_project_organization_and_contribution_management | improvement]] identified was documentation <a class="yt-timestamp" data-t="00:34:15">[00:34:15]</a>. It is crucial for software engineers and AI agent builders to focus not only on functionality but also on presentation and documentation <a class="yt-timestamp" data-t="00:34:27">[00:34:27]</a>. Effective documentation helps communicate how to use an agent, its value, and its underlying build process <a class="yt-timestamp" data-t="00:34:39">[00:34:39]</a>.

*   **Example of Good Documentation:** The Stream Buzz agent was highlighted for its powerful functionality and very good documentation, which included explanations like "Why Stream Buzz" and a demo <a class="yt-timestamp" data-t="00:34:47">[00:34:47]</a>. The Indoor Farming agent also featured phenomenal documentation with images, overviews, and demos <a class="yt-timestamp" data-t="01:00:08">[01:00:08]</a>.

### Agent Design and Uniqueness
The host noted that every agent had different qualities that made them stand out, whether it was functionality, uniqueness, or documentation <a class="yt-timestamp" data-t="00:33:37">[00:33:37]</a>.

*   **Custom Front-End Components:** The Ask Reddit agent was the *only* submission that leveraged the option to create a custom React component to display AI responses in a more advanced way <a class="yt-timestamp" data-t="00:38:40">[00:38:40]</a>.
*   **Dynamic Tool Injection (MCP):** The mCP agent demonstrated a "phenomenal" ability to turn the Live Agent Studio into a platform compatible with Model Context Protocol (MCP), allowing dynamic injection of tools into an AI agent <a class="yt-timestamp" data-t="00:36:46">[00:36:46]</a>.
*   **Unique Learning Approaches:** The YouTube Educator Plus agent stood out by not just summarizing videos but generating fill-in-the-blank worksheets and quizzes, even providing PDF versions, offering a practical twist on a basic function <a class="yt-timestamp" data-t="00:52:03">[00:52:03]</a>.
*   **System Prompt Management:** The Smart Select Multi-Tool agent dynamically fetched system prompts from a GitHub repository based on the user's message, enabling the agent to behave differently for various tasks (e.g., writing an essay vs. a short story) <a class="yt-timestamp" data-t="00:53:35">[00:53:35]</a>.
*   **Persistent Knowledge Bases:** The n8n YouTube assistant was unique for its ability to permanently add YouTube videos to its knowledge base, allowing it to serve as a long-term assistant that builds on learned information over time <a class="yt-timestamp" data-t="01:01:41">[01:01:41]</a>.

### Addressing Weaknesses
*   **Conversation History:** The Tiny DM agent, while "super cool," had some issues processing conversation history correctly, meaning it didn't always acknowledge previous statements in follow-up questions <a class="yt-timestamp" data-t="01:17:12">[01:17:12]</a>.
*   **Configuration Challenges:** Some agents, like the one involving Stripe, faced difficulties in configuration on the Live Agent Studio, highlighting the challenges of working with new platforms and technologies in a competition setting <a class="yt-timestamp" data-t="01:05:51">[01:05:51]</a>.

## Learning and Community
The hackathon was deemed a valuable learning experience for all participants <a class="yt-timestamp" data-t="03:00:50">[03:00:50]</a>. The innovation demonstrated by the community was inspiring <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>.
Organizers aim to help participants understand what contributes to building better AI agents and production-ready code <a class="yt-timestamp" data-t="01:04:27">[01:04:27]</a>. The Live Agent Studio will continue to be a platform for [[community_contributions_to_software_development | open-source AI agent development]] beyond the hackathon <a class="yt-timestamp" data-t="01:02:55">[01:02:55]</a>. All submitted agents are open source, allowing others to inspect their workflows and learn from them <a class="yt-timestamp" data-t="01:08:57">[01:08:57]</a>.

The core advice given is to focus on **capabilities, not tools** <a class="yt-timestamp" data-t="01:25:45">[01:25:45]</a>. This means prioritizing learning higher-level concepts like architecture for agentic workflows, rather than getting too caught up in mastering a single tool or prompting for one LLM <a class="yt-timestamp" data-t="01:26:07">[01:26:07]</a>. This approach ensures that knowledge remains relevant even as tools evolve and are replaced <a class="yt-timestamp" data-t="01:26:51">[01:26:51]</a>.

### Future Development
The organizer is launching a new open-source project called Archon, an AI agent that can build other AI agents, powered by Pydantic AI and LangGraph <a class="yt-timestamp" data-t="01:19:09">[01:19:09]</a>. This project will serve as instructional material to teach powerful AI agent development iteratively, aiming to make complex topics more accessible, even for those new to Python <a class="yt-timestamp" data-t="01:28:18">[01:28:18]</a>. Future iterations plan to include self-feedback loops and tool libraries for prepackaged functionalities <a class="yt-timestamp" data-t="01:22:41">[01:22:41]</a>.

The project also aims to address the limitations of current AI coding assistants (like Cursor or Windswept) that often hallucinate when dealing with agent frameworks like Pydantic AI due to training cutoffs <a class="yt-timestamp" data-t="01:23:52">[01:23:52]</a>. Archon seeks to be a more robust solution that understands Pydantic AI at every step <a class="yt-timestamp" data-t="01:37:38">[01:37:38]</a>.

The importance of **human-in-the-loop** workflows was also stressed <a class="yt-timestamp" data-t="01:34:45">[01:34:45]</a>. This concept allows for interruptions in agentic execution to receive user feedback or approval, preventing AI hallucinations from causing negative real-world impacts (e.g., sending an incorrect email) <a class="yt-timestamp" data-t="01:35:02">[01:35:02]</a>.