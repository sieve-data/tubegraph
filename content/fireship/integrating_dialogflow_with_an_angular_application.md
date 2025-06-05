---
title: Integrating Dialogflow with an Angular application
videoId: CKhV7-NF2OI
---

From: [[fireship]] <br/> 

[[building_a_chatbot_with_angular | Building a chatbot with Angular]] and Dialogflow is designed to be straightforward, allowing a basic chatbot to be built rapidly <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This guide demonstrates how to [[integrating_dialogflow_with_nodejs_and_angular | integrate Dialogflow]] with an Angular application using the JavaScript SDK <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## What is Dialogflow?

Dialogflow, formerly known as API.AI, is an engine for [[building_a_chatbot_using_dialogflow | building conversational experiences]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. It leverages Google's machine learning and natural language processing (NLP) technology, providing a user-friendly interface for developers to build and deploy chatbots to various platforms like web, Slack, or Facebook Messenger <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Project Setup and Structure

To begin [[integrating_dialogflow_with_nodejs_and_angular | integrating Dialogflow with Node.js and Angular]], start by creating a new Angular application and setting up the necessary modules and components.

### Initialize Angular App

1.  Generate a new Angular application from the command line: `ng new chatbot` <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
2.  Navigate into the new project directory: `cd chatbot` <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
3.  Install the Dialogflow JavaScript SDK via npm: `npm install apiai --save` (at this point, the SDK might still be called API.AI) <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

### Angular CLI Configuration

Modify the `angular.json` (or `angular-cli.json`) file to remove the default `app` prefix for components <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Replace `'app'` with an empty string in the `prefix` property <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

### Feature Module Setup

It's good practice to encapsulate chatbot functionality within a feature module, though it's optional <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

1.  Generate a new module named `chat`: `ng generate module chat` <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
2.  Generate a service within this module: `ng generate service chat/chat --module chat` <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
3.  Generate a component named `chat-dialog` within this module: `ng generate component chat/chat-dialog --module chat` <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
4.  Add the `FormsModule` to the `chat.module.ts` imports <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
5.  Export the `ChatDialogComponent` from `chat.module.ts` so it can be used in other modules like `AppModule` <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
6.  Import `ChatModule` into your `AppModule` (`app.module.ts`) by adding it to the `imports` array <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
7.  Include the `chat-dialog` component in `app.component.html` to display it: `<chat-dialog></chat-dialog>` <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## [[building_a_chatbot_using_dialogflow | Building a Chatbot Using Dialogflow]]

[[using_dialogflow_for_chatbot_development | Using Dialogflow for chatbot development]] involves defining how your chatbot will understand and respond to user input.

### Creating a Dialogflow Agent

1.  Sign up for Dialogflow (it's a free service) <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
2.  Create your first agent, for example, named "Angular Bot" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. This agent will provide information about the Angular framework <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

### [[setting_up_dialogflow_agents_and_intents | Setting up Dialogflow Agents and Intents]]

The core function of an agent is to detect user intent <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

1.  **Create a Custom Intent**:
    *   Add a user phrase like "What is a component?" <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
    *   Add multiple similar phrases to make the bot more robust to different expressions of the same intent <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
    *   Define a response for this intent, e.g., "It's just JavaScript" <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
    *   Save the intent and test it using the testing console in Dialogflow <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
2.  **Use Small Talk**:
    *   Dialogflow's "Small Talk" feature allows quick customization of the bot's personality without creating custom intents <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
    *   Customize responses for common questions like "Who are you?" <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. For example, the bot can respond: "I'm Angular Bot. I know stuff about Angular" <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

## Connecting Angular to Dialogflow

To enable communication between your Angular application and the Dialogflow agent, you need to obtain an access token and configure your Angular service.

### Obtain Client Access Token

1.  In Dialogflow, click on your agent <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
2.  Copy the **Client Access Token** from the main agent page <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
3.  Add this token to your `environment.ts` file in your Angular project <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

### Chat Service Implementation

The `ChatService` will handle communication with Dialogflow.

1.  **Import Dependencies**:
    *   Import `environment` to access the API token <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
    *   Import `ApiAiClient` from the installed SDK <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
    *   Import `Observable` and `BehaviorSubject` from `rxjs` for data management <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
2.  **Initialize API Client**:
    *   Declare a `read-only` variable for the token: `private readonly token = environment.dialogflow.angularBot;` <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
    *   Initialize the `ApiAiClient`: `private client;` in the constructor, then `this.client = new ApiAiClient({ accessToken: this.token });` <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
3.  **Define Message Structure**:
    *   Create a `Message` interface or class to define how messages are structured:
        ```typescript
        export class Message {
          content: string;
          sentBy: string; // 'bot' or 'user'
        }
        ```
        <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>
4.  **Manage Conversation with RxJS**:
    *   Create a `BehaviorSubject` to hold the conversation: `conversation = new BehaviorSubject<Message[]>([]);` <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
    *   Create an `update` method to add new messages to the conversation:
        ```typescript
        update(msg: Message) {
          this.conversation.next([this.conversation.value, msg]); // Using spread operator for concatenation
        }
        ```
        The original code used `this.conversation.next([...this.conversation.value, msg]);` but the speaker concatenates `old array` and `new array` <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
5.  **Send Text Request to Dialogflow**:
    *   Create a `converse` method that takes user input:
        ```typescript
        converse(msg: string) {
          const userMessage = { content: msg, sentBy: 'user' };
          this.update(userMessage); // Add user message to UI

          this.client.textRequest(msg)
            .then(res => {
              const speech = res.result.fulfillment.speech;
              const botMessage = { content: speech, sentBy: 'bot' };
              this.update(botMessage); // Add bot response to UI
            });
        }
        ```
        <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>
        This sends an HTTP request to Dialogflow, which responds with JSON containing the agent's response <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. The actual text response is found in `result.fulfillment.speech` <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

## Building the Angular Chat UI

The `ChatDialogComponent` will display the conversation and allow user input.

### Chat Dialog Component Implementation

1.  **Import Dependencies**:
    *   Import `ChatService` and `Message` class <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
    *   Import `Observable` and the `scan` operator from `rxjs/operators` <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
2.  **Component Properties**:
    *   Declare `messages: Observable<Message[]>;` to hold the conversation <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
    *   Declare `formValue: string;` for the user's input field <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
3.  **Constructor**: Inject the `ChatService`: `constructor(private chat: ChatService) { }` <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.
4.  **`ngOnInit` (or similar lifecycle hook)**:
    *   Convert the `BehaviorSubject` from the service into an observable array suitable for `ngFor` <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
    *   Use the `scan` operator to concatenate new messages to the existing array:
        ```typescript
        ngOnInit() {
          this.messages = this.chat.conversation.asObservable()
            .scan((acc, val) => acc.concat(val) ); // Concatenate new messages
        }
        ```
        The `scan` operator provides the current value (`val`) and the accumulated total (`acc`), allowing a new array to be concatenated <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
5.  **Send Message Handler**:
    *   Create a method, e.g., `sendMessage()`, to call the service's `converse` method with the `formValue`:
        ```typescript
        sendMessage() {
          this.chat.converse(this.formValue);
          this.formValue = ''; // Clear input field
        }
        ```
        <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>

### HTML Template (`chat-dialog.component.html`)

[[using_angular_components_and_component_architecture | Angular components and component architecture]] allow for a clean UI.

1.  **Display Messages**:
    *   Loop over the `messages` observable using `ngFor` and the `async` pipe <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
    *   Use `ngClass` to apply different styles based on who sent the message (`sentBy` property):
        ```html
        <div *ngFor="let message of messages | async"
             [ngClass]="{ 'friend-message': message.sentBy === 'bot', 'my-message': message.sentBy === 'user' }">
          {{ message.content }}
        </div>
        ```
        <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>
2.  **User Input Form**:
    *   Set up an input field with `ngModel` bound to `formValue` <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
    *   Bind the `(keyup.enter)` event to call `sendMessage()` when the user presses Enter <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
    *   Add a button to trigger `sendMessage()` on click <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.

```html
<!-- Example structure -->
<form (ngSubmit)="sendMessage()">
  <input [(ngModel)]="formValue" name="messageInput" placeholder="Type your message..." />
  <button type="submit">Send</button>
</form>
```

### Styling (Optional)

For similar front-end styling, you can include the Milligram CSS framework and custom CSS styles in your project <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

## Demonstration

After setting up, run `ng serve` and access your Angular application.

*   **Default Small Talk**: If you type "hello there," the bot might respond with "good day" <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
*   **Customized Small Talk**: If you ask "who are you?", the bot will respond with the customized message "I'm Angular Bot I know stuff about angular" <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
*   **Custom Intent**: Asking "what is a component mr. bot?" will trigger the custom intent and respond with "it's just JavaScript" <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.

This demonstrates the basic functionality of [[building_a_chatbot_with_angular | building a chatbot with Angular]] and Dialogflow <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.