---
title: Web search agent development with Brave API
videoId: pC17ge_2n0Q
---

From: [[colemedin]] <br/> 

Developing web search agents is crucial for connecting [[ai_agents_and_their_development | AI agents]] to real-world information <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. The Brave Search API is highlighted as one of the best and free options for web browsing <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

## Pydantic AI for Production-Grade Agents

Pydantic AI is an open-source Python agent framework designed to simplify the development of production-grade [[ai_agents_and_their_development | AI agents]] <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. It addresses common shortcomings in newer frameworks by implementing essential features that are often overlooked <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

Key features of Pydantic AI that are vital for robust agent development include:
*   Context management <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>
*   Error handling and retry logic <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>
*   Testing and evaluation capabilities <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>
*   Logging and monitoring <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>
*   Large Language Model (LLM) output validation <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>

Pydantic AI leverages the core Pydantic library for its validation layer, ensuring that expected inputs and outputs are received, similar to how FastAPI utilizes Pydantic for endpoint validation <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This focus on validation is a key differentiator, as many other frameworks neglect structured output validation, LLM testing, or proper tool invocation <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

Pydantic AI is model-agnostic, supporting various providers like OpenAI, Anthropic, and Google's Gemini, and allows for custom provider additions <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. It also provides type-safe dependency injection for managing context, such as database connections and API keys, which is critical for testing and evaluation <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

## Prerequisites for Building a Web Search Agent

To build the web search agent demonstrated, the following prerequisites are needed <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>:
*   Python <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>
*   An OpenAI API key (for GPT models) <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>
*   Ollama (for running local LLMs) <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>
*   A Brave Search API key <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>

## Agent Implementation with Pydantic AI

The development starts with setting up the Python environment and configuring API keys in a `.env` file <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

### LLM Configuration
The agent can be configured to use either OpenAI's models (e.g., GPT) or local LLMs via Ollama <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. For Ollama, a custom asynchronous OpenAI instance is created, overriding the base URL to point to the local Ollama server <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.

### Dependencies and Context Management
Pydantic AI's dependency injection system allows for managing essential resources like the HTTP client and the Brave API key <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. This prevents sensitive credentials from being exposed to the LLM directly, while still making them available to tools <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

```python
# Example: Defining dependencies
# client (HTTP client) and brave_api_key (Brave API Key)
# These are accessible by tools but not passed to the LLM directly
```

### Defining the Agent
The agent is defined with a model (e.g., GPT-4o or a local Ollama model), a system prompt (including the current time for fresh searches), expected dependencies, and `model_retry` logic for handling errors like overloads <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

```python
# Example: Agent definition
# agent = PydanticAgent(model=llm_model, system_prompt="...", dependencies=...)
```

### Implementing the Web Search Tool (`search_web`)
A tool to search the web is defined using a Pydantic AI decorator (`@agent.tool`) <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.
*   **Parameters:** The tool function accepts `context` (containing dependencies) and `query` (defined by the LLM) <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   **Docstring:** A crucial docstring informs the LLM when and how to use the tool and what arguments to provide <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.
*   **API Call:** It sets up HTTP headers and uses the `client` from the context to make an asynchronous call to the Brave Search API <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.
*   **Logging:** A Logfire span (`logfire.span(...)`) is used to segment and monitor the tool's execution, aiding debugging <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.
*   **Result Formatting:** The raw JSON response from Brave API is massaged into a structured string that the LLM can easily reason about <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.

```python
# Example: search_web tool
# @agent.tool
# async def search_web(context: ..., query: str) -> str:
#     """Searches the web for the given query."""
#     # ... API call logic ...
#     return formatted_results
```

### Running the Agent
The agent is run by calling `agent.run()` with the user's prompt and the defined dependencies <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. The result can then be printed, and Pydantic AI's debug library can show the entire history of tool calls and LLM interactions <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.

## Demo and Execution
The web search agent can be executed from the command line, and it will use the configured LLM (e.g., a local Ollama model like "Quen 2.5 Coder 32b" or GPT-4o) to search the web based on the prompt <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.

An example query for "articles talking about the new release of React 19" demonstrates the agent's ability to identify relevant articles and return their links <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>. The debug output provides detailed insights into the tool calls and reasoning process <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

## Streamlit Integration for Enhanced Interaction

A more advanced version of the web search agent integrates with a Streamlit UI, providing [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | chat history]] and text streaming capabilities <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.

*   **Chat History:** The agent maintains conversation history by passing the entire message history to the `agent.run()` function, allowing for follow-up questions <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>.
*   **Text Streaming:** Text output from the LLM is streamed in real-time (typewriter style), eliminating the need to wait for the full response <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. (Note: Streaming with Ollama and Pydantic AI may not currently be supported <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>).
*   **UI Management:** Streamlit handles displaying chat history, user input, and managing the state of messages within the application <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>.

The Streamlit version demonstrates persistent chat, accurately responding to follow-up questions based on prior conversation <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>, and performing new web searches like "what is the net worth of Elon Musk" <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>.

## Conclusion

Pydantic AI is presented as a robust framework for [[ai_agents_and_their_development | AI agent development]], offering crucial features like validation, context management, testing, and error handling that are often overlooked in other tools <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>. Understanding these features and how to leverage them is essential for building production-grade, enterprise-level [[ai_agents_and_their_development | AI agents]] <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.