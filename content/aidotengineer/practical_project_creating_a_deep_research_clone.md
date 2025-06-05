---
title: Practical project Creating a deep research clone
videoId: kDlqpN1JyIw
---

From: [[aidotengineer]] <br/> 

This section focuses on building a deep research clone using the AI SDK in Node.js, demonstrating how to construct complex AI systems by combining various AI SDK functions and integrating with external tools <a class="yt-timestamp" data-t="00:25:24">[00:25:24]</a>. The project aims to take a user query, conduct deep research by searching the web, aggregate findings, and compile them into a markdown report <a class="yt-timestamp" data-t="00:24:52">[00:24:52]</a>.

## Project Workflow Overview

Deep research products, like those offered by OpenAI or Google's Gemini, typically take a topic, search the web, aggregate resources, and return a comprehensive report <a class="yt-timestamp" data-t="00:26:12">[00:26:12]</a>. This project's workflow is broken down into several autonomous agentic steps:

1.  **Input Query**: Start with a user-provided prompt or rough query <a class="yt-timestamp" data-t="00:26:53">[00:26:53]</a>.
2.  **Generate Subqueries**: Based on the initial prompt, generate a list of specific search queries <a class="yt-timestamp" data-t="00:26:58">[00:26:58]</a>.
3.  **Search the Web**: For each subquery, search the web for relevant results <a class="yt-timestamp" data-t="00:27:15">[00:27:15]</a>.
4.  **Analyze Results**: Analyze the search results to extract key learnings and identify follow-up questions <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a>.
5.  **Recursive Research**: If necessary, take the follow-up questions and existing research to generate new queries, recursively repeating the process to explore topics in depth <a class="yt-timestamp" data-t="00:27:26">[00:27:26]</a>. This allows the system to go down "webs of thought" and accumulate a comprehensive set of information <a class="yt-timestamp" data-t="00:27:47">[00:27:47]</a>.
    *   **Depth and Breadth**: The `depth` setting controls how many levels deep the research goes, while `breadth` dictates how many different lines of inquiry are pursued at each step <a class="yt-timestamp" data-t="00:28:06">[00:28:06]</a>.
6.  **Generate Report**: Synthesize all the accumulated research into a final markdown report <a class="yt-timestamp" data-t="00:26:26">[00:26:26]</a>.

## Implementation Details

The project utilizes the AI SDK's capabilities for [[prototyping_and_production_in_ai | prototyping and production in AI]], especially its `generateObject` and `generateText` functions, along with ZOD for schema definition <a class="yt-timestamp" data-t="01:52:05">[01:52:05]</a>.

### Project Setup

To follow along with the implementation:
1.  Clone the repository <a class="yt-timestamp" data-t="00:35:00">[00:35:00]</a>.
2.  Install dependencies <a class="yt-timestamp" data-t="00:38:00">[00:38:00]</a>.
3.  Copy environment variables <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>.
4.  Run the `index.ts` file using `pmpp rundev` (or `pd` as an alias) <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>.

### 1. Generating Search Queries

The initial step involves taking a broad user query and generating more specific search queries for a search engine <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.

*   **`generateSearchQueries` function**:
    *   Takes a `query` (string) and `numberOfSearchQueries` (defaulting to 3) <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.
    *   Uses `generateObject` with a `mainModel` (e.g., GPT-4o mini) <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>.
    *   The prompt instructs the model to generate `n` search queries for the given input query <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>.
    *   The output schema is an array of strings (`Z.array(Z.string())`) with a minimum of 1 and maximum of 5 items, though the default is 3 <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.
    *   Example for "what do you need to be a D1 shotput athlete?": "requirements to become a D1 shotput athlete", "training regiment for D1 shotput athlete", "qualifications for NCAA division one shot put" <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>.

### 2. Web Search with Exa

For searching the web, the Exa service is used, known for its speed and cost-effectiveness <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>.

*   **`searchWeb` function**:
    *   Takes a `query` (string) <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>.
    *   Uses `exa.searchAndContents` <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>.
    *   Configurable options: `resultsLimit` (defaulting to 1 for simplicity) and `liveCrawl` (ensures up-to-date results, potentially impacting performance) <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>.
    *   Crucially, results are mapped to return only relevant information (e.g., `url`, `title`, `text`) to reduce token usage and improve model effectiveness by trimming irrelevant data <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>. This is a common strategy in [[generative_ai_project_challenges_and_strategies | Generative AI project challenges and strategies]] related to prompt engineering and cost optimization.

### 3. Analyzing Results for Learnings and Follow-up Questions

