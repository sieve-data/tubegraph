---
title: Updates and future goals for oTToDev AI coding assistant
videoId: _YzTntvUWN4
---

From: [[colemedin]] <br/> 

[[ottodev_open_source_ai_coding_assistant | oTToDev]] is an [[ai_coding_assistant_development | AI coding assistant]] that originated as a fork of Bolt.new approximately a month ago <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>. Its initial purpose was to enable chatting with various large language models (LLMs), including local ones via Ollama <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>. Since its inception, a significant community has rapidly formed around the project, propelling its development far beyond initial expectations <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>.

## Community Building

A key aspect of [[opensource_ai_coding_assistants_and_community_building | oTToDev]]'s development is its focus on community. The project aims to foster a strong, organized community to drive its future.

### Discourse Community Launch
The official Discourse community, named "Think Tank," has been launched and is accessible at thinktank.automator.ai <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>. This platform is designed to:
*   Keep the community organized <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>.
*   Serve as a central place for discussions, replacing YouTube comments and GitHub issues/pull requests for general chat <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>.
*   Provide a professional forum experience with features like official plugin support (e.g., [[improvements_to_ai_coding_assistants | AI integration]] for summarizing conversations) and robust organization/search functionality <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>.

To encourage engagement, a giveaway is being held: users who create an account and make a non-spam post on the Discourse community by Tuesday, November 12th, will be entered to win a $200 Amazon gift card <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>.

### Broader Platform: Automator
The Discourse community is part of a larger initiative called Automator.ai <a class="yt-timestamp" data-t="09:57:00">[09:57:00]</a>. This platform is an extension of the creator's YouTube channel, aiming to provide deeper, more production-ready [[effective_use_of_ai_coding_assistants | AI education]] and resources beyond the concise tutorials typically found on YouTube <a class="yt-timestamp" data-t="12:03:00">[12:03:00]</a>.

Automator seeks to provide:
*   **Enhanced Community & Networking**: A dedicated space for users to connect and discuss AI beyond specific video content <a class="yt-timestamp" data-t="12:50:00">[12:50:00]</a>.
*   **Production-Ready Content**: Advanced courses for building production-ready AI solutions <a class="yt-timestamp" data-t="13:46:00">[13:46:00]</a>.
*   **Specific Use Cases**: Resources for implementing generative AI to solve specific business problems <a class="yt-timestamp" data-t="14:33:00">[14:33:00]</a>.
*   **Latest Tools**: A place to stay updated on the newest [[ai_coding_assistant_development | AI tools]] and technologies like Cursor <a class="yt-timestamp" data-t="15:30:00">[15:30:00]</a>.
*   **Developer-Business Owner Connection**: Facilitating connections between developers and business owners seeking AI implementations <a class="yt-timestamp" data-t="16:24:00">[16:24:00]</a>.

The goal for Automator is to provide significant value for free while also offering paid opportunities for those who wish to invest further <a class="yt-timestamp" data-t="16:05:00">[16:05:00]</a>. A notable feature under development for Automator is the **[[open_source_ai_agent_development | AI Agent Studio]]**, a platform where users can test and learn to implement various [[open_source_ai_agent_development | AI agents]], including a hosted version of [[ottodev_open_source_ai_coding_assistant | oTToDev]] <a class="yt-timestamp" data-t="20:54:00">[20:54:00]</a>.

## [[new_features_in_ottodev | Updates to oTToDev]]

Recent progress on [[ottodev_open_source_ai_coding_assistant | oTToDev]] has been significant, driven by community contributions and new maintainers.

### Core Development
*   **New Maintainers**: A team of maintainers is being formed to help manage the growing demand and development efforts for [[ottodev_open_source_ai_coding_assistant | oTToDev]] <a class="yt-timestamp" data-t="26:00:00">[26:00:00]</a>.
*   **Containerization**: The application has been containerized using Docker, simplifying installation <a class="yt-timestamp" data-t="27:37:00">[27:37:00]</a>. Troubleshooting assistance is available through the Discourse community <a class="yt-timestamp" data-t="27:57:00">[27:57:00]</a>.

