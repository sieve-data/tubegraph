---
title: Building a chatbot using Dialogflow
videoId: 0NXqwT3Y09E
---

From: [[fireship]] <br/> 

While chatbots in 2017 were hyped to eliminate jobs and replace forms, they largely failed to live up to expectations by 2019 <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>. However, [[understanding_natural_language_processing_with_chatbots | conversational experiences]] can be highly effective when tailored to specific business needs <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>. This guide demonstrates how to [[using_dialogflow_for_chatbot_development | build a chatbot from scratch]] using [[integrating_dialogflow_with_nodejs_and_angular | Dialogflow]], Node.js, and [[using_cloud_functions_for_backend_chatbot_integration | Cloud Functions]] <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a>.

The goal is to create a simple [[using_dialogflow_for_chatbot_development | chatbot]] that collects user information and saves it permanently in a backend database <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>.

## Core Technologies

*   **[[using_dialogflow_for_chatbot_development | Dialogflow]]**: Powers the [[understanding_natural_language_processing_with_chatbots | Natural Language Processing]] (NLP) or artificial intelligence, enabling the creation of virtual agents that intelligently respond to user input (voice or text) <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>.
*   **Node.js**: Used for backend integration and interacting with the [[integrating_dialogflow_with_nodejs_and_angular | Dialogflow]] API <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.
*   **[[using_cloud_functions_for_backend_chatbot_integration | Cloud Functions]]**: Serves as the backend for handling API calls and business logic <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>.
*   **[[building_a_chatbot_with_angular | Angular]]**: Utilized for the frontend user interface <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.
*   **[[building_a_realtime_chat_app_with_firebase | Firebase]]**: Provides project setup and backend services like Firestore and Cloud Functions <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.

## Chatbot Architecture

The system's architecture involves several components working together:

1.  **Frontend Application**: The user interacts with the bot here, built with [[building_a_chatbot_with_angular | Angular]] in this demo <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>.
2.  **Gateway [[using_cloud_functions_for_backend_chatbot_integration | Cloud Function]]**: Serves as a proxy to make secure calls to the [[integrating_dialogflow_with_nodejs_and_angular | Dialogflow]] API from the frontend <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>. User messages are passed from the frontend to this function via HTTP calls <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>.
3.  **[[integrating_dialogflow_with_nodejs_and_angular | Dialogflow]] Agent**: Processes the user's message, determines intent, and provides a response <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a>.
4.  **Webhook [[using_cloud_functions_for_backend_chatbot_integration | Cloud Function]]**: When a conversation finishes and the user's intention is fulfilled, [[integrating_dialogflow_with_nodejs_and_angular | Dialogflow]] sends a webhook to this separate function <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>. This function handles additional backend work, such as sending emails, processing payments, or updating a database <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.

## [[setting_up_dialogflow_agents_and_intents | Setting up Dialogflow Agents and Intents]]

To begin, you need a [[building_a_realtime_chat_app_with_firebase | Firebase]] project and access to the [[integrating_dialogflow_with_nodejs_and_angular | Dialogflow]] console <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>.

### Creating an Agent

An agent represents an individual [[using_dialogflow_for_chatbot_development | chatbot]], which translates user input (text or speech) into structured data for your application <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>. Think of it as a virtual call center with a trained customer service representative <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>.

### Defining Intents

When a user provides input, the agent determines their *intention* <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>. For example, to allow users to update their profile information, a new intent named "update profile" can be created <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>.

Key options when defining an intent:

*   **Context**: A mechanism for passing data between intents (advanced topic not covered in this guide) <a class="yt-timestamp" data-t="03:15:00">[03:15:00]</a>.
*   **Events**: An optional way to trigger an intent programmatically without manual user input, useful for onboarding processes <a class="yt-timestamp" data-t="03:23:00">[03:23:00]</a>.
*   **Training Phrases**: Short user phrases that would trigger this intent. The machine learning algorithm uses [[understanding_natural_language_processing_with_chatbots | Natural Language Processing]] to identify similar phrases <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>.
*   **Action and Parameters**:
    *   **Action Name**: A good practice is to use a reverse domain name followed by the intent name (e.g., `com.example.updateProfile`) <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>.
    *   **Parameters**: Pieces of data the bot needs to collect to fulfill the intent <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>. These can be optional or required <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.
        *   **Entity**: Represents the type of data being collected, allowing [[integrating_dialogflow_with_nodejs_and_angular | Dialogflow]] to automatically validate it <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>. Custom entities can also be created <a class="yt-timestamp" data-t="04:39:00">[04:39:00]</a>.
        *   **Prompt**: The question the agent asks the user to collect the required data <a class="yt-timestamp" data-t="04:44:00">[04:44:00]</a>.

