---
title: Challenges in productizing AI capabilities
videoId: Awvj4yLYafo
---

From: [[redpointai]] <br/> 

The rapid evolution of AI models, particularly in the realm of agents, presents significant opportunities but also notable [[challenges_in_ai_product_development | challenges in productizing AI capabilities]] and integrating them effectively into existing systems and new applications <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. While the models are advancing quickly, the ability to leverage their full potential in real-world products remains a key hurdle <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>.

## Current Landscape and Vision for Agents

Initially, AI interactions were confined to specific platforms like ChatGPT <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. The vision is for agents to become deeply embedded across the web, automating tasks within browsers or day-to-day work activities, reducing the need for manual clicking and form filling <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. The focus for platforms is to disperse these agentic capabilities everywhere <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. Developers, with their domain-specific knowledge, are expected to create diverse, verticalized applications <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

Agents are moving beyond single-turn interactions to more complex "chain of thought" processes, where models access information, reconsider stances, and even open multiple web pages in parallel <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. This tool-calling in the reasoning process is a significant shift <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. Future evolution will see seamless embedding of tool calling between the internet, private data, and private agents <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

Companies are advised to build AI agents internally first to solve real problems before exposing them to the public internet <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. Multi-agent architectures are already popular for complex business problems like customer support automation, where different agents handle specific tasks (e.g., refunds, billing) and make decisions (e.g., escalating to a human) <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. The Agents SDK aims to facilitate this <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

## Key Challenges in Productizing

### 1. Agent Workflow Design and Tool Management

*   **Evolution of Agent Workflows**: In 2024, agentic products typically followed clearly defined workflows with fewer than a dozen tools <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. In 2025, the shift is towards models performing chain-of-thought reasoning, capable of calling multiple tools, backtracking, and trying alternative paths, moving away from deterministic workflows <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
*   **Scaling Tools**: A major unlock will be removing the constraint on the number of tools an agent can access, allowing them to figure out which of hundreds of tools to call <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
*   **Increased Runtime**: Models need to operate for longer durations, from minutes to hours or even days, to yield more powerful results <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
*   **Guardrails vs. Flexibility**: While earlier models required strict guardrails, newer models allow for more flexibility, with the ultimate goal being to provide models with a vast array of tools and let them figure out the task <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

### 2. Evaluation and Fine-tuning

*   **Task and Grader Creation**: A significant [[challenges_in_ai_product_development | challenge in productizing AI capabilities]] is creating robust tasks and graders for reinforcement fine-tuning to ensure agents find the correct tool-calling paths for unique domain-specific problems <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. This process is currently challenging and takes a lot of iteration <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>.
*   **Domain Specificity**: While foundational building blocks for graders are provided (e.g., cross-referencing model output with ground truth like medical textbooks), creating off-the-shelf grading and evaluation tools for highly specific domains is difficult <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Beyond Simple Grading**: The biggest question is what can *actually* be graded <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. For example, being a lawyer is more than just passing the bar exam <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>. The ideal is to train a model to "think" like a legal scholar or medical doctor <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

### 3. Developer Experience and Infrastructure

*   **Ease of Use vs. Customizability**: A tension exists between providing easy-to-use, out-of-the-box solutions and offering ultimate customizability <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>. The strategy is to offer simple defaults that just work, with "knobs" (parameters) available for deeper customization as needed <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>.
*   **Orchestration Complexity**: [[challenges_in_deploying_ai_models_effectively | Orchestrating agents and tools]] is the most important thing for AI startups, as models are far ahead of current application utilization <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>. This involves meticulous prompt engineering, tracing, and using eval sets to prevent degradation <a class="yt-timestamp" data-t="00:20:46">[00:20:46]</a>.
*   **Debugging Multi-Agent Systems**: Splitting tasks among multiple agents makes debugging workflows easier, as changes to individual agents have a smaller "blast radius" <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.
*   **AI Infrastructure Landscape**: While core model providers offer out-of-the-box tools, there is still significant opportunity for [[challenges_of_building_ai_infrastructure_companies | AI infrastructure companies]] building low-level, infinitely flexible APIs <a class="yt-timestamp" data-t="00:27:58">[00:27:58]</a>. Vertical-specific AI infrastructure (e.g., VMs for coding startups) and LLM Ops companies (for managing prompts, billing, usage) are also emerging <a class="yt-timestamp" data-t="00:28:23">[00:28:23]</a>.
*   **Computer Use Models**: The "computer use" model, which automates tasks on legacy applications without APIs or performs complex web research (e.g., Google Maps Street View for climate tech startups), is very promising but still early <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. A key [[challenges_in_deploying_ai_models_effectively | challenge in deploying AI models effectively]] is securely and reliably deploying and observing these virtual machines within enterprise infrastructure <a class="yt-timestamp" data-t="00:30:05">[00:30:05]</a>. There is also significant fragmentation in environments (e.g., browser vs. iPhone screenshots, different OS flavors) <a class="yt-timestamp" data-t="00:31:18">[00:31:18]</a>.

## Addressing the Challenges

*   **Simplifying the "Flywheel"**: The process from evaluation to production and fine-tuning needs to be much simpler <a class="yt-timestamp" data-t="00:35:01">[00:35:01]</a>. It needs to be about ten times easier than it is today <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.
*   **Making AI Accessible**: It is crucial to make it easier for developers and non-ML experts to build powerful things with models <a class="yt-timestamp" data-t="00:34:24">[00:34:24]</a>.
*   **Focus on Internal Automation**: Enterprises should start by exploring frontier models and computer use models, identifying internal manual workflows that can be automated using multi-agent architectures <a class="yt-timestamp" data-t="00:36:41">[00:36:41]</a>. The biggest productivity gains come from automating employees' least favorite day-to-day tasks <a class="yt-timestamp" data-t="00:38:15">[00:38:15]</a>.

## Outlook

*   **Underhyped/Overhyped Agents**: Agents are both overhyped (due to hype cycles) and underhyped (due to their potential to automate complex manual tasks) <a class="yt-timestamp" data-t="00:38:53">[00:38:53]</a>.
*   **Differentiators for Application Builders**: Long-term differentiation for application builders will come from a combination of deep model knowledge, strong domain expertise, and the "special sauce" for orchestrating models, tools, and data to unlock the models' full AGI capabilities <a class="yt-timestamp" data-t="00:40:42">[00:40:42]</a>.
*   **Underexplored Applications**: Scientific research and robotics are noted as underexplored applications <a class="yt-timestamp" data-t="00:41:41">[00:41:41]</a>. A key is finding the right interfaces for fields like academia <a class="yt-timestamp" data-t="00:42:07">[00:42:07]</a>.
*   **Accelerated Model Progress**: Model progress is expected to accelerate further, driven by feedback loops where models themselves help improve data and refinement <a class="yt-timestamp" data-t="00:33:33">[00:33:33]</a>.