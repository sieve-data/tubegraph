---
title: Voice AI in business negotiations
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

Voice AIs are capable of automating phone-based work, with the potential for widespread adoption within the next one to three years <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. These AI agents can be developed to handle complex tasks, such as business negotiations, by interacting with existing tools and adapting their communication style for more effective outcomes <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

## Case Study: The "Lowballer 9000" AI

Tony, an automation expert, created a voice AI named "Alex" (dubbed "Lowballer 9000") designed to negotiate prices for Rolex Daytona watches with secondhand luxury watch dealers across the US <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>, <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This AI's primary job is to find Rolex Daytonas and, knowing it's speaking with dealers, it performs several critical functions:
*   Gathers details: Inquires about the watch's condition, original documentation, and packaging, as these significantly impact the quoted cost <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   Negotiates: Engages in a lowballing strategy to acquire the watches <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.
*   Records data: Logs call transcripts and determines if an offer was received, the lowball amount, and if it was accepted, or if a final counter-price was given <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>, <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. This data helps in identifying actionable calls from hundreds of interactions <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>, <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.

### Key Tools and Components

*   **[[building_voice_ai_agents_with_vappy | Vappy]]**: This platform was used to build the voice AI agents <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. [[building_voice_ai_agents_with_vappy | Vappy]] offers flexibility, allowing users to integrate their own prompts and select various service providers <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **Prompt Design**: The AI's prompt was developed through iterative testing and observation of real-world human negotiation behaviors <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>, <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. Key refinements included:
    *   **Conciseness**: Keeping responses brief (one to two sentences max) to avoid overwhelming the recipient and sound more natural <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>, <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   **Simplicity**: Instructing the AI to use "sixth grade English" to increase call durations and make conversations sound more human <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>, <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **AI Model Selection**: The choice of AI model (e.g., Gemini 2.0 Flash) is dependent on factors like cost and availability <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>, <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. API reliability is crucial, as some models can become "slammed" during hype cycles, leading to unresponsiveness <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>, <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
*   **Temperature Setting**: This setting controls the AI's creativity. A temperature of one indicates a desire for more creative responses, whereas a setting closer to zero would result in more predictable, deterministic answers, which might fail when facing uncommon questions <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>, <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   **Voice Configuration**: The voice can be customized (e.g., "Cartisia" or "New York man") to match the desired persona for the AI <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>, <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.
*   **Tool Calls**: Voice AIs become powerful when they can interact with other tools. For the "Lowballer 9000," this includes:
    *   **AirTable Integration**: A tool call (`get best offer`) is used to communicate with an AirTable spreadsheet (database) to record and track all calls, especially those resulting in offers <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>, <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
    *   **[[leveraging_ai_for_business_efficiency | Lindy]] Integration**: [[leveraging_ai_for_business_efficiency | Lindy]] is used for flexible data extraction and classification, taking large amounts of text (like call transcripts) and populating spreadsheets, even adding new columns automatically based on context <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>, <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>, <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.
*   **Twilio**: Essential for initiating phone calls. Users must bring their own registered numbers and complete KYC (Know Your Customer) to comply with "shake and stir" FCC regulations, preventing calls from going straight to voicemail <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>, <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.

## [[practical_use_cases_for_ai_agents_in_business | Practical Use Cases for Voice AI Agents]]

Beyond watch negotiations, voice AI agents have broad applicability in business:

*   **Sales and Prospecting**: Automating outreach to prospect lists, such as in real estate, to gather specific information (e.g., likelihood of a house entering the market) <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.
*   **Data Collection for Arbitrage**: Voice AIs excel at gathering data that can create an unfair advantage, enabling arbitrage opportunities in various markets <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>, <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>. If knowledge or data provides a competitive edge, there's likely a voice AI opportunity <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.
*   **Customer Feedback Collection**: Voice AIs can collect detailed feedback through unstructured "brain dumps," categorize it, and use it to improve services <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>, <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>. This feedback can then be automatically summarized and posted to internal communication channels (like Slack) <a class="yt-timestamp" data-t="00:21:19">[00:21:19]</a>, <a class="yt-timestamp" data-t="00:21:39">[00:21:39]</a>. This represents a potential business idea for offering such a service to other companies <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.

Ultimately, voice AI agents can provide an [[automating_business_processes_with_ai | automated]] means to gather critical data at scale, offering significant advantages in business and negotiation <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>, <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.