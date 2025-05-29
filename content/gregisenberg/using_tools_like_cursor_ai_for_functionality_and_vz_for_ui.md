---
title: Using tools like Cursor AI for functionality and VZ for UI
videoId: BblTkXR-3eo
---

From: [[gregisenberg]] <br/> 

When [[using_ai_tools_for_design | developing a user interface using AI tools]], a recommended workflow is to prioritize building functionality using tools like Cursor before refining the UI with tools like VZ <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>. This approach is considered ideal, contrasting with the common practice of starting with VZ for wireframes and then moving to Cursor <a class="yt-timestamp" data-t="04:25:00">[04:25:00]</a>.

## Why this Workflow?

The primary goal of this workflow is to achieve more predictable and consistent results when [[building_ai_apps_with_cursor_firebase_and_vercel | building AI apps with Cursor, Firebase, and Vercel]] <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>. Large Language Model (LLM)-based coding can be challenging due to the unpredictable nature of AI, which may "hallucinate" or produce errors, making smooth development difficult <a class="yt-timestamp" data-t="00:53:00">[00:53:00]</a>.

### Benefits of Functionality First

*   **Reduces Ambiguity**: Focusing on core functionality upfront, similar to how product teams operate, clarifies requirements and leaves less room for uncertainty <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>.
*   **Uncovers Uncertainties**: Planning the functionality first helps to identify and address uncertainties early in the development process <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>.
*   **Predictable Changes**: If the project remains too open-ended, the initial output may not align with expectations, and making changes to the structure later can be very difficult <a class="yt-timestamp" data-t="05:58:00">[05:58:00]</a>.
*   **Reduced Errors**: Breaking down the development into smaller, focused tasks for functionality first reduces the likelihood of errors and allows for a more step-by-step approach <a class="yt-timestamp" data-t="40:06:00">[40:06:00]</a>.

### Benefits of UI Second

*   **More Predictable UI**: Once the project's core functionality is built, refining the UI becomes a more predictable and easier task <a class="yt-timestamp" data-t="46:10:00">[46:10:00]</a>.
*   **Lower Error Rate**: Providing existing code to VZ for UI updates, rather than starting with UI, significantly reduces the room for errors <a class="yt-timestamp" data-t="49:24:00">[49:24:00]</a>.

## Workflow for AI Coding

The suggested workflow involves several key steps to ensure a consistent and successful AI coding process:

### 1. Write Clear and Detailed Specs Upfront

This is the most crucial step, requiring significant upfront time <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>. It's an art that ensures effective communication with the AI <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>.

*   **Simulate Product Team Process**: Mimic the workflow of a product team where Product Managers (PMs) write core functionality specs and Engineering Managers (EMs) detail individual tickets or project architecture <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>. This approach minimizes ambiguity for developers <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>.
*   **Spec Structure**:
    *   **Project Overview**: Define the project's goal <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>.
    *   **Core Functionality**: Outline the must-have features <a class="yt-timestamp" data-t="09:25:00">[09:25:00]</a>. Keep it clear enough to communicate goals but don't force every single detail at this stage <a class="yt-timestamp" data-t="12:31:00">[12:31:00]</a>.
    *   **Key Feature Implementation Docs (Proof of Concept)**: Include documentation or proof-of-concept code snippets for key features. This is vital because Cursor's direct documentation insertion often doesn't work well <a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a>. For example, testing API calls or structured outputs from LLMs ensures the core functionality works before full implementation <a class="yt-timestamp" data-t="12:53:00">[12:53:00]</a>. Debugging these early on is beneficial as errors will likely appear later anyway <a class="yt-timestamp" data-t="17:19:00">[17:19:00]</a>.
    *   **Current File Structure**: Provide the AI with the project's current file structure to prevent it from creating files in the wrong places or mismanaging dependencies <a class="yt-timestamp" data-t="10:00:00">[10:00:00]</a>. Tools like `tree -L 2` can generate this easily <a class="yt-timestamp" data-t="34:25:00">[34:25:00]</a>.
    *   **Additional Requirements**: Add common pitfalls or specific needs for the project type (e.g., `use client` for web apps, environment variables, error handling) <a class="yt-timestamp" data-t="10:20:00">[10:20:00]</a>. These sets of requirements can be saved and reused for different project types (web, iOS, etc.) <a class="yt-timestamp" data-t="10:43:00">[10:43:00]</a>.

