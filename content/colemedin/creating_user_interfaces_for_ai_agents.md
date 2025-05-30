---
title: Creating User Interfaces for AI Agents
videoId: JyolNYRbAcs
---

From: [[colemedin]] <br/> 

While n8n is widely used to [[building_ai_agents | build AI agents]] without writing code, it often requires a custom frontend for user interaction beyond its default chat widget <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. This article details a method for [[creating_custom_frontends_for_ai_agents | creating custom frontends for AI agents]] using a powerful combination of tools, allowing for rapid development and deployment <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This approach avoids needing a full React or Next.js project and minimizes manual coding by leveraging large language models (LLMs) <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## Recommended Technology Stack

The recommended combination for [[building_and_deploying_custom_ai_front_ends | building and deploying custom AI front ends]] is:

*   **Claude**: An LLM used to generate the frontend code <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Claude excels at coding with Streamlit <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **Streamlit**: A Python package that simplifies website creation without requiring JavaScript <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   **Supabase**: Used for easy authentication and often already utilized with n8n for features like chat memory and RAG (Retrieval Augmented Generation) <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

## Building a Basic Streamlit Interface

The first step involves using Claude to generate a basic Streamlit interface for an n8n [[understanding_ai_agents | agent]] without advanced authentication <a class="yt-timestamp" data-t="01:50:50">[01:50:50]</a>.

1.  **Initial Prompt to Claude**: Provide a prompt to Claude asking it to create a basic Streamlit application with a chat interface to communicate with an LLM <a class="yt-timestamp" data-t="02:33:00">[02:33:00]</a>. It's crucial to specify:
    *   The structure of chatting with the LLM.
    *   When and how to use the webhook <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>.
    *   The need for basic, hardcoded bearer token authentication for initial protection (not for production) <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.
    *   Specific payload requirements for the POST request to the webhook, including a `session ID` (for chat history) and `chat input` (user prompt) <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>.
    *   The expected response format, particularly an `output` key from the JSON response that contains the LLM's reply <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>.
2.  **Claude's Code Generation**: Claude quickly generates the Python code, including a function to send requests to the LLM and a main function to set up the Streamlit user interface <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>. It generates a random `session ID` for chat memory <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>.
3.  **Filling Placeholders**: The generated code will have placeholders for the webhook URL and bearer token, which need to be filled in a code editor like Visual Studio Code <a class="yt-timestamp" data-t="03:55:00">[03:55:55]</a>.
4.  **Running the Streamlit App**: After installing necessary Python packages (e.g., via `pip install -r requirements.txt`), the app can be run using `streamlit run [script_name].py` <a class="yt-timestamp" data-t="09:28:00">[09:28:00]</a>.

## n8n Workflow Configuration for Frontend Integration

To make the n8n [[understanding_ai_agents | agent]] accessible to the Streamlit frontend via a webhook:

1.  **Webhook Trigger**: Add a "Webhook" trigger node at the start of your n8n workflow, in addition to the "When Chat Message Received" trigger (which provides the internal chat widget) <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>.
2.  **Respond to Webhook**: Add a "Respond to Webhook" node at the very end of the workflow, after the [[creating_tools_and_dependencies_for_ai_agents | tools agent]] <a class="yt-timestamp" data-t="05:38:00">[05:38:00]</a>. This node automatically returns the output items from the previous node, including the LLM's response <a class="yt-timestamp" data-t="07:04:00">[07:04:00]</a>.
3.  **Webhook Node Settings**:
    *   **Production URL**: This URL (controlled by the path in the Webhook node) is what you'll use in your Python code <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>.
    *   **Authentication**: Select "Header Auth" and create a new credential. The name must be `Authorization`, and the value `Bearer [YourTokenName]` <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>. This is for basic authentication and should not be used in production <a class="yt-timestamp" data-t="06:18:00">[06:18:00]</a>.
    *   **Respond**: Change from "Immediately" to "Using Respond to Webhook Node" <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>.
4.  **Payload Handling**: Ensure the n8n workflow can correctly process the `session ID` and `chat input` from the webhook payload. For example, in an "Edit Fields" node, you might define the `chat input` as `json.body.chat_input` and `session ID` similarly, allowing the workflow to work with both the chat widget and webhook triggers <a class="yt-timestamp" data-t="07:33:00">[07:33:00]</a>.

## Adding Supabase Authentication

To make the interface more robust and secure, Supabase authentication is integrated.

