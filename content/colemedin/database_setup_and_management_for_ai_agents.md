---
title: Database setup and management for AI agents
videoId: FGeB9w1ZeHE
---

From: [[colemedin]] <br/> 

When [[building_ai_agents | building AI agents]], setting up a database is a crucial step after prototyping your agent <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

## Why a Database is Needed

A database is essential for an AI agent to store various types of information <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>:
*   **Chat History**: To maintain conversation context <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
*   **Knowledge Base (RAG)**: For Retrieval Augmented Generation (RAG) purposes, allowing the agent to access and leverage external information <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
*   **Backend Information Storage**: Any other structured information required for the agent's operations <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

## Recommended Database Solution

A highly recommended solution for managing databases for AI agents is **Supabase** <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

> [!INFO] Supabase Features
> *   **Cost-Effective**: It can be used for free <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
> *   **Underlying Technology**: Uses PostgreSQL under the hood <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
> *   **Power and Versatility**: It is a powerful tool suitable for various agent needs <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
> *   **RAG Capabilities**: Supports RAG implementations <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

This platform is consistently used for agents, including those hosted on the Automator Live Agent Studio <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

When setting up your database, the key is to keep it very simple, focusing on establishing your tables and knowledge base <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.