---
title: Voice AI in Business Negotiations
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

Voice AIs are rapidly advancing and are expected to automate significant portions of phone-based work within the next 1 to 3 years <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. This technology offers powerful opportunities for businesses to gain an "unfair advantage" through automated data collection and negotiation <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>.

## Case Study: The "Lowballer 9000" AI Bot

An illustrative example of [[voicefirst_interfaces_and_applications | voice AI]] in business negotiations is the "Lowballer 9000," an AI designed to lowball luxury watch dealers for a Rolex Daytona <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

### Purpose and Target
Named "Alex," this voice AI's primary job is to find Rolex Daytonas by contacting secondhand luxury watch dealers across the US, not official Rolex factory dealers <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a><a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>.

### Key Information Gathering
During conversations, Alex is programmed to gather critical details that impact the watch's quoted cost, such as its condition and whether it comes with original documentation and packaging <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.

## [[building_and_configuring_voice_ai_agents | Building and Configuring Voice AI Agents]]

The "Lowballer 9000" was built using Vappy, a flexible Voice API platform that allows users to bring their own prompts and select service providers for different functionalities <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a><a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>.

### Prompt Engineering
The AI's prompt was developed through an iterative process, much like "patching holes" in a sinking boat <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>. This involved observing real-world lowballing conversations and adjusting the AI's responses based on test calls <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>.

*   **Conciseness and Simplicity**: A key best practice discovered was to keep AI responses concise (1-2 sentences max) to prevent the AI from overwhelming the caller and making it sound less like an AI <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a><a class="yt-timestamp" data-t="05:05:00">[05:05:00]</a>. Additionally, instructing the AI to use "sixth-grade English" significantly increased call durations and made interactions sound more human <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a><a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>.
*   **Iterative Improvement**: The prompt was refined based on live tests, for example, to prevent the AI from "ramming every single question down [the caller's] throat" in the first turn <a class="yt-timestamp" data-t="04:12:00">[04:12:00]</a>.

### Model Selection
The choice of AI model (e.g., Gemini 20 Flash, DeepSeek) is crucial and can be influenced by current trends, often described as "flavor of the month" <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a><a class="yt-timestamp" data-t="06:18:00">[06:18:00]</a>. The stability of the chosen model's API is vital; for instance, a bot using DeepSeek crashed when its API became overloaded due to increased demand <a class="yt-timestamp" data-t="06:33:00">[06:33:00]</a><a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>.

### Temperature
"Temperature" in AI configuration determines the creativity of the AI's responses <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>. A temperature closer to zero yields a more deterministic and predictable system, while a higher temperature allows for more creative responses, which can be useful when facing uncommon questions <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a>.

### Voice Configuration
Voice AI platforms allow users to select specific voices, such as "Cartisia" or "New York man," to align with the desired character of the AI agent <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a><a class="yt-timestamp" data-t="09:19:00">[09:19:00]</a>. This contributes to [[using_ai_to_create_voice_character_apps | creating a voice character app]].

## [[function_calling_in_ai_voice_apps | Function Calling]] and Integrations

The true power of a voice AI agent lies in its ability to interact with existing tools through "tool calls" <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a><a class="yt-timestamp" data-t="10:18:00">[10:18:00]</a>.

### Airtable for Data Tracking
The "Lowballer 9000" leverages Airtable as a database to record every call it places <a class="yt-timestamp" data-t="10:31:00">[10:31:00]</a>. After a conversation, a tool call analyzes the entire transcript to determine if an offer was received, if the lowball was accepted, and the final price <a class="yt-timestamp" data-t="10:58:00">[10:58:00]</a>. This allows for easy sifting through hundreds of calls to find actionable outcomes <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>.

### Lindy for Flexible Data Processing
Lindy is an AI tool particularly effective at flexibly processing large amounts of text and structuring it into spreadsheets <a class="yt-timestamp" data-t="12:47:00">[12:47:00]</a>. For example, if adding a new column like "vegan friendly" to a restaurant research spreadsheet, Lindy can automatically read the column name and populate it based on provided text (e.g., website scrapes or menus), eliminating the need for manual rule writing or logging back into automation platforms <a class="yt-timestamp" data-t="13:32:00">[13:32:00]</a><a class="yt-timestamp" data-t="14:16:00">[14:16:00]</a>. This capability makes [[integration_of_ai_in_business_plan_development | business plan development]] more dynamic and responsive to changing data needs.

## [[challenges_and_opportunities_in_voice_ai_deployment | Challenges in Voice AI Deployment]]

A significant hurdle in deploying voice AI for outbound calls is ensuring that calls actually ring phones rather than going straight to voicemail <a class="yt-timestamp" data-t="14:57:00">[14:57:00]</a>. This is often due to regulations like STIR/SHAKEN, an FCC mechanism that requires phone numbers to be registered in a database for KYC (Know Your Customer) purposes. Failing to register can result in calls being blocked <a class="yt-timestamp" data-t="15:07:00">[15:07:00]</a>.

## [[use_cases_for_ai_agents_in_business_operations | Business Applications and Use Cases]]

Beyond specific negotiation scenarios, voice AI agents present broad [[business_applications_of_ai_prompting | business applications of AI prompting]] and opportunities for various industries:

*   **Sales Prospecting**: Voice AIs can automate initial outreach for sales. For instance, in real estate, an AI can call a prospect list to ask qualifying questions (e.g., about recent family events or house market plans) to identify leads with a higher probability of putting their house on the market <a class="yt-timestamp" data-t="16:20:00">[16:20:00]</a><a class="yt-timestamp" data-t="16:59:00">[16:59:00]</a>.
*   **Data for Arbitrage and Unfair Advantage**: Voice AI is excellent for gathering specific data, creating an "unfair advantage" in markets <a class="yt-timestamp" data-t="17:30:00">[17:30:00]</a>. By collecting granular information (like watch prices from numerous dealers), businesses can identify arbitrage opportunities—buying low and selling high at scale <a class="yt-timestamp" data-t="17:42:00">[17:42:00]</a><a class="yt-timestamp" data-t="19:08:00">[19:08:00]</a>. The core principle is that if knowledge provides an unfair advantage, there is likely a voice AI opportunity <a class="yt-timestamp" data-t="18:28:00">[18:28:00]</a>.
*   [[utilizing_ai_for_internal_business_communication | Automated Feedback Collection]]: Voice AIs can serve as automated feedback bots, allowing users to "brain dump" their thoughts vocally instead of filling out forms <a class="yt-timestamp" data-t="20:24:00">[20:24:00]</a>. This feedback can then be categorized, classified, and summarized (e.g., posted to a Slack channel) to improve services and products efficiently <a class="yt-timestamp" data-t="20:58:00">[20:58:00]</a><a class="yt-timestamp" data-t="21:39:00">[21:39:00]</a>. This represents a significant business opportunity for companies offering such services <a class="yt-timestamp" data-t="22:03:00">[22:03:00]</a>.