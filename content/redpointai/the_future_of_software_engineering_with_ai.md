---
title: The future of software engineering with AI
videoId: n6PazYmo_Qo
---

From: [[redpointai]] <br/> 

Omid Mad, founder of Replit and an early hire at Codecademy, shared his insights on the evolving landscape of software development and the [[the_impact_of_ai_on_software_development_and_programming_jobs | impact of AI on coding]] in a discussion with Jacob Efron and Pat Chase. Replit is a company focused on bringing the next billion developers into the space and is at the forefront of [[the_role_of_ai_in_the_future_of_coding_and_developer_ecosystems | using AI in various ways]] <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Learning to Code in the AI Era

Omid's advice for those starting to learn coding today remains consistent with his pre-AI beliefs: the best way to learn is by making things <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. He argues that traditional academic methods, which involve learning random facts that may never be applied, are not effective for most people <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. Instead, people learn by setting a goal and acquiring knowledge along the way to achieve it <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

AI, particularly Large Language Models (LLMs), takes this "learning by doing" approach to an extreme conclusion <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. With an LLM-powered editor, users can get something running in as little as five minutes, bypassing the drudgery of installations and configurations <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. This provides immediate "dopamine hits" of seeing results, encouraging further experimentation and bigger projects <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

## The Bifurcation of Software Engineering

Omid predicts that [[role_and_expectations_of_software_developers_in_the_context_of_ai_advancements | software engineering]] will bifurcate into two distinct paths, widening the existing gap between front-end and back-end roles <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>:

1.  **Product Creator/Entrepreneur:** This role involves focusing on making something, acquiring customers, and getting users, with less emphasis on traditional coding skills <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. The majority of the time will be spent prompting and iterating on prompts, though debugging code will still be necessary for a period <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
2.  **Traditional Software Engineer:** This path remains largely unchanged, focusing on building cloud infrastructure, data pipelines, and backend systems <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. For this path, a computer science degree is still relevant <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

For those who simply want to be a builder, starting directly with building is encouraged <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

## Replit's AI Integration Strategy

Replit's approach to AI integration is distinctive:

### Embedding AI, Not as an Add-on
Replit initially offered AI features as an add-on called "Ghostwriter," but later renamed it "Replit AI" to reflect its complete integration into the product <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. Omid believes the current era of "co-pilots" as add-ons is transitional, and companies relying on such add-on revenue should be concerned <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. Replit aims to make every interaction with its product AI-powered, including as part of the free plan <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. This internal structural decision encourages designers to start with AI in their workflows, rather than considering AI as an optional addition <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

### Key AI Features
Replit AI currently offers:
*   **Code Suggestions:** Similar to co-pilots, providing suggestions as users type code <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. Replit trains its own models for this, prioritizing speed and power <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
*   **File Generation:** Users can prompt the AI to generate an entire file based on context <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   **AI Debug Button:** When an error occurs in the console, a button appears that opens the AI chat, pre-prompted with the error and relevant context for debugging <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

### Decision to Build Proprietary Models
Replit chose to build its own models, including a 3B parameter model, for several reasons <a class="yt-timestamp" data-t="00:27:10">[00:27:10]</a>:
*   **Latency:** Commercial models did not meet Replit's strict low-latency requirements for an interactive coding environment <a class="yt-timestamp" data-t="00:28:07">[00:28:07]</a>.
*   **Cost:** Building and deploying small models (like their 3B model, which cost around $100K to train) was more affordable than relying solely on commercial APIs, especially for offering AI as part of the free experience <a class="yt-timestamp" data-t="00:28:43">[00:28:43]</a>.
*   **Strategic Advantage:** Developing internal AI talent and having control over the model's characteristics was crucial for Replit to be an "AI-native" company <a class="yt-timestamp" data-t="00:29:45">[00:29:45]</a>.

Despite building their own core models, Replit also uses commercial models for other use cases, such as general-purpose chat features <a class="yt-timestamp" data-t="00:30:10">[00:30:10]</a>.

## Understanding AI Model Capabilities (Data & Training)

Omid views LLMs in a very reductive way, as a function of data and a compression of data <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>. Their power lies in interpolating different data distributions, such as writing a rap song in the style of Shakespeare <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.

### Importance of Data Quality and Diversity
To understand a model's capabilities, one must understand the data it was fed <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>. Key aspects of data quality include:
*   **Size and Compute:** More tokens and more compute generally lead to better models <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.
*   **Diversity and Freshness:** A greater diversity and freshness of tokens are beneficial <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>.
*   **Avoiding "Bad" Data:** Training on minified JavaScript, for example, can negatively impact a model <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>.
*   **Emulating Best Programmers:** GPT models essentially emulate human thinking by guessing the next token, so training on data generated by the best programmers yields higher quality models <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>.
*   **Application Code vs. Infrastructure Code:** While GitHub is rich in high-quality infrastructure code (libraries), there's a "poverty of application code" <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>. Replit shines here as many users write applications on their platform, providing valuable data <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>.
*   **Coding-Adjacent Reasoning:** Even non-coding data, like scientific data or legal text, has been shown to improve code generation abilities by enhancing reasoning <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>. Omid expects 2-3 more years of increased coding capabilities <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.