### Fulfillment

After all necessary data is collected, there are two ways to fulfill an intent:

*   **Direct Response**: Define a static response directly in the [[integrating_dialogflow_with_nodejs_and_angular | Dialogflow]] console if no additional backend work is needed <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>.
*   **Webhook**: For more complex scenarios like updating a database or making a third-party API call, use a webhook <a class="yt-timestamp" data-t="04:59:00">[04:59:00]</a>. This allows you to write custom backend code to dynamically format responses and handle business logic <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>.

[[integrating_dialogflow_with_nodejs_and_angular | Dialogflow]] offers built-in integrations for platforms like Facebook Messenger, Slack, Twitter, and Twilio <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>. A new "[[integrating_dialogflow_with_nodejs_and_angular | Dialogflow]] Phone Gateway" allows connection to a phone line <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>. For custom UI, direct interaction with the [[integrating_dialogflow_with_nodejs_and_angular | Dialogflow]] API via a Node.js backend is necessary <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>.

## Backend Integration with Node.js and [[using_cloud_functions_for_backend_chatbot_integration | Cloud Functions]]

Start by initializing [[using_cloud_functions_for_backend_chatbot_integration | Cloud Functions]] and installing necessary libraries: `dialogflow` (API client), `cors` (for frontend requests), and `dialogflow-fulfillment` (for webhooks) <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a>.

### Gateway Function (`dialogflowGateway`)

This secure gateway function allows the frontend to communicate with [[integrating_dialogflow_with_nodejs_and_angular | Dialogflow]] <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>.