### Recent Feature Implementations
*   **UI for API Keys**: Users can now enter API keys directly within the user interface for providers like Anthropic, removing the need to edit .env files <a class="yt-timestamp" data-t="28:44:00">[28:44:00]</a>. This feature is crucial for future self-hosting capabilities and deployment on the [[open_source_ai_agent_development | AI Agent Studio]] <a class="yt-timestamp" data-t="29:17:00">[29:17:00]</a>.
*   **XAI Grok Beta Integration**: Grok is now integrated as a usable model within [[ottodev_open_source_ai_coding_assistant | oTToDev]] <a class="yt-timestamp" data-t="29:36:00">[29:36:00]</a>.
*   **Provider Choice Respect**: Fixed an issue where the application would sometimes default to an incorrect LLM provider <a class="yt-timestamp" data-t="30:18:00">[30:18:00]</a>.
*   **Ollama Context Setting**: Automatically sets the context length for Ollama models to prevent issues where code might not be properly rendered in the web container <a class="yt-timestamp" data-t="30:50:00">[30:50:00]</a>.

### Upcoming Features
*   **Bolt Terminal Integration**: A high-priority feature, this will add a visible terminal to the interface, allowing users to see commands being run as [[ottodev_open_source_ai_coding_assistant | oTToDev]] builds applications <a class="yt-timestamp" data-t="31:29:00">[31:29:00]</a>. This is expected to significantly reduce hallucinations, especially for local LLMs, by providing visibility into command execution and errors <a class="yt-timestamp" data-t="31:41:00">[31:41:00]</a>. This feature, present in the commercial Bolt version but not the open-source one, is a significant undertaking <a class="yt-timestamp" data-t="32:01:00">[32:01:00]</a>.

## Future Goals and Roadmap

[[ottodev_open_source_ai_coding_assistant | oTToDev]] has an ambitious roadmap, leveraging tools like Roadmap.sh to organize development efforts <a class="yt-timestamp" data-t="33:53:00">[33:53:00]</a>.

### Short-Term High-Priority Goals
*   **Local Project Loading/Interaction**: Enabling [[ottodev_open_source_ai_coding_assistant | oTToDev]] to load and interact with existing local projects, including pulling from Git or integrating with IDEs like VS Code <a class="yt-timestamp" data-t="35:17:00">[35:17:00]</a>. This is a critical and frequently requested feature <a class="yt-timestamp" data-t="35:35:00">[35:35:00]</a>.
*   **Backend Agent Integration**: Implementing the ability to run [[open_source_ai_agent_development | AI agents]] in the backend for improved code generation, potentially with multiple agents collaborating and checking each other's work <a class="yt-timestamp" data-t="48:50:00">[48:50:00]</a>.
*   **Improved Prompting for Smaller LLMs**: Developing optimized system prompts specific to different large language models to maximize their performance within [[ottodev_open_source_ai_coding_assistant | oTToDev]] <a class="yt-timestamp" data-t="59:32:00">[59:32:00]</a>.

### Long-Term Vision
*   **Extension Marketplace**: A long-term goal is to create an extension marketplace where developers can implement and upload extensions for [[ottodev_open_source_ai_coding_assistant | oTToDev]] without directly modifying its core codebase, offering optional functionalities like backend agents <a class="yt-timestamp" data-t="36:09:00">[36:09:00]</a>.
*   **Hosting [[ottodev_open_source_ai_coding_assistant | oTToDev]] as an [[open_source_ai_agent_development | AI Agent]]**: Making [[ottodev_open_source_ai_coding_assistant | oTToDev]] available on the planned [[open_source_ai_agent_development | AI Agent Studio]] as a self-hostable instance <a class="yt-timestamp" data-t="21:48:00">[21:48:00]</a>.

