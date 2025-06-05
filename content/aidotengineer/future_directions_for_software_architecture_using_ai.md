---
title: Future directions for software architecture using AI
videoId: -rsTkYgnNzM
---

From: [[aidotengineer]] <br/> 

The central idea in future software architecture, particularly with the advent of AI, is that systems designed to scale with compute will outperform those that do not <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This principle suggests that rigid, fixed, and deterministic systems are less advantageous than those that can leverage increased computational power <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

## The "Bit or Lesson" Principle

The "Bit or Lesson" emphasizes that exponentials are rare, and when encountered, they should be embraced to gain a significant advantage <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Historically, in domains like chess, Go, computer vision, and Atari games, human-engineered systems with clever software and synthesized human reasoning could win if compute was fixed <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. However, when the amount of search or compute is allowed to scale, the more general, less rigid methods consistently win <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

## Evolution of AI Agents at Ramp

The speaker, having worked on large language models (LLMs) for four years, initially focused on building what are now called [[future_opportunities_and_transformation_with_ai_agents | AI agents]] for customer support, aiming to make chatbots smarter <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Early models like GPT-2 were frustratingly limited by small context windows and poor reasoning capabilities, requiring extensive code to achieve even reliable, albeit minimal, functionality <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. As models became more intelligent, much of this scaffolding code could be deleted, revealing patterns for building [[future_opportunities_and_transformation_with_ai_agents | agents]] that scale with intelligence <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. An example of this is the JSONFormer library, built to force models to output valid JSON due to their early limitations <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

Ramp, a finance platform, extensively uses AI to automate tasks for finance teams and employees, such as expense reports, flight bookings, and reimbursements <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. This involves interacting with existing and legacy systems <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

### Case Study: The Switching Report Agent

A "switching report" agent at Ramp processes CSV files from third-party card providers, which have arbitrary schemas, to help users onboard transactions to Ramp <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. The problem is parsing these diverse CSV formats into a standardized internal format <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

1.  **Version 1: Manual/Deterministic Approach (No AI)**
    This approach involved manually writing code for the 50 most common third-party card vendors <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. While functional, it requires significant manual effort to understand schemas and maintain the code if formats change <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

2.  **Version 2: Hybrid Approach (Classical with AI Components)**
    To create a more general system, LLMs were introduced <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. This version involved using classical scripting with calls to LLMs (e.g., OpenAI) or embedding models for semantic similarity <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. Each CSV column would be classified (e.g., date, transaction amount, merchant name) using the LLM, then mapped to a desired schema <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. In this architecture, most compute still ran in classical code, with some fuzzy LLM compute <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. This approach represents [[enhancing_existing_systems_with_ai_capabilities | enhancing existing systems with AI capabilities]].

3.  **Version 3: AI-First Approach (Mostly Fuzzy with Classical Tools)**
    This approach directly gives the CSV to the LLM, treating it as a code interpreter <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. The LLM has access to tools like Pandas and Python packages, can inspect CSV data, and is tasked with returning a CSV in a specific format with a provided unit test/verifier <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. While a single run might not work, running it 50 times in parallel drastically increases success rates and generalization across diverse formats <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

    Though this version uses potentially 10,000 times more compute than the first approach, the cost (less than a dollar per transaction) is negligible compared to the value of successful transactions and the scarcity of engineer time <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. This highlights the strategic advantage of leveraging scalable compute even at higher raw cost, as it frees up valuable human resources.

## Generalizing Software Architectures

These three approaches illustrate a general pattern for software architecture:
*   **Approach 1 (Classical):** No AI; code is entirely classical and deterministic <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. This reflects how almost all systems were built historically <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
*   **Approach 2 (Classical calls AI):** Regular programming languages call into AI services (e.g., OpenAI) for "fuzzy" compute <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. This is common today as companies integrate AI <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **Approach 3 (AI calls Classical):** The LLM is primary, deciding when to utilize classical tools (like writing Python/Pandas code) to interact with classical environments <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. Much of the compute is "fuzzy" <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

Ramp is increasingly adopting the third approach because it leverages the constant improvement of LLMs by major labs <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. This means a codebase utilizing more "fuzzy" compute automatically benefits from external advancements in AI without additional internal effort, aligning with the power of exponential trends <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

## Future of Web Application Architecture

A radical proposition for future web application architecture is to have the LLM *be* the backend, rather than merely a code generation tool <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

### Traditional Web App Model
In a traditional web app (e.g., Gmail), a static file server sends HTML, CSS, and JavaScript to the browser <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. The frontend then makes requests to a backend, which hits a database to retrieve data <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. Any LLM use in this model is typically limited to code generation during development <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.

### AI-as-Backend Model
The proposed model shifts the backend entirely to an LLM <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. This LLM has direct access to tools like code interpreters, can make network requests, and interact with databases <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.

**Demo: LLM-powered Gmail Client**
A proof-of-concept email client demonstrates this architecture <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.
*   Upon logging in, the Gmail token is sent to an LLM <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.
*   The LLM is prompted to simulate a Gmail client, having access to emails, the user's token, and a code interpreter <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
*   It renders the UI (in this case, Markdown) for the Gmail homepage, displaying emails <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.
*   When a user clicks on an email, the LLM is informed of the click and the email ID <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.
*   The LLM then decides how to render the page, potentially making a GET request to fetch the email body <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.
*   The LLM also determines other appropriate UI features, such as "mark as unread" or "delete email" options <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.

While currently slow and experimental, this type of software, which barely works today, may become viable in the future due to exponential trends in AI capabilities <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>. The speaker encourages exploring this direction for future software architecture <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.