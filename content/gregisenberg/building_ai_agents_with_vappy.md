---
title: Building AI agents with Vappy
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

Vappy is a highly flexible platform designed for [[generating_and_deploying_ai_agents_with_nocode_tools | building AI agents]]. Specifically, it excels at creating voice agents by allowing users to bring their own prompts, select their preferred service providers, and then simply deploy the agent <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

## The "Lowballer 9000" Experiment

Tony, an automation expert, developed a voice AI he named "Lowballer 9000" (also called Alex) <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. The AI's purpose was to lowball luxury watch dealers across the U.S. for a Rolex Daytona, a watch valued at around $35,000 <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This experiment "kind of worked" <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

The project aimed to demonstrate the underestimated capabilities of voice AIs <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>, with the belief that any work performed over the phone could be automated within the next one to three years <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

### Alex's Mission

Alex's primary objective was to find a Rolex Daytona from secondhand luxury watch dealers <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. To do this, it needed to gather critical details during conversations, such as:
*   The condition of the watch <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   Whether all original documentation and packaging were available <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
These details significantly impact the watch's quoted cost <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## Key Aspects of Building with Vappy

### Prompt Engineering
The prompt for "Lowballer 9000" was self-written, incorporating general best practices from Vappy's documentation <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. The development of the prompt was an iterative and reactive process:
*   **Observation:** Studying how real-life lowballers interact with watch sellers <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   **Simulation & Refinement:** Simulating these conversations with Alex and then modifying the prompt based on undesirable AI responses <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. For instance, an early issue was Alex overwhelming sellers by asking all questions at once, leading to the prompt instruction to "Keep responses concise. One to two sentences max" <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
*   **Clarity:** A general lesson learned is that most conversations occur at a "sixth-grade English level." Adjusting the prompt to reflect this led to significantly longer call durations and more human-sounding interactions <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

### Model Selection
The choice of model in Vappy is often a "flavor of the month" scenario, meaning it's dependent on current trends and performance <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. While DeepSeek was initially used for its cost-effectiveness, it experienced crashes due to high demand, leading to the bot not responding to calls <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. The recommendation is to select a model that is currently available and stable <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

### Temperature Setting
"Temperature" in Vappy controls the creativity of the AI's responses <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
*   **Lower Temperature (closer to 0):** Results in a more deterministic and predictable system <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. However, it may struggle to respond appropriately to uncommon questions <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   **Higher Temperature:** Allows for more creative and varied responses.

### Voice Configuration
Vappy allows selection of different voices <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. For "Lowballer 9000," the "Cartisia, New York man" voice was chosen, humorously linked to a "very popular TV show" character <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

## Advanced Capabilities: Tool Calls

One of Vappy's most powerful features is its "tool calls," which enable a voice AI to interact with existing external tools <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

### Data Extraction and Analysis
For the "Lowballer 9000" project, tool calls were used to:
1.  **Record Calls:** Every call placed by the AI was recorded <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
2.  **Analyze Transcripts:** After each conversation, a tool call took the entire transcript and determined if an offer was received, whether the bot engaged, the lowball amount, and if it was accepted <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>. This data was then sent to an AirTable spreadsheet (referred to as a "watch list") <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
This process allowed for easy sifting through over 800 calls to identify those that resulted in actionable offers, crucial for content creation <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.

### Integration with Lindy
Vappy can integrate with other tools like Lindy, which excels at flexibly taking large amounts of text and structuring it into spreadsheets <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>. Lindy can automatically infer and populate data based on column names in a spreadsheet. For example, if a "vegan friendly" column is added, Lindy can read a restaurant menu and automatically check the box based on the content <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.

## Critical Setup: Twilio and Phone Number Registration

A significant hurdle in deploying voice AIs is ensuring calls actually ring the recipient's phone <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. Due to FCC regulations like STIR/SHAKEN, unregistered phone numbers may have their calls go straight to voicemail <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. Therefore, it's crucial to:
1.  Bring your own phone number <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
2.  Complete KYC (Know Your Customer) registration for the number <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.
Failing to do so can result in hundreds of calls going unanswered <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.

## Use Cases and Business Opportunities for Voice AI Agents

Voice AI agents offer significant potential for automation and business advantages:

*   **Automation of Phone-Based Work:** Any task currently done over the phone can be automated <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   **Sales and Lead Generation:**
    *   **Real Estate:** An AI can call a prospect list to inquire about potential property sales (e.g., recent family passing, house going on market soon) <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>. By asking specific questions, the AI can identify leads with a higher probability of putting their house on the market, then pass these qualified leads to human agents <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.
*   **Arbitrage Businesses:** Voice AI can be used to gather data that creates an unfair advantage, leading to arbitrage opportunities <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>.
    *   **Example:** In the watch market, an AI can identify watches that can be bought at a low price (e.g., $19,000) and then resold on the secondary market for a profit (e.g., $22,000) <a class="yt-timestamp" data-t="00:19:09">[00:19:09]</a>. This can be scaled and even automated further by dispatching a team to pick up the item once an offer is accepted <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.
    *   This framework suggests that if "data is an unfair advantage," or "knowledge is an unfair advantage," then a voice AI opportunity likely exists <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.
*   **Customer Feedback Collection:** Voice AIs can collect unstructured feedback more efficiently than traditional forms <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>.
    *   **Startup Empire Example:** A voice AI is used to collect feedback from members of Startup Empire, a private membership for [[building_ai_agents_for_business_automation | building cash-flowing internet businesses]] <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>. Members can "brain dump" their thoughts, which the AI then categorizes, classifies, and summarizes, posting it to a Slack channel. This allows for immediate and convenient access to member feedback for product improvement <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>.

This demonstrates the potential for [[ai_agents_in_problemsolving | AI agents in problem-solving]] and [[setting_up_ai_agents_as_virtual_employees | setting up AI agents as virtual employees]] for various business functions.