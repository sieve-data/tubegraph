---
title: Integrating agents into existing development workflows
videoId: g_tdb0PHPoA
---

From: [[everyinc]] <br/> 

## GitHub Copilot Agent Launch

GitHub has launched GitHub Copilot agents, a development that excited the team and their collaborators at Microsoft <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. The announcement included immediate availability without a waitlist, allowing users to try the agents right away <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. The next phase involves collecting feedback and listening to user reactions <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

## The Evolution of AI in Coding

GitHub Copilot was recognized as one of the first significant [[integrating_ai_with_creative_processes | AI applications]] in the current wave of AI tools, even predating [[integrating_tools_like_chatgpt_in_writing_and_research_processes | ChatGPT]] <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. While Copilot emerged before [[integrating_tools_like_chatgpt_in_writing_and_research_processes | ChatGPT]], it followed the impact of earlier GPT models, such as GPT-2 and GPT-3 <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

The initial idea for Copilot stemmed from playing with GPT-3, observing its ability to generate code in different programming languages <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. Early concepts explored included "code to text" for explaining code in natural language and "conversational coding" or chat interfaces <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. However, these were initially deemed not good enough, with concerns about negative developer reactions if the models weren't yet sufficiently capable <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

The auto-completion or "text to code" approach was pursued first because it fit well with existing developer workflows <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. Developers frequently use imperfect code snippets from various sources, and an AI providing suggestions could complement this process <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. This initial approach created a new market for [[transformative_technologies_in_software_development | AI developer tools]] <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

Copilot has since evolved from auto-completions to include chat, voice, and CLI support <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. It has also incorporated customization, code search, and more context for prompts, leading to the current agent mode in VS Code and the coding agent on GitHub <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

## GitHub's Competitive Landscape

The past year has solidified a race among co-pilot, cursor, and WindSurfs in the AI coding space, with GitHub maintaining the largest user base among them <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. In any competition, continuous reinvention is necessary <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. GitHub emphasizes moving quickly, having shipped over 100 changelogs for Copilot in 2025 by May <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

GitHub views itself as part of the broader developer ecosystem, providing a platform for integration and collaboration <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. They offer Copilot support across multiple IDEs, including VS Code (soon to be open source), Xcode, JetBrains, and Visual Studio <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. Beyond coding, GitHub also plays a role in continuous integration/continuous deployment (CI/CD) and security, competing with various companies in these areas <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

## Foundation: GitHub Actions

The [[development_of_autonomous_agents | Copilot agent]] leverages GitHub Actions, which were introduced in 2018 <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>. GitHub Actions facilitate continuous integration and deployment by allowing users to define workflows (YAML files) that trigger scripts on compute instances based on events like new commits, issues, or pull requests <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. This ecosystem has grown to include over 25,000 actions in their marketplace, allowing for composable automation, including for AI scenarios <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

A key advantage is that customers already trust GitHub's compute layer for their source code and intellectual property <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. When actions run, source code is cloned onto a virtual machine that is shut down and deleted after the script completes, maintaining compliance and access controls <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>. This existing trust facilitates the [[development_of_autonomous_agents | agent]] integration <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

## Seamless Integration and Trust

GitHub believes the best place for [[development_of_autonomous_agents | agents]] is where developers already work <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>. The coding agent can be triggered from Copilot Chat in VS Code, spinning off tasks on GitHub Actions to create draft pull requests, describe plans, and commit changes <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. This mirrors the process of delegating tasks to co-workers, integrating [[development_of_autonomous_agents | agents]] into existing team workflows <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.

The integration ensures that all information, whether from a human or [[development_of_autonomous_agents | agentic]] developer, remains in one place, with session logs stored alongside the repository <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>. Audit logging is also available, allowing enterprises to monitor agent activity for security and compliance <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>. While traditional CI/CD scripts are deterministic, [[development_of_autonomous_agents | AI agents]] are non-deterministic, meaning they can produce different outcomes for the same task <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. This makes seamless integration into familiar review and approval workflows crucial for trust <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.

## Shaping Agent Behavior

GitHub supports multiple models for Copilot, including OpenAI models, Anthropic's Claude series, Google Gemini, and allows users to bring their own keys for services like OpenRouter and DeepSeek <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>. This choice is offered because developers desire flexibility, similar to how they choose programming languages or frameworks <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>. Benchmarks don't always capture a model's suitability for specific languages or personal styles, encouraging developers to experiment and find what works best <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.

[[shaping_ai_agents_to_meet_diverse_developer_needs | Custom instructions]] allow developers to customize agent behavior by creating their own prompt files within the repository <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>. This enables preferences such as receiving responses in a specific human language, while still maintaining code comments in English for team collaboration <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>. This capability helps democratize access to software development by supporting major human languages, unlike the past where English proficiency was often a prerequisite <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>.

## Serving Diverse Developer Audiences

While enterprise customers are a significant part of GitHub's revenue, the largest user base consists of open-source developers and those with free accounts using public repositories <a class="yt-timestamp" data-t="00:21:25">[00:21:25]</a>. Historically, both audiences have been equally important, with GitHub initially focusing on product-led growth <a class="yt-timestamp" data-t="00:21:58">[00:21:58]</a>. A core principle at GitHub is to "put the developer first," meaning all roles within the company use GitHub daily, fostering a deep understanding of developer needs <a class="yt-timestamp" data-t="00:22:43">[00:22:43]</a>.

The definition of a developer is evolving, with some "AI-first" developers potentially writing 90-100% of their code with AI <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>. However, for complex software projects, understanding the code remains fundamental <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>. While low-code/no-code solutions and micro-apps created by [[development_of_autonomous_agents | agents]] for personal tasks are emerging, software as a business still requires human oversight, code review, and approval to prevent security vulnerabilities or functional issues <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>.

## The Future of AI in Development

The future will see a dramatic increase in the use of [[development_of_autonomous_agents | AI agents]], including coding, code review, security, and CI/CD agents <a class="yt-timestamp" data-t="00:27:43">[00:27:43]</a>. Developers who adapt their projects to work efficiently with these [[development_of_autonomous_agents | agents]] will achieve significant productivity gains <a class="yt-timestamp" data-t="00:27:55">[00:27:55]</a>.

However, older codebases (e.g., mainframes, COBOL, C++, Perl) will continue to exist, and while progress is being made in application migration and upgrade agents, a world where everyone works solely with agents is still distant <a class="yt-timestamp" data-t="00:28:05">[00:28:05]</a>. The IDE will remain relevant, becoming increasingly [[development_of_autonomous_agents | agentic]], as will GitHub <a class="yt-timestamp" data-t="00:28:37">[00:28:37]</a>.

There will be opportunities for small companies to use [[development_of_autonomous_agents | agents]] across the entire developer lifecycle—from feature design and prototyping to customer research, competitive analysis, business model creation, implementation, testing, deployment, and monitoring <a class="yt-timestamp" data-t="00:29:06">[00:29:06]</a>. The concept of a "full stack builder" empowered by [[development_of_autonomous_agents | agents]] will likely emerge <a class="yt-timestamp" data-t="00:29:24">[00:29:24]</a>. Despite this, millions of professional software developers will continue to write code traditionally <a class="yt-timestamp" data-t="00:29:28">[00:29:28]</a>. The "race is on" in the AI coding space, driven by a belief in developer choice <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.