---
title: The Future of Programming and AI Tools like GitHub Copilot
videoId: qcvMjoJdck4
---

From: [[dwarkesh | The Dwarkesh Podcast]]

The advent of powerful AI models, particularly large language models (LLMs), is poised to significantly reshape the landscape of software development. GitHub Copilot, an AI pair programmer developed by GitHub and OpenAI, stands as a prominent early example of this transformation. Nat Friedman, CEO of GitHub from 2018 to 2021, provided insights into Copilot's development, its current impact, and the broader implications of AI for the future of programming.

## The Genesis of GitHub Copilot

The development of GitHub Copilot was sparked by the release of OpenAI's GPT-3 model in May 2020 <a class="yt-timestamp" data-t="00:50:30">[00:50:30]</a>. Friedman, then CEO of GitHub, was "blown away" by its capabilities and recognized the potential for building products with it <a class="yt-timestamp" data-t="00:50:40">[00:50:40]</a>. Microsoft, GitHub's parent company, had already made a significant investment in OpenAI a year prior, a move Friedman described as a "very prescient bet" <a class="yt-timestamp" data-t="00:50:54">[00:50:54]</a>, <a class="yt-timestamp" data-t="00:52:11">[00:52:11]</a>.

### Early Prototypes and Iterations
The path to the final Copilot product involved several iterations and explorations:

1.  **Chatbot/Q&A System:** The initial prototype was a chatbot intended to function like a Q&A system, similar to Stack Overflow <a class="yt-timestamp" data-t="00:52:51">[00:52:51]</a>. While demos were "fabulous," the models at the time were not reliable enough, often providing useless or wrong answers, leading to a poor product experience <a class="yt-timestamp" data-t="00:53:19">[00:53:19]</a> - <a class="yt-timestamp" data-t="00:53:40">[00:53:40]</a>.
2.  **Large-Scale Code Synthesis:** The team then explored synthesizing large chunks of code, such as entire function bodies <a class="yt-timestamp" data-t="00:53:44">[00:53:44]</a>. An early idea was to display multiple options for the user to choose from, with the intent of using human feedback to improve the model. However, this proved to be a "bad experience" due to the cognitive effort required to evaluate multiple code blocks, many of which were not suitable <a class="yt-timestamp" data-t="00:54:31">[00:54:31]</a> - <a class="yt-timestamp" data-t="00:55:03">[00:55:03]</a>.
3.  **Small-Scale Auto-Complete:** The next step involved simple, small-scale auto-completion using large models, initially presented via an IntelliSense-style drop-down UI <a class="yt-timestamp" data-t="00:54:02">[00:54:02]</a>. This was better but still not quite right.

### The Breakthrough
The key breakthroughs that led to Copilot's current form included:
*   **Inline Suggestions:** Alex Gravely's idea to use the cursor position within the Abstract Syntax Tree (AST) to heuristically determine whether to complete a single line or suggest a full block of code, shown inline <a class="yt-timestamp" data-t="00:55:13">[00:55:13]</a> - <a class="yt-timestamp" data-t="00:55:30">[00:55:30]</a>.
*   **"Gray Text" UI:** Adopting a "gray text" suggestion style, similar to Gmail's smart compose, within the editor <a class="yt-timestamp" data-t="00:55:42">[00:55:42]</a>.
*   **Model Optimization:** Finding a balance for the model size—small enough for low latency but large enough for accuracy—was crucial <a class="yt-timestamp" data-t="00:55:48">[00:55:48]</a>.

This process of tinkering and exploring took approximately four to five months <a class="yt-timestamp" data-t="00:56:05">[00:56:05]</a>.

### Internal Success and Validation
Once these pieces came together, internal usage by GitHub engineers provided strong validation. Retention numbers were "extremely high," with over 60% of users still actively using Copilot 30 days after first install, despite it being an "intrusive product" <a class="yt-timestamp" data-t="00:56:16">[00:56:16]</a> - <a class="yt-timestamp" data-t="00:56:43">[00:56:43]</a>. This indicated a strong product-market fit.

## Impact and Future of AI in Programming

### Productivity Gains
Friedman highlighted that Copilot has already made significant inroads into code generation. At the time of the interview, he stated that "on average, more than half of the code is written by Copilot" for its users, a figure that had grown from the low 20s percent range when it first shipped <a class="yt-timestamp" data-t="01:18:23">[01:18:23]</a>. He sees "no reason why that won't be 95%" in the future <a class="yt-timestamp" data-t="01:18:33">[01:18:33]</a>. These tools are seen as increasing the productivity of both average and the best engineers <a class="yt-timestamp" data-t="01:17:33">[01:17:33]</a>.

