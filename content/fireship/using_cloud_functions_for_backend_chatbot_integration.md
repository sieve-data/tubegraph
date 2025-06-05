---
title: Using cloud functions for backend chatbot integration
videoId: 0NXqwT3Y09E
---

From: [[fireship]] <br/> 

Despite the initial hype cycle, chatbots have largely failed to live up to their lofty expectations of eliminating millions of call center jobs or replacing lawyers by 2019, having passed the peak of their hype cycle and currently residing in the trough of disillusionment <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. However, conversational experiences can be very effective when tailored to a specific business need <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

This article outlines how to [[building_a_chatbot_using_dialogflow | build a chatbot]] from scratch using [[using_dialogflow_for_chatbot_development | Dialogflow]], Node.js, and [[cloud_functions_and_integration_with_firebase | Cloud Functions]] <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. The goal is to create a simple chatbot that can collect information from a user and save it permanently in a backend database <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Core Technologies

*   **[[using_dialogflow_for_chatbot_development | Dialogflow]]**: Powers the natural language processing (NLP) and artificial intelligence, acting as a tool for [[building_a_chatbot_using_dialogflow | building virtual agents]] that intelligently respond to user input (voice or text) <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   **Node.js**: Used as the backend server for interacting with the [[using_dialogflow_for_chatbot_development | Dialogflow]] API <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   **[[cloud_functions_and_integration_with_firebase | Firebase Cloud Functions]]**: Serverless functions used for handling backend logic and integration with [[using_dialogflow_for_chatbot_development | Dialogflow]] <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
*   **Angular**: Used for the frontend UI in this demo, but any frontend framework can be used <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

## Chatbot Architecture

The architecture involves a frontend application, a gateway [[cloud_functions_and_integration_with_firebase | Cloud Function]], [[using_dialogflow_for_chatbot_development | Dialogflow]], and a fulfillment webhook [[cloud_functions_and_integration_with_firebase | Cloud Function]] <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

### Frontend Application
The frontend application (e.g., [[building_a_chatbot_with_angular | Angular]]) is where the user interacts with the bot <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. It makes API calls to the gateway [[cloud_functions_and_integration_with_firebase | Cloud Function]] <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

### Gateway Cloud Function
This [[cloud_functions_and_integration_with_firebase | function]] serves as a proxy to make secure calls to the [[using_dialogflow_for_chatbot_development | Dialogflow]] API <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   It receives the user's message via an HTTP call from the frontend <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
*   It passes this message to the [[using_dialogflow_for_chatbot_development | Dialogflow]] bot <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   It sends the bot's response back down to the client <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   It utilizes a service account private key (stored securely and excluded from public repositories) to initialize [[firebase_cloud_messaging_services | Firebase]] Admin for [[using_dialogflow_for_chatbot_development | Dialogflow]] interaction <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   It expects `query input` (user's text or audio) and a `session ID` (unique per user to track conversation context) <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
*   The `detect intent` method is called with the session and query input to get a response from the chatbot, extracting the `fulfillment text` to display to the user <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

### Fulfillment Webhook Cloud Function
When a conversation concludes, or a user's intention is fulfilled, [[using_dialogflow_for_chatbot_development | Dialogflow]] sends a webhook to a separate [[cloud_functions_and_integration_with_firebase | Cloud Function]] <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   This [[cloud_functions_and_integration_with_firebase | function]] handles additional backend work, such as updating a database or making a third-party API call <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   It dynamically computes the bot's response based on the backend operations <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   This single [[cloud_functions_and_integration_with_firebase | function]] can handle multiple intents that require webhook fulfillment <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
*   For a custom intent like "update profile," it can update a backend database (e.g., Firestore) with user-provided parameters <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   After backend work, a message is added to the agent, which the user sees as the bot's response <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
*   Intents are mapped to functions within the webhook using a JavaScript map <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.

## Setting up Dialogflow

To begin, a [[firebase_cloud_messaging_services | Firebase]] project is needed, followed by navigating to the [[using_dialogflow_for_chatbot_development | Dialogflow]] console <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

