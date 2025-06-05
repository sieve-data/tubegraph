---
title: Customizing chatbot responses with Dialogflow
videoId: CKhV7-NF2OI
---

From: [[fireship]] <br/> 

[[using_dialogflow_for_chatbot_development | Dialogflow]], formerly known as API.AI, is an engine designed for [[building_a_chatbot_using_dialogflow | building conversational experiences]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. It leverages Google's machine learning and [[understanding_natural_language_processing_with_chatbots | natural language processing]] technology to provide a user-friendly interface for developers to create and deploy chatbots across various platforms, including the web, Slack, and Facebook Messenger <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## Agent and Intent Detection
The primary function of a [[setting_up_dialogflow_agents_and_intents | Dialogflow agent]] is to detect user intent <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. When a user inputs a phrase, such as "what is a component," a chatbot trained to recognize this phrase will detect the corresponding intent <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. Upon intent detection, the system can either execute backend code or send a predefined response to the user <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. For example, if the "component" intent is recognized, the bot might respond with "it's just JavaScript" <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

If the bot fails to recognize an intent, it can be configured to deliver a custom message <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. [[using_dialogflow_for_chatbot_development | Dialogflow]] offers extensive options for customization, focusing on the back-and-forth dialogue between the user and the bot <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Defining User Phrases and Bot Responses
To make your bot robust, you should add multiple phrases that a user might say to express a particular intent <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. Once the intent is recognized, the bot will send its programmed response <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

For example:
*   **User phrase**: "what is a component" <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>
*   **Bot response**: "it's just JavaScript" <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>

### Enhancing Personality with Small Talk
[[using_dialogflow_for_chatbot_development | Dialogflow]] includes a "Small Talk" feature that allows for quick customization of your bot's personality without requiring custom intents <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. This feature comes with a large list of predefined scenarios to which you can add your own custom language <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

For instance, if a user asks "who are you?", the bot can be configured to respond with "I'm angular bot I know stuff about angular" <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. This is an excellent way to impress users by providing entertaining or intelligent replies to common questions <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

## Testing Chatbot Responses
After defining intents and responses, you can test them directly within the [[using_dialogflow_for_chatbot_development | Dialogflow]] interface. After saving an intent, a test area in the top right corner allows you to input phrases and see the bot's response <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. You can also view the JSON response that your application would receive <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

For example, testing the "who are you" intent:
*   **User Input**: "who are you" <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>
*   **Bot Response**: "I'm angular bot I know stuff about angular" <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>

Testing a custom intent:
*   **User Input**: "what is a component mr. bot" <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>
*   **Bot Response**: "it's just JavaScript" <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>