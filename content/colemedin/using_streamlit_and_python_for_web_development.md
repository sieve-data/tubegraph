---
title: Using Streamlit and Python for Web Development
videoId: JyolNYRbAcs
---

From: [[colemedin]] <br/> 

Developing user interfaces for AI agents often requires a robust frontend that can interact with the backend in a clean and simple way <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>. While [[setting_up_ai_agents_with_langchain_and_streamlit | n8n]] offers a chat widget, more advanced user experiences typically necessitate a custom frontend <a class="yt-timestamp" data-t="00:28:44">[00:28:44]</a>. This article details how to use Streamlit, Claude, and Supabase to create powerful and secure interfaces for AI agents without extensive manual coding <a class="yt-timestamp" data-t="00:36:03">[00:36:03]</a>.

## The Streamlit, Claude, and Supabase Combo

This combination allows for the rapid creation and deployment of secure AI agent interfaces <a class="yt-timestamp" data-t="00:43:08">[00:43:08]</a>.
*   **Streamlit** is a Python package that simplifies website building, eliminating the need for JavaScript <a class="yt-timestamp" data-t="01:19:54">[01:19:54]</a>.
*   **Claude** excels at generating Streamlit code, making the development process highly efficient <a class="yt-timestamp" data-t="01:27:38">[01:27:38]</a>.
*   **Supabase** provides easy authentication and can also be used for other backend functions like chat memory and RAG (Retrieval Augmented Generation) for [[setting_up_ai_agents_with_langchain_and_streamlit | n8n agents]] <a class="yt-timestamp" data-t="01:38:09">[01:38:09]</a>.

## Building a Basic Streamlit Interface

The process begins by using Claude to generate a basic Streamlit application for an AI agent <a class="yt-timestamp" data-t="01:47:04">[01:47:04]</a>.

### Prompting Claude for the Basic App
To create the initial Streamlit app, Claude is prompted with specific requirements for the chat interface, including how to interact with the LLM (Large Language Model) via a webhook <a class="yt-timestamp" data-t="02:11:03">[02:11:03]</a>.
Key prompt details include:
*   Specifying a chat interface to communicate with an LLM <a class="yt-timestamp" data-t="02:34:02">[02:34:02]</a>.
*   Defining the POST request to the webhook, requiring `session ID` (for chat history) and `chat input` (user prompt) in the payload <a class="yt-timestamp" data-t="03:07:07">[03:07:07]</a>.
*   Indicating that the LLM's response is contained within an `output` key in the JSON response <a class="yt-timestamp" data-t="03:33:04">[03:33:04]</a>.
*   Including a basic hardcoded bearer token for temporary protection, though not recommended for production <a class="yt-timestamp" data-t="02:50:23">[02:50:23]</a>.

### Generated Streamlit Code Structure
Claude quickly generates the Python code, which includes:
*   Placeholders for the webhook URL and bearer token to be filled in <a class="yt-timestamp" data-t="03:55:03">[03:55:03]</a>.
*   A function to generate a random session ID for chat memory <a class="yt-timestamp" data-t="04:02:07">[04:02:07]</a>.
*   A function to send requests to the LLM and retrieve responses, adhering to the specified headers and `output` key <a class="yt-timestamp" data-t="04:04:09">[04:04:09]</a>.
*   A main function setting up the Streamlit user interface with a chat input and displaying responses from the LLM <a class="yt-timestamp" data-t="04:15:02">[04:15:02]</a>.

### Integrating with [[setting_up_ai_agents_using_python | n8n]]
To make the Streamlit frontend communicate with an [[setting_up_ai_agents_with_langchain_and_streamlit | n8n]] agent, specific configurations are needed:
1.  **Webhook Trigger:** Add a "Web Hook" trigger node at the start of the [[setting_up_ai_agents_with_langchain_and_streamlit | n8n]] workflow, alongside the existing "When Chat Message Received" trigger <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>.
2.  **Respond to Web Hook:** Add a "Respond to Web Hook" node at the very end of the workflow, after the tools agent, to return the LLM's output <a class="yt-timestamp" data-t="05:38:06">[05:38:06]</a>.
3.  **Webhook Configuration:**
    *   The production URL of the webhook becomes active when the [[setting_up_ai_agents_with_langchain_and_streamlit | n8n]] workflow is active <a class="yt-timestamp" data-t="05:56:06">[05:56:06]</a>.
    *   For basic authentication, select "Header Auth" with the credential name `Authorization` and a value of `Bearer` followed by your token <a class="yt-timestamp" data-t="06:14:04">[06:14:04]</a>.
    *   Set the "Respond" option from "Immediately" to "Using Respond to Webhook Node" <a class="yt-timestamp" data-t="06:57:07">[06:57:07]</a>.
