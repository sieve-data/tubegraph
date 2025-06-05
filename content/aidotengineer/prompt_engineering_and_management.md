---
title: Prompt Engineering and Management
videoId: n9rjuBuShko
---

From: [[aidotengineer]] <br/> 

LinkedIn's journey in building its Generative AI (GenAI) platform highlights the evolving role and [[importance_of_prompt_engineering | importance of prompt engineering]] and management. The platform was developed incrementally, addressing immediate needs before expanding into a comprehensive system <a class="yt-timestamp" data-t="09:28:00">[09:28:00]</a>.

## Early Stages: Collaborative Articles

LinkedIn launched its first formal GenAI feature, "collaborative articles," in 2023 <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>. This feature was a straightforward "prompt in, string out" application, leveraging the GPT-4 model to create long-form articles that members could comment on <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>.

During this initial phase, the team helped build key backend components, including:
*   A gateway for centralized access to the model <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>.
*   Python notebooks for [[techniques_and_patterns_in_ai_orchestration_and_prompt_engineering | prompt engineering]] <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>.

At this time, LinkedIn used two distinct tech stacks: Java for the online experience and Python for the backend <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>. This initial setup was not yet considered a full platform <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>.

## Evolution to Platform Capabilities

By mid-2023, LinkedIn began developing its second generation of GenAI products, internally referred to as "co-pilot" or "coach" <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>. An example is a feature that provides personalized job recommendations based on a user's profile and job descriptions, using a Retrieval-Augmented Generation (RAG) process <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.

This phase marked the beginning of building dedicated platform capabilities:
*   **Unified Tech Stack:** Realizing the high cost and error potential of transferring Python prompts to Java, the team started unifying the tech stack, prioritizing Python <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>, <a class="yt-timestamp" data-t="14:40:00">[14:40:00]</a>. Python was chosen due to its prevalence in research and open-source communities, and its scalability <a class="yt-timestamp" data-t="14:50:00">[14:50:00]</a>.
*   **Prompt Management (Source of Truth):** A significant investment was made in a sub-module for "prompt management" or "prompt source of truth" <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>. This component helps developers version their prompts and provides structure for meta-prompts <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>.

## Importance of Prompt Source of Truth

A prompt source of truth is considered a critical component for the operational stability of GenAI applications <a class="yt-timestamp" data-t="15:13:00">[15:13:00]</a>. It functions similarly to traditional model parameters, requiring a robust system for version control <a class="yt-timestamp" data-t="15:06:00">[15:06:00]</a>. This prevents accidental edits to prompts in production that could lead to severe negative effects <a class="yt-timestamp" data-t="15:18:00">[15:18:00]</a>.

## Prompt Engineering within the GenAI Ecosystem

The LinkedIn GenAI platform classifies its components into four main layers, one of which is [[techniques_and_patterns_in_ai_orchestration_and_prompt_engineering | prompt engineering]] tools <a class="yt-timestamp" data-t="07:44:00">[07:44:00]</a>.

Even with a centralized platform, developers still need to engage in [[importance_of_prompt_engineering | prompt engineering]] <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>. However, the platform simplifies much of the infrastructure integration complexity, allowing developers to easily switch between models (e.g., OpenAI to an on-premise model) by changing a single parameter <a class="yt-timestamp" data-t="08:50:00">[08:50:00]</a>.

> [!NOTE] Key takeaway for building a GenAI platform:
> Prioritize building a "prompt source of truth" system that allows for robust version control of prompts, similar to how traditional model parameters are managed. This is critical for operational stability and preventing unintended production issues <a class="yt-timestamp" data-t="15:03:00">[15:03:00]</a>.

The platform's centralized nature also provides a mechanism to enforce best practices and governance, ensuring applications are built efficiently and responsibly <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>.