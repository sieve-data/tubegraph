---
title: Introduction and application of AI in business platforms
videoId: -rsTkYgnNzM
---

From: [[aidotengineer]] <br/> 

The application of Artificial Intelligence (AI), particularly Large Language Models (LLMs), is transforming business operations by enabling systems that can scale with computational power. This approach contrasts with traditional, rigid software development, offering significant advantages in adaptability and efficiency <a class="yt-timestamp" data-t="02:30:16">[02:30:16]</a>.

## Evolution of AI Agents and LLMs

The speaker, head of AI at Ramp, has been working with LLMs for four years, noting that the field significantly accelerated with the release of ChatGPT <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>. Early attempts at building AI agents for customer support faced challenges with LLMs like GPT-2, which were "frustratingly stupid," had small context windows, and lacked strong reasoning capabilities <a class="yt-timestamp" data-t="00:48:07">[00:48:07]</a>. Developers had to write extensive code to make these models work reliably <a class="yt-timestamp" data-t="00:58:12">[00:58:12]</a>.

As models became smarter, much of this "scaffolding" code could be deleted, revealing patterns for building agents that scale with increased intelligence <a class="yt-timestamp" data-t="01:06:05">[01:06:05]</a>. An example of such scaffolding was "Jsonformer," a structured extraction library developed to force earlier, less capable models to output JSON in a desired format <a class="yt-timestamp" data-t="01:40:07">[01:40:07]</a>.

## The "Bit or Lesson": Scaling with Compute

The core idea presented is that "systems that scale with compute beat systems that don't" <a class="yt-timestamp" data-t="02:30:16">[02:30:16]</a>. This means building systems that inherently improve with more computational resources <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>. Exponential trends, like the improvement in AI models, are rare and should be leveraged <a class="yt-timestamp" data-t="03:01:08">[03:01:08]</a>.

Historically, in domains like chess, Go, computer vision, and Atari games, people initially built "rigid systems" by writing clever, highly abstracted software that tried to synthesize human reasoning <a class="yt-timestamp" data-t="03:17:09">[03:17:09]</a>. While this approach might win with a fixed amount of compute, scaling the amount of search or computational power (the "general method") consistently leads to superior performance <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.

## AI in Ramp's Business Platform

Ramp is a finance platform that helps businesses manage expenses, payments, procurement, travel, and bookkeeping <a class="yt-timestamp" data-t="03:59:03">[03:59:03]</a>. The platform extensively uses AI to automate "boring stuff" for finance teams and employees, such as submitting expense reports, booking flights, and handling reimbursements <a class="yt-timestamp" data-t="04:06:04">[04:06:04]</a>. Much of Ramp's backend work involves [[integration_of_ai_in_business_operations | interacting with other systems]] and assisting employees more quickly <a class="yt-timestamp" data-t="04:18:00">[04:18:00]</a>.

### Case Study: The "Switching Report" Agent

A key [[integrating_ai_into_business_operations | application of AI]] at Ramp is the "switching report" agent <a class="yt-timestamp" data-t="04:37:07">[04:37:07]</a>. This simple agent's task is to process CSV files of arbitrary format, typically from third-party card providers, and convert them into a standardized format for Ramp's platform <a class="yt-timestamp" data-t="04:40:07">[04:40:07]</a>. This allows Ramp to help businesses migrate their transactions smoothly onto the platform <a class="yt-timestamp" data-t="04:53:07">[04:53:07]</a>.

Three approaches for developing this agent illustrate the concept of scaling with compute:

1.  **Approach 1: Manual Code (Rigid System)**
    *   This involved manually writing code for the 50 most common third-party card vendors <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>.
    *   While functional, it required significant effort to understand each vendor's schema and was brittle, breaking if a vendor changed their format <a class="yt-timestamp" data-t="05:41:00">[05:41:00]</a>.

2.  **Approach 2: Hybrid LLM + Classical Scripting (Constrained Agent)**
    *   This approach introduced LLMs to classify columns (e.g., date, transaction amount, merchant name) within the incoming CSVs <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>.
    *   Most of the compute still ran in traditional scripting, with a portion running in "fuzzy LLM land" for classification <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>. This resulted in a more general system <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>.

