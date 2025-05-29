---
title: Writing clear and detailed specs
videoId: BblTkXR-3eo
---

From: [[gregisenberg]] <br/> 

When engaging in [[AI tools for building software | AI coding]], a common challenge is the unpredictable nature of the results, often due to the large language model's tendency to "hallucinate" or provide errors <a class="yt-timestamp" data-t="00:53:00">[00:53:00]</a>. To achieve more predictable and consistent outcomes, it's crucial to adopt a structured workflow, starting with the creation of clear and detailed specifications <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>.

## Why Detailed Specs are Essential

Many tutorials suggest simply prompting [[AI tools for building software | AI]] to build an entire application <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>. However, in reality, this often leads to unpredictable results and numerous errors because the [[AI tools for building software | AI]] lacks a complete understanding of the project's structure and dependencies <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>, <a class="yt-timestamp" data-t="00:45:00">[00:45:00]</a>. Detailed specifications help to:
*   **Reduce Uncertainty**: Uncover and address uncertainties upfront in the planning phase <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>.
*   **Improve Consistency**: Lead to more consistent and accurate results from the [[AI tools for building software | AI]] <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>.
*   **Prevent Future Errors**: Many errors encountered later can be mitigated by thorough upfront planning <a class="yt-timestamp" data-t="07:21:00">[07:21:00]</a>.

## Simulating a Product Team Workflow

The process of writing detailed specs for [[AI tools for building software | AI coding]] can simulate the workflow of a typical product team <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.
*   A [[creating_a_project_roadmap_and_execution | Product Manager]] defines the core functionality and overall goals <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>.
*   An Engineering Manager then breaks down the project into individual tasks, defines architecture, and outlines project structure, leaving less ambiguity for the [[engineer | engineers]] <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>.

This structured approach helps to ensure the [[AI tools for building software | AI]] delivers exactly what is desired <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>.

## How to Write Detailed Specs

A comprehensive specification document for [[AI tools for building software | AI coding]] should include:

1.  **Project Overview**: A simple summary of the project's goal <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>. For example, building a Reddit analytics platform where users can view top content and categorized insights from subreddits <a class="yt-timestamp" data-t="11:26:00">[11:26:00]</a>.
2.  **Core Functionality**: Break down the "must-have" features <a class="yt-timestamp" data-t="11:43:00">[11:43:00]</a>. For the Reddit analytics platform, this includes:
    *   Listing available subreddits and adding new ones <a class="yt-timestamp" data-t="11:57:00">[11:57:59]</a>.
    *   A subreddit page with "top posts" and "analysis" tabs <a class="yt-timestamp" data-t="12:02:00">[12:02:00]</a>.
    *   Fetching Reddit post data and analyzing it into different categories <a class="yt-timestamp" data-t="12:15:00">[12:15:00]</a>.