This is an agentic part of the workflow, where the model decides how to proceed based on the relevance of search results <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>.

*   **`searchAndProcess` function**:
    *   Uses `generateText` with `maxSteps` (e.g., 5) to create an autonomous loop <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>.
    *   **Tools Defined**:
        *   `searchWeb`: Searches the web for a query. The result is added to `pendingSearchResults` <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>.
        *   `evaluate`: Evaluates the latest `pendingSearchResult` <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.
            *   Uses `generateObject` in enum mode (`relevant` or `irrelevant`) to determine relevance <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>.
            *   If irrelevant, the tool returns a string like "Search results are irrelevant, please search again with a more specific query," which guides the language model to refine its next search <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>.
            *   If relevant, the result is moved to `finalSearchResults` <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>.
            *   Crucially, this tool also checks `accumulatedSources` to avoid reusing previously processed URLs, preventing redundant searches and saving tokens <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>. This addresses a common [[design_challenges_in_building_web_research_agents | design challenge in building web research agents]].
    *   The `maxSteps` parameter allows the model to autonomously continue searching and evaluating until a relevant result is found or the step limit is reached <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>.

*   **`generateLearnings` function**:
    *   Takes the original `query` and the `searchResult` (scraped web page content) <a class="yt-timestamp" data-t="04:39:00">[04:39:00]</a>.
    *   Uses `generateObject` to extract a `learning` (insight) and `followUpQuestions` (an array of strings) from the content <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>.
    *   The prompt emphasizes the user's research goal and the relevant search result <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>.

### 4. Introducing Recursion for Deeper Research

To enable [[handling_complex_queries_with_deep_research | handling complex queries with deep research]] and go deeper into specific topics, a recursive `deepResearch` function is implemented.

*   **`deepResearch` function**:
    *   Manages the entire research process recursively, tracking accumulated research state (original query, active queries, search results, learnings, completed queries) <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.
    *   Accepts `prompt`, `depth`, and `breadth` parameters to control the scope <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>.
    *   Generates search queries, calls `searchAndProcess` for each, and then `generateLearnings` <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>.
    *   Updates the global `accumulatedResearch` store with new findings <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.
    *   Recursively calls itself with new queries derived from `followUpQuestions`, decrementing `depth` and `breadth` to ensure termination <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.
    *   A base case handles `depth` reaching zero, at which point the recursion stops <a class="yt-timestamp" data-t="05:26:00">[05:26:00]</a>.

### 5. Generating the Final Report

Once all research is accumulated, a final model synthesizes the information into a coherent report.

*   **`generateReport` function**:
    *   Takes the `accumulatedResearch` object <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>.
    *   Uses `generateText` with a reasoning model (e.g., `GPT-3.5 mini` was found effective) <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>.
    *   A detailed system prompt is used to guide the model on formatting (e.g., Markdown), persona (expert researcher), and specific instructions (e.g., using today's date, allowing speculation but flagging it) <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>. This ensures a structured and high-quality output report.
    *   The final report is then written to a markdown file <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>.

## Key Takeaways

*   This project demonstrates how to break down complex problems like deep research into a structured, multi-step AI workflow <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.
*   The AI SDK's `generateObject` and `generateText` functions, combined with tool calling and recursion, allow for the creation of sophisticated, autonomous agents <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.
*   Effective prompt engineering, including system prompts and the use of ZOD for structured outputs, is crucial for guiding language models and ensuring desired results <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>.
*   Optimizing token usage by filtering irrelevant information from tool results is essential for cost-efficiency and model performance <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>.
*   The project provides a practical example of [[deep_research_features_of_gemini_at_google | deep research features of Gemini at Google]] and OpenAI's research capabilities.

## Tools and Technologies

*   **AI SDK**: Core library for interacting with Large Language Models (LLMs) and building agents <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.
    *   `generateText`: Generates text from an LLM, supports tools and `maxSteps` for agentic behavior <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>.
    *   `generateObject`: Dedicated function for generating structured JSON objects based on a defined schema, preferred for its type safety and control <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>.
    *   `streamText`, `streamObject`: Streaming versions of the generation functions <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.
    *   Unified Interface: Allows switching between different LLM providers (OpenAI, Perplexity, Google Gemini) by changing a single line of code <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>.
*   **ZOD**: A TypeScript-first schema declaration and validation library, used for defining structured output schemas <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>. Its `describe` function can add specific instructions to the model for individual schema fields <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>.
*   **Exa**: A search service used for web crawling and searching, providing live and cached content <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.
*   **Node.js**: The runtime environment for the project <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>.