3.  **Approach 3: LLM-Driven Execution (Fuzzy Land Centric)**
    *   This radical approach involved giving the LLM the entire CSV and instructing it to produce a CSV in a specific target format <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>.
    *   The LLM was provided with a code interpreter (e.g., Python with Pandas), allowing it to inspect the CSV data and write its own code for transformation <a class="yt-timestamp" data-t="07:03:00">[07:03:00]</a>.
    *   It also had a unit test or verifier to confirm if its output was correct <a class="yt-timestamp" data-t="07:23:00">[07:23:00]</a>.
    *   Initially, a single run of this approach didn't work well <a class="yt-timestamp" data-t="07:28:00">[07:28:00]</a>. However, running it 50 times in parallel made it "very likely that it works really well and generalizes across a ton of different formats" <a class="yt-timestamp" data-t="07:31:00">[07:31:00]</a>.
    *   This approach required significantly more compute (estimated 10,000 times more) than the first <a class="yt-timestamp" data-t="07:40:00">[07:40:00]</a>. However, the speaker argued that engineer time is the truly scarce resource <a class="yt-timestamp" data-t="07:50:00">[07:50:00]</a>. The cost of compute (less than a dollar per transaction) is negligible compared to the cost of failed transactions or engineer time spent on manual coding <a class="yt-timestamp" data-t="07:58:00">[07:58:00]</a>. This illustrates a system that scales with compute <a class="yt-timestamp" data-t="07:56:00">[07:56:00]</a>.

## Generalizing AI Agent Architectures

The three approaches for the switching report agent can be generalized into broader patterns for [[implementing_ai_in_enterprises | enterprise AI implementations]]:

*   **Type 1: Classical Compute Only**
    *   Software relies entirely on manually written code, with no AI involvement <a class="yt-timestamp" data-t="08:39:00">[08:39:00]</a>.

*   **Type 2: Classical Calling Fuzzy LLM (Constrained Agent)**
    *   Regular programming languages call into LLM services (e.g., [[openais_approach_to_ai_deployment_and_enterprise_integration | OpenAI APIs]]) for specific, "fuzzy" computations like classification or embeddings <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>. This is common today <a class="yt-timestamp" data-t="09:42:00">[09:42:00]</a>.

*   **Type 3: Fuzzy LLM Calling Classical Tools (LLM as Backend)**
    *   The LLM is the central orchestrator, with most of the compute being "fuzzy" <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>. The LLM decides when to call into classical tools (e.g., writing Python code to interact with a database or perform complex logic) <a class="yt-timestamp" data-t="08:54:00">[08:54:00]</a>.
    *   Ramp is increasingly moving towards this third approach because the continuous improvements from major AI labs directly enhance the company's codebase without significant internal effort <a class="yt-timestamp" data-t="09:58:00">[09:58:00]</a>. This exemplifies [[transformative_role_of_ai_in_business_operations | leveraging exponential trends]] <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>.

## The Future of Software: LLM as the Backend

The speaker proposed a radical future model where the LLM *is* the backend of a web application <a class="yt-timestamp" data-t="11:38:00">[11:38:00]</a>.

### Traditional Web App Model

In a traditional web application (e.g., Gmail), a static file server sends JavaScript, HTML, and CSS to the browser <a class="yt-timestamp" data-t="10:47:00">[10:47:00]</a>. The frontend renders the UI, and user interactions trigger requests to a backend, which then interacts with a database <a class="yt-timestamp" data-t="11:06:00">[11:06:00]</a>. While AI tools might be used during code generation, the deployed application runs on classical compute <a class="yt-timestamp" data-t="11:20:00">[11:20:00]</a>.

### Proposed Model: LLM as the Backend

In the proposed model, the LLM itself acts as the backend <a class="yt-timestamp" data-t="11:40:00">[11:40:00]</a>. This LLM has access to tools like a code interpreter and can make network requests or access databases <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>.

### Demo: LLM-Powered Mail Client

A demonstration of a mail client built on this principle was provided <a class="yt-timestamp" data-t="12:00:00">[12:00:00]</a>. When logging in, the Gmail token is sent to an LLM, initiating a chat session <a class="yt-timestamp" data-t="14:03:00">[14:03:00]</a>. The LLM is instructed to simulate a Gmail client, given access to emails and a code interpreter, and renders the UI (in markdown format) <a class="yt-timestamp" data-t="14:07:00">[14:07:00]</a>.

User interactions (e.g., clicking on an email) are sent back to the LLM, which then uses this information to render the next page state, similar to a web framework <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a>. The LLM determines the appropriate UI and available actions (e.g., mark as unread, delete) <a class="yt-timestamp" data-t="15:10:00">[15:10:00]</a>.

Although the demo was "very slow" <a class="yt-timestamp" data-t="15:34:00">[15:34:00]</a> and such software "barely works today," the speaker emphasized the potential impact of exponential trends, suggesting that this type of [[applications_and_future_of_ai_technology | AI-driven software]] could become prevalent in the future <a class="yt-timestamp" data-t="15:54:00">[15:54:00]</a>. This vision suggests a future where [[ai_in_enterprise_applications | complex enterprise applications]] could be orchestrated primarily by intelligent models.