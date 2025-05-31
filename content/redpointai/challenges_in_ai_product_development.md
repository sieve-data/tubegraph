---
title: Challenges in AI product development
videoId: XsANqI-WnjY
---

From: [[redpointai]] <br/> 

Developing AI products, particularly in the realm of coding, presents a unique set of [[challenges_in_productizing_ai_capabilities | challenges and opportunities]]. While the field is rapidly evolving, product developers face hurdles ranging from model performance and evaluation to user experience and infrastructure costs <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>.

## Current State of AI Coding Tools

Today's AI coding tools primarily serve as "inner loop accelerants" <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. This refers to the frequent, iterative process a developer goes through daily: figuring out how to do something, writing the code, testing it, and repeating <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. Tools like inline code completion and code-aware chat are in heavy use <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

### Hype vs. Reality in AI Coding <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>

There's a significant difference between flashy demos and what works consistently in day-to-day usage <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>:

*   **Consistent Work**: Inner loop accelerants, such as code completion or chat for common functions, work reliably <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. These are especially useful for tasks that are "not interesting" or have been written before <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
*   **On the Horizon / Working Sometimes**: More advanced automation, like multi-step, bot-driven development, is still on the horizon <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. Even tools like Devin, which show promise, still require a human in the loop for watching and checking <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **What Doesn't Work Well Yet**: Fully automated systems for resolving complex issues in production are virtually non-existent <a class="yt-timestamp" data-t="01:04:01">[01:04:01]</a>.

## Key Challenges in AI Product Development

### 1. Moving from Inner Loop Acceleration to Full Automation

Achieving full automation, where an AI bot drives development with human oversight, requires significant advancements <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. The core challenge is enabling the AI to reliably create a pull request that satisfies a high-level goal <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. This requires:

*   **Robust Context Fetching**: The ability to pull in relevant information from the code base (e.g., surrounding code structure, existing patterns) is crucial <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. This is a limiting factor in how much "juice" can be squeezed out of each step <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
*   **Effective Feedback Loops and Execution Environments**: AI needs a way to try things, observe results, learn from mistakes, and incorporate that history into subsequent attempts <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. This necessitates virtual execution environments for testing code changes <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. Shortening the number of cycles to get to a correct answer is key due to cost and time <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.

### 2. Model Performance and Limitations

*   **Model Quality and Context Integration**: Older models like GPT-3.5 struggled significantly with integrating search results and additional code contexts compared to newer models like GPT-4 and Claude 3 <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.
*   **Long Context Windows**: While helpful for tying many concepts together, simply stuffing an entire codebase into a context window does not guarantee good performance <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>. Models still struggle with attending to multiple things or composing them effectively, performing better at simple recollection tasks <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a>.
*   **Language-Specific Performance**: LLM performance varies across programming languages. Python, JavaScript, and other well-represented languages perform better due to their presence in training data, while languages like Rust and Ruby often perform less well <a class="yt-timestamp" data-t="00:28:20">[00:28:20]</a>. This necessitates fine-tuning models for specific languages <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>.

### 3. User Experience and Adoption

*   **Different User Needs**: Junior developers often find inline completions useful as a pedagogical tool, providing a starting point <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>. Senior engineers, however, can find completions disruptive if not smart enough, preferring to guide the AI more directly through chat interfaces <a class="yt-timestamp" data-t="00:22:02">[00:22:02]</a>.
*   **"Bad Code" as Context**: A significant challenge is that not all code in an existing codebase is "good code" <a class="yt-timestamp" data-t="00:29:47">[00:29:47]</a>. Product designers must consider how to allow users and engineering leaders to control which code context is used for generation, potentially excluding low-quality or sensitive files <a class="yt-timestamp" data-t="00:30:04">[00:30:04]</a>.

### 4. Evaluation and Prioritization

