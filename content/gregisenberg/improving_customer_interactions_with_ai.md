---
title: Improving customer interactions with AI
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

Voice AIs are capable of automating tasks typically done over the phone, with the potential for widespread adoption within the next one to three years <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. This technology offers a flexible way to build voice agents that can significantly [[improving_manual_processes_with_ai | improve manual processes]] and customer interactions.

## Case Study: "Lowballer 9000" Voice AI

Tony, an automation expert, developed a voice AI named "Lowballer 9000" (also known as Alex) to negotiate prices for Rolex Daytonas with secondhand luxury watch dealers across the US <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. This AI's primary job was to find a Rolex Daytona, gather critical details like the watch's condition and original documentation, and then attempt to lowball the dealers <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>. The experiment demonstrated the practical capabilities of voice AI in real-world scenarios <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>.

### Technical Implementation with Vappy

The core platform used for building the voice AI was Vappy, which functions as a flexible voice API <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>. Vappy allows users to bring their own prompts and select various service providers without proprietary lock-ins <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.

### Prompt Engineering and Best Practices

Developing effective prompts for voice AIs involves an iterative process of testing and refinement <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>. Key lessons from the "Lowballer 9000" project include:

*   **Conciseness:** Keep AI responses brief, ideally one to two sentences max, to prevent overwhelming the interlocutor and maintain engagement <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>. This also reduces the chance of the AI making errors <a class="yt-timestamp" data-t="05:05:00">[05:05:00]</a>.
*   **Simplicity of Language:** Aim for a "sixth-grade English level" in the AI's language. This has been shown to result in longer call durations and more human-sounding interactions <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>.

> [!tip] AI Creativity (Temperature)
> The "temperature" setting in AI models controls the creativity of responses <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>. A temperature closer to zero makes the system more deterministic and predictable <a class="yt-timestamp" data-t="08:35:00">[08:35:00]</a>. However, a very low temperature might cause the AI to fail in responding to uncommon questions <a class="yt-timestamp" data-t="08:41:00">[08:41:00]</a>.

### Model and Voice Selection

The choice of AI model (e.g., Gemini 20 Flash, DeepSeek) is crucial and often depends on current performance and availability <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>. Market hype cycles can impact model stability and cost, potentially leading to call crashes if the API becomes overloaded <a class="yt-timestamp" data-t="06:18:00">[06:18:00]</a>.

Voice configuration allows selecting specific voices. For "Lowballer 9000," "Cartisia" (dubbed "New York man") was chosen to give the AI a distinct persona <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>.

### Integrating with Existing Tools (Tool Calling)

The true power of a voice AI comes from its ability to interact with existing tools through "tool calls" <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>. For the watch negotiation AI, this meant recording and analyzing calls to track outcomes efficiently. A tool call was set up to process transcripts after each conversation, determining if an offer was received, the lowball amount, and whether it was accepted <a class="yt-timestamp" data-t="10:58:00">[10:58:00]</a>. This data was then compiled into a spreadsheet, allowing easy sifting through hundreds of calls to find actionable information <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>.

> [!info] Data as an Unfair Advantage
> Building AI voice agents is an excellent way to acquire specific data that can provide an "unfair advantage" in various businesses <a class="yt-timestamp" data-t="17:36:00">[17:36:00]</a>. If knowledge or data provides a competitive edge, there is likely a voice AI opportunity <a class="yt-timestamp" data-t="18:21:00">[18:21:00]</a>.

### Regulatory Considerations

A significant hurdle in implementing voice AI for outbound calls is adhering to regulations like Shake and Stir, an FCC rule <a class="yt-timestamp" data-t="15:07:00">[15:07:00]</a>. This requires registering phone numbers and completing KYC (Know Your Customer) processes to ensure calls are honored and not sent straight to voicemail <a class="yt-timestamp" data-t="15:20:00">[15:20:00]</a>.

## Broader Applications of Voice AI in Business

The capabilities demonstrated by "Lowballer 9000" extend to numerous other business functions, showcasing the [[potential_applications_of_ai_in_business_automation | potential applications of AI in business automation]].

*   **Sales and Prospecting:** Voice AIs can automate outbound calls for sales, such as in real estate, by asking targeted questions to qualify leads (e.g., assessing the likelihood of a house coming onto the market) <a class="yt-timestamp" data-t="16:16:00">[16:16:00]</a>.
*   **Data Arbitrage:** By gathering specific data points (like low offers on watches), businesses can identify arbitrage opportunities, buying low and selling high at scale <a class="yt-timestamp" data-t="17:45:00">[17:45:00]</a>.
*   **Automated Feedback Collection:** Voice AIs can collect unstructured feedback from customers. An example given is a bot that listens to "brain dumps" from community members (both positive and negative feedback), categorizes it, and posts summaries to a Slack channel for product improvement <a class="yt-timestamp" data-t="20:27:00">[20:27:00]</a>. This is an excellent example of [[future_of_ai_in_customer_support_and_service_industries | implementing AI assistants in different business functions]].

## Combining AI Tools: Vappy & Lindy

Integrating voice AI platforms like Vappy with other tools, such as Lindy, further enhances their utility <a class="yt-timestamp" data-t="12:26:00">[12:26:00]</a>. Lindy excels at flexibly taking large amounts of text (e.g., from a website scrape or a voice AI transcript) and structuring it into spreadsheets <a class="yt-timestamp" data-t="12:47:00">[12:47:00]</a>. For instance, Lindy can automatically populate or update columns in a spreadsheet based on content, like checking if a restaurant is "vegan friendly" without needing manual rule creation or re-configuration <a class="yt-timestamp" data-t="13:52:00">[13:52:00]</a>. This combination is particularly powerful for [[implementing_ai_assistants_in_different_business_functions | improving data collection]] and analysis from customer interactions.