### Post-Training Mechanisms
These mechanisms refine a foundation model's capabilities for specific downstream tasks <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>. Examples include instruction fine-tuning, RLHF (Reinforcement Learning from Human Feedback), and DPO (Direct Preference Optimization) <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.

### Limits of "Open Source" Tokens
Omid argues that many "open source" models are not truly open source because their training cannot be reproduced <a class="yt-timestamp" data-t="00:31:48">[00:31:48]</a>. Users are dependent on the goodwill of companies like Meta to continue releasing new versions <a class="yt-timestamp" data-t="00:32:27">[00:32:27]</a>. The training data for models like GPT-4 includes vast amounts of internet code data plus hundreds of millions of dollars spent on contractors to annotate coding data <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.

A significant security risk exists when the training process and data of an LLM are not transparent. Backdoors can be hidden in the model that are activated only under specific conditions, and without access to the "source code" (the data), these cannot be recovered or inspected <a class="yt-timestamp" data-t="00:36:17">[00:36:17]</a>. This leads to a future where distinguishing between fiction and reality, or AI-generated content, will become increasingly difficult ("hyperreality") <a class="yt-timestamp" data-t="00:37:05">[00:37:05]</a>.

## Impact of AI on Different Engineer Skill Levels

Initially, Omid believed that AI disproportionately benefited beginners due to the significantly increased return on investment for learning to code <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>. He cited examples of Replit users going from zero to building successful applications and companies in months <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>. Studies, like one on BCG consultants, also indicated that AI benefited lower-rated consultants more than advanced ones <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.

However, Omid suggests that this might change once people are properly trained to use AI effectively <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>. Advanced users, who possess both coding skills and proficiency in prompt engineering techniques (e.g., Chain of Thought), will likely see even greater benefits <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>. Younger generations, due to their brain plasticity, are naturally better at adapting to and building mental models for what LLMs can do <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>. Replit observed that younger users "rolled with it" when AI suggestions appeared, while older, more established users were initially jarred <a class="yt-timestamp" data-t="00:22:35">[00:22:35]</a>. This is analogous to the calculator's introduction in education <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.

## Organizational Structure for AI

Replit structures its teams horizontally, integrating AI across all products rather than in vertical silos <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>. Omid believes this makes business sense, as AI will touch every aspect of software development <a class="yt-timestamp" data-t="00:24:30">[00:24:30]</a>. He is surprised by the slow pace of AI integration into everyday technology and corporate structures, despite its rapid advancement <a class="yt-timestamp" data-t="00:24:38">[00:24:38]</a>.

## The Future of the AI Coding Market

### Microsoft's Dominance
The "default pessimistic assumption" is that Microsoft will dominate the [[the_current_state_and_future_potential_of_ai_in_coding | AI coding market]] due to its existing install base, enterprise relationships, sales team, and leadership <a class="yt-timestamp" data-t="00:51:26">[00:51:26]</a>.

### Emergence of Specialized Companies
However, Omid is optimistic about a new wave of specialized companies focusing on different parts of the software development stack or specific coding workflows <a class="yt-timestamp" data-t="00:52:03">[00:52:03]</a>. For example, companies specializing solely in generating tests (like Codium) could do well <a class="yt-timestamp" data-t="00:53:02">[00:53:02]</a>.

### New Platforms and Holistic Approaches
Companies like Replit, which offer a holistic approach by providing a cloud development environment with AI integrated throughout the entire stack, can build more ambitious AI products, including [[future_of_ai_agents_in_productivity_tools | agentic workflows]] <a class="yt-timestamp" data-t="00:52:36">[00:52:36]</a>. This contrasts with tools like GitHub Co-pilot, which are often locked into an editor and lack broader context (e.g., other repos, Git history, Jira tickets) <a class="yt-timestamp" data-t="00:52:20">[00:52:20]</a>.

### Code Generation Startups
For pure code generation startups, the challenge is that larger models like GPT-5 could make significant leapfrog advancements, potentially outpacing specialized models that cost millions to train <a class="yt-timestamp" data-t="00:54:41">[00:54:41]</a>. While Code Llama has shown strong performance on benchmarks, its "vibes" (practical usability) may not yet match proprietary models <a class="yt-timestamp" data-t="00:54:58">[00:54:58]</a>. Replit, as an applied AI company, is willing to work with any model that delivers value to its users <a class="yt-timestamp" data-t="00:56:12">[00:56:12]</a>.

## The Future of AI Agents

Omid believes [[future_of_ai_agents_in_productivity_tools | AI agents]] represent the next significant leap, more profound than multimodal AI (which he sees as incremental) <a class="yt-timestamp" data-t="00:46:56">[00:46:56]</a>.

