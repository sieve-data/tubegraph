---
title: AI agents and large language models
videoId: pC17ge_2n0Q
---

From: [[colemedin]] <br/> 

[[AI agents and their development | AI agents]], which are [[Reasoning large language models and their impact | large language models]] capable of performing tasks autonomously, are a relatively new concept <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Existing frameworks like LangChain, CrewAI, and Swarm, as well as no-code agent builders, are generally not mature or production-ready for building robust [[AI agents and their development | AI agents]] without significant additional work <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. However, Pydantic AI is emerging as a solution that simplifies the development of production-grade [[AI agents and their development | agents]] <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## What is Pydantic AI?
Pydantic AI is an open-source Python agent framework designed to make the development of production-grade [[AI agents and their development | agents]] much easier <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. It implements crucial features often overlooked in other frameworks, such as context management, error handling, retry logic, testing, evaluation capabilities, logging and monitoring, and large language model output validation <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

### Core Philosophy: Validation
Pydantic AI leverages the established Pydantic library, which is a Python validation library <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. This foundation ensures that expected data formats and structures are adhered to, similar to how FastAPI uses Pydantic for validating API endpoint payloads <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. For [[Reasoning large language models and their impact | large language models]], Pydantic AI acts as a validation layer to ensure that the expected structured output (e.g., specific JSON keys) is actually received <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. Many other frameworks, including OpenAI, Anthropic, LangChain, LlamaIndex, and CrewAI, also utilize Pydantic for validation <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. The Pydantic AI team's focus on validation, especially for LLM output, testing, and tool invocation, sets it apart <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## Key Features of Pydantic AI
Pydantic AI incorporates several features vital for building robust and production-ready [[AI agents and their development | agents]]:

*   **Model Agnostic** <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>: It supports various LLM providers, including Google Gemini and OpenAI, and allows users to add custom providers <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. It can also integrate with [[Working with local large language models | local large language models]] via Ollama <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Type Safe with Structured Responses** <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>: Leverages classic Pydantic for structured and streamed responses, ensuring data integrity <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   **Type Safe Dependency Injection System** <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>: This system allows for effective context management for the agent, handling important details like database connections and API keys <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. It's also crucial for testing and evaluation, enabling the use of mock dependencies <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. This ensures sensitive credentials are not exposed to the LLM <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
*   **Logfire Integration** <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>: Provides robust debugging and monitoring capabilities, offering a UI to track LLM and tool calls <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Built-in Error Handling and Retry Logic** <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>: Includes features like `model_retry`, allowing the agent to automatically retry operations in case of errors (e.g., overload errors from Anthropic) <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Testing and Evaluation Capabilities** <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>: Supports features like "test models," which allow for running unit or integration tests without incurring costs by calling a real large language model <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   **Easy Tool Binding** <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>: Tools can be easily attached to an agent using a decorator (`@agent.tool`), with context automatically passed to tool calls <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. The tool's docstring helps the LLM understand when and how to use the tool <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
*   **Comprehensive Results and Chat History** <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>: Allows easy access to information like cost and other metadata from results <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. The entire chat history can be retrieved after any LLM call <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

## Building a Web Search Agent with Pydantic AI
A demonstration of building a web search agent using Pydantic AI and the Brave Search API highlights its capabilities <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

### Prerequisites
*   Python <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>
*   Brave Search API Key <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>
*   OpenAI API Key (for GPT models) <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>
*   Ollama (for [[Working with local large language models | local large language models]]) <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>

### Agent Construction Steps
1.  **Environment Setup**: Load API keys and the desired LLM model from an `.env` file <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
2.  **LLM Configuration**:
    *   For [[Working with local large language models | local large language models]] via Ollama, a custom asynchronous OpenAI instance is configured to point to the Ollama server's local host <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
    *   The specific LLM instance (GPT or Ollama) is chosen based on an environment variable <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
3.  **Dependencies Definition**: Define necessary dependencies for the agent, such as an HTTP client for web browsing and the Brave API key <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. These are accessed by tools without being passed directly to the LLM <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
4.  **Agent Definition**: Initialize the `PydanticAgent` with the chosen model, a system prompt (including current time for relevance), defined dependencies, and `model_retry` settings <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
5.  **Tool Definition (Web Search)**:
    *   A function for web search is defined using the `@agent.tool` decorator <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.
    *   It accepts the `context` (containing client and API key) and a `query` provided by the LLM <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
    *   A docstring instructs the LLM on its usage <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.
    *   The tool handles cases where the API key might not be defined (e.g., for testing) <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.
    *   It uses the `client` from the context to make an HTTP call to the Brave Search API <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.
    *   Logfire spans are used to monitor the tool's execution <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
    *   The raw JSON response from the API is formatted into a human-readable string for the LLM to reason about <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
6.  **Running the Agent**: The agent is run by calling `agent.run()` with a prompt and dependencies <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. A debug library shows the entire history of tool calls and responses <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.

### Demonstration
The web search agent successfully finds articles related to "React 19" using a [[Working with local large language models | local large language model]] (Quen 2.5 coder 32B via Ollama) <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. The output includes direct links to the articles and the debug output shows the complete interaction history <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.

## Advanced Features: Streamlit UI Integration
Pydantic AI can be integrated with UIs like Streamlit to provide a more interactive experience <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>.

*   **Chat History**: The Streamlit version demonstrates persistent chat history, allowing for multi-turn conversations <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>. This involves passing the entire message history to the agent's `run` function <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>.
*   **Text Streaming**: The LLM's output can be streamed in real-time, showing a typewriter-style effect <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. (Note: Streaming with Ollama and Pydantic AI might have compatibility limitations at present, using GPT-4o for this demo) <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>.

The Streamlit UI version successfully maintains conversation history and responds to follow-up questions, demonstrating the agent's ability to retain context <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.

## Conclusion
Pydantic AI represents a significant step forward in building production-grade [[AI agents and their development | AI agents]] <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>. Its emphasis on crucial but often overlooked features like robust validation, context management through dependency injection, comprehensive testing tools, and detailed logging makes it a powerful framework for developing enterprise-level [[AI agents and their development | AI agents]] <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>. Understanding these features and how to leverage them is essential for developers working with [[AI agents and their development | AI agents]] <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.