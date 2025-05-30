---
title: The evolution of GitHub Copilot and AI coding tools
videoId: g_tdb0PHPoA
---

From: [[everyinc]] <br/> 

GitHub Copilot initially captured the [[the_evolution_of_ai_in_software_engineering|developer zeitgeist in AI]] as one of the first impactful AI applications, even preceding ChatGPT <a class="yt-timestamp" data-t="01:24:00">[01:24:00]</a>. It quickly garnered a significant user base, reportedly reaching around 15 million users <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>. Despite its early success, the broader ecosystem of next-generation [[the_role_of_ai_in_programming_assistance|AI coding]] tools, such as Cursor, Widsf, and Cloud Code, have since emerged, creating a highly [[the_competitive_landscape_in_aipowered_code_suggestion_tools|competitive landscape]] <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>. GitHub acknowledges this competition and continuously aims to [[the_competitive_landscape_in_aipowered_code_suggestion_tools|reinvent itself]] to stay ahead <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>.

## Origin of GitHub Copilot

GitHub Copilot's journey began five years ago, before ChatGPT, but after the advent of [[the_evolution_of_artificial_intelligence|GPT]]-2 and GPT-3 <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>. Following a session by Kevin Scott and Sam Altman discussing transformers and large language models, the GitHub team gained access to GPT-3 <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>. Through [[tinkering_and_experimentation_with_ai_tools|experimentation]]—dictating prompts and observing the model generate code in various programming languages—they realized its potential <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.

Three core concepts were initially explored:
*   **Code to Text (Explanation)**: Explaining code in natural language was considered cool but not good enough, as early prototypes often provided unsatisfactory descriptions <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>.
*   **Chat/Conversational Coding**: This idea was part of the initial concept paper, but the models at the time were not robust enough, leading to concerns about negative user experiences and early abandonment <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>.
*   **Autocompletion (Text to Code)**: This approach, where the editor suggests what comes next, proved to be the most viable <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>. It aligned with existing developer workflows, where developers often deal with imperfect code from typos, forgotten APIs, or copied snippets from sources like Stack Overflow, which require manual adjustment <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>. This became the foundation for GitHub Copilot.

This initial success created a new market, leading to an [[the_competitive_landscape_in_aipowered_code_suggestion_tools|explosion of startups]] in the developer tools space <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>.

## GitHub Copilot's Evolution and Repositioning

Over time, GitHub Copilot expanded its capabilities beyond autocompletion to include chat, voice integration, and CLI support <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>. The latest strategic repositioning involves the launch of **GitHub Copilot agents** <a class="yt-timestamp" data-t="07:49:00">[07:49:00]</a>.

Key aspects of the agent launch:
*   **Agent Mode in VS Code**: Allows synchronous work with an agent in the IDE <a class="yt-timestamp" data-t="07:12:00">[07:12:00]</a>.
*   **Coding Agents on GitHub**: Users can assign issues or tasks to agents that run in the background, capable of parallel execution (e.g., 10 agents at once) <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>.
*   **Integration with GitHub Actions**: The agents leverage GitHub's existing CI/CD infrastructure, actions, which provides a trusted compute layer where source code is temporarily cloned for execution <a class="yt-timestamp" data-t="10:59:00">[10:59:00]</a>. This ensures intellectual property remains within the user's compliance boundary <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>.
*   **Seamless Workflow Integration**: Agents integrate directly into current developer workflows. For instance, a coding agent can be triggered from Copilot Chat in VS Code to create a pull request with tests, mimicking human delegation <a class="yt-timestamp" data-t="13:31:00">[13:31:00]</a>. This preserves the existing review and approval processes <a class="yt-timestamp" data-t="15:28:00">[15:28:00]</a>.
*   **Auditability**: Pull requests from agents are indistinguishable from human-generated ones, and a session log with audit trails is stored with the repository, aiding trust and monitoring for enterprise customers <a class="yt-timestamp" data-t="14:11:00">[14:11:00]</a>.

