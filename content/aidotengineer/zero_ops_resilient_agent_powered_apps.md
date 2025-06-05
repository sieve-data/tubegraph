---
title: Zero ops resilient agent powered apps
videoId: UcW_s4BmuD0
---

From: [[aidotengineer]] <br/> 

Full stack AI engineering in a serverless environment involves deploying "zero ops resilient agent-powered user-ready apps" <a class="yt-timestamp" data-t="00:00:23">00:00:23</a>. The goal for AI engineers is to get agentic workflows into the hands of users <a class="yt-timestamp" data-t="00:00:28">00:00:28</a>.

## Core Components of AI Engineering Infrastructure

A modern AI engineering infrastructure typically consists of:
*   A client application <a class="yt-timestamp" data-t="00:00:50">00:00:50</a>
*   An agent framework <a class="yt-timestamp" data-t="00:00:52">00:00:52</a>
*   An orchestration layer <a class="yt-timestamp" data-t="00:00:53">00:00:53</a>
*   A serverless cloud environment <a class="yt-timestamp" data-t="00:00:54">00:00:54</a>

There are numerous options for each component:
*   **Client App Frameworks**: Remix, Astro, Vue, Svelte, Next.js, and others <a class="yt-timestamp" data-t="00:01:09">00:01:09</a>.
*   **Agent Frameworks**: LangChain, Vercel's AI SDK, Flowise agents, OpenAI's Agents SDK <a class="yt-timestamp" data-t="00:01:21">00:01:21</a>.
*   **Orchestration Layers**: Temporal, AWS Step Functions, Langsmith, Ingest <a class="yt-timestamp" data-t="00:01:32">00:01:32</a>.
*   **Serverless Environments**: AWS (Lambda API Gateway + Bedrock), Google Vertex, Azure AI Studio, Vercel <a class="yt-timestamp" data-t="00:01:43">00:01:43</a>.

With potentially millions of combinations, choosing the right stack that works together effectively can be challenging <a class="yt-timestamp" data-t="00:02:00">00:02:00</a>, and LLMs often struggle to provide accurate reference code <a class="yt-timestamp" data-t="00:02:18">00:02:18</a>.

## Recommended Full Stack AI Engineering Stack

A preferred combination for building full stack AI applications includes:

### Client App: Next.js
Next.js is chosen for its built-in streaming, first-class server actions, file-based and nested routing, and deep integration with Vercel hosting <a class="yt-timestamp" data-t="00:02:58">00:02:58</a>.

### Agent Framework: OpenAI's Agents SDK
The OpenAI Agents SDK offers native tool calling, one-shot and [[Multiagent Systems and Their Applications | multi-agent]] calls, built-in tracing and eval hooks for observability, and strong backing from OpenAI <a class="yt-timestamp" data-t="00:03:20">00:03:20</a>. It also allows for model interchangeability, preventing vendor lock-in <a class="yt-timestamp" data-t="00:03:37">00:03:37</a>.

### Orchestration Layer: Ingest
Ingest is an event-driven orchestration layer that eliminates the need to manage JSON state machine documents <a class="yt-timestamp" data-t="00:03:53">00:03:53</a>. It operates on-demand, removing concerns about server warm-up times, and includes automatic retry, step-level observability, and a one-click integration with Vercel <a class="yt-timestamp" data-t="00:04:01">00:04:01</a>.

### Serverless Environment: Vercel
Vercel is the preferred serverless environment due to:
*   **Preview Deployments**: Provides preview deployments with every push, integrating continuous deployment into the workflow <a class="yt-timestamp" data-t="00:04:21">00:04:21</a>.
*   **Edge Network**: Offers a strong edge network and automatic CDNs <a class="yt-timestamp" data-t="00:04:50">00:04:50</a>.
*   **Integrated Databases**: Supports various integrated database options like PostgreSQL, Redis, and blob storage <a class="yt-timestamp" data-t="00:04:55">00:04:55</a>.
*   **Next.js Alignment**: As the company behind Next.js, Vercel provides strong alignment for developing the ideal cloud platform for Next.js infrastructure <a class="yt-timestamp" data-t="00:05:05">00:05:05</a>.
*   **Ecosystem**: Part of a strong ecosystem of tools found in Next.js Forge <a class="yt-timestamp" data-t="00:05:22">00:05:22</a>.

This combination of tools allows for seamless integration of [[AI agents in DevOps | AI workflows]] directly into client applications <a class="yt-timestamp" data-t="00:05:32">00:05:32</a>.

## Architecture Overview

The architecture for such an application involves:
1.  **User Interaction**: A user connects to the Next.js application <a class="yt-timestamp" data-t="00:06:02">00:06:02</a>.
2.  **Workflow Trigger**: The Next.js app checks a database for cached results; if new work is needed, it triggers a new workflow by sending an event to the Ingest service <a class="yt-timestamp" data-t="00:06:05">00:06:05</a>.
3.  **Orchestration**: Ingest, as the orchestration layer, manages connections to Python serverless functions where [[Stateful AI Agents | AI agents]] run <a class="yt-timestamp" data-t="00:06:17">00:06:17</a>.
4.  **Agent Execution**: The OpenAI Agents SDK (currently Python-only) executes within these Python functions, which Vercel automatically hosts <a class="yt-timestamp" data-t="00:06:26">00:06:26</a>. These functions handle inference by interacting with OpenAI <a class="yt-timestamp" data-t="00:06:41">00:06:41</a>.
5.  **Results and Caching**: Results are returned to the orchestration layer, which then informs the client app that the work is done, caching results in the database as needed <a class="yt-timestamp" data-t="00:06:50">00:06:50</a>.

