---
title: Applications of voice AI in sales and feedback collection
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

Voice AI is rapidly advancing, with the potential to automate phone-based work within the next one to three years <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This technology can be leveraged to gain an unfair advantage through efficient data collection and process automation <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.

## Case Study: Lowballer 9000 - Voice AI in Sales Negotiation

Tony, an [[Using AI for business automation | automation]] expert, demonstrated a [[voice_ai_in_business_negotiation | voice AI]] he created, dubbed "Lowballer 9000," whose job was to lowball luxury watch dealers across the US for a Rolex Daytona <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>, a watch valued at $35,000 <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. The AI, named Alex, specifically targeted secondhand dealers, not official Rolex stores <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

### Objectives of Lowballer 9000
Alex's primary goal was to find a Rolex Daytona, but it also needed to gather critical details during conversations with dealers, such as:
*   The watch's condition <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>
*   Availability of original documentation and packaging <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>
These details dramatically impact the quoted cost of the watch <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### Tools and Workflows
The project utilized several key [[Tools and models for voice automation | tools and models for voice automation]]:

*   **Vapi (`vapi.ai`)**: This platform, which stands for Voice API, is used for [[Building and optimizing voice AI agents | building and optimizing voice AI agents]] <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. It's flexible, allowing users to bring their own prompts and choose their preferred providers for different services <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Prompt Engineering**:
    *   The prompt was initially written by Tony, informed by Vapi's best practices documentation <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    *   It was iteratively refined through testing and observation of real-life lowballers <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
    *   Specific rules were added to improve natural conversation flow, such as "Keep responses concise. One to two sentences max" to prevent the AI from "ramming every single question... down my throat" <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   A significant improvement came from instructing the AI to use "sixth grade English" <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>, which resulted in longer call durations and a more human-like sound <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **AI Model Selection**: Tony initially used DeepSeek before its popularity surged, saving money on calls <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. However, DeepSeek's API became "slammed," causing the bot to crash and not respond during calls <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. He later used Gemini 2.0 Flash <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. The choice of model depends on availability and performance <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   **Temperature Setting**: A "temperature" setting of one (on a scale where zero is deterministic) was used to allow for creative responses, as a lower temperature might cause the AI to fail when encountering uncommon questions <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
*   **Voice Configuration**: The "Cartisia" voice, also called "New York man" (a reference to a popular fictional character), was used to give the AI a distinct persona <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Tool Calls and Data Management**:
    *   One of Vapi's most powerful features is its ability to interact with existing tools via "tool calls" <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
    *   Tony integrated an AirTable spreadsheet (his "watch list") to record all calls <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
    *   A `get best offer` tool was created to analyze transcripts post-call and automatically determine if an offer was received, the lowball amount, acceptance, and final price <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. This made it easy to sift through over 800 calls for actionable results <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.
*   **Twilio for Calls**: A major hurdle was ensuring calls actually rang phones and didn't go straight to voicemail <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. This requires users to register their phone numbers and complete KYC (Know Your Customer) due to FCC regulations like "shake and stir" <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.

### General Sales Use Cases
Beyond luxury watch negotiation, [[creating_automated_marketing_and_sales_processes_with_ai | AI voice agents]] can be used for sales in various industries <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>:
*   **Real Estate Prospecting**: An AI can call prospects to ask specific questions, identifying homes likely to enter the market soon and generating qualified leads at scale <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.
*   **Data Arbitrage**: Voice AI is excellent for gathering data to create an "unfair advantage" or arbitrage <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>. For example, buying a watch for $19,000 via the AI and selling it for $22,000 on the secondary market creates a $3,000 profit per transaction, which can then be scaled and even further automated by dispatching teams to pick up items <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.

> "If knowledge is an unfair advantage and knowing something more than your competitor, then chances are that there's a [[Voicefirst interfaces and their future potential | voice AI]] opportunity there." <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>

## Case Study: Startup Empire Feedback Bot - Voice AI for Feedback Collection

Tony also discussed another application of voice AI: collecting feedback for Startup Empire, a private membership for building cash-flowing internet businesses <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>.

### Problem and Solution
Traditional feedback forms are often cumbersome and prevent users from providing detailed "brain dumps" of their thoughts <a class="yt-timestamp" data-t="00:20:34">[00:20:34]</a>. To address this, a [[advanced_ai_voice_note_applications | voice AI]] was created to listen to members' feedback <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>.

### Workflow and Benefits
*   Members call a dedicated number to provide feedback, whether positive or negative <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>.
*   The [[building_and_optimizing_voice_ai_agents | voice AI]] processes this information.
*   [[Using AI to create voice character apps | Lindy]], another AI tool, is used to take the spoken feedback, summarize it, and categorize/classify it <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>.
*   This summarized feedback is then automatically posted to a Slack channel used by the Startup Empire team <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>.
*   This automated feedback collection allows the team to receive insights directly, without having to actively seek them out, and use them to improve the service <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>.

### Business Opportunity
This feedback collection service presents a significant business opportunity, as many companies would pay for such an automated, categorized, and reported feedback system <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>.

---
For more insights from Tony, his social media and YouTube channel are available in the show notes <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>. He also provides demos and content within Startup Empire <a class="yt-timestamp" data-t="00:20:02">[00:20:02]</a>.