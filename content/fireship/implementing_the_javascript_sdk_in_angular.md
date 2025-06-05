---
title: Implementing the JavaScript SDK in Angular
videoId: CKhV7-NF2OI
---

From: [[fireship]] <br/> 

Building a chatbot with [[building_a_chatbot_with_angular | Angular]] and Dialogflow is made straightforward using the JavaScript SDK [00:00:00] [00:00:29]. This guide details how to integrate the SDK into an [[building_a_chatbot_with_angular | Angular]] application to create conversational experiences [00:00:31]. Dialogflow, previously known as API.AI, is an engine that leverages Google's machine learning and natural language processing for building chatbots [00:00:08] [00:00:13] [00:00:15].

## Setting up the Angular Application

To begin, create a new [[building_a_chatbot_with_angular | Angular]] application from the command line:
```bash
ng new chat-bot
cd chat-bot
```
<a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>

Next, install the JavaScript SDK (which was still called API.AI at the time of recording) via NPM in the development environment:
```bash
npm install apiai
```
<a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a> <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>

Optionally, you can configure the [[using_angular_components_and_component_architecture | Angular]] CLI to not prefix components with `app` by modifying the `angular-cli.json` file [00:01:00]. At this point, running `ng serve` should display a basic [[building_a_chatbot_with_angular | Angular]] application [00:01:10].

## Module and Component Structure

It is good practice to flesh out a feature module for your code to make your application more manageable as it grows [00:01:14] [00:01:19].

1.  **Generate a Module**: Create a new module named `chat`:
    ```bash
    ng generate module chat
    ```
    <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>
2.  **Add a Service**: Generate a service within this module using the `-m` flag to ensure it's included:
    ```bash
    ng generate service chat -m chat
    ```
    <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>
3.  **Add a Component**: Create a component called `chat-dialog` and place it in the same module:
    ```bash
    ng generate component chat-dialog -m chat
    ```
    <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>

This structure nests all resources under the `chat` folder, with [[using_angular_components_and_component_architecture | components]] and services registered inside the chat module [00:01:39] [00:01:45].

Additional steps for the chat module:
*   Import the [[using_tensorflowjs_with_angular | Angular]] forms module [00:01:47].
*   Set the `chat-dialog` [[using_angular_components_and_component_architecture | component]] to `exports` so it can be used directly in the app [[using_angular_components_and_component_architecture | component]] [00:01:51].
*   Import the `ChatModule` into the main `AppModule` [00:02:02].

Finally, declare the `chat-dialog` [[using_angular_components_and_component_architecture | component]] in the `app.component.html` file to display it [00:02:13] [00:02:16].

## Dialogflow Agent Setup

To interact with a chatbot, you first need to set one up in Dialogflow [00:02:23].
1.  **Sign Up**: Dialogflow is a free service [00:02:27] [00:02:29].
2.  **Create an Agent**: Create a new agent, for example, "Angular bot," whose purpose is to provide general information about the [[building_a_chatbot_with_angular | Angular]] framework [00:02:31] [00:02:35].
3.  **Define Intents**: The core function of an agent is to detect user intent [00:02:47].
    *   **User Phrases**: Add multiple phrases a user might say, such as "what is a component?" to make the bot more robust [00:02:51] [00:03:22].
    *   **Bot Response**: Define the bot's response when an intent is recognized; for "what is a component?", the bot might respond, "it's just JavaScript" [00:03:03] [00:03:31] [00:03:37].
    *   **Default Fallback**: Customize messages for when the bot doesn't recognize an intent [00:03:09].
4.  **Small Talk**: Utilize the "small talk" feature to quickly customize the bot's personality with pre-existing scenarios [00:03:57]. You can add custom language to responses for common questions like "who are you?" [00:04:09] [00:04:12].

You can test the bot's responses directly within the Dialogflow console [00:03:42].

## Integrating the SDK