4.  **Payload Parameters:** Ensure the [[setting_up_ai_agents_with_langchain_and_streamlit | n8n]] workflow processes `json.body.chat input` and `json.body.session ID` from the webhook payload, allowing the agent to handle chat history and user prompts <a class="yt-timestamp" data-t="07:33:04">[07:33:04]</a>.

### Running and Testing the Streamlit App
After filling in the webhook URL and bearer token in the Python script, the Streamlit application can be run using `streamlit run [script_name].py` <a class="yt-timestamp" data-t="09:53:08">[09:53:08]</a>. This immediately opens the chat widget in the browser, allowing interaction with the [[setting_up_ai_agents_with_langchain_and_streamlit | n8n]] agent and demonstrating its functionality, such as a RAG agent processing documents <a class="yt-timestamp" data-t="10:07:05">[10:07:05]</a>.

## Adding Supabase Authentication

To enhance security and robustness, Supabase authentication is integrated into both the Streamlit frontend and the [[setting_up_ai_agents_with_langchain_and_streamlit | n8n]] backend <a class="yt-timestamp" data-t="10:37:05">[10:37:05]</a>.

### Prompting Claude for Supabase Integration
Claude is prompted to update the Streamlit app to include Supabase authentication <a class="yt-timestamp" data-t="11:07:07">[11:07:07]</a>. Important instructions for Claude include:
*   Implementing both login and signup functionalities <a class="yt-timestamp" data-t="11:11:03">[11:11:03]</a>.
*   Using the user's Supabase token as the bearer token for the webhook <a class="yt-timestamp" data-t="11:19:07">[11:19:07]</a>. This allows [[setting_up_ai_agents_with_langchain_and_streamlit | n8n]] to verify the token and retrieve user information <a class="yt-timestamp" data-t="11:37:08">[11:37:08]</a>.
*   Displaying user information like the email in a sidebar <a class="yt-timestamp" data-t="11:57:07">[11:57:07]</a>.
*   Explicitly advising against using deprecated Streamlit features to prevent hallucinations <a class="yt-timestamp" data-t="12:04:09">[12:04:09]</a>.

### Updating the [[setting_up_ai_agents_with_langchain_and_streamlit | n8n]] Workflow for Supabase Auth
The [[setting_up_ai_agents_with_langchain_and_streamlit | n8n]] workflow requires adjustments to handle Supabase-based authentication:
1.  **Disable Webhook Authentication:** Turn off the authentication setting in the "Web Hook" trigger node in [[setting_up_ai_agents_with_langchain_and_streamlit | n8n]] <a class="yt-timestamp" data-t="13:30:00">[13:30:00]</a>.
2.  **Retrieve Supabase Credentials:** Obtain your Supabase project URL and API keys (service role secret and anonymous public key) from the API settings in your Supabase project <a class="yt-timestamp" data-t="13:47:04">[13:47:04]</a>.
3.  **HTTP Request for User Verification:** Add an HTTP Request node after the webhook trigger to verify the user's Supabase bearer token:
    *   Set the URL to `[your_supabase_project_url]/auth/v1/user` (a GET request) <a class="yt-timestamp" data-t="15:19:08">[15:19:08]</a>.
    *   Include two headers:
        *   `apiKey`: Set to your **secret** Supabase API key <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a>.
        *   `Authorization`: Set to `json.headers.authorization` to use the bearer token passed from the frontend <a class="yt-timestamp" data-t="15:01:00">[15:01:00]</a>.
    *   This request returns a user object if the token is valid <a class="yt-timestamp" data-t="15:27:07">[15:27:07]</a>.
4.  **Conditional Authentication Check:** Use an If statement to check for the presence of an `email` attribute in the returned user object; if present, authentication is successful <a class="yt-timestamp" data-t="15:41:03">[15:41:03]</a>. If not, return an error <a class="yt-timestamp" data-t="15:58:08">[15:58:08]</a>.

### Updating and Testing the Streamlit App with Authentication
The Streamlit script is updated with the new code from Claude, filling in placeholders for the Supabase URL and anonymous authentication key, as well as the [[setting_up_ai_agents_with_langchain_and_streamlit | n8n]] webhook URL <a class="yt-timestamp" data-t="17:21:05">[17:21:05]</a>.
After addressing minor hallucinations (e.g., deprecated Streamlit features), the app presents a login/signup interface <a class="yt-timestamp" data-t="18:37:00">[18:37:00]</a>. Upon successful login, the user's email and session ID are displayed, and the chat interface becomes accessible, now with secure Supabase-verified interactions with the [[setting_up_ai_agents_with_langchain_and_streamlit | n8n]] agent <a class="yt-timestamp" data-t="19:27:02">[19:27:02]</a>.

This robust setup provides a secure and functional frontend for [[setting_up_ai_agents_with_langchain_and_streamlit | n8n]] AI agents, built efficiently with Streamlit, Claude, and Supabase <a class="yt-timestamp" data-t="19:54:02">[19:54:02]</a>.