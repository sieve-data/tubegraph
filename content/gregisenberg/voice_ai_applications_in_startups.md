---
title: Voice AI applications in startups
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

Voice AI is rapidly advancing, with the potential to automate much of the work currently done over the phone within the next one to three years <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This creates significant [[ai_opportunities_for_startups | AI opportunities for startups]] to leverage this technology for various business functions.

## Case Study: The "Lowballer 9000" Voice AI

Tony, an automation expert, developed a voice AI named "Lowballer 9000" (also referred to as Alex) to negotiate prices for Rolex Daytonas with secondhand luxury watch dealers across the US <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>, <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. The AI's primary goal was to lowball dealers for a $35,000 watch, and the experiment "actually kind of worked" <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

### AI's Role and Target Audience
The AI's specific job was to seek out a Rolex Daytona and interact with luxury watch dealers <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. It needed to gather critical details such as the watch's condition, whether original documentation was available, and if the original packaging was included, as these factors significantly impact the watch's quoted cost <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. The AI targeted secondhand dealers, not official Rolex stores <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

### Tools and Workflow

The core platform used for this project was **Vappy** <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. Vappy acts as a flexible voice API that allows users to bring their own prompts and select their preferred service providers for different functionalities <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

#### Prompt Engineering
The prompt for the AI was developed by Tony, informed by Vappy's best practices documentation <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. The process was iterative, involving:
1.  **Observation**: Watching real-life watch sellers lowballing to understand negotiation tactics <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
2.  **Simulation & Refinement**: Simulating these conversations with the Vappy AI and adjusting the prompt based on undesirable AI responses <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. For example, initially, the AI would ask all questions at once, which sounded unnatural. The prompt was adjusted to keep responses concise, ideally one to two sentences max <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
3.  **Language Level**: A key learning was that most conversations occur at a "sixth-grade English level" <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. Changing the prompt to use simpler language significantly increased call durations and made the AI sound more human <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

#### Model Selection
The choice of AI model is often dynamic, akin to a "flavor of the month" <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. The project initially used DeepSeek due to cost-effectiveness, but DeepSeek's API became "slammed" during a hype cycle, causing the bot to crash and not respond to calls <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>, <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. This highlights the importance of choosing a currently available and reliable model <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

#### Temperature Setting
The "temperature" setting in the AI model dictates how creative its responses will be <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. A temperature closer to zero yields a more deterministic, predictable system, but it may struggle to respond appropriately to uncommon questions <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

#### Voice Selection
The AI's voice was configured using "Cartisia," described as a "New York man" voice, deliberately chosen for its resemblance to a character from "The Sopranos" to give it a distinct "Italian" or "New Jersey" man persona <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>, <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

#### Tool Calling and Data Management
A powerful aspect of Vappy is its ability to interact with existing tools through "tool calls" <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>, <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. For the "Lowballer 9000," this involved:
*   **Call Recording and Analysis**: A tool was created to record calls and, once a conversation concluded, analyze the transcript to determine if an offer was received, if the AI lowballed them, and the final price <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.
*   **Database Integration (AirTable)**: This data was automatically stored in an AirTable spreadsheet, functioning as a "watch list" database for all calls <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. This streamlined the process of sifting through over 800 calls to identify actionable offers <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
*   **Lindy Integration**: The system also integrated with Lindy, an AI tool adept at flexibly taking large amounts of text and structuring it into spreadsheets <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. Lindy can read column names (e.g., "vegan friendly") and automatically extract relevant information from text (e.g., a restaurant menu) to populate the spreadsheet, eliminating manual rule-writing for data classification <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.

#### Technical Hurdles: Twilio and FCC Compliance
A significant bottleneck encountered was ensuring calls actually rang through to phones <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>. This was due to FCC regulations, specifically "shake and stir," which require phone numbers to be registered in a database (KYC) to prevent calls from going straight to voicemail <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. Bringing a registered phone number and completing KYC is crucial for successful outbound calling <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.

## Broader Use Cases for Voice AI in Startups

Voice AI presents substantial opportunities for [[building_ai_startup_using_ai_tools | building AI startup using AI tools]] and [[building_a_successful_ai_startup | building a successful AI startup]].

### Sales and Prospecting
Voice AI can automate sales calls, especially for lead qualification. For example, in real estate, an AI could call prospects to determine if a family member has recently passed or if a house is likely to go on the market soon <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>. By asking a few targeted questions, the AI can identify high-potential leads that a human can then pursue <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.

### Data Collection and Arbitrage
A core strength of building Vappy AI voice agents is efficiently gathering data to create an "unfair advantage" <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>. The watch lowballing example itself demonstrates how data (e.g., dealer prices) can enable an arbitrage business with thousands of dollars in profit potential <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>.

The framework for [[ai_startup_ideas | AI startup ideas]] or [[ai_startups_and_business_ideas | AI startups and business ideas]] is to identify businesses where acquiring specific data or knowledge provides a competitive edge <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>. If knowledge is an unfair advantage, there's likely a [[voice_ai_in_business_negotiations | voice AI in business negotiations]] opportunity <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>. This can create a more transparent secondary market <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a>.

### Customer Feedback Collection
Voice AI can revolutionize feedback processes. For example, a voice AI feedback bot was developed for Startup Empire, a private membership for entrepreneurs <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>. Instead of filling out tedious forms, members can call a number and "brain dump" their feedback (positive or negative) to the AI <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>. This voice feedback is then summarized and posted to a Slack channel, categorized and classified using tools like Lindy, allowing the team to easily review and improve their service <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>, <a class="yt-timestamp" data-t="00:21:59">[00:21:59]</a>. This concept could be offered as a service to other companies <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>.

> "If knowledge is an unfair advantage and knowing something more than your competitor, then chances are that there's a voice AI opportunity there." <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>

The potential for [[ai_startup_ideas_for_micro_apps | AI startup ideas for micro apps]] and [[integrating_ai_tools_in_building_saas_startups | integrating AI tools in building SaaS startups]] is vast, especially when combined with voice AI for data acquisition and process automation.