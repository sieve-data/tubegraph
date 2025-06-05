---
title: Pain points in documentation workflows
videoId: pSqpC7fFLZA
---

From: [[aidotengineer]] <br/> 

Documentation teams often face significant challenges that can lead to burnout and reduced throughput <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. These issues are particularly acute for smaller teams managing a large volume of requests <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Key Challenges

### 1. Error-Prone First Drafts
A major pain point is receiving error-prone first drafts from numerous product teams, sometimes over 100 <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. These drafts require substantial cleanup and correction before they can be published.

### 2. Time-Consuming Grooming
Even once drafts are submitted, the "grooming" process is a significant time sink <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. This includes:
*   **Style checks:** Ensuring consistency with established style guides <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   **Alt text generation:** Creating descriptive alternative text for images to improve accessibility <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   **SEO optimization:** Adding appropriate meta-titles and descriptions for search engine discoverability, while adhering to character limits <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>, <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>, <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **Jargon simplification:** Translating technical development terms into plain English for broader understanding <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

### 3. Hallucination Risk with AI
While [[AI integration in documentation teams | AI]] offers many [[benefits_and_challenges_of_using_ai_in_workflow | benefits]], there's a significant risk of "hallucinations" – instances where the AI generates incorrect or nonsensical information – if not properly managed <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>, <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. Mitigating this requires a layered approach with human oversight and validation <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>, <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

### 4. Inconsistent AI Performance
Even with advanced models, AI can exhibit [[issues_with_nondeterministic_and_deterministic_workflows | nondeterministic behavior]]. For example, an automated editor might sometimes catch a missing SEO description but miss it at other times <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. This inconsistency necessitates additional human review or specialized tools for specific tasks.

## Mitigating Pain Points with AI

To address these pain points, teams can leverage [[multiagent_systems_in_technical_workflows | multiagent systems]] and layered workflows <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>, <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. By building single-purpose AI agents for repeatable, high-volume, and rule-based tasks with low creativity requirements, human team members can focus on judgment and clarity <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>, <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

### Guard Rails Against Risks
To ensure quality and reduce risks, several guard rails can be implemented:
*   **Hallucination Mitigation:** Utilize linting tools (e.g., Veil Lint) and CI/CD tests <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>, <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. Crucially, human review (code owner, product, and engineering reviews) is required before merging any AI-suggested changes <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>, <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>, <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
*   **Bias Reduction:** Implement data set tests and conduct regular prompt audits <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   **Stakeholder Misalignment:** Conduct weekly pull request (PR) reviews and maintain Slack feedback loops with product managers and engineering teams to continuously tune AI prompts <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.

This strategic [[impact_of_ai_on_development_workflow | integration of AI]] helps [[improving_developer_experience_and_productivity | improve developer experience and productivity]] by streamlining repetitive tasks, allowing humans to focus on higher-value work <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.