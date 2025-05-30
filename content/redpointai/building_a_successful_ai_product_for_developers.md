---
title: Building a successful AI product for developers
videoId: XsANqI-WnjY
---

From: [[redpointai]] <br/> 

Sourcegraph, led by CTO and co-founder Beyang Liu, has been at the forefront of [[Developing and utilizing AI models in the tech industry | building AI products]] for developers. Their flagship product, Cody, is an AI coding assistant designed to enhance software development by providing contextual assistance and automation <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This article explores Sourcegraph's approach to [[Building AI startups and the challenges of scaling | building and scaling AI products]], their insights into the evolving landscape of AI in coding, and their vision for the future of software engineering.

## The Evolving Role of Software Developers in the Age of AI

AI is rapidly transforming software development. While some may provocatively ask if AI will "steal my job," the reality is that coding is one of the best use cases for AI seen so far, with over a million paying users for tools like GitHub Copilot <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a> <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

Instead of replacing developers, AI is expanding the horizons of software creation, enabling the generation of high-quality software with increased leverage from technical thinking <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a> <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a> <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. The essence of software creation lies in connecting the product side (delivering value to end-users) with the underlying computational pieces (bits, bytes, data structures, algorithms) <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. A significant portion of a developer's time is spent understanding existing codebases and acquiring context, rather than actively producing and shipping features <a class="yt-timestamp" data-t="01:07:10">[01:07:10]</a> <a class="yt-timestamp" data-t="01:07:17">[01:07:17]</a>. AI aims to automate this "toil and drudgery," allowing developers to focus on more creative and high-value tasks <a class="yt-timestamp" data-t="01:08:06">[01:08:06]</a> <a class="yt-timestamp" data-t="01:08:09">[01:08:09]</a>.

The definition of "engineering" and the day-to-day experience of a software developer are expected to change drastically, leading to a potentially better job <a class="yt-timestamp" data-t="01:06:11">[01:06:11]</a> <a class="yt-timestamp" data-t="01:06:56">[01:06:56]</a>. The number of engineers is projected to grow, possibly accelerating in the medium to long term <a class="yt-timestamp" data-t="01:05:48">[01:05:48]</a>.

## Sourcegraph's AI Offerings: Cody and Code Search

Sourcegraph offers two main products for developers:
1.  **Code Search Engine**: Designed to help human developers understand code. It allows users to search vast codebases, acquire understanding, and navigate code references (e.g., go to definition, find references) to gain context and effectiveness <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a> <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
2.  **Cody (AI Coding Assistant)**: Performs functions expected of an AI coding assistant, including:
    *   **Inline completion**: Completing thoughts as code is typed in the editor <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
    *   **Chat**: Answering high-level questions about code and generating code for specific tasks <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
    *   **Commands**: Targeting specific actions and "toil" in the software development loop, such as writing doc strings or high-quality unit tests <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

Cody's differentiator is its ability to operate with contextual awareness of the user's codebase, providing more relevant and precise suggestions than general models trained on open-source code or Stack Overflow <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a> <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. This context is supplied by Sourcegraph's search capabilities <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

## [[Challenges in building and deploying AI features | Current State of AI in Coding]]

Currently, AI in coding primarily excels as "inner loop accelerants" <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. The "inner loop" refers to the daily cycle of a developer: figuring out how to do something, writing code, testing it, and repeating <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. Tools like code completion or code-aware chat help automate commonplace or "uninteresting" functions, allowing the AI to autocomplete or generate boilerplate code <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a> <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

The next frontier is "multi-step, bot-driven development," where the AI drives the process and the human acts as an advisor <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a> <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. While tools like Devin show promise, human oversight and assistance are still required for the majority of issues <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a> <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

## Factors Driving AI Product Improvement

