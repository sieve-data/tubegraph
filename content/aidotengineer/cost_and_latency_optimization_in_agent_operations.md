---
title: Cost and latency optimization in agent operations
videoId: y2Drx0SDZLo
---

From: [[aidotengineer]] <br/> 

[[evaluating_and_optimizing_ai_agents_and_workflows | Evaluating and optimizing AI agents]] requires considering practical aspects beyond their functional performance, particularly [[cost_considerations_in_ai_agent_deployment | cost]] and latency <a class="yt-timestamp" data-t="08:07:07">[08:07:07]</a>, <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>, <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>.

## Core Objectives
The primary goal in [[developing_and_optimizing_ai_agents | developing and optimizing AI agents]] is to ensure they achieve their objectives as quickly and cheaply as possible <a class="yt-timestamp" data-t="08:27:00">[08:27:00]</a>, <a class="yt-timestamp" data-t="08:30:00">[08:30:00]</a>, <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>. This involves:
*   **Cost and Latency Optimization** <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>
*   **Number of Steps Optimization** <a class="yt-timestamp" data-t="08:36:00">[08:36:00]</a>, <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>

## The Double-Tier Optimization Challenge (Eval Ops)
When implementing evaluation methodologies for AI agents, a common pitfall is to adopt a "single-tier approach" <a class="yt-timestamp" data-t="10:44:00">[10:44:00]</a>. This approach focuses solely on optimizing the "operative element flow," meaning the agent itself <a class="yt-timestamp" data-t="10:46:00">[10:46:00]</a>, <a class="yt-timestamp" data-t="10:48:00">[10:48:00]</a>, <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>, <a class="yt-timestamp" data-t="10:52:00">[10:52:00]</a>.

However, this often overlooks the [[cost_considerations_in_ai_agent_deployment | costs]], latencies, and uncertainties associated with the evaluation mechanism itself, referred to as "the charge" <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>, <a class="yt-timestamp" data-t="11:01:00">[11:01:00]</a>, <a class="yt-timestamp" data-t="11:04:00">[11:04:00]</a>, <a class="yt-timestamp" data-t="11:07:00">[11:07:00]</a>.

To address this, it's crucial to adopt a "Double tier" approach, optimizing both <a class="yt-timestamp" data-t="11:21:00">[11:21:00]</a>:
1.  The operative LLM (Large Language Model) flow that powers the agent <a class="yt-timestamp" data-t="11:23:00">[11:23:00]</a>, <a class="yt-timestamp" data-t="11:26:00">[11:26:00]</a>.
2.  The chargement flow that powers the evaluations <a class="yt-timestamp" data-t="11:28:00">[11:28:00]</a>.

This complex situation is termed "Eval Ops" <a class="yt-timestamp" data-t="11:31:00">[11:31:00]</a>, <a class="yt-timestamp" data-t="11:34:00">[11:34:00]</a>, <a class="yt-timestamp" data-t="11:37:00">[11:37:00]</a>. Evaluations can be complicated, expensive, and slow, warranting their own category of activities within this framework <a class="yt-timestamp" data-t="11:43:00">[11:43:00]</a>, <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>, <a class="yt-timestamp" data-t="11:49:00">[11:49:00]</a>, <a class="yt-timestamp" data-t="11:52:00">[11:52:00]</a>. Eval Ops is considered a special case of LLM Ops, operating on different entities and requiring distinct thinking, software implementations, and resource allocation to ensure accurate evaluations <a class="yt-timestamp" data-t="12:08:00">[12:08:00]</a>, <a class="yt-timestamp" data-t="12:10:00">[12:10:00]</a>, <a class="yt-timestamp" data-t="12:13:00">[12:13:00]</a>, <a class="yt-timestamp" data-t="12:15:00">[12:15:00]</a>, <a class="yt-timestamp" data-t="12:19:00">[12:19:00]</a>, <a class="yt-timestamp" data-t="12:23:00">[12:23:00]</a>, <a class="yt-timestamp" data-t="12:24:00">[12:24:00]</a>, <a class="yt-timestamp" data-t="12:26:00">[12:26:00]</a>, <a class="yt-timestamp" data-t="12:29:00">[12:29:00]</a>, <a class="yt-timestamp" data-t="12:32:00">[12:32:00]</a>.