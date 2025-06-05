---
title: Multiagentic systems in AI
videoId: VTJHR7rQ2KI
---

From: [[aidotengineer]] <br/> 

True AI is built incrementally, with each step verified and refined through collaborative effort, rather than relying on a single, massive leap of faith <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Manish Sanwal, Director of AI at News Corp, focuses on AI reasoning, explainability, and automation, aiming to build AI that is structured and self-correcting using Layered Chain of Thought with [[multiagent_systems_and_their_applications | multi-agentic systems]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## What are Multi-Agentic Systems?

In simple terms, [[multiagent_systems_and_their_applications | multi-agentic systems]] are a collection of specialized [[components_of_ai_agents | AI agents]] that work together to tackle complex tasks <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Each [[components_of_ai_agents | agent]] is designed to handle a specific part of an overall problem <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. This approach contrasts with relying on massive, monolithic systems <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

A self-driving car serves as an example: instead of one massive system, it operates as a team of specialized [[components_of_ai_agents | agents]] <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. One [[components_of_ai_agents | agent]] might detect pedestrians, another reads traffic signals, and a third checks for the best route <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This harmonious collaboration makes the entire system more robust and efficient <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### Advantages of Multi-Agentic Systems

The modular approach of [[multiagent_systems_and_their_applications | multi-agentic systems]] offers several concrete advantages <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>:
*   **Specialization** <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>: Each [[components_of_ai_agents | agent]] can be finely tuned for a specific task, leading to better accuracy and performance <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Flexibility and Scalability** <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>: Since the system is distributed, individual [[components_of_ai_agents | agents]] can be updated or improved without overhauling the entire system <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   **Fault Tolerance** <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>: If one [[components_of_ai_agents | agent]] encounters an issue, others can often compensate, ensuring overall system reliability <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
*   **Robustness and Effectiveness** <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>: By integrating these well-coordinated [[components_of_ai_agents | agents]], a system becomes inherently more robust and effective <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

## Chain of Thought (CoT) Reasoning

When [[multiagent_systems_and_their_applications | multi-agentic systems]] are combined with Chain of Thought reasoning, each [[components_of_ai_agents | agent]] not only performs its task but also explains its decision-making process step-by-step <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. This combination enhances both transparency and resiliency in AI systems <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

Chain of Thought is a method that guides AI to think through a problem step-by-step, rather than simply guessing answers <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Traditionally, large language models (LLMs) often jump directly to a conclusion without revealing their reasoning <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. By asking the model to walk through its reasoning process, outlining every step, it demonstrates how it processes information and exposes its path to a conclusion <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

### Benefits of Traditional CoT
*   **Transparency**: Provides insight into each stage of the reasoning process, aiding in understanding how the model tracks the problem <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   **Opportunity for fine-tuning and debugging**: Mistakes in intermediate steps can be spotted and corrected by adjusting prompts or processes before the final answer is provided <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

CoT transforms AI's internal reasoning into a verifiable sequence, making the process more interpretable <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

### Limitations of Traditional CoT
Despite its benefits, Chain of Thought has several limitations <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>:
*   **Prompt Sensitivity**: The process is highly sensitive to prompt phrasing; slight changes can lead to vastly different outputs, complicating reproducibility and reliability <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   **No Real-time Feedback**: There is no built-in mechanism to verify or correct mistakes during the process, meaning no error correction opportunity while the chain is being produced <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   **Error Propagation**: If an early inference is flawed, it can cause a cascade of errors compromising the integrity of the entire process <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Incomplete Conclusions**: When faced with interdependent factors, CoT can sometimes miss critical connections, leading to oversimplified or incomplete conclusions <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

## Layered Chain of Thought (Layered CoT) Prompting

Layered CoT prompting is designed to overcome the limitations of standard Chain of Thought methods by integrating a verification step at every stage of the reasoning process <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

It works in two steps <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>:
1.  **Generation of Initial Thought**: An [[components_of_ai_agents | AI agent]] produces an initial thought or hypothesis from the input prompt, serving as the starting point for further reasoning <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
2.  **Verification Against Knowledge Base**: The generated thought is immediately verified by cross-referencing it against a structured knowledge base or external database <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. This verification can involve fact-checking algorithms, consistency checks through contextual reasoning, or an ensemble model <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. This crucial step ensures only accurate and reliable information influences subsequent reasoning <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

This iterative process repeatedly generates new thoughts, verifies them, and then proceeds <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. The chain of reasoning is built step-by-step, with each link confirmed before the next is added <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

### Benefits of Layered CoT
The additional verification step offers significant benefits <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>:
*   **Self-Correction**: Verification at each step allows the system to catch and correct errors early, preventing mistakes from propagating through the reasoning chain <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
*   **Robustness Against Prompt Variability**: Independent verification at each step makes the overall process less sensitive to small changes in input, leading to higher reproducibility <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
*   **Enhanced Accuracy and Trustworthiness**: Each verified step ensures the final output is built on accurate and validated information, resulting in more trustworthy conclusions <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
*   **Increased Transparency**: Breaking down reasoning into discrete, verifiable steps makes the AI's thought process much more transparent, allowing for easier auditing and interpretation <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

Layered CoT transforms AI reasoning into a robust, iterative framework where every step is checked for accuracy, mitigating weaknesses of traditional CoT and leading to more reliable, reproducible, and interpretable AI models <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

## Conclusion

Layered Chain of Thought prompting overcomes the limitations of traditional CoT by adding a verification step after each generated thought <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>. This method can be seamlessly implemented using existing Large Language Model (LLM) tools and integrates perfectly within [[multiagent_systems_and_their_applications | multi-agentic systems]], where each specialized [[components_of_ai_agents | agent]] contributes to a robust overall system <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.

Overall, Layered CoT enhances both accuracy and reproducibility by ensuring every inference is validated before proceeding <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. The future of AI focuses on creating systems that are structured, explainable, and reliable, prioritizing transparency, self-correction, collaboration, and validation to lay the foundation for truly trustworthy AI <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>. A paper on Layered Chain of Thought prompting is available for further reading <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.