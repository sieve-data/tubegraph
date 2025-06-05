---
title: Design process improvements with AI
videoId: 8D_VdU6DBhI
---

From: [[aidotengineer]] <br/> 

## The Current State of AI in UX
Currently, AI faces a "trust gap" in user experience (UX) <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Research from December 2024 by Edelman indicates that only 32% of US adults trust AI, and merely 44% globally are comfortable with how businesses use AI <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This skepticism is often attributed to "AI slop," where generative AI fails to provide correct or useful information, such as absurd search results or unrealistic product prices <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

Despite these issues, the true "magic" of Generative AI (GenAI) lies in its ability to enable users to interact with machine learning models in natural language, marking a significant [[building_user_experiences_with_ai | UX revolution]] <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## The Opportunity: Invisible Interfaces and Accelerated Need Finding
Drawing from Don Norman's principle of "invisible interfaces"—software that feels so seamless and intuitive users forget they are using it—the opportunity for AI is to design interfaces that genuinely feel magical <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. This can be achieved not by haphazardly integrating chatbots, but by accelerating the "need finding" phase of design <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

## A New Approach to the Design Life Cycle with AI Simulation
The current [[product_development_process_in_ai | design process]], which predates GenAI, is data-driven, relying on qualitative observations, quantitative data, and ethnographic studies to guide [[prototyping_and_production_in_ai | prototyping and production]] <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

A new approach proposes empowering designers to work with "invisible users" through AI simulation <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. This process converts traditional data artifacts from need finding into "active participants" in the design process, providing designers with a mini feedback cycle to work with AI simulation <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. This concept is likened to how pilots use flight simulators for practice in complex environments <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

## Accelerated Need Finding Process with AI Simulation
The improved need finding process in the era of AI simulation shares similarities with existing methods but introduces key differences in components and workflow <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

The steps include:
1.  **Defining Audiences**: Start with rich data representing target audiences, such as demographic, psychographic, and contextual data, to simulate user behaviors <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. Huge, for example, utilizes its "Live" data platform for this <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
2.  **Applying Intent Mapping**: This transforms audience data into "intelligent twins"—simulations representing user behaviors, desired outcomes, needs, and motivations <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. These intelligent twins become active participants in the design simulation <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
3.  **Briefing Intelligent Twins**: Intelligent twins can be briefed to evaluate interfaces by focusing on specific tasks, similar to how a human designer might conduct a heuristic analysis <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. This allows for evaluation of specific interfaces or websites <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

### Example Project: Global Sports Website Audit
To demonstrate the advantages of AI simulation—particularly its scale and speed—a global audit of sports websites was conducted <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. This audit imagined a business seeking to partner with global sports leagues and understand audience engagement across different countries and cultures <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

#### Methodology
*   **Personas**: Two distinct personas were created: a "casual fan" new to sports and a "super fan" who is lifelong and savvy <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   **Websites & Tasks**: Three different sports league websites (basketball, Olympics, English Premier League) were audited <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   **Task Categories**: Tasks were briefed across categories such as navigation, information architecture, and fan engagement, with four tasks per category <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **Simulation**: This resulted in 72 AI-simulated actions, serving as a test drive for the AI-accelerated design audit <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

#### Findings
The audit revealed insights at both high and granular levels <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
*   **High-Level**: Navigation tasks generally performed well across all sites <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. However, as fans delved deeper into browsing content, information architecture, and engagement pathways, initial successes dropped off <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   **Addressing Trust Gap**: This methodology helps identify user pain points, potentially leading to solutions that repair the "AI trust gap" caused by poorly integrated AI <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
*   **Detailed Insights**: The simulation can scale to surface friction in specific, nuanced areas of the user experience, allowing for the creation of focused, broad, and deep design briefs for human teams <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. Computer vision models and human-in-the-loop observation can further refine this process <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

## Future Outlook and Limitations
Looking ahead, tools like Anthropic's MCP protocol show promise in converting prototype components (e.g., in Figma) directly into code components (e.g., React, Node.js) <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. This acceleration in design creation emphasizes the importance of focusing on the "why"—the strategy and user problems to solve—rather than just the "how" <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.

### Limitations and Improvements
This methodology is currently experimental. Key areas for improvement include:
*   **Reproducibility**: Standardizing parameters in a code repository, such as briefing instructions, simulated audience dimensions, audit runs, and task completion/failure parameters <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Validation**: Applying a test and control methodology to isolate the strengths of intelligent twins for design need finding <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>. This will help understand how AI simulation can complement human teams across different industries, geographies, and domains <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.

## Conclusion
Users do not need more non-functional GenAI chatbots on websites <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. Instead, they benefit from better websites, mobile apps, and interfaces that offer clarity and simplicity <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. AI simulation can be a valuable tool to empower design teams to gather insights smarter, faster, and better, ultimately leading to interfaces that restore and repair user trust in AI <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.