## Personalization and Choice

GitHub Copilot agents support multiple models, including OpenAI, Anthropic's Claude series, Google Gemini, and DeepSeek <a class="yt-timestamp" data-t="16:30:00">[16:30:00]</a>. This choice allows developers to select models that best fit their personal style or specific language needs, as benchmarks don't always tell the whole story <a class="yt-timestamp" data-t="17:02:00">[17:02:00]</a>. Developers can also provide "custom instructions" through prompt files within the repository to customize model behavior, such as specifying interaction language while maintaining English code comments <a class="yt-timestamp" data-t="18:25:00">[18:25:00]</a>. This democratizes access to software development by enabling interaction in any major human language <a class="yt-timestamp" data-t="19:36:00">[19:36:00]</a>.

## Serving Diverse Developer Audiences

GitHub serves a wide array of users, from large enterprise customers (a significant portion of its revenue) to a larger base of open-source and hobbyist developers who use free accounts <a class="yt-timestamp" data-t="21:23:00">[21:23:00]</a>. GitHub's core principle is "developer first," meaning product decisions prioritize the individual developer's needs <a class="yt-timestamp" data-t="22:47:00">[22:47:00]</a>. The company itself extensively uses its own products internally, ensuring a deep understanding of the developer experience <a class="yt-timestamp" data-t="23:06:00">[23:06:00]</a>.

While the definition of a "developer" is evolving with the rise of [[the_evolution_of_ai_in_software_engineering|AI-first developers]] who might [[the_role_of_ai_in_programming_assistance|write 90-100% of their code with AI]] <a class="yt-timestamp" data-t="20:41:00">[20:41:00]</a>, GitHub believes that understanding the underlying code remains crucial, especially for complex projects where software is the core business <a class="yt-timestamp" data-t="24:14:00">[24:14:00]</a>. Although [[developing_apps_and_prototypes_using_ai|low-code/no-code]] solutions exist, and [[developing_apps_and_prototypes_using_ai|Manos]] is an example of creating a [[developing_apps_and_prototypes_using_ai|micro-app or personal software]] quickly from a prompt, the ability to inspect and understand the generated code is vital for security, functionality, and long-term maintainability <a class="yt-timestamp" data-t="24:27:00">[24:27:00]</a>.

## The Future of Coding with AI

Looking ahead, GitHub anticipates a future where [[exploring_human_and_ai_collaboration|AI agents]] become ubiquitous across the entire developer lifecycle <a class="yt-timestamp" data-t="27:43:00">[27:43:00]</a>. This includes:
*   **Coding Agents**: For generating code <a class="yt-timestamp" data-t="27:43:00">[27:43:00]</a>.
*   **Code Review Agents**: For reviewing pull requests <a class="yt-timestamp" data-t="10:05:00">[10:05:00]</a>.
*   **Security Agents**: For identifying and fixing vulnerabilities <a class="yt-timestamp" data-t="10:07:00">[10:07:00]</a>.
*   **CI/CD Agents**: For monitoring cloud resources <a class="yt-timestamp" data-t="10:17:00">[10:17:00]</a>.
*   **App Migration Agents**: For upgrading codebases (e.g., Java upgrades) <a class="yt-timestamp" data-t="28:24:00">[28:24:00]</a>.

These agents can be stitched together for end-to-end automation, from feature design and prototyping to testing, deployment, and monitoring <a class="yt-timestamp" data-t="10:10:00">[10:10:00]</a>. The "full stack builder" concept, powered by agents, is expected to grow <a class="yt-timestamp" data-t="29:24:00">[29:24:00]</a>. However, while some progress will be made in app migration, traditional development with IDEs and manual code writing will persist, particularly for complex and legacy systems <a class="yt-timestamp" data-t="28:05:00">[28:05:00]</a>. The IDE will become increasingly "agentic," but developers will still be hands-on with the code, understanding its intricacies and debugging challenges <a class="yt-timestamp" data-t="28:37:00">[28:37:00]</a>.