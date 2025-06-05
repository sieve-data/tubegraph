---
title: Integrating OpenAI API with voice agents
videoId: pzmbleiOfCM
---

From: [[aidotengineer]] <br/> 

Building robust AI voice agents presents significant [[challenges_in_building_ai_voice_agents | challenges]], extending beyond those typically encountered with large language models (LLMs) [00:00:08]. While LLMs themselves are difficult to "wrangle" due to issues like hallucination and evaluation complexities, voice agents amplify these problems [00:00:17].

Key difficulties with LLMs generally include:
*   **Hallucination**: LLMs can generate incorrect or nonsensical information [00:00:21].
*   **Evaluation**: It's challenging to develop metrics to assess system performance, especially for conversational AI where objective measures are scarce [00:00:23].
*   **Latency**: This is a critical concern for conversational user interfaces that aim for fluid, human-like interaction [00:00:37].

When dealing with audio and voice agents, these issues become even more pronounced. Additional complications arise from transcription, which is not always straightforward, and the need to operate in a streaming environment rather than a batched text interaction [00:00:51]. These factors collectively make development very difficult [00:01:10].

## Case Study: Automating Consulting-Style Interviews

To illustrate these challenges in practice, Fractional AI developed an application to automate consulting-style interviews [00:01:15]. This involves interviewing employees within large companies to gather information, a process typically performed by human consultants [00:01:31].

Traditionally, this qualitative research is:
*   **Expensive**: Sending consultants to interview employees is costly [00:01:56].
*   **Inefficient**: It requires significant time for consultants and complex scheduling [00:02:05].
*   **Human-centric**: It demands a "human touch" for improvisation, trust-building, and dynamic follow-up questions [00:02:24]. People also tend to provide more detailed, rambling answers in conversation than when typing responses to forms [00:02:44].

The goal was to build an [[building_effective_ai_agents | AI interview agent]] that could:
*   Conduct interviews like a human [00:02:53].
*   Feel conversational, not like a form [00:02:59].
*   Interview hundreds of people simultaneously, overcoming scheduling and cost barriers [00:03:03].
*   Provide automatic transcription for data extraction and aggregation [00:03:12].

<iframe width="560" height="315" src="https://www.youtube.com/embed/P-Y3o96m3bM?start=2m27s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
The demonstration showcased an AI agent conducting a basic interview, responding naturally and adapting to user input [00:03:23].

## Initial Approach and Its Limitations

The initial development leveraged the OpenAI real-time API, using a monolithic prompt that detailed the interview objectives, questions, and navigation instructions [00:04:51].

However, this "monolithic prompt" approach quickly proved unsuitable for desired functionality, such as displaying a "roadmap" of questions on screen, indicating the current question, and allowing users to jump between questions [00:05:20]. The LLM had no inherent way to know which question it was currently asking or to be easily coaxed into switching questions upon user interaction [00:05:41].

## Refining the Approach: Tool Use and Modular Prompts

To address these limitations, a more modular approach was adopted:
1.  **One Question at a Time**: Only the current question was sent to the LLM within the prompt [00:05:53].
2.  **[[integration_of_thirdparty_tools_with_ai_web_agents | Tool Use]]**: The LLM was given access to a tool that allowed it to indicate it wanted to move to the next question [00:06:00]. This enabled deterministic feeding of the next question [00:06:07].
3.  **Injected Prompts**: Additional prompts were injected into the stream to inform the LLM when a user clicked around the roadmap, allowing the agent to acknowledge user-initiated navigation (e.g., "Sure, let's move on to XYZ") [00:06:15].

## Addressing "Rabbit Holes" with a Drift Detector Agent

A significant challenge arose from the LLM's tendency to "chitchat," ask excessive follow-up questions, and generally go down "rabbit holes," reluctance to move to the next topic [00:07:01]. Forcing it too hard would eliminate its ability to improvise, which was undesired [00:07:25].

To mitigate this, a [[building_effective_ai_agents | background agent]] called the **Drift Detector** was introduced [00:07:32].
*   This is a separate, non-voice, text-based LLM operating in a side thread [00:07:35].
*   It listens to the conversation's transcript and assesses whether the discussion is "off-track" or "on-track" [00:07:44].
*   Its role is to determine if the current question has been answered and if it's time to move on [00:07:57].
*   When a strong signal to move on is received, it can force the main agent to use the "next question" tool, preventing further rabbit-holing [00:08:04].

