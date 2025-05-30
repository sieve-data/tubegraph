---
title: Future Work and Feature Requests for AI Tools
videoId: p1YvKuRfEhg
---

From: [[colemedin]] <br/> 

This article outlines the future development goals and community-requested features for a community-driven fork of the `bolt.new` AI code generator. The project aims to continuously improve and expand upon the capabilities of the original tool, driven by community feedback and contributions <a class="yt-timestamp" data-t="00:46:58">[00:46:58]</a>. The project serves as a way to learn how to leverage AI to build things <a class="yt-timestamp" data-t="01:47:56">[01:47:56]</a>.

## Project Overview and Community Involvement

A fork of `bolt.new`, one of the most popular AI code generators, was created to enable users to choose their own Large Language Model (LLM) for code generation, including local LLMs via tools like Ollama, allowing for free and unlimited code generation <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The initial video about this fork received significant engagement, with many users providing suggestions, feedback, and even code contributions <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>. This has led to the formation of a community around the project, transforming it from a personal fork into a collaborative endeavor <a class="yt-timestamp" data-t="01:10:48">[01:10:48]</a>.

While the fork is not yet perfect, the community sees this as an opportunity to work together to improve it, drawing inspiration from other tools to create something truly exceptional <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>.

### Recently Implemented Features

Several key features have already been implemented based on community requests:
*   **OpenRouter Integration**: This allows users to access a wide range of models available on the OpenRouter platform <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>.
*   **Gemini Integration**: Support for Gemini 1.5 Flash and Pro models has been added <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.
*   **Dynamic Ollama Model List**: The list of available Ollama models dynamically updates to show only those downloaded locally by the user, preventing confusion and ensuring functionality <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>.
*   **Provider-based Model Filtering**: Users can now filter models by their provider (e.g., OpenAI, Ollama, OpenRouter, Google), simplifying model selection <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>.
*   **Download Code as Zip File**: A highly requested feature, users can now download all generated code files as a single zip archive, eliminating the need for manual copy-pasting <a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a>.

## Future Work and Requested Additions

The following is a comprehensive list of requested additions and planned future work for the `bolt.new` fork, compiled from community feedback <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>:

### New LLM Integrations

*   **LM Studio Integration**: Many users have requested integration with LM Studio as an alternative for managing local models, similar to Ollama <a class="yt-timestamp" data-t="11:33:00">[11:33:00]</a>.
*   **DeepSeek API Integration**: Integration with the DeepSeek API is desired, particularly to leverage the powerful DeepSeek Coder models <a class="yt-timestamp" data-t="11:43:00">[11:43:00]</a>.

### Prompting and Model Performance Improvements

*   **Improve Prompting for Smaller Models**: There's an opportunity to optimize the `bolt.new` prompting to work more effectively with smaller LLMs, which sometimes struggle to generate the expected web container and code output <a class="yt-timestamp" data-t="12:03:00">[12:03:00]</a>. A temporary workaround exists where re-prompting after opening the code container can help <a class="yt-timestamp" data-t="12:35:00">[12:35:00]</a>.
*   **General `bolt.new` Prompt Improvements**: Enhancements to the main `bolt.new` prompt are needed to achieve better overall code generation results, especially concerning UI/UX design and state management, as the paid version sometimes produces better visual UIs <a class="yt-timestamp" data-t="14:50:00">[14:50:00]</a>. The main prompt file is accessible in the source control <a class="yt-timestamp" data-t="15:27:00">[15:27:00]</a>.

### Advanced Features and Functionality

*   **Attach Images to Prompts**: The ability to attach images to prompts, a feature present in the paid version of `bolt.new` but not the open-source one, is a requested addition <a class="yt-timestamp" data-t="13:11:00">[13:11:00]</a>.
*   **[[incorporating_ai_agents_and_advanced_development_features | Run Agents in the Backend]]**: This is a major requested feature, aiming to implement an agentic workflow where multiple LLMs can work together to generate code in a more robust way than a single model <a class="yt-timestamp" data-t="13:33:00">[13:33:00]</a>. This could utilize tools like LangGraph, LangChain, or OpenAI Swarm <a class="yt-timestamp" data-t="14:03:00">[14:03:00]</a>.
*   **Publish Projects Directly to GitHub**: Similar to the paid version of `bolt.new`, users desire the ability to publish their generated projects directly to GitHub <a class="yt-timestamp" data-t="14:27:00">[14:27:00]</a>.
*   **Load Local Projects into the App**: The functionality to import existing local projects (e.g., from VS Code) into the `bolt.new` environment would allow for continued AI assistance on ongoing projects rather than starting from scratch <a class="yt-timestamp" data-t="14:34:00">[14:34:00]</a>.

## Call for Contributions

The project heavily relies on community contributions to implement these requested features <a class="yt-timestamp" data-t="11:14:00">[11:14:00]</a>. By working together, the aim is to build a truly amazing `bolt.new` fork that continually incorporates new features and learns from other tools <a class="yt-timestamp" data-t="11:18:00">[11:18:00]</a>. This collaborative effort makes the project "our Fork" rather than just "my Fork" <a class="yt-timestamp" data-t="14:48:00">[14:48:00]</a>.