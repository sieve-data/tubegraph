---
title: Daily Bots and their functionality
videoId: 2ukMoQRsL6w
---

From: [[gregisenberg]] <br/> 

Daily Bots are voice character applications that are transforming the landscape of digital interaction by enabling sophisticated, responsive, and personalized [[ai_agents_and_automation | AI agents]] [00:00:00]. Described as an "audio [[introduction_to_chatgpt_codex | ChatGPT]]" [00:00:53], these bots are becoming a significant new form of content and applications, with some even "printing money" [00:00:04]. The core idea is that "characters are the new apps" [00:00:13], offering a vast opportunity for both technical and non-technical users to innovate [00:00:08].

## How Daily Bots Work

The underlying system of Daily Bots orchestrates a complex process to enable real-time voice interactions:
1.  **Speech-to-Text (STT)**: The system takes audio input from a microphone and converts it into text using a Speech-to-Text provider [00:10:39].
2.  **Large Language Model (LLM) Processing**: This text is then fed into an [[ai_tools_and_productivity_enhancement | AI model]] (LLM), such as Llama 3.1 70B, which processes the input and generates a text response [00:10:50]. Daily handles the LLM calls on its backend [00:04:25].
3.  **Text-to-Speech (TTS)**: The LLM's text response is then piped into a Text-to-Speech provider to convert it back into audio [00:11:00].
4.  **Audio Output**: Finally, this audio is streamed to the user's browser or device [00:11:09].

This entire process, including handling performance, errors, and complexity, is managed by the Daily system, allowing developers to focus on the bot's personality and functionality [00:11:14].

## Getting Started: Setting Up a Daily Bot

Building a Daily Bot involves several key tools and steps, even for those without extensive coding knowledge:

### Essential Tools
*   **Daily**: The main service provider for building and hosting voice bots [00:03:43].
*   **[[differences_between_bolt_and_cursor_ai | Cursor]]**: A code editor integrated with LLMs to assist with coding [00:03:25].
*   **Next.js**: A React framework used for building the web application and server routes [00:20:21].
*   **Vercel**: A platform for deploying Next.js applications online [00:29:21].

### Setup Process
1.  **Obtain Daily API Key**: Sign up for Daily and acquire an API key from their dashboard [00:04:31].
2.  **Clone the Demo Repository**: Download Daily's demo repository to your local system [00:04:47]. This provides a pre-set foundation, making it easier to build incrementally [00:28:03].
3.  **Configure API Key**: Insert the Daily API key into the `.env.local` file within the cloned repository [00:05:13].
4.  **Start the Server**: Run the command `yarn dev` to start the local server [00:05:49].
5.  **Access Locally**: Navigate to the local host URL in your browser to interact with the demo bot [00:05:56].

### Deployment
To make the bot accessible online:
1.  **Use Vercel CLI**: Vercel provides a command-line interface (CLI) tool for deployment [00:30:08].
2.  **Deploy Command**: After logging in, a simple command like `vercel` will deploy your Next.js application live on the internet [00:30:35]. The deployment process typically takes about 1.5 minutes [00:31:21].

## Configuration and Personalization

Daily Bots are highly customizable, allowing users to define their bot's character and capabilities:

*   **Personality Prompts**: The bot's behavior is dictated by configuration files that include specific prompts [00:08:40]. For example, the default prompt might be: "You are an assistant called Example Poot. You can ask me anything," followed by instructions on how to speak for correct audio output [00:10:17].
*   **Voice Customization**: Users can easily change the bot's voice [00:09:03].
*   **Character Definition**: New characters can be added by simply editing the configuration file, which directly reflects on the character selection screen [00:12:26]. This direct link between file editing and character appearance highlights the ease of customization [00:12:55].

## [[function_calling_tools | Function Calling]]

A critical feature that extends a Daily Bot's capabilities beyond simple conversation is [[function_calling_tools | function calling]]:

### What is [[function_calling_tools | Function Calling]]?
LLMs inherently only take in text and output text [00:16:07]. [[function_calling_tools | Function calling]] is the mechanism that allows an [[ai_agents_and_automation | AI]] system to "do stuff" [00:09:21] outside of just generating text. It works by providing the LLM with detailed instructions about available external functions. When the LLM determines a function is needed based on the user's prompt, it outputs a specific text format indicating which function to call and with what parameters [00:16:35]. The external system then intercepts this formatted text, executes the corresponding function (e.g., calling an API to get data, making an Instagram post), and provides the result back to the LLM [00:16:55].

### Implementing the Weatherman Example
As a practical demonstration, a weatherman bot was created. This bot can tell you the weather by:
1.  **Defining the Tool**: A "weather tool" is defined in the configuration, including its name (`get_weather`) and parameters (e.g., `location`) [00:17:42].
2.  **LLM Understanding**: The AI model is instructed on the format it needs to use when calling this function [00:18:51].
3.  **Server-Side Execution**: When the AI outputs a call to `get_weather`, the system (a Next.js API route) executes the corresponding code [00:19:27]. In the demo, this route was configured to return humorous, "nonsense" weather conditions like "whimsical singing rainbows" or "flying pigs" [00:21:13]. This intentionally silly output serves as clear validation that the [[function_calling_tools | function calling]] mechanism is working correctly [00:22:25].
4.  **Interaction**: When asked, "Can you give me the weather for New York City?" [00:25:58], the bot successfully called the function and reported "whimsical singing rainbows" for the Big Apple [00:26:09].

## "Characters are the New Apps"

The concept that "characters are the new apps" [00:13:04] signifies a huge market opportunity, especially with the rise of [[ai_agents_and_automation | AI agents]] and their applications. Retention graphs for AI character chat apps indicate they are "not going away" [00:14:05], suggesting a future where highly engaging consumer (and B2B) apps will involve creating characters that perform specific actions and interact in unique ways [00:14:14]. Designing these characters with unique elements, like the "singing rainbows" weather report, can even lead to viral moments and free distribution [00:23:01].

## Advanced Applications: The Vtuber App

Beyond simple chatbots, Daily's tools enable more complex [[multimodal_live_api_and_realtime_ai_interaction | multimodal live API and real-time AI interaction]]. An example is an app that allows users to have a FaceTime-like call with an [[ai_agents_and_automation | AI]]-powered vtuber (a virtual YouTuber) [00:32:42]. Vtubers are content creators who use software to embody virtual avatars, often anime characters [00:32:52]. This app leverages voice APIs (like Daily's Pip Cat library for more developer control [00:34:46]) to create a personal, interactive experience with a virtual character [00:34:05].

## Development Philosophy

When building with these powerful [[ai_tools_and_productivity_enhancement | AI tools]], it's beneficial to:
*   **Make Small, Understandable Changes**: Especially when starting out, focus on incremental modifications rather than trying to "one-shot" an entire application [00:27:28].
*   **Build Off Existing Projects**: Starting with a pre-existing demo or repository, like Daily's, provides a solid foundation and helps in understanding how files connect [00:28:03].
*   **Read Documentation and Ask [[introduction_to_chatgpt_codex | AI]]**: Developing the habit of reading documentation is crucial [00:15:32], but also leveraging [[introduction_to_chatgpt_codex | ChatGPT]] or Claude to understand complex concepts is highly effective in the age of [[ai_agents_and_automation | AI]] [00:15:42].