1.  **Authentication**: A [[building_a_realtime_chat_app_with_firebase | Firebase]] service account private key (JSON file) is needed. Download it from the [[building_a_realtime_chat_app_with_firebase | Firebase]] console and keep it secure (add to `.gitignore`) <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>.
2.  **Function Setup**: Define an HTTP [[using_cloud_functions_for_backend_chatbot_integration | Cloud Function]] (e.g., `dialogflowGateway`) and wrap it with `cors` to enable cross-origin requests from the browser <a class="yt-timestamp" data-t="06:58:00">[06:58:00]</a>.
3.  **Request Parameters**: [[integrating_dialogflow_with_nodejs_and_angular | Dialogflow]] expects `queryInput` (the user's text or audio) and a `sessionID` (a unique ID per user to track conversation history) <a class="yt-timestamp" data-t="07:11:00">[07:11:00]</a>.
4.  **Detect Intent**: Initialize the session client with the service account and call `detectIntent` with the session and query input to get a response from the [[using_dialogflow_for_chatbot_development | chatbot]] <a class="yt-timestamp" data-t="07:26:00">[07:26:00]</a>.
5.  **Response**: The `queryResult` contains the `fulfillmentText` (the bot's response), which is sent back to the frontend <a class="yt-timestamp" data-t="07:52:00">[07:52:00]</a>.

### Webhook Function

This separate HTTP [[using_cloud_functions_for_backend_chatbot_integration | Cloud Function]] handles fulfillment and is not directly called from the frontend <a class="yt-timestamp" data-t="09:11:00">[09:11:00]</a>.

1.  **Initialization**: Initialize a `WebhookClient` instance using the request and response objects <a class="yt-timestamp" data-t="09:22:00">[09:22:00]</a>.
2.  **Intent Handling**: This function is called for *all* intents enabled for webhook fulfillment <a class="yt-timestamp" data-t="09:27:00">[09:27:00]</a>.
3.  **Backend Logic**: For custom intents (e.g., "update profile"), set up a function to update the backend database ([[building_a_realtime_chat_app_with_firebase | Firebase]] Firestore in this case) with the parameters passed by the user <a class="yt-timestamp" data-t="09:50:00">[09:50:00]</a>.
4.  **Agent Response**: After backend work is done, add a message to the agent that the user will see as the bot's response <a class="yt-timestamp" data-t="10:08:00">[10:08:00]</a>.
5.  **Mapping Intents**: Map different intent names to their corresponding handling functions using a JavaScript map <a class="yt-timestamp" data-t="10:16:00">[10:16:00]</a>.

After setting up both functions, deploy them using `firebase deploy --only functions` <a class="yt-timestamp" data-t="10:32:00">[10:32:00]</a>.

## Frontend Integration with [[building_a_chatbot_with_angular | Angular]]

To create the user interface for the [[using_dialogflow_for_chatbot_development | chatbot]], [[building_a_chatbot_with_angular | Angular]] is combined with the free "Nebular" theme <a class="yt-timestamp" data-t="10:45:00">[10:45:00]</a>. Nebular includes a full chat UI module <a class="yt-timestamp" data-t="10:53:00">[10:53:00]</a>.

1.  **Installation**: Install Nebular using `ng add @nebular/theme` <a class="yt-timestamp" data-t="10:57:00">[10:57:00]</a>.
2.  **Module Imports**: Import `NbChatModule` and `NbSpinnerModule` in your Angular `app.module.ts`, along with `HttpClientModule` from `@angular/common/http` <a class="yt-timestamp" data-t="11:06:00">[11:06:00]</a>.
3.  **Chatbot Component**: Create a new Angular component (e.g., `ChatbotComponent`) to encapsulate the chat logic <a class="yt-timestamp" data-t="11:21:00">[11:21:00]</a>.

### Template (`.html`)

Nebular's components simplify the UI:

*   `<nb-chat>`: A wrapper for messages and the input form <a class="yt-timestamp" data-t="11:33:00">[11:33:00]</a>.
*   `<nb-chat-message>`: Used to display individual messages from both the bot and the user, typically looped over using `ngFor` <a class="yt-timestamp" data-t="11:39:00">[11:39:00]</a>. Customize with inputs like `text`, `reply` (for user messages), `date`, and `avatar` <a class="yt-timestamp" data-t="11:48:00">[11:48:00]</a>. A loading spinner can be shown using `nbSpinner` while the bot is responding <a class="yt-timestamp" data-t="12:03:00">[12:03:00]</a>.
*   `<nb-chat-form>`: The input form with a `(send)` event that fires when the user clicks send or hits enter <a class="yt-timestamp" data-t="12:14:00">[12:14:00]</a>.

### Component Logic (`.ts`)

The component primarily uses Angular's `HttpClient` to make requests to the `dialogflowGateway` function <a class="yt-timestamp" data-t="12:22:00">[12:22:00]</a>.

*   **State Variables**:
    *   `messages`: An array to store chat messages <a class="yt-timestamp" data-t="12:33:00">[12:33:00]</a>.
    *   `loading`: A boolean to indicate if the bot is currently responding <a class="yt-timestamp" data-t="12:35:00">[12:35:00]</a>.
    *   `sessionID`: A randomly generated string unique to the user, passed to the backend for conversation context <a class="yt-timestamp" data-t="12:37:00">[12:37:00]</a>.
*   **Message Handling**:
    *   Methods to `addBotMessage` and `addUserMessage`, setting `reply: true` for user messages to handle styling <a class="yt-timestamp" data-t="12:44:00">[12:44:00]</a>.
    *   Initial bot message displayed when the app loads <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>.
*   **Sending Messages**:
    1.  When a user sends a message, add it to the `messages` array and set `loading` to `true` <a class="yt-timestamp" data-t="13:14:00">[13:14:00]</a>.
    2.  Make an HTTP POST request to the `dialogflowGateway` function URL <a class="yt-timestamp" data-t="13:21:00">[13:21:00]</a>.
    3.  The request body includes the `sessionID` and `queryInput` (containing the user's `text` and `languageCode`) <a class="yt-timestamp" data-t="13:31:00">[13:31:00]</a>.
    4.  Subscribe to the response. The `fulfillmentText` from the backend is the bot's next message <a class="yt-timestamp" data-t="13:46:00">[13:46:00]</a>.
    5.  Add the bot's message to the chat and set `loading` to `false` <a class="yt-timestamp" data-t="13:53:00">[13:53:00]</a>.

This combination of [[integrating_dialogflow_with_nodejs_and_angular | Angular]] and the Nebular theme greatly simplifies the process of [[building_a_chatbot_with_angular | building a chat UI]] <a class="yt-timestamp" data-t="13:57:00">[13:57:00]</a>.