1.  **Prompting Claude for Supabase Integration**: Update the Claude prompt to:
    *   Instruct it to use Supabase for authentication <a class="yt-timestamp" data-t="10:07:00">[10:07:00]</a>.
    *   Specify the creation of both login and signup tabs <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>.
    *   Crucially, tell it to use the user's Supabase token as the bearer token for the webhook <a class="yt-timestamp" data-t="11:19:00">[11:19:00]</a>. This token is dynamically generated via the Supabase Python library upon successful sign-in <a class="yt-timestamp" data-t="11:28:00">[11:28:00]</a>.
    *   Request the display of user information, like the email, in a left side panel <a class="yt-timestamp" data-t="11:57:00">[11:57:00]</a>.
    *   Add a note to prevent Claude from using deprecated features <a class="yt-timestamp" data-t="12:04:00">[12:04:00]</a>.
2.  **Claude's Enhanced Code**: Claude generates a more robust Streamlit application. The `send_message_to_llm` function now includes a `token` parameter, dynamically retrieved from the user's session state after sign-in <a class="yt-timestamp" data-t="12:25:00">[12:25:00]</a>.
3.  **Filling Supabase Placeholders**: The updated Python code will require your Supabase project URL and Anonymous authentication key, obtained from your Supabase API settings <a class="yt-timestamp" data-t="17:21:00">[17:21:00]</a>.

## n8n Workflow Configuration for Supabase Authentication

To verify the Supabase token in the n8n workflow:

1.  **Disable Webhook Authentication**: Turn off the basic authentication on the Webhook trigger node, as authentication will now be handled manually within the workflow <a class="yt-timestamp" data-t="13:30:00">[13:30:00]</a>.
2.  **Supabase API Keys**:
    *   **Project URL**: Found in Supabase Project Settings > API > Configuration <a class="yt-timestamp" data-t="13:59:00">[13:59:00]</a>.
    *   **Service Role Secret (Private API Key)**: This secret key should be used securely (e.g., via AWS Secrets Manager for production) <a class="yt-timestamp" data-t="14:10:00">[14:10:00]</a>.
    *   **Anonymous API Key (Public)**: This key is safe to share if row-level security is properly defined in your Supabase tables <a class="yt-timestamp" data-t="14:19:00">[14:19:00]</a>.
3.  **HTTP Request Node for Verification**:
    *   Add an "HTTP Request" node immediately after the Webhook trigger <a class="yt-timestamp" data-t="14:40:00">[14:40:00]</a>.
    *   **Headers**:
        *   `apiKey`: Set this to your **Service Role Secret** <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a>.
        *   `Authorization`: Set this to `json.headers.authorization` to fetch the Supabase token passed from the frontend <a class="yt-timestamp" data-t="15:01:00">[15:01:00]</a>.
    *   **URL**: Use a GET request to `[YourProjectURL]/auth/v1/user` <a class="yt-timestamp" data-t="15:19:00">[15:19:00]</a>. This endpoint returns a valid user object if the token is legitimate <a class="yt-timestamp" data-t="15:27:00">[15:27:00]</a>.
4.  **Conditional Logic for Authentication**: Use an "If" statement (or similar logic) to check if a valid user object is returned (e.g., by checking for an `email` attribute) <a class="yt-timestamp" data-t="15:41:00">[15:41:00]</a>. If valid, continue the workflow; otherwise, return an error <a class="yt-timestamp" data-t="15:58:00">[15:58:00]</a>.

## Iteration and Testing

Building with Claude is an iterative process. Claude might initially "hallucinate" or use deprecated features (e.g., `experimental_rerun` in Streamlit) <a class="yt-timestamp" data-t="18:33:00">[18:33:00]</a>. Provide corrective prompts (e.g., "don't include experimental stuff") to guide Claude to a functional and robust solution <a class="yt-timestamp" data-t="18:48:00">[18:48:00]</a>.

Once the code is refined and deployed, the Streamlit frontend will present a login/signup interface. After successful authentication, it will display the user's email and session ID, enabling secure interaction with the n8n [[understanding_ai_agents | AI agent]] <a class="yt-timestamp" data-t="19:27:00">[19:27:00]</a>. This setup provides a strong foundation for [[customizing_ai_agent_interfaces | customizing AI agent interfaces]] and [[developing_ai_agents_without_coding | developing AI agents without coding]] <a class="yt-timestamp" data-t="19:52:00">[19:52:00]</a>.