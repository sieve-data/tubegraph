---
title: Challenges and Opportunities in Voice AI Deployment
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

Voice AIs are capable of much more than commonly estimated, with the potential to automate phone-based work within the next 1 to 3 years <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. The deployment of these agents involves specific considerations, from technical setup to strategic application.

## Case Study: The Lowballer 9000 Voice AI

A practical example of [[building_and_configuring_voice_ai_agents | building and configuring a voice AI agent]] is the "Lowballer 9000," an AI named Alex designed to lowball luxury watch dealers in the US for Rolex Daytonas <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The goal was to acquire a $35,000 watch and demonstrate the capability of voice AIs in real-world business negotiations <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

This AI's job was to:
*   Identify luxury watch dealers, specifically second-hand dealers, not official Rolex factories <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   Gather critical details like the watch's condition, original documentation, and packaging, which significantly impact the quoted cost <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   Attempt to lowball offers and record the outcomes <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Tools and Platforms for Voice AI Deployment

### Vappy
The platform used for this deployment was Vappy (Voice API), chosen for its flexibility in [[building_and_configuring_voice_ai_agents | building voice agents]] <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. It allows users to bring their own prompts and select different service providers <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

### Prompt Engineering
A significant aspect of [[challenges_and_solutions_in_ai_app_development | AI app development]] and deployment is prompt engineering. The prompt for Lowballer 9000 was self-written, but its refinement was an iterative process driven by real-world testing and reactions <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This highlights a key [[challenges_in_coding_with_ai | challenge in coding with AI]]:

*   **Iterative Refinement:** Initial tests revealed issues, such as the AI asking too many questions at once, making it sound "not engaging" and "obviously AI" <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. This required patching the prompt to ensure concise responses, typically one to two sentences max <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   **Language Level:** A crucial insight was to instruct the AI to use "sixth-grade English" for more human-like conversations and longer call durations, as most human conversations occur at this level <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

### Model Selection
Choosing the right AI model is crucial for deployment. The "model game" is often dictated by the "flavor of the month" <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
*   **Challenge:** The Lowballer 9000 initially used DeepSeek, which saved money but later crashed due to high demand (hype cycle), causing the bot to become unresponsive <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. This emphasizes the need to select models that are readily available and stable <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   **Temperature Parameter:** The "temperature" setting (e.g., Temperature 1 for Lowballer 9000) controls the creativity of the AI's responses <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. A lower temperature (closer to zero) results in a more deterministic and predictable system, but it may fail to respond appropriately to uncommon questions <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

### Voice Configuration
For realistic [[voicefirst_interfaces_and_applications | voice-first applications]], selecting an appropriate voice is key. Vappy allows for voice configuration, with options like "Cartisia" (also known as "New York man"), which was used for Lowballer 9000 to mimic a Sopranos-like character <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. This falls under [[using_ai_to_create_voice_character_apps | using AI to create voice character apps]].

### Tool Calling and Integration
One of the most powerful aspects of voice AI deployment is tool calling, which allows the AI to interact with existing external tools <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

*   **Data Management:** The Lowballer 9000 integrates with an Airtable spreadsheet (a "watch list") to record all calls placed <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
*   **Automated Analysis:** A tool call was set up to automatically analyze the entire transcript after a conversation, determining if an offer was received, if the lowball offer was accepted, or if another price was given <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>. This allowed for efficient sifting through 800+ calls to find actionable insights <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.
*   **Lindy Integration:** Lindy is highlighted for its ability to flexibly take large amounts of text and organize it into spreadsheets <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. It can automatically add data based on column names (e.g., "vegan friendly" for restaurants) without manual re-configuration, streamlining data processing for AI applications <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.

### Twilio and Regulatory Hurdles
A significant deployment challenge was ensuring calls actually rang phones, often due to regulatory mechanisms like "shake and stir" <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.
*   **Challenge:** The FCC's "shake and stir" rule requires phone numbers to be registered in a database for KYC (Know Your Customer) purposes; otherwise, calls may go straight to voicemail <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>. This resulted in over 300 calls going to voicemail for the Lowballer 9000 <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.
*   **Solution:** Users must bring their own registered phone numbers and complete KYC to ensure successful call placement <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.

## Opportunities and Use Cases for Voice AI

[[Building and deploying AI agents for business tasks | Building and deploying AI agents for business tasks]] offers numerous opportunities across various industries.

*   **Automation of Phone-Based Work:** Any work conducted over the phone has the potential to be automated <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   **Sales and Lead Qualification:**
    *   Voice AIs can call prospect lists in industries like real estate to qualify leads, asking targeted questions (e.g., about family status or property market intentions) to identify high-potential prospects <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.
    *   By making thousands of calls, AIs can generate lists of individuals who meet specific criteria for sales teams to pursue <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>.
*   **Arbitrage Businesses:**
    *   Voice AIs excel at gathering data, which can provide an unfair advantage in arbitrage opportunities <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>. For example, the Lowballer 9000 demonstrated how to identify luxury watches at low prices to resell for profit <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>.
    *   This concept can be applied to any business where knowing something more than a competitor (data/knowledge) provides an advantage <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.
*   **Customer Feedback Collection:**
    *   A voice AI can act as a "feedback bot," allowing users to "brain dump" their thoughts via phone calls instead of filling out forms <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>.
    *   This raw feedback can then be categorized, classified, and summarized by other AI tools (like Lindy) and posted directly to internal channels (e.g., Slack) for immediate use in service improvement <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>. This presents a business idea to offer this service to other companies <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>.

These [[opportunities_in_ai_design_for_startups | opportunities in AI design for startups]] highlight the transformative potential of voice AI in acquiring valuable data and automating key business processes.