### Funding Development
The team is exploring crowdfunding options to incentivize developers for tackling more complex, time-intensive features <a class="yt-timestamp" data-t="45:08:00">[45:08:00]</a>. The idea of bounties for specific code implementations is also being considered <a class="yt-timestamp" data-t="46:00:00">[46:00:00]</a>.

## [[issues_with_current_ai_coding_assistants | Issues with current AI coding assistants]] and Technical Details

### Common Problems and Troubleshooting
*   **Installation Issues**: Some users have encountered problems running [[ottodev_open_source_ai_coding_assistant | oTToDev]] with Docker due to system differences <a class="yt-timestamp" data-t="27:49:00">[27:49:00]</a>. The Discourse community will be a resource for troubleshooting these issues <a class="yt-timestamp" data-t="27:57:00">[27:57:00]</a>.
*   **Preview Not Loading**: Often, this is due to LLM hallucinations rather than an application issue <a class="yt-timestamp" data-t="28:28:00">[28:28:00]</a>.
*   **"Message didn't complete its response" error**: This is a general backend error. More specific details can typically be found in the terminal where the website was started or in the browser's developer console (F12) <a class="yt-timestamp" data-t="49:21:00">[49:21:00]</a>.

### Running LLMs Locally
*   **Hardware Recommendations**: For running a 70 billion parameter model like Neotron 70B locally, substantial hardware is required, ideally at least two NVIDIA RTX 3090 GPUs (each with 24GB VRAM) <a class="yt-timestamp" data-t="52:41:00">[52:41:00]</a>. Smaller models, like a 30 billion parameter model (e.g., Codellama 34B), would still benefit from a 3090 <a class="yt-timestamp" data-t="52:48:00">[52:48:00]</a>.
*   **Quantization**: This technique involves adjusting the size of model weights to make LLMs run faster with minimal performance loss, allowing larger models to run on less powerful hardware or even mobile devices <a class="yt-timestamp" data-t="53:29:00">[53:29:00]</a>.
*   **Motherboard Considerations**: When building a PC for multiple GPUs, it's crucial to select a motherboard that supports identical PCI Lane speeds for both GPU slots (e.g., X8 X8 configuration) to ensure both GPUs receive optimal performance <a class="yt-timestamp" data-t="01:01:16">[01:01:16]</a>.
*   **Ollama Models**: Ollama models, by default, have a context length of 2,000 tokens, regardless of model size, which impacts performance within [[ottodev_open_source_ai_coding_assistant | oTToDev]] if not manually adjusted <a class="yt-timestamp" data-t="30:55:00">[30:55:00]</a>.

### Limitations of Current [[ai_coding_assistant_development | AI Coding Assistants]]
*   **Self-Improvement**: Currently, LLMs are not capable of complex self-improvement, such as independently developing and implementing new features, creating pull requests, and performing extensive testing, as this requires artificial general intelligence (AGI) <a class="yt-timestamp" data-t="00:59:02">[00:59:02]</a>.
*   **No Bash Terminal**: The lack of a Bash terminal within [[ottodev_open_source_ai_coding_assistant | oTToDev]] is a limitation inherited from its base, Bolt.new <a class="yt-timestamp" data-t="44:20:00">[44:20:00]</a>.

## Accessibility and Engagement
The developer is committed to keeping [[ottodev_open_source_ai_coding_assistant | oTToDev]] accessible and free, even considering covering API costs for certain models like DeepSeek Coder on the [[open_source_ai_agent_development | AI Agent Studio]] <a class="yt-timestamp" data-t="40:11:00">[40:11:00]</a>. The primary goal remains to teach users how to achieve incredible things with AI <a class="yt-timestamp" data-t="24:09:00">[24:09:00]</a>.

To get involved in [[opensource_ai_coding_assistant_development | oTToDev development]], users can sign up for the Discourse community to chat with other developers and contribute via pull requests on GitHub <a class="yt-timestamp" data-t="24:35:00">[24:35:00]</a>.