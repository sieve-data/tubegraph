---
title: Selfhosting Supabase with Docker
videoId: U1_0swrCiAY
---

From: [[colemedin]] <br/> 

Supabase is an [[Supabase as an opensource platform | open-source platform]] that serves as a popular database for [[Using Supabase for AI agents | AI agents]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. It is built on PostgreSQL, allowing it to manage conversation history and state for agents <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. With the PG Vector extension, Supabase can also function as a [[Using Supabase as a vector database | vector database]] for RAG (Retrieval Augmented Generation) <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Beyond its database capabilities, Supabase includes features such as [[Supabase features like authentication and object storage | authentication]] and [[Supabase features like authentication and object storage | object storage]] right out of the box <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Why Self-Host Supabase?

Given its utility, many users have requested its inclusion in [[building_a_local_ai_package_with_supabase | local AI packages]] <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Since Supabase is entirely [[Supabase as an opensource platform | open-source]] and provides instructions for [[running_supabase_locally_with_docker | self-hosting it with Docker]] <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>, it is straightforward to integrate it into [[integrating_local_ai_services_with_supabase | local AI services]] <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## Process of Self-Hosting with Docker

While integrating Supabase might be slightly more complex than other platforms <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>, detailed step-by-step guidance is available to facilitate its setup <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. For users familiar with Supabase in a non-local environment, the interface and functionality will remain very familiar when self-hosting <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. The process allows for the creation of fully local AI agents, such as a RAG AI agent in [[integrating_n8n_and_supabase | n8n]], utilizing the self-hosted Supabase instance <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.