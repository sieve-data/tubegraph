---
title: Challenges with early AI models and improvements
videoId: -rsTkYgnNzM
---

From: [[aidotengineer]] <br/> 

The development of AI agents has seen significant [[evolution_and_limitations_of_ai_models | evolution]] from early, rudimentary models to more sophisticated systems. Early challenges primarily stemmed from the limited capabilities of the foundational AI models themselves, necessitating extensive manual engineering to achieve even basic reliability <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## Initial Limitations of LLMs
When working with Large Language Models (LLMs) four years prior to the widespread adoption of ChatGPT, models like GPT-2 presented considerable [[challenges_with_current_ai_implementation | challenges]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>:
*   **Lack of Intelligence:** Early models were "frustratingly stupid" <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   **Small Context Windows:** They had limited memory for information within a single interaction <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   **Poor Reasoning:** Their ability to logically process information and respond intelligently was weak <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   **Need for Scaffolding Code:** To make these models work "somewhat reliably," significant amounts of code had to be written around them <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. An example of such scaffolding was "Jsonformer," a structured extraction library created because models were too "stupid to up with Json" and needed to be forced into desired formats <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

## Evolution of AI Agents and Architectural Shifts
As AI models have grown smarter, the need for extensive scaffolding code has diminished, leading to the deletion of much of that initial engineering effort <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This has revealed patterns for building [[challenges_in_building_reliable_ai_agents | agents]] that [[continuous_improvement_in_ai_systems | scale]] with increasing intelligence <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

A core idea driving this [[advancements_in_ai_model_technology and performance | advancement]] is that "systems that scale with compute beat systems that don't" <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This principle, akin to the "Bit or Lesson," suggests harnessing rare exponential trends, such as the increasing power of AI models, rather than relying on rigid, fixed, or deterministic systems <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

### Case Study: Ramp's CSV Switching Report Agent
Ramp, a finance platform utilizing AI across its product, offers a "switching report" agent designed to parse arbitrary CSV transaction files from various third-party card providers <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. The problem involves converting diverse CSV schemas into a consistent internal format <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

Three approaches to building this system illustrate the shift in AI architecture:

1.  **Manual/Rigid Code Approach:**
    *   Involves manually writing code for the 50 most common third-party vendors <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
    *   This approach is effective but requires manual updates when schemas change <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
    *   It relies entirely on classical compute <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.

2.  **Constrained Agent (Hybrid) Approach:**
    *   Introduces LLMs to classify columns (e.g., date, amount, merchant name) within a classical scripting flow <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
    *   Most compute is classical, with some "fuzzy LLM land" for specific tasks <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
    *   This is a step towards a more general system <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.

3.  **General Agent (LLM-Driven) Approach:**
    *   The LLM is given the entire CSV, a code interpreter (like Pandas), access to the CSV's head and tail, and a verifier/unit test to ensure the output format <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
    *   Initially, running it once may not work, but running it "50 times in parallel" significantly improves its reliability and generalization across different formats <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
    *   This approach uses "10,000 times more compute" than the first but is still cost-effective given the scarcity of engineer time <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
    *   This represents a model where the LLM (fuzzy compute) largely dictates the flow, calling into classical tools when needed <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

The trend observed at Ramp, moving towards the third approach, demonstrates how leveraging the exponential [[continuous_improvement_in_ai_systems | improvements]] made by large AI labs directly benefits companies without much internal effort <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

### The Future: LLM as the Backend
This shift suggests a future where the LLM itself acts as the backend, rather than merely being a tool for code generation <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. In this model, the LLM has access to tools like code interpreters, can make network requests, and interact with databases <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.

An experimental LLM-driven email client exemplifies this vision <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>:
*   When a user logs in, the Gmail token is sent to an LLM <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.
*   The LLM simulates a Gmail client, having access to emails, the user's token, and a code interpreter <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.
*   It then renders the UI (e.g., as Markdown) based on what it deems reasonable for a Gmail homepage <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
*   User interactions, like clicking an email, are fed back to the LLM, which then decides the next page state and appropriate UI (e.g., fetching and displaying the email body) <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.

While such software is currently slow and "barely works" <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>, the exponential [[advancements_in_ai_model_technology_and_performance | trends]] in AI could lead to it becoming common in the future <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. This highlights the ongoing [[challenges_and_innovations_in_ai_engineering | challenges and innovations]] in developing AI agents, including [[challenges_and_insights_in_developing_ai_coding_agents | coding agents]] and [[challenges_in_creating_personal_ai_agents | personal AI agents]].