*   **Benchmarks vs. Product Metrics**: While internal benchmarks are run, product usage metrics (e.g., acceptance rate for completions, engagement for chat) are considered the most authoritative <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>. A model might top a benchmark list but not provide real value to users <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.
*   **The "Dumb Thing First" Philosophy**: It's crucial to prioritize simple, "brain dead" solutions first to establish a baseline and iterate quickly, rather than immediately pursuing complex, "fancy" approaches that might not perform as well or be harder to debug <a class="yt-timestamp" data-t="00:25:29">[00:25:29]</a>. This applies particularly to Retrieval Augmented Generation (RAG) engines, where classical keyword search can be highly effective initially <a class="yt-timestamp" data-t="00:52:08">[00:52:08]</a>.

### 5. Cost and Infrastructure

*   **Inference Costs**: While not the primary focus, inference costs can add up with heavy usage, especially for larger models <a class="yt-timestamp" data-t="00:31:17">[00:31:17]</a>. Rate limiters are employed to counteract abuse rather than legitimate high usage <a class="yt-timestamp" data-t="00:32:15">[00:32:15]</a>. The expectation is that costs will decrease over time <a class="yt-timestamp" data-t="00:31:35">[00:31:35]</a>.
*   **Pricing Models**: Determining an effective pricing model for AI products is an ongoing challenge <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a>. An active user per month model, where customers only pay if a user logs in and uses the product, aligns incentives with value <a class="yt-timestamp" data-t="00:33:03">[00:33:03]</a>. Usage-based pricing might be introduced for particularly expensive but valuable features <a class="yt-timestamp" data-t="00:33:53">[00:33:53]</a>.

### 6. Architectural and Organizational Challenges

*   **Context Engine Complexity**: Building a robust context engine involves deep challenges in finding models good at integrating contexts and effective prompt engineering to ensure models use context as intended <a class="yt-timestamp" data-t="01:17:23">[01:17:23]</a>.
*   **Search Strategies for RAG**: RAG is a generalization of the search problem <a class="yt-timestamp" data-t="00:51:09">[00:51:09]</a>. While tempting to use sophisticated methods like embeddings and vector databases, naive approaches can be noisy and less effective than keyword search <a class="yt-timestamp" data-t="00:53:31">[00:53:31]</a>. The challenge is in "not forgetting anything important and bumping up the things that are important to the top quickly" <a class="yt-timestamp" data-t="00:51:24">[00:51:24]</a>.
*   **Organizational Structure**: Organizing teams to effectively build AI products is an iterative process. Sourcegraph, for example, has a distinct team for the model layer (fine-tuning, benchmarks) and separate product engineering teams for core code search and AI coding assistant (Cody), with a long-term goal of integration due to synergies <a class="yt-timestamp" data-t="00:36:21">[00:36:21]</a>.

## Future Outlook

The landscape of AI product development is rapidly changing. Key aspirations include:

*   **Full Automation Milestones**: Reaching points where specific classes of problems, such as simple bug fixes identified from production logs, can be automatically fixed by AI <a class="yt-timestamp" data-t="01:03:55">[01:03:55]</a>.
*   **The Rise of Local Inference**: Running models locally on user hardware addresses concerns about privacy, cost, and network connectivity (e.g., coding on an airplane) <a class="yt-timestamp" data-t="00:45:10">[00:45:10]</a>. As GPUs become faster and inference times decrease, local processing could become the preferred method for latency-sensitive "inner loop" activities <a class="yt-timestamp" data-t="00:45:50">[00:45:50]</a>.
*   **Open Ecosystems**: Ensuring the emerging AI ecosystem remains open, preserving freedom of choice for developers regarding models, code hosts, and technology stacks <a class="yt-timestamp" data-t="01:11:08">[01:11:08]</a>. This means providing building blocks and APIs for others to create AI-enabled tools, rather than forcing everyone onto a proprietary platform <a class="yt-timestamp" data-t="01:00:54">[01:00:54]</a>.
*   **Formal Languages and AI**: AI is complementary to formal specifications and programming languages. While natural language is imprecise, formal languages provide the precision needed for useful tasks, similar to how mathematics evolved from natural language to precise notation <a class="yt-timestamp" data-t="01:15:36">[01:15:36]</a>.