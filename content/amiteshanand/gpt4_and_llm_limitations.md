---
title: GPT4 and LLM limitations
videoId: 6GVRFV940Qs
---

From: [[amiteshanand]] <br/> 

Large Language Models (LLMs), including GPT-4o, can exhibit knowledge gaps, particularly concerning very recent or niche information. This limitation means they may not be aware of newly open-sourced frameworks or technologies [00:00:17].

## Demonstrating a Knowledge Gap

An example of this limitation was demonstrated with "MOP," a Python-based UI framework that was recently open-sourced [00:00:13]. When queried, GPT-4o LM initially provided an incorrect definition for MOP, stating it stood for "management Equity stock option plan" [00:00:39]. This response confirmed that the model lacked specific knowledge about the MOP UI framework [00:00:40].

## Overcoming Limitations with Live Context

To address such knowledge gaps, features like [[live_context_windows_for_llms | Pieces live context]] can be utilized [00:00:44]. By activating [[live_context_windows_for_llms | live context windows for LLMs]] along with "WSP" (Work Stream Pattern), which is an algorithm running with Pieces Copilot, the system can dynamically pick up relevant information [00:00:51]<a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

After enabling live context and scrolling through a page containing information about MOP, Pieces Copilot was able to extract the necessary context [00:01:13]. When the same question, "What is MOP," was asked again, GPT-4o successfully provided the correct definition: "MOP is a python based framework designed to rapidly build web application such as demos and internal apps" [00:01:52]. Furthermore, it could provide step-by-step instructions for setting up and installing MOP [00:02:17].

This demonstrates how [[live_context_windows_for_llms | Pieces live context]] can augment LLM capabilities, enabling them to access and use information beyond their pre-trained knowledge base [00:02:31].