---
title: Evolution and growth of Windsurf as an AI coding tool
videoId: 5Z0RCxDZdrE
---

From: [[lennyspodcast]] <br/> 

Windsurf, co-founded by Varun Mohan, has rapidly emerged as a leading [[Impact of AI on coding practices and developer productivity | AI coding tool]], positioning itself as a main competitor to [[cursor_ai_coding_tool | Cursor]] with over a million users in just four months <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. The company behind Windsurf, Kodium, has a history of strategic pivots that led to its current success in the AI software development space <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Kodium's Origins and Strategic Pivots

Kodium was founded nearly four years ago, before [[Role of AI in Software Development | AI coding]] and ChatGPT were prevalent <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

### From GPU Infrastructure to AI Applications
Initially, Kodium focused on building GPU virtualization and compiler software, operating under the belief that deep learning would permeate many industries beyond just autonomous vehicles, including financial services, defense, and healthcare <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. Their service optimized complex deep learning applications to run efficiently on computers without dedicated GPUs <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

By mid-2022, Kodium was generating millions in revenue and managing over 10,000 GPUs with a lean team of eight, operating cash flow positive <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. However, with the rise of generative AI models, the company realized that their infrastructure-focused offerings would become less valuable as everyone would eventually use similar underlying infrastructure <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

This led to a pivotal decision: Kodium decided to "vertical integrate" and leverage their inference infrastructure to build applications, viewing generative AI as the "next internet" <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. They became early adopters of GitHub Copilot and recognized the immense disruption coming to the coding space <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. Kodium began by offering a free autocomplete model across various IDEs (VS Code, JetBrains, Eclipse, Visual Studio, Vim, Emacs), made possible by their infrastructure optimization <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

### The Birth of Windsurf as a Custom IDE
As large businesses like Dell and JP Morgan Chase showed interest, the focus shifted from mere autocomplete to secure, personalized offerings that deeply understood private company data and codebases <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. Six months prior to the interview, Kodium realized that existing IDEs, particularly VS Code, were limiting the AI capabilities they could offer users <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

This led to their second major pivot: forking VS Code to build their own IDE, Windsurf, incorporating [[ai_interfaces_and_future_trends_in_software_development | new agentic capabilities]] <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. This decision, though risky, significantly improved user experience, tripling the acceptance rate of AI suggestions for features like inline refactors, even with the same machine learning models <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>. The core premise was that if AI would write over 90% of the software, the interface needed to evolve beyond a pure text editor <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

## What is Windsurf?

Windsurf is an Integrated Development Environment (IDE) designed to build software and applications <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.

### Core Features and Differentiators
*   **AI-Centric Interface**: Unlike traditional IDEs, Windsurf's interface anticipates AI writing the vast majority of code, shifting the developer's role to reviewing and guiding the AI <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>. It includes custom review flows tailored for AI-generated code <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>.
*   **Codebase Understanding**: A key differentiator is Windsurf's deep codebase understanding, crucial for large enterprises with hundreds of millions of lines of code, like Dell <a class="yt-timestamp" data-t="00:37:58">[00:37:58]</a>. This involves proprietary models that consume and rank vast code chunks in parallel to provide relevant snippets for any query <a class="yt-timestamp" data-t="00:38:18">[00:38:18]</a>.
*   **Multi-Platform Support**: While Windsurf is a custom IDE, Kodium remains committed to supporting other platforms like JetBrains, which is popular among Java developers <a class="yt-timestamp" data-t="00:39:41">[00:39:41]</a>. The goal is to provide an "agentic experience" to every developer, meeting them where they are <a class="yt-timestamp" data-t="00:40:06">[00:40:06]</a>.
*   **Enterprise Security & Hybrid Mode**: Windsurf offers robust security features, including FedRAMP compliance for government entities, and a hybrid mode where code indexing and data live on the user's tenant, protecting intellectual property <a class="yt-timestamp" data-t="00:40:48">[00:40:48]</a>.
*   **Visual Development**: Windsurf can generate and modify applications based on images and natural language prompts. Users can select UI elements directly in a live preview to make changes, bridging the gap between app space and code space <a class="yt-timestamp" data-t="00:45:17">[00:45:17]</a>.
*   **Intelligent Refactoring**: Windsurf understands user changes to the codebase and can propagate these changes throughout the entire application, making large-scale refactors and migrations more efficient <a class="yt-timestamp" data-t="00:47:19">[00:47:19]</a>.

## Traction and Growth
In a little over four months since its launch, Windsurf has attracted over 1 million developers and currently boasts hundreds of thousands of monthly active users <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.

