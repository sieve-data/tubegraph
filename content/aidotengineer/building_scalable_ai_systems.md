---
title: Building scalable AI systems
videoId: -rsTkYgnNzM
---

From: [[aidotengineer]] <br/> 

Rahul, Head of AI at Ramp, shares insights on [[best_practices_for_building_ai_systems | building AI systems]] that are inherently scalable, drawing from his four years of experience working with large language models (LLMs) [00:00:17]. His background includes attempts to build an [[scaling_ai_agents_in_production | AI agent]] company focusing on customer support, where early LLMs like GPT-2 were "frustratingly stupid" with small context windows and poor reasoning [00:00:36]. This necessitated writing significant code around these models to achieve even partial reliability [00:00:58]. As models became smarter, much of this scaffolding code could be deleted, revealing patterns for [[challenges_and_solutions_in_scaling_ai_agents | building agents]] that [[scaling_ai_agents_in_production | scale]] with increased intelligence [00:01:07]. Rahul also developed Jsonformer, an early structured extraction library, which was another example of scaffolding around less capable models [00:01:40].

## The Core Idea: Scale with Compute

The fundamental principle for [[building_and_scaling_ai_use_cases_for_enterprises | building scalable AI systems]] is that "systems that scale with compute beat systems that don't" [00:02:30]. This concept, derived from "the Bit or Lesson," suggests that systems able to leverage more computation will inherently outperform rigid, fixed, and deterministic systems [00:02:37]. The reasoning is that exponential growth, while rare in the world, should be leveraged when found [00:03:01].

Historical examples demonstrate this:
*   **Chess, Go, Computer Vision, Atari games**: Early efforts involved extensive manual coding, trying to synthesize human reasoning into clever features [00:03:17]. While effective with fixed compute, [[scaling_ai_solutions_in_production | scaling]] out search or general methods consistently wins over rigid approaches when compute is allowed to increase [00:03:45].

## AI Adoption at Ramp

Ramp is a finance platform that helps businesses manage expenses, payments, and bookkeeping [00:03:59]. They extensively use AI to automate mundane tasks for finance teams and employees, such as submitting expense reports and booking travel [00:04:06]. A significant part of their backend work involves interacting with other systems and legacy platforms to streamline employee workflows [00:04:20].

### Case Study: The Switching Report Agent

To illustrate [[scaling_ai_solutions_in_production | scaling AI solutions in production]], Rahul details the evolution of Ramp's "switching report" agent [00:04:29]. This simple agent needs to parse arbitrary CSV files from third-party card providers to help new users onboard transactions to Ramp [00:04:40]. The challenge is to support parsing diverse CSV schemas into a consistent format [00:05:18].

Three approaches were considered for architecting this system:

1.  **Manual Code (Classical Approach)**:
    *   This involved writing manual code for the 50 most common third-party card vendors [00:05:32].
    *   **Pros**: Works reliably for known formats.
    *   **Cons**: Requires significant manual effort to identify schemas and write specific parsers; breaks if external formats change [00:05:41]. This approach is rigid and does not [[building_and_scaling_ai_use_cases_for_enterprises | scale]] well with the variety of incoming data.

2.  **Hybrid Approach (Classical with Fuzzy LLM Calls)**:
    *   Introduced LLMs to make the system more general, reducing the need for extensive manual coding [00:06:01].
    *   Classical scripting logic calls an LLM (e.g., OpenAI or embedding models) to classify CSV columns (e.g., date, transaction amount, merchant name) [00:06:17].
    *   **Pros**: More general than purely manual code; some compute runs in "fuzzy LLM land" [00:06:49].
    *   **Cons**: Still relies heavily on classical code orchestrating the fuzzy parts; may not be as adaptive to entirely novel formats.

3.  **LLM-First Approach (Fuzzy with Classical Tools)**:
    *   This radical approach involves giving the raw CSV directly to an LLM with a code interpreter (e.g., Pandas, Rust-based tools) [00:06:59].
    *   The LLM can inspect the CSV head/tail, write code to transform it, and is provided with a unit test or verifier to ensure the output matches the desired format [00:07:06].
    *   **Initial finding**: Running this once might not work [00:07:28].
    *   **Key insight for [[scaling_ai_solutions_in_production | scaling]]**: Running it 50 times in parallel makes it "very likely that it works really well and generalizes across a ton of different formats" [00:07:31].
    *   **[[cost_and_efficiency_in_deploying_ai_systems | Cost and efficiency]]**: Although this approach uses "10,000 times more compute" than the first, it still costs less than a dollar per transaction [00:07:40]. The true scarcity is engineer time, and a well-working system, even if compute-intensive, is more valuable than a system that fails frequently [00:07:50]. Failed CSV conversions would cost Ramp significantly more than the compute expenditure [00:08:03].

## Generalizing System Architectures

These three approaches generalize into common backend architectures for [[building_and_scaling_ai_use_cases_for_enterprises | building AI systems]]:

1.  **Classical Only**: The entire system is written in classical code, with no AI components [00:08:39].
2.  **Classical Calling LLM**: A regular programming language calls an LLM API (e.g., OpenAI servers) for "fuzzy compute" [00:09:42]. This is common today [00:09:46].
3.  **LLM Calling Classical Tools**: The LLM is the orchestrator, deciding when to "break into classical land" by writing and executing code (e.g., Pandas, Python) when needed [00:09:54]. Most of the compute is "fuzzy" [00:09:58].

Ramp is increasingly moving towards the third approach [00:09:58]. This is because the underlying LLMs (the "blue arrows" in the analogy) are continuously improved by large labs spending billions of dollars [00:10:05]. By maximizing the use of these "blue arrows," a company's product directly benefits from external advancements without significant internal effort [00:10:17]. This is the essence of "hitching a ride" on exponential trends [00:10:28].

## Future Vision: The LLM as the Backend

Rahul proposes an even more radical model: the LLM itself serving as the backend [00:11:38].

*   **Traditional Web App**: A static file server sends HTML, JavaScript, and CSS to the browser. The frontend makes requests to a classical backend, which interacts with databases [00:10:47]. LLMs might assist engineers in *writing* this code, but the deployed system is purely classical compute [00:11:27].
*   **LLM as Backend**: In this model, the LLM *is* the execution engine [00:11:40]. It has access to tools like code interpreters, can make network requests, and interact with databases [00:11:46].

Rahul demonstrated this with a conceptual email client [00:12:00]. When logging into this client, the Gmail token is sent to an LLM, which is instructed to simulate a Gmail client [00:14:03]. The LLM has access to emails and a code interpreter and renders the UI (e.g., in Markdown) based on what it deems reasonable for a Gmail homepage [00:14:16]. When a user clicks on an email, the LLM receives this interaction and decides how to render the next page, potentially making a `GET` request for the email's body [00:14:45]. The LLM can even decide to offer features like marking an email as unread or deleting it [00:15:17].

While this kind of software is currently slow and "barely works" [00:15:34], Rahul emphasizes that exponential trends suggest it "might just take off" in the future [00:15:57]. This pushes the audience to consider how software and backends might evolve [00:16:01].