Before integrating, you need to obtain the client access token from your Dialogflow agent's settings [00:04:27] [00:04:29]. This token should be added to your `environment.ts` file in [[building_a_chatbot_with_angular | Angular]] [00:04:37]. While storing API keys here isn't always secure, it's acceptable for Dialogflow's free service as it doesn't have write access [00:04:43].

## Communicating with the Bot via SDK

Communication with the bot happens within the `chat.service.ts` file [00:04:55] [00:04:58].

1.  **Imports**: Import the `environment` file (containing the API token) and the `ApiAIClient` from the SDK [00:05:00] [00:05:05].
2.  **Initialize Client**: Set a read-only variable for the token and then initialize the `ApiAIClient` using this token [00:05:09] [00:05:15].
3.  **Send Text Request**: Create a `talk` method that uses `client.textRequest()` to send user messages to Dialogflow [00:05:24] [00:05:30]. This sends an HTTP request, and Dialogflow responds with JSON containing the agent's reply, including the `fulfillmentSpeech` [00:05:34] [00:05:37] [00:06:01].

## Refactoring for User-Friendly Messages

To manage and display messages in a user-friendly way, RxJS is used [00:06:10] [00:06:14].

1.  **Message Class**: Define a `Message` class with `content` (string) and `sentBy` (string to distinguish 'bot' or 'user') properties [00:06:25].
2.  **Conversation Subject**: In the `chat.service.ts`, create a `conversation` variable as a `BehaviorSubject` typed to an array of `Message` objects, initialized as an empty array [00:06:38] [00:06:41].
3.  **Update Method**: Implement an `update` function that calls `next` on the `BehaviorSubject` to add new messages to the feed [00:06:49] [00:06:51] [00:06:57].
4.  **`converse` Method**: This method in the service takes a user's message, converts it to a `Message` object, updates the conversation, sends the request to Dialogflow, and then formats the bot's response (`result.fulfillmentSpeech`) as another `Message` object to update the conversation [00:07:05] [00:07:09] [00:07:26] [00:07:41] [00:07:43].

## Displaying Messages in HTML

In the `chat-dialog.component.ts`:
1.  **Imports**: Import `ChatService`, `Message` class, `Observable`, and the `scan` operator from RxJS [00:07:57] [00:08:03].
2.  **Messages Observable**: Convert the `BehaviorSubject` from the service into an observable array of messages using the `scan` operator [00:08:11] [00:08:16] [00:08:29] [00:08:33]. The `scan` operator concatenates old and new arrays to maintain the conversation history [00:08:45] [00:08:52] [00:08:56].
3.  **Send Message**: Define a `sendMessage` method that takes the form value (user input) and calls the `converse` method from the `ChatService` [00:09:08] [00:09:17].

In `chat-dialog.component.html`:
1.  **Loop Messages**: Use `ngFor` with the `async` pipe to loop over the observable list of messages [00:09:26] [00:09:28].
2.  **Styling**: Use `ngClass` to distinguish between bot (`friend`) and human (`you`) messages [00:09:35] [00:09:38].
3.  **Display Content**: Display the `message.content` [00:09:49].
4.  **Input Form**: Set up a form input with `ng model` bound to `formValue` for user input [00:09:54] [00:09:59].
5.  **Event Handling**: Bind the `sendMessage` event handler to the form's `(ngSubmit)` event and a button's `(click)` event [00:10:06] [00:10:15].

Styling can be achieved using a CSS framework like Milligram and custom CSS [00:10:20] [00:10:26].

## Testing the Chatbot

Upon loading the [[building_a_chatbot_with_angular | Angular]] app, the chatbot can be tested [00:10:31].
*   The bot will respond to `small talk` queries like "hello there" or "how are ya" with default or customized responses [00:10:32] [00:10:36] [00:10:38] [00:10:41].
*   It will recognize and respond to custom intents, such as "what is a component?" with "it's just JavaScript" [00:10:44] [00:10:52] [00:10:55] [00:10:59].
*   The bot can handle farewells like "see you later" [00:11:02].