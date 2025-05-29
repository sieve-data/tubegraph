---
title: Voice AI in business negotiations
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

Voice AI technology is emerging as a powerful tool for automating tasks, particularly those involving phone interactions and data gathering, offering significant advantages in business negotiations and sales. One notable example is the "lowballer" AI, designed to negotiate prices for luxury watches <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## The Lowballer 9000 AI: A Case Study

Tony, an automation expert, developed a voice AI named "Lowballer 9000" (also known as Alex) with the specific goal of acquiring a Rolex Daytona for a significantly reduced price <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This AI targeted secondhand luxury watch dealers across the US <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

### AI's Objective and Information Gathering
Alex's primary job was to find a Rolex Daytona <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. To do this, it needed to gather critical details from dealers, such as:
*   The watch's condition <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>
*   Availability of original documentation and packaging <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>
These details are crucial as they can dramatically impact the quoted cost of the watch <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### Tools and Setup
The voice AI was built using several key technologies:

*   **Vappy:** This platform, essentially a "voice API," provides a flexible way to [[building_ai_agents_for_business_automation | build voice agents]]. It allows users to bring their own prompts, select various service providers, and run the agent without proprietary lock-in <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **Prompt Engineering:** The AI's prompt was primarily written by Tony, with iterative refinement based on testing <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    *   **Iterative Testing:** The process involved observing how real-life lowballers interacted with watch sellers and then simulating those conversations with Alex <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. If Alex responded inappropriately (e.g., asking too many questions at once), the prompt was adjusted <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
    *   **Conciseness:** Prompts were designed to keep responses concise, typically one to two sentences max, to prevent errors and make the AI sound more natural <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   **Language Level:** A significant improvement in call duration and human-like interaction was observed when the prompt was refined to use "sixth-grade English" <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   **AI Model Selection:** The choice of AI model (e.g., Gemini 20 Flash, DeepSeek) is crucial and can be influenced by current trends, availability, and cost. Server load on popular models can lead to service disruptions <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   **Temperature Setting:** This parameter controls the creativity of the AI's responses <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. A temperature closer to zero makes the system more deterministic and predictable, while a higher temperature allows for more creative, but potentially off-topic, answers <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   **Voice Configuration:** The AI used a "Cartisia" voice, which sounded like a "New York man" or "Sopranos" character, adding to its persona <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Tool Calls:** A powerful feature of Vappy is its ability to integrate with existing tools <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. For the lowballer AI, a tool call was created to:
    *   Record all calls <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
    *   Analyze call transcripts post-conversation to determine if an offer was received, the lowball amount, and whether it was accepted <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
    *   This data was stored in an AirTable spreadsheet, allowing for easy sifting through hundreds of calls to find actionable information <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
*   **Twilio and Shake and Stir:** A critical hurdle in deploying the AI was ensuring calls actually rang through. The "Shake and Stir" FCC mechanism requires phone numbers to be registered with a database (KYC) to prevent calls from going straight to voicemail <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. Without proper registration, a significant number of calls might fail <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.
*   **Lindy Integration:** Lindy is effective at flexibly processing large amounts of text and structuring it into spreadsheets <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>. For example, it can automatically populate spreadsheet columns (like "vegan friendly" for restaurants) by reading column names and analyzing text content, eliminating manual rule writing in traditional automations <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.

## Broader Applications of [[voice_ai_technology_in_sales_and_real_estate | Voice AI Technology in Sales and Real Estate]]
The capabilities demonstrated by the lowballer AI highlight a broader potential for [[automated_business_with_ai_assistants | automated business with AI assistants]]:

*   **Automation of Phone-Based Work:** It is believed that any work conducted over the phone could be automated within the next 1 to 3 years <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   **Sales and Real Estate:** Voice AIs can be used for prospecting in industries like real estate. For example, an AI could call a prospect list, ask specific questions (e.g., about family passing or house going on the market), and identify leads with a higher probability of selling their house <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>. This allows businesses to call thousands of numbers and identify highly qualified prospects <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>.
*   **[[Automating business tasks with AI | Data-Driven Arbitrage Businesses]]:** Voice AI agents excel at gathering data, providing an [[automated_business_with_ai_assistants | unfair advantage]] <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>. The Rolex example demonstrates creating an arbitrage business by identifying watches at a low price and reselling them on the secondary market for profit <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>. Any business where "data is an unfair advantage" or "knowledge is an unfair advantage" presents a voice AI opportunity <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.
*   **Market Transparency:** Voice AI can contribute to more transparent secondary markets by efficiently gathering pricing information <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>.
*   **Customer Feedback Collection:** Voice AIs can be used to collect qualitative feedback from customers. For instance, a voice AI can listen to "brain dumps" from users, summarize their feedback, and categorize it for service improvement, as demonstrated by Startup Empire's feedback bot <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>. This automated feedback collection can integrate directly into platforms like Slack, providing real-time insights <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>. This concept could even be offered as a service to other companies <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.