---
title: Integrating Dialogflow with Nodejs and Angular
videoId: 0NXqwT3Y09E
---

From: [[fireship]] <br/> 

This article details how to [[building_a_chatbot_with_angular | build a chatbot from scratch]] by [[using_dialogflow_for_chatbot_development | using Dialogflow]], Node.js, and Cloud Functions, with a focus on [[integrating_dialogflow_with_an_angular_application | integrating it with an Angular application]] for the front-end. The goal is to create a simple chatbot that can collect information from a user and save it permanently in a backend database [00:00:39].

## Chatbot Hype Cycle and Reality

In 2017, chatbots were predicted to be the "next big thing," expected to eliminate call center jobs, replace lawyers, and prevent users from needing to fill out HTML forms [00:00:08]. By 2019, the hype had peaked, and chatbots largely failed to meet these high expectations [00:00:19]. However, while expectations are often overestimated in the short term and underestimated in the long term, conversational experiences can be very effective when tailored to a specific business need [00:00:26].

## Core Technologies

The chatbot discussed in this guide utilizes:
*   [[using_dialogflow_for_chatbot_development | Dialogflow]] for natural language processing and virtual agent creation [00:00:57].
*   Node.js for backend logic [00:00:42].
*   Cloud Functions for serverless backend execution [00:00:42].
*   Angular for the front-end user interface [00:01:43].

## Understanding Dialogflow

[[using_dialogflow_for_chatbot_development | Dialogflow]] is a tool for [[building_a_chatbot_using_dialogflow | building virtual agents]] that can intelligently respond to user input, whether voice or text [00:01:00]. It processes natural language to translate user input into structured data for your application [00:02:42].

### How Dialogflow Works

A [[setting_up_dialogflow_agents_and_intents | Dialogflow]] agent acts as a virtual call center representative trained to solve various problems [00:02:48]. When it receives input, it first determines the user's *intention* [00:02:57].

[[using_dialogflow_for_chatbot_development | Dialogflow]] allows automatic integration with various platforms like Facebook Messenger, Slack, and even phone lines [00:01:21]. This guide, however, focuses on direct interaction with the [[using_dialogflow_for_chatbot_development | Dialogflow]] API using a Node.js backend [00:01:31].

### Setting Up a Dialogflow Agent

1.  **Create a New Agent:** This represents your individual chatbot [00:02:35].
2.  **Define Intents:** Intents represent the user's intention or the problem they're trying to solve [00:02:59].
    *   **Context:** A mechanism for passing data between intents (not covered in this guide) [00:03:15].
    *   **Events:** Allows an intent to be triggered programmatically without manual user input, useful for onboarding processes [00:03:23].
    *   **Training Phrases:** Short phrases that would trigger the intent. The machine learning algorithm uses natural language processing to identify similar phrases [00:03:39]. More data generally leads to better performance [00:03:50].
    *   **Action and Parameters:**
        *   **Action Name:** Good practice to use a reverse domain name followed by the intent name [00:04:02].
        *   **Parameters:** Pieces of data that the chatbot needs to collect to fulfill the intent [00:04:19]. They can be optional or required [00:04:21].
        *   **Entities:** Represent the type of data being collected, allowing [[using_dialogflow_for_chatbot_development | Dialogflow]] to validate data automatically. Custom entities can also be created [00:04:30].
        *   **Prompts:** What the agent asks the user to collect required data [00:04:44].
    *   **Fulfillment:** Once all data is collected, an intent can be fulfilled in two ways [00:04:50]:
        *   **Direct Response:** Define a simple text response in the [[using_dialogflow_for_chatbot_development | Dialogflow]] console if no backend work is needed [00:04:55].
        *   **Webhook:** For backend operations (e.g., updating a database, making API calls, sending emails), a webhook is used to send data to a custom backend server [00:05:01]. This allows for dynamic responses and complex logic [00:05:07].

## System Architecture

The typical architecture for [[integrating_dialogflow_with_an_angular_application | integrating Dialogflow with an Angular application]] and Node.js Cloud Functions involves:

1.  **Front-end Application (Angular):** Where the user interacts with the chatbot [00:01:38]. It makes API calls to a gateway Cloud Function [00:01:48].
2.  **Gateway Cloud Function (Node.js):** Acts as a secure proxy to make calls to the [[using_dialogflow_for_chatbot_development | Dialogflow]] API, protecting sensitive API keys [00:01:50]. It receives user messages, passes them to [[using_dialogflow_for_chatbot_development | Dialogflow]], and sends the bot's response back to the front-end [00:01:58].
3.  **Dialogflow API:** Processes the natural language input and manages the conversation flow [00:02:04].
4.  **Webhook Cloud Function (Node.js):** Triggered by [[using_dialogflow_for_chatbot_development | Dialogflow]] when an intent is fulfilled, allowing for additional backend work like processing payments, sending emails, or updating databases [00:01:10]. It can also dynamically compute the bot's response [00:02:23].
5.  **Backend Database (e.g., Firestore):** Stores collected information or other persistent data [00:00:54].

## Backend Integration with Cloud Functions

[[using_cloud_functions_for_backend_chatbot_integration | Cloud functions]] are used to handle the secure communication with [[using_dialogflow_for_chatbot_development | Dialogflow]] and fulfill intents on the backend.

### Initialization

