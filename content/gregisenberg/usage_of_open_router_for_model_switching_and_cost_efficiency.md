---
title: Usage of Open Router for model switching and cost efficiency
videoId: 9YPebrSjskU
---

From: [[gregisenberg]] <br/> 

Open Router is a service that allows developers to easily connect to and switch between various Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>. It integrates with over 300 models <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>, providing developers with flexibility in their [[aidriven_scalable_business_models | AI-driven app development]] <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## Key Benefits

### Seamless Model Switching
Open Router's primary advantage is its ability to swap out LLM models with just a single line of code, typically a string or piece of text <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>. This means a developer can easily test different models like Gemini, Claude, or OpenAI without significant code changes <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>. This flexibility is highly beneficial during the development phase for evaluating model responses and performance <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>.

### Cost Efficiency and Visibility
The service displays the price points of various models <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>, which is crucial for managing development costs. While there is a fee for using Open Router, its benefit in terms of development speed and the ability to compare costs makes it worthwhile <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>. By pulling data directly from Open Router, developers can see the total tokens consumed (prompt and completion tokens) and the associated cost for each LLM call <a class="yt-timestamp" data-t="00:45:56">[00:45:56]</a>. This allows for real-time monitoring of expenses during the testing and development phases <a class="yt-timestamp" data-t="00:48:08">[00:48:08]</a>.

It also provides context window sizes for different models, such as Claude 3.5 supporting 200,000 tokens and Gemini supporting 1 million tokens, helping developers make informed decisions based on the required [[understanding_model_context_protocol_mcp | model context]] <a class="yt-timestamp" data-t="00:47:58">[00:47:58]</a>.

## Implementation with Cursor

Chris utilizes Cursor for native iOS development <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>, and his integration of Open Router highlights several key techniques:

*   **Initial Prompting**: To integrate Open Router, Chris asks Cursor to make the chat functionality, which was initially hardcoded, functional. He specifically requests the use of Open Router for quick model swapping and the addition of a UI setting (like a top-right toggle) to switch between models (e.g., GPT or Claude) <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>.
*   **Leveraging Documentation (`@docs`)**: A significant tip is to feed Open Router's documentation directly into Cursor using the `@docs` feature <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>. This allows Cursor to index the entire documentation, providing it with the necessary context for API calls and reducing hallucinations <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>. This is especially useful as AI APIs are constantly changing <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a>.
*   **Tool/Function Calling**: Chris uses Open Router's tool/function calling feature to enable the LLM to access specific local functions or "tools" within the app <a class="yt-timestamp" data-t="00:36:46">[00:36:46]</a>. For example, he created tools to `get transactions for a specific date range` and `get the user's current budget` <a class="yt-timestamp" data-t="00:40:21">[00:40:21]</a>. This allows the LLM to dynamically retrieve relevant data (e.g., only transactions for the last week) instead of feeding it large, costly datasets every time <a class="yt-timestamp" data-t="00:35:56">[00:35:56]</a>. This process of using tools to gather context before answering is a foundational element of building AI agents <a class="yt-timestamp" data-t="00:37:01">[00:37:01]</a>.
*   **Displaying Costs and Tokens**: Chris further enhanced the app to display the total tokens consumed and the cost of each conversation right below the messages <a class="yt-timestamp" data-t="00:45:52">[00:45:52]</a>. He achieved this by prompting Cursor to make a call to Open Router's generation endpoint to pull run data, including cost and tokens <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>.

## Limitations and Security Considerations

While powerful, it's important to note some limitations and security concerns:

*   **Front-end API Keys**: For demo and speed purposes, API keys were sometimes hardcoded into the front-end of the application <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>. This is a significant security risk, as keys should ideally reside in the backend <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>. Cursor might place these keys in the front end, which can lead to rapid credit consumption if a bot discovers them <a class="yt-timestamp" data-t="00:55:28">[00:55:28]</a>.
*   **Model Compatibility**: Not all Open Router models consistently support advanced features like tool and function calling, requiring some manual selection or hardcoding of compatible models <a class="yt-timestamp" data-t="00:47:36">[00:47:36]</a>.
*   **Learning Curve for Non-Developers**: While AI tools like Cursor are accelerating development, non-developers should be cautious. Tools like Replit or Lovable might offer more guardrails <a class="yt-timestamp" data-t="00:55:57">[00:55:57]</a>. Learning programming basics is highly recommended to effectively use these tools and avoid potential pitfalls <a class="yt-timestamp" data-t="00:56:05">[00:56:05]</a>.