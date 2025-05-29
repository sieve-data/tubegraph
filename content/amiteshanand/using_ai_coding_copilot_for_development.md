---
title: Using AI coding copilot for development
videoId: 6GVRFV940Qs
---

From: [[amiteshanand]] <br/> 

This article explores how AI coding copilots, specifically "Pieces Copilot," can be enhanced using features like "Live Context" to improve their knowledge base and assist in development tasks, even with recently introduced frameworks <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Initial Challenge: LLM Unawareness of New Frameworks

When initially queried, [[Using AI coding copilot for development | Pieces Copilot]] (powered by GPT-4o LM) was asked "what is Mup?" <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. Mup is a Python-based UI framework that was recently open-sourced <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. Due to its recent open-source status, large language models (LLMs) are often unaware of it <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. As expected, [[Using AI coding copilot for development | Pieces Copilot]] provided an incorrect definition, identifying "Msub" as "management equity stock option plan," indicating it had no knowledge of the Mup framework <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Enhancing Knowledge with Pieces Live Context

To address the LLM's lack of information, the "Pieces Live Context" feature was utilized <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

### Enabling Live Context and WSP

To activate this feature:
1.  Create a new chat in [[Using AI coding copilot for development | Pieces Copilot]] <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
2.  Turn on "Live Context" as a context <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
3.  Ensure "WSP" (Work Stream Pattern) is also enabled <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. WSP is an algorithm and feature running with Pieces that allows Live Context to function properly <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

### Providing Context to the AI

With Live Context and WSP turned on, the user scrolled through a webpage containing information about Mup for a few seconds <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. During this time, [[Using AI coding copilot for development | Pieces Copilot]] actively picked up context from the scrolled content <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. WSP observes everything the user scrolls through on the screen <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## Improved Understanding and Problem-Solving

After providing the context, the same question, "what is Mup?", was asked again to [[Using AI coding copilot for development | Pieces Copilot]] <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

### Correct Definition and Functionality

This time, [[Using AI coding copilot for development | Pieces Copilot]] provided a correct and accurate answer: "Mup is a Python-based framework designed to rapidly build web applications such as demos and internal apps" <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

### Step-by-Step Installation Guide

Following the correct definition, a follow-up question was posed: "how to set up and install Mup?" <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. [[Using AI coding copilot for development | Pieces Copilot]] then provided a step-by-step solution for installation and project setup, including:
*   Python installation <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>
*   Installing Mup <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>
*   Adding necessary files and code <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>
*   Running the application <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>

This demonstration highlights how "Pieces Live Context" allows [[Using AI coding copilot for development | Pieces Copilot]] to pick up relevant information and operate at its maximum capability, significantly aiding in development by providing contextually aware assistance <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.