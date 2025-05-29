---
title: Challenges in integrating LLMs with external services
videoId: 7j_NE6Pjv-E
---

From: [[gregisenberg]] <br/> 

Large Language Models (LLMs) have evolved significantly, but integrating them with external services presents several complex challenges. While LLMs are powerful for text prediction and generation, they are inherently limited in performing "meaningful" actions on their own <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

## Inherent Limitations of LLMs Alone

Without external connections, an LLM cannot perform tasks such as sending an email <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a> or searching the internet <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. Their primary function is to predict the next word in a sequence, like completing "My Big Fat Greek" with "wedding" <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. Fundamentally, LLMs are described as "very, very dumb" without external capabilities <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

## The Evolution: LLMs Combined with Tools

To overcome these limitations, developers began combining LLMs with external tools, such as APIs <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. This allows LLMs to access external services, like searching the internet (as seen with Perplexity) <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a> or integrating with automation services like Zapier or n8n <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. This step made LLMs "a bit more powerful" <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

## Significant Integration Challenges

Despite the advancements, integrating multiple tools with LLMs is fraught with difficulties, making it cumbersome and frustrating <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. This is a primary reason why an "Iron Man level Jarvis assistant" is not yet widely available <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

Key challenges include:

*   **Lack of Unified Standards:** While REST APIs exist as a standard, individual service providers construct their APIs differently. Each tool essentially speaks its "own language" (e.g., English, Spanish, Japanese), requiring developers to understand and translate different information and setup procedures <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   **Manual and Cumbersome Integration:** Connecting and stacking multiple tools requires significant manual work, step-by-step planning <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>. It often feels like "gluing a bunch of different things together" <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. While this can work, it becomes "very difficult" at scale <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
*   **Cohesion and Reliability:** Making disparate tools work cohesively, quickly, and flawlessly with an LLM is a "nightmare" <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. It's challenging to ensure the LLM doesn't hallucinate or produce "stupid" outputs when connected to external services <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **Maintenance and Breaking Changes:** API updates from external services can break existing integrations. For instance, if a Slack or text service updates its API, the entire automation workflow might collapse, creating a "nightmare" for engineers <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. This complexity is why good engineers remain highly valued in the age of LLMs <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.

## The Role of MCPs

The proposed solution to these challenges is the introduction of MCPs (Multi-Tool Communication Protocols), which act as a unifying layer between LLMs and various services <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. This layer translates the "different languages" of various tools into a single, unified language that the LLM can understand <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

The architecture involves:
*   **MCP Client:** The LLM-facing side (e.g., Tempo, Windswept, Cursor) <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
*   **MCP Protocol:** The two-way communication standard <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
*   **MCP Server:** Responsible for translating an external service's capabilities to the client, typically built by the service provider themselves <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

The goal of MCPs is to make integrations "seamless" and "much easier" <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>, allowing LLMs to access a broader range of external resources more efficiently <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. However, setting up an MCP server can still be "annoying" with many local file operations involved <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>, indicating that the standard is still in its early stages <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.

## Future Outlook

While MCPs represent the "next evolution" in [[evolution_of_large_language_models_llms_with_tools | LLM development with tools]] <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>, the standard is still nascent and might be challenged or updated <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>. Monitoring the finalization of this standard is crucial for anyone looking to build new businesses or integrate [[integrations_with_existing_platforms_and_services | LLMs with existing platforms]] <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>.