### Model Advancements and [[Challenges and strategies in AI model development | Evaluation]]
Model advancements, such as the progression from GPT-3.5 to GPT-4 and Claude 3, have significantly enabled new use cases and improved reliability in AI coding assistants <a class="yt-timestamp" data-t="01:13:10">[01:13:10]</a> <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>. Sourcegraph allows users to select between different frontier models (e.g., GPT-4, Claude 3, Mixtral) in Cody's chat view, finding that Claude 3 and GPT-4 excel at integrating context into working code examples, while Mixtral is favored for its speed <a class="yt-timestamp" data-t="01:13:21">[01:13:21]</a> <a class="yt-timestamp" data-t="01:14:01">[01:14:01]</a>.

When a new model like GPT-5 is released, Sourcegraph aims to integrate it quickly to allow users to experiment and provide feedback <a class="yt-timestamp" data-t="01:17:37">[01:17:37]</a>. This user feedback, combined with product usage metrics (like completion acceptance rate and overall volume), is often prioritized over traditional benchmarks, as real-world usage reflects true value <a class="yt-timestamp" data-t="01:18:02">[01:18:02]</a> <a class="yt-timestamp" data-t="01:19:07">[01:19:07]</a>.

### Context Windows and [[Compound AI systems and their development | Retrieval Augmented Generation]] (RAG)
Larger context windows in models are beneficial as they allow more information to be incorporated into the model's answer, especially for questions involving tying many concepts together <a class="yt-timestamp" data-t="01:16:02">[01:16:02]</a>. However, simply stuffing an entire codebase into a context window is not yet effective for complex tasks beyond simple recollection <a class="yt-timestamp" data-t="01:16:21">[01:16:21]</a>. The best application architectures combine larger context windows with tailored [[Retrieval Augmented Generation and its challenges | information retrieval mechanisms]] <a class="yt-timestamp" data-t="01:17:08">[01:17:08]</a>. Sourcegraph is not getting rid of RAG <a class="yt-timestamp" data-t="01:17:19">[01:17:19]</a>.

Sourcegraph's [[Retrieval Augmented Generation and its challenges | RAG]] approach prioritizes simple, effective solutions first. Initially, Cody's context engine largely relied on "classical keyword search" combined with clever chunking strategies, proving highly effective for context quality <a class="yt-timestamp" data-t="00:52:08">[00:52:08]</a> <a class="yt-timestamp" data-t="00:52:49">[00:52:49]</a>. While vector databases and complex embeddings models were explored, they often performed poorly or were noisy compared to keyword search <a class="yt-timestamp" data-t="00:53:28">[00:53:28]</a> <a class="yt-timestamp" data-t="00:53:53">[00:53:53]</a>. The search problem is considered a "meaty" challenge, involving data-driven approaches combined with human judgment for ranking and relevance <a class="yt-timestamp" data-t="00:56:52">[00:56:52]</a>.

### Local Inference Models
A growing trend is the use of local inference models, running on users' local hardware (e.g., via Olama or LM Studio) <a class="yt-timestamp" data-t="00:44:01">[00:44:01]</a>. This is particularly useful for scenarios without network connectivity (like on an airplane) and for addressing privacy and cost concerns <a class="yt-timestamp" data-t="00:44:50">[00:44:50]</a> <a class="yt-timestamp" data-t="00:45:22">[00:45:22]</a>. As GPUs become faster and models more efficient, local inference will reduce latency, which is critical for developers who are highly sensitive to even milliseconds of delay in their workflow <a class="yt-timestamp" data-t="00:46:13">[00:46:13]</a> <a class="yt-timestamp" data-t="00:46:26">[00:46:26]</a>.

## [[Building and scaling AI infrastructure companies | Building and Scaling Sourcegraph's AI Product]]

### Organizational Structure
Sourcegraph's product engineering organization is structured into three main areas <a class="yt-timestamp" data-t="00:36:21">[00:36:21]</a>:
1.  **Model Layer Team**: Focused on fine-tuning models for better code generation in specific use cases (especially for less common programming languages like Rust or Ruby) and defining quantitative benchmarks <a class="yt-timestamp" data-t="00:28:06">[00:28:06]</a> <a class="yt-timestamp" data-t="00:37:22">[00:37:22]</a>.
2.  **Code Search Team**: Works on the core code search engine <a class="yt-timestamp" data-t="00:36:35">[00:36:35]</a>.
3.  **Cody Team**: Focuses on the AI coding assistant <a class="yt-timestamp" data-t="00:36:36">[00:36:36]</a>.