*   **Cost as a Barrier:** Agentic workflows, especially with models like GPT-4, are currently very expensive, making them cost-prohibitive for most consumers and developers, particularly for background tasks like refactoring code and running tests <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>.
*   **Accidental Agentic Capabilities:** LLMs like GPT-4 have demonstrated unexpected agentic capabilities <a class="yt-timestamp" data-t="00:41:03">[00:41:03]</a>, although Omid initially thought dedicated "action transformers" would be necessary <a class="yt-timestamp" data-t="00:41:31">[00:41:31]</a>.
*   **Milestones for Agents:** A key milestone for agents will be their ability to reliably follow a bulleted list of actions without going "off the rails" or requiring extensive chain-of-thought prompting <a class="yt-timestamp" data-t="00:49:32">[00:49:32]</a>. The reliability of function calls is also crucial, as current catastrophic failures make them unsuitable for sensitive workflows <a class="yt-timestamp" data-t="00:50:05">[00:50:05]</a>. Metrics like pull request acceptance rates (e.g., Sweep.dev's 30%) indicate progress, but Omrid wants to see this reach 80-90% reliability <a class="yt-timestamp" data-t="00:50:43">[00:50:43]</a>.

Omid expects background agentic workflows to start appearing this year, potentially leading to a "ChatGPT moment" for agents <a class="yt-timestamp" data-t="00:48:01">[00:48:01]</a>. Entrepreneurs should be willing to "walk through walls" and make agents work even if expensive, while more established companies might wait and see <a class="yt-timestamp" data-t="00:48:27">[00:48:27]</a>.

## AI Product Pricing Strategies

Replit adopts a value-based pricing strategy, assuming AI will become table stakes, rather than a cost-plus approach based on current AI expenses <a class="yt-timestamp" data-t="00:42:41">[00:42:41]</a>. They project future reductions in model costs and inference efficiency, while also considering competitive landscapes <a class="yt-timestamp" data-t="00:43:08">[00:43:08]</a>.

Omid also predicts that usage-based pricing will become more prevalent <a class="yt-timestamp" data-t="00:44:24">[00:44:24]</a>. This is because a pure subscription SaaS model can be unsustainable when power users incur significant costs from AI model usage <a class="yt-timestamp" data-t="00:44:43">[00:44:43]</a>. Replit offers bundles with AI, compute, and storage, allowing for overages <a class="yt-timestamp" data-t="00:45:15">[00:45:15]</a>. This model is particularly important when AI models are integrated into CI/CD pipelines, running automatically and incurring costs even when developers are not actively working <a class="yt-timestamp" data-t="00:46:04">[00:46:04]</a>.

## Overhyped and Underhyped AI Trends

*   **Overhyped:** Chatbots, as many things should not be chatbots <a class="yt-timestamp" data-t="00:57:51">[00:57:51]</a>.
*   **Underhyped:** Using LLMs as part of everyday systems and backend call chains <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>.

## Key Learnings from Building LLM Features at Replit

*   **Latency Matters:** The biggest surprise was how crucial latency is. A two-to-three-second response completely changes the user experience compared to 300 milliseconds <a class="yt-timestamp" data-t="00:58:27">[00:58:27]</a>.
*   **Initially Flawed Features:** Inline actions, which leverage cursor context for highly contextual suggestions within the IDE, were initially a "flop" because they weren't exposed well to users <a class="yt-timestamp" data-t="00:59:07">[00:59:07]</a>. After prompting users with UI patterns, adoption grew <a class="yt-timestamp" data-t="00:59:30">[00:59:30]</a>.

## Exciting AI Startups/Companies (Outside Replit)

*   **OpenAI:** Admired for its ambition and willingness to pursue seemingly random ventures like university partnerships, robotics, and self-driving <a class="yt-timestamp" data-t="00:59:56">[00:59:56]</a>. Sam Altman's ability to "spin a whole lot of plates" is impressive <a class="yt-timestamp" data-t="01:00:27">[01:00:27]</a>.
*   **Perplexity:** Highly bullish on Perplexity due to its strong engineering competency and ability to zoom ahead of competitors in search <a class="yt-timestamp" data-t="01:00:57">[01:00:57]</a>.

## Impact on Engineering Team Size

Omid believes that in five years, companies could achieve current outcomes with one-tenth the number of engineers <a class="yt-timestamp" data-t="01:01:43">[01:01:43]</a>. Over ten years, he envisions a "1000x" improvement, leading to a significant reduction in company size due to [[the_impact_of_ai_on_software_development_and_programming_jobs | AI's impact on programming jobs]] <a class="yt-timestamp" data-t="01:01:55">[01:01:55]</a>. While the number of "software creators" will continue to grow, the role might be called something else, much like "movie stars" became "creators" on platforms like TikTok <a class="yt-timestamp" data-t="01:02:12">[01:02:12]</a>.