## Example Application: AI-Powered Newsletter Generator

An example application built with this stack demonstrates how [[AI agents in DevOps | AI agents]] can create a newsletter <a class="yt-timestamp" data-t="00:07:08">00:07:08</a>.

### Key Features and Benefits
*   **Serverless Scalability**: Supports [[scaling_ai_agents_in_production | serverless scalability]] for [[longrunning_agents_and_failure_resilience | long-running jobs]], preventing agent tasks from crashing or exceeding cloud function time limits <a class="yt-timestamp" data-t="00:07:34">00:07:34</a>.
*   **Cost Optimization**: Allows for paying only for actual usage, avoiding costs for idle servers <a class="yt-timestamp" data-t="00:07:48">00:07:48</a>.
*   **Local Developer Experience**: Provides a smooth local development experience <a class="yt-timestamp" data-t="00:07:56">00:07:56</a>.
*   **Type Safety**: Achieves full type safety with Pydantic in Python and TypeScript across Next.js <a class="yt-timestamp" data-t="00:08:03">00:08:03</a>.

### Local Setup and Execution
To run the example app locally, three terminals are needed: one for Python agents, one for Next.js, and one for the Ingest dev server <a class="yt-timestamp" data-t="00:08:13">00:08:13</a>.

The application allows users to enter comma-separated topics, and it generates a newsletter based on the intersection of these topics <a class="yt-timestamp" data-t="00:09:11">00:09:11</a>. For instance, generating a newsletter about "AI engineering in Seattle" <a class="yt-timestamp" data-t="00:09:22">00:09:22</a>. The app polls a Vercel blob storage for results <a class="yt-timestamp" data-t="00:09:40">00:09:40</a>. The Ingest server shows the task broken down into individual steps, each capable of scaling to the full length allowed for Vercel cloud functions <a class="yt-timestamp" data-t="00:10:11">00:10:11</a>.

### Code Structure
The project structure includes:
*   **Ingest Endpoint**: An Ingest endpoint provides detailed observability of step-by-step processes directly from the app <a class="yt-timestamp" data-t="00:11:26">00:11:26</a>.
*   **Newsletter API Endpoints**: These endpoints are called by Ingest, which in turn invokes the Python agents <a class="yt-timestamp" data-t="00:11:47">00:11:47</a>.
*   **Top-Level API Directory**: Vercel automatically serves each file in this directory as an independent cloud function (e.g., Python functions) <a class="yt-timestamp" data-t="00:11:57">00:11:57</a>.
*   **Ingest Folder**: Located within the source code, this folder defines workflows triggered by specific events <a class="yt-timestamp" data-t="00:12:10">00:12:10</a>.

### Agent Implementation
The [[AI agents in DevOps | AI agents]] are built using FastAPI, providing a quick way to assemble them <a class="yt-timestamp" data-t="00:12:32">00:12:32</a>. For example, one agent handles research, and another handles formatting <a class="yt-timestamp" data-t="00:12:37">00:12:37</a>. Vercel can deploy these independent Python files with a single line of code, without requiring a `vercel.json` config file <a class="yt-timestamp" data-t="00:12:49">00:12:49</a>.

### Ingest Workflow Structure
Ingest workflows are defined to keep each step clear and isolated <a class="yt-timestamp" data-t="00:13:20">00:13:20</a>. Each `step.run` invocation executes in order, passing results to subsequent steps <a class="yt-timestamp" data-t="00:14:16">00:14:16</a>. Code outside `step.run` may be executed multiple times <a class="yt-timestamp" data-t="00:14:19">00:14:19</a>.

Example workflow steps:
1.  Call the research agent <a class="yt-timestamp" data-t="00:13:54">00:13:54</a>.
2.  Format the newsletter with another agent <a class="yt-timestamp" data-t="00:13:56">00:13:56</a>.
3.  Save the results to blob storage for the front end to access <a class="yt-timestamp" data-t="00:13:58">00:13:58</a>.

## Deployment to Vercel

The entire Next.js repository can be deployed to Vercel <a class="yt-timestamp" data-t="00:15:23">00:15:23</a>. Vercel provides full build logs, showing how the `api` agents folder is deployed as a Python function, running on Python 3.12 <a class="yt-timestamp" data-t="00:15:58">00:15:58</a>. Deployment is as simple as running the `vercel` CLI command from the terminal <a class="yt-timestamp" data-t="00:16:24">00:16:24</a>.

### Environment Variables
To run this project, the following environment variables are needed:
*   An OpenAI API key <a class="yt-timestamp" data-t="00:16:50">00:16:50</a>
*   A Vercel blob storage token <a class="yt-timestamp" data-t="00:16:54">00:16:54</a>

> [!NOTE]
> Environment variables can be pulled down from production and run locally using the Vercel CLI <a class="yt-timestamp" data-t="00:16:44">00:16:44</a>.

## Conclusion

This combination of Next.js, OpenAI's Agents SDK, Ingest, and Vercel provides:
*   Scalability expected from a serverless environment <a class="yt-timestamp" data-t="00:15:29">00:15:29</a>.
*   Resilience from a robust orchestration layer <a class="yt-timestamp" data-t="00:15:33">00:15:33</a>.
*   Agentic power from OpenAI's Agents SDK <a class="yt-timestamp" data-t="00:15:38">00:15:38</a>.

The example code is open-source and available on GitHub for exploration and contributions <a class="yt-timestamp" data-t="00:17:14">00:17:14</a>.