These teams are expected to integrate more over time due to synergies between their respective areas, such as using context APIs from code search to improve Cody, and using AI for better ranking mechanisms in search <a class="yt-timestamp" data-t="00:36:41">[00:36:41]</a>. Cody started with a small team of two people and grew to 5-6, with the client team remaining relatively small (less than 10 people) supported by others improving context fetching <a class="yt-timestamp" data-t="00:37:41">[00:37:41]</a>.

### Product Development Philosophy: "Do the Dumb Thing First"
Sourcegraph's philosophy for [[Building AI startups and the challenges of scaling | building AI products]] is to "do the dumb thing first" <a class="yt-timestamp" data-t="00:25:29">[00:25:29]</a>. This involves starting with the simplest possible solution to establish a baseline and quickly iterate <a class="yt-timestamp" data-t="00:27:22">[00:27:22]</a>. This approach allowed them to achieve high context quality rapidly with keyword search before exploring more complex methods like fine-tuning or specialized embeddings <a class="yt-timestamp" data-t="00:52:08">[00:52:08]</a>. Fine-tuning becomes important when simpler [[Retrieval Augmented Generation and its challenges | RAG]] approaches are no longer sufficient to achieve desired model performance <a class="yt-timestamp" data-t="00:27:51">[00:27:51]</a>.

### Data Curation: "Cody Ignore"
Sourcegraph has a feature called "Cody ignore," which is a file format that tells Cody to disregard certain files in a codebase when generating completions or responses <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>. Initially for sensitive files, it's evolving to allow users and engineering leaders to control which code (e.g., "bad code") is used as context, enabling higher quality outputs and improving overall code quality within an organization <a class="yt-timestamp" data-t="00:29:35">[00:29:35]</a> <a class="yt-timestamp" data-t="00:29:50">[00:29:50]</a>.

### Inference Cost and Pricing
While inference cost is a consideration, Sourcegraph has not prioritized over-optimizing it, believing that costs will significantly decrease over time <a class="yt-timestamp" data-t="00:31:35">[00:31:35]</a>. Their focus remains on adding user value <a class="yt-timestamp" data-t="00:31:47">[00:31:47]</a>. Rate limiters are primarily used to counteract abuse rather than manage legitimate user costs <a class="yt-timestamp" data-t="00:32:15">[00:32:15]</a>.

Sourcegraph employs an "active user per month" pricing model for both code search and Cody <a class="yt-timestamp" data-t="00:33:03">[00:33:03]</a>. This is a variant of seat-based pricing where customers only pay if a user logs in and actively uses the product, aligning incentives with the value seen by the customer <a class="yt-timestamp" data-t="00:33:11">[00:33:11]</a>. While usage-based pricing might be introduced for high-value but expensive features in the future, simplicity is prioritized for now <a class="yt-timestamp" data-t="00:33:53">[00:33:53]</a>. Cody can be used for free or with a Pro tier without adopting Sourcegraph's code search, but connecting it to a Sourcegraph instance enhances its value by providing more context <a class="yt-timestamp" data-t="00:34:25">[00:34:25]</a>.

### Market and Ecosystem Vision
The AI coding market is viewed as a "hot investment area," a stark contrast to the pre-AI era for [[The evolution of AI developer tools and hardware | developer tools]] <a class="yt-timestamp" data-t="01:08:41">[01:08:41]</a> <a class="yt-timestamp" data-t="01:09:05">[01:09:05]</a>. Software creation itself is becoming a significant market, expanding software literacy and putting the power of software creation into more hands <a class="yt-timestamp" data-t="01:09:33">[01:09:33]</a> <a class="yt-timestamp" data-t="01:10:28">[01:10:28]</a>. This implies significant room for diverse applications that cater to different domains and styles of software building <a class="yt-timestamp" data-t="01:10:50">[01:10:50]</a>.