*   Initialize Cloud Functions with JavaScript [00:05:43].
*   Install necessary NPM packages [00:06:08]:
    *   `dialogflow`: The [[using_dialogflow_for_chatbot_development | Dialogflow]] API client [00:05:52].
    *   `cors`: To enable cross-origin requests from the front-end [00:05:54].
    *   `dialogflow-fulfillment`: Specifically for [[customizing_chatbot_responses_with_dialogflow | Dialogflow fulfillment]] logic [00:06:02].
    *   `actions-on-google`: If integrating with Google Assistant actions [00:06:05].

### Gateway Cloud Function (`dialogflowGateway`)

This function acts as a secure intermediary between the Angular front-end and the [[using_dialogflow_for_chatbot_development | Dialogflow]] API.

1.  **Service Account:** Obtain a JSON file containing your private API key from the Firebase console (Settings -> Service Account) and download it to your functions directory. Keep this file secure and add it to `.gitignore` [00:06:26].
2.  **Initialization:**
    *   Import `cors` and initialize Firebase Admin with the service account credentials [00:06:17].
    *   Import `SessionClient` from `dialogflow` [00:06:55].
3.  **HTTP Cloud Function Setup:** Define an HTTP Cloud Function and wrap its request/response with `cors` to allow browser requests [00:06:59].
4.  **Request Handling:**
    *   The function expects `queryInput` (user's text or audio) and `sessionID` (a unique ID per user to maintain conversation context) from the front-end [00:07:11].
    *   Initialize the `SessionClient` with the service account [00:07:27].
    *   Reference the session using `sessionPath` with your Firebase project ID and `sessionID` [00:07:31].
    *   Call `detectIntent` with the session and `queryInput` to get a response from [[using_dialogflow_for_chatbot_development | Dialogflow]] [00:07:38].
    *   Send the `fulfillmentText` from the `queryResult` back to the front-end as the response [00:07:51].

### Webhook Cloud Function (Fulfillment)

This function is triggered by [[using_dialogflow_for_chatbot_development | Dialogflow]] when an intent requires backend processing.

1.  **HTTP Function Setup:** Define a separate HTTP function (no `cors` needed as it's not called directly from the front-end) [00:09:13].
2.  **Webhook Client:** Initialize an instance of the `WebhookClient` using the request and response objects [00:09:21].
3.  **Intent Handling:** This function is called for all intents enabled for webhook fulfillment [00:09:27].
    *   Implement specific functions for each custom intent (e.g., `updateProfile` for "update profile" intent) [00:09:50].
    *   Within the intent function, perform backend operations (e.g., update Firestore database with user parameters) [00:09:53].
    *   Add a message to the agent (`agent.add()`) that will be sent back to the user as the bot's response [00:10:08].
4.  **Intent Mapping:** Map the custom intent functions to their corresponding intent names using a JavaScript Map [00:10:16].
5.  **Deployment:** Deploy the Cloud Functions using `firebase deploy --only functions` [00:10:32].

## Frontend Integration with Angular

[[integrating_dialogflow_with_an_angular_application | Integrating Dialogflow with an Angular application]] provides a user-friendly interface. This example uses the Nebula theme for rapid UI development.

### Setup

1.  **Install Nebula Theme:** Add Nebula to your Angular app by running `ng add @nebular/theme` [00:10:56].
2.  **Import Modules:** In `app.module.ts`, import `NbChatUiModule`, `NbSpinnerModule`, and `HttpClientModule` from `@angular/common/http` [00:11:06].
3.  **Chatbot Component:** Generate a new Angular component (e.g., `ChatbotComponent`) to encapsulate the chatbot logic [00:11:21].

### Component Template (`.html`)

Nebula's UI modules simplify chat interface creation.

*   `nb-chat` component: A wrapper for messages and the input form [00:11:33].
*   `nb-chat-message`: Used to display individual messages. Loop over a messages array using `*ngFor` [00:11:41].
    *   Customize messages with inputs like `message` text, `reply` (true for user messages), `date`, and `avatar` [00:11:48].
    *   A loading spinner can be shown using `nbSpinner` directive when the bot is responding [00:12:04].
*   `nb-chat-form`: Provides the input field and send button. It emits a `send` event when the user sends a message [00:12:14].

### Component Logic (`.ts`)

The Angular component handles communication with the gateway Cloud Function.

1.  **Dependencies:** Inject Angular's `HttpClient` [00:12:21].
2.  **Properties:**
    *   `messages`: An empty array to store chat messages [00:12:33].
    *   `loading`: Boolean flag to indicate bot response loading state [00:12:35].
    *   `sessionID`: A unique identifier for the conversation (e.g., a randomly generated string or user ID) [00:12:37].
3.  **Message Handling Helpers:**
    *   A method to add user-generated messages to the `messages` array, setting `reply` to `true` for correct styling [00:12:45].
    *   A similar method for bot messages, defining an `avatar` property [00:13:00].
4.  **Initial Bot Message:** When the app loads, add an initial bot message to greet the user [00:13:06].
5.  **`sendMessage` Function:** Triggered when the user sends a message from the `nb-chat-form`.
    *   Add the user's message to the chat [00:13:18].
    *   Set `loading` to `true` [00:13:20].
    *   Make an HTTP POST request using `HttpClient.post()` to the `dialogflowGateway` Cloud Function URL [00:13:23].
    *   The request body includes the `sessionID` and a `queryInput` object containing the user's text and language code [00:13:31].
    *   Subscribe to the response:
        *   Extract the `fulfillmentText` (the bot's response) [00:13:48].
        *   Add the bot's message to the chat [00:13:51].
        *   Set `loading` to `false` [00:13:53].

This completes the process of [[integrating_dialogflow_with_an_angular_application | integrating Dialogflow with an Angular application]] and Node.js Cloud Functions to build a functional chatbot [00:13:57].