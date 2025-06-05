---
title: Scaffolding AI agents for scalability
videoId: -rsTkYgnNzM
---

From: [[aidotengineer]] <br/> 

The concept of [[scaling_ai_agents_in_production | scaffolding AI agents for scalability]] focuses on architecting systems that improve with increased computational power, rather than relying on rigid, pre-coded logic <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>. This approach leverages the exponential improvements in large language models (LLMs) to create more general and adaptable AI solutions <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>.

## Speaker Background and Early Challenges <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>

The speaker, head of AI at Ramp, has been working with LLMs for four years, starting before the widespread adoption of models like ChatGPT <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. In the early days, attempts to [[building_effective_ai_agents | build AI agents]] for customer support using models like GPT-2 and BT were frustrating due to their limited intelligence, small context windows, and poor reasoning abilities <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This necessitated writing extensive "scaffolding" code around these models to achieve even somewhat reliable performance <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. As models became smarter, much of this supporting code could be deleted, revealing patterns for [[building_effective_ai_agents | building agents]] that scale with increasing intelligence <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>. The speaker also developed Jsonformer, an early structured extraction library, which was another form of scaffolding to force models to output JSON when they were not inherently capable <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.

## The Bit or Lesson: Scaling with Compute <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>

The core idea is that systems designed to scale with compute consistently outperform those that are rigid and fixed <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>. This is because exponential trends, like the growth in LLM intelligence, are rare and offer a "free pass" for improvement without direct engineering effort <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>.

Historically, in fields like chess, Go, computer vision, and Atari games, extensive human-engineered systems with clever abstractions and synthesized human reasoning were initially dominant <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>. However, when compute could be scaled, general methods, particularly those involving extensive search, consistently won out <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>.

## AI Agents at Ramp: The Switching Report Example <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a>

Ramp, a finance platform, uses AI to automate various financial tasks <a class="yt-timestamp" data-t="04:06:00">[04:06:00]</a>. One example is the "switching report" agent, designed to parse arbitrary CSV transaction schemas from third-party card providers <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a>. The goal is to onboard users by helping them transfer existing transactions onto the Ramp platform <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.

Three approaches to building this agent were discussed:

1.  **Manual Code (Rigid System)**:
    *   Manually writing code for the 50 most common third-party card vendors <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>.
    *   This approach is simple and works, but requires significant upfront work and maintenance if formats change <a class="yt-timestamp" data-t="05:41:00">[05:41:00]</a>.
    *   Depicted as purely "classical compute" <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>.

2.  **Constrained Agent (Classical Calls Fuzzy)**:
    *   Introduces LLMs to classify CSV columns (e.g., date, transaction amount, merchant name) and map them to a desired schema <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>.
    *   Most compute still runs in classical code, with some fuzzy LLM compute for classification <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>.
    *   This is depicted as a "constrained agent" where classical code calls into the fuzzy LLM <a class="yt-timestamp" data-t="08:44:00">[08:44:00]</a>.

3.  **LLM-Driven Agent (Fuzzy Calls Classical)**:
    *   The LLM is given direct access to the CSV, a code interpreter (e.g., Python with Pandas), and the ability to view parts of the CSV (head, tail) <a class="yt-timestamp" data-t="06:59:00">[06:59:00]</a>.
    *   The LLM is tasked with producing a CSV in a specific format and is provided with unit tests/verifiers to check its output <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>.
    *   While running once might not work, running this approach 50 times in parallel significantly increases success and generalizes across many formats <a class="yt-timestamp" data-t="07:28:00">[07:28:00]</a>.
    *   Despite using "10,000 times more compute," the cost is likely less than a dollar, which is negligible compared to the value of a successful transaction switch or the cost of engineer time <a class="yt-timestamp" data-t="07:40:00">[07:40:00]</a>.
    *   This approach flips the control: the LLM decides when to execute classical code <a class="yt-timestamp" data-t="08:52:00">[08:52:00]</a>. Most of the compute is "fuzzy" (within the LLM) <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>.
    *   Ramp is increasingly moving towards this third approach because the "blue arrows" (LLM capabilities) will continue to improve without internal effort, directly benefiting the company <a class="yt-timestamp" data-t="09:58:00">[09:58:00]</a>.

## The Future of Backend Systems: LLM as the Backend <a class="yt-timestamp" data-t="10:39:00">[10:39:00]</a>

Traditional web applications involve a frontend making requests to a backend, which then interacts with a database <a class="yt-timestamp" data-t="10:47:00">[10:47:00]</a>. LLMs might assist engineers in writing this code, but the deployed system relies on classical compute <a class="yt-timestamp" data-t="11:20:00">[11:20:00]</a>.

A proposed future model suggests the backend *is* the LLM itself <a class="yt-timestamp" data-t="11:38:00">[11:38:00]</a>. This LLM has access to tools like a code interpreter, can make network requests, and interact with a database <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>.

An example of this is a mail client where the LLM simulates the Gmail client, renders UI in markdown, and processes user interactions <a class="yt-timestamp" data-t="12:00:00">[12:00:00]</a>. When a user clicks an email, the LLM receives this information and decides how to render the next page or perform actions like deleting an email <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a>. While currently slow, this demonstrates the potential for software to evolve dramatically due to exponential trends in LLM capabilities <a class="yt-timestamp" data-t="15:34:00">[15:34:00]</a>.