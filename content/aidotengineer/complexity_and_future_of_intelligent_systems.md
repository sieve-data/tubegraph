---
title: Complexity and future of intelligent systems
videoId: -rsTkYgnNzM
---

From: [[aidotengineer]] <br/> 

The future of software architecture and [[the_future_of_ai_engineering | AI engineering]] is poised for a significant shift, driven by the exponential growth in artificial intelligence capabilities. A core idea influencing this shift is that systems designed to scale with computational power will inherently outperform those that are rigid and fixed in their design <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>.

## Speaker's Background

The speaker, head of AI at Ramp, has been working with Large Language Models (LLMs) for four years <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. His experience dates back to before the widespread awareness spurred by ChatGPT, when he was building what would now be called an [[future_prospects_in_ai_and_agentbased_technologies | AI agent]] company for customer support <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Early models like GPT-2 and GPT-3 were often "frustratingly stupid," with small context windows and poor reasoning abilities, requiring extensive custom code to function somewhat reliably <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. As models became smarter, much of this scaffolding code could be deleted, revealing patterns for building agents that scale with increasing intelligence <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>. The speaker also built Jsonformer, an early structured extraction library, which served as scaffolding for models that were too "stupid" to produce valid JSON outputs <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.

## The Bit or Lesson: Scaling with Compute

The fundamental principle guiding this perspective is that "systems that scale with compute beat systems that don't" <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>. This is because exponential trends, like the growth in AI model intelligence, are rare and offer a "free pass" for rapid improvement <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>.

Historically, in fields like chess, Go, computer vision, and Atari games, attempts to build rigid, deterministic systems by synthesizing human reasoning through extensive hand-written code eventually yielded to general methods that scaled with increased search or computational power <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>. While a fixed amount of compute might favor a rigid, optimized approach, scaling compute invariably leads to the general method winning <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>.

## AI at Ramp: The Switching Report Agent Example

Ramp is a finance platform that leverages AI to automate tasks like expense management, payments, and bookkeeping <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. One specific example is the "switching report" agent, designed to parse arbitrary CSV files from third-party card providers to help users onboard transactions to Ramp <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a>.

Three approaches to architecting this agent illustrate the core idea:

1.  **Deterministic, Manually Coded Approach:** Manually writing code for the 50 most common third-party card vendors. This works but is rigid, requires significant manual effort, and breaks if formats change <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>.
2.  **Constrained Agent (Hybrid Approach):** Introduces LLMs to classify CSV columns (e.g., date, transaction amount, merchant name) and map them to a desired schema <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>. Most of the compute remains "classical," with some "fuzzy LLM land" integration <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>. This is more general but still limited.
3.  **Fuzzy/LLM-Centric Approach:** The most radical approach involves giving the LLM direct access to a code interpreter (e.g., Pandas or Rust-based ones) and the ability to view parts of the CSV <a class="yt-timestamp" data-t="06:59:00">[06:59:00]</a>. The LLM is tasked with producing a CSV in a specific format and is provided with a unit test/verifier <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>. While a single run might not work, running it multiple times in parallel (e.g., 50 times) significantly increases its reliability and generalization across various formats <a class="yt-timestamp" data-t="07:31:00">[07:31:00]</a>. This approach uses vastly more compute (e.g., 10,000 times more) but is still cost-effective (less than a dollar per transaction) compared to the cost of engineer time or failed CSVs <a class="yt-timestamp" data-t="07:43:00">[07:43:00]</a>.

## Generalizing Software Architectures

These three approaches can be generalized to broader software architectures:

*   **Approach 1 (Classical):** Purely classical compute, where code is hand-written and deterministic <a class="yt-timestamp" data-t="08:39:00">[08:39:00]</a>.
*   **Approach 2 (Hybrid/Fuzzy-Called-By-Classical):** Classical programming languages call into "fuzzy" LLM services (e.g., OpenAI APIs) for specific tasks like similarity scoring <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a>. This is common today.
*   **Approach 3 (Fuzzy-Calls-Classical):** The LLM itself decides when to "break into classical land" by writing and executing code (e.g., Python/Pandas) <a class="yt-timestamp" data-t="08:54:00">[08:54:00]</a>. Most of the compute occurs in the "fuzzy" LLM space <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>. Ramp's codebase is increasingly moving towards this architecture <a class="yt-timestamp" data-t="09:58:00">[09:58:00]</a>.

The advantage of Approach 3 is that the "blue arrows" (representing LLM capabilities) improve constantly due to the billions of dollars invested by large labs, effectively enhancing a company's product without internal effort <a class="yt-timestamp" data-t="10:05:00">[10:05:00]</a>. This allows companies to "hitch a ride" on the exponential [[advancements_in_ai_and_future_implications | advancements in AI]] <a class="yt-timestamp" data-t="10:24:00">[10:24:24]</a>.

## The Future: LLM as the Backend

The speaker proposes a radical shift where the LLM itself acts as the backend for web applications <a class="yt-timestamp" data-t="11:40:00">[11:40:00]</a>.

*   **Traditional Web App:** Frontend (JavaScript, HTML, CSS) makes requests to a classical backend, which interacts with a database <a class="yt-timestamp" data-t="10:47:00">[10:47:00]</a>. LLMs might be used for code generation during development, but not at runtime <a class="yt-timestamp" data-t="11:27:00">[11:27:00]</a>.
*   **LLM-as-Backend Model:** The LLM is the execution engine, having access to tools like code interpreters, network request capabilities, and database access <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>. The frontend communicates directly with the LLM, which then renders the UI and handles logic <a class="yt-timestamp" data-t="14:11:00">[14:11:00]</a>.

The speaker demonstrated a mail client built on this principle. When a user logs in, their Gmail token is sent to an LLM <a class="yt-timestamp" data-t="14:03:00">[14:03:00]</a>. The LLM is prompted to simulate a Gmail client, given access to the user's emails and a code interpreter, and then renders the homepage UI in markdown <a class="yt-timestamp" data-t="14:11:00">[14:11:00]</a>. When a user clicks on an email, the LLM is informed of the action and re-renders the page, making further API calls (e.g., to fetch email content) as needed <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a>.

While this kind of software is currently slow and "barely works" <a class="yt-timestamp" data-t="15:34:00">[15:34:00]</a>, the speaker suggests that exponential trends in [[advancements_in_ai_and_future_implications | AI advancements]] could lead to its rapid proliferation in the [[applications_and_future_of_ai_technology | future of AI technology]] <a class="yt-timestamp" data-t="15:56:00">[15:56:00]</a>. This vision implies a future where [[multiagentic_systems_in_ai | multi-agentic systems in AI]] handle not just specific tasks but entire application backends, significantly impacting [[future_of_ai_in_improving_user_experience_and_integrations | user experience and integrations]] through enhanced [[efficiency and smart execution in AI systems | efficiency and smart execution]].