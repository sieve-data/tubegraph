---
title: Full stack AI engineering in serverless environments
videoId: UcW_s4BmuD0
---

From: [[aidotengineer]] <br/> 

Full stack [[challenges_and_innovations_in_ai_engineering | AI engineering]] in a serverless environment involves deploying "zero ops" resilient, agent-powered, user-ready applications [00:00:23]. The goal for [[challenges_and_innovations_in_ai_engineering | AI engineers]] is to get agentic workflows into the hands of users [00:00:28].

## Core Components of a Modern Full Stack AI Infrastructure

A typical full stack AI setup in a serverless environment requires several interconnected components:
*   **Client App** [00:00:50]
*   **[[agent_frameworks_and_orchestration_layers_in_ai_engineering | Agent Framework]]** [00:00:52]
*   **[[agent_frameworks_and_orchestration_layers_in_ai_engineering | Orchestration Layer]]** [00:00:53]
*   **Serverless Cloud Environment** [00:00:54]

The challenge for [[challenges_and_innovations_in_ai_engineering | AI engineers]] is piecing together the right components from the myriad of available options to ensure they function correctly [00:02:12]. Traditional resources like LLMs or original documentation may not provide complete reference code or clear integration pathways [00:02:18].

## Recommended Full Stack AI Engineering Stack

Brook Riio, a technology partner with thrive.com, shares his preferred combination for running [[scaling_ai_solutions_in_production | production AI engineering workloads]] in a full stack and serverless environment [00:00:12].

### Client Application: Next.js and Vercel

The preferred choice for the client application is Next.js, particularly Next.js 5, due to several features:
*   Built-in streaming [00:02:58]
*   First-class server actions [00:03:00]
*   File-based and nested routing [00:03:01]
*   Deep integration with Vercel hosting [00:03:09]

### Agent Framework: OpenAI's Agents SDK

For [[agent_frameworks_and_orchestration_layers_in_ai_engineering | agent frameworks]], OpenAI's Agents SDK is recommended because it offers:
*   Native tool calling [00:03:20]
*   One-shot and multi-agent calls [00:03:22]
*   Built-in tracing and evaluation hooks for observability [00:03:26]
*   Strong backing and support from OpenAI [00:03:33]
*   Ability to interchange models, preventing vendor lock-in despite being an OpenAI open-source framework [00:03:37]

### Orchestration Layer: Ingest

Ingest is the chosen [[agent_frameworks_and_orchestration_layers_in_ai_engineering | orchestration layer]] because of its event-driven nature and operational benefits:
*   Uses events to trigger workflows, eliminating the need to manage JSON state machines [00:03:53]
*   Operates entirely on demand, removing concerns about server warm-up times [00:04:01]
*   Includes automatic retry mechanisms [00:04:06]
*   Provides step-level observability, allowing users to see what's happening step by step and identify errors [00:04:09]
*   Offers a one-click integration with Vercel [00:04:12]

### Serverless Environment: Vercel

Vercel is the ideal serverless platform for this stack due to:
*   **Preview Deployments**: Provides preview deployments with every code push, integrating continuous deployment seamlessly into the workflow [00:04:21]. This allows teams to review changes on preview branches before merging to main [00:04:33].
*   **Strong Edge Network and CDNs**: Features a robust edge network and automatic Content Delivery Networks (CDNs) [00:04:50].
*   **Integrated Database Options**: Supports various integrated database options, including PostgreSQL, Redis, and blob storage [00:04:55].
*   **Alignment with Next.js**: As the company behind Next.js, Vercel has a strong alignment in developing the ideal cloud platform for the Next.js infrastructure [00:05:04].
*   **Rich Ecosystem**: Offers a comprehensive ecosystem of tools for client-based applications [00:05:24].

This specific combination of tools is proven to work together effectively for integrating AI workflows directly into client applications [00:05:37].

## Architectural Overview

