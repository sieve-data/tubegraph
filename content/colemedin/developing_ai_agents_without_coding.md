---
title: Developing AI agents without coding
videoId: ieLdMih5_V0
---

From: [[colemedin]] <br/> 

Developing AI agents exists on a spectrum, with one end requiring extensive custom coding for complex needs and specific requirements <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, for simpler use cases or quick proofs of concept, it's often more efficient to utilize existing platforms <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. These platforms significantly reduce development time and effort compared to [[Advancing AI agents with Python and custom coding | coding from scratch]] <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Benefits of [[no_code_ai_agent_builders | No-Code Platforms]] for [[Building AI Agents | AI Agents]]

[[no_code_ai_agent_builders | No-code platforms]] offer significant convenience and speed for [[Building AI Agents | developing agents]] <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. They allow users to create powerful, robust, and simple AI agents quickly <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. This approach is particularly useful for rapid prototyping and establishing proof of concepts <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## Vector Shift: A [[no_code_ai_agent_builders | No-Code]] Solution

Vector Shift is a platform that simplifies the creation of AI agents through a drag-and-drop component workflow builder <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. It is designed to focus heavily on AI development <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

### Getting Started with Vector Shift

To begin using Vector Shift, one can visit VectorShift.ai and click "get started" <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. A free tier is available to create an initial knowledge base and workflow <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

The Vector Shift dashboard features three main components:
*   **Chatbots**: Used for integrating the AI agent into a website <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   **Knowledge**: Manages knowledge bases, such as connecting to Google Drive to ingest documents for Retrieval Augmented Generation (RAG) <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Pipelines**: Where workflows are created, including those utilizing AI <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

### [[Step by step process for building AI agents | Step-by-Step Process for Building a RAG AI Agent]]

This section details how to build a full RAG AI agent using Vector Shift in minutes <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

#### 1. Setting Up the Knowledge Base

1.  Navigate to the "Knowledge" section in Vector Shift <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
2.  Click "New" to create a new knowledge base <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
3.  Name the knowledge base (e.g., "test KB") <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. Default settings for chunk size and embedding model are typically sufficient <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
4.  Add documents by selecting an integration, such as Google Drive <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. Authenticate Google Drive if not already done <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
5.  Select a specific Google Drive folder (e.g., "meeting notes folder") to ingest documents <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
6.  The documents are quickly added as vectors into the knowledge base <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. This integration constantly syncs with the Google Drive folder, updating with file deletions, creations, and updates <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

#### 2. Creating the Pipeline

1.  Go to the "Pipelines" section <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
2.  Create a new pipeline from scratch <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
3.  Add an "Input" component, typically the start of any Vector Shift workflow <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. Set the field name (e.g., "input") and type (text) <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
4.  Add an LLM component (e.g., Anthropic, using Claude 3.5 Sonnet) <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
5.  Drag the "Input" into the LLM's prompt. A custom variable can be used to combine input and context <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
6.  Set the LLM's system prompt (e.g., "You are a helpful assistant who answers questions to the best of your ability") <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
7.  Add the "Knowledge Base" component from the top-left tab <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
8.  Select the previously created knowledge base (e.g., "test KB") <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
9.  Connect the pipeline's "Input" to the knowledge base query <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
10. Feed the results from the knowledge base (retrieved context) into the LLM's "context" variable <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
11. Add an "Output" component and connect the LLM's response to it <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. Name it "output" and set the type to text <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

#### 3. Testing the Agent

1.  Click "Deploy Changes" in the top right <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
2.  Click "Run Pipeline" <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
3.  Input a query that requires access to the integrated documents (e.g., "what are the action items from the 8/23 meeting?") <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
4.  Verify that the LLM's response accurately retrieves information from the knowledge base <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

#### 4. Deploying the Agent

1.  Once the agent is created and validated, click "Export Pipeline" in the top right <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
2.  Choose to export as an "Automation," "Chatbot," "Search," or "Form" <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
3.  For a chatbot, name it (e.g., "test chatbot") and create <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
4.  The deployed agent can be accessed via a URL, API, or integrated directly into Slack <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

### Templates for Quick Starts

Vector Shift provides numerous templates to help users get started without [[Step by step process for building AI agents | building a workflow from scratch]] <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. Examples include a Blog article generator template, which can even use multiple LLMs working together <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.

> [!NOTE]
> While a free tier provides some credits for LLMs, custom API keys are typically needed for extended use <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

## Conclusion

[[no_code_ai_agent_builders | No-code platforms]] like Vector Shift offer a valuable alternative for [[Developing AI Agents using Python | developing AI agents]], especially for simple use cases or initial proofs of concept <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>. They save significant time by avoiding the need to "reinvent the wheel" with custom coding <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. While custom coding has its place for highly specific and complex needs, [[no_code_ai_agent_builders | no-code tools]] provide an efficient and robust way to [[Building AI Agents | build and deploy AI applications]] rapidly <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.