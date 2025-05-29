---
title: Tools and models for voice automation
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

Tony, an automation expert from SA Checkout, demonstrates how he used [[building_and_optimizing_voice_ai_agents | voice AI]] to lowball luxury watch dealers for a Rolex Daytona, a $35,000 watch, with some success <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. He believes people are significantly underestimating the capabilities of [[voicefirst_interfaces_and_their_future_potential | voice AIs]] and that any phone-based work could be automated within the next 1 to 3 years <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. He shares the tools, workflows, and prompts used for this project <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Lowballer 9000: An AI Voice Agent Example

Tony's [[building_and_optimizing_voice_ai_agents | voice AI]], named Alex (also known as Lowballer 9000), was designed for one primary task: to find a Rolex Daytona by contacting secondhand luxury watch dealers <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. The AI's job involves gathering critical details like the watch's condition, original documentation, and packaging, as these factors significantly impact the quoted price <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. The targets for these calls were independent secondhand dealers, not official Rolex factory dealers <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

## Core Tool: Vapi

The primary platform used for this project is Vapi, which stands for "Voice API" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. Vapi offers a flexible way to build voice agents, allowing users to "bring your prompt, pick your providers for your different services, and then literally hit go and run it" <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

### Prompt Engineering and Refinement

The prompt for Lowballer 9000 was primarily written by Tony, drawing inspiration from Vapi's documentation on general best practices <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. A significant part of prompt development involves an iterative process of testing and reacting to the AI's responses <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

Key prompt refinement strategies include:
*   **Conciseness**: Initially, the AI would "ram every single question... down my throat within the first term" <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. This was addressed by instructing the AI to "keep responses concise. One to two sentences max" <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   **Language Level**: Tony discovered that most human conversations happen at a "sixth grade English level" <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. Changing the prompt to "only use like sixth grade English" resulted in significantly longer call durations and more human-sounding interactions <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. This approach is like "patching the holes" in a sinking boat, incrementally improving the AI's performance <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

### AI Models and Temperature

The choice of AI model is "flavor of the month" dependent <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. Tony initially used DeepSeek, which was cost-effective but later crashed due to high demand, causing the bot to stop responding to calls <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. The current model used is Gemini 20 Flash <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

The **temperature** setting controls how creative the AI's responses are <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>:
*   A temperature closer to zero creates a more deterministic and predictable system <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. However, it may fail to respond appropriately to uncommon questions <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   A higher temperature (e.g., 1) allows for more creative and flexible responses.

### Voice Configuration

Vapi allows users to select specific voices. For Lowballer 9000, Tony chose "Cartisia" and "New York man," which was humorously noted to sound like a Sopranos-inspired voice <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

## Extending Functionality with Tool Calls

A significant feature of Vapi is **tool calling**, which enables the [[building_and_optimizing_voice_ai_agents | voice AI]] to interact with existing tools and services <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

### Call Recording and Analysis with Airtable

To manage over 800 calls, Tony integrated Vapi with an Airtable spreadsheet (dubbed "watch list") <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. After each conversation, a tool call takes the entire transcript and analyzes it to determine:
*   If an offer was received <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   If the AI successfully lowballed the dealer <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   The final price offered by the dealer, even if the lowball was not accepted <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.
This integration allowed Tony to easily sift through calls to find actionable offers for his content <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. The "get best offer" tool talks to the Airtable spreadsheet to retrieve and use the best offer during negotiation <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.

### Flexible Data Processing with Lindy

Lindy is highlighted as an effective tool for flexibly taking large amounts of text and organizing it into a spreadsheet <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>. For example, if researching restaurants and needing to add a "vegan friendly" column halfway through, Lindy can automatically read the column name and the text content (e.g., website scrape or menu) to check the relevant box without requiring manual rule writing or logging back into an automation <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>. This capability makes a powerful combination with Vapi <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

## Telephony Integration: Twilio

A critical hurdle in setting up voice AI calls is ensuring they actually ring phones instead of going straight to voicemail <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>. This often involves adherence to regulations like **Shake and Stir**, an FCC mechanism requiring phone numbers to be registered in a database for KYC (Know Your Customer) <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. Failure to register can result in calls being sent directly to voicemail <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>. Tony notes that he had at least 300 calls go to voicemail before addressing this <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.

## Broader [[applications_of_voice_ai_in_sales_and_feedback_collection | Applications of Voice AI]]

The potential of [[voicefirst_interfaces_and_their_future_potential | voice AI]] extends beyond specific use cases:

*   **Sales**: [[applications_of_voice_ai_in_sales_and_feedback_collection | Voice AIs]] can automate prospecting calls in industries like real estate. For example, an AI can ask specific questions to identify prospects whose homes are likely to enter the market soon, calling thousands of numbers to gather leads for human follow-up <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.
*   **Data Collection for Arbitrage**: [[building_and_optimizing_voice_ai_agents | Voice AI agents]] are excellent for gathering data, which can provide an unfair advantage <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>. This data can enable arbitrage businesses, such as identifying items to buy low and sell high <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>. If knowing more than competitors is an advantage, there's likely a [[voice_ai_in_business_negotiation | voice AI]] opportunity <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.
*   **Feedback Collection**: An example within Startup Empire (a private membership for building cash-flowing internet businesses) is a [[applications_of_voice_ai_in_sales_and_feedback_collection | voice AI]] feedback bot <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>. This bot allows users to "brain dump" their feedback via a phone call, which the AI then categorizes, classifies, and summarizes into a Slack channel for the team <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>. This automates the feedback process, making it easier to improve services <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>. This setup, involving a voice AI for input and Lindy for summarization/categorization, represents a marketable business idea for other companies <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.

Ultimately, [[building_and_optimizing_voice_ai_agents | voice AI agents]] enable the collection of valuable data at scale, creating opportunities for automation and competitive advantage in various business contexts <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.