3.  **Key Feature Implementation Documentation (Proof of Concept)**: Include specific documentation or code examples for crucial features <a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a>, <a class="yt-timestamp" data-t="12:51:00">[12:51:00]</a>.
    *   **Research**: Use tools like ChatGPT or Google to identify appropriate packages or APIs (e.g., `snoowrap` for Reddit data) <a class="yt-timestamp" data-t="13:21:00">[13:21:00]</a>.
    *   **Proof of Concept Script**: Create small, simple scripts for core functionalities (e.g., fetching Reddit posts, categorizing with OpenAI's structured output) <a class="yt-timestamp" data-t="14:29:00">[14:29:00]</a>, <a class="yt-timestamp" data-t="20:02:00">[20:02:00]</a>.
    *   **Debugging**: Expect and embrace errors during this phase. Use prompts like "help me debug" or "let's think step by step" to guide the [[AI tools for building software | AI]] in fixing issues, which is a common "chain of thought" technique to improve results <a class="yt-timestamp" data-t="17:33:00">[17:33:00]</a>, <a class="yt-timestamp" data-t="29:42:00">[29:42:00]</a>.
    *   **Include Results**: Document the working code examples and expected outputs in the spec <a class="yt-timestamp" data-t="19:19:00">[19:19:00]</a>, <a class="yt-timestamp" data-t="31:54:00">[31:54:00]</a>.
4.  **Current File Structure**: Provide the [[AI tools for building software | AI]] with the existing file structure. This prevents the [[AI tools for building software | AI]] from creating files in the wrong place or with incorrect dependencies <a class="yt-timestamp" data-t="10:02:00">[10:02:00]</a>, <a class="yt-timestamp" data-t="34:06:00">[34:06:00]</a>. Tools like `tree` can help generate this <a class="yt-timestamp" data-t="34:16:00">[34:16:00]</a>.
5.  **Additional Requirements/Common Prompts**: Include boilerplate instructions specific to the project type (e.g., web app, iOS app) <a class="yt-timestamp" data-t="10:20:00">[10:20:00]</a>. These can include:
    *   Ensuring `use client` directives are added.
    *   Correct file creation locations.
    *   Use of environment variables.
    *   Error handling <a class="yt-timestamp" data-t="10:30:00">[10:30:00]</a>.

## Leveraging Stronger Models for Refinement

After creating an initial draft spec, use a stronger [[AI tools for building software | AI model]] (e.g., GPT-4o) to refine it <a class="yt-timestamp" data-t="35:40:00">[35:40:00]</a>.
*   Treat the [[AI tools for building software | AI]] as an "engineer manager" to fill in missing details <a class="yt-timestamp" data-t="35:48:00">[35:48:00]</a>.
*   Ask it to structure the project files and identify dependencies, aligning with standard best practices <a class="yt-timestamp" data-t="36:12:00">[36:12:00]</a>.
*   This refined document, similar to a Product Requirements Document (PRD), defines functionality, variables, and file structures in much greater detail, delighting [[engineer | engineers]] and reducing ambiguity <a class="yt-timestamp" data-t="37:31:00">[37:31:00]</a>, <a class="yt-timestamp" data-t="38:05:00">[38:05:00]</a>.

## Structured [[AI tools for building software | AI Coding]] Workflow

With a detailed spec, the actual [[AI tools for building software | AI coding]] can proceed more smoothly using tools like Cursor:
1.  **Prioritize Functionality**: Focus on building core functionality first. Ignore UI details initially <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>, <a class="yt-timestamp" data-t="40:19:00">[40:19:00]</a>.
2.  **Step-by-Step Implementation**: Break down the project into smaller, manageable tasks and ask the [[AI tools for building software | AI]] to implement them one by one. This reduces errors and improves predictability <a class="yt-timestamp" data-t="39:43:00">[39:43:00]</a>, <a class="yt-timestamp" data-t="40:42:00">[40:42:00]</a>.
3.  **UI Refinement Later**: Once functionality is built, use tools like [[Figma design best practices | Vercel v0]] to refine the UI bit by bit <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>, <a class="yt-timestamp" data-t="46:02:00">[46:02:00]</a>. Provide specific style preferences or examples (e.g., "similar to Vercel") to guide the [[AI tools for building software | AI]] effectively <a class="yt-timestamp" data-t="46:38:00">[46:38:00]</a>.

## Reusable Modular Prompts

An exciting aspect of this workflow is the potential for **reusable modular prompts** <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>.
*   Many features (e.g., user authentication, payment systems) are standard across applications <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>, <a class="yt-timestamp" data-t="52:27:00">[52:27:00]</a>.
*   A community-shared collection of these prompts could allow [[AI tools for building software | AIs]] like Cursor to generate entire functionalities efficiently <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>, <a class="yt-timestamp" data-t="55:14:00">[55:14:00]</a>.
*   This approach, akin to [[technical_standards_and_protocols_in_programming_and_apis | technical standards and protocols]], accelerates development by providing proven, pre-defined instructions for common tasks <a class="yt-timestamp" data-t="55:17:00">[55:17:00]</a>.

By spending significant time upfront on detailed specifications, focusing on functionality before UI, and leveraging reusable prompts, [[AI tools for building software | AI coding]] becomes a much more structured, predictable, and ultimately successful endeavor <a class="yt-timestamp" data-t="56:05:00">[56:05:00]</a>. It transforms the process from an open-ended "one-shot" attempt to a systematic "crawl, walk, run" approach <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>, <a class="yt-timestamp" data-t="41:17:00">[41:17:00]</a>.