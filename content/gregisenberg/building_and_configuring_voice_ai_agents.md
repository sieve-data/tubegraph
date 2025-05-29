---
title: Building and Configuring Voice AI Agents
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

Voice AIs are capable of much more than people currently estimate, with the potential to automate work done over the phone within the next one to three years <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. The process of [[building_apps_with_ai_tools | building apps with AI tools]] and specifically voice AI agents involves understanding tools, workflows, and prompts <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Case Study: The "Lowballer 9000" AI

Tony, an automation expert, created a voice AI named "Lowballer 9000" (also called Alex) <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Its purpose was to call secondhand luxury watch dealers in the U.S. and lowball them for a Rolex Daytona, a $35,000 watch <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

The AI's job was to:
*   Identify itself as looking for a Rolex Daytona <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   Recognize it was speaking to luxury watch dealers <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
*   Gather critical details, such as the watch's condition, original documentation, and packaging, which significantly impact the quoted price <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   Lowball offers to dealers <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Key Components and Tools for Voice AI Agents

### Voice Agent Platform: VAPI

VAPI is a flexible platform used for [[creating_and_customizing_ai_agents_for_specific_use_cases | building voice agents]] <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. It allows users to:
*   Bring their own prompts <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   Select providers for different services <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   Run the agent directly <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

### Prompt Engineering

Crafting an effective prompt is crucial for voice AI performance <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   **Iterative Process:** Prompts are often refined through testing and observation of AI responses <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. For example, if the AI asks too many questions at once, the prompt can be adjusted to ensure concise, one-to-two sentence responses <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   **Simplicity:** Using language at a "sixth-grade English level" can lead to longer call durations and more human-sounding interactions <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

### Model Selection

The choice of AI model can significantly impact performance <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
*   Models can be "flavor of the month," with popularity affecting availability <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
*   API reliability is a concern; a model's API being slammed can cause the bot to crash or not respond <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. Selecting a model that is currently available is recommended <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.
*   **Temperature Setting:** This parameter controls the creativity of the AI's responses <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
    *   A temperature closer to zero makes the system more deterministic and predictable <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
    *   Higher temperatures allow for more creative responses, which can be useful when handling uncommon questions <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

### Voice Configuration

Voice AI agents allow for specific voice configurations <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. For example, the "Lowballer 9000" used a voice labeled "Cartisia" or "New York man" <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

### [[function_calling_in_ai_voice_apps | Tool Calls]] and Integrations

The true power of a voice AI lies in its ability to interact with existing tools <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
*   **Data Collection and Analysis:** The Lowballer 9000 used a tool call to record and analyze all calls in a database (like an AirTable spreadsheet) <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. After each conversation, the AI would process the transcript to determine:
    *   If an offer was received <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
    *   If the bot engaged <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
    *   The lowballed amount <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
    *   Whether the lowball was accepted or if another price was given <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
    *   This enabled easy sifting through hundreds of calls to find actionable outcomes <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.
*   **Lindy Integration:** Lindy is particularly useful for flexibly extracting and organizing large amounts of text into spreadsheets <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. It can automatically categorize and classify information based on column names, such as determining if a restaurant is "vegan friendly" from a menu scrape <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.
*   **Feedback Bots:** A voice AI can be used to collect feedback by allowing users to "brain dump" verbally. This information can then be categorized, classified, summarized, and posted to platforms like Slack, providing instant, actionable insights for product improvement <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>.

### Telephony: Twilio and STIR/SHAKEN

A significant challenge in [[challenges_and_opportunities_in_voice_ai_deployment | voice AI deployment]] is ensuring calls actually ring through <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.
*   **Twilio:** This service is used for placing calls <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.
*   **STIR/SHAKEN:** This FCC mechanism requires phone numbers to be registered in a database for KYC (Know Your Customer) <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. Without proper registration, calls may go straight to voicemail <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>. It's crucial to bring your own registered number and complete KYC before placing calls <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.

## Use Cases and Business Opportunities

[[building_and_deploying_ai_agents_for_business_tasks | Building and deploying AI agents for business tasks]] offers numerous opportunities:
*   **Sales Automation:** Voice AIs can prospect leads by asking specific questions to qualify them. For example, in real estate, an AI could call a prospect list to identify houses likely to go on the market soon, then dispatch human agents to pursue qualified leads <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.
*   **Data Arbitrage:** Voice AIs are excellent for gathering data, providing an unfair advantage <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>.
    *   The "Lowballer 9000" demonstrated this by identifying opportunities to buy watches at low prices and resell them for significant profit <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>.
    *   This concept can be applied to any business where getting specific data allows for arbitrage <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>.
    *   If knowledge is an unfair advantage, there's likely a voice AI opportunity to collect that data <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.
*   **Customer Feedback Collection:** Voice AIs can automate the collection of customer feedback, making it easier for users to provide detailed input without filling out forms, and instantly summarizing it for internal teams <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>. This could be offered as a service to other companies <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>.

The ability to [[voice_ai_in_business_negotiations | use AI to create voice character apps]] and then automate negotiation or data collection on a massive scale presents significant opportunities for [[building_businesses_around_ai_agents | building businesses around AI agents]] and achieving high-volume arbitrage <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.