---
title: Prompt engineering techniques
videoId: exzPO4hAD9s
---

From: [[everyinc]] <br/> 

[[prompt_engineering_and_its_importance | Prompt engineering]] is fundamentally about injecting domain knowledge into a large language model (LLM) system to achieve desired outputs <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>. It's often described as a process of continuous iteration and experimentation, rather than a rigid science <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. The core goal is to effectively map inputs to the desired outputs <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>.

Jared, co-founder and CEO of Prompt Layer, describes his company's platform as a [[the_role_of_prompt_engineering_in_app_development | prompt engineering]] platform, launched around the time ChatGPT was introduced <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>, <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>. It originated as an internal tool <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>, focusing on building a workflow to iterate and improve the "source code" of LLM applications <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>.

## Core Primitives of Prompt Engineering

Prompt engineering workflows are built around three core primitives: the prompt, the evaluation (eval), and the data set <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. While one of these elements can be automated, the others remain essential <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>.

### The Prompt

The prompt consists of the instructions given to the LLM <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. For example, in an AI math tutor application, this would include the specific prompts guiding how the AI responds to student questions <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>.

Some criticisms exist regarding common prompting practices:
*   **Research Papers on Prompting** Research papers suggesting new prompting strategies are often viewed with skepticism, as prompt engineering is seen as more akin to the scientific method—trying things, observing results, and iterating—rather than a theoretical science <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>, <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.
*   **General Purpose System Prompts** System prompts used by models like ChatGPT or Anthropic are criticized for being "bad" <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. These prompts often accumulate "prompt debt" by being long and constantly updated with new "do this/don't do this" rules to cover broad use cases <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>, <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>. This approach makes them less clear and concise <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>.

### Evaluation (Eval)

Evaluations are methods used to test the prompt's effectiveness <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. A simple starting point is to backtest on old data to observe how changes in the prompt affect responses <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>. If a "ground truth" (e.g., thumbs up/down, a completed sale) is available, A/B testing can be used to anchor evaluations on real metrics <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>.

For use cases without a clear ground truth, such as summarizing calls or emails, evaluations require defining specific heuristics <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>. This involves breaking down what a human would consider a "good" summary into individual characteristics (e.g., "does not contain an excerpt at the bottom," "uses correct markdown") and building metrics based on those characteristics <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>.

### Data Set

Data sets are crucial for training and testing prompts <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. If backtest data isn't available, focus on building ground truth data sets <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>. Synthetic data generation can also be used to bootstrap data sets <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.

The challenge of evaluating problems without ground truth (e.g., in AI therapy) highlights a key limitation of relying solely on data-driven approaches <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>. While data can help reach a "local minimum," human domain expertise provides the necessary differentiation and ability to define the problem and handle edge cases <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>.

## Best Practices in Prompt Engineering

Effective [[prompt_engineering_and_its_importance | prompt engineering]] prioritizes rapid iteration and closing the feedback loop <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>, <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>.

### Operationalizing Prompts

Instead of trying to find a "correct" prompt, focus on making prompts easily editable and testable in an operational context <a class="yt-timestamp" data-t="03:15:00">[03:15:00]</a>. The best prompt engineers treat the LLM as a "black box," focusing on mapping inputs to desired outputs rather than understanding internal mechanisms <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>, <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>.

### Prompt Routing Approach

A recommended technique is the "prompt router" approach <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>. Instead of stacking messages in one monolithic prompt, build a workflow, directed acyclic graph (DAG), or graph, and route user queries to the appropriate prompt <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>. This approach offers several benefits:
*   **Specialization:** Prompts do "one thing and do one thing really well" <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>.
*   **Testability:** Easier to test and collaborate <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>.
*   **Reliability:** Less likely to fail <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>.
*   **Jailbreaking Prevention:** If each prompt has a specific function, it reduces the risk of unintended outputs <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.

However, there's a trade-off: specialized prompts may have less flexibility for unexpected user messages, while a single general prompt, though capable of answering anything, might not always be accurate <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>, <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>. It might be beneficial to start with a single prompt for initial iterations and then transition to a more structured, routed approach as the product matures and use cases become clearer <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>.

### Model-Specific Idioms

Understanding model-specific "idioms" is also beneficial. For example, Claude models work better with XML, while GPT models prefer Markdown <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>. Using tool calling and function calling, even for non-function tasks, can convey more information to the AI because it's a language the model understands implicitly <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>.

