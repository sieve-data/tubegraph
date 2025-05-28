---
title: limitations of traditional software engineering roles
videoId: tFwYD1UPIfM
---

From: [[hu-po]] <br/> 

Traditional software engineering organizations often employ a "waterfall method" that defines specific job roles and workflows from analysis to delivery, aiming to promote teamwork <a class="yt-timestamp" data-t="09:56:06">[09:56:06]</a>. This approach includes distinct roles such as:
*   **Product Manager:** Determines requirement documents <a class="yt-timestamp" data-t="13:30:19">[13:30:19]</a>.
*   **Architect:** Determines system design <a class="yt-timestamp" data-t="13:25:34">[13:25:34]</a>.
*   **Project Manager:** Determines tasks <a class="yt-timestamp" data-t="13:23:44">[13:23:44]</a>.
*   **Engineer:** Writes code <a class="yt-timestamp" data-t="13:19:59">[13:19:59]</a>.
*   **QA Engineer:** Tests the code <a class="yt-timestamp" data-t="13:16:32">[13:16:32]</a>.

## Criticisms of Role Specialization

The specialization and hierarchical structure of these roles are subject to several criticisms regarding their effectiveness and underlying motivations:

### Engineer's Role and Cross-Functionality
Ideally, the engineer, as the person writing the code, should also be responsible for testing it and determining tasks, given their intimate knowledge of the system <a class="yt-timestamp" data-t="17:01:01">[17:01:01]</a>. Large, specialized teams often prove slower and less effective than small teams where individuals perform more technical work <a class="yt-timestamp" data-t="17:24:26">[17:24:26]</a>. The overwhelming majority of successful products are created by small teams largely performing all technical work themselves, with waterfall-type teams rarely resulting in anything novel or useful <a class="yt-timestamp" data-t="17:44:00">[17:44:00]</a>.

### Loss of Technical Relevance by Management
A significant concern is that product managers, architects, and project managers often cease writing code after several years in their roles <a class="yt-timestamp" data-t="18:09:00">[18:09:00]</a>. This disconnect means they may not fully understand the technical realities or limitations of the current coding landscape <a class="yt-timestamp" data-t="18:46:00">[18:46:00]</a>. The effectiveness of a manager who hasn't coded in 10 or 20 years is questioned, as their intuition about what's important may no longer apply in a rapidly changing technological world <a class="yt-timestamp" data-t="21:39:00">[21:39:00]</a>. The analogy is drawn to a fitness trainer who no longer works out, questioning their ability to effectively guide others <a class="yt-timestamp" data-t="22:04:00">[22:04:00]</a>.

### Hierarchical Systems and Misaligned Incentives
The existence of these specialized, non-coding roles can be attributed to a "Ponzi scheme" where older, more senior individuals siphon value from younger, energy-rich engineers <a class="yt-timestamp" data-t="19:00:00">[19:00:00]</a>. This hierarchical system, based on age and seniority, is argued to be a legacy from medieval times when environments were stable, but it's no longer applicable in a world of rapid technological change <a class="yt-timestamp" data-t="23:02:00">[23:02:00]</a>.

In this structure, lower-level employees find it difficult to push back against higher-level management <a class="yt-timestamp" data-t="27:22:00">[27:22:00]</a>. The incentives are often misaligned: engineers are incentivized to get on the good side of product managers to eventually transition into cushier, higher-paying project manager roles that require less work <a class="yt-timestamp" data-t="27:56:00">[27:56:00]</a>. This means people are primarily interested in making money and gaining status, rather than contributing to the company's mission or building good products <a class="yt-timestamp" data-t="29:56:00">[29:56:00]</a>.

## Implications for AI-Driven Development
The MetaGPT project, which uses a multi-agent collaborative framework to mimic traditional software engineering roles, highlights these limitations <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a>. By assigning roles like product manager, architect, and project manager to different Large Language Models (LLMs), MetaGPT generates verbose and often nonsensical intermediate documents (such as requirement documents, system designs, and API specifications) <a class="yt-timestamp" data-t="51:30:00">[51:30:00]</a>. This extensive, unnecessary context leads to inefficient and incorrect code output from the "engineer" LLM <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.

In contrast, a direct [[Prompt Engineering using LLMs | prompt engineering]] approach by asking a single LLM (like GPT-4) to write code for the same task produced a more functional and concise result with significantly fewer tokens <a class="yt-timestamp" data-t="01:12:44">[01:12:44]</a>. This suggests that the process of breaking down tasks through these specialized, managerial roles, even when mimicked by AI, adds unnecessary complexity and can degrade the final output. The experiment implies that much of the documentation and managerial layers in traditional software development might be pointless in an AI-driven future, as they create "extra context that doesn't really help" <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>.

The benchmarks used to evaluate MetaGPT (HumanEval and MBPP) primarily test the ability to write individual functions from docstrings, rather than complex system design or product development, further suggesting that the value of these layered roles for large-scale problem-solving is not adequately assessed <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.

## Conclusion
The analysis suggests that the current structure of traditional software engineering organizations, with their rigid, specialized, and often hierarchical roles, may be inefficient and counterproductive, especially in an era where AI can generate code directly. The argument is made that streamlining these processes by empowering engineers and reducing unnecessary managerial layers could lead to more optimal and efficient product development <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>.