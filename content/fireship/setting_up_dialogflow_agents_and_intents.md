---
title: Setting up Dialogflow agents and intents
videoId: 0NXqwT3Y09E
---

From: [[fireship]] <br/> 

[[using_dialogflow_for_chatbot_development | Dialogflow]] is a tool used for [[building_a_chatbot_using_dialogflow | building virtual agents]] that can intelligently respond to user input, whether it's voice or text <a class="yt-timestamp" data-t="01:00:57">[01:00:57]</a>. It powers the natural language processing (NLP) or artificial intelligence aspects of a chatbot <a class="yt-timestamp" data-t="00:56:55">[00:56:55]</a>.

## Dialogflow Agents
An agent in [[using_dialogflow_for_chatbot_development | Dialogflow]] represents an individual chatbot <a class="yt-timestamp" data-t="02:37:54">[02:37:54]</a>. A chatbot functions as a tool that translates user input, such as text or speech, into structured data that can be used in an application <a class="yt-timestamp" data-t="02:40:48">[02:40:48]</a>. The agent acts like a customer service representative in a virtual call center, trained to address various problems <a class="yt-timestamp" data-t="02:48:07">[02:48:07]</a>.

## Dialogflow Intents
When a user provides input, the agent first needs to determine their "intention" or the problem they are trying to solve <a class="yt-timestamp" data-t="02:56:54">[02:56:54]</a>. This is where intents come in.

### Creating a New Intent
To create an intent, you give it a name, such as "update profile" <a class="yt-timestamp" data-t="03:06:05">[03:06:05]</a>. Intents have several configurable options:

*   **Context**
    Context is an advanced mechanism for passing data from one intent to another <a class="yt-timestamp" data-t="03:14:48">[03:14:48]</a>. It is not covered in detail in this video <a class="yt-timestamp" data-t="03:16:34">[03:16:34]</a>.

*   **Events**
    Events are optional but provide a way to programmatically trigger an intent without manual user input <a class="yt-timestamp" data-t="03:22:42">[03:22:42]</a>. This is useful for scenarios like user onboarding processes, where you can kick off a conversation in your code <a class="yt-timestamp" data-t="03:28:44">[03:28:44]</a>.

*   **Training Phrases**
    These are short phrases from the user that would trigger the specific intent <a class="yt-timestamp" data-t="03:38:22">[03:38:22]</a>. [[using_dialogflow_for_chatbot_development | Dialogflow]]'s machine learning algorithm uses natural language processing to identify similar phrases that convey the same intent <a class="yt-timestamp" data-t="03:44:40">[03:44:40]</a>. Providing more data here generally improves accuracy <a class="yt-timestamp" data-t="03:51:24">[03:51:24]</a>.

*   **Action and Parameters**
    *   **Action:** When naming an action, it's good practice to use your domain name in reverse, followed by the intent name, similar to a bundle ID for a mobile application <a class="yt-timestamp" data-t="04:02:18">[04:02:18]</a>.
    *   **Parameters:** When an intent is triggered, you often need to collect multiple pieces of data to resolve the user's problem <a class="yt-timestamp" data-t="04:13:30">[04:13:30]</a>. Parameters allow you to set up optional and required data points that [[using_dialogflow_for_chatbot_development | Dialogflow]] will attempt to collect <a class="yt-timestamp" data-t="04:19:35">[04:19:35]</a>.
        *   **Example:** For an "update profile" intent, you might collect the user's display name, giving it a parameter name like "name" <a class="yt-timestamp" data-t="04:26:30">[04:26:30]</a>.
        *   **Entity:** The "entity" option specifies the type of data being collected, which helps [[using_dialogflow_for_chatbot_development | Dialogflow]] automatically validate the data <a class="yt-timestamp" data-t="04:31:18">[04:31:18]</a>. You can also create custom entities for unique data types <a class="yt-timestamp" data-t="04:39:13">[04:39:13]</a>.
        *   **Prompt:** A prompt is what the agent will ask the user to collect the necessary data <a class="yt-timestamp" data-t="04:44:26">[04:44:26]</a>. For example, if a user says "update my profile," the bot might respond by asking, "What is your preferred name?" <a class="yt-timestamp" data-t="08:27:54">[08:27:54]</a>.

*   **Fulfillment**
    After all necessary data is collected, there are two ways to fulfill an intent <a class="yt-timestamp" data-t="04:50:09">[04:50:09]</a>:
    1.  **Defined Response:** If no additional backend work is needed, you can simply define a response directly in the [[using_dialogflow_for_chatbot_development | Dialogflow]] console <a class="yt-timestamp" data-t="04:53:50">[04:53:50]</a>.
    2.  **Webhook:** For scenarios requiring updates to a database or API calls to third parties, a webhook is used <a class="yt-timestamp" data-t="04:59:17">[04:59:17]</a>. This allows you to write custom code on your backend server (e.g., [[using_cloud_functions_for_backend_chatbot_integration | Cloud Functions]]) to dynamically format the response and handle other tasks requested by the user, such as sending an email, processing a payment, or updating a database <a class="yt-timestamp" data-t="05:07:05">[05:07:05]</a>.

### Saving and Integrating Intents
Once an intent is configured, it can be saved <a class="yt-timestamp" data-t="05:14:14">[05:14:14]</a>. [[using_dialogflow_for_chatbot_development | Dialogflow]] agents can be automatically integrated with various platforms like Facebook Messenger, Slack, Twitter, and Twilio, and can even connect to a phone line <a class="yt-timestamp" data-t="05:17:33">[05:17:33]</a>. For custom UI or specific backend interactions, you would interact with the [[using_dialogflow_for_chatbot_development | Dialogflow]] API directly using a [[integrating_dialogflow_with_nodejs_and_angular | Node.js]] backend and [[using_cloud_functions_for_backend_chatbot_integration | Cloud Functions]] <a class="yt-timestamp" data-t="05:30:05">[05:30:05]</a>.

To set up your environment for [[building a chatbot with Angular | chatbot development]], you'll need a [[setting_up_firebase_for_signaling_in_video_chat_apps | Firebase]] project <a class="yt-timestamp" data-t="02:28:22">[02:28:22]</a>.