## Underlying Technology and Models
Windsurf employs a hybrid approach, combining powerful foundational models with custom, internally developed models:
*   **Planning**: It utilizes models like Anthropic's Sonnet or OpenAI's GPT-4o for high-level planning <a class="yt-timestamp" data-t="00:54:14">[00:54:14]</a>.
*   **Retrieval and Context**: Kodium runs its own models for high-quality retrieval to help the agent understand the codebase. This is crucial for large codebases (e.g., 100 million lines of code) which are too large for commercial models to handle efficiently due to token limits, cost, and latency <a class="yt-timestamp" data-t="00:54:30">[00:54:30]</a>.
*   **Edits and Autocomplete**: Custom models, post-trained on popular open-source models, are used for fast edits and autocomplete functionality. These models are better at applying changes and handling incomplete code states, leveraging millions of pieces of user feedback hourly <a class="yt-timestamp" data-t="00:55:08">[00:55:08]</a>.

This strategy ensures that Windsurf builds or trains models where it can be best, while leveraging external models for other tasks, avoiding "ego-driven" development <a class="yt-timestamp" data-t="00:56:15">[00:56:15]</a>.

## Impact on Software Development and Future Outlook

Windsurf's rise reflects a significant shift in software development, with Varun Mohan predicting that AI will write over 90% of the code <a class="yt-timestamp" data-t="00:14:09">[0:14:09]</a>.

### The Evolving Role of Engineers
The [[Impact of AI on coding practices and developer productivity | role of a developer]] is transforming <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. Instead of primarily writing code, engineers will focus more on defining "what should I solve for" and "how should I solve it" <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>. AI will increasingly handle the "solving it" part, and with deep codebase understanding, even suggest "how to solve it" based on best practices <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>. This means engineers can dedicate more time to identifying critical business problems and making strategic technical decisions <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.

Varun emphasizes that foundational understanding of computer science principles remains valuable for engineers, as it aids in debugging, performance optimization, and architectural decisions <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>.

### The Rise of Agency
A crucial skill for the evolving engineering landscape is "[[Skills for the Evolving Engineering Landscape | agency]]" <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>. This refers to individuals who are driven to build and solve problems without being given rigid, well-defined paths <a class="yt-timestamp" data-t="00:21:47">[00:21:47]</a>. Windsurf's capabilities empower non-developers, such as those in marketing or sales, to build their own custom applications and tools, reducing the need for expensive vertical SaaS products <a class="yt-timestamp" data-t="00:51:51">[00:51:51]</a>. This highlights how [[Building and scaling AIenabled tools | building more and more of our products]] internally can be achieved with AI tools, transforming the cost-benefit analysis of building versus buying software <a class="yt-timestamp" data-t="00:52:17">[00:52:17]</a>.

### Hiring Philosophy
Kodium maintains a lean hiring philosophy, only bringing on new staff when a function is "underwater," ensuring ruthless prioritization and avoiding manufactured work <a class="yt-timestamp" data-t="00:24:41">[00:24:41]</a>. This strategy aims to be the "smallest company we can be to satisfy our ambitions" <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>. The company values high technical aptitude, passion for the mission, and a strong work ethic <a class="yt-timestamp" data-t="00:31:01">[00:31:01]</a>.

Despite AI writing more code, the overall [[Impact of AI on coding practices and developer productivity | engineering output]] per person has increased, leading to a higher ROI for building technology <a class="yt-timestamp" data-t="01:05:56">[01:05:56]</a>. For companies with high technology ceilings, this means they may even hire *more* engineers, as AI tools amplify their capacity to innovate and build <a class="yt-timestamp" data-t="01:06:04">[01:06:04]</a>.

### Long-Term Vision
Kodium's long-term strategy involves continuous, self-cannibalizing innovation <a class="yt-timestamp" data-t="01:07:20">[01:07:20]</a>. They aim to make their existing product "look silly" every 6 to 12 months by developing new features and capabilities that are not merely incremental but truly disruptive, anticipating user needs rather than just responding to them <a class="yt-timestamp" data-t="01:07:24">[01:07:24]</a>. This [[the_future_of_ai_in_software_development | future of AI in software development]] requires a blend of listening to users for iterative improvements and making bold, long-term bets that redefine the product <a class="yt-timestamp" data-t="01:07:51">[01:07:51]</a>.

## Tips for Success with Windsurf
For new users, Varun offers a few key tips:
1.  **Patience and Explicit Prompts**: Be patient and as explicit as possible when asking the AI to make changes, especially starting with smaller modifications to avoid large, irrelevant changes <a class="yt-timestamp" data-t="00:43:28">[00:43:28]</a>.
2.  **Understand Capabilities**: Users should develop an intuitive understanding of the model's capabilities, similar to how one learns the "hills and valleys" of an autocomplete product. This helps in knowing when to expect success or to refine commands <a class="yt-timestamp" data-t="00:44:06">[00:44:06]</a>.
3.  **Get Hands Dirty**: The best way to leverage tools like Windsurf is to actively use them for [[Building Web Products with AI Tools | building apps]], [[prototyping_and_experimenting_with_ai | making mocks]], and modifying existing codebases <a class="yt-timestamp" data-t="01:11:30">[01:11:30]</a>. This enables individuals to become a "force multiplier" within their organizations, even allowing product managers to directly make and push code changes <a class="yt-timestamp" data-t="01:11:39">[01:11:39]</a>.