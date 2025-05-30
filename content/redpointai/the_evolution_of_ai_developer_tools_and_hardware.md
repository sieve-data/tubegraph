---
title: The evolution of AI developer tools and hardware
videoId: nkOB4LDNo7I
---

From: [[redpointai]] <br/> 

Mike Schroepfer, former CTO at Facebook (now Meta) for nine years and founder of venture capital firm Gigascale, discusses the significant evolution of [[the_role_of_ai_in_the_future_of_coding_and_developer_ecosystems | AI developer tools]] and hardware. His insights span from the foundational changes in programming languages to the complexities of managing large-scale AI infrastructure and the strategic decisions around building proprietary hardware <a class="yt-timestamp" data-t="00:59:02">[00:59:02]</a>.

## From Low-Level to AI-Generated Code

The progression of programming has consistently moved towards higher levels of abstraction, making developers more productive while "throwing away compute cycles" <a class="yt-timestamp" data-t="00:59:59">[00:59:59]</a>. This historical trend is summarized as:
*   **Assembly Language** to **C**: Stanford stopped requiring assembly programming for CS majors, allowing the use of higher-level languages <a class="yt-timestamp" data-t="00:59:35">[00:59:35]</a>.
*   **C** to **Python/Rust/JavaScript**: These high-level languages further increase developer productivity <a class="yt-timestamp" data-t="00:59:55">[00:59:55]</a>.
*   **Current Shift to AI Systems**: The next logical step involves [[the_impact_of_ai_on_software_development_and_programming_jobs | AI systems writing code]] <a class="yt-timestamp" data-t="01:00:03">[01:00:03]</a>. While these AI systems are often "less power efficient per cycle," they continue the trend of accelerating human productivity <a class="yt-timestamp" data-t="01:00:09">[01:00:09]</a>.

Schroepfer likens this progression to the invention of the backhoe for digging, making tasks significantly faster <a class="yt-timestamp" data-t="00:40:08">[00:40:08]</a>. [[the_future_of_software_engineering_with_ai | AI is seen as an extension of this trend]], enabling expression of thoughts at increasingly higher levels of abstraction <a class="yt-timestamp" data-t="00:40:27">[00:40:27]</a>.

## Evolution of AI Development Frameworks

Meta (then Facebook) played a pivotal role in the [[ai_infrastructure_and_developer_tools | evolution of AI developer tools]] through its Facebook AI Research (FAIR) lab, founded in 2013 <a class="yt-timestamp" data-t="01:37:37">[01:37:37]</a>. Key contributions include:
*   **PyTorch**: FAIR developed PyTorch, which has become the "dominant framework" for [[building_a_successful_ai_product_for_developers | AI development]] <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.
*   **Open-Sourcing Models**: Meta's decision to open-source models like Llama was not common but is now being recognized for its power in accelerating progress <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>, fostering decentralized innovation and collaboration <a class="yt-timestamp" data-t="01:28:26">[01:28:26]</a>. This approach ensures access to the best technology at zero cost for companies <a class="yt-timestamp" data-t="01:16:19">[01:16:19]</a>.

## Current Gaps and System Design Challenges

While model architectures are largely standardized (e.g., Transformers), the challenges in [[ai_infrastructure_and_developer_tools | AI developer tooling]] have shifted to broader system design and management <a class="yt-timestamp" data-t="01:59:26">[01:59:26]</a>.
*   **Beyond Architecture**: Focus is now on managing data sets for pre-training, post-training (RLHF, RL), and the entire system around the models <a class="yt-timestamp" data-t="01:59:37">[01:59:37]</a>.
*   **Large-Scale Cluster Management**: The move from individual GPUs under a desk to requiring large clusters (e.g., 25,000 nodes) necessitates sophisticated software for managing downtime, restarts, and checkpoints <a class="yt-timestamp" data-t="02:00:17">[02:00:17]</a>.
*   **Shift from Desktop to "Supercloud"**: AI development now resembles physics, requiring massive computing infrastructure rather than just personal machines <a class="yt-timestamp" data-t="02:10:08">[02:10:08]</a>.

## Hardware Development and Supply Chain Decisions

Hyperscalers are increasingly building their own hardware due to the massive energy and compute demands <a class="yt-timestamp" data-t="00:40:02">[00:40:02]</a>.
*   **Meta's Hardware Journey**: Facebook initially leased data centers and bought off-the-shelf servers <a class="yt-timestamp" data-t="02:21:20">[02:21:20]</a>. As they scaled, inefficiencies led them to build their own data centers from the ground up and design their own servers <a class="yt-timestamp" data-t="02:21:35">[02:21:35]</a>. Today, most equipment in a Meta data center is custom-designed <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.
*   **Build vs. Buy**: A critical strategic decision for companies is determining which parts of the supply chain to own <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>. While Nvidia makes "unbelievably great Tech" and has a deep moat with their R&D, the significant capex cost of GPUs leads companies to consider specialized hardware for cheaper, better, faster operations <a class="yt-timestamp" data-t="02:22:15">[02:22:15]</a>.
*   **Specialization Challenge**: It's difficult to beat general-purpose chips like Nvidia's GPUs. The advantage lies in specializing hardware for specific algorithms, which can yield 10x performance per watt or price advantages <a class="yt-timestamp" data-t="02:32:08">[02:32:08]</a>. However, this carries the risk of "guessing the algorithm right" – a specialized chip can become worthless if the dominant algorithms change before its release <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>.
*   **Long-Term Commitments**: The physical world's long lead times for building data centers and ordering equipment create an "impedance mismatch" with the fast-moving pace of AI development <a class="yt-timestamp" data-t="02:07:07">[02:07:07]</a>. Schroepfer advises that "underpredicting" capacity is more regrettable than overpredicting, as unused compute can be repurposed <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.

## The Future of AI Development

The future of [[role and expectations of software developers in the context of AI advancements | AI development]] will see continued progress in models <a class="yt-timestamp" data-t="02:42:10">[02:42:10]</a>. Key trends include:
*   **Reasoning Models**: The focus is shifting from pure scaling of LLMs to treating them as inputs for reasoning models through post-training and reinforcement learning <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>. The question remains how much "legs" this approach has across different domains <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.
*   **Memory and Context**: Advancements like Gemini 2's million-token context window are impressive, but the need for associative long-term memory, akin to humans, remains a significant challenge for LLMs <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.
*   **Verifiability of Outputs**: [[challenges_and_advancements_in_ai_model_development | AI models excel in domains where outputs are easily verifiable]], such as math or coding (does it compile?) <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>. However, domains like video, where grounding the model is harder, present more significant challenges <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>.
*   **AI as a "Tutor"**: AI tools like "Deep Research" can act as "really fast tutors," explaining complex topics and summarizing large amounts of information, accelerating learning and understanding for users <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>.

## The CTO of the Future

The [[role_and_expectations_of_software_developers_in_the_context_of_ai_advancements | role of a CTO in the age of AI]] will be "more similar than people think" <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>. While AI tools accelerate technical execution, the fundamental challenges remain:
*   **Problem Identification**: Identifying "what problems are we trying to solve" and "what's important to go after" <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.
*   **Team Organization**: Organizing "groups of smart humans" to address these problems <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>.
*   **Prioritization**: The ability to maintain a "priority queue" in one's head, consistently focusing on the "highest leverage most important thing" <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>.
*   **Smaller Teams**: AI tools are enabling companies to achieve significant results with smaller teams, potentially leading to faster growth and smaller organizational sizes <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>.