Sourcegraph's goal is to ensure the emerging ecosystem is open and preserves freedom of choice for individual developers and companies regarding models, code hosts, and technology stacks <a class="yt-timestamp" data-t="01:11:06">[01:11:06]</a>. They provide not just end-user applications but also "building blocks" (like the Cody API and custom commands) for other developers to integrate and build upon <a class="yt-timestamp" data-t="01:00:54">[01:00:54]</a> <a class="yt-timestamp" data-t="01:01:10">[01:01:10]</a> <a class="yt-timestamp" data-t="01:01:51">[01:01:51]</a>. This includes working closely with various model vendors, both open and closed source <a class="yt-timestamp" data-t="01:13:30">[01:13:30]</a>.

## The Future of AI in Coding

### Agents and Automation
Sourcegraph is actively experimenting with [[Compound AI systems and their development | systems targeting full automation]] for specific problem sectors <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>. These systems combine existing context providers with an execution loop, aiming for recurring usage <a class="yt-timestamp" data-t="00:58:18">[00:58:18]</a>. Solving these "outer loop" problems also improves "inner loop" cases, as sub-routines (e.g., test generation for verification) are reusable across both <a class="yt-timestamp" data-t="00:58:43">[00:58:43]</a>.

### Key Milestones for AI in Coding
Meaningful milestones for AI in coding would include the ability for fully automated systems to solve classes of problems that are currently impossible in production, such as automatically fixing 80% of simple bugs identified from production logs <a class="yt-timestamp" data-t="01:03:55">[01:03:55]</a> <a class="yt-timestamp" data-t="01:04:25">[01:04:25]</a>. Continued advancements in model quality and controllability will also reduce the need for "hacking around" model limitations <a class="yt-timestamp" data-t="01:04:36">[01:04:36]</a> <a class="yt-timestamp" data-t="01:05:07">[01:05:07]</a>.

### Overhyped vs. Underhyped
*   **Overhyped**: The notion of AGI (Artificial General Intelligence), particularly the "messianic vision" of it solving all problems or causing doom. Simply scaling Transformers is seen as a fundamentally flawed approach to achieving AGI <a class="yt-timestamp" data-t="01:14:12">[01:14:12]</a> <a class="yt-timestamp" data-t="01:14:35">[01:14:35]</a>.
*   **Underhyped**: Building complementary technologies to AI, especially formal specifications and formal languages <a class="yt-timestamp" data-t="01:15:28">[01:15:28]</a>. While AI can process natural language, the precision needed for useful tasks means that programming languages and mathematical notations will remain crucial for describing intentions with precision <a class="yt-timestamp" data-t="01:15:59">[01:15:59]</a> <a class="yt-timestamp" data-t="01:16:10">[01:16:10]</a>.

### Open Source Models
Open-source models are expected to become very widespread, complementing proprietary models <a class="yt-timestamp" data-t="01:29:30">[01:29:30]</a>. The increasing accessibility of key research means that the ability to train high-quality models will become more common <a class="yt-timestamp" data-t="01:20:24">[01:20:24]</a>. Sourcegraph itself uses open-source models like StarCoder as their primary code completion model <a class="yt-timestamp" data-t="01:20:44">[01:20:44]</a>. Advantages of open-source models include the ability to fine-tune them and peer into internal states like attention weights, which is useful at the application level <a class="yt-timestamp" data-t="01:20:50">[01:20:50]</a>.

## Contact Information
To learn more about Cody, visit cody.dev <a class="yt-timestamp" data-t="01:26:24">[01:26:24]</a>. It can be downloaded from the VS Code Marketplace or the JetBrains plugin store <a class="yt-timestamp" data-t="01:26:31">[01:26:31]</a>. For code search, visit sourcegraph.com <a class="yt-timestamp" data-t="01:26:39">[01:26:39]</a>. Users can also join their Discord community for discussions and feedback <a class="yt-timestamp" data-t="01:26:41">[01:26:41]</a>.