The architecture for this full stack AI setup functions as follows:
1.  A user connects to the Next.js application [00:06:00].
2.  The Next.js app checks a database (e.g., for cached results) [00:06:05].
3.  If new work is needed, a workflow is triggered by sending an event to Ingest [00:06:11].
4.  Ingest, as the [[agent_frameworks_and_orchestration_layers_in_ai_engineering | orchestration layer]], manages the connection to Python serverless functions where AI agents run [00:06:17].
5.  OpenAI Agents SDK is currently Python-only, but Vercel automatically hosts these Python functions when deployed [00:06:26].
6.  These Python functions handle inference, communicate with OpenAI, and perform the necessary work [00:06:41].
7.  Results are returned to the [[agent_frameworks_and_orchestration_layers_in_ai_engineering | orchestration layer]], which can then inform the client app that the work is done and cache results in the database as needed [00:06:50].

## Example Application: AI Newsletter Generator

To demonstrate this architecture, an example application was built that uses AI agents to create a newsletter [00:07:08]. The code for this application is open-source and available on GitHub [00:07:20].

### Key Features and Benefits

The example app highlights several advantages of this stack:
*   **Serverless Scalability**: Designed for [[building_scalable_ai_systems | serverless scalability]], supporting long-running jobs without crashing or exceeding cloud function time limits [00:07:34].
*   **Cost Efficiency**: Allows for paying only for actual usage, avoiding costs for idle servers [00:07:48].
*   **Local Developer Experience**: All tools work together to provide a seamless local development experience [00:07:56].
*   **Full Type Safety**: Achieved with Pydantic in Python and TypeScript across Next.js [00:08:03].

### Local Development Setup

To run the example application locally, three terminals are needed:
1.  One for Python agents [00:08:14]
2.  One for Next.js [00:08:16]
3.  One for the Ingest development server [00:08:18]

The Ingest server provides a specific development environment to manage orchestration [00:08:23].

### Application Workflow

When a user enters topics for a newsletter:
1.  The Next.js app triggers a process to generate the newsletter, polling a database (Vercel's blob storage in the example) for results [00:09:11].
2.  The Ingest server breaks down the task into individual, scalable steps (e.g., agent calls for research, formatting) [00:10:11]. Each step can scale up to the maximum duration allowed by Vercel for cloud functions [00:10:18].
3.  Once completed, the results are found in the database and presented as a formatted newsletter on the frontend [00:10:36].

### Code Structure and Deployment

The project structure includes:
*   **Ingest Endpoint**: An endpoint that the [[agent_frameworks_and_orchestration_layers_in_ai_engineering | orchestration layer]] connects to for detailed observability of step-by-step processes [00:11:26].
*   **Newsletter API Endpoints**: These are called by Ingest and in turn invoke the Python agents [00:11:47].
*   **Top-level API Directory**: Vercel serves each file within this directory as its own independent cloud function [00:11:57].
*   **Ingest Folder**: Contains workflow definitions, with each workflow triggered by a specific event [00:12:10]. Workflows clearly define each step (e.g., calling research agent, formatting, saving to blob storage) using `step.run` functions [00:13:31]. Code outside of `step.run` may execute multiple times [00:14:19].

AI agents are powered by FastAPI, a fast and easy way to create API endpoints for agents [00:12:32]. Vercel can automatically deploy Python functions within the top-level API directory without requiring a `vercel.json` config file [00:12:49].

### Environment Variables

To run the project, two environment variables are necessary:
*   An OpenAI API key [00:16:50]
*   A Vercel blob storage token [00:16:54]

These variables can be managed and pulled down from production environments using the Vercel CLI [00:16:41].

This combination provides [[building_scalable_ai_systems | scalability]] from the serverless environment, resilience from the robust [[agent_frameworks_and_orchestration_layers_in_ai_engineering | orchestration layer]], and agentic power from OpenAI's SDK [00:15:29].