### Shift Towards Special-Purpose Software
A potential consequence of drastically lowering the cost of software creation is a shift towards more special-purpose software. Instead of relying heavily on general-purpose tools like spreadsheets, organizations might opt for custom-coded solutions for specific tasks, leading to "every company [having] just a custom piece of code" <a class="yt-timestamp" data-t="01:18:42">[01:18:42]</a> - <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.

### Economic Impact of Text-to-Text AI
Friedman noted that text-to-text tasks, which many AI models excel at, currently represent "low double digit percentages" of the economy <a class="yt-timestamp" data-t="01:23:28">[01:23:28]</a>. The future economic impact is hard to predict; while the cost of such tasks may go down, potentially shrinking certain markets (e.g., gig marketplaces like Upwork <a class="yt-timestamp" data-t="01:24:12">[01:24:12]</a>), Friedman bets that overall demand for these capabilities will increase as new uses are found <a class="yt-timestamp" data-t="01:24:49">[01:24:49]</a>.

### Solving "IQ Soluble" Problems
Friedman posits that "large scale engineering projects are more soluble in IQ than they appear" <a class="yt-timestamp" data-t="01:17:15">[01:17:15]</a>. AI tools like Copilot can effectively augment the "IQ" applied to these problems, thereby enhancing the capabilities of engineering teams.

## Broader Trends in Software Development

### Developer Empowerment
The role of developers has been increasingly empowered, with Friedman noting that developers are now often making IT purchasing decisions, a shift from traditional IT-led procurement [[impact_of_ai_on_software_development_and_productivity | impact of AI on software development and productivity]] <a class="yt-timestamp" data-t="00:42:08">[00:42:08]</a>. Software itself is viewed as "magic" for its ability to systematize and scale valuable processes efficiently <a class="yt-timestamp" data-t="01:00:35">[01:00:35]</a> - <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>.

### Open Source and AI
The open-source ethos of tinkering and accessibility is playing a role in AI development. Friedman mentioned the excitement around efforts like quantizing LLaMA models to run on consumer hardware, enabling more people to experiment [[open_source_ai_models_and_their_implications | open source AI models and their implications]] <a class="yt-timestamp" data-t="00:38:27">[00:38:27]</a> - <a class="yt-timestamp" data-t="00:38:46">[00:38:46]</a>. The fundamental components for current AI models—large datasets (the internet) and powerful GPUs (driven by video games)—are largely commodities <a class="yt-timestamp" data-t="00:39:30">[00:39:30]</a>.

### Proliferation of AI Models
Friedman described the current period as "the year of proliferation" for AI models, APIs, and tools <a class="yt-timestamp" data-t="00:40:12">[00:40:12]</a>. He anticipates widespread proliferation due to factors like the relative ease of training, the public nature of much of the data, commodity hardware, and the rapid propagation of new techniques <a class="yt-timestamp" data-t="01:27:23">[01:27:23]</a> - <a class="yt-timestamp" data-t="01:28:22">[01:28:22]</a>.

## Challenges and Considerations

### Diminishing Returns from Scale
While scaling models has driven progress, Friedman pointed to potential diminishing returns. He noted that GPT-4 was likely two orders of magnitude more expensive to train than GPT-3 but not proportionally more capable or economically valuable [[data_center_energy_requirements_and_scaling | data center energy requirements and scaling]] <a class="yt-timestamp" data-t="01:26:09">[01:26:09]</a> - <a class="yt-timestamp" data-t="01:26:30">[01:26:30]</a>. This raises questions about the long-term cost-effectiveness of simply scaling up.

### Alignment and Safety
Friedman expressed increasing worries about safety issues in the long term, not in the "hijacked version of safety," but more akin to "industrial accident type situations" or misuse [[ai_alignment_and_safety_concerns | AI alignment and safety concerns]] <a class="yt-timestamp" data-t="00:37:55">[00:37:55]</a>. He highlighted a perplexing lack of an "open source technical alignment community" actually implementing alignment tools, with much work happening behind closed doors or remaining in the realm of philosophizing <a class="yt-timestamp" data-t="01:35:45">[01:35:45]</a> - <a class="yt-timestamp" data-t="01:36:05">[01:36:05]</a>.

Despite these challenges, Friedman maintains a "very optimistic" outlook on AI's potential and is actively looking for areas to contribute [[exploring_the_future_of_society_and_economy_with_ai | exploring the future of society and economy with AI]] <a class="yt-timestamp" data-t="01:27:03">[01:27:03]</a>, <a class="yt-timestamp" data-t="01:37:20">[01:37:20]</a>. The development of AI tools like GitHub Copilot represents a significant step in what is likely to be a continuing evolution of programming practices.