---
title: Voice AI technology in sales and real estate
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

Voice AI is rapidly changing how businesses operate, with the potential to automate phone-based work within one to three years <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Its capabilities are often underestimated <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## How a Voice AI Lowballed Luxury Watch Dealers

An illustrative example of [[building_ai_agents_for_business_automation | building AI agents for business automation]] involves a voice AI, affectionately named "Lowballer 9000" (or Alex), designed to negotiate with secondhand luxury watch dealers across the U.S. <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. The AI's objective was to find a Rolex Daytona, a watch valued around $35,000, and negotiate a low price <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. This experiment actually yielded results <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

The AI's negotiation process involved gathering critical details such as the watch's condition, original documentation, and packaging, as these factors significantly impact the quoted cost <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. The target audience for these calls was individual secondhand dealers, not official factory outlets <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

## Tools and Techniques for Building Voice AIs

The platform used for this [[ai_agent_platforms | AI agent platform]] was Vapi, described as a flexible voice API that allows users to bring their own prompts and select different service providers <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

Key aspects of developing an effective voice AI include:
*   **Prompt Engineering** The prompt used was initially written by the developer and refined through extensive testing <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. The process involved observing human negotiators and then simulating those conversations with the AI, making adjustments when the AI's responses were not ideal (e.g., asking too many questions at once) <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. A crucial tip for prompts is to instruct the AI to "keep responses concise" and use "one to two sentences max" to prevent it from overwhelming the caller <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. Additionally, writing prompts at a "sixth grade English level" can lead to longer, more human-sounding conversations <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   **Model Selection** The choice of underlying model (e.g., Gemini 20 Flash or DeepSeek) is crucial <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>. It's important to select a model that is available and not experiencing high demand that could lead to crashes or non-responses <a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>.
*   **Temperature Setting** The "temperature" setting controls the AI's creativity <a class="yt-timestamp" data-t="08:23:44">[08:23:44]</a>. A temperature closer to zero results in a more deterministic system, while a higher temperature allows for more creative and flexible responses to uncommon questions <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a>.
*   **Voice Configuration** Selecting a specific voice (e.g., Cartisia, known as "New York man") can enhance the AI's persona <a class="yt-timestamp" data-t="09:06:01">[09:06:01]</a>.
*   **Tool Calls** This is considered the most powerful feature of Vapi, allowing the voice AI to interact with existing tools and databases <a class="yt-timestamp" data-t="10:09:02">[10:09:02]</a>. For the watch negotiation AI, a tool call was set up to record all calls to a database (like Airtable) <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>. After each conversation, the AI analyzed the transcript to determine if an offer was received, the lowball amount, and whether the offer was accepted, streamlining the review of over 800 calls <a class="yt-timestamp" data-t="10:52:00">[10:52:00]</a>. This feature can also be integrated with tools like Lindy for flexible data management <a class="yt-timestamp" data-t="12:47:00">[12:47:00]</a>.
*   **Phone Number Registration** A significant hurdle was ensuring calls actually rang through and didn't go straight to voicemail due to FCC's Shake and Stir mechanism <a class="yt-timestamp" data-t="14:57:00">[14:57:00]</a>. Users must register their phone numbers and complete KYC (Know Your Customer) procedures with providers like Twilio to avoid calls being blocked <a class="yt-timestamp" data-t="15:32:00">[15:32:00]</a>.

## [[examples_and_use_cases_of_ai_agents | Use Cases of Voice AI in Sales]] and Real Estate

Voice AI presents a significant opportunity for [[using_ai_in_lead_generation and recruiting | using AI in lead generation and recruiting]] and sales:
*   **Real Estate Lead Generation** For real estate professionals, an AI can call a prospect list to identify potential sellers (e.g., if a family member recently passed or if a house is likely to go on the market soon) <a class="yt-timestamp" data-t="16:20:00">[16:20:00]</a>. By asking specific questions, the AI can filter leads, identifying properties with a higher chance of being listed in the next six months <a class="yt-timestamp" data-t="16:33:00">[16:33:00]</a>.
*   **Arbitrage Opportunities** Voice AI is excellent for gathering data, which can create an "unfair advantage" and facilitate arbitrage businesses <a class="yt-timestamp" data-t="17:32:00">[17:32:00]</a>. The watch example demonstrates this: an AI can find watches at low prices from one seller and then sell them on the secondary market for a profit <a class="yt-timestamp" data-t="19:09:00">[19:09:09]</a>. This concept can be applied to any business where knowing more than competitors provides an advantage <a class="yt-timestamp" data-t="18:25:00">[18:25:00]</a>.
*   **Automated Feedback Collection** A voice AI can be used to collect feedback from customers by allowing them to simply call a number and "brain dump" their thoughts <a class="yt-timestamp" data-t="20:27:00">[20:27:00]</a>. The AI can then categorize and summarize this information, posting it to internal channels (like Slack), thus providing valuable insights without manual data entry <a class="yt-timestamp" data-t="20:58:00">[20:58:00]</a>. This type of service could be offered to other companies <a class="yt-timestamp" data-t="22:04:00">[22:04:00]</a>.

Overall, [[automated_business_with_ai_assistants | automated business with AI assistants]] can transform operations by efficiently collecting data, identifying opportunities, and streamlining communication processes.