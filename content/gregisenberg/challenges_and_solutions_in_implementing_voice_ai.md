---
title: Challenges and solutions in implementing voice AI
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

The capabilities of voice AIs are often drastically underestimated, with the potential for any phone-based work to be automated within the next 1 to 3 years <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Implementing such systems, however, involves various [[challenges_and_solutions_in_ai_app_development | challenges]] and requires specific solutions and best practices.

## Case Study: The "Lowballer 9000" Voice AI

Tony, an automation expert, developed a voice AI named "Lowballer 9000" (also known as Alex) to negotiate prices for Rolex Daytona watches with secondhand luxury watch dealers across the US <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This AI's primary job was to find a Rolex Daytona, knowing it was speaking to luxury watch dealers, and gather critical details such as the watch's condition, original documentation, and packaging, which significantly impact pricing <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

### Platform and Tools

The project utilized Vappy, a voice API platform designed for building flexible voice agents without locking users into proprietary systems <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. It allows users to bring their own prompts and select providers for different services <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

A critical hurdle was ensuring calls actually rang phones, which required integrating Twilio and adhering to FCC regulations like "Shake and Stir" <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. This means registering the phone number in a database for KYC (Know Your Customer) to prevent calls from going straight to voicemail <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>. Neglecting this step can result in hundreds of calls failing to connect <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.

### [[prompt_engineering_for_voice_ai | Prompt Engineering]] and Best Practices

Developing effective prompts for voice AIs is an iterative process <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. Tony's approach involved:
*   **Observational Learning:** Watching real-life lowballing conversations to simulate them with the AI <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   **Iterative Refinement ("Patching Holes"):** Adjusting the prompt based on undesirable AI responses. For example, to prevent the AI from "ramming every single question down [the user's] throat," the prompt was modified to "keep responses concise" and "one to two sentences max" <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
*   **Language Level:** A key discovery was that most human conversations occur at a "sixth-grade English level" <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. Adjusting the prompt to use simpler language significantly increased call durations and made the AI sound more human <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

### Model Selection and Configuration

*   **Model Dependence:** Model choice often depends on current trends, with specific models experiencing "hype cycles" <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
*   **Capacity Challenges:** High demand for popular models (like DeepSeek) can lead to API overload, causing the voice AI to crash or not respond to requests <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. The solution is to select an available model <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   **Temperature Parameter:** This setting controls the creativity of the AI's responses <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. A lower temperature (closer to zero) results in a more predictable, deterministic system, but it may struggle with uncommon questions <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   **Voice Configuration:** Platforms like Vappy offer various popular voices, allowing developers to choose a persona that fits the AI's role (e.g., "Cartisia" or "New York man" for a negotiation bot) <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

### Integration with Existing Tools

The power of voice AIs is greatly enhanced through "tool calls," allowing them to interact with other systems <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

*   **Data Collection and Analysis:** For the "Lowballer 9000," a tool call was created to record all calls to an AirTable database <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. After each conversation, the entire transcript is analyzed to determine if an offer was received, the lowball amount, and if it was accepted, or if another price was given <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>. This automation streamlined the process of sifting through hundreds of calls to find actionable insights <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.
*   **Flexible Data Structuring with Lindy:** Lindy, another AI tool, excels at flexibly taking large amounts of text and organizing it into spreadsheets <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. It can automatically read column names (e.g., "vegan friendly") and categorize information from text, eliminating the need to manually update rules for new data points <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. This capability enables seamless integration between voice AI transcripts and structured data <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.

## Voice AI Use Cases and Opportunities

Voice AI presents significant [[opportunities_and_challenges_in_the_ai_industry | opportunities and challenges in the AI industry]], especially for businesses. Any work done over the phone is susceptible to automation <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

*   **Sales and Prospecting:** Voice AIs can automate initial outreach in fields like real estate, asking qualifying questions from a prospect list to identify leads (e.g., properties likely to enter the market soon) <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.
*   **Data Arbitrage:** Voice AI agents are excellent for gathering data, which can provide an unfair advantage <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>. By collecting specific data (e.g., watch prices), businesses can identify arbitrage opportunities, like buying a watch low from one seller and selling it higher on a secondary market <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>. If data or knowledge is an unfair advantage, there is likely a voice AI opportunity <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.
*   **Automated Feedback Collection:** Voice AIs can be used to collect feedback from users or customers <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>. An example is a voice AI that allows community members (like those in Startup Empire) to "brain dump" their thoughts on a call <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>. This feedback can then be categorized, classified, summarized, and posted to platforms like Slack, providing continuous insights for service improvement <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>. This also highlights [[designing_user_experience_for_ai_apps | designing user experience for AI apps]] where voice input might be preferred over traditional forms.