1.  **Create a New Agent**: An agent represents an individual chatbot that translates user input into structured data <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
2.  **Define Intents**: Intents determine the user's intention <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
    *   **Context**: A mechanism for passing data between intents (not covered in detail) <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
    *   **Events**: Optional, allows triggering an intent programmatically without manual user input, useful for onboarding <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
    *   **Training Phrases**: Short user phrases that trigger the intent; the machine learning algorithm uses NLP to find similar phrases <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. More data improves accuracy <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
    *   **Action and Parameters**:
        *   **Action Name**: Follows a reverse domain name convention (e.g., `com.example.updateProfile`) <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
        *   **Parameters**: Collect specific pieces of data required to fulfill the intent <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. These can be optional or required <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
        *   **Entity**: Represents the data type, allowing for automatic validation <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. Custom entities can be created <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
        *   **Prompt**: What the agent asks the user to collect required data <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
    *   **Fulfillment**:
        *   **Defined Response**: Simple responses defined directly in the [[using_dialogflow_for_chatbot_development | Dialogflow]] console if no backend work is needed <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
        *   **Webhook**: Used when backend work (e.g., database update, API call) is required, allowing custom code to format dynamic responses <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

## Setting up Cloud Functions

After defining intents, [[setting_up_firebase_cloud_functions | Cloud Functions]] are initialized, typically with JavaScript <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

1.  **Install Dependencies**:
    *   `dialogflow`: The [[using_dialogflow_for_chatbot_development | Dialogflow]] API client <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
    *   `cors`: Allows requests from the frontend application <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
    *   `dialogflow-fulfillment`: Specific library for webhook fulfillment <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
    *   `actions-on-google` (if applicable) <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.
2.  **Service Account Setup**:
    *   Generate a new private key JSON file from the [[firebase_cloud_messaging_services | Firebase]] console (Settings > Service Account) <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
    *   Download this file into the functions directory <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
    *   Keep this file secure and add it to `.gitignore` for public repositories <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
3.  **Implement Gateway Function**: This HTTP [[cloud_functions_and_integration_with_firebase | function]] (`dialogflowGateway`) is wrapped with `cors` <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. It initializes the [[using_dialogflow_for_chatbot_development | Dialogflow]] `session client` with the service account and processes user input <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
4.  **Implement Webhook Function**: This HTTP [[cloud_functions_and_integration_with_firebase | function]] is not wrapped in `cors` as it's not called directly from the frontend <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. It initializes a `webhook client` and contains logic to handle different intents by mapping them to specific functions (e.g., updating a database) <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.

### Backend Interaction Example
When a user types "update my profile," the bot will respond by asking for parameters (e.g., "What is your preferred name?") <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. As the user provides information, the bot continues to collect parameters until the intent is fulfilled, at which point the fulfillment webhook is triggered <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

## Frontend UI with Angular

For the frontend, an [[building_a_chatbot_with_angular | Angular]] application is used with the `Nebula` theme, specifically its chat UI module, to quickly build the interface <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

*   The `NbChatComponent` acts as a wrapper for messages and the input form <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.
*   `NbChatMessageComponent` is used to display messages from both the bot and the user, with options for text, reply status, date, and avatar <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.
*   A loading spinner can be shown using Nebula's `spinner directive` while the bot is responding <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.
*   The `NbChatForm` handles user input and triggers a `send` event <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.
*   Angular's `HttpClient` makes HTTP POST requests to the `dialogflowGateway` [[cloud_functions_and_integration_with_firebase | function]] <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.
*   The frontend generates a `session ID` (e.g., a random string or user ID) to maintain conversation context <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.
*   When a user sends a message, it's added to the chat, the loading state is set, an HTTP POST request containing the `session ID` and `query input` (user text) is sent, and the `fulfillment text` from the response is displayed <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.

By combining [[building_a_chatbot_with_angular | Angular]] with the Nebula theme, [[using_dialogflow_for_chatbot_development | Dialogflow]], and [[cloud_functions_and_integration_with_firebase | Firebase Cloud Functions]], [[building a realtime chat app with Firebase | building a real-time chat app with Firebase]] with backend integration for dynamic responses becomes extremely simple <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.