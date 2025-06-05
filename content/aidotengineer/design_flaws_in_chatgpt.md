---
title: Design flaws in ChatGPT
videoId: y6L5RkEqQ8g
---

From: [[aidotengineer]] <br/> 

Despite ChatGPT being one of the fastest-growing applications in history, with hundreds of millions of daily users, questions arise regarding its confusing design [00:00:00].

## Current Design Challenges

A key issue in ChatGPT's current interface is the separation of voice and text interactions. For example, when interacting via voice, there are two distinct buttons for voice-to-text and voice-to-voice communication [00:00:20]. While it can respond verbally to requests, such as drafting an email, it only responds through voice [00:01:01]. If a user wishes to collaborate on the written email, the only option is to end the call and then review a voice transcript, with the final formatted text appearing at the end [00:01:07]. This design highlights a lack of multimodal functionality where text and voice could be used together [00:01:14].

This separation makes it feel as though the voice and text features were developed by "two different companies" [00:01:18]. This phenomenon, where an organization's internal structure is reflected in its product design, is termed "shipping the org chart" by Scott Hansselman [00:01:22]. An analogy used to explain this is observing an electric vehicle's dashboard where maps, climate controls, and speedometer are all on different screens with inconsistent fonts, revealing the distinct teams that built them [00:01:26]. OpenAI is similarly "guilty of this" [00:01:47], often releasing technical improvements that consumers desire without sufficient marketing consultation, leading to a "science fair full of potential options" [00:01:59].

## Proposed Solutions for Improved User Experience

To address these design flaws, two primary changes are suggested for ChatGPT:
1.  Allowing simultaneous voice and text interaction [00:02:11].
2.  Intelligently selecting the appropriate model based on the user's request [00:02:16].

These improvements can be implemented using "off-the-shelf tools" [00:02:20]. For instance, "40 Realtime" can provide live audio chat [00:02:23], while "tool calls" can manage other functionalities [00:02:26]. This enables the AI to send text for longer details like links and drafts [00:02:29]. A research tool could also hand off complex queries to a smarter model, then return a detailed answer [00:02:34].

### Multimodal Interaction in Practice

A conceptual re-design of ChatGPT would involve a voice button that transitions to a voice mode, featuring mute, end call, and a new "chat" button [00:02:40]. This "chat" button would reveal a panel resembling iMessage [00:02:51], allowing users to text while on a voice call, much like "texting your friend while you're on a FaceTime call" [00:02:56]. This panel would display call controls at the top, a reminder of the initial query, and a text response for detailed needs like email drafts [00:02:59]. This approach aims to provide a seamless [[improving_chatgpts_voice_and_text_features | asynchronous experience]] within the chatbot.

### Smart Model Selection for Complexity

For questions requiring more detail, a system could leverage a reasoning model. As demonstrated by Warp Terminal, a developer tool for writing code, simple requests (e.g., "undo my last commit") can be handled by a coding agent [00:03:19]. More complex requests (e.g., "refactor this entire codebase to use Flutter") would be detected as intricate, prompting the system to write a plan using a reasoning model to ensure the code functions correctly [00:03:30]. This pattern is effective with heuristics; for example, if a user asks for details, pros, and cons, the system could hand off to a reasoning model, indicate its thinking time, and then return a more detailed response [00:03:44].

### Technical Implementation

Implementing these features involves using readily available APIs [00:03:57]. For multimodal interactions, a "send chat message tool" can be utilized to convey details that are more easily explained via text [00:04:37]. This tool, requiring only a simple description rather than a complex system prompt, smartly sends the appropriate information via text [00:04:46]. For deeper dives into a topic, a "reasoning models" tool can be employed [00:04:57]. When a user wants to explore a subject further, this tool can send details to a specialized model, which then responds back or directly outputs to the client application [00:05:01]. The source code for this "fix gpt" concept is available on GitHub [00:05:13].