### 2. Leverage Stronger Models for Detailed Planning

After drafting the initial spec, use a stronger AI model like GPT-4 to refine it <a class="yt-timestamp" data-t="35:40:00">[35:40:00]</a>. Treat this model as an "engineer manager" to fill in details and architectural plans <a class="yt-timestamp" data-t="35:48:00">[35:48:00]</a>.

*   **Generate File Structure**: Ask the model to propose a final file structure and identify necessary components and dependencies <a class="yt-timestamp" data-t="36:12:00">[36:12:00]</a>. This step helps in architecting the project <a class="yt-timestamp" data-t="37:16:00">[37:16:00]</a>.
*   **Elaborate on PRD**: Instruct the model to add details to the original Product Requirement Document (PRD), including file structures and documentation. This creates a highly detailed spec that engineers appreciate, reducing ambiguity <a class="yt-timestamp" data-t="37:29:00">[37:29:00]</a>.

### 3. Build Functionality with Cursor (Step-by-Step)

Once the detailed spec is ready, use Cursor to build the application's functionality. It's crucial to proceed step-by-step <a class="yt-timestamp" data-t="39:43:00">[39:43:00]</a>.

*   **Break into Small Tasks**: Instead of trying to build the entire app at once, which often leads to errors or skipped steps, break down the process into smaller, manageable tasks based on the detailed spec <a class="yt-timestamp" data-t="40:47:00">[40:47:00]</a>.
*   **Debugging**: When errors occur, add debug information to the code <a class="yt-timestamp" data-t="42:35:00">[42:35:00]</a>. Use prompts like "help me debug" or "let's think step by step" to guide the AI, leveraging techniques like Chain-of-Thought prompting to break down complex problems <a class="yt-timestamp" data-t="29:42:00">[29:42:00]</a>.

### 4. Refine UI with VZ

After the core functionality is implemented and stable, switch to VZ for UI improvements <a class="yt-timestamp" data-t="46:02:00">[46:02:00]</a>.

*   **Provide Existing Code**: Paste the relevant code into VZ and instruct it to "make the UI a ton better" while strictly keeping the functionality intact <a class="yt-timestamp" data-t="46:31:00">[46:31:00]</a>.
*   **Specific Style Guidance**: Provide clear design preferences (e.g., "prefer black and white, dark mode, similar to Vercel") to guide the AI's aesthetic choices <a class="yt-timestamp" data-t="46:41:00">[46:41:00]</a>. This prevents the AI from interpreting "looks better" in undesirable ways <a class="yt-timestamp" data-t="47:00:00">[47:00:00]</a>.
*   **Learn Design Language**: To get the most out of VZ, it's beneficial to become well-versed in design concepts, potentially by reading design books, to formulate more effective prompts <a class="yt-timestamp" data-t="47:54:00">[47:54:00]</a>.

## Reusable Modular Prompts

An exciting future for AI coding involves creating and sharing [[best_practices_for_using_cursor_ai | reusable modular prompts]] <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>. Many functionalities, such as user authentication or payment systems, are standard across projects <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.

*   **Community Aggregation**: A collection of prompts for common features (e.g., user authentication, payments) could allow developers to quickly generate entire functionalities by simply providing a prompt to Cursor <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>.
*   **Standardized Features**: These modular prompts streamline the development of standard features, making it faster to spin up new startup ideas without rebuilding common components <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>.
*   **Future Development Tools**: Future developer tools might offer new ways to integrate these prompts directly into applications, moving beyond manual document-based approaches <a class="yt-timestamp" data-t="55:32:00">[55:32:00]</a>.

This structured approach transforms the process from simply prompting an AI to being an "AI coder" <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>, enabling individuals with product backgrounds to build their own products <a class="yt-timestamp" data-t="08:46:00">[08:46:00]</a>. It's akin to an electric-assisted bicycle: it provides a boost but still requires effort <a class="yt-timestamp" data-t="57:37:00">[57:37:00]</a>.