## The Rise of the Non-Technical Prompt Engineer

A significant shift in [[the_role_of_prompt_engineering_in_app_development | prompt engineering]] is the emergence of non-technical domain experts in the driver's seat <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>, <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. This became apparent when Prompt Layer discovered that a prompt engineer for an AI parenting coach app was a teacher with 15 years of experience and no technical background <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>, <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>. Engineers set up the tool for her, allowing her to directly edit prompts and see immediate changes in the app <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>, <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>.

The core thesis is that success in the age of generative AI won't come from hiring the best ML engineers or building defensibility through machine learning for most companies <a class="yt-timestamp" data-t="04:45:00">[04:45:00]</a>, <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>. Instead, it will come from collaborating with domain experts who can accurately define the problem and its specifications <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>.

Examples like AI teachers, therapists, doctors, and lawyers highlight this need. An engineer lacks the domain knowledge to dictate how an AI therapist should respond to someone experiencing depression <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>, <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>. This approach acknowledges that for many problems, there isn't one "best" prompt or solution, and different approaches will cater to different contexts and user needs <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>, <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>, <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a>.

This shift means:
*   **Domain knowledge is key:** It's about bringing the deep expertise of a field into the AI's "source code" <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>.
*   **Focus on Problem Definition:** The hardest part is defining the problem to be solved, even with advanced [[transformative_technologies_in_software_development | AI tools]] <a class="yt-timestamp" data-t="06:10:00">[06:10:00]</a>, <a class="yt-timestamp" data-t="06:24:00">[06:24:00]</a>.
*   **Irreducibility:** Similar to computational irreducibility (a concept from Stephen Wolfram), there are parts of problem-solving that cannot be simplified or collapsed, even with powerful AI <a class="yt-timestamp" data-t="07:54:00">[07:54:00]</a>, <a class="yt-timestamp" data-t="08:25:00">[08:25:00]</a>. The irreducible part is often defining *what* to tell the AI to solve <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>.

Companies are starting to realize this need for non-technical prompt engineers when they begin building revenue-generating products that require team collaboration. The need for handoffs between engineers and QA testers or legal experts who ask specific questions highlights the bottleneck of traditional ML engineering in domain-specific applications <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>, <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>, <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a>, <a class="yt-timestamp" data-t="08:07:00">[08:07:00]</a>.

This evolving landscape reflects a broader trend where [[ai_tools_for_design_and_creation | AI tools]] are lowering the cost of creation, enabling "single-use software" and personalized content that previously wouldn't have been economically viable to produce <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>, <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>, <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>. While AI can produce "junk food" content, there will always be a place for human-crafted, "farm-to-table" creative works <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>.

## The Future of Prompt Engineering

The [[the_evolution_and_future_of_software_engineering | evolution and future of software engineering]] in AI suggests a move toward more nuanced and diversified approaches <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>, <a class="yt-timestamp" data-t="04:23:00">[04:23:00]</a>.
*   **Multiple Models/Approaches:** There is "no one prompt to rule them all" <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>, and different companies will differentiate themselves by how they define and solve problems with AI <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>, <a class="yt-timestamp" data-t="05:59:00">[05:59:00]</a>.
*   **Pluralistic Framework:** The future of AI will involve multiple models, stakeholders, and approaches to a given problem, reflecting the inherent complexity and context-dependency of real-world solutions <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>, <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>.
*   **Domain Experts Driving Innovation:** The market will naturally push companies to empower domain experts, as these will be the winners in delivering highly tailored and effective AI applications <a class="yt-timestamp" data-t="08:27:00">[08:27:00]</a>.
*   **Beyond AGI:** The focus should be on building with AI as a cool technology for language-to-data and data-to-language transformation, rather than solely on the hypothetical future of AGI (Artificial General Intelligence) <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>, <a class="yt-timestamp" data-t="10:33:00">[10:33:00]</a>. Current models like [[prompting_techniques_for_o1_model | O1]] have limitations in basic reasoning that humans easily grasp, indicating there's still "a lot of work to do" before AGI is achieved <a class="yt-timestamp" data-t="09:17:00">[09:17:00]</a>, <a class="yt-timestamp" data-t="09:59:00">[09:59:00]</a>.