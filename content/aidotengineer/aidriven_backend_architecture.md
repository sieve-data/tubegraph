---
title: AIdriven backend architecture
videoId: -rsTkYgnNzM
---

From: [[aidotengineer]] <br/> 

The speaker, head of AI at Ramp, has been working with Large Language Models (LLMs) for four years, starting before the widespread adoption of tools like ChatGPT <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Initially, the focus was on building an [[agent_frameworks_and_orchestration_layers_in_ai_engineering | AI agent]] company for [[integration_and_architecture_of_ai_customer_support_platforms | customer support]], using early models like GPT-2 <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. These early models were "frustratingly stupid," had small context windows, and lacked smart reasoning, requiring significant code to achieve reliable performance <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. As models improved, much of this supporting code became obsolete, revealing patterns for building scalable [[agent_frameworks_and_orchestration_layers_in_ai_engineering | agents]] that can adapt to increasing intelligence <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. The speaker also built Jsonformer, an early structured extraction library for models that struggled with JSON output <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

The core idea presented is that systems which scale with compute outperform those that don't <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This concept, derived from the "Bit or Lesson" (likely Bit and a half lesson), suggests that if a system can inherently leverage more computation to improve, it will ultimately win <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. Exponential trends are rare, and when encountered, it's beneficial to "hop on and take the free pass" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

Historical examples illustrating this principle include Chess, Go, computer vision, and Atari games <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. While rigid, hand-coded systems might win with a fixed amount of compute by synthesizing human reasoning, scaling out search (i.e., using more compute) with a general method consistently leads to superior performance <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

## AI Integration at Ramp

Ramp is a finance platform that helps businesses manage expenses, payments, procurement, travel, and bookkeeping <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. AI is extensively used across its product to automate routine tasks for finance teams and employees, such as submitting expense reports or booking flights <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This often involves interacting with legacy systems to streamline workflows <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

### Case Study: The Switching Report Agent

A specific example at Ramp is the "switching report" agent, which helps onboard new users by migrating transaction data from third-party card providers <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. The challenge is parsing CSV files with arbitrary schemas into a format Ramp understands <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

Three approaches for architecting this system were explored:

1.  **Manual Code (Rigid System)**:
    *   This approach involved manually writing code for the 50 most common third-party card vendors <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
    *   While functional, it requires manual effort to understand each schema and breaks if vendors change their format <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. This is a purely classical compute approach <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.

2.  **Constrained Agent (Hybrid System)**:
    *   To achieve a more general system, LLMs were introduced into the classical scripting flow <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
    *   An embedding model would classify each column in the incoming CSV (e.g., date, transaction amount, merchant name) before mapping it to a desired schema <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
    *   Most compute remains in classical land, with some "fuzzy" LLM compute for classification <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. This approach involves classical code calling into fuzzy LLM land <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

3.  **Full AI Agent (Fuzzy/Compute-Scalable System)**:
    *   This approach involved giving the raw CSV directly to an LLM with access to a code interpreter (e.g., Python with pandas) <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
    *   The LLM could examine the CSV head/tail and was tasked with producing a specific output format, with a unit test/verifier <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
    *   Initially, this approach failed when run once, but when run 50 times in parallel, it worked very well and generalized across many formats <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
    *   Despite using "10,000 times more compute," the cost (under a dollar per transaction) was negligible compared to the loss from a failed CSV <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
    *   The core idea is that [[roles_and_personas_in_aidriven_organizations | engineer time]] is scarcer than compute <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. In this model, the LLM decides when to execute classical code, with most compute being "fuzzy" <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

## Generalizing AI Backend Architectures

The speaker illustrates three common architecture patterns for backends:

1.  **Pure Classical**: All compute is rigid, deterministic, and coded <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
2.  **Hybrid (Classical-to-Fuzzy)**: Classical programming languages call into "fuzzy" LLM servers for some compute <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
3.  **AI-Driven (Fuzzy-to-Classical)**: The LLM is the orchestrator, and it decides when to break into classical code execution (e.g., using a code interpreter) <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

The speaker argues that Ramp's codebase is increasingly moving towards the third approach because the "blue arrows" (fuzzy LLM compute) will continuously improve without direct effort from internal teams, as major labs invest billions into making models better <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. This allows companies to "hitch a ride" on exponential AI trends <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

## Future Vision: The LLM as the Backend

A more radical future model is proposed where the LLM *is* the backend itself, not just a code generation tool for engineers <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. In this model, the LLM has access to tools like code interpreters, network requests, and databases <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.

As a demonstration, the speaker showcases a mail client built on this principle <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>. When a user logs in, the Gmail token is sent to an LLM, which is instructed to simulate a Gmail client <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>. The LLM has access to emails and a code interpreter and renders the UI (e.g., in Markdown) <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>. When a user clicks on an email, the LLM receives this interaction and decides how to render the next page, potentially making a GET request to fetch the email body <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. The LLM also determines what actions are available, like marking an email unread or deleting it <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.

While this type of software "barely works today" and is slow due to the extensive compute involved <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>, the speaker encourages thinking in this direction due to the potential of exponential AI trends <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. The question remains if more software will adopt this AI-driven backend architecture <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.