---
title: Building a chatbot with Angular
videoId: CKhV7-NF2OI
---

From: [[fireship]] <br/> 

[[Building a chatbot using Dialogflow | Building a chatbot]] with Angular and Dialogflow is described as a straightforward process, achievable from scratch in approximately 10 minutes <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This article outlines the steps for [[integrating_dialogflow_with_an_angular_application | integrating Dialogflow with an Angular application]] using the JavaScript SDK <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## What is Dialogflow?

Dialogflow, formerly known as API.AI, is an engine designed for [[using_dialogflow_for_chatbot_development | building conversational experiences]] <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. It leverages Google's machine learning and [[understanding_natural_language_processing_with_chatbots | natural language processing]] (NLP) technology <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. Developers are provided with a user-friendly interface to create chatbots and deploy them across various platforms, including the web, Slack, or Facebook Messenger <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Setting Up the Angular Application

The initial setup for an Angular chatbot involves creating a new Angular project and installing the necessary SDK <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>:

1.  **Create a New Angular App**:
    *   Use the Angular CLI: `ng new chatbot` <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
    *   Navigate into the project directory: `cd chatbot` <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
2.  **Install the JavaScript SDK**:
    *   Install the API.AI JavaScript SDK via NPM: `npm install apiai --save` <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
    *   *Note*: The SDK might still be called API.AI at this point, but may change to Dialogflow in the future <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
3.  **Adjust Angular CLI Prefix (Optional)**:
    *   To prevent components from being prefixed with `app-`, modify the `angular.json` file (formerly `angular-cli.json`) <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Replace `app` with an empty string in the `prefix` property <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

### Structuring with a Feature Module

While optional, creating a feature module is considered good practice for growing applications <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>:

1.  **Generate `chat` Module**: `ng generate module chat` <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
2.  **Generate `chat` Service**: `ng generate service chat --module chat` <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
3.  **Generate `chat-dialog` Component**: `ng generate component chat-dialog --module chat` <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
    *   These resources will be nested under the `chat` folder <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
4.  **Import `AngularForms` Module**: Add the `AngularForms` module to the `chat.module.ts` file <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
5.  **Export `ChatDialogComponent`**: Set the `ChatDialogComponent` to `exports` in `chat.module.ts` so it can be used in `app.component.ts` <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
6.  **Import `ChatModule`**: In `app.module.ts`, import `ChatModule` and add it to the `imports` array <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
7.  **Declare `chat-dialog` Component**: In `app.component.html`, declare the `chat-dialog` component tag <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

## Building the Chatbot in Dialogflow

[[Building a chatbot using Dialogflow | Building the chatbot]] itself occurs within the Dialogflow console:

1.  **Sign Up and Create an Agent**: Dialogflow is a free service <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. Create a new agent, for example, "Angular Bot," intended to provide general information about the Angular framework <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
2.  **Define Intents**: The core purpose of an agent is to detect user intent <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
    *   Add training phrases that a user might say, e.g., "What is a component?" <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. Add multiple variations for robustness <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
    *   Define a response for the detected intent, e.g., "It's just JavaScript" <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
    *   Save the intent and test it in the Dialogflow console <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
3.  **Utilize Small Talk (Optional)**:
    *   Small Talk allows quick customization of the bot's personality without creating custom intents <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
    *   It provides a list of predefined scenarios where custom language can be added <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. For example, if a user asks "Who are you?", the bot can respond with "I'm Angular Bot, I know stuff about Angular" <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

## Integrating Dialogflow with Angular

To connect the Angular app to Dialogflow:

1.  **Obtain Client Access Token**:
    *   In Dialogflow, click on the agent, then copy the Client Access Token from the main agent page <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
    *   *Security Note*: For Dialogflow, adding the API key directly to `environment.ts` is acceptable because the service is free and does not provide write access <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
2.  **Configure Chat Service (`chat.service.ts`)**:
    *   Import `environment` and the `ApiAiClient` from the installed SDK <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
    *   Initialize the `ApiAiClient` with the client access token <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
    *   **Define `Message` Class**: Create a class to define message structure, including `content` (string) and `sentBy` (to distinguish between 'bot' and 'user') <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
    *   **Manage Conversation State with `BehaviorSubject`**:
        *   Create a `BehaviorSubject` called `conversation`, typed to an array of `Message` objects, initialized as an empty array <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
        *   Implement an `update` method that calls `next` on the `BehaviorSubject` to add new messages to the conversation <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
    *   **Implement `talk` Method**:
        *   This method takes a user message (string) <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
        *   Format the user message into a `Message` object and add it to the conversation using `update` <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
        *   Send the user's text to Dialogflow using `client.textRequest()` <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. This sends an HTTP request and returns a promise <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
        *   Process the Dialogflow response: extract the bot's speech from `result.fulfillment.speech` <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
        *   Format the bot's response into a `Message` object and add it to the conversation using `update` <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
3.  **Configure Chat Dialog Component (`chat-dialog.component.ts`)**:
    *   Import `ChatService`, `Message` class, `Observable`, and `scan` operator from RxJS <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
    *   Inject `ChatService` into the constructor <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
    *   **Transform `BehaviorSubject` to Observable Array**:
        *   Convert the `chatService.conversation` BehaviorSubject into an observable array of messages <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
        *   Use the `scan` operator: `chatService.conversation.asObservable().scan((acc, val) => acc.concat(val))` <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. The `scan` operator concatenates new messages with the accumulated array, resulting in an observable array <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.
    *   **Implement `sendMessage` Method**: This method takes the `formValue` (user input) and calls `chatService.talk()` with that value <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
4.  **Design Chat Dialog Template (`chat-dialog.component.html`)**:
    *   **Display Messages**:
        *   Loop over the `messages` observable array using `*ngFor` and the `async` pipe <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
        *   Use `[ngClass]` to apply different styles based on `message.sentBy` (e.g., `friend` for bot, `me` for user) <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
        *   Display `{{ message.content }}` <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
    *   **User Input Form**:
        *   Create a form with an input field using `ngModel` bound to `formValue` <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
        *   Bind the `(keyup.enter)` event to call `sendMessage()` when the user presses Enter <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
        *   Add a button that also calls `sendMessage()` on `(click)` <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
    *   *Styling*: Milligram CSS framework and custom CSS styles can be used for front-end styling <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

## Testing the Chatbot

After setup, run the Angular application. The chatbot should respond to messages, including:
*   Default small talk responses (e.g., "good day" to "hello there") <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
*   Customized small talk responses (e.g., "I'm Angular Bot, I know stuff about Angular" to "who are you?") <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
*   Custom intent responses (e.g., "It's just JavaScript" to "what is a component?") <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.