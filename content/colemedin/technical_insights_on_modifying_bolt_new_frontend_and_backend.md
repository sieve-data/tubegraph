---
title: Technical insights on modifying Bolt new frontend and backend
videoId: 3PFcAu_oU80
---

From: [[colemedin]] <br/> 

This article provides a technical overview of how the open-source web development platform Bolt.new was forked and modified to address its limitations, specifically its restricted usage and fixed Large Language Model (LLM) selection <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. The modifications allow users to run [[advantages_of_running_bolt_new_locally | Bolt.new]] locally, choose from a variety of LLMs, and gain unlimited usage <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a> <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

## Overview of Bolt.new and its Limitations

[[introduction_to_ottodev_and_the_boltnew_fork | Bolt.new]] is a powerful, open-source LLM web development platform that enables users to create and deploy full-stack applications directly in the browser with AI assistance <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. While it significantly speeds up full-stack development and acts as a fantastic coding assistant, it has two primary issues <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a> <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>:
*   **Limited Usage:** Similar to services like Claude or Vercel, usage is capped, which can interrupt coding sessions <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **Fixed LLM:** [[integrating_various_models_with_bolt_new | Bolt.new]] is hardcoded to use Claude 3.5 Sonnet, preventing users from leveraging other LLMs like GPT or local, fine-tuned coding models <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

By forking [[integrating_various_models_with_bolt_new | Bolt.new]] and running it locally, these problems were resolved, allowing for platform extension beyond a single LLM <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a> <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

## Setting Up the Forked Version

To run the modified [[integrating_various_models_with_bolt_new | Bolt.new]] version:
1.  **Clone the Repository:** Download the forked repository from the provided link <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a> <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
2.  **Install Packages:** Install all necessary packages <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
3.  **Set Environment Variables:** Configure API keys in the `.env.example` file for specific models (e.g., GPT, Groq). API keys are not required for local models like [[integrating_various_models_with_bolt_new | OlaMA]] <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
4.  **Run Development Command:** Execute `pnpm run dev` to start [[integrating_various_models_with_bolt_new | Bolt.new]] with all LLMs on your machine <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
5.  **Browser Requirement:** Use Google Chrome Canary browser to run the application <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

## Frontend Modifications

The frontend structure adheres to standard front-end application development (e.g., Next.js, React) <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

### `constants` File (`utils` folder)
*   **Default Model and Providers:** Defines the default model (Claude 3.5 Sonnet) and default provider (Anthropic), consistent with the original [[integrating_various_models_with_bolt_new | Bolt.new]] <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   **Model List:** A comprehensive list of available models, each defined as an object with `name` (model ID), `label` (display name), and `provider` <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.
*   **Adding New Models:** New models can be easily added by copying an existing record and specifying the new model ID, label, and provider <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. For [[integrating_various_models_with_bolt_new | OlaMA]] models, users need to install [[integrating_various_models_with_bolt_new | OlaMA]] and pull the desired models <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.

### UI Components
*   **Main Chat Component:** A new state was introduced to represent the selected LLM, which updates based on the dropdown selection <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.
*   **Passing Model to Backend:** Due to the `useChat` Hook from the Vercel AI SDK, directly adding a parameter for the model was not straightforward <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>. Instead, the model ID is embedded within the content of the user's message, extracted by the API, and then removed before being passed to the LLM and displayed <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>. This approach mirrors [[integrating_various_models_with_bolt_new | Bolt.new]]'s method for passing file modifications <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.
*   **Base Track Component:** This component iterates over the model list to construct the dropdown menu displaying all LLM options <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.
*   **User Message Component:** Utilizes regular expressions to remove the model ID from user messages displayed in the frontend, preventing confusion for the LLM <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.

## Backend Modifications

The core logic for interacting with LLMs resides in the backend.

### API Endpoint and `streamText.TS`
*   **API Entry Point:** The API endpoint serves as the primary entry point to the backend, calling the `streamText` function to process requests and obtain responses from the LLM <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.
*   **`streamText` Function:** Within this function, messages are looped over to extract the latest specified model from the user's input (enabling model changes mid-conversation) <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>. Messages are also sanitized to ensure the model ID is not included in the prompt sent to the LLM <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.

### Model and API Key Retrieval
*   **`getModel` Function:** This function retrieves the appropriate model instance based on the provider and model ID <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.
*   **`API key typescript file` (`getAPIKey`):** A simple switch statement retrieves the correct API key based on the provider (e.g., Anthropic, OpenAI, Groq). For local models like [[integrating_various_models_with_bolt_new | OlaMA]], an empty string is returned as no API key is required <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.
*   **Model Instance Functions:** Separate functions are used to obtain model instances for each provider, all leveraging the Vercel AI SDK <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>.

### Extending to New Providers
*   **Vercel AI SDK Support:** The platform can be extended to support new LLM providers (e.g., Together AI, Fireworks) if they are available as packages within the Vercel AI SDK <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>.
*   **Implementation Steps:** Adding a new provider involves:
    1.  Adding a new function for the provider.
    2.  Adding a new API key in the environment variable file.
    3.  Updating the switch statements in `getAPIKey` and the model instance retrieval functions <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.

While adding new models for existing providers is straightforward, integrating entirely new providers requires more technical changes <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>. This comprehensive modification allows for greater flexibility and control over the LLMs used within [[integrating_various_models_with_bolt_new | Bolt.new]].