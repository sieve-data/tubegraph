---
title: Best practices for building GenAI teams
videoId: n9rjuBuShko
---

From: [[aidotengineer]] <br/> 

Building a dedicated team for a GenAI platform is a critical component for success, especially given the unique challenges and opportunities presented by Generative AI systems <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

## Why a Dedicated GenAI Team is Critical <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>

GenAI systems differ significantly from traditional AI systems. In traditional AI, there's a clear separation between model optimization and model serving phases, allowing AI engineers and product engineers to operate in different tech stacks without needing to work on the same codebase <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. However, in GenAI, this distinction blurs, meaning everyone is an engineer who can optimize overall system performance <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>. This creates new challenges for tooling and [[best_practices_for_implementing_ai_in_teams | best practices]] within a company <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

GenAI and agent systems are considered "compound AI systems," tackling AI tasks using multiple interacting components, such as multiple calls to models, retrievers, or external tools <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. A dedicated GenAI platform team helps bridge the skill gap between AI engineers and product engineers <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.

## Ideal Candidate Qualities <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>

When [[building_and_recruiting_ai_teams | building and recruiting AI teams]] for GenAI, an ideal candidate possesses a mix of technical and soft skills:
*   **Strong Software Engineer**: Capable of building infrastructure integrations <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.
*   **Developer PM Skills**: Good at designing interfaces <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.
*   **AI and Data Science Background**: Understanding of the latest techniques <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.
*   **Hands-on Learner**: Able to learn from the latest techniques while being practical <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.

Finding a single "unicorn" engineer with all these qualities can be very challenging <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.

## Hiring Principles <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>

Given the difficulty in finding ideal candidates, companies often make trade-offs in hiring. Key principles include:
*   **Prioritize Software Engineering Skills**: Strong software engineering skills are generally prioritized over AI expertise <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
*   **Hire for Potential**: Focus on a candidate's potential rather than just experience or degrees, as the field evolves rapidly and experience can quickly become outdated <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
*   **Critical Thinking**: Emphasize critical thinking, as solutions built today may be outdated within a year or even less than six months. Teams must constantly evaluate new open-source packages, engage with vendors, and proactively deprecate their own solutions <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>.

## Building a Diversified Team <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>

To overcome the challenge of finding a single engineer with all desired qualifications, a recommended approach is to hire a diversified team <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>. This can include:
*   Full-stack software engineers <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>
*   Data scientists <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>
*   AI engineers <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>
*   Data engineers <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>
*   Fresh graduates from top research universities <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>
*   Individuals with startup backgrounds <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>

By combining these diverse skills within projects, strong engineers will naturally pick up new skills and evolve into the ideal candidates over time <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. This strategy contributes to [[building_successful_ai_projects_with_small_teams | building successful AI projects with small teams]] and fostering [[strategies_for_effective_ai_implementation | effective AI implementation]].

## Tech Stack Considerations <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>

When choosing a tech stack for a GenAI team, Python is strongly recommended due to its prevalence in research and open-source communities <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>. It has proven to be scalable in practice <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.

## Key Components for GenAI Teams <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>

Teams building GenAI platforms should focus on:
1.  **Prompt Source of Truth**: Establish a robust system for version controlling prompts, similar to how traditional model parameters are managed. This is crucial for operational stability and preventing accidental production errors <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.
2.  **Memory Management**: Build a system for managing conversational and experiential memory, which allows for injecting rich data into the agent experience and extracting tacit knowledge from interactions <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. This is vital for [[best_practices_for_building_ai_agents | building AI agents]].
3.  **Skill Uplifting**: In the agent era, a key new component is uplifting APIs into "skills" that agents can easily call. This requires surrounding tooling and infrastructure <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>. This relates to the [[role_of_engineering_teams_in_ai_agent_production | role of engineering teams in AI agent production]].
4.  **Observability**: Because agents are autonomous and can make decisions on which APIs or LLMs to call, predicting their behavior is difficult. Investing in observability tools (e.g., in-house solutions on top of OpenTelemetry) to track low-level telemetry data allows for replaying agent calls and guiding future optimization <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. This is a key aspect of [[best_practices_for_building_resilient_ai_workflows | building resilient AI workflows]].

## Scaling and Adoption Strategies <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>

To ensure successful adoption and scaling of the GenAI platform:
*   **Solve Immediate Needs First**: Instead of trying to build a full-fledged platform from the outset, focus on solving immediate needs. Start with simpler components (e.g., a Python library for orchestration) and allow the platform to grow organically <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.
*   **Focus on Infrastructure and Scalability**: Leverage existing robust infrastructure where possible, such as using messaging infrastructure as a memory layer for cost efficiency and scalability <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>. This contributes to [[leadership_and_organizational_strategies_for_ai_integration | leadership and organizational strategies for AI integration]].
*   **Prioritize Developer Experience**: The ultimate goal of a GenAI platform is to enhance developer productivity. Design the platform to align with existing developer workflows to ease adoption and increase success <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>. This addresses a common issue in [[challenges_in_implementing_gen_ai_projects | implementing Gen AI projects]].