## Enhancing Interview Flow: Goals, Priorities, and Next Question Agent

Further refinement was needed because the human-like interviews were difficult to tune, often following up too little or too much, and rephrasing questions in unhelpful ways [00:08:22]. The linear flow, where the agent could only dig in or move to the next question, also limited natural conversation [00:08:45].

Two key additions improved the flow:
1.  **Goals and Priorities**: Instead of just providing the question, the LLM was given the "why" behind each question as a first-class concept [00:09:04]. This included high and medium priority goals (e.g., "get a clear picture of this person's regular activities," "start to sus out where AI might be useful") to guide follow-up questions and rephrasing [00:09:16].
2.  **Next Question Agent**: Another [[building_effective_ai_agents | side agent]] was introduced, solely responsible for determining what should be asked next [00:09:25]. This bot, running on the transcript in the background, is trained on what makes a good interviewer and can guide the main conversation back on track [00:10:29].

## Transcription Challenges and UX Solutions

The background agents, and the user interface itself, rely on accurate transcripts [00:10:54]. While OpenAI's API makes transcription easy by providing what the user said [00:11:05], the underlying Whisper model (used for transcription) has limitations [00:11:26].

*   **Whisper vs. Core Model**: The core LLM is "fully integrated" and understands sounds (like claps or coughs), but Whisper merely converts audio to text [00:11:30].
*   **Transcription Errors**: Whisper can produce nonsensical text for silence or background noise, even when the conversation history suggests otherwise [00:11:51]. This leads to a poor user experience [00:12:20].
*   **Lack of Control**: The OpenAI real-time API doesn't offer knobs to tune Whisper's behavior at a low level [00:12:25].

To address this at the UX level, a separate [[building_effective_ai_agents | agent]] was added [00:12:38]. This agent's sole task is to decide whether to hide a piece of the transcript from the user if it suspects a transcription error [00:12:47]. The full transcript is still captured, but the user doesn't see embarrassing errors [00:12:54]. Crucially, the core model still processes the original input, allowing it to respond appropriately (e.g., "I didn't really get that") [00:13:06].

## The Importance of [[evaluation_techniques_for_multimodal_and_voice_ai_agents | Evaluation]]

The iterative process of adding multiple agents and prompts to fix issues leads to significant complexity [00:13:27]. This "vibes-driven" development, while useful initially, becomes unsustainable [00:13:43]. It's difficult to know which prompt or agent to update, and fixes can inadvertently introduce regressions [00:13:54].

To overcome this, **[[evaluation_techniques_for_multimodal_and_voice_ai_agents | evaluation]] (evals)** are critical [00:14:20]. A systematic way to measure performance is needed, using a set of metrics to assess attributes like clarity, completeness, and professionalism [00:14:29]. These metrics are often measured by an LLM acting as a judge based on the conversation [00:14:36].

While perfect objective ground truth is often unavailable for conversational AI, evals provide a more objective way to iterate beyond pure intuition [00:15:01].

### Synthetic Conversations for Evaluation

To further automate and scale [[evaluation_techniques_for_multimodal_and_voice_ai_agents | evaluation]], **synthetic conversations** were introduced [00:15:15].
*   LLMs are used to simulate various "fake users" (personas) who act as interviewees [00:16:17].
*   Personas are created with specific characteristics (e.g., "snarky teenager," different job functions, personalities) [00:16:41].
*   The AI agent then interviews these personas, and the same [[evaluation_techniques_for_multimodal_and_voice_ai_agents | eval]] suite is run over the synthetic conversations [00:17:01].
*   This allows for measuring average metrics across a broad population of expected users, automating testing, and providing insights into how the system performs with different types of interactions [00:17:13].

## Conclusion

Building robust voice applications with the OpenAI API requires more than just basic API calls and prompt engineering [00:17:31]. While a good starting point, a truly robust application necessitates:
*   **[[building_effective_ai_agents | Out-of-band checks]]**: Employing separate agents, often operating in the text domain, to make decisions and guide the main agent [00:17:54].
*   **[[integration_of_thirdparty_tools_with_ai_web_agents | Tool Use]]**: Utilizing tools to constrain LLM behavior and instrument it, providing insights into its actions [00:18:10].
*   **[[evaluation_techniques_for_multimodal_and_voice_ai_agents | Evals]]**: Crucially, implementing comprehensive evaluation methods, even with no objective ground truth, to measure success and guide the development process [00:18:28].