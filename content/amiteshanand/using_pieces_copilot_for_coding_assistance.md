---
title: Using Pieces copilot for coding assistance
videoId: 6GVRFV940Qs
---

From: [[amiteshanand]] <br/> 

This [[pieces_copilot_plus_demo | demonstration]] illustrates how Pieces Copilot can be used as an [[ai_coding_copilot_use_case | AI coding copilot]] to overcome the limitations of standard Large Language Models (LLMs) when dealing with new or obscure frameworks <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It showcases the [[features_of_pieces_copilot_plus | Live Context]] feature of Pieces Copilot <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Overcoming LLM Knowledge Gaps with Pieces Live Context

### The Problem: LLM Limitations on New Frameworks
When queried about "Mop," a Python-based UI framework recently open-sourced <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>, a direct query to GPT-4o LM initially yielded an incorrect answer, confusing "Mop" with "Management Equity Stock Option Plan" <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This highlights that LLMs may not have current or comprehensive knowledge of all frameworks <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

### Solution: Pieces Live Context
To address this, the [[features_of_pieces_copilot_plus | Live Context]] feature of Pieces Copilot can be enabled <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. This feature allows Pieces Copilot to ingest information from the user's active screen or workstream <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

#### How Live Context Works
*   **Enabling Live Context:** Users must activate the Live Context feature within the Pieces Copilot chat <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   **Work Stream Pattern (WSP):** The WSP algorithm, a feature running with Pieces, must also be turned on for Live Context to function properly <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. WSP observes everything the user scrolls through on their screen <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   **Context Ingestion:** By scrolling through a web page or document related to the unknown topic (e.g., the Mop framework documentation) for a few seconds, Pieces Copilot can gather relevant context <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Demonstration: Querying the Mop Framework

After enabling Live Context and WSP, and allowing the system to pick up context by scrolling through the Mop framework's page <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>:

*   **Successful Initial Query:** When asked "What is Mop?" again, Pieces Copilot correctly identified Mop as "a Python-based framework designed to rapidly build web applications such as demos and internal apps" <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   **Follow-up Question:** The system could also provide a step-by-step solution for setting up and installing Mop, including Python installation, Mop installation, adding files, and running the app <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

This demonstration shows how [[using_ai_models_for_coding_assistance | Pieces Copilot's Live Context]] enhances an [[ai_coding_copilot_use_case | AI coding copilot's]] capability by dynamically incorporating real-time context from the user's environment, thereby maximizing its utility <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.